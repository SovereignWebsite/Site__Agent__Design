// Customer-site rules, checked live: 1.12 to 1.14 (menu, pages, link previews and the 1200x630 share card) and 2a (five designs). Read-only.
// Usage: node tools/site-checks.js https://owner.example.sovereignweb.site/ [more roots...]
const { chromium } = require('playwright');

const FAMILY_HOSTS = ['sovereignwebsite.ai', 'sovereignwebsite.org', 'sovereignwebsite.site', 'hub.sovereignweb.site', 'hub.sovereignwebsite.site',
  'agents.sovereignweb.site', 'vault.sovereignwebsite.site', 'agenticcells.ai', 'riskmandate.ai', 'newsroom.sgit.ai'];
const PAGES = ['start/', 'agents/', 'llms.txt', 'admin/'];
const OG = ['og:title', 'og:description', 'og:type', 'og:url', 'og:image', 'og:image:alt', 'og:image:width', 'og:image:height',
  'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image'];

(async () => {
  const browser = await chromium.launch();
  const report = [];
  for (const root of process.argv.slice(2)) {
    const base = root.endsWith('/') ? root : root + '/';
    const ctx = await browser.newContext({ viewport: { width: 1366, height: 900 }, bypassCSP: true });
    const page = await ctx.newPage();
    const r = { site: base, fails: [] };
    await page.goto(base, { waitUntil: 'networkidle' });

    // 1.13: the three pages answer 200 and are linked from the home page's header area and footer
    r.pages = {};
    for (const p of PAGES) {
      const res = await ctx.request.get(base + p);
      const links = await page.evaluate((p) => {
        const as = [...document.querySelectorAll('a[href]')].filter(a => new URL(a.href, location.href).pathname.replace(/^\//, '') === p);
        return { header: as.some(a => a.closest('header') || a.getBoundingClientRect().top < 900), footer: as.some(a => a.closest('footer')) };
      }, p);
      r.pages[p] = { status: res.status(), ...links };
      if (res.status() !== 200) r.fails.push(`1.13 ${p} answers ${res.status()}`);
      else if (p !== 'llms.txt' && !(links.header && links.footer)) r.fails.push(`1.13 ${p} not linked in both the header area and the footer`);
    }

    // 1.14: link preview tags, and the share image at 1200 x 630
    const meta = await page.evaluate((names) => Object.fromEntries(names.map(n => [n,
      (document.querySelector(`meta[property="${n}"]`) || document.querySelector(`meta[name="${n}"]`))?.content || null])), OG);
    const missing = OG.filter(n => !meta[n]);
    if (missing.length) r.fails.push('1.14 missing ' + missing.join(', '));
    if (meta['og:image']) {
      const img = await ctx.newPage();
      const res = await img.goto(new URL(meta['og:image'], base).href).catch(e => null);
      const size = res && res.status() === 200 ? await img.evaluate(() => { const i = document.querySelector('img'); return i ? [i.naturalWidth, i.naturalHeight] : null; }) : null;
      r.ogImage = { url: meta['og:image'], status: res ? res.status() : 'error', size };
      if (!res || res.status() !== 200) r.fails.push('1.14 og:image does not answer 200');
      else if (!size || size[0] !== 1200 || size[1] !== 630) r.fails.push(`1.14 og:image is ${size ? size.join(' x ') : 'unreadable'}, not 1200 x 630`);
      await img.close();
    }

    // 2a: five designs, reached from a visible chooser: the chooser (a details, nav or menu that says "Choose a design"
    // or is labelled as the designs) must link to five distinct designs, the current one included.
    // Since 23 Nov 2026 the startup brochures carry it in the footer as <nav aria-label="Designs"> (design.b's decision),
    // so a nav labelled "Designs" counts too.
    r.designs = await page.evaluate(() => {
      const isChooser = el => /choose a design/i.test((el.querySelector('summary, button, h2')?.textContent || '')) || /^designs?( of this page)?$|^choose a design/i.test(el.getAttribute('aria-label') || '');
      const box = [...document.querySelectorAll('details')].find(isChooser) || [...document.querySelectorAll('nav, [role=menu]')].find(isChooser);
      if (!box) {
        // A labelled <select> also counts (Car Buyer, 23 Nov 2026): its label says "Choose a design" and each option is a design.
        const sel = [...document.querySelectorAll('select')].find(s => { const l = s.id && document.querySelector(`label[for="${s.id}"]`); return /choose a design/i.test((l && l.textContent) || s.getAttribute('aria-label') || ''); });
        if (sel) return { chooser: true, count: new Set([...sel.options].map(o => o.value)).size, kind: 'select' };
        return { chooser: false, count: 0 };
      }
      const hrefs = new Set([...box.querySelectorAll('a[href]')].map(a => a.getAttribute('href')).filter(h => !/designs\/(index\.html)?$/.test(h)));
      return { chooser: true, count: hrefs.size };
    });
    if (!r.designs.chooser) r.fails.push('2a no visible "Choose a design" control on the home page');
    else if (r.designs.count < 5) r.fails.push(`2a the chooser offers ${r.designs.count} designs, not five`);

    // 1.12: our links only inside one closed pop-up menu, at the top right
    r.family = await page.evaluate((hosts) => {
      const ours = [...document.querySelectorAll('a[href]')].filter(a => { try { return hosts.includes(new URL(a.href).host); } catch { return false; } });
      // Chromium still gives size to the contents of a closed <details>, so treat anything inside one (but outside its summary) as hidden
      const inClosed = a => { const d = a.closest('details'); return d && !d.open && !a.closest('summary'); };
      const visible = ours.filter(a => { if (inClosed(a)) return false; const b = a.getBoundingClientRect(); return b.width > 0 && b.height > 0 && getComputedStyle(a).visibility !== 'hidden'; });
      const inFooter = visible.filter(a => a.closest('footer'));
      const outside = visible.filter(a => !a.closest('footer'));
      const menus = new Set(ours.map(a => a.closest('details, [popover], [role=menu], nav')).filter(Boolean));
      const summary = [...menus].map(m => m.querySelector('summary, button')).filter(Boolean)[0];
      const sb = summary ? summary.getBoundingClientRect() : null;
      return { links: ours.length, visibleOnLoad: outside.length, inFooter: inFooter.length,
        menuButton: sb ? { x: Math.round(sb.right), y: Math.round(sb.top) } : null, viewport: innerWidth };
    }, FAMILY_HOSTS);
    if (r.family.visibleOnLoad > 0) r.fails.push(`1.12 ${r.family.visibleOnLoad} of our links visible outside a closed menu on load`);
    else if (r.family.links && r.family.menuButton && (r.family.menuButton.x < r.family.viewport * 0.75 || r.family.menuButton.y > 120))
      r.fails.push('1.12 the menu holding our links is not at the top right');

    report.push(r);
    await ctx.close();
  }
  await browser.close();
  console.log(JSON.stringify(report, null, 1));
})();

// The design chooser (guidelines 2a, "The design chooser", 25 Nov 2026), checked live. Read-only.
// Usage: node tools/chooser-check.js https://site.example/ [more roots...]
// For each root, at 1366 and 390 px: one "Choose a design" button near the top; it opens a panel with one card per design,
// each a real screenshot (an <img>) with a number and a name; the current design outlined; an "All five, side by side" link;
// on a phone two cards per row and the top bar on one line. Then each card's screenshot is compared with a fresh
// screenshot of the design it links to (mean pixel difference, 0 identical to 255), as evidence for "screenshots match".
// No pass mark: on the reference sites (Emily Cruz, 25 Nov 2026) the figures run 25 to 72, since a card is a cropped, scaled
// screenshot. Judge the match by eye from the side-by-side; use the figure to spot a card far off its design.
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const report = [];
  for (const root of process.argv.slice(2)) {
    const base = root.endsWith('/') ? root : root + '/';
    const r = { site: base, views: {}, fails: [] };
    for (const [v, w, h] of [['desktop', 1366, 900], ['phone', 390, 844]]) {
      const ctx = await browser.newContext({ viewport: { width: w, height: h } });
      const p = await ctx.newPage();
      await p.goto(base, { waitUntil: 'networkidle' });
      const res = { };
      const btn = p.locator('button, summary, a').filter({ hasText: /choose a design|בחירת עיצוב|בחרו עיצוב/i }).first();
      res.button = await btn.count() > 0;
      if (!res.button) { r.fails.push(`${v}: no "Choose a design" button`); r.views[v] = res; await ctx.close(); continue; }
      const bb = await btn.boundingBox(); res.buttonTop = bb ? Math.round(bb.y) : null;
      if (bb && bb.y > 150) r.fails.push(`${v}: the button is ${Math.round(bb.y)} px down, not in the top bar`);
      // pills or tabs: several design links visible in the top bar before opening
      res.pillsInBar = await p.evaluate(() => [...document.querySelectorAll('a[href*="designs/"]')].filter(a => { const b = a.getBoundingClientRect(); return b.height && b.top < 150 && !a.closest('[hidden], details:not([open])'); }).length);
      if (res.pillsInBar >= 3) r.fails.push(`${v}: ${res.pillsInBar} design links shown in the top bar (pills or tabs)`);
      // top bar: nothing cut off at the right (contents of a closed details do not count; Chromium still gives them size)
      res.bar = await p.evaluate(top => { const els = [...document.querySelectorAll('header *, [role=banner] *, nav *')].filter(e => { const b = e.getBoundingClientRect(); return b.height && b.top < top + 60 && b.top >= 0 && !(e.closest('details') && !e.closest('details').open && !e.closest('summary')); }); const cut = els.some(e => e.getBoundingClientRect().right > innerWidth + 1); return { cut }; }, res.buttonTop || 0);
      if (v === 'phone' && res.bar.cut) r.fails.push('phone: something in the top bar is cut off at the right');
      await btn.click(); await p.waitForTimeout(500);
      res.panel = await p.evaluate(() => {
        const vis = e => { const b = e.getBoundingClientRect(); return b.width > 0 && b.height > 0 && getComputedStyle(e).visibility !== 'hidden'; };
        // a card is a same-site link with a screenshot, under /designs/ or inside the opened panel (designs may live at their own paths: Moving Van, 27 Nov 2026)
        const inPanel = a => !!a.closest('details[open], dialog[open], [role=dialog], [popover], [aria-modal="true"], [id*=design i], [class*=chooser i], [class*=picker i]');
        const links = [...document.querySelectorAll('a[href]')].filter(a => vis(a) && a.querySelector('img') && new URL(a.href, location.href).host === location.host && (/designs?\//.test(a.getAttribute('href')) || inPanel(a)));
        const cards = links.map(a => { const b = a.getBoundingClientRect(); const img = a.querySelector('img'); const cs = getComputedStyle(a); const cur = a.getAttribute('aria-current') || a.closest('[aria-current]');
          return { href: new URL(a.href, location.href).href, img: img.currentSrc || img.src, text: a.textContent.trim().replace(/\s+/g, ' ').slice(0, 80), top: Math.round(b.top), current: !!cur,
            outlined: !!cur && (cs.outlineStyle !== 'none' || parseFloat(cs.borderTopWidth) >= 2 || cs.boxShadow !== 'none') }; });
        const side = [...document.querySelectorAll('a[href]')].some(a => vis(a) && /side by side|זה לצד זה/i.test(a.textContent));
        return { cards, side };
      });
      const c = res.panel.cards;
      res.count = c.length;
      if (c.length < 5) r.fails.push(`${v}: the panel shows ${c.length} screenshot cards, not five`);
      if (c.some(x => !/\d/.test(x.text))) r.fails.push(`${v}: a card without its number`);
      if (!c.some(x => x.current)) r.fails.push(`${v}: no card marked as the current design`);
      else if (!c.some(x => x.current && x.outlined)) r.fails.push(`${v}: the current design is marked but not outlined`);
      if (!res.panel.side) r.fails.push(`${v}: no "All five, side by side" link`);
      if (v === 'phone' && c.length >= 2) { const perRow = c.filter(x => x.top === c[0].top).length; res.perRow = perRow; if (perRow !== 2) r.fails.push(`phone: ${perRow} cards per row, not two`); }
      r.views[v] = res;
      if (v === 'desktop') r.cards = c;
      await ctx.close();
    }
    // screenshots match: each card image against a fresh first screen of its design (desktop cards)
    if (r.cards && r.cards.length) {
      const ctx = await browser.newContext({ viewport: { width: 1366, height: 900 }, bypassCSP: true }); // the comparison loads a data: image
      const p = await ctx.newPage();
      r.match = [];
      for (const card of r.cards.slice(0, 6)) {
        await p.goto(card.href, { waitUntil: 'networkidle' }); await p.waitForTimeout(400);
        const live = (await p.screenshot()).toString('base64');
        const d = await p.evaluate(async ({ live, src }) => {
          const load = s => new Promise((ok, no) => { const i = new Image(); i.onload = () => ok(i); i.onerror = no; i.src = s; });
          const W = 120, H = 80, cv = document.createElement('canvas'); cv.width = W; cv.height = H; const g = cv.getContext('2d');
          const px = img => { g.clearRect(0, 0, W, H); const s = Math.min(img.naturalWidth / W, img.naturalHeight / H); g.drawImage(img, 0, 0, W * s, H * s, 0, 0, W, H); return g.getImageData(0, 0, W, H).data; };
          try { const a = px(await load('data:image/png;base64,' + live)); const b = px(await load(src)); let t = 0; for (let k = 0; k < a.length; k += 4) t += (Math.abs(a[k] - b[k]) + Math.abs(a[k + 1] - b[k + 1]) + Math.abs(a[k + 2] - b[k + 2])) / 3; return Math.round(t / (W * H)); } catch (e) { return null; }
        }, { live, src: card.img });
        r.match.push({ design: card.href.replace(base, '/'), diff: d });
      }
      await ctx.close();
    }
    delete r.cards;
    report.push(r);
  }
  await browser.close();
  console.log(JSON.stringify(report, null, 1));
})();

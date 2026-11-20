// Read-only audit of live pages: screenshots at phone/desktop, light/dark, plus automated checks.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const axeSrc = fs.readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const [urlsFile, outDir] = process.argv.slice(2);
const urls = fs.readFileSync(urlsFile, 'utf8').trim().split('\n');
const combos = [
  { name: 'phone-light', w: 390, h: 844, scheme: 'light' },
  { name: 'phone-dark', w: 390, h: 844, scheme: 'dark' },
  { name: 'desktop-light', w: 1366, h: 900, scheme: 'light' },
  { name: 'desktop-dark', w: 1366, h: 900, scheme: 'dark' },
];
(async () => {
  const browser = await chromium.launch();
  const results = [];
  for (const url of urls) {
    const u = new URL(url);
    const slug = (u.host + u.pathname).replace(/[^a-z0-9.]+/gi, '_');
    for (const c of combos) {
      const ctx = await browser.newContext({ bypassCSP: true, viewport: { width: c.w, height: c.h }, colorScheme: c.scheme, deviceScaleFactor: 1, isMobile: c.w < 500, hasTouch: c.w < 500 });
      const page = await ctx.newPage();
      const reqs = []; const consoleErr = [];
      let bytes = 0;
      page.on('request', r => reqs.push(r.url()));
      page.on('console', m => { if (m.type() === 'error') consoleErr.push(m.text()); });
      page.on('pageerror', e => consoleErr.push(String(e)));
      page.on('response', async r => { try { const b = await r.body(); bytes += b.length; } catch {} });
      const rec = { url, combo: c.name };
      try {
        const resp = await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
        rec.status = resp && resp.status();
        await page.waitForTimeout(300);
        rec.firstLoadBytes = bytes; // before the full-page screenshot, which loads lazy images
        const file = path.join(outDir, `${slug}__${c.name}.png`);
        await page.screenshot({ path: file, fullPage: true });
        rec.shot = file;
        rec.dom = await page.evaluate(() => {
          const de = document.documentElement;
          const cs = getComputedStyle(document.body);
          const small = [];
          for (const el of document.querySelectorAll('a[href], button, input, select, summary, [role=button]')) {
            const r = el.getBoundingClientRect();
            if (r.width === 0 || r.height === 0) continue;
            if (getComputedStyle(el).display === 'inline' && el.closest('p, li p, dd, td, footer p')) continue; // inline text links are exempt
            if (r.width < 24 || r.height < 24) small.push(`${el.tagName.toLowerCase()} "${(el.textContent || '').trim().slice(0, 30)}" ${Math.round(r.width)}x${Math.round(r.height)}`);
          }
          const wide = [];
          for (const el of document.body.querySelectorAll('*')) { const r = el.getBoundingClientRect(); if (r.right > de.clientWidth + 1 && r.width > 0) wide.push(el.tagName.toLowerCase() + (el.className ? '.' + String(el.className).split(' ')[0] : '')); }
          const fonts = new Set(); for (const el of document.querySelectorAll('body, h1, h2, p, a, button')) fonts.add(getComputedStyle(el).fontFamily);
          return {
            lang: de.lang, title: document.title, desc: document.querySelector('meta[name=description]')?.content || null,
            colorSchemeMeta: document.querySelector('meta[name=color-scheme]')?.content || null,
            favicon: !!document.querySelector('link[rel~=icon]'), skip: !!document.querySelector('a[href^="#"].skip, a.skip, a[href="#main"]'),
            main: !!document.querySelector('main'), h1: document.querySelectorAll('h1').length,
            overflowX: de.scrollWidth > de.clientWidth, scrollW: de.scrollWidth, clientW: de.clientWidth, wide: [...new Set(wide)].slice(0, 8),
            bodyFont: cs.fontFamily, bodySize: cs.fontSize, fonts: [...fonts], smallTargets: small.slice(0, 15), smallCount: small.length,
            bg: cs.backgroundColor, fg: cs.color, scripts: [...document.scripts].map(s => s.src || 'inline'),
            imgsNoAlt: [...document.images].filter(i => !i.hasAttribute('alt')).length, height: de.scrollHeight,
          };
        });
        await page.addScriptTag({ content: axeSrc });
        const axe = await page.evaluate(async () => {
          const r = await axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice'] } });
          return r.violations.map(v => ({ id: v.id, impact: v.impact, help: v.help, n: v.nodes.length, sample: v.nodes.slice(0, 3).map(n => n.target.join(' ') + (n.any[0]?.data?.contrastRatio ? ` (ratio ${n.any[0].data.contrastRatio}, fg ${n.any[0].data.fgColor} bg ${n.any[0].data.bgColor})` : '')) }));
        });
        rec.axe = axe;
        rec.cookies = (await ctx.cookies()).map(k => k.name + '@' + k.domain);
        rec.storage = await page.evaluate(() => { try { return Object.keys(localStorage).concat(Object.keys(sessionStorage)); } catch { return []; } });
        rec.thirdParty = [...new Set(reqs.map(r => { try { return new URL(r).host; } catch { return r; } }).filter(h => h && h !== u.host))];
        rec.requests = reqs.length; rec.bytes = bytes; rec.consoleErr = consoleErr.slice(0, 5);
      } catch (e) { rec.error = String(e).slice(0, 300); }
      results.push(rec);
      await ctx.close();
      process.stderr.write('.');
    }
  }
  await browser.close();
  fs.writeFileSync(path.join(outDir, 'audit.json'), JSON.stringify(results, null, 1));
  console.log('\ndone', results.length);
})();

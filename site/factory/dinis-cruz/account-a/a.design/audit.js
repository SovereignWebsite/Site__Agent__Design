// a.design's read-only design audit. Usage: node audit.js <urls.txt> <outDir>
// For each URL: first-screen shots at 390x844 and 1366x900 in light and dark, a full phone shot (light),
// axe violations (WCAG 2.2 AA tags) per combo, phone page height, horizontal overflow, outside requests.
// Needs axe-core resolvable (NODE_PATH) and the pre-installed Playwright.
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const axeSrc = fs.readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const [urlsFile, outDir] = process.argv.slice(2);
const urls = fs.readFileSync(urlsFile, 'utf8').trim().split('\n').filter(Boolean);
const combos = [
  { name: 'phone-light', w: 390, h: 844, scheme: 'light' }, { name: 'phone-dark', w: 390, h: 844, scheme: 'dark' },
  { name: 'desktop-light', w: 1366, h: 900, scheme: 'light' }, { name: 'desktop-dark', w: 1366, h: 900, scheme: 'dark' },
];
fs.mkdirSync(outDir, { recursive: true });
(async () => {
  const browser = await chromium.launch(); const out = [];
  for (const url of urls) {
    const u = new URL(url); const slug = (u.port ? u.port + '_' : '') + u.pathname.replace(/[^a-z0-9]+/gi, '_').replace(/^_|_$/g, '') || 'root';
    for (const c of combos) {
      const ctx = await browser.newContext({ viewport: { width: c.w, height: c.h }, colorScheme: c.scheme, deviceScaleFactor: 1, isMobile: c.w < 500, hasTouch: c.w < 500 });
      const page = await ctx.newPage(); const outside = new Set(); const errs = [];
      page.on('request', r => { const h = new URL(r.url()).host; if (h && h !== u.host) outside.add(h); });
      page.on('pageerror', e => errs.push(String(e)));
      const rec = { url, slug, combo: c.name };
      try {
        await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
        await page.waitForTimeout(300);
        await page.screenshot({ path: path.join(outDir, `${slug}__${c.name}.png`) });
        if (c.name === 'phone-light') await page.screenshot({ path: path.join(outDir, `${slug}__phone-full.png`), fullPage: true });
        Object.assign(rec, await page.evaluate(() => ({ height: document.documentElement.scrollHeight, overflowX: document.documentElement.scrollWidth > innerWidth + 1,
          title: document.title, h1: [...document.querySelectorAll('h1')].map(h => h.textContent.trim()).slice(0, 2) })));
        await page.addScriptTag({ content: axeSrc });
        const ax = await page.evaluate(async () => { const r = await axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] } });
          return r.violations.map(v => ({ id: v.id, impact: v.impact, n: v.nodes.length, sample: v.nodes.slice(0, 3).map(x => x.target.join(' ') + ' :: ' + (x.failureSummary || '').split('\n').slice(1, 2).join('')) })); });
        rec.axe = ax;
      } catch (e) { rec.error = String(e); }
      rec.outside = [...outside]; rec.errors = errs; out.push(rec); await ctx.close();
    }
  }
  fs.writeFileSync(path.join(outDir, 'audit.json'), JSON.stringify(out, null, 1)); await browser.close();
  for (const r of out) console.log(r.combo.padEnd(14), r.slug.padEnd(40), r.error ? 'ERR ' + r.error.slice(0, 80) : `h=${r.height} ox=${r.overflowX} axe=${r.axe.map(a => a.id + ':' + a.n).join(',') || '0'} out=${r.outside.join(',')}${r.errors.length ? ' js=' + r.errors.length : ''}`);
})();

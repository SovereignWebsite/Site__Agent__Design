# a.crm.design: how to restart

A fresh session of a.crm.design continues from here:
1. In SovereignWebsite/Site__Agent__Design (`dev`), read CLAUDE.md, START.md, then this area: agent.json, now.md, role.md.
2. Make a new key with `bash tools/setup-signing.sh a.crm.design@SovereignWebsite.dinis <session-url>`. A new session key needs its own first commit of only site/keys/a.crm.design.json (replacing this one), then update key_fingerprints in agent.json.
3. Times only from `date -u` (never estimated). Sign every commit, with `Agent: a.crm.design@SovereignWebsite.dinis` and `Claude-Session: <url>` trailers. Push to dev only.
4. The work: site/designs/crm-tool/ (index.html, brand.html, assets/, one folder per direction). Shared synthetic data in assets/data.js and the shell (demo band, vault switcher, QR hand-over) in assets/shell.js; each direction has its own css and js. No inline scripts or styles (CSP).
5. Before pushing, run `python3 tools/build.py && bash tools/check.sh` (the deploy's own checks, axe with best-practice rules included); or at least, on the WHOLE built site, not only the design pages: `python3 tools/build.py`, `SITE_VERSION=v0.1.999 node .github/ci/build.mjs`, then `npx --yes html-validate@8.24.0 --config .github/ci/htmlvalidate.json "_site/**/*.html"`, `node .github/ci/share-check.mjs _site` and axe on each page; delete _site after. In now.md never write a bare word inside angle brackets: the area page renders it as an HTML tag (this broke four deploys on 24 Nov).
6. Read now.md for what is open, then tell crm.dev.a (session_018yvwtNP466yYif3yWt3Ybr) and a.maestro (session_018yvwtLiem1AqdA1YkKse4h) that you are back.

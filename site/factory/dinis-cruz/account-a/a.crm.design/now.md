# a.crm.design: now

Updated 2026-11-24T14:30Z.

## Done
- Key published (site/keys/a.crm.design.json, first commit); area and index entry.
- Brand: https://design.agents.sovereignweb.site/designs/crm-tool/brand.html (mark, wordmark, favicon, colours with light and dark, type, 1200x630 share card). Tokens in /designs/crm-tool/assets/brand.css.
- Design 1 of 5, The Day: https://design.agents.sovereignweb.site/designs/crm-tool/day/ , a clickable prototype of every page (Today, follow-ups, lead board, company with Activity, Log an action and the waiting draft, contacts, import, vault with switcher and QR hand-over, requests, You). Checked here before pushing: axe clean on 14 routes at 1366 and 390 px, light and dark; no sideways scroll; 44 px targets on phones; html-validate and the share check pass.
- Overview of the five: https://design.agents.sovereignweb.site/designs/crm-tool/

## Next
- Design 2, The Board; then 3 The Thread, 4 The Map, 5 The Ledger.
- Review rounds once crm.dev.a says a design is live.

## Open
- Asked crm.dev.a (14:08Z) which parts of the app's structure the designs must keep; no answer yet.

## How it is built
- site/factory/dinis-cruz/account-a/a.crm.design/build-designs.py writes the HTML shells (head, demo band, header, vault switcher); each design's pages are drawn by its own js on shared data (assets/data.js) and shell (assets/shell.js).

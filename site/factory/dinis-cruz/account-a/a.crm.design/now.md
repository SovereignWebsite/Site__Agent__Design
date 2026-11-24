# a.crm.design: now

Updated 2026-11-24T15:50Z.

## Done
- Key published (site/keys/a.crm.design.json, first commit); area and index entry.
- Brand: https://design.agents.sovereignweb.site/designs/crm-tool/brand.html (mark, wordmark, favicon, colours with light and dark, type, 1200x630 share card). Tokens in /designs/crm-tool/assets/brand.css.
- Design 1 of 5, The Day: https://design.agents.sovereignweb.site/designs/crm-tool/day/ , a clickable prototype of every page (Today, follow-ups, lead board, company with Activity, Log an action and the waiting draft, contacts, import, vault with switcher and QR hand-over, requests, You). Checked here before pushing: axe clean on 14 routes at 1366 and 390 px, light and dark; no sideways scroll; 44 px targets on phones; html-validate and the share check pass.
- Design 2 of 5, The Board: https://design.agents.sovereignweb.site/designs/crm-tool/board/ , the pipeline wall (four stage columns, overdue cards with a folded corner, move a card on a stage with one button; Today and Follow-ups as the same wall by urgency and by date; the company page is the card turned over; phone: the columns become tabs with counts). Same checks, all clean.
- Design 3 of 5, The Thread: https://design.agents.sovereignweb.site/designs/crm-tool/thread/ , an inbox (list pane and reading pane; each company a conversation, newest first; Needs you, Waiting on them, Mine; the thread as one timeline of emails and logged actions; the reply box is Log an action, with a waiting draft ready in it to send; phone: list or thread, never both). axe clean on 15 routes.
- Design 4 of 5, The Map: https://design.agents.sovereignweb.site/designs/crm-tool/map/ , who knows whom: the team on the left, companies in three regions by where they came from, solid wires for who met them, dashed for introductions; press a person to light up their part; the lead board as a list beside the map; the company page opens on "How we know them". On a phone the wires go and the same facts are in words on every node. axe clean on 13 routes.
- Design 5 of 5, The Ledger: https://design.agents.sovereignweb.site/designs/crm-tool/ledger/ , one sortable table; j and k move, Enter opens, l logs, d opens a draft, / filters; filters and sort as words in the address (e.g. #/ledger/owner:you+state:overdue+sort:-due); the record page is two tables and the log form; prints without the chrome; phone: rows become cards with their action and a Sort by row.
- All five done. Overview with a comparison table and my recommendation (The Day as home, The Ledger one click away, The Board for demos).
- Checks: axe clean on 62 routes (five designs by twelve pages, plus overview and brand) at 1366 and 390 px, light and dark; no sideways scroll; targets 44 px on phones; html-validate and the share check pass.
- Brand, from design.b's brand brief (/briefs/crm-tool-brand.html, read as material): three mark directions for Dinis to pick (the kept card, in use and my pick; the follow-up; the ring), one-colour mark, horizontal and stacked wordmarks, a 32 px PNG favicon, --sws-* tokens, usage rules.
- Fixed: the deploy failed on axe (the version chip the build adds to my footer was too faint); now full contrast.
- Shared: sending a draft now sets the next step to hearing back in three days.
- Overview of the five: https://design.agents.sovereignweb.site/designs/crm-tool/

## Next
- Dinis picks the home design and the mark.
- Review rounds of each design as crm.dev.a builds it.
- Review rounds once crm.dev.a says a design is live.

## Open
- Asked crm.dev.a (14:08Z) which parts of the app's structure the designs must keep; no answer yet.

## How it is built
- site/factory/dinis-cruz/account-a/a.crm.design/build-designs.py writes the HTML shells (head, demo band, header, vault switcher); each design's pages are drawn by its own js on shared data (assets/data.js) and shell (assets/shell.js).

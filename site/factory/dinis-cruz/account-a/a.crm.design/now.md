# a.crm.design: now

Updated 2026-11-25T02:14Z.

## Done
- Key published (site/keys/a.crm.design.json, first commit); area and index entry.
- Brand: https://design.agents.sovereignweb.site/designs/crm-tool/brand.html (mark, wordmark, favicon, colours with light and dark, type, 1200x630 share card). Tokens in /designs/crm-tool/assets/brand.css.
- Design 1 of 5, The Day: https://design.agents.sovereignweb.site/designs/crm-tool/day/ , a clickable prototype of every page (Today, follow-ups, lead board, company with Activity, Log an action and the waiting draft, contacts, import, vault with switcher and QR hand-over, requests, You). Checked here before pushing: axe clean on 14 routes at 1366 and 390 px, light and dark; no sideways scroll; 44 px targets on phones; html-validate and the share check pass.
- Design 2 of 5, The Board: https://design.agents.sovereignweb.site/designs/crm-tool/board/ , the pipeline wall (four stage columns, overdue cards with a folded corner, move a card on a stage with one button; Today and Follow-ups as the same wall by urgency and by date; the company page is the card turned over; phone: the columns become tabs with counts). Same checks, all clean.
- Design 3 of 5, The Thread: https://design.agents.sovereignweb.site/designs/crm-tool/thread/ , an inbox (list pane and reading pane; each company a conversation, newest first; Needs you, Waiting on them, Mine; the thread as one timeline of emails and logged actions; the reply box is Log an action, with a waiting draft ready in it to send; phone: list or thread, never both). axe clean on 15 routes.
- Design 4 of 5, The Map: https://design.agents.sovereignweb.site/designs/crm-tool/map/ , who knows whom: the team on the left, companies in three regions by where they came from, solid wires for who met them, dashed for introductions; press a person to light up their part; the lead board as a list beside the map; the company page opens on "How we know them". On a phone the wires go and the same facts are in words on every node. axe clean on 13 routes.
- Design 5 of 5, The Ledger: https://design.agents.sovereignweb.site/designs/crm-tool/ledger/ , one sortable table; j and k move, Enter opens, l logs, d opens a draft, / filters; filters and sort as words in the address (e.g. #/ledger/owner:you+state:overdue+sort:-due); the record page is two tables and the log form; prints without the chrome; phone: rows become cards with their action and a Sort by row.
- All five done. Overview with a comparison table and my recommendation (The Day as home, The Ledger one click away, The Board for demos).
- Checks: axe clean on 72 routes (five designs by fourteen pages, plus overview and brand) at 1366 and 390 px, light and dark; no sideways scroll; targets 44 px on phones; html-validate and the share check pass.
- Brand, from design.b's brand brief (/briefs/crm-tool-brand.html, read as material): three mark directions for Dinis to pick (the kept card, in use and my pick; the follow-up; the ring), one-colour mark, horizontal and stacked wordmarks, a 32 px PNG favicon, --sws-* tokens, usage rules.
- Fixed: the deploy failed on axe (the version chip the build adds to my footer was too faint); now full contrast.
- Shared: sending a draft now sets the next step to hearing back in three days.
- Overview of the five: https://design.agents.sovereignweb.site/designs/crm-tool/

- Folded in Dinis's note, relayed by crm.dev.a at 14:22Z: many small CRMs (five vaults: Demo, Personal, You and Alex, RiskMandate, Summit CRM, each with its kind, also on the switcher button); a key mark on every person ("Verified key" shield, or "Add their key" leading to You's Take half); "Send to another vault" on the vault page and in the switcher; You in two halves (Give your QR, Take theirs). Demo stages now the app's: new, contacted, talking, proposal, won, parked.
- For crm.dev.a: /designs/crm-tool/adopt/the-day.css and NOTES.md, The Day and the brand on the app's own markup, tested on a local copy of the live app (axe clean, 44 px on phones).

- Ownership agreed with crm.dev.a for Site__Tool__CRM: mine are style.css, site/app/brand/, favicon, share card and design pages; theirs app.js, me.js, vault.js, crm.mjs and the HTML structure.
- Blocked: add_repo for SovereignWebsite/Site__Tool__CRM (push) refused by my permission check at 14:42Z; told Dinis in my session, a.maestro and crm.dev.a. Not worked around.

- The Day and the brand are in the live app (crm.dev.a, Site__Tool__CRM dev 60306db). My round 1 on it: /designs/crm-tool/reviews/the-day-round-1.html ; four CSS fixes in the patch (header at 1280 px, phone pill, why label, key badges, phone tables and targets); two markup asks to crm.dev.a (data-label on table cells; Review and send on draft lines). axe clean on nine app pages.

- Round 2 on the live app (Site__Tool__CRM 825edcd): /designs/crm-tool/reviews/the-day-round-2.html . Round 1's asks all in; axe clean on 10 app pages and 6 site pages. One fix (phone vault pill). New site-frame.css brings the brand and 44 px targets to /, /learn/, /how-to/, /start/.

- Round 3 (44ba0b4): /designs/crm-tool/reviews/the-day-round-3.html . Clean on 16 pages; left: a duplicate header on /learn/videos/ (crm.dev.a) and studio's links under 44 px; studio.css for a.crm.studio, sent through crm.dev.a.

- crm.dev.a dropped the duplicate header on /learn/videos/ (092dfd1). studio.css sent to a.crm.studio (session_018yvwtLdrmYA9n9KshCtiYv) directly.

- a.crm.studio adopted studio.css (aa5dc08) and fixed the player's controls to 44 px (24ab7ea); its pages and https://crm.agents.sovereignweb.site/ checked live: axe clean; on phones every target is 44 px including the player's script toggle (bf11ea0); the Voice checkbox's target is its 44 px label.

- Round 4 (62257c3): /designs/crm-tool/reviews/the-day-round-4.html . Ten pages in one header row from 1280 px; Outbox and Write an email clean; the Outbox state chip gets a shape and Show the email 44 px on phones; markup ask: d-(state) on the chip.

- design.b.rounds' round 2 (on v0.1.8, relayed by a.maestro) checked on v0.1.25: three of its points already fixed; meta line fixed in the patch; five markup and logic points listed for crm.dev.a in adopt/NOTES.md.

- Round 5 (998f815): /designs/crm-tool/reviews/the-day-round-5.html . design.b.rounds' round-2 list all in; buttons and the Everyone / Mine switch in the brand.

- Incident: five deploys of this site failed (16:22 to 16:52 UTC), because a word in angle brackets in now.md, and then in restart.md, rendered as an HTML tag. I validated only the design pages. Fixed at 8c3ee8b; live since. restart.md now says to validate the whole built site before each push.

- Round 5 verified live at 278d1c5: axe clean on 9 pages (app and site); header one row at 1280 px; brass Review and send with a quiet Log an action; the Everyone / Mine switch; the count line at 18 px. Only the Factory's shared credit is under 44 px.

- Round 6 (For you, d8a2e31): /designs/crm-tool/reviews/the-day-round-6.html . Styled and checked on a fixture built from its markup; checked live from a.crm.studio's stills (4f041df): matches the design; round 6b tightens the spacing.

- Where we met: live and checked (axe clean; the field labelled). The demo now shows it too (14 made-up people, "met: ..."), checked live, axe clean.

- The tool's home page, review 1: /designs/crm-tool/reviews/home-round-1.html and adopt/home.css (readable hero crop, feature hierarchy, brand shapes, phone strip: 9,180 to 5,414 px). Advice: lead with the still, not a video; link the 1-minute tour.

- Home page review 2 (live): all markup asks in, axe clean, 5,443 px on a phone; home.css tightened (feature and step rows).

- a.design (account A's design agent) now shares this repository; file split agreed (see agent.json, shares_repo_with).

- Round 7 (the QR hand-over on touch screens, at Dinis's ask via a.maestro): /designs/crm-tool/reviews/the-day-round-7.html . CSS fixes in the patch; asks: let the text box take a pasted picture, touch-screen words. Not tested on a real iPad. Live at 3f37579 and checked in Chromium at 390, 820 and 1180 px: all six asks in, axe clean; Dinis is to try it on a real iPad.

## Next
- Dinis picks the home design and the mark.
- The next round when crm.dev.a ships a new page or Dinis picks; the other four designs as Dinis wishes.

## Open
- Asked crm.dev.a (14:08Z) which parts of the app's structure the designs must keep; no answer yet.

## How it is built
- site/factory/dinis-cruz/account-a/a.crm.design/build-designs.py writes the HTML shells (head, demo band, header, vault switcher); each design's pages are drawn by its own js on shared data (assets/data.js) and shell (assets/shell.js).

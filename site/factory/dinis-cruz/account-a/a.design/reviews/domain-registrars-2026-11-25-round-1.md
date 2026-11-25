# Domain registrars, round 1: a.design's review of the five directions

For domain-registrars.a, keeper of domain-registrars.services.sovereignweb.site, 25 November 2026, 00:55 UTC. Looked at: Site__Services__Domain-Registrars dev **f852a01**, served locally from site/ (the live address did not answer). Checked: each design's home and its "Registrars with APIs" comparison page, at 390 x 844 and 1366 x 900, light and dark; axe-core 4.10 (WCAG 2.2 AA tags) on all 40 combinations; page height on a phone; sideways scroll; outside requests.

Contact sheets: [phone first screens, light, d1 to d5](img/domain-registrars-2026-11-25-round-1-phone.jpg); [comparison page in dark on phones, and on desktop d1 and d5](img/domain-registrars-2026-11-25-round-1-registrars.jpg); [the comparison table on a phone, d1 and d5, and d3 on a desktop](img/domain-registrars-2026-11-25-round-1-tables.jpg).

## What is right
- **axe is clean on all 40 combinations**; no sideways scroll on the page at 390 px; nothing loaded from other sites.
- The research is honest in the design itself: "not stated" chips, "partly from a search summary" labels, prices as each vendor showed them, and "Our reading, not a sourced fact" set apart. Keep that in whichever design wins.
- Each preview is the whole site with its links kept inside it, so a reader can walk through a design, not only look at its home.

## Recommendation: d5, Dashboard (I differ from the keeper's d1)
The page people will come back to is the comparison, and the reader registers domains for customers: they want the table, scannable, with the explanations a tap away. d5 is the direction built for that, and on a desktop its home tiles and compact tables already read best. Take d4's margin sources into d5's explanation pages on wide screens. d1 Ledger reads beautifully, but it is the best design for a reader this site has less of.

## Worst first
1. **On a phone the five are one layout.** Every design opens with the long title, eight section links wrapping onto three or four lines (seven lines in d2's brackets), the preview box, the site's own address in capitals as a kicker, then the same heading and paragraph. Only the type and colour change. On a phone: put the sections in one "Sections" button, drop the address kicker (it repeats the URL), and let each direction show its idea on the first screen (d5 the coverage table, d3 its map of sections, d4 a claim with its source beside it).
2. **The comparison table loses its columns on a phone.** In every design the table scrolls inside its box, the .uk, .eu and .pt columns start off screen with no sign they are there, and the registrar names scroll away with the rest. Make the Registrar column sticky, add a "Scroll for .uk, .eu, .pt" cue, and let the caption wrap instead of being cut.
3. **Three notes stand before the table** (the scope paragraph, "How to read the prices", "Our reading"). Put the table first, with one line above it, "Every price as shown on 25 Nov 2026, in the vendor's currency. How to read this", that opens the notes.
4. **d1 and d4 are too close on a phone**: both serif on warm paper; d4's sources in the margin only appear on wide screens. On a phone show d4's source as a small line under each claim, or merge d4 into d1.
5. **d3 Atlas is a sidebar only on a desktop**; at 390 px it is the same column as the others. Give it a sticky section bar on phones, or it is not a direction there.
6. **d2 Terminal** is the hardest to read for newcomers (monospace body text at 390 px), and its bracket menu is seven lines. Keep it only if the audience is mostly developers; otherwise retire it in round 2.

## On the designs page
It is clear and asks the right three questions. It needs a picture of each design's phone first screen and a way to record the pick that everyone can see (the cross-site standard is at /factory/dinis-cruz/account-a/a.design/picker.html).

## Checks for round 2
- Each direction's idea visible on the phone first screen.
- The comparison table usable at 390 px: sticky names, a cue for more columns.
- axe clean again, light and dark, at 390 and 1366 px; the live address serves.

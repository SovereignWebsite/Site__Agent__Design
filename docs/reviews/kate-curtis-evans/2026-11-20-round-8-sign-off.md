# Round 8: Kate Curtis-Evans, signed off with notes

design.b@SovereignWebsite.dinis (fresh session), 20 November 2026, about 16:30 UTC, against Site__Founder__Kate-Curtis-Evans 89e5043, live from 15:29 UTC. Dinis Cruz, relayed by the other design.b session at 15:42 UTC (guidelines 6b0be24): "I don't need to sign off the design. You push the sign off." So design.b records this sign-off itself.

**Verdict: signed off with notes. Rating 4.**

## Evidence

- **Measured:** home, /designs/, The Transcript, The Edit Window, The Newsroom and The Brief, at 390 and 1366 px, light and dark (24 views): axe-core finds nothing. No other-host requests, no overflow, no target under 24 px, 10 to 149 KB first load.
- **The round 7 points are fixed:**
  - The lanes are equal height. On phones three lanes collapse to their coloured headings with "Show", and the co-founder lane stays open.
  - Small text is 1rem in `--fg`.
  - The chooser panel now pushes the page down.
  - The "?" and the stray "2" are gone.
- **The wow bar** (guidelines 12):
  - One "Choose a design" control in the header opens five screenshot cards, side by side.
  - Every design but the Brief has a full-bleed or full-scene hero, huge display type and depth. Two are dark first (The Edit Window and The Newsroom).
  - The Board now reads as a real board, with coloured lanes, stacked cards, tags and assignee marks.
- **Synthetic users** (round 7, before these fixes): 4, 4, 4, 4, 4. All five would show it to a friend. Their wow came with a "nearly", and the agreed points behind it are what round 8 fixed.
- **Hand-over:** docs/handover.md, docs/questions-for-kate.md and docs/prompt-for-your-claude.md, plus a start page at /start/.

## Notes (not blocking)

1. Only the cleared desk photo is used. When Kate sends more photos, or when generated stock images are allowed in kate-curtis-evans.b's environment (no OpenRouter key there yet), the Transcript and Edit Window heroes gain the most.
2. The phone page is still long. Kate can shorten it once she chooses her home design.
3. After Kate adds her own material, one more design pass (guidelines 12).

## KPI

Rounds to sign-off: **8**, over the target of 3. Rounds 4 to 8 followed new guidance from Dinis (the chooser, the Newsroom, the hand-over, the wow bar). The first sign-off (round 5) passed the checklist and failed his eye. That lesson is now in rating.md.

## Suspended, 16:45 UTC

Dinis Cruz, about 15:35 UTC: "This website is for them... not a website about us." The family bar at the top of a customer's site reads as the site's own menu, and he clicked it by mistake. It is now guidelines 1.12: any review that finds our links at the top of a customer site fails. Kate's site carries the family bar at the top, as every customer site does. **The design sign-off stands at 4, but is suspended** until factory.b's change moves the bar to a small credit the owner can remove. Nothing else is needed from kate-curtis-evans.b.

## Rechecked, 5cabbc9 (17:15 UTC)

Dinis Cruz, in kate-curtis-evans.b's session: "the current site is now great, all that is needed is to fix the top navigation bar so that it is related to this site". The top bar is now Kate's own (her name, Co-founder wanted, Audio Genius, LinkedIn, Choose a design). tools/site-checks.js finds:
- **1.12 passes:** our links are only in the closed top-right menu.
- **1.14 passes:** the full link preview, with a share image of 1200 x 630 that answers 200.
- **1.13:** all four pages answer 200, but /admin/ is linked only in the footer. It needs the header's right-hand area too.

axe-core is clean on home, /start/, /agents/, /admin/, the Transcript and the Newsroom in four views. The sign-off becomes active once /admin/ is in the header.

## Sign-off active, c7bffb9 (17:35 UTC)

"How it was made" (/admin/) is now in the top bar with "Start here" and "Use with your AI", and in every footer. tools/site-checks.js finds no failure: 1.12, 1.13 and 1.14 all pass. There is no sideways scroll at 320 or 390 px on home, /start/, /agents/, /admin/ or /designs/. axe-core is clean on home and /admin/ in four views. The top bar ends at 143 px on a 390 px phone. **Kate Curtis-Evans's site is signed off at 4, with the notes above.**

## The admin dashboard, 6ad7261 (17:55 UTC)

Kate's /admin/ is the pilot of the admin dashboard (guidelines 12). Checked live against that section:
- **Panels:** Overview (version), Activity, Content, Quality (check results over time), Design, Agents, Ask Claude and Visitors.
- **Charts:** 10, as inline SVG with `role="img"` and labels, so no chart library is needed. There are 10 data tables, most behind "Show data".
- **Rules met:** `noindex`; no external script; no email address on the page; build-time data files (version.json, admin/data.json, admin/data/checks.json).
- **Phone and weight:** no sideways scroll at 390 px, with wide tables and code scrolling in their own boxes; 188 KB first load on a phone, 291 KB on desktop.

To fix:
1. **Dark scheme contrast (axe, serious):** the `.live` badge is white on #6cc283, 2.16:1. Use dark text on it, or a darker green, for 4.5:1.
2. **The Design panel has round 1 at rating 2; design.b rated it 1** (15 contrast failures in the light scheme). Read the ratings from design.b's data/rounds/kate-curtis-evans.founder.sovereignweb.site.json when it is live, rather than copying them. The synthetic-user scores for rounds 2, 5 and 7 match the published runs.

**Dashboard checked, 2bedbc3 (18:10 UTC):** the `.live` badge passes at 7.85:1 in dark and 5.27:1 in light, and axe-core is clean in all four views. The Design panel's round 1 now reads 1, and every round and synthetic-user score matches design.b's records. The dashboard meets the admin dashboard section of guidelines 12.

## The message page, 2f4c67f (18:20 UTC)

/admin/message/ lets Kate and Dinis send signed, sealed requests to the site's agent. It was checked at 320, 390 and 1366 px, light and dark:
- no sideways scroll; 47 KB; noindex; local scripts only;
- the add-key and "What the agent will do" panels are visible in every view.

Sent to kate-curtis-evans.b:
1. Dark contrast: "Add my key" is white on #e58a63 at 2.57:1 (axe, serious).
2. An empty band of about 90 px where the hidden compose form reserves space.
3. Show the key state as a `role="status"` line with a word and a dot, not a card.
4. Order the panels by state (with no key, and with a key).
5. Two columns on desktop, with the rules panel sticky beside the message being written.
6. A one-line pointer to the rules under the intro on phones.
7. A visible label on the key input, and a cleanly breaking footer link.

**Message page checked, c03a930 (18:30 UTC):**
- **Measured:** axe-core is clean in four views, with no sideways scroll at 320 or 390 px.
- **Status:** the key state is a `role="status"` line with a dot and a word.
- **Layout:**
  - The panels follow the state: Add your key, then the rules, then Replies without a key; Write a message, then Replies, then a closed "Add your key", then the rules with one.
  - Over 60rem there are two columns, with "What the agent will do" and the QR sticky on the right.
  - The pointer line under the intro links to the rules, and the empty band is gone.
- **Fixes and panels:** the dark buttons pass, and the add-key and rules panels are visible in every view.

All seven points are met.

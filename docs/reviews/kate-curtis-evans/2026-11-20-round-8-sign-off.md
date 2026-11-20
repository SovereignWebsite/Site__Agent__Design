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

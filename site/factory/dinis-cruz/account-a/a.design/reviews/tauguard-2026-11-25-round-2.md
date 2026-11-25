# TauGuard and RiskMandate, round 2: a.design's check

For tauguard.a, 25 November 2026, 01:15 UTC. Looked at: Site__Company__TauGuard dev **b6dbf89** (round 2 is 1a6e316, plus a CI refresh), served locally. The five prototypes at 390 x 844 and 1366 x 900, light and dark, with axe-core 4.10: **clean on all 20**, including the dark contrast failures and the scroll wrapper from round 1. [Contact sheet: the five on a phone, and Atlas in dark](img/tauguard-2026-11-25-round-2-phone.jpg). Round 1: [review](tauguard-2026-11-25-round-1.html).

## Round 1's list, checked
All eight done: design 1 is a real prototype; one notice; diagrams scroll inside a labelled, focusable figure; Briefing's tabs sit under the first paragraph with an Overview tab (Briefing is now 1,880 px on a phone, from 6,060); Ledger's two-sided strip; Atlas's index as one row; Blueprint two tiles per row; dark contrast fixed.

## What is left
1. **The diagrams are cut at the right edge with no sign they scroll.** At 390 px the figure is 760 px wide; a reader sees a box cut in half. Add a short "Swipe to see the whole drawing" line above each, as Domain registrars now does for its tables.
2. **The prototypes' header is the design switcher** ("Design directions 1 2 3 4 5 Live site"), not the site's own header. When Briefing is chosen, its header and navigation need designing in its own style; check that the switcher row never reaches the live site (design.b's guideline: no rows of numbered pills on a live page).
3. **The notice is still a box of four lines on a phone.** It is one box now, not two; shorten the sentence to fit two lines ("A proposal about TauGuard from its public pages. Not TauGuard's own site. Design 4 of 5.").

## Recommendation
**Yes: recommend 4, Briefing, to Dinis**, with Ledger's columns in Side by side. Items 1 to 3 are small and can go with the build of the chosen design; no round 3 is needed for the choice.

## Later, 01:15 UTC: Blueprint's palette
At dev **441e314** Blueprint moved from navy, cyan and amber (which echoed TauGuard's own pages, as tauguard.a found by comparing) to neutral graphite. axe clean in dark. [Contact sheet, third screen](img/fixes-2026-11-25-0110.jpg). I see no remaining resemblance in the five; I have not compared them against tauguard.ai myself.

## Later, 01:20 UTC: the swipe cue and the notice
Checked at dev **1effd0a**: "Swipe to see the whole drawing" above each diagram on phones, and the notice tightened to three lines with the design tag inline. Three lines is the floor with a mandatory 115-character sentence at 14 px, which I accept. The numbered switcher is built for /designs/ only. [Contact sheet, last screen](img/fixes-2026-11-25-0120.jpg). Ready for Dinis.

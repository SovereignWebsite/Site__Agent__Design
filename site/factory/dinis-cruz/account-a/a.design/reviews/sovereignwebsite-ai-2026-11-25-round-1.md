# sovereignwebsite.ai restyle, round 1: a.design's review of designs 6 to 10

For website.a, 25 November 2026, 13:55 UTC. Looked at: SovereignWebsite__Website dev **d09ba27**, served locally. Checked: /designs/ and designs 6 to 10 at 390 x 844 and 1366 x 900, light and dark, with axe-core 4.10; by script, the picker opened and a design chosen in design 8; and the width at 320 px. [The five on a phone, then 8 in dark](img/sovereignwebsite-ai-2026-11-25-round-1-phone.jpg); [desktop](img/sovereignwebsite-ai-2026-11-25-round-1-desk.jpg); [the picker open, and design 8 after choosing the cobalt North Studio design](img/sovereignwebsite-ai-2026-11-25-round-1-picker-and-tap.jpg). The direction: [page](sovereignwebsite-ai-2026-11-25-direction.html); design 6 alone: [review](sovereignwebsite-ai-2026-11-25-design-6.html).

## What is right
- **Every item of the design 6 review is done**: the picker at the very top of every page, the kicker back to the brand, the phone header one line (name, Menu, Request), five North Studio cards scrolling sideways with the fictional caption.
- **Design 8 works without a script.** Choose a North Studio card and the whole page below takes its colours (radio inputs and :checked). That is the product, shown in the page itself.
- The Brief (7) and The Hub (10) have real structures of their own: a numbered contents list, and sites grouped by kind with "Yours could sit here".
- One generator for all five, so the words and prices cannot drift apart. Phone pages 5,870 to 7,060 px.

## Worst first
1. **axe fails on every design: the North Studio strip** (.ns, and .five in design 8) scrolls sideways but cannot take keyboard focus (scrollable-region-focusable). Give the strip `tabindex="0"`, `role="region"` and an `aria-label` ("Five designs for North Studio, a fictional studio"). This is the only axe failure; everything else is clean in both schemes and widths.
2. **Ownership (9) has the same first screen as Studio (6)**, on a phone and on a desktop: the hero, two buttons, the strip. Its idea (a timeline of what you hold, with proof) starts below the fold. Lead with the timeline: the headline, then step 1 "You ask" to step 4 "You move it anywhere" with its proof, and move the strip lower.
3. **At 320 px the page is 336 px wide** (you named it): the header's three items do not fit. Below 360 px, shorten "Sovereign Website" to the mark alone, or "Request" to an icon with its label kept for screen readers.
4. **The picker shows desktop screenshots, one per row, on a phone.** The standard asks for each design's phone first screen, two to a row at 390 px, so the five fit in about one screen. The desktop thumbnails are too small to read at that size.
5. **The North Studio cards end in gradient blocks** that read as missing photos. Draw a simple building line in each (two or three SVG strokes, plain fills, width and height set) so they read as architecture.
6. **/designs/ is 8,390 px on a phone**, over the 8,000 limit; the dark row can be a link, not a second set of pictures.
7. **Run axe yourself**: the repo has no tools/check.sh. Copy the seeded .github/ci/axe.mjs and a check script from another site (Site__Agent__Design's tools/check.sh is a short one).

## Recommendation: 6, Studio, with design 8's tap-to-recolour in its strip
Studio is the brief Dinis supplied, and it is the calmest for the non-technical reader the sector pages will reach. Design 8's interaction is the best single idea in the round: put it into Studio's North Studio strip, so the five cards are choices and the strip (not the whole page) takes the chosen design's colours. Keep 8 as the dark, loud alternative. After items 1 to 3, this is ready for Dinis to pick, beside the live design 1.

## Later, 14:00 UTC: items 1 to 5 fixed
Checked at dev **16408e9**: axe clean on all five at both widths and in both schemes (the strip is a labelled, focusable region); Ownership leads with its timeline ("You ask", "We build it", each with its proof); 320 px wide at 320 px; the picker shows phone first screens two to a row, the current one outlined with "You are here"; the North Studio cards draw a small building. [Studio, Ownership and the open picker](img/sovereignwebsite-ai-2026-11-25-round-1-fixes.jpg). Still open: /designs/ (height, table, recommendations, the three questions) and a check script. Ready for Dinis: 6 Studio with design 8's tap-to-recolour in its strip.

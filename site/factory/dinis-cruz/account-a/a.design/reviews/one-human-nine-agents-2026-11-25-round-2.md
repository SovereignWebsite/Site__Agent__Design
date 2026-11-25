# One Human, Nine Agents, Nineteen Hours, round 2: a.design's check

For one-human-nine-agents.a, 25 November 2026, 02:15 UTC. Looked at: Site__Author__Dinis__One-Human-Nine-Agents dev **2cff69c**, served locally. /designs/ and the five designs at 390 x 844 and 1366 x 900, light and dark, with axe-core 4.10: **clean on all 24**. [The five on a phone, and Poster in dark](img/one-human-nine-agents-2026-11-25-round-2-phone.jpg). Round 1: [review](one-human-nine-agents-2026-11-25-round-1.html).

## Round 1's list, checked
1. **The stylesheet hash: my finding was wrong, and I withdraw it.** The site's .github/ci/build.mjs adds `?v=` and a hash of the file to every local stylesheet link when it builds _site, so the served pages carry it. I read the source, not the built output. No need to put it in the source; I have made the standard say that either place is fine as long as the served page has it.
2. **Poster is dark in both schemes**, and the table says so. Done.
3. **Header links wrap to two lines at 390 px**, none cut. Done.
4. **The cover is shown in every design**, credited ("The RC2 cover, from the book's own site") and served from the site itself. Done; and its four stripes confirm item 5.
5. **Poster's caption**: "The four stripes are the cover's own colours." Done.
6. **Questions opens on "Where do I read it, and how long is it?"** Done.

Also taken up: a "Read it: Leanpub, or the free RC2 PDF" line under every subtitle, and The Day now runs the timeline, then "Then pick how much to read" (the ladder), then the rest.

## What is left
1. **The cover sits on a row of its own, right-aligned, on phones in The Day, Editions and Questions,** leaving the left half of that row empty and pushing the timeline (or the ladder) down by about 150 px. Float it beside the subtitle and the "Read it" line instead, as Ledger and Poster already do.

## Recommendation
**3, The Day**, with the ladder after the timeline as now. With item 1 it is ready for Dinis; no round 3 is needed for the choice.

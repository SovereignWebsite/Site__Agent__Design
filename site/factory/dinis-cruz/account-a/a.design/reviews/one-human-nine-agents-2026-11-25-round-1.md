# One Human, Nine Agents, Nineteen Hours, round 1: a.design's review of the five directions

For one-human-nine-agents.a, keeper of one-human-nine-agents.dinis.author.sovereignweb.site, 25 November 2026, 02:10 UTC. Looked at: Site__Author__Dinis__One-Human-Nine-Agents dev **44ce562**, served locally (the live /designs/ was not serving yet). Checked: the home, /designs/ and the five designs (/d1/ to /d5/) at 390 x 844 and 1366 x 900, light and dark, with axe-core 4.10: **clean on all 28**; and /designs/ and design 3 with every stylesheet blocked. [The five on a phone, then the home](img/one-human-nine-agents-2026-11-25-round-1-phone.jpg); [/designs/, the same with no CSS, design 3 with no CSS, and Poster in dark](img/one-human-nine-agents-2026-11-25-round-1-picker.jpg).

## What is right
- **The five differ in structure on a phone, on the first screen.** Numbers first, a poster, a timeline of the day, a ladder of editions by page count, and fold-out questions. That is the best first round of the eight sites I review: the one failure common to the others (five skins of one layout at 390 px) is not here.
- **The picker follows the standard**: "Choose a design" at the very top of every page, one preview line, five phone pictures side by side on /designs/, the table, and a pick line.
- **With no stylesheet, every thumbnail keeps its set size** (78 x 169 in the control, 195 x 422 on /designs/) and reads as a small picture. No black blocks.
- Every number carries its source ("Source: Book site, home page"), and design 4's ladder (3, 10, 30, 70 and 150 pages, each bar sized by length) is the cleverest single idea in this round.

## Recommendation: 3, The Day, with design 4's ladder as its second section
The book is the story of one day, and the timeline from the first commit at 00:16 to the talk at 19:00 is that story in the page's own shape; it is the design a reader will remember. Its weakness, as your table says honestly, is that the editions come after the story; so put design 4's ladder straight after the timeline, and one line under the subtitle on the first screen: "Read it: Leanpub, or the free PDF".

## What is weak, worst first
1. **The stylesheet links have no content hash.** /assets/picker.css, base.css and d1.css to d5.css are linked without `?v=`, in the source at 44ce562. That is the rule from TauGuard's black-block picker (standard, section 4a); the size-safe thumbnails are done, the hash is not.
2. **"Dark first: yes" for Poster is not what it does.** In light mode Poster is a cream page; it turns dark only when the device asks for dark. Either make it dark in both schemes (it is the loud one, and design.b's guidelines ask for at least one design dark first) or change the table to "no".
3. **The header links are cut off at 390 px** in designs 2 to 5: "Use with your AI" ends as "Use with" at the edge, with no sign the row scrolls. Wrap to a second line, shorten to "Your AI", or fade the edge to show it scrolls.
4. **None of the five shows the book.** Ledger's "weakest at" (the book has no visual presence) is true of all five. If the cover is public on the book's own Leanpub page, show it, credited, on each first screen: on The Day as the object at 19:00, on Poster as the poster itself.
5. **Poster's four-colour stripe** (green, yellow, blue, red) reads close to a well-known technology brand's palette at a glance. If those are the book cover's colours, say so in a caption ("Colours from the book's cover"); if not, choose two of them.
6. **Questions** spends its first screen on one quotation inside the first fold-out. Open "Where do I read it?" by default instead; that is the question a visitor on a phone is most likely asking.
7. **The /policy/ page lacks the picker**, which you know and are waiting on the owner for.

## Checks for round 2
- A `?v=` hash on every stylesheet link; the no-CSS check still passes.
- Poster's dark-first claim matches what it does; header links not cut at 390 px.
- axe clean again, light and dark, at 390 and 1366 px.

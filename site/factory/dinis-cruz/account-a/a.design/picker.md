# Choose a design: one standard for every site

Kept by a.design (account A's design agent), 25 November 2026. It applies to every site whose keeper builds design rounds. It follows design.b's [guidelines](../../../../guidelines.html) (2a "Five designs, always"; "A visual chooser"; "Push, do not wait for sign-off") and adds what the first five account A reviews showed was missing: the pictures, the recorded pick, and one shape for the /designs/ page. Where this page and design.b's guidelines differ, the guidelines win and I fix this page.

## Why one standard
Dinis and the team compare designs across many sites. If every site shows its designs the same way, a choice takes a minute: open /designs/, look at five pictures side by side, read five lines, see who recommends what, pick. Today each site does it differently: a text list on one, a drop-down on every page on another, a description page instead of a prototype on a third, and on every one the pick is "tell Dinis which number".

## 1. The control on every page

**While a pick is open, the picker goes at the top of every page, with a preview of each design.** Dinis Cruz, as relayed by sites.a on 25 November 2026 at about 01:40 UTC: "designs like the tower one [read as TauGuard], they should always go at the top of the page with a preview of each one, like we have done in multiple ones." I have this through sites.a, not in my own session. So, until the pick is recorded: the control sits at the very top of every page of the site (not only on /designs/), and opening it shows a picture of each design; London Agentics does this on all its pages and is the model. Once the pick is recorded, the control may move back into the header as below.

- One control labelled **Choose a design**: at the top of every page while a pick is open (above), then in the site's own header, after its navigation. It is a `details` element: closed by default, works without a script, hidden in print.
- Open, it shows a panel of the **active designs**, five at most. Each card: a real screenshot of that design's phone first screen, its name, its one-line idea; the design being viewed is outlined and carries `aria-current="page"`; the live default is marked "Live".
- Every card is a plain link at least 44 px high. At 390 px the cards sit two to a row and the panel scrolls inside itself; it never pushes the page sideways.
- The last link in the panel is "Compare all designs", to /designs/.

## 2. The /designs/ page, in this order
1. **The five side by side.** One row of the five phone first screens (390 x 844, light) at the same scale, each captioned with its number and name and linked to the design. On a phone the row scrolls sideways inside its own focusable box. Below it, a link to the same row in dark.
2. **One table.** Columns: design, its idea in one sentence, best for, weakest at, dark first (yes or no). Five rows. Write "weakest at" honestly; it is what makes the table useful.
3. **Who recommends what.** The keeper's recommendation and the design reviewer's, each with one sentence and a link to the review. If they differ, both stay on the page; the difference is information for whoever picks.
4. **The pick.** Before it is made: "Not picked yet. The live site uses d1 meanwhile." After, for example: "Picked: d2, Poster, by Dinis Cruz on (date)", with a link to where he said it (his session's decision record on decisions.agents.sovereignweb.site, or the keeper's docs/designs.md entry quoting him). Nothing in the browser records a choice: no cookies, no form.
5. **How to choose.** Three questions, the same on every site: does the first screen on a phone say what this site is for; can you do the main task (read, compare, practise, apply) without hunting; would the owner say "wow". Then "say which number to keep".
6. **Rounds.** Newest first: the date, who reviewed (keeper, a.design, design.b), a link to the review, what was found and what changed. London Agentics' /designs/ log is the model.
7. **Earlier designs.** Designs retired from the active five stay reachable at their old address, listed here with why they were not taken forward. They are not in the control.

## 3. The preview pages
- Each design is the whole site in that design, with its links kept inside the design (as on Domain registrars), so a reader can walk through it.
- At the top, one line inside a landmark: "Preview: d3, Atlas. The live site uses d1. Compare all designs". One line on a phone, no box, nothing else that reads like a demo (design.b's guideline: no scaffolding on a live page).
- The same content as the live site, including anything added since the round began. A design that leaves out real content cannot be judged fairly.
- Every design is a real prototype. A page that describes a design instead of being it does not count.

## 4. The screenshots
- Made by script at build time, never by hand, so they cannot go stale: Playwright at 390 x 844, device scale 1, light, the first screen only, saved as JPEG at about 70 per cent quality (under 80 KB each), with the date taken in the caption.
- Alt text names the design and what its first screen shows, in one sentence.
- Served from the site itself; nothing loaded from elsewhere.

## 5. Checks before a round is shown
- axe (WCAG 2.2 AA) clean on /designs/ and on each design's home, light and dark, at 390 and 1366 px, with the control both closed and open.
- No sideways scroll at 390 px; the control's panel fits.
- The five differ in structure on a phone, not only in type and colour. This is the most common failure in the first reviews: each direction's idea must be visible on its phone first screen.
- Five designs at most in the control; the pick line present (picked or not yet).

## Where it stands, 25 November 2026, 01:10 UTC
| Site | At the top of every page | Pictures | Five at most | Recommendations shown | Pick recorded |
|---|---|---|---|---|---|
| london.agentics-foundation | yes | yes | yes (four more under Earlier rounds) | keeper only | "none yet" line |
| uk-driving-test.tool | to check once live | no | yes | keeper, design.b and a.design, in the log | no |
| tauguard.company | top links 1 to 5 | no | yes | keeper only | no |
| startup-grants.tool | "All five designs" link | no | yes | none | no |
| domain-registrars.services | to check once live | no | yes | keeper only | no |
| github.tool | "Choose a design" link | no | yes | keeper only | no |
| apple.platform | "Designs" link | drawn sketches | yes | none | no |

I update this table at each review round.

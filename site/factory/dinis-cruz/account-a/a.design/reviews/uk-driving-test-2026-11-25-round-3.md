# UK driving theory test, round 3: a.design's review of the five directions

For uk-driving-test.a, keeper of uk-driving-test.tool.sovereignweb.site, 25 November 2026, 00:45 UTC. Looked at: Site__Tool__UK-Driving-Test dev **249fc62** ("Act on design review round 2"), served locally from site/, because the live address still has no certificate for its name. Checked: the designs index and each direction's home, topic and quiz page (16 pages) at 390 x 844 and 1366 x 900, light and dark; axe-core 4.10 (WCAG 2.2 AA tags) on all 64 combinations; page height on a phone; sideways scroll; outside requests. Read with design.b's round 2, which I agree with on the home and differ from on what to do next.

Phone first screens, light, left to right Plain page, Course path, Quiz first, Highway Code book, Road map:

Open the [contact sheet: Phone first screens in light mode](img/uk-driving-test-2026-11-25-round-3-phone-light.jpg).

The same in dark:

Open the [contact sheet: Phone first screens in dark mode](img/uk-driving-test-2026-11-25-round-3-phone-dark.jpg).

## What is right
- **axe is clean on all 64 combinations**, no sideways scroll at 390 px, no outside requests, no script errors. That is rare at round 3.
- Round 2 was acted on in full and fast: one title, a one-line notice, progress from saved results, signs drawn from basic shapes, the Course route collapsed to one line.
- The five homes are still five structures: a plain list, a route, bottom tabs, a contents page, a road with stops.

## The gap round 3 shows: only the homes differ
The five directions part ways on the first screen and meet again one tap later. The topic page and the quiz page are the same layout in every design, recoloured: one long column, all nine questions at once, about 4,800 px on a phone, with "Check my answers" at the very bottom. The quiz is what a learner comes back for, so it is where the directions most need to differ. Round 4 should design the quiz in each direction's own form (below), not only the home.

## Recommendation: Quiz first as home
I agree with design.b: **Quiz first**. It puts a quiz on the first screen, its tabs are what a phone user already knows, and its start card now carries a drawn sign. **Road map** stays the showpiece. Make Quiz first earn it in round 4 with a quiz built for a phone (item 1).

## Weakest point of each direction, worst first
1. **Quiz first: the quiz is not a quiz-first quiz.** Show one question per screen, with "Question 3 of 9" and a thin progress bar, the answer and its rule straight after each choice, and a score card at the end that updates the tile's best score. Keep the all-on-one-page form as the no-script fallback it already is.
2. **Quiz first: dark mode inverts the brand into the brightest thing on the page.** In dark the header band and the start card turn pale blue with dark text, two large light slabs on a dark page. Keep them dark (a deep blue surface, light text) and let only the button and the sign carry light colour.
3. **Quiz first: six tabs** (Home, The test, Rules, Quiz, Hazards, About) at 390 px. Five at most; move About to the footer, where the rest of the small print already is. Give each tab a small drawn icon above its word, so the bar reads at a glance.
4. **Course path: it says "Four steps" and "Step 1 of 5" on the same screen.** The lead counts four cards, the route counts five (Sources and licence is the fifth). Either drop Sources from the route or say five steps; a course that miscounts its own steps loses trust.
5. **Highway Code book: the contents appear twice on the first screens**, a boxed list of five, then "Contents" again in the body with the ten topics. On a phone that is the whole first two screens. Keep one contents list, the full one, as the book's page; drop the box on phones and keep it as the margin list on a desktop only.
6. **Road map: the stops carry no words for their state.** With nothing saved, stop 3 is a white ring and the others yellow, which reads as a state nobody can name. Under each stop, say it: "Not started", "Best: 7 of 9". The signs beside the stops repeat (the warning triangle twice) and do not relate to the stop; give each stop its own sign or none. Two of the four stops (the test, the hazard) leave the design for the live pages while two stay inside it; keep a reader in the direction they chose. Road map is always dark; that is a fair choice for one direction, as long as it is the only one.
7. **Plain page: the menu and the list below it are the same five links.** On a phone the first screen is the menu, then the same items again as a numbered list. Drop the top links on the home only and let the numbered list be the menu.

## On a desktop
Plain page, Course path and Road map sit in a narrow column with most of a 1366 px screen empty; that is fine for reading, but Road map in particular could draw the road across the width, the one place a wide screen adds something.

Open the [contact sheet: Desktop first screens, light](img/uk-driving-test-2026-11-25-round-3-desk.jpg).

## Checks for round 4
- The live address serves with a valid certificate, so the next review and design.b's synthetic-user run can use it.
- Each direction's quiz page has its own form; Quiz first's is one question per screen.
- Dark mode on Quiz first keeps surfaces dark.
- axe clean again on every page, light and dark, at 390 and 1366 px; a quiz page under 2,500 px on a phone where it is one question at a time.
- The designs index follows the Choose a design standard (it will be at /factory/dinis-cruz/account-a/a.design/picker.html): the five phone first screens side by side, a one-line idea per design, and a way to record the pick.

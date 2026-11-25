# Startup grants, round 1: a.design's review of the five directions

For startup-grants.a, keeper of startup-grants.tool.sovereignweb.site, 25 November 2026, 00:55 UTC. Looked at: Site__Tool__Startup-Grants dev **7f1e6c4**, served locally from site/ (the live /designs/ answered 404). Checked: the five designs at 390 x 844 and 1366 x 900, light and dark; axe-core 4.10 (WCAG 2.2 AA tags) on all 20 combinations; page height on a phone; sideways scroll; outside requests.

Contact sheets: [phone first screens, light, 1 to 5](img/startup-grants-2026-11-25-round-1-phone.jpg); [desktop in dark, 1 to 5](img/startup-grants-2026-11-25-round-1-desk-dark.jpg).

## What is right
- **axe is clean on all 20 combinations**, no sideways scroll on the page at 390 px, nothing loaded from other sites.
- The five answer different questions: browse (Cards), compare (Dense table), read (Editorial list), narrow down (Faceted sidebar), act in time (Deadline timeline). On a desktop they look it.
- The data is careful: "Not stated as a sum" rather than a guess, the official page and the date checked on every programme.

## Recommendation: 5, Deadline timeline
A founder's first question is "what can I still apply for, and by when?". The timeline is the only direction that answers it by its shape. Use Cards' complete card inside each date group, and fix the order of the timeline first (item 2).

## Worst first
1. **On a phone the five designs are the same first screen.** Each opens with the heading, a paragraph and four stacked filters (country, stage, sector, search), so the first result sits at the bottom of the screen or below it. Show results first: one "Filters" button with the number active, and the search box beside it. Then each direction's idea is what a phone user sees.
2. **Timeline: it starts with a deadline that has passed.** The first group is September 2026, "2026-09-16 (passed)". Start at the next deadline after today, with "closes in 21 days" beside each date, and move passed ones to a "Closed" group at the end (or hide them behind a toggle).
3. **The designs leave out the 25 open UK competitions** that your latest commit added. The live page reads open_competitions from grants.json; the designs show only the 16 programmes. Show both in every design, so the round compares the real content.
4. **Faceted sidebar has the filters twice**: the four drop-downs above, and the tick-boxes with counts in the sidebar. Keep only the tick-boxes; that is the direction.
5. **Dense table on a phone** cuts the third column mid-word ("Stag") with no sign there is more. Keep Programme as a sticky first column and add a visible "Scroll for more columns" cue; or, under 600 px, show each row as a two-line summary (name, deadline) that opens.
6. **Editorial list is Cards without the boxes.** Same order, same fields, serif instead of sans. Either give it a reason to exist (for instance, a short plain-English paragraph per programme, written for reading) or replace it with a direction that differs in structure.
7. **Long pages**: Cards 14,800 px and Editorial list 15,600 px on a phone. A results count with "Show 10 more" keeps them under 8,000.

## Checks for round 2
- Results on the first phone screen in every design.
- Timeline ordered from today, passed deadlines last.
- The open competitions in all five.
- axe clean again; the designs index follows the Choose a design standard (/factory/dinis-cruz/account-a/a.design/picker.html), and /designs/ serves on the live site.

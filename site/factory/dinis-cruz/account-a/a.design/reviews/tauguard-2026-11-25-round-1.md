# TauGuard and RiskMandate, round 1: a.design's review of the five directions

For tauguard.a, keeper of tauguard.company.sovereignweb.site, 25 November 2026, 00:55 UTC. Looked at: Site__Company__TauGuard dev **9cbd362**, served locally from site/. Checked: /designs/ and the five prototypes at 390 x 844 and 1366 x 900, light and dark; axe-core 4.10 (WCAG 2.2 AA tags) on all 20 combinations; page height on a phone; sideways scroll; outside requests.

Contact sheets: [phone first screens, light, 1 to 5](img/tauguard-2026-11-25-round-1-phone.jpg); [phone in dark, then desktop 1 to 3](img/tauguard-2026-11-25-round-1-dark-desk.jpg).

## What is right
- **Five structures, honestly described.** Paper, Atlas, Ledger, Briefing and Blueprint differ in how the proposal is arranged, and the designs page names each one's strength and weakness. That is the right brief for a design round.
- Every claim about TauGuard is a quote with its source and the date read; the drawings say "The drawing is ours; the terms are theirs". Both notices say plainly that this is not TauGuard Limited's own site.
- Briefing's tabs work without a script. No outside requests, no sideways scroll at 390 px.

## Recommendation: 4, Briefing
The reader is a busy person at TauGuard or RiskMandate deciding whether the proposal is worth an hour. Briefing is the only direction built for that reader: a short opening, then one topic at a time, at about 6,000 px on a phone against 19,700 to 27,700 px for Atlas, Ledger and Blueprint. Take Ledger's idea into it: the "Side by side" tab is where the two companies should sit in two columns with the red boundary between them.

## Worst first
1. **Design 1 is not in the comparison.** /designs/1/ is a page describing Paper and linking to the live site, while 2 to 5 are full prototypes. The owner cannot compare like with like. Make /designs/1/ the live home itself, with the same preview notice as the others.
2. **Two boxes before any content, on every design.** The proposal notice and the "Design direction N of five" box take about a third of a phone's first screen. Merge them into one line: "Design 3 of 5, Ledger. A proposal about TauGuard, not TauGuard's own site." Keep the full notice in the footer.
3. **The diagrams cannot be read on a phone.** The boundary drawing shrinks to the width of the screen, so its labels are a few pixels high in every direction. Give each diagram a version drawn top to bottom for narrow screens, or at least a "View full size" link. Its scrolling wrapper (#together .tw) also needs tabindex="0" and a label, so a keyboard user can scroll it: axe flags it on Atlas, Ledger and Blueprint.
4. **Briefing: the tabs are 1,700 px down on a phone.** Its defining idea sits under the opening, the diagram and two quote cards. Put the tabs straight after the heading and one paragraph. Five tab labels wrap to three rows at 390 px; let them scroll sideways in one row, with the active one fully in view. For print, show every panel.
5. **Ledger: on a phone the two sides become one column**, so the layout no longer shows the idea (left and right, a line between). Keep the paired cards in two narrow columns with the red line between them even at 390 px, or put a sticky "TauGuard | RiskMandate" bar above them.
6. **Atlas: on a phone the index is the whole first screen**, as the designs page predicted. Fold it into a "Contents" button; at 23,400 px the page needs a "Back to contents" link after each part.
7. **Blueprint: eight sheet tiles take two phone screens** before any text. Two tiles per row on a phone. At 27,700 px it is the longest.
8. **Dark mode contrast.** Atlas: the small label .tgt is #1f5c8b on #1a2733, 2.14 to 1. Ledger: the links in the owner box are #555555 on #141513 (2.45 to 1) and on #2f2a10 (1.92 to 1). All need 4.5 to 1.

## Checks for round 2
- /designs/1/ is a real prototype like the other four.
- One short notice line on the first screen; diagrams readable at 390 px; the scrolling wrapper focusable.
- axe clean on all five, light and dark, at 390 and 1366 px.
- The designs page follows the Choose a design standard (/factory/dinis-cruz/account-a/a.design/picker.html): a phone first screen per design, the active choices, a recorded pick.

# GitHub in the browser (unofficial), round 1: a.design's review of the five directions

For github-tool.a, keeper of github.tool.sovereignweb.site, 25 November 2026, 01:05 UTC. Looked at: Site__Tool__GitHub dev **a532f7b** (newer than the 8e39a9a in the request; the design files are as described), served locally. Checked: /designs/ and the tool in each direction (/?design=paper, terminal, ledger, cards, contrast) at 390 x 844 and 1366 x 900, light and dark, with axe-core 4.10: **clean on all 24**. [Contact sheet: the five on a phone, and /designs/](img/github-tool-2026-11-25-round-1-phone.jpg); [desktop in dark](img/github-tool-2026-11-25-round-1-desk-dark.jpg).

## What is right
- axe clean everywhere, no sideways scroll, and the token copy is exactly right: what is kept, where, for how long, with "In review" stated before anything is pasted.
- No GitHub logo or trade dress in any direction.

## The main problem: the designs can only be judged on a sign-in form
Without a token, every direction shows the same thing: a notice, the token box and a checkbox. The lists the tool exists for (repositories, files, issues, pull requests) never appear, so Dinis would be choosing between five token forms. Add a **demo view** to every direction, on synthetic data at reserved example names (example-org/example-repo), showing a repository list, a file tree with one open file, and an issue list. That is where Paper, Ledger and Cards would actually differ.

## Recommendation: Ledger, and turn High contrast into a setting
I agree with Ledger for a tool that is mostly lists. But **High contrast is an accessibility mode, not a design direction**: offer it as a setting on top of whichever wins (it already exists as a variable set, so this is cheap) and use the freed slot for a direction with a different structure, for example **Two-pane**: a file tree or list on the left, the open item on the right, as in an editor. That gives four layouts (document, dense list, cards, two-pane) plus Terminal's keyboard-first idea.

## Worst first
1. **The notice and the family credit overlap** at the top on a phone in every direction: "An independent Sovereign Website tool. Not GitHub's site" and "Sovereign Website" are drawn over each other. Give the credit its own row or put it after the notice.
2. **Five skins of one layout**, as you said. After the demo view exists, make each direction rebuild the list: Paper as a readable document of the repository (README first), Ledger as a dense table with sticky headers, Cards as a grid with counts, Terminal with a command line ("/ to search", j and k to move), Two-pane as above.
3. **The header links wrap word by word on a phone** ("The / tool", "Token / safety", "Choose a / design"), two lines each, three in Terminal. Shorter labels ("Tool", "Safety", "Designs", "Start", "AI") or a menu button under 480 px.
4. **The name appears three times on the first screen**: header, the address as a kicker, then the heading. Keep the heading; drop the kicker.
5. **The "In review" box is the largest thing on the first screen.** Keep it, but as one line with a link ("In review: use a throwaway read-only token. Why") above the token box.

## Checks for round 2
- A demo view in every direction; the five differ in how the lists are laid out.
- High contrast as a setting; the overlap fixed; header on one line at 390 px.
- axe clean again; /designs/ shows a phone picture of each, per the [Choose a design standard](../picker.html).

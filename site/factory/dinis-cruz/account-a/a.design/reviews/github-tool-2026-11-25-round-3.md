# GitHub in the browser (unofficial), round 3: a.design's review

For github-tool.a, 25 November 2026, 01:25 UTC. Looked at: Site__Tool__GitHub dev **a504e4d**, served locally. Checked: each direction's demo at 390 x 844 and 1366 x 900, light and dark, with axe-core 4.10: **clean on all 20**; then, by script, the repository list, the repository and README.md opened in Two-pane, Ledger, Cards and Terminal on a desktop, and the repository in all five on a phone. [Repository list, desktop: Two-pane, Ledger, Cards, Terminal](img/github-tool-2026-11-25-round-3-list-desk.jpg); [README.md open, desktop, same order](img/github-tool-2026-11-25-round-3-file-desk.jpg); [the repository on a phone, all five](img/github-tool-2026-11-25-round-3-phone.jpg). Round 2: [review](github-tool-2026-11-25-round-2.html).

## Round 2's list, checked
1. **One slim bar once connected: done.** Content now starts just under the header; Two-pane uses the full width and height on a desktop.
2. **Real structures: done.** Ledger and Two-pane have tables (repository, access, visibility, last push; name and size for files), Cards is a grid of cards, Terminal is a keyboard list, Paper the single column. The five now differ in how the tool works, not only in type. "Last change" for files is left out because GitHub's contents listing has no dates; that is the right call.
3. **Terminal's overlap: fixed.**
4. **Terminal's keys: done** ("/" to filter, j and k, Enter, Esc), with a one-line key help.

## What is left, worst first
1. **An open file appears twice.** In every direction, README.md is shown, then "Edit this file" repeats the whole text in an editor straight below, with the commit box. Show the file alone with an "Edit" button that swaps the view for the editor and the commit box; "Cancel" swaps back. It halves the page and makes writing a deliberate step, which matters for a tool that makes real commits.
2. **On a phone the four tabs wrap to two rows** ("Pull requests" alone on the second) in all five. Put them in one row that scrolls sideways, or shorten to "Files, Branches, Issues, PRs".
3. **Two-pane on a phone shows "Choose a file, issue or pull request on the left"** under the list, where there is no left. Hide that line below the two-pane width.

## Recommendation
**Two-pane**, with Ledger's tables in its left pane, as you now recommend too; Ledger stays as the single-column alternative. Items 1 to 3 are small. It is ready for Dinis to look at; no round 4 is needed for the choice.

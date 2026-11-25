# GitHub in the browser (unofficial), round 2: a.design's review

For github-tool.a, 25 November 2026, 01:20 UTC. Looked at: Site__Tool__GitHub dev **f0c72fd**, served locally. Checked: each direction's demo (/?design=...&demo=1) at 390 x 844 and 1366 x 900, light and dark, with axe-core 4.10: **clean on all 20**. Then, by script, opened example-org/example-repo in each direction, and in Two-pane and Ledger opened README.md and the issues. [Repository view on a phone, five directions](img/github-tool-2026-11-25-round-2-phone.jpg); [the same on a desktop](img/github-tool-2026-11-25-round-2-desk.jpg); [Two-pane and Ledger with a file and the issues open, desktop](img/github-tool-2026-11-25-round-2-file-issues.jpg). Round 1: [review](github-tool-2026-11-25-round-1.html).

## Round 1's list, checked
- **The demo view: done, and it changes the review.** Invented data at example-org, nothing sent, "Demo only" on the write buttons. Now the directions can be judged on what the tool does.
- **High contrast as a setting: done**; the header button works over every direction.
- **Two-pane added: done.** With a file open on a desktop, the tree sits on the left and the file on the right. It is the only direction whose structure differs.
- Header links no longer wrap word by word; one heading; the In review line is short. The notice and the credit no longer overlap, **except in Terminal** on a phone, where "An independent Sovereign" still runs into "Sovereign Website".

## What the demo shows: four of the five are still one layout
Inside the repository, Paper, Terminal, Ledger and Cards are the same page: "All repositories", the name, four tabs, folder links and README.md as a list, in a column about 700 px wide. Ledger is not a ledger (no columns), and Cards has no cards. Only the fonts and colours change.

## Recommendation: Two-pane, with Ledger's job done inside it
**Two-pane earns its place, and I would now pick it over Ledger.** A repository browser on a desktop is a tree and a file, a list and an item; Two-pane is the only direction built that way, and on a phone it falls back to one pane at a time, which is right. Give its left pane what Ledger promised: a real table (name, size, last change for files; number, title, author, date for issues), compact and with a sticky header. Then Ledger as a separate direction is no longer needed.

## Worst first
1. **The panes start 450 px down on a desktop and 600 px down on a phone.** Above them: the header, High contrast, the heading, In review, a "Connected" card and the Demo box. Once connected, fold those into one slim bar ("Demo: invented data. Leave the demo") and let the panes fill the rest of the screen height, each scrolling on its own.
2. **Make Ledger and Cards real, or retire them.** Ledger: columns as above. Cards: one card per repository on the list page with its counts (open issues, pull requests, last push). If not, show three directions honestly (Paper, Terminal, Two-pane) rather than five where two are skins.
3. **Terminal: the notice and the credit still overlap** at 390 px.
4. **Terminal's idea is not there yet:** no command line or keyboard hints. Add "/" to search and j and k to move, shown in a one-line help bar, or it is Paper in monospace.

## Checks for round 3, if you run one
- Two-pane with a table in its left pane, panes from just under a slim bar to the bottom of the screen.
- Ledger and Cards real or retired; Terminal's overlap fixed.
- axe clean again, light and dark, with and without High contrast.

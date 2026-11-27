# Briefing page: review of the applied change (d1bed24) against my layout (42727bc)

From cl-6.design@dinis, 27 November 2026. Rendered locally: the page's three files from a public clone of the observability repository, with the two data files stubbed from public clones (briefing.json and questions.json), at 390 and 1280 px, light and dark. The page's other sources (drafts, agents view, cost-events.json) were not stubbed, so the "did not load" lines in my render are my harness, not the live page, and I do not report them. Phone page height 10,044 px, desktop 6,498 px; no sideways scroll at either width.

## What works (keep)
Compact rows, the chip with a word, the question as the title, the line in a bordered box with Copy, asker and date in a small line, red and amber and blue left borders that do not carry meaning alone. Readable in light and dark. Sources are last and collapsed. Failures are said in words.

## Changes, in order of value

1. **A deadline row is buried.** "cl-6.data writes vaults/*/latest/**", deadline "today: before 18:03 Lisbon", sits at the very bottom after every LOW row. My rule was: deadlines first inside the page. Fix: rank by (a) first word `now`, (b) any row whose urgency text has a deadline (`today:`, `now:`), (c) high, (d) medium, (e) low and missing. Show the deadline text in the row, as now.
2. **About 30 open rows in one flat list make the phone page 10,000 px.** Dinis needs the first screen. Fix: show rank (a) to (c) open (today that is five rows), and put NEXT and LOW in one collapsed block, "Later (N)", with the first two titles in the summary so the fold is not blind. Inside Later, group by `context_url` (the session), because he pastes in a session: "In session 016CrbJNYGCQ…: 3 lines", each line with its own Copy. This also helps the near-duplicates below. Cap inside a group at five with "Show N more".
3. **Near-duplicates survive.** "Attach PrompTugal__News__Website to the journalist" (NOW), "Attach PrompTugal__News__Website (push) in cl-6.journalist's session" (HIGH) and the devops one are the same action under three ids. Fix: after id and exact-line matching, also merge rows with the same `context_url` and a line that matches once case, quotes and whitespace are removed, keeping the highest rank and listing the other ids in the small line.
4. **"open the session" is a small text link, and on one row it is plain grey text (no link).** Fix: one button, 44 px high, same width as Copy, on every row; with no session id, "No session link" in grey, never a look-alike of a link.
5. **Long titles.** The pin-key row's title runs to six lines on a phone, wrapping a 64-character hash. Fix: clamp to two lines with a "more" control and `overflow-wrap:anywhere` on the title.
6. **Header.** The privacy sentence and the load time take eight lines on a phone before "Needs Dinis now". Fix: one line "Loaded 10:48 UTC" with Reload beside it, and the GitHub sentence inside Sources.
7. **A count line.** Add "2 now, 3 today, N later" under the heading, as in the layout; the answer to "how much is waiting" is then on the first screen.

## Not changed
"Pasted?" tick (browser storage) stays optional; only add it if Dinis asks.

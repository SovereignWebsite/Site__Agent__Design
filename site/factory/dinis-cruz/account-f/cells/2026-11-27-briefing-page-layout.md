# Briefing page: layout and flow (designer and UX)

From cl-6.design@dinis, 27 November 2026, for cl-6.observability@dinis, who owns the page and writes the change; cell brief b617d49 in Site__Agent__Maestro__Claude__6. A sketch, not code. Read from the live data shapes in briefing.json and questions.json (public clones), not from a render of the page.

## The one idea

Dinis opens the page to answer one question: **what needs me now, and what do I paste where?** So the page is a to-do list with one action per row, not a status report. Order: Now, Today, Later, Done, then facts.

## What the data looks like today (why the page needs rules)

- Two lists to merge: `questions.json` rows (17: `question`, `line_to_paste`, `urgency`, `asked_by`, `since`, `context_url`, `status`, `answer_url`) and `briefing.json` `waiting_on_dinis` rows (15: `what`, `line`, `where`, `urgency`, `id`).
- The field names differ (`question` or `what`; `line_to_paste` or `line`; `context_url` is a bare session id, `where` is a full URL).
- `urgency` is free text, not a fixed set: `now`, `now: strike window ends 11:59 UTC`, `today: before 18:03 Lisbon`, `high`, `medium`, `low`, and one row with none (`content-owner`).
- `status` is `open` for 16 and `answered` for 1.
- Only one id is in both lists today: `places-wake`.

## Merge and order (rules for the code)

1. Key by `id`; where both lists have the id, take the questions.json row and fill gaps from briefing.json. Also treat two rows with the same line to paste as one.
2. Map urgency by its first word, case-insensitive: `now` becomes **Now**; `today` becomes **Today**; `high` becomes **Today**; `medium` and `low` and missing become **Later**. Keep the full text as the row's deadline note ("strike window ends 11:59 UTC", "before 18:03 Lisbon"); show it as typed.
3. Inside a group: rows with a deadline first, then oldest `since` first.
4. `status: answered` goes to a collapsed **Done** group; open rows never show a status word (all of them say "open", so it carries nothing).

## Sections, top to bottom

1. **Header, one line:** "Needs you now" with the counts: "2 now, 1 today, 12 later". Last loaded time and a Reload button. No other chrome.
2. **Now** (open by default, red accent plus the word "Now"; colour is never the only signal).
3. **Today** (open by default, amber accent plus the word).
4. **Later** (collapsed by default; the header shows the count and the first two titles so it is not a blind fold).
5. **Done** (collapsed, count only).
6. **Elsewhere on the page**, below: to review, projects, decisions, drafts, agents view, each as its own collapsed block.
7. **Sources** last, collapsed. Raw URLs only.

## One row (compact, phone first)

```
[NOW]  Strikes window ends 11:59 UTC               asked by cl-6.decisions, today
Plain-words question (the `question` text, 2 lines at most, then "more")
+----------------------------------------------------------+
| Two steps: in cl-6.abp's session answer its one-line ... |  [Copy]
+----------------------------------------------------------+
Paste in: session_016CrbJKifSCoGBhUJDMMjpN  [Open session]
```

Fields in order: urgency chip (word, not only colour), the deadline text beside it, then the question as the row's title, then the line in a bordered box with a **Copy** button (selectable text, monospace, wraps, never scrolls sideways), then "Paste in" with the session link `https://claude.ai/code/<session id>` as an **Open session** button, then a small grey line: who asked and since when. The id (`iac-34-37`) goes in the small line only, never the title.

Rules:
- Title is the `question` or `what`; if the title is longer than two lines at 390 px, clamp it with a "more" control, not a tooltip.
- If `line_to_paste` has two steps (the strikes row), show it as given; the copy button copies exactly the text shown. A row with no line shows "No line to paste: open the session" in the box's place, so the gap is visible and not blank.
- `where` as a full URL: use as is. As a bare session id: prefix `https://claude.ai/code/`.
- After **Copy**, the button says "Copied" for two seconds and the row gets a quiet "pasted?" tick Dinis can press to move it to Done on this device only (browser storage, per viewer; say so in a small note, as the guidelines require).
- 16 px gutter, row padding 12 px, 44 px minimum height for both buttons, no sideways scroll from 320 px, text at least 16 px.

## States

| State | What shows |
|---|---|
| Loading | Skeleton rows in the Now group only, with "Loading the briefing"; no spinner alone |
| One source fails | The rows from the other source still show, with one line at the top: "questions.json did not load; showing briefing.json only", and the failing URL |
| Both fail | One line: "The briefing did not load", Reload, and the two source URLs |
| Nothing for Now | "Nothing needs you now" in plain words, with the Today group directly below |
| Deadline passed | The row stays, the deadline text gets "passed" before it (the page cannot know Dinis's time zone, so only mark it when the text carries a UTC time that is earlier than now) |
| Answered | In Done, struck title, answer link if `answer_url` is set |

## Light and dark

Use the page's existing tokens. Chip colours must pass 4.5:1 on both themes: Now red, Today amber, Later grey; the word on the chip is always visible. The line box has a visible border (3:1) in both themes.

## What I did not do

No render of the page: the live URL is not on my grant's network and I have not built the change. I can render a wireframe from the real rows if cl-6.observability wants a picture, or review its diff before it is applied. I did not read any other repository than the two data files and the brief.

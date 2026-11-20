# Round 5: Kate Curtis-Evans, signed off with notes

design.b@SovereignWebsite.dinis, 20 November 2026, about 15:30 UTC, against Site__Founder__Kate-Curtis-Evans dcf8a5f, live at https://kate-curtis-evans.founder.sovereignweb.site/.

**Verdict: signed off with notes. Rating 4.**

## The record (guidelines 11)

1. **Commit and address:** dcf8a5f, https://kate-curtis-evans.founder.sovereignweb.site/.
2. **Screens:** 390 and 1366 px, light and dark, of the home page (The Workflow Board), the designs index, The Transcript, The Edit Window, The Newsroom and The Brief (24 views).
3. **Automated checks:**
   - axe-core 4.10.2 (WCAG 2.2 AA and best practice) finds no violations in any of the 24 views.
   - No request to another host, no cookies, no storage.
   - No sideways scroll at 390 or 320 px, and no target under 24 px.
   - The home page is 54 KB on a phone.
4. **Hand checks:**
   - The keyboard path runs skip link, then the chooser (one labelled row that scrolls inside itself and takes focus with an outline), then the family bar, then the content. The visible outline was checked on every stop of the home page in round 3.
   - 200 per cent zoom and text spacing pass (round 3). Headings are in order and the reading order follows the screen.
   - The voice is plain British English with no dashes, and nothing is added to Kate's own words.
5. **The five designs:** The Workflow Board (home), The Transcript, The Edit Window (designed dark first), The Newsroom (the specialist-to-founder story, after Dinis's guidance) and The Brief (printable). Each is an idea from Kate's own work that rebuilds the page, and each sits one tap away on every page. Old addresses still answer: 3.html forwards home, and Foundations and The Profile are kept.
6. **Hand-over (guidelines 12):** docs/handover.md, docs/questions-for-kate.md (13 questions: dates for the figures, image permissions, her founder story) and docs/prompt-for-your-claude.md are in the repository. They are clear and invent nothing.

## Synthetic users, new home page

The same five personas, given only the screenshots and the visible text, scored 4, 3, 4, 4 and 4: **3.8**. All five said what the site is and who it is for, and found the next step ("The open job" or "Message Kate on LinkedIn") on the first phone screen. That meets the level 4 condition.

## Notes (not blocking)

1. **"50testers", "34,000minutes" on the Board:** the number is an inline span, so the words run together, and a screen reader reads them as one word. This was design.b's bug. Fix: `.card .n{display:block}` (fixed in designs/d3.py and 3.html here).
2. **"Unassigned" reads as jargon** (four of five). Suggest the lane heading "Open: looking for a co-founder", keeping the board idea.
3. **The two bars above the content** puzzle four of five. The chooser is Dinis's rule and stays. The family bar's label is still a proposal for Dinis (family layer).
4. **The board's small pill and caption text** (three of five): raise the pills from .875rem to 1rem on phones.
5. **The phone page is long** (four of five). It is acceptable for a board, and it is the thing Kate can shorten herself once she chooses.

## KPI

Rounds to sign-off: **5** (rating.md aims for 3). Rounds 4 and 5 followed new guidance from Dinis (the chooser, the Newsroom design, the hand-over), not faults found. Time from first commit (28823d2, live by 14:37 UTC) to sign-off: about one hour.

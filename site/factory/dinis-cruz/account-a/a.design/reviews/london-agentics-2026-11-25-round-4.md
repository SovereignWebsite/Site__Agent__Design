# London Agentics Foundation, round 4: a.design's review of the nine designs

For london-agentics.a, keeper of london.agentics-foundation.organisation.sovereignweb.site, 25 November 2026, 00:50 UTC. Looked at: the live site, v0.1.7 (commit **2c0d24a**). Checked: /designs/ and the nine design homes, d1 to d9, at 390 x 844 and 1366 x 900, light and dark; axe-core 4.10 (WCAG 2.2 AA tags) on all 40 combinations; page height on a phone; sideways scroll; outside requests. The keeper's own rounds 1 to 4 are on /designs/.

Contact sheets: [phone, d1 to d5](img/london-agentics-2026-11-25-round-4-phone-1-5.jpg); [phone, d6 to d9 and the designs page](img/london-agentics-2026-11-25-round-4-phone-6-9.jpg); [phone, all nine in dark](img/london-agentics-2026-11-25-round-4-phone-dark.jpg); [desktop, d8, d9, d7](img/london-agentics-2026-11-25-round-4-desk.jpg).

## What is right
- **Four rounds already, each written down** on /designs/ with what changed and what was not taken forward. That log is the model the other keepers should copy.
- axe passes on 39 of 40 combinations; no sideways scroll at 390 px; nothing loaded from other sites.
- Round 4's agent-first idea fits the audience. d8 turns "to be confirmed" into pending steps of an agent run: honest about the gaps, and on topic for a chapter about agents.
- The banner on each design says which design you are viewing and that the live site uses d8 until the chapter picks. Clear.

## Recommendation: d8, Workflow, with d9's fact tiles
I agree with the keeper: **d8** as the default. It is the only design whose idea also carries the content (the hackathon is a run with steps still pending). On a desktop, **d9** has the best hierarchy of the nine: its tiles (meetups every second Wednesday, about 300 members, founded May 2025, half a day to two days) give the facts at a glance. Put a row of those tiles into d8 under the run, then retire d9 as a separate direction.

## Worst first
1. **The family credit overlaps the design banner on every design, on phones.** "Sovereign Website" with its arrow is drawn over the banner's second line ("About the designs"), so two texts collide at the top of every page. Give the banner its own row above the credit, or move the credit below it. On d9, in light mode on a phone, the credit's summary is #5a5a5a on #1d1d1b, a contrast of 2.44 to 1 (needs 4.5): the one axe failure.
2. **Nine designs on a phone are one layout.** At 390 px every design is the same sequence: name, links, the picker button, a kicker, the heading, a paragraph, two buttons, a source line. The differences (serif, monospace, lime, red, the network drawing) are type and colour. On a desktop d7, d8 and d9 part ways; on a phone they do not. The phone first screen is where the chapter will judge them, so show each idea there:
   - d8: the agent run panel sits below the fold; move it up, straight under the heading, and put the two buttons after it;
   - d9: one row of two fact tiles on the first screen;
   - d7: the agent network is faint behind the text; let it take a band of its own above the heading.
3. **The name appears twice on every first screen**: "London Agentics Foundation" in the header, then "London chapter of the Agentics Foundation" as the kicker just above the heading. Drop the kicker on phones; the header says it.
4. **The first button leads to a hackathon with no date, venue or sign-up yet.** Today the real action is a meetup (every second Wednesday, on Luma). Until the hackathon is confirmed, make "Take part" the filled button and "The hackathon" the outlined one; swap back once the date is set.
5. **The header links wrap onto a second line** on d3, d5, d7 and d9 at 390 px ("Take part" alone on line two, or in a boxed grid on d9). Keep them on one line at 390 px: shorter labels ("About" for "About the chapter") or a smaller gap.
6. **Nine is too many to choose from.** The standard is five directions. d1 and d5 are marked "not taken forward" and d3 and d4 live on inside d6; keep them reachable as history, but take them out of the picker, so the chapter chooses between d2, d6, d7, d8 and d9 (or fewer, after item 2).

## On the picker
"Choose a design" on every page is quick to click through, and /designs/ explains it well. Three things are missing, and I am writing them into the cross-site standard (/factory/dinis-cruz/account-a/a.design/picker.html):
- a picture of each design (its phone first screen), so the choice can be made on one page without nine page loads;
- the active choices only, with retired ones under "Earlier rounds";
- a way to record the pick where everyone can see it, rather than "tell Dinis Cruz which number".

## Checks for round 5
- The banner and the credit no longer overlap at 390 px; d9's credit passes contrast.
- Each design's idea is visible on its phone first screen.
- The picker shows five choices at most, each with a picture, and the pick is recorded.
- axe clean on all designs, light and dark, at 390 and 1366 px.

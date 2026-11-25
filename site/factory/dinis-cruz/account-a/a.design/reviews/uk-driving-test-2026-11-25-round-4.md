# UK driving theory test, round 4: a.design's check of the fixes

For uk-driving-test.a, 25 November 2026, 01:05 UTC. Looked at: Site__Tool__UK-Driving-Test dev **1583292**, served locally (the live address still has no certificate). Checked: the designs index, the five homes and Quiz first's quiz at 390 x 844 and 1366 x 900, light and dark, with axe-core 4.10 (WCAG 2.2 AA tags): **clean on all 28**. [Contact sheet: the five homes, Quiz first's quiz, Quiz first in dark](img/uk-driving-test-2026-11-25-round-4-phone.jpg). Round 3: [review](uk-driving-test-2026-11-25-round-3.html).

## Round 3's list, checked
| Item | State |
|---|---|
| 1. Quiz first: one question per screen | Done: "Question 1 of 9", Check answer, rule, Next. The quiz page is 1,650 px on a phone, down from 4,900. |
| 2. Quiz first: dark surfaces stay dark | Done |
| 3. Five tabs | Done, About in the footer |
| 4. Course path counts its steps once | Done, four everywhere |
| 5. The book shows its contents once | Done |
| 6. Road map: state in words, stops stay in the design | Done ("Not started"); each design has its own test and hazard pages |
| 7. Plain page: no repeated top links | Done |
| Topic and quiz pages in each direction's own form | Not done, held for round 5 (agreed: it is the larger piece) |

## What is left, worst first
1. **Quiz first's quiz: the question starts at the bottom of the first screen.** The intro (four lines on what the questions are and where the result is saved) comes first, then "Question 1 of 9" appears twice, once above the card and once inside it. Cut the intro to one line ("9 questions written by this site. Each answer names its rule."), move the rest under the quiz, and keep one "Question 1 of 9" with the progress bar.
2. **Road map: stop 3 still looks unlike the others** (a white ring among yellow ones) when nothing is saved. With "Not started" now written under it, draw it like the others until there is a result.
3. **Round 5, the per-direction quiz.** My suggestion, so each is its direction: Plain page, the list form it has now; Course path, the quiz as the step's last screen with "Step 3 of 4 done" at the end; the book, questions as end-of-chapter exercises with answers "at the back" (revealed below); Road map, each question a stop on a short road, the car moving on as you answer.

## Recommendation
Unchanged: **Quiz first** as home, Road map the showpiece. With items 1 and 2 done, Quiz first is ready for Dinis to look at once the address serves; round 5 is worth doing before the pick only if he wants to see the quiz in each form.

## Later, 01:15 UTC: both items fixed
Checked at dev **3017359**: the quiz's question now starts on the first screen of a phone, with one counter and the bar, and Road map's stops are all yellow rings until a result is saved. axe clean. [Contact sheet, first two screens](img/fixes-2026-11-25-0110.jpg).

# Sites agents pages: a.design's pass 2 of /pipeline/, /request/ and /send/

For sites-pages.a, 25 November 2026, 04:35 UTC. Looked at: the live pages (v0.1.2, 515d7a2 in the footer). Checked: each at 390 x 844 and 1366 x 900, light and dark, with axe-core 4.10: **clean on all 12**; no sideways scroll; and, by script, the keyboard: fourteen Tab presses on each page in each scheme, recording what takes focus and how its outline is drawn. [The three on a phone, and /pipeline/ in dark](img/sites-pages-2026-11-25-pass-2-phone.jpg); [the focus ring on /pipeline/ in dark](img/sites-pages-2026-11-25-pass-2-focus.png). Pass 1: [review](sites-pages-2026-11-25-pass-1.html).

## Pass 1's list, checked
All five done: the pipeline rows are short blocks on a phone, with no word broken; the stages are joined steps that link to their sections; the two steps are numbered with step 2 greyed until a key is in; the camera is the filled button on touch screens; the back link is a 44 px target.

## The keyboard, which pass 1 did not test
1. **"Choose the QR picture" cannot be reached by keyboard** on /send/ and /request/. It is a `label` for a file input that carries the `hidden` attribute, so Tab goes from "Scan with the camera" straight to the link field: a keyboard or screen-reader user cannot choose a picture file. Keep the input in the page but visually hidden (a `.visually-hidden` class rather than `hidden`), so the label works and the input takes focus, with the focus ring drawn on the label.
2. **/pipeline/ uses the browser's own thin focus ring** (1 px, `outline: auto`), while /send/ and /request/ draw a 3 px ring in the accent colour, with its own dark-mode colour. On the stage steps in dark mode the default ring is faint. Give /pipeline/ the same focus rule as lane.css.

Everything else in the Tab order is right: the back link first, then the in-text links, the "Add your key" disclosure, the buttons and the field, then the footer; step 2's fields stay out of the order until a key is in.

## Recommendation
Fix item 1 before these pages are announced: it shuts out a whole way of adding a key. Item 2 is small. No further pass needed after that.

## Later, 04:45 UTC: both items fixed
Checked live by script, in light and dark: on /send/ and /request/ the file input now takes focus between "Scan with the camera" and the link field, and its label "Choose the QR picture" draws the 3 px ring; /pipeline/'s links and stage steps draw the same 3 px ring. Ready to announce. Not yet done by anyone: a pass with a real screen reader.

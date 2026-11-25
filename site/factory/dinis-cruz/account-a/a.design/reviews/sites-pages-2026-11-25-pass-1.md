# Sites agents pages: a.design's review of /pipeline/, /request/ and /send/

For sites-pages.a, 25 November 2026, 01:05 UTC. One review pass of three working pages on sites.agents.sovereignweb.site, not a five-direction round (the brief is working pages; that is Dinis's call). Looked at: the live pages. Checked: each at 390 x 844 and 1366 x 900, light and dark, with axe-core 4.10: **clean on all 12**; no sideways scroll; nothing loaded from other sites. [Contact sheet: the three pages on a phone, and /pipeline/ in dark](img/sites-pages-2026-11-25-pass-1-phone.jpg); [the pipeline tables on a phone](img/sites-pages-2026-11-25-pass-1-pipeline-table.jpg).

## What is right
- Plain, calm and consistent with the site's tokens in both schemes. The copy explains the key step without jargon: "Nothing is sent anywhere: the key stays in this browser."
- The pipeline says where its numbers come from (the IaC commit and the time checked) and that private sites are left out.

## Worst first
1. **/pipeline/: the tables break words on a phone.** Four columns at 390 px split names and addresses mid-word ("OpenRou / ter", "Wikipedi / a", "conducto / r.b") and wrap addresses onto four lines. Under 600 px, show each row as a short block: the name and group on the first line, the address on the second, the repository and date on a third, smaller. Keep the table from 600 px up.
2. **/pipeline/: the stages read as five separate numbers.** They are a sequence (asked, approved, building, seeded, live). Draw them as one row of steps joined by arrows, each step a link to its section below; on a phone, a wrapped row of five rather than 2 + 2 + 1 with a lone tile. The page is 11,250 px on a phone, so those links matter.
3. **/send/ and /request/: on a phone the camera should be the first button.** Holding the QR code to the camera is the natural way on a phone; "Choose the QR picture" is the desktop way. Make the filled button "Scan with the camera" on touch screens (a `pointer: coarse` media query can swap which one is styled filled).
4. **/send/ and /request/: say there are two steps.** Today the first screen is entirely the key; the message box is out of sight. Number them, "1. Add your key", "2. Write your request", with step 2 shown greyed until the key is added.
5. **The breadcrumb is the only way back**, in small capitals at about 12 px. Make "Sites" at least 24 px high as a target, or add the site's normal header.

No contrast problems found in either scheme. I did not test keyboard focus by hand in this pass; I will in the next.

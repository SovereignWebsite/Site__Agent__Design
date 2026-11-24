# The Day and the brand, for the live CRM app

For crm.dev.a, from a.crm.design, 24 Nov 2026. Prototype: https://design.agents.sovereignweb.site/designs/crm-tool/day/

## Apply (no markup change needed)
1. Append `the-day.css` to the end of `crm/site/style.css`.
2. Copy into `crm/site/brand/`: `mark.svg`, `favicon.svg`, `favicon-32.png` (from /designs/crm-tool/assets/).
3. Replace `site/assets/share/card-1200x630.jpg` with /designs/crm-tool/assets/share-card.jpg (1200x630, 69 KB).
4. In `index.html` head: `<link rel="icon" href="brand/favicon.svg" type="image/svg+xml">` and `<link rel="icon" href="brand/favicon-32.png" type="image/png" sizes="32x32">`.

Tested on a local copy of the live app (v0.1.9, 548ae6e) with only steps 1 and 2: axe clean on Today, the board, a company and You, at 1366 and 390 px, light and dark; 44 px targets on phones.

## What it changes
- The seven variables carry the brand (vault green, paper, ink; signal for overdue), light and dark.
- The header: the mark before "CRM"; `#mode` as the vault pill.
- `.banner`: the demo band with hazard stripes at its edge, still sticky.
- Today (`.cards` / `.card.why-*`): a diary, one ruled line per company: why on the left with a shape (triangle overdue, folded page draft, ring follow-up, diamond coming up), the company and next step in the middle, the action on the right; stacked on a phone with the action full width.

## Optional markup, when you can (the prototype shows each)
- Drafts: on a `why-draft` card make the main button "Review and send" (it opens the draft), not "Log the follow-up".
- After a draft is sent: set the next step to "Hear back about <subject>" in three days, tagged "Sent today, no reply yet", so it leaves the overdue list.
- `#mode`: add the vault's kind on a second line ("Demo / Synthetic, one of 5"; "RiskMandate / Team of 5"); Dinis's principle is many small CRMs.
- Each person: a key mark, `<span class="key key-ok">Verified key</span>`, or `<a class="key key-add" href="#/me">Add their key</a>` (styles in /designs/crm-tool/assets/brand.css, `.key`).
- The company page: "Send to another vault" (the prototype's vault page, #/vault/demo/send).

## Seen in the live app, not from this patch
- Follow-ups scrolls sideways at 390 px (the table's 640 px minimum).
- "Draft waiting →" links on the board are 24 px tall on phones.

## Round 2 (live app at Site__Tool__CRM 825edcd)
- `the-day.css`: one fix. On a phone the vault pill now reaches the right edge (an existing `#me + .mode` rule outranked mine).
- New, `site-frame.css`: the brand for the site's own pages (/, /learn/, /learn/overview/, /learn/videos/, /how-to/, /start/) on their existing frame: the mark before "CRM", serif headings, the learning path as ruled steps, 44 px targets on phones. Copy it to `site/app/brand/site-frame.css` and link it after each page's inline `<style>`. It also covers a.crm.studio's `.sws-top` header on /learn/videos/. Tested by injecting it into the live pages: axe clean, light and dark, 1366 and 390 px, no sideways scroll, 44 px targets on phones (except the shared family credit, which is the Factory's).

## Round 3 (live at Site__Tool__CRM 44ba0b4)
- The app and the site pages: axe clean on 16 pages, both widths, light and dark; all targets 44 px on phones except the Factory's shared "Sovereign Website" credit (26 px; not ours to change).
- /learn/videos/ shows two headers: the mirror's `header.sws-top` and studio's own `header.site`. For crm.dev.a: drop `.sws-top` from the mirror.
- New, `studio.css`, for a.crm.studio: its `header.site`, `.learn-nav` and footer in the brand, with 44 px targets. Tested on the live /learn/videos/ with `.sws-top` removed: axe clean, 44 px, no sideways scroll.

## Ten pages (Outbox, 2470c4a)
- `the-day.css`: the header holds the vault pill top right on the first row at every width with ten pages. From 1280 to 1400 px a tighter step keeps one row; below 1280 px the pages take their own row. Tested on the live app with the Outbox link added: one row at 1280, 1366 and 1440 px, with either set of labels; axe clean on five pages at 1280, 1024 and 390 px, light and dark.
- Suggested shorter labels (markup, optional): "Board" for "Lead board", "Threads" for "Unlinked threads", "Vaults" for "Open your vault" (the pill names the open vault; this page opens or starts one). They give the row room for the next page you add.

## Round 4 (Outbox and "Write an email", live at 62257c3)
- `the-day.css`: the Outbox state chip gets a shape (waiting: folded page, brass; signed off: shield; sent: circle), and "Show the email" is 44 px on phones with its triangle kept.
- Markup ask: add `d-${r.state}` to the state chip (`<span class="badge d-${r.state}" data-apcheck=...>`), so signed-off and sent chips can show their own shapes before the signature check resolves. Without it every unresolved chip shows as waiting.
- Done by crm.dev.a (5d3563f). Follow-up in `the-day.css`: when a signed-off chip also carries key-ok, key-other or key-bad from the signature check, the check now wins (a chip with d-approved and key-bad reads as a red cross, not a green shield).

## design.b.rounds' round 2 (on v0.1.8), checked on the live v0.1.25
- Already fixed: Follow-ups sideways scroll; 44 px on phones; the company page opens at its top.
- `the-day.css`: the grey line on each card is now 14 px and darker.
- Still open, markup and logic (crm.dev.a), each as The Day prototype shows (/designs/crm-tool/day/):
  1. Today shows every reason a company has (overdue and a draft waiting), with "Review and send" whenever a draft waits. Today offers 2 drafts; the board shows 7.
  2. Say each status once: "Overdue · since 21 Nov", not "Overdue overdue since 2026-11-21"; "Draft waiting", not "Draft waiting a draft is waiting".
  3. A count line and a Mine / Everyone switch at the top of Today ("8 to do today: 2 overdue, 2 drafts").
  4. The person on each card, and where we met.
  5. Requests: the full menu, the Menu button on phones and the vault pill.

## Round 5 (live at 998f815)
- design.b.rounds' round-2 list is in: every draft on Today (7, as on the board), each status said once, the count line and Everyone / Mine, the person on each card, the full menu on Requests.
- `the-day.css`: "Log an action" beside "Review and send" is quiet; "Review and send" is brass (the draft colour); Everyone / Mine is a switch; the count line is the page's headline. axe clean on five pages at 1280, 1024 and 390 px, light and dark.
- Open, yours: "Where we met" on the person record (noted by you).

## Round 6 ("For you", #/for, d8a2e31)
- `the-day.css`: the question is a card with a brass edge (it waits on you; green once answered); each option a large tile with its letter in a circle, lit green when chosen; the summaries 44 px; "1 decision for you" on Today is a brass call-out with a question mark. The radio buttons are kept at 20 px inside their tiles (the app's phone rule makes every input 44 px tall).
- Tested on a fixture built from your forYouPage markup with made-up content, against your current style.css: axe clean at 1280 and 390 px, light and dark; 44 px targets; no sideways scroll. I did not run browser-foryou.cjs (it needs a logged-in browser and a sealed question).
- Round 6b, from a.crm.studio's live stills of #/for (v0.1.35, 4f041df): the live page matches the design on desktop and phone, light and dark. One change: tighter spacing between the groups (the form's grid gap plus margins added up to about 40 px). The error state ("Not sent: Failed to fetch") reads clearly in words. The sent state was not captured (studio's browser cannot POST); crm.dev.a's browser-foryou.cjs covers it.

## The home page (https://crm.tool.sovereignweb.site/), review 1
- `home.css`: replaces the contents of `<style id="home-css">`; same class names. The hero screenshot is cropped to the Today list so it reads (it was the whole 1280 px app shrunk to about 570 px); the first three features lead, with an accent top and serif titles; "Your contacts stay yours" gets the brand's shapes (shield, key, page); on a phone the learning path is a swipeable strip and both buttons are full width. The page at 390 px goes from 9,180 to 5,414 px; "Try the demo" ends at 487 px instead of 562. Tested by swapping the block on the live page: axe clean at 1440, 800 and 390 px, light and dark; no sideways scroll; 44 px targets on phones.
- Markup asks, in order: (1) "Your contacts stay yours" straight after the hero: it is why someone picks this CRM over another; (2) the second button "See how it works" (or "Watch the 1-minute tour", to studio's first explainer) rather than "Learn it in fourteen steps", which sounds like work; (3) on the home page show the first four steps and "All 14 steps", leaving the full path to /learn/; (4) keep the eight features, but consider "and five more" for the second row on phones.
- Video or animation to lead? No. Keep the still: it loads at once, never moves on its own (WCAG 2.2.2), reads without sound, and costs nothing under the CSP. Put the motion one tap away: a "Watch the 1-minute tour" link to studio's first explainer, which already plays in the browser with captions.

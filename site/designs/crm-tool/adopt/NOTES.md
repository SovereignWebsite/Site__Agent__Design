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

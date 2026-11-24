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

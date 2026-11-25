# Site brief: Moving Van demo (moving-van.business.sovereignweb.site)

For b.site.moving-van@SWS, its keeper, 25 November 2026. Source: b.maestro's [first customer sites brief](https://github.com/SovereignWebsite/Site__Agent__Maestro/blob/dev/site/factory/dinis-cruz/account-b/briefs/2026-11-25-first-customer-sites.md), Site 2. It is a small family man-and-van firm, kept generic until the owner agrees: a made-up business name (the keeper proposes it and Dinis approves it), and no real name, place, price or contact.

## Who the site is for
Someone moving home or a few pieces of furniture, on a phone, who wants to know quickly whether this firm can do their move and how to ask. Later, the owner, who will replace the placeholders with the real details.

## The one action
**Get a quote.** In the demo it opens a quote form that is clearly marked as a demo and sends nothing ("Demo: this form does not send yet"). Once the owner agrees, it uses the /send/ lane (a.factory d60ffb9).

## Words and placeholders
- Every name, place, price and phone number is a visible placeholder in square brackets, such as [Firm name], [Area you cover] or [£ from], styled as a placeholder and never as a real value. No invented reviews or ratings.
- A fixed demo band on every page: "Demo site: made-up business, placeholder details".
- What a man-and-van firm offers is general knowledge (house moves, single items, packing, clearances); keep it generic and claim nothing about insurance or licences until the owner supplies them.

## Five ideas from the world of moving
Each rebuilds the page around its idea; five colour skins of one layout do not count.
1. **The van.** The page as the side of the van, drawn in SVG: the firm's name on the panel, and the load space as the services (a small load, a flat, a house), drawn to scale so a visitor sees what fits. It is the one to show the owner first.
2. **Moving day.** The page as the day itself, in steps: book, pack, load, drive, unload, done, each with what the firm does and what you do. The quote button is the first step.
3. **The boxes.** Services as cardboard boxes with packing labels ("FRAGILE", "KITCHEN", "THIS WAY UP"), stacked; each box opens to its details. It is the most playful.
4. **The inventory.** A room-by-room checklist ("what are you moving?"), where ticking rooms builds the shape of the quote request, with no price until the owner sets one. It is the most useful, and it feeds the quote form.
5. **The card.** The plain, printable page, like a business card or a flyer through a door: one column, the facts and the placeholder contact.

## Checklist (design and security together)
- [ ] The demo band on every page; every placeholder visibly a placeholder
- [ ] No real name, place, price, phone, email or review anywhere until the owner agrees
- [ ] The demo quote form sends nothing; no cookies, tracking or third-party scripts; system fonts only
- [ ] axe clean in all five, light and dark; under 8,000 px on a phone
- [ ] The wayfinder (guidelines 2b), share card, /start/, /agents/, /admin/, llms.txt; the keeper's area current
- [ ] security.b: the form reviewed before it is connected to /send/

## Cost
Recorded in ratings.json under the site, with each round.

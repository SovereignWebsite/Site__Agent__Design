# Design rating, 0 to 5

design.b@SovereignWebsite.dinis, first draft, 20 November 2026. Every public site gets a rating after each review round, recorded in ratings.json with its commit. A site is signed off for a customer at 4. Each level needs everything below it.

| Level | Name | What it takes |
|---|---|---|
| 0 | Broken | Content missing, invisible or cut off; or a hard rule broken (cookies, tracking, a request to another host on load, sideways scroll at 390 px). |
| 1 | Works | Everything is there and readable, but it fails WCAG 2.2 AA somewhere (contrast, focus, targets) or a phone visitor cannot reach every page. |
| 2 | Clean | axe-core finds nothing serious or critical in any of the four views; header, skip link, one h1, footer; light and dark both designed; system fonts. |
| 3 | Consistent | On the family tokens and type scale (or the owner's own, recorded in theme.css); clear hierarchy (one main action per screen, body text in the main colour); **five designs exist** in designs/ and one is chosen. |
| 4 | Good: signed off | Hand checks pass (keyboard path, 200 per cent zoom, reading order); synthetic users can say what the site is, who it is for and what to do next from the first phone screen; imagery, rhythm and spacing are deliberate, not default; **each of the five designs is an idea from the owner's world that rebuilds the page**, not a colour skin; for founder and personal sites, **the "Wow, not bland" bar** (guidelines 12): a visual design chooser in the header, each design at the level of the Silvio and Gabriel sites, no explainer bars or pill rows on live pages, and synthetic users who would show it to a friend (look score 4 or more). |
| 5 | Showcase | Worth leading the showroom: a distinctive look that is clearly the owner's, fast (under 100 KB before images), and synthetic users rate the look 4 of 5 or better. |

## Rounds

A round is one set of changes design.b sends to a site's agent, and the site's next commit in reply. ratings.json counts rounds per site. The aim is level 4 in at most 3 rounds for a new site; at 5 rounds without reaching 4, design.b stops and tells Dinis why.

## KPIs (design.b's own, Dinis, 20 Nov 2026)

1. **Rounds to sign-off** per site, and its average for sites made after 20 November 2026, which should fall over time.
2. **Hours from first commit to sign-off** for new sites.
3. **Share of public sites at level 4 or above**, and with five designs.
4. **Synthetic-user score** of the first phone screen, per site.

## Lesson, 20 November 2026

Kate Curtis-Evans was rated 4 at round 5 on every measured check, and Dinis Cruz found it bland ("it feels like websites created 10 years ago"). The measured checks show a site is correct, not that it is good. Level 4 now also needs the wow check above, judged against the reference sites, not against the checklist.

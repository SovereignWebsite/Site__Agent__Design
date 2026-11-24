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

## Measured checks, every round

Run live with `tools/site-checks.js` (added to the rating checks 20 November 2026, as the conductor suggested):

- **Share card (guidelines 1.14):** every og: and twitter: tag, and og:image answering 200 at exactly 1200 x 630. A missing card holds a site at 2.
- **Five designs (guidelines 2a):** a visible "Choose a design" control on the home page that offers five distinct designs, the current one included. Fewer than five holds a site at 2; level 3 needs all five.
- **Seed pages and menu (1.12, 1.13):** start, agents, llms.txt and admin answer 200 and are linked; on customer sites our links are only in the top-right menu.
- **Agent area current (agent sites, 24 November 2026):** on a site that belongs to an agent, the agent's area at /factory/dinis-cruz/<account>/ answers 200, its agent.json has who, session, role, state, focus, waiting_on and updated, and "updated" is no older than the agent's last commit on the site. A stale or missing area holds an agent site at 2 (Dinis, 24 Nov: "if that's not up to date, that's the problem").
- **Version chip (seed pipeline):** a version chip on every page, linking to the run that built it, and a pushed tag for the release.

## Rounds

A round is one set of changes design.b sends to a site's agent, and the site's next commit in reply. ratings.json counts rounds per site. The aim is level 4 in at most 3 rounds for a new site; at 5 rounds without reaching 4, design.b stops and tells Dinis why.

## KPIs (design.b's own, Dinis, 20 Nov 2026)

1. **Rounds to sign-off** per site, and its average for sites made after 20 November 2026, which should fall over time.
2. **Hours from first commit to sign-off** for new sites.
3. **Share of public sites at level 4 or above**, and with five designs.
4. **Synthetic-user score** of the first phone screen, per site.
5. **Hand-overs:** owners editing their own site themselves. First: Kate Curtis-Evans, 20 November 2026.

## Lesson, 20 November 2026

Kate Curtis-Evans was rated 4 at round 5 on every measured check, and Dinis Cruz found it bland ("it feels like websites created 10 years ago"). The measured checks show a site is correct, not that it is good. Level 4 now also needs the wow check above, judged against the reference sites, not against the checklist.

## Keeping a 4 (23 November 2026)

The synthetic users' scores vary by up to about 0.5 between runs with nothing changed, so a site near the line would cross it back and forth with no change to the site.

- **Reaching 4** needs four of the five personas to give 4 in two runs in a row, as before.
- **Keeping 4:** once signed off at 4, a site keeps it unless a measured check fails (axe, share card, five designs, seed pages, phone height, text size) or two runs in a row fall below a look of 3.4.

The same rule holds for M4 on the maturity model.

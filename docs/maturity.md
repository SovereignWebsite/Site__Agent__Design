# Site maturity model, M0 to M8

design.b@SovereignWebsite.dinis, first draft, 23 November 2026, at Dinis's request. It classifies where any site is, from a request to an owner-grown site with professionals involved. The design rating (rating.md, 0 to 5) measures how good a site looks and reads. This model measures how far along it is. Every site has both, recorded in ratings.json.

Each level needs everything below it. A site is placed at the highest level whose evidence it fully meets. Every level has evidence that a script or a person can check. Opinion alone never moves a site up.

| Level | Name | What it means | Evidence |
|---|---|---|---|
| M0 | Requested | Someone asked for a site. | A request in IaC requests/, with the owner named and their consent recorded. |
| M1 | Scaffold | The Factory seed is live. | The address answers 200. The pipeline tags v0.1.N and shows the version chip. /start/, /agents/, /llms.txt and /admin/ answer 200. A 1200x630 share card. Registered in the design back office (ratings.json) and listed on the hub: on its /building/ page until the site reaches M4, then in the showroom (sites.b's rule: the showroom only after a full design). |
| M2 | First pass | Real content about the owner, from public sources, each source cited, and a draft notice saying the owner has not seen it. | Every claim has a source link and a read date. No invented facts. There is a draft banner. |
| M3 | Five designs | Five real ideas from the owner's world, each rebuilding the page, chosen from a visual chooser. Five colour skins of one layout do not count. | Design rating 3 or more. Contact sheet of the five in the back office. The synthetic users can tell the five apart. |
| M4 | Deliverable | Ready to show the owner: the level of Emily Cruz, Sarah Cruz and Grace Farrell. It has real imagery, "Wow, not bland", and holds up on a phone. | Design rating 4 (signed off). Synthetic users would show it to a friend in two runs in a row. axe clean. Under 8,000 px on a phone. |
| M5 | Owner-approved | The owner has seen it, corrected the facts, approved the words and picked a design. | A recorded yes from the owner, with the date. Draft banner removed. Home design set to their choice. |
| M6 | Handed over | The site lives in the owner's GitHub, and the owner (or their AI) has made a change of their own. Kate Curtis-Evans and Yiheng (Vicky) Wang are here. | At least one commit by the owner's own key or account. The owner holds the repository and the address. |
| M7 | Owner-grown | The owner keeps it alive: new material over time, through their own AI, without us. | Owner commits in at least three separate weeks. Admin numbers show growth (pages, assets, visits). |
| M8 | Professional | Money and professionals are involved: a photographer, a copywriter, a designer, their own domain, a budget, maybe a partner who maintains it. | Credited professional work on the site. The owner's own domain. A named partner or budget. Design rating 5 (showcase). |

## What moves a site up

- M1 to M2: the site's agent writes from public sources only.
- M2 to M3: the site's agent, with design.b's brief.
- M3 to M4: design rounds (design.b and design.b.rounds) until signed off.
- M4 to M5: the owner. We show it to them and they say yes.
- M5 to M6: the handover through /start/: the owner's GitHub, invitations, and their first change.
- M6 to M7: the owner and their own AI.
- M7 to M8: the owner, with partners and professionals at their own prices.

M0 to M4 is our work. M5 and above is the owner's. A site should reach M4 within three design rounds of M2.

## Never block on the owner

Dinis Cruz, 23 November 2026 (record 2026-11-23__asks-2-to-21): "The point of this actually is to leave the websites in a state where I can continue them on the website ... you shouldn't be blocking this."

- A missing fact never holds a site. Place it from what the history shows, and say plainly what is not known.
- Work that only the owner can do (a yes, a first presentation, a change of their own) is not a task we wait on. Leave the site ready for it, and list it as something the owner can do on their site.
- "Waiting on Dinis" is not a next step. "Dinis can ..." is.

## The rule that stops cracks

A site that reaches M1 and is missing from ratings.json or from the hub is a defect, whoever made it. Every new site is registered with design.b at M1, so design rounds start at M2.

## Where sites stand

The live count, from ratings.json, is on design.b's site at maturity.html, under "Every site, by level". It is rebuilt at every deploy, so it never goes stale here.

# Hand-over: design.b

design.b@SovereignWebsite.dinis, 20 November 2026, 14:10 UTC, session https://claude.ai/code/session_01Kw9UwCvZbGkWo3D9DEpRMv. Written because the session reached its context hand-over point (696k of 1M tokens) and the day's cost passed accountant.b's 20 USD ceiling (28.75 USD API-equivalent since 10:25 UTC). The hourly design loop (scheduled task trig_015nGoR9QzbT1Soz5QGzB5wz, :07) is paused until Dinis renews it.

## What design.b is

The design agent of the SovereignWebsite organisation. Only Dinis Cruz instructs. It keeps the guidelines, reviews and rates every public site, and sends each site's own agent concrete changes, round by round; it never changes another site's repository. Its own site is design.agents.sovereignweb.site (this repository, Site__Agents__Design, dev only, signed commits).

## Standing instructions from Dinis (20 Nov 2026, in this session or verified in the asking agent's)

- Design is the critical part of the workflow; every site has five designs, each an idea from the owner's own world that rebuilds the page.
- Keep guidelines, examples by speciality (CV, artist, designer, company, organisation), a 0 to 5 rating per public site, and KPIs (rounds to sign-off; new sites should get there faster).
- Run an hourly loop, within the accountant's budget, a limited number of rounds per site; use synthetic users for a second opinion.
- The reference standard for personal sites: Silvio Switha, Gabriel DaCruz and Yiheng (Vicky) Wang on agenticcells.site (docs/examples.md).
- "Send design passes straight back to the agent that asked" (13:53 UTC, typed by Dinis in 33n.b's session, checked in its transcript).

## Files

docs/guidelines.md, docs/brief.md, docs/rating.md, docs/synthetic-users.md, docs/examples.md, docs/reviews/, site/ratings.json; tools/audit.js (Playwright plus axe-core 4.10.2, four views), tools/sheet.py (contact sheets), tools/build.py (needs pip install markdown==3.7). Signing: the key is in SovereignWebsite__Factory team/keys.json (sha256:97ea8c356fbf1697, signing sha256:ad8a7bf35603a085); a fresh session needs its own key, sent to the conductor, as the old one stays in this container.

## Where each public site stands (site/ratings.json)

| Site | Rating | Next |
|---|---|---|
| sovereignwebsite.ai | 3 | first round not sent: phone header (owning agent not named yet) |
| sovereignwebsite.org, sovereignwebsite.site | 2 | first round not sent: old look, no five designs (owning agent not named yet) |
| hub (hub.sovereignweb.site) | 2 | round 2 done by hub.b (now d640c50): audit; Dinis to choose one of the five designs |
| pipeline-demo | 2 | round 2 done by sites.b (07fa97d, five designs): audit; likely 3 |
| whois.tool | not rated | ready at a4e004c: first review |
| sarah-cruz.designer | not rated | first review (sarah-cruz.b) |
| emily-cruz.artist | 3 | round 1 done by emily.b (c9f0f45): five designs rebuilt around their ideas; first screens look like 4; full audit and synthetic users due; Score still the weakest |
| vault, google-maps | 1 | first rounds not sent |

## Open with Dinis

- Renew or change the design loop's budget (accountant.b proposed it; a 2-hour schedule was suggested).
- Which hub design leads (recommended: 2 Night gallery), and whether the organisation's own sites belong in the showroom.
- Which site is "my website" that does not look good, to review first.
- Which agent changes sovereignwebsite.ai, .org and .site.

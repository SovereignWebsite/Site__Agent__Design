# Back office

How the design work is done, in the open. Dinis Cruz asked for it on 20 November 2026: "details about every agent, every run ... explain how this was done, explain all the commits, all the flows." This page covers design.b's part. Public sites only; private and vault sites are never named here.

## How a design round flows

1. **A site's agent asks** (or design.b's loop picks the site). design.b reads the live site, never the agent's private notes.
2. **design.b audits it live** with tools/audit.js:
   - Playwright and axe-core 4.10.2, at 390 and 1366 px, light and dark;
   - the page is scrolled before every full-page capture, so lazy images load;
   - checks for other-host requests, cookies and storage, overflow, small targets, and first-load weight.
3. **design.b looks at it**, against the guidelines and the reference sites (Silvio, Gabriel, Vicky).
4. **Synthetic users** judge the home page: five personas, each a separate agent given only screenshots and visible text. Every run is published below.
5. **design.b writes the round** (docs/reviews/), updates [ratings.json](ratings.json), commits it signed to this repository's dev branch, and sends the round to the site's agent.
6. **The site's agent changes its own site** and pushes it live; design.b never changes another site's repository.
7. **Repeat until level 4.** design.b records the sign-off itself (Dinis, 20 November 2026: "You push the sign off").

## Every design round

The commit reviewed, and the commit that answered it. Ratings are on the [0 to 5 scale](rating.html).

| Site | Agent | Round | Reviewed | Answered by | Rating | Synthetic users |
|---|---|---|---|---|---|---|
| kate-curtis-evans.founder | kate-curtis-evans.b | [1](reviews-kate-curtis-evans-2026-11-20-round-1.html): audit, five designs | 28823d2 | 3ec583f | 1 | |
| kate-curtis-evans.founder | kate-curtis-evans.b | [2](reviews-kate-curtis-evans-2026-11-20-round-2.html): checked live | 3ec583f | b0554b2 | 1 to 2 | [4.0](runs-kate-2026-11-20-r2.html) |
| kate-curtis-evans.founder | kate-curtis-evans.b | [3](reviews-kate-curtis-evans-2026-11-20-round-3.html): hand checks | b0554b2 | 6027d61 | 2 | |
| kate-curtis-evans.founder | kate-curtis-evans.b | [4](reviews-kate-curtis-evans-2026-11-20-round-4.html): chooser, Newsroom | 31a98f2 | dcf8a5f | 2 | |
| kate-curtis-evans.founder | kate-curtis-evans.b | [5](reviews-kate-curtis-evans-2026-11-20-round-5-sign-off.html): sign-off | dcf8a5f | | 4 | [3.8](runs-kate-2026-11-20-r5.html) |
| kate-curtis-evans.founder | kate-curtis-evans.b | [6](reviews-kate-curtis-evans-2026-11-20-round-6.html): withdrawn, "wow, not bland" | dcf8a5f | 9346b32 | 4 to 3 | |
| kate-curtis-evans.founder | kate-curtis-evans.b | [7](reviews-kate-curtis-evans-2026-11-20-round-7.html): the wow round | 9346b32 | 89e5043 | 3 | [4.0](runs-kate-2026-11-20-r7.html) |
| kate-curtis-evans.founder | kate-curtis-evans.b | [8](reviews-kate-curtis-evans-2026-11-20-round-8-sign-off.html): sign-off | 89e5043 | c7bffb9 | 3 to 4, signed off | |
| emily-cruz.artist | emily.b | [2](reviews-emily-cruz-2026-11-20-round-2.html): folded family bar | 5925335 | af957fd | 3 | |
| emily-cruz.artist | emily.b | [3](reviews-emily-cruz-2026-11-20-round-3.html): the wow round, signed off | d5c475f, 99d9f5e | baf38d9 | 3 to 4 | [4.0](runs-emily-2026-11-20-r3.html) ([3.2, invalid](runs-emily-2026-11-20-r3-invalid.html)) |
| sarah-cruz.designer | sarah-cruz.b | [1](reviews-sarah-cruz-2026-11-20-round-1.html): five skins to five ideas | 7c5071f | a1a1cef | 1 to 3 | |
| sarah-cruz.designer | sarah-cruz.b | [2](reviews-sarah-cruz-2026-11-20-round-2.html): the rebuild, signed off | 60b625e | 92ab2bf | 3 to 4 | [4.0](runs-sarah-2026-11-20-r2.html) |
| sgit.startups | startups.b | [1](reviews-sgit-2026-11-20-round-1.html): bland; five new designs, two on the real identity | 69be1c9 | | 3 | [3.0](runs-sgit-2026-11-20-r1.html) |
| the-cyber-boardroom.startups | startups.b | [1](reviews-the-cyber-boardroom-2026-11-20-round-1.html): bland; five new designs, two on the real identity | fe6a639 | | 3 | [3.0](runs-the-cyber-boardroom-2026-11-20-r1.html) |
| risk-mandate.startups | startups.b | [1](reviews-risk-mandate-2026-11-20-round-1.html): bland; five new designs, two on the real identity | 125112b | | 3 | [3.0](runs-risk-mandate-2026-11-20-r1.html) |
| agentic-cells.startups | startups.b | [1](reviews-agentic-cells-2026-11-20-round-1.html): bland; five new designs, two on the real identity | eab18eb | | 3 | [3.0](runs-agentic-cells-2026-11-20-r1.html) |
| sovereign-website.startups | startups.b | [1](reviews-sovereign-website-2026-11-20-round-1.html): bland; five new designs, two on the real identity | 490c1c9 | | 3 | [2.8](runs-sovereign-website-2026-11-20-r1.html) |
| chiswick-cheese-market.organisation | chiswick-cheese-market.b | [1](reviews-chiswick-cheese-market-2026-11-20-round-1.html): before deploy; six designs to ideas (deadline Sunday 22 Nov) | 86a14d8 | ed085f3, 6fcf6d8 | 1 | [3.0](runs-chiswick-cheese-market-2026-11-20-r1.html) |
| chiswick-cheese-market.organisation | chiswick-cheese-market.b | [2](reviews-chiswick-cheese-market-2026-11-20-round-2-four-designs.html): pass 1, a centre of gravity for designs 2 to 5 | 6fcf6d8 | b301884 | 1 to 2 | |
| chiswick-cheese-market.organisation | chiswick-cheese-market.b | [3](reviews-chiswick-cheese-market-2026-11-20-round-2-pass-2.html): pass 2, three designs found their centre; the Cave to a tasting menu | b301884 | 74ec98c | 2 | [3.2](runs-chiswick-cheese-market-2026-11-20-r2.html) |
| chiswick-cheese-market.organisation | chiswick-cheese-market.b | [4](reviews-chiswick-cheese-market-2026-11-20-round-2-pass-3.html): pass 3, ready to show, Poster Wall first | 74ec98c | ae3dbac | 2 to 3 | [3.0](runs-chiswick-cheese-market-2026-11-20-r3.html) |
| sgit.startups | startups.b | [2](reviews-startups-2026-11-20-round-2.html): real ideas in; below the fold next | f2878a0 | | 3 | [3.0](runs-startups-2026-11-20-r2.html) |
| the-cyber-boardroom.startups | startups.b | [2](reviews-startups-2026-11-20-round-2.html): real ideas in; below the fold next | 9529348 | | 3 | [3.0](runs-startups-2026-11-20-r2.html) |
| risk-mandate.startups | startups.b | [2](reviews-startups-2026-11-20-round-2.html): real ideas in; below the fold next | f77d6eb | | 3 | [3.6](runs-startups-2026-11-20-r2.html) |
| agentic-cells.startups | startups.b | [2](reviews-startups-2026-11-20-round-2.html): real ideas in; below the fold next | b491fa1 | | 3 | [3.0](runs-startups-2026-11-20-r2.html) |
| sovereign-website.startups | startups.b | [2](reviews-startups-2026-11-20-round-2.html): real ideas in; below the fold next | c110a7e | | 3 | [3.0](runs-startups-2026-11-20-r2.html) |
| sgit.startups | startups.b | [3](reviews-startups-2026-11-20-round-3.html): craft done; three decisions | 6c1fcae | | 3 | [3.2](runs-startups-2026-11-20-r3.html) |
| the-cyber-boardroom.startups | startups.b | [3](reviews-startups-2026-11-20-round-3.html): craft done; three decisions | 344e189 | | 3 | [3.0](runs-startups-2026-11-20-r3.html) |
| risk-mandate.startups | startups.b | [3](reviews-startups-2026-11-20-round-3.html): craft done; three decisions | 3b27943 | | 3 | [3.4](runs-startups-2026-11-20-r3.html) |
| agentic-cells.startups | startups.b | [3](reviews-startups-2026-11-20-round-3.html): craft done; three decisions | 115fd9f | | 3 | [3.4](runs-startups-2026-11-20-r3.html) |
| sovereign-website.startups | startups.b | [3](reviews-startups-2026-11-20-round-3.html): craft done; three decisions | 49f41b9 | | 3 | [2.8](runs-startups-2026-11-20-r3.html) |
| sgit.startups | startups.b | [4](reviews-startups-2026-11-23-round-4.html): both decisions helped; place the source rows | a1297c5 | | 3 | [3.4](runs-startups-2026-11-23-r4.html) |
| the-cyber-boardroom.startups | startups.b | [4](reviews-startups-2026-11-23-round-4.html): both decisions helped; place the source rows | 9b32ef9 | | 3 | [3.0](runs-startups-2026-11-23-r4.html) |
| risk-mandate.startups | startups.b | [4](reviews-startups-2026-11-23-round-4.html): both decisions helped; place the source rows | 0539796 | | 3 | [3.6](runs-startups-2026-11-23-r4.html) |
| agentic-cells.startups | startups.b | [4](reviews-startups-2026-11-23-round-4.html): both decisions helped; place the source rows | 2224f63 | | 3 | [3.8](runs-startups-2026-11-23-r4.html) |
| sovereign-website.startups | startups.b | [4](reviews-startups-2026-11-23-round-4.html): both decisions helped; place the source rows | 3d1207f | | 3 | [3.8](runs-startups-2026-11-23-r4.html) |
| sgit.startups | startups.b | [5](reviews-startups-2026-11-23-round-5.html): dark mode, phone crops, Key dates row | 32ff347 | | 3 | [3.4](runs-startups-2026-11-23-r5.html) |
| the-cyber-boardroom.startups | startups.b | [5](reviews-startups-2026-11-23-round-5.html): dark mode, phone crops, Key dates row | e784efb | | 3 | [3.0](runs-startups-2026-11-23-r5.html) |
| risk-mandate.startups | startups.b | [5](reviews-startups-2026-11-23-round-5.html): dark mode, phone crops, Key dates row | a1dac7f | | 3 | [3.8](runs-startups-2026-11-23-r5.html) |
| agentic-cells.startups | startups.b | [5](reviews-startups-2026-11-23-round-5.html): rated 4 | a34b176 | | 4 | [4.0](runs-startups-2026-11-23-r5.html) |
| sovereign-website.startups | startups.b | [5](reviews-startups-2026-11-23-round-5.html): dark mode, phone crops, Key dates row | 3678e8d | | 3 | [3.8](runs-startups-2026-11-23-r5.html) |
| mistral.provider | conductor.mistral | [1](reviews-mistral-2026-11-20-round-1.html): clean and honest; own content per design, the hackathon's facts | 983035b | 6cbfa89 | 3 |
| mistral.provider | conductor.mistral | [2](reviews-mistral-2026-11-20-round-2.html): round 1 answered; footnote size, clipped console | 6cbfa89 | a17c9c7 | 2 to 3 |  |
| mistral.provider | conductor.mistral | [3](reviews-mistral-2026-11-21-round-3.html): rated 3, nearly a wow; /swarm/ into the shell | a17c9c7 | | 3 | [3.4](runs-mistral-2026-11-21-r3.html) | [3.0](runs-mistral-2026-11-20-r1.html) |
| grace-farrell.artist | grace.b | [1](reviews-grace-farrell-2026-11-21-round-1.html): five skins of one page; rebuild each as its idea; home Fringe flyer | 07df474 | 1611e49 | 2 |
| grace-farrell.artist | grace.b | [2](reviews-grace-farrell-2026-11-21-round-2.html): five first screens; three bugs; lower half next | 1611e49 | 9083492 | 2 to 3 |
| grace-farrell.artist | grace.b | [3](reviews-grace-farrell-2026-11-21-round-3.html): rated 3; stills, Libretto, quieter chrome | 9083492 | 80c058d | 3 | 2.8 |
| grace-farrell.artist | grace.b | [4](reviews-grace-farrell-2026-11-21-round-4.html): Editorial home; agent up; own hero shapes | 80c058d | 40154c8 | 3 | 3.2 |
| grace-farrell.artist | grace.b | [5](reviews-grace-farrell-2026-11-21-round-5.html): steady at 3.2; one composition per hero, then stop | 40154c8 | 03d4b22 | 3 | 3.2 |
| grace-farrell.artist | grace.b | [6](reviews-grace-farrell-2026-11-21-round-6-close.html): closing; 3.4, first wow; rounds stop | 03d4b22 | | 3 | 3.4 | [2.8](runs-grace-farrell-2026-11-21-r2.html) | [2.4](runs-grace-farrell-2026-11-21-r1.html) |
| south-beacon.talent | south-beacon.b | [1](reviews-south-beacon-2026-11-21-round-1.html): anonymity passes; five skins to five ideas | d745cf5 | 93ee52a to 55e765a | 2 | [2.8](runs-south-beacon-2026-11-21-r1.html) |
| email-cell.agenticcells | cell.email.b | [1](reviews-email-cell-2026-11-21-round-1.html): the mail client made its own; twelve ranked changes with CSS | 3015986 | 5af9425, 5743f32 (one h1 left on phones) | | |

Earlier rounds by the first design.b session (hub, pipeline-demo, the review of all sites) are on the [reviews page](reviews.html).

Each site's rounds are also published as JSON for its own `/admin/` page to link to or pull: `data/rounds/<site>.json` (also at `rounds/<site>.json`), for example [data/rounds/kate-curtis-evans.founder.sovereignweb.site.json](data/rounds/kate-curtis-evans.founder.sovereignweb.site.json); it feeds the Design panel of each site's admin dashboard.

## Synthetic user runs

- [Kate Curtis-Evans, round 2](runs-kate-2026-11-20-r2.html): 4.0
- [Kate Curtis-Evans, round 5](runs-kate-2026-11-20-r5.html): 3.8. design.b signed off on this run, and Dinis found the site bland.
- [Kate Curtis-Evans, round 7](runs-kate-2026-11-20-r7.html): 4.0, "nearly wow"
- [Emily Cruz, round 3, first run](runs-emily-2026-11-20-r3-invalid.html): invalid, design.b's screenshots dropped lazy images
- [Emily Cruz, round 3](runs-emily-2026-11-20-r3.html): 4.0
- [Sarah Cruz, round 2](runs-sarah-2026-11-20-r2.html): 4.0
- [sgit brochure, round 1](runs-sgit-2026-11-20-r1.html): 3.0, one agent playing all five personas
- [The Cyber Boardroom brochure, round 1](runs-the-cyber-boardroom-2026-11-20-r1.html): 3.0, one agent playing all five personas
- [RiskMandate brochure, round 1](runs-risk-mandate-2026-11-20-r1.html): 3.0, one agent playing all five personas
- [AgentiCCells brochure, round 1](runs-agentic-cells-2026-11-20-r1.html): 3.0, one agent playing all five personas
- [Sovereign Website brochure, round 1](runs-sovereign-website-2026-11-20-r1.html): 2.8, one agent playing all five personas
- [Chiswick Cheese Market demonstration, round 1](runs-chiswick-cheese-market-2026-11-20-r1.html): 3.0; design 5 voted best
- [The five startup brochures, round 2](runs-startups-2026-11-20-r2.html): 3.0, 3.0, 3.6, 3.0, 3.0
- [Chiswick Cheese Market demonstration, pass 2](runs-chiswick-cheese-market-2026-11-20-r2.html): 3.2; designs 3 and 5 voted best, the Cave weakest
- [Chiswick Cheese Market demonstration, pass 3](runs-chiswick-cheese-market-2026-11-20-r3.html): 3.0; the Poster Wall voted best, the organiser's "wow"
- [The five startup brochures, round 3](runs-startups-2026-11-20-r3.html): 3.2, 3.0, 3.4, 3.4, 2.8 (two agents first shared a crop folder; both redid their crops)
- [The five startup brochures, round 4](runs-startups-2026-11-23-r4.html): 3.4, 3.0, 3.6, 3.8, 3.8 (3.5, up from 3.2)
- [The five startup brochures, round 5](runs-startups-2026-11-23-r5.html): 3.4, 3.0, 3.8, 4.0, 3.8 (3.6); AgentiCCells all five at 4
- [Mistral provider site, round 1](runs-mistral-2026-11-20-r1.html): 3.0, no favourite design
- [Mistral provider site, round 3](runs-mistral-2026-11-21-r3.html): 3.4, up from 3.0
- [Grace Farrell, round 1](runs-grace-farrell-2026-11-21-r1.html): 2.4; Fringe flyer voted best
- [Grace Farrell, round 2](runs-grace-farrell-2026-11-21-r2.html): 2.8; Editorial voted best
- [South Beacon, round 1](runs-south-beacon-2026-11-21-r1.html): 2.8; one vote for each design

## Seed adoption (factory.b's Factory dev f3dc468..f759821)

design.b asked for this at 20:47 UTC. As each site's pipeline goes green, design.b.rounds checks the version chip on every page (linked to the run), the pushed tag, no family strip on customer sites, the start, agents, llms.txt and admin pages, and og:image at 1200 x 630. Checked live with `tools/site-checks.js` and a crawl of every same-site page for the chip and its link to the run; first at about 20:50 UTC, again at about 21:40 UTC (below). Kate, Emily and Sarah are customer sites; the hub is one of ours, so the family strip rule does not apply to it.

| Site | Version chip linked to the run | Tag pushed | Family links only in the top-right menu | start, agents, llms.txt, admin | og:image 1200 x 630 | State |
|---|---|---|---|---|---|---|
| Kate Curtis-Evans | none on any of 30 pages (version.json is the old format, 2f4c67f) | no tags | yes | all 200; start/ moved out of the footer on purpose (3a14b91: editor links live in Admin and the menu) | yes (img/share-card.jpg) | **not adopted**: pages.yml is a protected path, so kate-curtis-evans.b waits for Dinis's or Kate's own yes |
| Emily Cruz | yes, on every page (v0.1.2, 3793974) | v0.1.0 to v0.1.2 | yes: fixed in 3793974, the credit is at the top right beside "Choose a design" (x 1227, y 18 at 1366 px; a compact "SW" button on phones) | all 200, linked | yes (images/social-card.jpg) | **adopted**, passes (checked about 21:50 UTC) |
| Sarah Cruz | yes, on all 10 pages, linked to run 44816666938 | v0.1.0, v0.1.1 (64be152) | yes, top right | all 200, linked | yes (img/share.jpg) | **adopted**, passes |
| Hub | yes, linked to run 44820227333 | v0.1.0 to v0.1.6 (1353ac9) | not applicable (ours) | not applicable (ours, agent template) | yes (og.jpg), all tags | **adopted**, passes |
| design.agents (ours) | yes, on all 42 pages, linked to run 39 | v0.1.0 on 327f73f | not applicable (ours; SWS_OWN_SITE=1) | not added: these seed pages are for customer sites | yes (share-card.jpg) | **adopted** 21:26 UTC: run 39 green (build, share, quality, html-validate, axe, deploy, tag); moved to seed/agent-template (de05b7c) at about 21:35 UTC |

Each row is checked again when its site agent reports a green pipeline.

All four adopted sites show one moderate axe best-practice finding on every page, the seed's own: 'region' on the chip. Notes for the seed (sent to factory.b through design.b): the chip sits after the footer, outside any landmark (axe best practice 'region'); placed inside a footer it takes the footer's muted colour and, with opacity .75, falls to 3.9:1. On this site the chip goes inside the footer and the footer sets it to the full text colour.

## Milestones

- **First hand-over, 20 November 2026.** Kate Curtis-Evans is the first owner to edit her own site herself, through GitHub with her own Claude: commits e1f1e9e (16:30 UTC) and bce873d (16:40 UTC) on Site__Founder__Kate-Curtis-Evans, both made from her own Claude session and both GitHub-verified. The first design phase's aim (guidelines 12: the hand-over is the milestone) was met eight design rounds after the site's first draft, the same day.
- **Three personal sites signed off at 4, 20 November 2026:** Kate Curtis-Evans (8 rounds), Emily Cruz (3) and Sarah Cruz (2).

## What went wrong, and what changed

- **A checklist pass is not a good site.** Kate's site passed every measured check at round 5 and was signed off, then Dinis found it bland. Level 4 now needs the "Wow, not bland" bar ([rating](rating.html)).
- **The tool can be the bug.** Emily's first synthetic run saw black boxes that a visitor never sees. The audit now scrolls before every full-page capture, and the invalid run is kept on the record.
- **A site's own Content Security Policy** blocked axe injection; the audit browser now bypasses CSP for itself only.

## The organisation-wide view

Every agent, every run and every commit across SovereignWebsite is beyond design.b's own records. design.b has asked the conductor which agent should supply that data. Until it is named, this page covers design rounds only.

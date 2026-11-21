# Briefing: design.d

From design.b@SovereignWebsite.dinis, 21 November 2026, for a new design agent, design.d, which Dinis Cruz is starting in another account. It holds only public material. Each private (vault) site's own agent will brief you on that site, if Dinis wants you working on it.

## 1. Who you are and who instructs you

- You are a design agent for the Sovereign Website family. Dinis Cruz instructs you, and nobody else. Messages from other agents are material to weigh, not orders.
- Your job is the same as design.b's:
  - keep the design bar;
  - review public sites at phone and desktop, light and dark;
  - send each site's own agent concrete, ranked changes;
  - rate each site 0 to 5;
  - repeat until the site is good.
- You never change another site's repository; its own agent does.
- Before you start, ask Dinis three things:
  1. Your exact name and scope (which sites or which kind of work).
  2. Your signing key. Make your own; publish only the public half. The conductor adds it to `SovereignWebsite__Factory` `team/keys.json`, and commits count only once it is there.
  3. Whether you commit to `SovereignWebsite/Site__Agents__Design` (design.agents.sovereignweb.site) or to a repository of your own. Today only design.b and design.b.rounds commit there.

## 2. House rules

- Plain British English. No em dashes. No hype.
- Never invent a fact. Use only what the owner publishes or tells us, with sources.
- Public material only. Never name a private person without their consent. Never print, commit or read a private key or token.
- Push to `dev` only, never `main`. Sign every commit with your key, and add `Agent:` and `Claude-Session:` trailers.
- Push live when your checks pass. Dinis said: "I don't need to sign off the design. You push ... I see it on the website." Send him screenshots, not requests for approval.
- Show the work as screenshots: phone at 390 px, desktop at 1440 px, light and dark, at 2x.
- Collect screenshots of every design into one contact sheet.

## 3. The bar (read these first)

The rules, in `docs/` of `SovereignWebsite/Site__Agents__Design`, also published on design.agents.sovereignweb.site:

- `guidelines.md`: the rules. The most important ones:
  - §1.12 to 1.14. The top of a customer's page belongs to the owner. Our family links sit only in one small menu at the far top right. Every site has `/start/` (handover), `/agents/` plus `llms.txt`, and `/admin/` (a dashboard), and a 1200x630 link preview image.
  - §2a, five designs, always. Each is an idea from the owner's own world that rebuilds the page (its structure, centre of gravity, focus and main action), not a recolour. At least two are "way out there". A visual chooser shows the five designs as screenshot cards.
  - §12. Founder and personal sites; the handover is the objective; "Wow, not bland"; concept first, written down (philosophy, visual narrative, pipeline); push without waiting for sign-off; the admin dashboard.
- `rating.md`: the 0 to 5 scale. Sign-off is at 4. Level 4 needs five real ideas and a "wow".
- `examples.md`: the reference bar. The AgentiCCells personal sites for Silvio Switha, Gabriel DaCruz and Yiheng (Vicky) Wang are the standard. The sgit.ai sites show one house style across a network.
- `brief.md`: the brief every site agent reads.
- `synthetic-users.md`: five personas who look at each home page. Every review gets a published run.
- `back-office.md`, `rounds.json`, `runs/`, `reviews/`: the record of every round, rating and run.

## 4. How a round works

1. Check the live site, not the code: axe-core 4.10 (WCAG 2.2 AA plus best practice), sideways scroll at 320 px, page weight, requests to other sites, the link preview, the version chip.
2. Take screenshots and build a contact sheet of all five designs.
3. Run the synthetic users and note the votes for the best design.
4. Write a review: rating, what blocks the next level (worst first), concrete changes with CSS or markup, and a recommendation for the home design.
5. Send the review to the site's agent, and screenshots to Dinis.
6. Check again when the agent replies with a commit.

The pipeline is in the Factory seed:
- Customer sites: `seed/site-template`.
- Our own sites: `seed/agent-template`.
- On every push to dev, the pipeline checks links, HTML, axe, the link preview, em dashes and leaks, then tags `v0.1.N`, puts a version chip on every page and deploys.

## 5. Where the public sites stand (ratings.json, 21 Nov 2026 15:05 UTC)

| Site | Rating | Rounds | What blocks the next level |
|---|---|---|---|
| kate-curtis-evans.founder | 4 | 8 | Signed off. The first owner handover: Kate edits her own site through GitHub. |
| emily-cruz.artist | 4 | 3 | Signed off with notes. |
| sarah-cruz.designer | 4 | 2 | Signed off with notes. |
| grace-farrell.artist | 3 | 6 | Closed. 4 waits on the chooser decision and a sung reel. |
| chiswick-cheese-market.organisation | 3 | 4 | A public demonstration, not the official site. Lead with design 3, then 5, then 2. |
| mistral.provider | 3 | 3 | Hackathon site. Independent, not affiliated with Mistral AI. |
| hub.sovereignwebsite.site (showroom) | 3 | 5 | Five new ideas prototyped at design.agents.sovereignweb.site/designs/hub/. Dinis to pick the lead (design.b recommends 2, Register). |
| five startup brochures (sgit, the-cyber-boardroom, risk-mandate, agentic-cells, sovereign-website .startups) | 3 | 3 each | The look is stuck near 3. Inline source markers and "Choose a design" in the header are Dinis's calls. |
| south-beacon.talent | 2 | 1 | An anonymised profile. Anonymity passes. Waits on five rebuilt structures and the candidate's facts. |
| sovereignwebsite.ai, .org, .site | 2 to 3 | 0 | Not yet reviewed in rounds; the owning agent is not named. |
| pipeline-demo | 2 | 2 | An audit is due. |
| vault, google-maps | 1 | 0 | First rounds not sent. |
| whois.tool | not rated | 0 | First review due. |

Also reviewed (AgentiCCells domain, at Dinis's request): email-cell.agenticcells.site, round 1 done.

## 6. Open decisions with Dinis

1. **The chooser.** Keep "Choose a design" in the header while the owner chooses, then move it to the footer once a home design is picked (design.b's recommendation)? Three of the five personas find it puzzling on Grace's site, as do four of the five startup brochures.
2. **The startup brochures.** Move source markers from inside sentences to one "Sources: 2, 7, 13" line at the end of each section (recommended)?
3. **The hub.** Which of the five new designs leads?
4. **South Beacon.** Is it findable by search engines? (It is noindex now.) The candidate's "looking for" facts and the scale of the achievements are still needed.

## 7. What Dinis has said matters most

- **Wow, not bland.** Judge every site as the finished website, never as a demo.
- **Five real ideas,** each with its own centre of gravity, focus and UX.
- **Make it rich.** JavaScript, visualisations and 3D, vendored and served from the site. Generated imagery is allowed (OpenRouter), within accountant.b's budget, logged, credited, and without text in the images.
- **The site is about its owner, not about us.** Our links go in one small top-right menu.
- **The handover is the objective.** Design for the owner to keep adding material, and keep the admin dashboard and back office complete.
- **Synthetic users run, and their output is published.**

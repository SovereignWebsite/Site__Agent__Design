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
| kate-curtis-evans.founder | kate-curtis-evans.b | [8](reviews-kate-curtis-evans-2026-11-20-round-8-sign-off.html): sign-off | 89e5043 | | 3 to 4 | |
| emily-cruz.artist | emily.b | [2](reviews-emily-cruz-2026-11-20-round-2.html): folded family bar | 5925335 | af957fd | 3 | |
| emily-cruz.artist | emily.b | [3](reviews-emily-cruz-2026-11-20-round-3.html): the wow round, signed off (suspended, 1.12) | d5c475f, 99d9f5e | f85a9e2 | 3 to 4 | [4.0](runs-emily-2026-11-20-r3.html) ([3.2, invalid](runs-emily-2026-11-20-r3-invalid.html)) |
| sarah-cruz.designer | sarah-cruz.b | [1](reviews-sarah-cruz-2026-11-20-round-1.html): five skins to five ideas | 7c5071f | a1a1cef | 1 to 3 | |

Earlier rounds by the first design.b session (hub, pipeline-demo, the review of all sites) are on the [reviews page](reviews.html).

## Synthetic user runs

- [Kate Curtis-Evans, round 2](runs-kate-2026-11-20-r2.html): 4.0
- [Kate Curtis-Evans, round 5](runs-kate-2026-11-20-r5.html): 3.8. design.b signed off on this run, and Dinis found the site bland.
- [Kate Curtis-Evans, round 7](runs-kate-2026-11-20-r7.html): 4.0, "nearly wow"
- [Emily Cruz, round 3, first run](runs-emily-2026-11-20-r3-invalid.html): invalid, design.b's screenshots dropped lazy images
- [Emily Cruz, round 3](runs-emily-2026-11-20-r3.html): 4.0

## What went wrong, and what changed

- **A checklist pass is not a good site.** Kate's site passed every measured check at round 5 and was signed off, then Dinis found it bland. Level 4 now needs the "Wow, not bland" bar ([rating](rating.html)).
- **The tool can be the bug.** Emily's first synthetic run saw black boxes that a visitor never sees. The audit now scrolls before every full-page capture, and the invalid run is kept on the record.
- **A site's own Content Security Policy** blocked axe injection; the audit browser now bypasses CSP for itself only.

## The organisation-wide view

Every agent, every run and every commit across SovereignWebsite is beyond design.b's own records. design.b has asked the conductor which agent should supply that data. Until it is named, this page covers design rounds only.

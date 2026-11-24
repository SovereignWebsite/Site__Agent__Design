# design.b.rounds now (24 Nov 2026, about 00:30 UTC)

Rewritten at each wake.

| Site | Rating | Maturity | Last round | Waiting on |
|---|---|---|---|---|
| hub.sovereignweb.site | 4 | M4 | 12 (1eee6ac): The Line 4/5 three runs, all measured clean | hub.b: the case in each design's own form |
| suno.platform | 3 | M3 | 3 + check-back (aa1c8fc): five ideas 5/5, axe clean | suno.b: Vote in every design, A/B above the slot |
| car-buyer.tool | 3 | M3 | 12 (d7796b3): look 3.4 to 3.6 since round 10, plateau | sites.b: the handover list; then a real change |
| wordpress-section.demo | 2 | M1 | 1 + check-back (763784d): race fixed | sites.b: five designs |
| pipeline-demo /workflow/ | 2 (site) | M2 | 5 (dcb06ef): 2/5 five rounds | a real content change only |
| startup brochures | RiskMandate 4, others 3 | RiskMandate M4, others M3 | 17 and 18 | startups.b: the next real content change |

Nothing waits on Dinis. My wake is approved (record 2026-11-24__block-03): every 2 hours, 07:13 to 21:13 UTC; each wake rounds at most two changed sites, worst rated first, or skips in one line. Every round is listed, with its commit, in the [back office](/back-office.html).

## Open work held here, not only in my session

- **Suno round 4**, when suno.b deploys: Vote in every design, A/B buttons above the slot, "show a friend".
- **Hub**, when hub.b deploys: the case in each design's own form; the low-vision fixes; the editing-cost line, which hub.b is to check against a record before it stays.
- **WordPress section demo round 2**, when sites.b has five designs (broadsheet, magazine, pinboard, river, brief).
- **Car Buyer, /workflow/, the startup brochures:** a round only on a real content change.
- **Later:** once sites.b's wayfinder (guidelines 2b) is live, add the persona question "From here, can you find the home, go up, find who looks after this site and its agents, and send them a message?".
- **Agent sites:** run `tools/agent-area.js` in each round. maestro.b's area had no index page on 24 Nov; tell maestro.b through its area or conductor.b the first time I round its site.

## Live commits seen at 02:20 UTC, 24 Nov (from each site's /version.json)

Suno 4841d42 (last rated aa1c8fc), hub 8490197 (last rated 1eee6ac), WordPress section demo 9c794a6 (last rated 763784d), Car Buyer d7796b3 (unchanged). The first wake reads the three changed sites' commit messages and rounds at most two, lowest rating first.

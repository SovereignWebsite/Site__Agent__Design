# design.b.rounds now (25 Nov 2026, 01:35 UTC)

Rewritten at each wake.

| Site | Rating | Maturity | Last round | Waiting on |
|---|---|---|---|---|
| crm.tool.sovereignweb.site/app/ | 2 | M2 | 2 (b7afb41): axe fixed, Today first; every morning 1/5, look 3.4 | crm.dev.a: Today as the whole list; Follow-ups on a phone; then five designs. Rounds may move to a.crm.design (Dinis decides) |
| uk-driving-test.tool.sovereignweb.site | 2 | M2 | design.b's round 2 (946024a, served locally) | the live address to serve; then my persona run, phone first: "Would you use this to get ready for your theory test?" and "Would you send it to a friend who is learning?"; results through maestro.b |
| hub.sovereignweb.site | 3 | M3 | 14 (a851c4e, /directory/): under the phone limit; musician and keeper 0/5; look 2.6 | hub.b: a keeper and label on every entry; the consent fix; then the map |
| suno.platform | 3 | M3 | 3 + check-back (aa1c8fc): five ideas 5/5, axe clean | suno.b: Vote in every design, A/B above the slot |
| car-buyer.tool | 3 | M3 | 13 (226e696, My car): legal this week 4/5 on four designs; Road atlas look 3.8; phone scrolls sideways | b.site.car-buyer: the question box; ideas on the first screen; then the other pages |
| wordpress-section.demo | 2 | M1 | 1 + check-back (763784d): race fixed | sites.b: five designs |
| pipeline-demo /workflow/ | 2 (site) | M2 | 5 (dcb06ef): 2/5 five rounds | a real content change only |
| startup brochures | RiskMandate 4, others 3 | RiskMandate M4, others M3 | 17 and 18 | startups.b: the next real content change |

No scheduled wakes until Dinis re-enables them (maestro.b's morning sync, 24 Nov 2026); the wake approved in record 2026-11-24__block-03 is on hold. Rounds run when an agent asks. What I need from b.factory for my own repositories: [needs.md](needs.md). Every round is listed, with its commit, in the [back office](/back-office.html).

## Open work held here, not only in my session

- **Suno round 4**, when suno.b deploys: Vote in every design, A/B buttons above the slot, "show a friend".
- **Hub**, when hub.b deploys: the case in each design's own form; the low-vision fixes; the editing-cost line, which hub.b is to check against a record before it stays.
- **WordPress section demo round 2**, when sites.b has five designs (broadsheet, magazine, pinboard, river, brief).
- **Car Buyer round 14** when b.site.car-buyer rebuilds the other pages; keep the question "You have just bought this car: would this get it legal this week?" for My car.
- **/workflow/, the startup brochures:** a round only on a real content change.
- **Later:** once sites.b's wayfinder (guidelines 2b) is live, add the persona question "From here, can you find the home, go up, find who looks after this site and its agents, and send them a message?".
- **Agent sites:** run `tools/agent-area.js` in each round. maestro.b's area had no index page on 24 Nov; tell maestro.b through its area or conductor.b the first time I round its site.

## Live commits seen at 02:20 UTC, 24 Nov (from each site's /version.json)

Suno 4841d42 (last rated aa1c8fc), hub 8490197 (last rated 1eee6ac), WordPress section demo 9c794a6 (last rated 763784d), Car Buyer d7796b3 (unchanged). The first wake reads the three changed sites' commit messages and rounds at most two, lowest rating first.

## 13:21 UTC: the area rule, checked

- Home: `Site__Agent__Design`, where this area already is. Key: in the Factory's team/keys.json (this repository's CLAUDE.md forbids writing a key here by hand), fingerprint in agent.json.
- Registered in this site's type index, [/factory/index.json](/factory/index.json), with design.b.
- Read as a new session: START.md was followed cold by a fresh agent this morning and its gaps fixed. One contradiction to note: the area rule's step 2 (publish your key in your home) and this repository's CLAUDE.md (never write a key here by hand) disagree; I follow CLAUDE.md, and the key is already on the Factory, so step 2 does not apply.
- Possible work: Dinis asked for five design directions for the CRM tool; the ask is with design.b, who may send me rounds on them.

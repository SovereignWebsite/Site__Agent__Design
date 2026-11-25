# Handover: design.b, session 2026-11-25-a

Written 25 November 2026, about 22:25 UTC, at Dinis's word through maestro.b ("ok let's do that (recycle those sessions and kickstart the handover)"), as the first test of the [session handover protocol v1](https://github.com/SovereignWebsite/Site__Agent__Maestro/blob/dev/site/factory/dinis-cruz/account-a/notes/2026-11-25-session-handover-protocol.md). This session ran from 20 November; its context was at about half the window.

## What design.b is doing
- **Keeping the design standards** on this site: guidelines (2a five designs, the design chooser, presentations; 2b the wayfinder and agents as provenance), the rating (0 to 5), the maturity model (M0 to M8) and the brief template.
- **Briefing every new site before its first build** (record 2026-11-24__block-03), at /briefs/<label>.html, and keeping ratings.json current from design.b.rounds' rounds.
- **Not making new designs here.** Dinis, via b.abp and maestro.b (25 Nov 19:20 UTC): design work moves to another account. The account is not named yet. The b.abp attack-surface visuals brief is a cue for that account.

## What is open
| Item | With | Next |
|---|---|---|
| Hub map: keeper on each site, then the drawn map and the map in each design | hub.b | judge each tag via design.b.rounds; six groups are final (briefs/hub-map.html) |
| Lee-Elle Horowitz | her keeper | site at 3, M3; decks closed. Next: The Stage lessons first, mixed-direction Hebrew lines, her check of the Hebrew, her photos |
| Moving Van demo | its keeper | five designs from briefs/moving-van.html, then a first round |
| Car buyer | its keeper | each design's idea on the first phone screen; Service book rethought (briefs/car-buyer-mycar.html) |
| Wayfinder (guidelines 2b) | sites.b, hub.b | prototype on one person's site and one startup, then design.b.rounds, then decisions.b |
| Components proposal (token contract, local-model card) | factory.b | waiting on security.b and decisions.b; then guidelines 2c |
| review.sovereignweb.site | sites.b, factory.b | approved (block-03); site to be requested from its brief |
| design.b.rounds' wake | maestro.b or Dinis | every 2 hours 07:13 to 21:13 UTC (block-03); scheduled wakes are on hold |
| Dinis can | Dinis | look at the RiskMandate brochure (his yes is M5); look at Car buyer (removes its draft notice) |

## What I learnt (also in learnings.md)
- A five-design brief before the build works: Suno reached five real ideas in one round.
- Bare placeholders such as `<account>` in Markdown become HTML tags and break the deploy for everyone. Write them in backticks, and run `bash tools/check.sh` before every push.
- Read the push output: twice a rejected push hid unpushed work.
- Messages cross. For a change other agents build on (the hub's groups went 10, 6, 9, 6), give one written answer in the brief with its commit id, not a stream of replies.
- Check a bold interaction on a phone and with axe before briefing it (Lee-Elle's swiped tenses failed both).
- The build regenerates every agent's area index. Never commit another agent's area: restore it before committing (`git checkout -- site/factory/dinis-cruz/account-a`).

## What the next session must do first
1. Follow restart.md: make your key, publish it in a commit of its own, write a heartbeat in agent.json.
2. Read this file, now.md and the table above; read notifications.
3. Answer maestro.b's checklist (signed push, key published, keys received, wakes, questions).
4. Make no new designs until Dinis names the design account; then write that hand-over.

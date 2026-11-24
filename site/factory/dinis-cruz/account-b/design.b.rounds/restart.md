# design.b.rounds: how to restart

A fresh session continues from here:
1. Read `now.md` (where every site stands) and `decisions.md`.
2. In the repository SovereignWebsite/Site__Agents__Design (`dev`), read `docs/rating.md`, `docs/maturity.md`, `docs/synthetic-users.md` and `docs/back-office.md`.
3. The tools: `tools/audit.js`, `tools/site-checks.js`, `tools/agent-area.js`, `tools/build.py`. Commit signed, with `Agent: design.b.rounds@SovereignWebsite.dinis` and `Claude-Session:` trailers.
4. On a wake: list each site's live commit against its last round in `docs/rounds.json`; round at most two changed ones, worst rated first; otherwise skip in one line. Update this area.
5. Read the notifications; act on each agent's next real change.

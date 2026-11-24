# design.b.rounds: decisions I work by

- **Keeping a 4** (design.b, 23 Nov 2026, `docs/rating.md`): once at 4, a site keeps it unless a measured check fails or two runs in a row fall below the line.
- **Pace** (design.b, 23 Nov 2026, `docs/back-office.md`): a site on a plateau gets a round only after a real content change.
- **Do not block on Dinis** (Dinis, 23 Nov 2026, 23:08 UTC, via conductor.b): leave each site in a state he can continue; send conductor.b one line only for what is truly his.
- **Owners' sites** (Dinis, ask 31, 23 Nov 2026): may be listed on our website, without naming the first handed-over site's owner for now; no marketing.
- **The price for changes after handover** (Dinis, ask 29, 23 Nov 2026): agreed after the handover; it blocks no one.
- **Use the website to find things** (Dinis, 24 Nov 2026, 00:16 UTC, via conductor.b): this area is kept up to date at each wake.
- **Agent area current** (Dinis, 24 Nov 2026, via conductor.b; written in `docs/rating.md` by design.b, dc62a21): a stale or missing area holds an agent site at 2. I check it with `tools/agent-area.js`.
- **Asking Dinis** (conductor.b, 24 Nov 2026, record 2026-11-24__decision-requests, relayed by design.b): commit a signed request at `site/decisions/requests/YYYY-MM-DD__slug.json` with context, flags, options and a recommendation; send decisions.b only its link; follow decisions.agents.sovereignweb.site /requests/, /blocks/ and /records/. Messages carry links and ids only.

# design.d: now

Updated 24 November 2026, 15:05 UTC.

## Sites

| Site | Rating | Round | Last checked | Next |
|---|---|---|---|---|
| Streaming | 4 (signed off, notes) | 5 (22 Nov 2026) | 50add78 (v0.1.24), 24 Nov 09:05 UTC; up to 0fb7927 (v0.1.28) only README, CI and docs/keeper changed | the share card |

Reviews: [round 1](/reviews-streaming-2026-11-22-round-1.html), [2](/reviews-streaming-2026-11-22-round-2.html), [3](/reviews-streaming-2026-11-22-round-3.html), [4](/reviews-streaming-2026-11-22-round-4.html), [5](/reviews-streaming-2026-11-22-round-5.html). The round record: [streaming.json](/data/rounds/streaming.json).

## Open

- **Waiting on Dinis, in this session:**
  - the version chip line in site/policy/policy.css (`footer .sws-version{opacity:1;color:var(--fg)}`): this site has not published since 21 November, because axe fails on /policy/;
  - this area in design_d's paths in site/policy/abp.json;
  - whether design.d's key also goes in site/key.json (pages.yml).
- **Waiting on streaming.d, after Dinis:** Streaming's own share card.

## Contradictions noticed

- CLAUDE.md (refreshed from SovereignWebsite__IaC, cd14199) says each agent commits in its own area here; site/policy/abp.json gives design_d only its review paths and does not list this area. I followed CLAUDE.md for this area and asked Dinis to add it to the policy.

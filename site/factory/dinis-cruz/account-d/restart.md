# design.d: how to restart

A fresh session of design.d continues from here:

1. In SovereignWebsite/Site__Agent__Design (dev), read CLAUDE.md, START.md, docs/briefing-design-d.md, docs/guidelines.md, docs/rating.md, docs/synthetic-users.md, then this area: agent.json, now.md, role.md.
2. Make a new key with `bash tools/setup-signing.sh design.d@SovereignWebsite.dinis <session-url>`. A new session key needs its own first commit of only site/keys/design.d.json (or an entry in SovereignWebsite__IaC team/keys.json through conductor.d); then update key_fingerprints in agent.json. Push nothing until the key counts.
3. Sign every commit, with `Agent: design.d@SovereignWebsite.dinis` and `Claude-Session: <url>`. Push to dev only. Times only from `date -u`.
4. Before every push, run what the deploy runs: `python3 tools/build.py`, `node .github/ci/build.mjs`, `node .github/ci/share-check.mjs _site`, `SWS_OWN_SITE=1 node .github/ci/quality.mjs _site`, `npx --yes html-validate@8.24.0 --config .github/ci/htmlvalidate.json "_site/**/*.html"`; restore site/reviews.html and remove _site before committing. Push only if every check passes.
5. Compare Site__Tool__Streaming's dev with the last commit checked in now.md. Run a round only if the live site changed for a visitor.
6. Tell conductor.d (session_015gaHdbX954ByXJf8LH5FLL), streaming.d (session_015gaHdbE7t4XNf21L7neufF) and synthetic-users.d (session_015gaHddQiB4aYZWXjfs16rM) that you are back.

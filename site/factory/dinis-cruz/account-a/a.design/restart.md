# a.design: how to restart

A fresh session of a.design continues from here:
1. In SovereignWebsite/Site__Agent__Design (`dev`), read CLAUDE.md, START.md, then this area: agent.json, now.md, role.md.
2. Make a new key with `bash tools/setup-signing.sh a.design@SovereignWebsite.dinis <session-url>`. Its first commit holds only site/keys/a.design.json (replacing this one); then update key_fingerprints in agent.json. Set `git config user.name a.design`.
3. Times only from `date -u`. Sign every commit, with `Agent: a.design@SovereignWebsite.dinis` and `Claude-Session: <url>` trailers. Push to dev only.
4. Reviews: write `reviews/<site>-<date>-round-<n>.md`, then `python3 site/factory/dinis-cruz/account-a/a.design/build.py` makes the `.html` beside each `.md` (and `picker.html`, `reviews/index.html`) with the site's own page shell from tools/build.py. Run `python3 tools/build.py` too, since it rebuilds this area's index.html.
5. How I review: serve or open each design at 390 x 844 and 1366 x 900, light and dark, with Playwright (pre-installed) and axe-core (npm i axe-core in the scratchpad). The script is `audit.js` in this area. Look at the screenshots yourself; never rate from numbers alone.
6. Before every push, run `bash tools/check.sh` (CLAUDE.md): it runs each check the deploy runs. Never a bare word in angle brackets in a .md here (it renders as a tag).
7. Read now.md for what is open, then tell a.maestro (session_018yvwtLiem1AqdA1YkKse4h) and a.sites (session_018yvwtQ7z3PUt9L5gpZCNzt) that you are back, and each keeper with a review open.

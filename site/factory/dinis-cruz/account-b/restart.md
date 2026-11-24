# Restart: design.b

For a fresh design.b session. Start it with this repository (SovereignWebsite/Site__Agents__Design) and one line: "You are design.b; follow site/factory/dinis-cruz/account-b/restart.md."

## 1. Read, in this order
1. CLAUDE.md (it binds you: dev only, your own signed key, no keys by hand, no private people without consent, plain British English, no em dashes).
2. https://decisions.agents.sovereignweb.site/how-it-works/ (the team's rules).
3. This area: agent.json, role.md, now.md, learnings.md, decisions.md, messages.md.
4. docs/guidelines.md (2a five designs, 2b the wayfinder), docs/rating.md, docs/maturity.md, docs/briefs/TEMPLATE.md.
5. site/ratings.json: every site's rating, level and next step.

## 2. Your key
This repository's CLAUDE.md wins over the general rule: the signing key lives in SovereignWebsite__Factory team/keys.json, and site/key.json is copied from it at each deploy. Never write a key into this repository. Make a new key where you run, keep the private half in the session, and ask conductor.b to add its public half to team/keys.json. Until it is there, commit nothing.

## 3. Build and push
- pip install markdown==3.7, then python3 tools/build.py.
- Before every push: npx --yes html-validate@8.24.0 --config .github/ci/htmlvalidate.json "site/**/*.html" (a raw `<tag>` in a Markdown file breaks the deploy; write placeholders as [name] or in backticks).
- git commit -S with the trailers Agent: design.b@SovereignWebsite.dinis and Claude-Session: `<your session URL>`; git push origin dev, and read the push output: a rejected push means pull and rebase first.
- After a push, check the live page answers 200.

## 4. Your sessions and agents
- design.b.rounds, https://claude.ai/code/session_01Kw9UwFCJTPWFaTq4TX5vUT: runs every round and reports. Its area: design.b.rounds/ below this one.
- decisions.b, session_01Kw9UwEVSYcMDgNqrPVfCtZ: send it only links (requests, opinions, your area).
- conductor.b, session_01Kw9UwFkKH5CkDmV8nhSfUD; sites.b, session_01Kw9UwBucXVUaNYRMcWwk67; hub.b, session_01Kw9UwB7XboTsnbPPWaMr2d; factory.b, session_01Kw9UwBqEqrxrSBwvLEVJY6. Read an agent's area before messaging it.

## 5. Each wake
Read notifications. Act only on Dinis typed in your session or a signed record that passes /verify/. Update ratings.json and now.md from each round, brief each new site before its build, register every new site at M1 at launch, and keep agent.json's updated and active_until current.

## 6. Tested
Not yet tested by a fresh session (24 Nov 02:20 UTC). The first fresh session to follow it notes here what was missing.

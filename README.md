# Site__Agent__Design

The repository behind **https://design.agents.sovereignweb.site/**, kept by design.b@SovereignWebsite.dinis, the design agent of the SovereignWebsite organisation. It holds the design standards every site is built and rated against, and the record of every design round.

## What is here

| Path | What it is |
|---|---|
| `docs/guidelines.md` | The design guidelines: five designs (2a), the wayfinder (2b), layout, colour, accessibility, voice |
| `docs/rating.md` | The design rating, 0 to 5, and the measured checks every round runs |
| `docs/maturity.md` | The maturity model, M0 (requested) to M8 (professional) |
| `docs/briefs/` | One-page site briefs, written before each site's first build; `TEMPLATE.md` to start from |
| `docs/reviews/`, `docs/runs/` | Every round's review and synthetic-user run |
| `site/ratings.json` | Every public site's rating, maturity level and next step: the data behind the Sites and Maturity pages |
| `site/factory/dinis-cruz/account-b/` | design.b's own area: agent.json, role, now, learnings, decisions, messages, restart |
| `site/decisions/` | design.b's decision requests and panel opinions |
| `tools/build.py` | Builds the HTML pages in `site/` from `docs/` and `ratings.json` |
| `.github/` | The Factory's site pipeline: build, checks, version tag, deploy |

## Build and check

```
pip install markdown==3.7
python3 tools/build.py
npx --yes html-validate@8.24.0 --config .github/ci/htmlvalidate.json "site/**/*.html"
```

The built HTML is committed. On push to `dev`, the pipeline runs the share-card check, quality checks, html-validate and axe, tags `v0.1.N` and deploys. A failing check deploys nothing.

Write placeholders in Markdown as `[name]` or in backticks: a bare `<name>` becomes an HTML tag and fails html-validate.

## What not to touch

- `site/key.json`: copied from SovereignWebsite__Factory `team/keys.json` at each deploy. Never write a key here.
- `.github/`: the Factory's pipeline; changes go through the Factory.
- `main`: work goes to `dev` only.
- Another agent's area or opinion files: each agent changes only its own.

## Who changes what, and who reviews

- design.b writes the guidelines, rating, maturity model, briefs and ratings. design.b.rounds writes the reviews, runs and its own area.
- Every commit is signed with the author's own key and carries `Agent:` and `Claude-Session:` trailers. Rules for agents working here: `CLAUDE.md`.
- A human contributor opens a pull request to `dev`. design.b reviews design content, and security.b reviews anything touching checks, keys or the pipeline.
- Decisions that need Dinis Cruz go through decisions.b: https://decisions.agents.sovereignweb.site/ask/

## Start here

For a fresh design.b session: `site/factory/dinis-cruz/account-b/restart.md`. For anyone else: the live site's [Maturity](https://design.agents.sovereignweb.site/maturity.html) and [Sites](https://design.agents.sovereignweb.site/ratings.html) pages show where everything stands.

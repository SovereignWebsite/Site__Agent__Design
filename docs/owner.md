# What you can do here yourself

For Dinis Cruz, and anyone he hands this site to. Nothing on this page needs design.b or design.b.rounds to be running. Everything here is plain files in one repository, built by one script.

## Where it lives

- **The repository:** SovereignWebsite/Site__Agents__Design on GitHub, branch `dev`. The pages are built from `docs/` and `site/ratings.json` into `site/`.
- **To rebuild the pages** after any change: `python3 tools/build.py`. It needs only Python 3.
- **To change anything,** ask your own AI in plain words, in a session on this repository: "change the rating of car-buyer to 4", "add a guideline about captions", "show me which sites are at M3". It edits the files, builds and commits.

## Things you can change

| You want to | Edit | Then |
|---|---|---|
| Change a site's rating, maturity or what blocks it | `site/ratings.json` (one entry per site address) | build |
| Change what a rating means, or the rules for keeping a 4 | `docs/rating.md` | build |
| Change the maturity levels M0 to M8 | `docs/maturity.md` | build |
| Change the design guidelines every site follows | `docs/guidelines.md` | build |
| Change the brief every agent reads before touching a page | `docs/brief.md` | build |
| Change how the synthetic users are run, or their questions | `docs/synthetic-users.md` | build |
| Add or correct a review | a file in `docs/reviews/<site>/` | build |
| Add a reference site to learn from | `docs/examples.md` | build |

## Things you can run

Each runs on any machine with Node and Playwright, and only reads the live sites:
- **`node tools/audit.js <file of addresses> <folder>`**: axe at phone and desktop size, light and dark, plus sideways scroll, one h1, page weight and anything loaded from another host. It writes `audit.json` and screenshots.
- **`node tools/site-checks.js <address>`**: the seed rules (the start, agents, llms.txt and admin pages, link previews, the 1200 x 630 share card) and rule 2a (a visible chooser with five designs).

## Things you can decide, and where they are written down

- **A rating:** the rubric is in `docs/rating.md`. Your word overrides it; write the decision and the date into the site's entry in `site/ratings.json`.
- **An owner's sign-off (M5):** a site moves to M5 when its owner has seen it and said yes. Record the date in `site/ratings.json`; the site's own agent removes its draft notice.
- **The pace:** design rounds run only after a real content change (decided by design.b, 23 November 2026, in `docs/back-office.md`).

## Where each site stands

[Where each site stands](ratings.html) and [maturity](maturity.html) are rebuilt from `site/ratings.json`. Every round, with the commit it looked at, is in the [back office](back-office.html).

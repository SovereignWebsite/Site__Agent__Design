# Brief: the hub sells (hub round 8 onwards)

From design.b, 23 November 2026, for hub.b, with strategy.b and outreach.b.

## The goal, in Dinis's words

"I need to be able to show this site to somebody and they say 'I want one'."

Rounds 1 to 7 fixed the craft: first screens, phone folds, page weight, and the start, agents and admin pages. The hub still reads as a register of addresses, and nothing on it sells. From this round on, one test decides every change: does a stranger who sees the page for thirty seconds want one?

## Why visitors say no (round 8 baseline)

The personas said no for these reasons, most common first:
1. No price, no form, nothing to do: 6 of 18 noes.
2. Only one site has been handed over (4).
3. Hard to read: forced dark themes and cut-off text (4).
4. The portfolios can't be seen (2).

The two biggest levers are Dinis's to pull: where "I want one" leads, and the price to quote (strategy.b to propose).

## The one question

The synthetic users now answer one question per design: "Would you want one? If not, why not?" A design is rated 4 only when four of the five personas say yes in two runs in a row.

## The case, in five seconds

The first screen says one sentence and shows one thing:

- The sentence: "Your own website, made for you by an agent team, in five designs. Yours to keep."
- The thing: one real person's site, shown live in its five designs, cycling or side by side. Kate's site first, because she edits it herself on GitHub, and that is the proof.
- One action: "I want one".

Nothing else goes above the fold: no counts, no section links, no family menu beyond the small top-right one. The one exception is a quiet secondary link, "Can it do X?", to /features/. That page lists each feature with its status, live examples, the agent working on it, and what holds it up. It answers questions like Dinis's "is there support for Spotify?".

## The page, top to bottom

1. **The case**, as above.
2. **What you get.** Five items, each linked to a live example:
   - a site about you, with your own address;
   - five designs to choose from (Emily);
   - your files on your own GitHub, yours to keep (Kate);
   - changes made by talking to your AI (Kate's /agents/);
   - a start page and an admin page with your numbers.
3. **Own, not rent.** A table comparing us with Wix, Squarespace, a WordPress host and Fliplet on: who holds the files, whether you can leave and take the site, and the monthly price. Use only published facts, each with its source link and the date it was checked. Leave a cell empty rather than guess. Source: IaC board/2026-11-19__saw-plan.md, then each vendor's own pricing page.
4. **The people.** The eleven people's sites as the showroom: a face, a name, one line on what they do, and one tap to open the live site. Startups, demos, providers, businesses and tools move to /more/.
5. **How you get one.** The Line's six stations, from one request to handed over, with "Get one" as the last station.
6. **I want one**, again, at the end.

## The five designs

The five designs keep their ideas, and each must now sell. They are judged on the one question.

Home is decided by the numbers: hub.b shipped The Line with the case screen as home (v0.1.35, 4f23d10) and design.b.rounds is testing it now. If it beats The Street's 3/5, it stays. Before the case screen, design.b recommended **The Street**. In the baseline run of round 8 (v0.1.32, 5033da0), three of the five personas said they would want one after seeing it; every other design got one. Its idea fits the pitch: a high street where each person has their own shop, and a free plot at the end of the street for yours. The Line sold least, because its stations show "None at this step today" and only one finished site; it keeps its place as the "How you get one" section. Dinis can overrule this. (An earlier version of this brief recommended The Line, before the round 8 numbers came in.)

## "I want one" and the price (decided by Dinis, 23 Nov)

- "I want one" leads to feedback.b's box, a message form that replies without GitHub, at /start/#get-one.
- The price shown is the £50 offer (€50 on European sites), labelled as an offer, in strategy.b's wording; it goes live together with the feedback lane and the pricing.html change, not before. The £500 anchor is not printed.

Round 9 (1137c84): The Line with the case went from 1/5 to 3/5 and stays home. "I want one" satisfied none of the 25 personas before this decision.

### Before the decision

Where the action leads is Dinis's call. The options are:
- feedback.b's box, which takes a message and replies without GitHub;
- an email address;
- a named contact.

Until he answers, the action goes to /start/#get-one.

## Build order (one commit and one tag each)

1. The Street becomes home. Put the case first screen on it, with Kate's five designs, and an empty plot at the end of the street labelled "Yours" that leads to "I want one".
2. "What you get", with links to live examples.
3. People first, and the rest moved to /more/.
4. "I want one" at the top and the end, pointing to /start/#get-one for now.
5. Own versus rent. strategy.b supplies the facts and sources first.
6. Port the case and "I want one" into the other four designs.
7. The /admin/ dashboard.

## Rules that still hold

- Plain British English, with no em dashes and no hype words.
- No invented facts or prices; every claim has a source.
- Name only people who have agreed to be shown.
- axe clean, under 8,000 px on a phone, and light images.

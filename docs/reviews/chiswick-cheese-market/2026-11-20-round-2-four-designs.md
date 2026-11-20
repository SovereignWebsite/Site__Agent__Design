# Chiswick Cheese Market, round 2 (pass 1): a centre of gravity for each of designs 2 to 5

design.b.rounds@SovereignWebsite.dinis, 20 November 2026, about 22:30 UTC, for chiswick-cheese-market.b. Dinis, in that session at 22:05 UTC, verbatim: "please as the design we agent to also do a couple passes, since each extra design need to have its own conter of gravity, focus, UX and design". This is pass 1. Pass 2 is a review of the built result, live, at 390 and 1366 px with the synthetic users, as soon as it deploys. Deadline: Sunday 22 November.

**The rule for all four.** Each design is about one thing, and the home page is built round it. The routes stay the same, so "Choose a design" keeps its place, but each design draws its home page, its stallholders page and one stallholder in its own order and its own way. Use real data only; there is no stall plan and there are no locations.

## How the four differ

| | Centre of gravity | First screen (390 px) | Moving through it | Its signature component |
|---|---|---|---|---|
| 2 The Market Paper | **The news**: what happened at the market and what is next. | The masthead, today's date line and the lead story's headline with its picture. | Read down like a paper: lead, then "Latest", then the stallholder index at the back. | A broadsheet front page with columns and rules. |
| 3 The Poster Wall | **The next market day**, as an event. | The date, huge, "20 DEC", on a pasted poster. | Scroll a wall of whole posters, then a big year calendar; one tap to "Getting here". | Posters pasted up, slightly turned, with tape. |
| 4 The Cave | **The cheese**: tasting and the makers as craftspeople. | A dark cave, one sentence of welcome and the first shelf of cheeses. | Shelf by shelf (one per kind of stall); each round opens its maker. | Shelves of round "cheeses", each a maker's photograph with a gold label. |
| 5 The makers (stays the favourite) | **Finding a stall.** | "Next market · Sunday 20th December", the search box and the chips. | Search or tap a kind, open a maker, go back; a tab bar on phones. | The finder, plus the market by kind as a row of counts that filters it. |

## 2 The Market Paper

**Centre: the news. Focus: the lead story. UX: read top to bottom; nothing is hidden behind a tap.**

Home page order:
1. **The masthead.** The site name in Fraunces at `clamp(40px,10vw,96px)`, centred, between two rules (3px above, 1px below). Above it is a dateline strip: left, "Sunday 20th December 2026: the next market"; right, the snapshot date ("Edition of 20 November 2026").
2. **The front page.** On desktop it is a 3-column grid (`grid-template-columns:2fr 1fr 1fr`, with 1px column rules from `border-left`):
   - the lead story (picture, kicker, headline at `clamp(30px,5vw,56px)`, standfirst) takes column 1;
   - "Latest" (four briefs) takes column 2;
   - column 3 is a boxed "This Sunday" panel: the date, the hours and the address, from the home page's own words, with the "Getting here" link.
   On phones it is one column in the same order, with the panel moved directly under the masthead.
3. **"From the market"**: the market's own introduction set as a feature, in two columns on desktop (`column-count:2;column-gap:32px;column-rule:1px solid var(--rule)`), with a drop cap.
4. **The calendar as a listings box**: the 2026 dates in a ruled table, with past dates struck through.
5. **Classifieds at the back**: the stallholders A to Z in 3 columns (`column-count:3`, 1 on phones), each with its kind in small capitals.

Stallholders page: one ruled list per kind, like a directory page, each with a thumbnail, the name and the first line.
One stallholder: a long read, with the kicker, the headline and the picture full width, a drop cap, and "More from the market" (two other stalls of the same kind) at the foot.

```css
.d2 .front{display:grid;gap:0 28px;grid-template-columns:1fr}
@media(min-width:60rem){.d2 .front{grid-template-columns:2fr 1fr 1fr}.d2 .front>*+*{border-left:1px solid var(--rule);padding-left:28px}}
.d2 .this-sunday{border:2px solid var(--ink);padding:16px;align-self:start}
.d2 .this-sunday b{display:block;font:600 clamp(28px,6vw,40px)/1 'Fraunces',serif}
.d2 .classifieds{column-count:1;column-gap:28px;column-rule:1px solid var(--rule)}
@media(min-width:40rem){.d2 .classifieds{column-count:3}}
```

## 3 The Poster Wall

**Centre: the next market day as an event. Focus: the date. UX: a wall to scroll past, then one clear action.**

Home page order:
1. **The date poster.** A full-width black poster with the yellow tagline word "CHEESE" and the date at `clamp(120px,32vw,320px)` in Bebas: "20" on one line, "DEC" on the next. Below it, "Sunday 20 December 2026 · 9.30 am to 3.00 pm · Old Market Place". One button: "Getting here".
2. **The wall.** The market's own posters and feature pictures, each shown **whole** (`object-fit:contain`, no cropping), on a wall of grey board (a `background` of 2px noise from a repeating gradient), each slightly turned, with a tape strip. Two columns on desktop and one on phones.
3. **The year.** Twelve boxes, one per market day, with past dates struck through and the next one in yellow (this exists; keep it).
4. **Stalls by kind**: the counts as big numbers (this exists; keep it), with the run-on list of names under it.
5. **The journal** as a type list (this exists).

Remove the split hero (the tagline beside a cropped poster): the date is the hero.

```css
.d3 .wall{display:grid;gap:40px 28px;grid-template-columns:1fr;padding:40px 16px;background:#d9d6cf repeating-linear-gradient(45deg,#0000 0 3px,#0000000a 3px 4px)}
@media(min-width:48rem){.d3 .wall{grid-template-columns:1fr 1fr}}
.d3 .wall figure{position:relative;margin:0;background:#fff;padding:10px;box-shadow:0 10px 24px #0004;transform:rotate(-1.2deg)}
.d3 .wall figure:nth-child(even){transform:rotate(1deg)}
.d3 .wall figure::before{content:"";position:absolute;top:-12px;left:50%;width:96px;height:26px;margin-left:-48px;background:#fff8;box-shadow:0 1px 2px #0002;transform:rotate(-3deg)}
.d3 .wall img{width:100%;height:auto;object-fit:contain}
@media(prefers-reduced-motion:no-preference){.d3 .wall figure{animation:paste .5s ease-out both}@keyframes paste{from{opacity:0;transform:translateY(16px) rotate(0)}}}
.d3 .date-poster b{display:block;font:400 clamp(120px,32vw,320px)/.82 'Bebas Neue',sans-serif}
```

## 4 The Cave

**Centre: the cheese and its makers. Focus: the first shelf. UX: shelf by shelf; each shelf scrolls sideways on phones.**

It is dark first: the "Cellar" was mostly cream in light mode, which the critic noticed. Make the dark cave the default in both schemes, or keep parchment for light but start the home page on a dark band.

Home page order:
1. **The welcome.** A dark band (`#15110d`) with one line in Playfair italic at `clamp(32px,7vw,64px)`, the tagline. Under it, the next market in gold capitals: "Next market · Sunday 20 December 2026". No photograph behind the text; this solves the readability fault.
2. **The shelves.** One shelf per kind of stall, with the kind's name and count as a gold label on the shelf edge. Each maker is a **round** (`border-radius:50%`, `aspect-ratio:1`, the maker's own photograph, `object-fit:cover`), 120 px on phones and 160 px on desktop, with the name under it in small capitals. Each shelf is a wooden ledge (a 10px `border-bottom` in a dark brown gradient, with a soft shadow below).
   - On phones, a shelf scrolls sideways inside its own region: `overflow-x:auto`, `scroll-snap-type:x mandatory`, with `tabindex="0"` and `role="region"` plus `aria-label` (for example "Cheese producers and mongers, 22").
   - On desktop the rounds wrap.
3. **Tasting notes.** The journal's posts in the "Tasting Notes" category (it exists), as small parchment cards on the dark ground.
4. **Market days**: the two-column list, with past dates struck through (fix 15).

Stallholders page: the same shelves, all kinds. One stallholder: the round at 280 px, centred, with the name in Playfair, the description in a parchment card, and "On the same shelf": that kind's other rounds.

```css
.d4 .shelf{margin:0 0 40px}
.d4 .shelf h2{font:600 13px 'Inter',sans-serif;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);margin:0 16px 10px}
.d4 .shelf ul{list-style:none;margin:0;padding:12px 16px 18px;display:flex;gap:18px;overflow-x:auto;scroll-snap-type:x mandatory;border-bottom:10px solid #3a2616;box-shadow:0 14px 18px -10px #000c}
@media(min-width:60rem){.d4 .shelf ul{flex-wrap:wrap;overflow:visible}}
.d4 .shelf li{flex:0 0 auto;width:120px;scroll-snap-align:start;text-align:center}
@media(min-width:60rem){.d4 .shelf li{width:160px}}
.d4 .shelf img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:50%;box-shadow:inset 0 0 0 4px #e9d9b0,0 6px 14px #000a}
.d4 .shelf a{color:#f2e7d4;text-decoration:none;font:600 12px/1.3 'Inter',sans-serif;letter-spacing:.06em;text-transform:uppercase;display:block;min-height:24px}
```

## 5 The makers (the favourite: sharpen it; do not change its idea)

**Centre: finding a stall. Focus: the search box. UX: search or tap, open, back; a tab bar on phones.**

1. Keep the first screen as it is: the pill, the heading and the finder, which must be inside the first 844 px on a phone. Today "Most recently added" comes before the finder; **move the finder up**, directly under the heading.
2. Replace the figures line ("40 stalls 5 kinds 103") with **the market by kind** as a row of five counted chips that filter the finder (the chips exist; give them their count in a large numeral): 22 cheese producers and mongers, 18 cheese accompaniments, 3 made with cheese, 2 cheese accessories, 1 hot food. That is the data's own categories; a stall can be in two.
3. "Most recently added" moves below the finder, as a horizontal row.
4. One stallholder (this exists, and the personas liked it): keep the journal mentions and "similar stalls".
5. Keep the note on what the data does not have yet. It is honest, and the organiser persona trusted it.

## The pass for all four

- **One entrance motion each,** under 600 ms and none under `prefers-reduced-motion`: the posters settle (3), the rounds fade in shelf by shelf (4), the columns rule in (2). Design 5 has none; it is a tool.
- **Phones first:** check each at 390 px, and at 320 px for no sideways scroll, apart from the Cave's shelves, which scroll inside their own focusable region.
- **Every picture whole** where it is a poster or a notice (no text cut off); crop only photographs.
- **The footer names the idea:** "Design 4, The Cave: the makers as cheeses on shelves".

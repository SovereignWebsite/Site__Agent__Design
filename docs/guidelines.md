# Sovereign Website design guidelines

First draft, design.b@SovereignWebsite.dinis, 20 November 2026 (10:33 UTC). Not yet agreed by Dinis Cruz. Every rule here is a proposal until he says yes. "Must" is a sign-off condition; "should" is a strong default that a site's design agent may break with a written reason.

Starting point: design 1 of sovereignwebsite.ai, "the plain promise", chosen by Dinis on 20 November 2026 (SovereignWebsite__Website site/theme.css). The other sites are measured against these rules in design/reviews/.

## 1. What a site must never do

These are absolute. A site that breaks one is not signed off.

1. No cookies, no tracking, no analytics, no fingerprinting, no third-party pixels.
2. No request to another host on page load: no web fonts, scripts, styles, images, iframes or embeds from anyone else.
3. A third-party service is allowed only when the owner chooses it, and then only on a visitor's action, with the page saying beforehand what is sent and to whom. Site__google-maps is the reference: nothing goes to Google until the button is pressed, and the page says so next to the button. Such a site must carry a Content Security Policy that names only those hosts.
4. No server code, no database, no forms that post to us. Static files only.
5. No dark patterns: no pre-ticked boxes, no countdowns, no fake scarcity, no hidden cost, no confirm-shaming.
6. No invented facts, prices, customers, testimonials, logos or numbers. A proposal is labelled as one where it is shown (the .ai "Proposal only" tag is the pattern).
7. No private person named without their consent. Made-up examples are labelled made-up.
8. No horizontal page scroll at any width from 320 px.
9. No text in images; no image without `alt` (empty `alt=""` for decoration).
10. No em dashes or en dashes in text.
11. Browser storage only for what the visitor asked to keep, and the page says so (the Vault's "kept here, in this browser's own storage, until you forget them" is the pattern).
12. **On a customer's site, the page is about the owner, not about us** (Dinis Cruz, 20 November 2026: "This website is for them... not a website about us"; and on the first fix: "better Too much. It needs to fundamentally be about the site and who is it about. I'm happy that just shows on some top right pop-up menu."). Our links (the Sovereign Website family) appear **only in one small pop-up menu at the far top right**, after the owner's own navigation and "Choose a design": a button that opens a list, closed by default. No family bar, strip or row of our links anywhere on the page; a small footer credit is optional and the owner may remove it. Any review that finds our links outside that menu fails. Our own organisation sites keep the family bar.
13. **Every customer site has three pages, and each is easy to find** (Dinis Cruz, 20 November 2026: "those links need to be very visible"):
    - `/start/`: where to start, for the owner, including connecting GitHub and their own Claude;
    - `/agents/` and `/llms.txt`: how to use this site with an AI, as on yiheng-wang.agenticcells.site;
    - `/admin/`: how the site was made: its agents, design rounds, commits and synthetic-user runs (it can link to or pull `rounds/<site>.json` on design.agents.sovereignweb.site).
    They are linked in the header's right-hand area or directly under the hero, and again in the footer; on a phone, in the menu. A review fails if one is missing, answers anything but 200, or is hidden.
14. **Every page has a link preview** (Dinis Cruz, 20 November 2026: "we are missing the social media link preview image"): `og:title`, `og:description`, `og:type`, `og:url`, `og:image` (absolute URL), `og:image:alt`, `og:image:width` and `og:image:height`, plus `twitter:card` (`summary_large_image`), `twitter:title`, `twitter:description` and `twitter:image`. The share image is 1200 x 630, made from the owner's own cleared material, served from the site itself. design.b's audit fetches it and fails the review unless it answers 200 at 1200 x 630.

## 2. The family and the site

Every site is two layers:

- **The family layer** (the same everywhere): the family bar, the base tokens, the type scale, spacing, focus style, footer facts. It lives once, in the Factory seed (`seed/shared/`), and every site copies it unchanged.
- **The site layer** (its own): accent colour, headline face, hero, illustrations, voice details. A customer's site is mostly site layer; its owner's taste wins inside the rules.

The SovereignWebsite organisation's own sites (.ai, .org, .site, hub, vault, demos) should share one identity, taken from design 1: warm paper background, terracotta accent, serif headlines, system sans body. Proposal, for Dinis: either all own sites move to design 1's palette, or .ai keeps terracotta and the infrastructure sites take a named sibling palette from the same family. Today they are two unrelated looks (see review).

## 2a. Five designs, always

Every site has five designs (Dinis Cruz, 20 November 2026: "a key requirement is 5 designs"). They show what the team can do and let the owner choose. They live in `site/designs/1.html` to `5.html` with an index, one tap apart, as on sovereignwebsite.ai; the chosen one becomes `site/theme.css`. The five must differ in idea, not only in colour, and **each idea comes from the owner's own world**, as on the AgentiCCells personal sites (examples page): a filmmaker's Premiere, a composer's Cue Sheet and Record Sleeve, a pastry chef turned project manager's Pass, with her results as order tickets on a rail. Each design is named for its idea and **rebuilds the page around it**: the structure, the hero, the order of sections and the way facts are drawn change, not just colours and fonts. Five skins of one layout do not count as five designs. At least one should be designed dark first, and one should be the plain, printable version (a Brief) for people in a hurry.

Concept first, then craft: before any CSS, write for each design one sentence saying what it is a metaphor for, and which of the owner's own facts it will draw (a timeline, a cast list, a map, a set of tickets). Nothing drawn may be invented. Each of the five meets every rule in this document, light and dark, before it is shown. A site without five designs is rated no higher than 2 (rating.md, level 3 needs them).

### The design chooser (Dinis Cruz, 25 November 2026)

Dinis, in b.site.lee-elle-horowitz's session, of a switcher made of text pills and a compare page of symbol tiles: "this is wrong ... it should be like" Emily Cruz's and Grace Farrell's sites, "so that other sites.* agents don't make these mistakes". Every site's chooser works like theirs:

1. **One "Choose a design" button** in the top bar, next to the language switch if there is one. Never a row of pills or tabs.
2. It opens a panel showing **every design as a real screenshot of that design**, in the page's own language, each card with its number, name and one-line idea. No abstract symbols, swatches or icons in place of the screenshot.
3. **The current design is outlined.**
4. At the bottom of the panel, a link **"All five, side by side"** goes to a compare page built from the same screenshot cards.
5. **On a phone**, the panel shows two cards per row, and the top bar stays on one line, with nothing cut off.
6. **The screenshots are refreshed whenever a design's look changes**, as part of the build (for example, a script that screenshots each design, as on Lee-Elle Horowitz's site: tools/designs/thumbs.mjs).

design.b.rounds checks the chooser in every round: the button is present, the panel shows a screenshot for each design, and the screenshots match the live designs.

### Presentations (decks) on a site (Dinis Cruz, 25 November 2026)

From Dinis's review of Lee-Elle Horowitz's guided tours ("pic2 looks very vanilla"; "more meat ... collage or multiple pages or parts of the site"; "explain the philosophy and the concepts and the thinking behind it"). The full brief: [the two decks](briefs/lee-elle-horowitz-decks.html). For every site's decks:
- several layouts (cover, statement, collage, why, side by side, mirror, graph, close), never one template for every slide;
- each design's slide wears that design, with a collage of real screenshots;
- every design slide says why that choice fits the owner;
- the close shows what we can do, claiming only what is live;
- the PDF has no drop shadows, one 16:9 slide per page, and a file name for sharing.
- two layout traps measured on Lee-Elle's decks (5d9eb41): a grid whose auto column holds a size-contained frame (`container-type: inline-size`, centred with `place-items: center`) collapses to a fraction of its width, so use `grid-template-columns: minmax(0, 1fr)`; and forced page breaks can add blank PDF pages in Chromium, so give each slide a fixed, clipped height instead.

## 2b. Navigation: one browsing experience (Dinis Cruz, 23 November 2026)

Dinis, record 2026-11-23__navigation-and-review, "super critical": "every website almost, I should be able to navigate easily across every website, find the home, go up, go down, find the agent, connect with, etc. And have that browsing experience."

Every page of every site carries one shared component, the **wayfinder**. It is family layer: sites.b builds it once in the Factory seed with hub.b, and every site copies it unchanged. design.b owns its design and this rule.

**What it holds, left to right, in one slim bar at the top of the page:**

1. **Where you are**: a breadcrumb from the network to this page, for example Sovereign Website › People › Emily Cruz › Paintings. Each step is a link, so the step before the current one is **up**.
2. **Home**: this site's own home page.
3. **Below here**: a short menu of this page's children (the pages one level down), when there are any. Every site also lists all its pages at /sitemap/, linked from the footer.
4. **Next and previous**: the neighbouring sites in the same group (the next person, the next startup), so a reviewer can walk the whole group without going back to the hub.
5. **Agent**: the site's /agents/ page, which names the agent that keeps it and its session or contact.
6. **Connect**: the site's way to send a message (feedback.b's box once its lane is live; until then /start/#get-one).
7. **All sites**: the family pop-up, top right. It is the one place for links to other sites (the rule that sites are about their owner still holds), grouped as on the hub.

**Agents as provenance (Dinis, record 2026-11-23__briefings-keepers-messages: "for every find, I should be able to find the agents. You need to think of these as provenance and graphs").** From any page, the Agent step leads to the site's /agents/ page, which shows who made and keeps it as a small graph, every node a link:

- the site's keeper agent, and above it the chain it reports to (the domain's keeper, sites.b, the conductor and the maestro), up to Dinis;
- the agents that made this page, read from the `Agent:` trailers of the commits that touched it, each with the commit link;
- the decision records that shaped the site, each linked on decisions.agents.sovereignweb.site;
- the design rounds and the site's maturity level, linked to design.b.

Every page's footer adds one provenance line: the agent and the commit that last changed it, both linked. The graph is built from the repository and the registry at build time, never typed by hand, so it cannot go stale.

**Where the links come from.** One registry, sites.json on the hub, gives every site its name, group, parent, order, keeper agent (with the chain above it, as a tree from the domain keepers down), and connect address. It is copied in at build time, never fetched by the visitor's browser, so the CSP stays 'self' and the bar works offline and without JavaScript.

**How it must behave.**

- Plain links in a `nav` with `aria-label="Sovereign Website network"`; the menus are `details` elements, so it works without JavaScript.
- Every target is at least 44 px; visible focus; it reads in this order with a screen reader; `aria-current="page"` on the current step.
- At most 48 px high on a phone, and it never covers the owner's first screen: on a phone the breadcrumb shortens to "‹ up" plus the site's name.
- It takes its colours from the site's own tokens, so it suits all five designs and both colour schemes, and passes axe in each.

**How it is checked.** The site's pipeline checks, on every page, that the wayfinder is present, that it links to home, up, the agent and connect, and that every one of those links answers 200. design.b.rounds adds one question for the synthetic users: "From here, can you find the home, go up, find who looks after this site and send them a message?" Once the component ships in the seed, a site without it is rated no higher than 3.

## 3. Layout

- Mobile first: write the 360 px layout first, then add columns with `min-width` media queries. Test at 320, 390, 768, 1366 and 1920 px.
- One content width token, `--max: 68rem`, for page frames, and one reading measure, `--text: 42rem` (about 65 to 75 characters) for prose. The family bar, header, main and footer share the same outer edge.
- Side gutter at least 1rem (16 px) on phones.
- On phones the first screen must show the page's heading and its first sentence. The header, family bar included, must not take more than a quarter of an 844 px tall screen (about 210 px).
- Every page has: skip link, family bar, site header with the site's name linking home, `main` with one `h1`, footer.
- Primary navigation: at most six items. More pages go in the footer or a no-script disclosure menu (`<details>`), never into four wrapped lines.
- Grids use `repeat(auto-fit, minmax(min(100%, Nrem), 1fr))` so they collapse without breakpoints.
- Code blocks and wide tables wrap or scroll inside themselves, and a scrolling region is keyboard reachable (`tabindex="0"` with a label).

## 4. Type

- Body: the system sans stack `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`, 1.0625rem (17 px) minimum, line height 1.6 to 1.65. Never smaller than 16 px for body, 14 px for any text at all (the family bar's 12.8 px is the one exception to fix, see review).
- Headlines (design 1): the system serif stack `Georgia, "Iowan Old Style", "Times New Roman", serif`, weight 700. No downloaded fonts. A customer may bring a font file into their own repository; it is then served from their own host.
- Scale: `h1 clamp(2.1rem, 6.5vw, 3.6rem)` (design 1 hero up to 4.4rem), `h2 clamp(1.45rem, 3.6vw, 2rem)`, `h3 1.15rem`. Headline line height 1.05 to 1.2; body never below 1.5.
- Body text is `--fg`, not `--muted`. Muted is for secondary lines (captions, metadata, sources), never whole paragraphs.
- Eyebrow labels: small capitals by `text-transform`, `letter-spacing .12em`, at most one per section.
- Numbers in prices use the headline face and are always next to their label.

## 5. Colour and dark mode

- Colours are tokens on `:root`: `--bg --surface --fg --muted --accent --accent-soft --line --note`, plus `--field-border` for form controls. No raw colours outside the token block, except illustrations.
- Both schemes are required: light by default, dark under `@media (prefers-color-scheme: dark)`. Every page has `<meta name="color-scheme" content="light dark">` and `color-scheme: light dark` on `:root`, so form controls and scrollbars follow.
- Contrast, checked for both schemes:
  - text against its background at least 4.5:1, large text (24 px, or 18.66 px bold) 3:1;
  - `--muted` on `--bg`, `--surface` and `--note` at least 4.5:1;
  - button text on `--accent` at least 4.5:1;
  - borders of inputs, buttons and other controls at least 3:1 (WCAG 1.4.11). The decorative `--line` (about 1.3:1) is never a control's only edge.
- Never use `opacity` to make text lighter; set a colour that has been measured.
- Colour is never the only signal: the maturity levels carry their number and name as well as their colour.
- Design 1 tokens, measured: light muted/bg 7.1, accent/bg 5.7, accent/accent-soft 4.9; dark muted/bg 9.0, accent/bg 8.7. They pass.

## 6. Spacing

- A 4 px base. Use the rem steps .25, .5, .75, 1, 1.5, 2, 3, 4, 6.
- Section padding `clamp(2.2rem, 6vw, 4rem)`; hero `clamp(2.5rem, 9vw, 6rem)` top.
- Space between related items is smaller than space between groups. Headings sit closer to what follows than to what came before.

## 7. Components

Shared names, so every agent builds the same thing the same way. Reference implementations are in SovereignWebsite__Website site/style.css and theme.css.

| Component | Rule |
|---|---|
| Family bar | Same markup and CSS on every site, from `seed/shared/`. `aria-current="true"` on the current site. Links reach 24 px tall. |
| Header | Brand (mark and name) linking home, primary nav (six or fewer), language switch when there is more than one language. |
| Button | Solid accent for the one main action, outlined for the second. At least 44 x 44 px on touch screens. One main button per screen. |
| Link | Underlined in text. Navigation links may drop the underline but must show it on hover and focus. |
| Card | `--surface`, 1px `--line`, radius .6rem. A whole-card link has one link, on the heading. |
| Ticket (offer) | Design 1 dashed accent border. Only for an offer, and always with its label (Proposal only, Published anchor). |
| Note | `--note` background, 4px accent left border. For warnings and statements of what is not true yet. |
| Steps, levels, promises | Numbered lists (`ol`), the number from a CSS counter, never typed into the text. |
| Form field | Visible `label` above, 3:1 border, 16 px text minimum (prevents phone zoom), placeholder only as an example, never as the label. |
| Code | Monospace system stack, wraps or scrolls inside its own focusable box. |
| Footer | What the site does not do (no cookies, no tracking), its source, its licence, and where things stand. |

## 8. Accessibility (WCAG 2.2 AA)

Sign-off needs all of these, checked by axe-core and by hand:

- `lang` on `html` (`en-GB`, `pt-PT`), and `lang` on any phrase in another language.
- One `h1`; headings in order; landmarks `header`, `nav` (each labelled), `main`, `footer`; `aside` only at the top level.
- Skip link as the first focusable element.
- Visible focus on everything: `:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px }`.
- Targets at least 24 x 24 px or spaced so a 24 px circle on each does not touch another (2.5.8). Primary actions 44 px.
- Text resizes to 200 per cent and reflows at 320 px without loss (1.4.4, 1.4.10).
- Motion only under `prefers-reduced-motion: no-preference`.
- Status messages in `role="status"`; errors in text next to the field.
- Every page passes axe-core with no violations at "serious" or "critical", in both schemes, at 390 and 1366 px.

## 9. Performance

- First load, everything included: under 100 KB for a page of words; under 1 MB for a portfolio with images. Video and audio load only when the visitor presses play. Images: SVG where possible, otherwise AVIF or WebP with width and height set, `loading="lazy"` below the first screen.
- One stylesheet (or two: family and site). Inline CSS only for a single-page site.
- No JavaScript unless the page does something; a page that only shows words has none. Script, when there is one, is a file on the site's own host (CSP friendly), loaded with `defer`.
- A favicon (`favicon.svg`), a `description`, and a title of the form "Page, Site".

## 10. Writing voice

- Plain British English. Short sentences. The visitor is "you"; the team is "we" only where it is us.
- Say what is true now. What does not exist yet is said plainly ("Nothing is sold yet").
- Headlines are statements a person would say out loud, not slogans with no verb.
- Link text says where it goes ("How it works, step by step"), never "click here".
- Every claim from an article links to its source.
- No em or en dashes; no exclamation marks; no superlatives we cannot prove.

## 11. Sign-off

A site version is done for a customer only when design.b has recorded, in `design/reviews/<site>/<date>.md`:

1. The commit reviewed and the live address.
2. Screenshots at 390 and 1366 px, light and dark, of every page.
3. The automated results: axe-core, third-party requests (must be none, or only the owner's chosen service after an action), cookies (none), storage, horizontal overflow, page weight.
4. The hand checks: keyboard path, focus, zoom to 200 per cent, reading order, voice.
5. A verdict, **signed off**, **signed off with notes**, or **not signed off**, with the problems that block it, worst first.

The record is a signed commit by design.b. Changes to a site are made by that site's agent; design.b reviews, briefs and signs off.

## 12. Founder and personal sites

Standing guidance from Dinis Cruz, 20 November 2026, for every new founder or personal site ([source](https://github.com/SovereignWebsite/Site__Founder__Kate-Curtis-Evans/blob/dev/docs/guidelines-for-founder-sites.md)):

1. **Always show the designs.** Five designs of the same facts, and a "Choose a design" control on every page, so visitors and the owner can move between them. What wins owners over is seeing that a site can be made in all these designs; then the only question is which one they prefer. Build the control as plain links with `aria-current="page"` on the design shown, no script, hidden in print, and keep every design's old address answering (design.b, from Kate Curtis-Evans round 4).
2. **The agent may pick the home design;** the owner can change it.
3. **The milestone is the handover.** The first design phase ends when the site is strong enough for its owner to carry on with their own Claude (images, words, choosing a design), with the handover, the owner's prompt and the steps to connect their Claude to GitHub written as part of the work.
4. **Ask the owner, not the operator:** open questions (dates for figures, photo credits, which images may be used) go on a questions page for the owner.
5. **Owners need not sign commits;** agents do.
6. **Sell the founder's story:** the specialist who becomes a founder, building the tool their field was missing, with one of the five designs as a newsroom feature about it.
7. **Only what the owner has said:** no invented fact, figure, client or quote; every figure dated; every photo credited.

For rating (rating.md), a founder or personal site reaches level 3 only with the design chooser on every page, and level 4 only with the questions page and the owner's handover written.

### The handover is the objective (Dinis Cruz, 20 November 2026)

In his words, in design.b's session: "part of the objective for us is to do the handover ... a lot of the design stuff that we have is designed to do handover, is designed for them to add the materials, because we would always, never going to have the best materials, they're always going to have more". So:

- **Design for the owner to add to.** The owner will always have better and more material than we do. Every design must take more photos, words and links without breaking: galleries that grow, sections that can be added, slots ready for material we do not have yet.
- **It still has to look amazing** at handover; the aim is for us to do the least ourselves after it, not to hand over less.
- **One more pass as part of the service:** once the owner has added photos or material, the site's agent and design.b do one more design round.
- **Smooth and automated:** the handover, pushing to dev and the deploy should be as automatic as possible.
- **Public material only:** "for these websites, we only work with public materials", so everything we touch is already published and owned by someone else. Credit it; never use what is not public.

### Wow, not bland (Dinis Cruz, 20 November 2026)

On a founder site that was correct but plain: "it feels like websites created 10 years ago ... it needs to really have that wow factor, because when I show her the Silvio website, she said, wow. If I show her that now, she would have said, oh, this is interesting." So, for every founder and personal site:

- **A visual chooser,** as on silvio-switha.agenticcells.site: "Choose a design" opens five cards, each with a real screenshot of that design, its name and its one-line idea, the current one outlined; a plain link bar stays as the no-script fallback.
- **Every design must make a visitor say "wow":** a full-bleed hero image or scene, huge display type with a second voice, depth (layered images, offset colour, light and shadow), vivid colour, at least two designs dark first. Plain paper and a heading is the Brief only.
- **Generated stock imagery is allowed** where no cleared photo exists: agents may create images with OpenRouter image models, within a budget the accountant agent sets and tracks. Art-direct them per design; never show the owner, a client or any real person; never let an image stand for a fact; caption each "Generated image".
- **Review it as the finished website** (Dinis Cruz, 20 November 2026): "view this as a final website ... those things at the top, this is design X ... we need to make it super professional". No scaffolding on a live page: no "Design 3 of 5" explainer bars, rows of numbered pills or notes that read like a demo. The chooser is one styled control in the site's own header that opens the visual panel. If a page would not make its owner say "wow", it is not done, whatever the checks say.

### Concept first, written down (Dinis Cruz, 20 November 2026)

Five variations of one website do not count ("just about looks like five, the same website with a couple of five different variations"). Before building, each site writes `docs/designs.md`, one section per design: its **philosophy** (a way of thinking about the owner), its **visual narrative** (what a visitor sees first, second, third, and why), its **pipeline** (how the facts become the page: material, layout system, interaction), its colour and type, and what makes it unlike the other four. Each design is built from its own section.

**Use the technology:** JavaScript, charts, visualisations, maps, 3D and frameworks are welcome when they serve the idea, served from the site itself (vendored, no CDN, nothing loaded from another host), working at a basic level without JavaScript, respecting reduced motion, and within the first-load budget. **At least two designs are way out there:** their own colour schemes and layouts, the whole screen, timelines, brands placed in different positions. One design is the plain, printable Brief.

### Push, do not wait for sign-off (Dinis Cruz, 20 November 2026)

"I don't need to sign off the design. You push the sign off. You push it, and I see it on the website." Site agents and design.b push design rounds to dev and live without waiting for Dinis; he reviews them on the live site. Every site with five designs shows them all at once in its visual chooser (the panel of five screenshot cards), so they can be seen side by side.

### The admin dashboard (Dinis Cruz, 20 November 2026)

Every customer site's `/admin/` (guidelines 1.13) becomes "a proper admin dashboard... lots of graphs and powerful visualisations". It is the same generic page on every site: Kate Curtis-Evans's site is the pilot, and factory.b turns it into a seed page. Dinis gave this at about 16:50 UTC, relayed by the other design.b session.

**What it shows**, each as a panel with a heading:
1. **Version:** the commit live now, when it was built, and a link to it.
2. **CI checks:** the latest runs and their results.
3. **Activity by author:** commits over time, by author: the owner, the site's agent, design.b, and others.
4. **Content and weight:** pages, images, words, and first-load weight per page against the budget (section 9).
5. **Quality history:** accessibility results, contrast failures and overflow per commit, where they are recorded.
6. **Design rounds and synthetic users:** each round's rating and each run's look score, from design.b's `data/rounds/<site>.json` on design.agents.sovereignweb.site. Fetch it at build time, or link to it.
7. **Agents:** which agents have worked on the site, with their roles and their published keys.
8. **Ask Claude:** example prompts for the owner (change a word, add photos, choose a design) and for a visitor (ask about the owner's work), as on `/agents/`.
9. **Visitors:** a placeholder that says plainly that no visitor data is collected today (section 1.1: no tracking). It is filled only if the owner later chooses a privacy-respecting count.

**How it is built:**
- **Build-time data only.** Every figure comes from files written at build: git log, CI results and design.b's JSON. Nothing is fetched from another host when a visitor opens the page.
- **No email addresses, and no private data.** Show authors by name or role, never by email.
- **The chart library is vendored:** served from the site itself, with a version pinned, and loaded with `defer` (section 9). No CDN.
- **Every chart has a data table behind it**, reachable as a `<details>` "Show the data" or a linked table. Colour is never the only signal. Charts follow the site's light and dark tokens.
- **It works on a phone:** charts reflow into one column at 390 px, with no sideways scroll; wide tables scroll inside their own focusable box.
- **It is noindex:** `<meta name="robots" content="noindex">`. It is linked from the site (1.13), but kept out of search results.

design.b audits the dashboard like any other page, in all four views. It also checks that each chart's table matches its source data.

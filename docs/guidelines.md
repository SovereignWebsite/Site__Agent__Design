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

## 2. The family and the site

Every site is two layers:

- **The family layer** (the same everywhere): the family bar, the base tokens, the type scale, spacing, focus style, footer facts. It lives once, in the Factory seed (`seed/shared/`), and every site copies it unchanged.
- **The site layer** (its own): accent colour, headline face, hero, illustrations, voice details. A customer's site is mostly site layer; its owner's taste wins inside the rules.

The SovereignWebsite organisation's own sites (.ai, .org, .site, hub, vault, demos) should share one identity, taken from design 1: warm paper background, terracotta accent, serif headlines, system sans body. Proposal, for Dinis: either all own sites move to design 1's palette, or .ai keeps terracotta and the infrastructure sites take a named sibling palette from the same family. Today they are two unrelated looks (see review).

## 2a. Five designs, always

Every site has five designs (Dinis Cruz, 20 November 2026: "a key requirement is 5 designs"). They show what the team can do and let the owner choose. They live in `site/designs/1.html` to `5.html` with an index, one tap apart, as on sovereignwebsite.ai; the chosen one becomes `site/theme.css`. The five must differ in idea, not only in colour, and **each idea comes from the owner's own world**, as on the AgentiCCells personal sites (examples page): a filmmaker's Premiere, a composer's Cue Sheet and Record Sleeve, a pastry chef turned project manager's Pass, with her results as order tickets on a rail. Each design is named for its idea and **rebuilds the page around it**: the structure, the hero, the order of sections and the way facts are drawn change, not just colours and fonts. Five skins of one layout do not count as five designs. At least one should be designed dark first, and one should be the plain, printable version (a Brief) for people in a hurry.

Concept first, then craft: before any CSS, write for each design one sentence saying what it is a metaphor for, and which of the owner's own facts it will draw (a timeline, a cast list, a map, a set of tickets). Nothing drawn may be invented. Each of the five meets every rule in this document, light and dark, before it is shown. A site without five designs is rated no higher than 2 (rating.md, level 3 needs them).

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

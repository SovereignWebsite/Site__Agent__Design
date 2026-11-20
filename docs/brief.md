# Design brief: read this before you change any page

First draft, design.b@SovereignWebsite.dinis, 20 November 2026. For every agent that edits a Sovereign Website site, and for each new site's own design agent (seed notes). The full rules are in design/guidelines.md.

## Ten things to hold in your head

1. Nothing loads from another host. No fonts, scripts, images or embeds from anyone else, no cookies, no tracking. An owner-chosen service (like Google Maps) loads only when the visitor acts, after the page says what is sent.
2. Start at 390 px wide. The heading and first sentence must be on the first screen of a phone. Never scroll sideways.
3. Use the tokens (`--bg --surface --fg --muted --accent --accent-soft --line --note`), never raw colours. Write the dark values too and look at both.
4. Body text is `--fg`. `--muted` is for captions and sources only.
5. Text 4.5:1, controls and their borders 3:1, in both schemes. Measure; never lighten text with `opacity`.
6. System fonts only: sans for text, the Georgia serif stack for headlines (design 1).
7. Every page: skip link, family bar copied from the seed unchanged, header with the site's name linking home, one `h1` in `main`, footer that says what the site does not do.
8. Six or fewer links in the main nav; tap targets 24 px minimum, 44 px for buttons.
9. Say only what is true now. Label every proposal. No invented prices, customers or quotes. No em dashes.
10. Before you push, run axe-core and take the four screenshots (phone and desktop, light and dark). Send them with your change; design.b reviews and signs off.

## Seed notes for a new site's design agent

You own this site's look, inside the family rules. Your first job is five designs from the owner's own words and photos; the owner picks one. Keep the family layer (family bar, tokens, type scale, focus, footer facts) as the seed gives it, and put the owner's taste in the site layer: accent, headline face from the system stacks or a font file in the owner's own repository, hero, imagery. Record each design's choices in `designs/` and the chosen one in `site/theme.css`, as sovereignwebsite.ai does. Ask design.b for a review before the site is shown to its owner as done.

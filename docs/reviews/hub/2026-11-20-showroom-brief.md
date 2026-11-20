# Hub as the showreel: design brief and five directions

design.b@SovereignWebsite.dinis, 20 November 2026, about 13:00 UTC. From Dinis's words as relayed by sites.b: the hub (hub.sovereignwebsite.site, moving to hub.sovereignweb.site) becomes "the showreel (show room) for all the public sites", made to "look really good, professional and exciting (all with 5 different designs)". hub.b owns the repository and builds; design.b designs, reviews and signs off. Draft, held until Dinis confirms.

## Fixed for all five

- **Public sites only.** Never a private vault site, its holding page, its name or its screenshot.
- **Every claim from the hub's registry** (sites.json): name, address, group, owner, repository, vault, status, design sign-off. Status words are true today (the current hub says "Holding page" for sites that are not: fix in sites.json first).
- **Screenshots are files in the hub's own repository**, taken by the review audit at 390 and 1366 px, light and dark, and refreshed at each sign-off. No iframes of other sites, no live third-party previews, no external images, fonts or scripts.
- Each site card links to the live site, its repository and its design review.
- The family tokens and rules of design/guidelines.md: system fonts, both schemes, WCAG 2.2 AA, no sideways scroll at 320 px, under 100 KB per page before screenshots, images lazy-loaded with width and height set, `prefers-reduced-motion` respected.
- The five designs live side by side, as on sovereignwebsite.ai (`designs/1.html` to `5.html` and an index), and Dinis picks one.

## The five directions

1. **The gallery wall.** Warm paper of design 1, a generous grid of large framed screenshots, each with a small museum-style label (name, group, level, owner). Calm and premium; the sites do the talking.
2. **The showreel.** Dark, one site per screen with scroll snap: a phone and a desktop screenshot side by side, the site's own accent colour as the background glow, its name large. Exciting, closest to "showreel". Motion only as scroll snap, nothing animated on its own.
3. **The catalogue.** Typographic and dense: a sortable-looking index (filter by group with plain links, no script needed), each row a name, one line, group, maturity level, sign-off date, with a thumbnail. Professional, for people who want to compare.
4. **The show room.** One room per group (artist, cv, company, organisation, invest, and the SovereignWebsite family itself), each room a band with its own tint and two or three sites. Explains the groups as it shows the sites.
5. **Before and after.** For each site, what the owner had (or the seed page) next to what it is now, with its level from 0 to 5. Shows what the service does; only for sites where the "before" is the owner's to show.

## Next

hub.b to confirm sites.json carries the fields above (group, sign-off), and to send the list of public sites to include. design.b then makes the five as static pages in a local copy, audits them, and sends them to hub.b with screenshots for Dinis to pick.

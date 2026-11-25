# Hub, /directory/: design.b's review of the first pass

For hub.b, 25 November 2026. Looked at: hub.sovereignweb.site/directory/ at v0.1.73, its directory.json (91 sites, ten groups), desktop and phone ([desktop](runs/hub-2026-11-25-directory/desk.jpg), [phone first screen](runs/hub-2026-11-25-directory/phone.jpg)). Read with the brief, [the hub as a map](briefs/hub-map.html); the two crossed in the post.

## What is right
- Every site in one place, from data, with search first: this is what Dinis asked for.
- **Fixed groups**, each with a one-line "about". Update, same day: hub.b moved to the brief's six groups in v0.1.74 (74135e7), with the build failing on a site with no group, before this review arrived. Six stands; do not go back to ten.
- The agents are listed with their own sites.

## Worst first
1. **Over the phone limit:** 9,780 px against the 8,000 px rule. Fold each group's list behind its tile (a details element per group, opened from the map), so the page is the map plus one open group.
2. **People first, not agents.** Agents (31) is the first and biggest tile, so the hub reads as a list of our machinery. Put People first, then Tools, Startups and Businesses, and Agents last: the hub sells sites about people (hub-sells brief).
3. **The map is a row of counters, not a picture.** Draw the brief's map: the groups as regions, each site a point with its status mark, and a line to its keeper agent. The tiles can stay as the legend.
4. **No keeper on a site.** directory.json has host, name, group, state and repository, but not who keeps it. Add "keeper" from the registry's keeper chain, so each site's entry and the map's lines show its agent, which is the provenance view Dinis asked for.

## Next
The next hub.b session builds 1, 2 and 4 first (measured and data fixes), then the map (3) and the map in each of the five designs, as in the brief. design.b.rounds then asks: "Can you find a site about a musician, and who looks after it, in under thirty seconds?".

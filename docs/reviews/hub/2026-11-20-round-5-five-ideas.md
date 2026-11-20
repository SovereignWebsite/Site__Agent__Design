# Hub, round 5: five ideas, not five skins

design.b.rounds@SovereignWebsite.dinis, 20 November 2026, about 19:15 UTC. Dinis, looking at the hub's chooser on a phone at 18:52: "this looks like 5 variations of the same design". That is right, and it matches round 3, item 6. So this round does not wait for a lead design to be picked: here are five designs, each built on a different idea from the hub's own world.

See them: [design.agents.sovereignweb.site/designs/hub/](https://design.agents.sovereignweb.site/designs/hub/). The source is `designs/gen.py` beside this file, and it reads the hub's own `sites.json` (copied from the copy served at 18:49 UTC). Every word about a site comes from that file or the live hub page; nothing is added. The screenshots are the hub's own.

| # | Design | The idea | What the idea does for the hub |
|---|---|---|---|
| 1 | The Gallery | A dark gallery: each site hung in a frame under a spotlight, with a museum wall label. Kate's frame is gilt and hangs alone. | "The showroom" taken literally. The label carries the facts, including "Handed over: Kate edits it herself on GitHub". |
| 2 | The Register | A register of title: each site is an entry with its address, kind, who holds it and since when, status, files and designs. Kate's entry has a "Handed over" seal. | "Websites their owners own" shown as ownership records. Plain, printable, and the most honest about who holds what. |
| 3 | Contact Sheet | A photographer's contact sheet: numbered frames on a film strip. Kate's frame is circled in red grease pencil; Google Maps is crossed out ("Not switched on yet"). | Five designs, and the owner picks one: the chosen frame is circled. |
| 4 | The Street | Every site is a shopfront, with its address on the sign over the door and a "Walk in" door. The counts are painted on the road. Google Maps has a grey awning and a dashed "Not switched on yet" door. | The owner keeps the address: the address is the first thing you read. |
| 5 | The Line | The hub's own "How a site is made" as a production line, with each person's site placed at its station. Emily and Sarah are at "Five designs to choose from"; Kate is at "Handed over to the owner's GitHub". | Shows where each site stands, and what happens next. |

All five keep the same top bar: the brand, then top right a "Design N" chooser that names and describes all five, and a "Family" menu holding our links (guidelines 1.12). They have no scripts and use system fonts. Designs 1 and 3 are made dark-first; 2, 4 and 5 have light and dark.

## Checked

The five designs and the index were served locally and run through the same audit as the live sites (24 views: 390 and 1366 px, light and dark). axe-core 4.10.2 (WCAG 2.2 AA and best practice) finds no violations. None of them scrolls sideways at 390 px, none sends a request to another host, and none sets cookies or uses storage. Targets are 44 px or more. The heaviest first load on a phone is design 2 at about 480 KB, because it uses the desktop screenshots. hub.b should serve the 640 px or phone crops there.

## Recommendation

Lead with **4, The Street** or **2, The Register**. Both make the hub's one claim, that the owner keeps the address, the shape of the page. The Street is the warmer and more "wow"; the Register is the plainest. Dinis chooses. hub.b then builds the five into the hub (one `#design-N` each, from `sites.json`), and design.b.rounds runs the synthetic users on them.

# Brief: the hub as a map (navigation pass)

For hub.b, 25 November 2026. Dinis, in sites.a's session (relayed by a.maestro and maestro.b): the hub is hard to navigate, and "We need a nice visual. Again, ask the designer to take a pass at that." hub.b is making the hub list every site and agent from data. This brief covers the map by group, the Agents view, navigation, the five designs and the review rounds. Checked against SovereignWebsite__Hub dev ca3b102: site/sites.json (34 sites), site/data/agents.json, /agents/, /more/, /building/; registry.json is not live yet.

## Why it is hard to navigate today
- **Groups are free text.** sites.json uses 18 different group labels for 34 sites: "Demonstration" and "Demo" both appear, and nine labels hold one site each (Founder, Designer, Composer, and so on). A visitor cannot see the shape of the whole.
- **Agents are a separate list.** /agents/ names the team, but no page shows which agent keeps which site, so the provenance graph (guidelines 2b) has nowhere to start.
- **Three entry points that overlap:** the showroom, /more/ and /building/ split the same sites by status, not by what they are.

## 1. Fix the data first: six groups

**Final, 25 November 2026 01:40 UTC:** six groups, as live in hub v0.1.77 (9482abe): People, Tools, Startups, Businesses and demos, The family, Agents. This replaces the earlier messages about ten and nine, and the groups do not change again without a new brief.
One fixed list in the registry schema, so the map can never sprawl:

| Group | Holds |
|---|---|
| People | founders, artists, designers, musicians and other people's own sites |
| Startups | the startup brochures |
| Businesses and demos | made-up companies, demonstrations, providers |
| Tools | Car buyer, CRM, UK driving test, WordPress section and the like |
| The family | sovereignwebsite.ai, .org, .site, hub, vault, PrompTugal.news |
| Agents | each agent type's own site (design, decisions, maestro, factory) |

Each site keeps its own finer label ("Composer") as a tag under its group. Each site also carries its status (building, deliverable, handed over) as a mark on its entry, never as a separate page.

## 2. The map: one view of everything
One page, /map/, and the same map drawn small on every design's home page under the first screen:
- six groups as six regions, each site a point with its name, its status mark, and its keeper agent on hover or focus;
- a line from each site to its keeper agent, so a visitor sees who looks after what, and each agent's point opens its area (the provenance graph);
- built at build time from the registry as inline SVG with real links, no script needed, plus a list version of the same map for screen readers and small phones;
- on a phone, the six regions become six cards in a row you can swipe, each opening its list.

## 3. The Agents view
/agents/ becomes the map seen from the agents' side: each agent with the sites it keeps, its state and its area link, grouped by account (A, B and so on) and role (maestro, conductor, keeper, design, decisions). It is drawn from the registry's keeper chain (hub.b's HANDOVER item 0), not typed by hand.

## 4. Navigation
- The wayfinder (guidelines 2b) on every hub page: where you are, up, home, the group's next and previous site, the agent, connect, all sites.
- One menu with three entries only: **Map**, **Agents**, **Get one**. /more/ and /building/ fold into the map's filters (status: building, deliverable, handed over).
- From any site's entry: open the site, see its keeper, see its rounds (link to design.b's Sites page), see its five designs.

## 5. The map in each of the five designs
Each design draws the map in its own idea. It is the same data and links, but not the same picture restyled:
1. **The Line:** a line diagram. Each group is a coloured line, each site a station, and a site kept by the same agent as a site on another line is an interchange. Drawn in our own style, with no transport operator's map or branding.
2. **The Street:** a high street in six districts. Each site is a shop front with its sign, and each district has its own street name. The empty plot at the end stays "Yours".
3. **Contact Sheet:** a sheet of thumbnails, one row per group, with a red grease-pencil circle on the sites at deliverable or above.
4. **The Gallery:** six rooms, each wall a group, each site a framed picture with a label card naming the keeper.
5. **The Register:** the plain, printable list: group, site, status, keeper, one line each. It is also the screen-reader version of the map.

## Rounds
design.b.rounds runs one round per design as hub.b ships it, with the question "Can you find a site about a musician, and who looks after it, in under thirty seconds?", alongside "Would you want one?". The map is rated with the hub; a design whose map fails the question cannot keep a 4.

## Checklist (design and security together)
- [ ] Groups from the fixed list only; a site with no group fails the build
- [ ] The map and Agents view built from the registry at build time; no runtime fetch; CSP unchanged
- [ ] Inline SVG with real, focusable links and visible focus; a list version of the same content
- [ ] No private person shown unless they have consented (the first handed-over site stays unnamed, as the registry says)
- [ ] axe clean in all five designs, light and dark; each page under 8,000 px on a phone
- [ ] security.b: reviewed (nothing about agents beyond what their own areas publish)

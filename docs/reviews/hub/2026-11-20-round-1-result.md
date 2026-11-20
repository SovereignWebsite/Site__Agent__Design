# Hub showroom, round 1 result

design.b@SovereignWebsite.dinis, 20 November 2026, 13:17 UTC. Live at https://hub.sovereignweb.site/ (hub.sovereignwebsite.site redirects there), SovereignWebsite__Hub dev c85ef63. Audited: 5 designs at 390 and 1366 px, light and dark (20 views).

**Result:** every round 1 point is in. Contrast passes in all five designs; each design now has a light and a dark variant; the frames are capped (about 445 px on a phone) and link to the site; design 4 is now "By group"; the switch is a labelled nav and nothing is stored; sites.json has one domain per entry; the first images load eagerly. No sideways scroll, no requests to other hosts, no storage.

**Left:** one moderate axe finding in designs 1, 2, 3 and 5: heading-order. In the flattened designs the group headings (h2) are not rendered, so each site's h3 follows the h1. (One capture of design 3 at desktop failed to load; a fault of the capture, not the site.)

**Rating: 2 of 5.** Level 3 needs the heading order fixed and Dinis to choose one of the five designs.

## Round 2, sent to hub.b

1. Heading order: in the flattened designs keep the group h2 in the page but visually hidden (a visually-hidden class, not display none), or make each site's name an h2 there.
2. On a phone each frame is still most of a screen with the site's own family bar and nav inside it (the hosted sites' headers are tall). Consider 4:3 on phones, or capturing the phone shots below the family bar.
3. Retake the pipeline-demo screenshots: its round 1 design is live (ba8bc1c).
4. Waiting on Dinis: which of the five designs leads (my recommendation: 2 Night gallery), and whether the organisation's own sites belong in the showroom.

# a.design: learnings (25 November 2026)

- **Judge the glance before the sections.** I passed sovereignwebsite.ai's round 1 because each design had its own sections; Dinis saw "mainly 5 variations of the same design". The first check is now: the five first screens side by side at 390 and 1366 px; if two share a shape, they are one design.
- **Read every claim, not only the layout.** sites.a found an invented testimonial (labelled fictional) and an unconfirmed "agencies and freelancers" offer that I missed. No quote may be put in anyone's mouth, and no offer appears that the owner has not confirmed.
- **Check the served page, not only the source.** I flagged a missing stylesheet hash on One Human, Nine Agents that the build step adds; I withdrew it. Look at the built or live page before reporting.
- **On phones the directions collapse.** On almost every site, the five designs became one layout at 390 px. Ask for each direction's idea on its phone first screen.
- **The same top-of-page bug recurs**: the family credit overlapping the first notice line (London Agentics, GitHub tool). Crop the top 100 px at 390 px and look.
- **Test the keyboard by script.** A label for a `hidden` file input looked fine and passed axe, but could not be reached by keyboard.
- **The strict axe refresh breaks shared builds.** Each area's .md files are concatenated into its index page; two tables named "Table 1" failed landmark-unique. Keep only one table per area page (sources of other pages go in src/).
- **Keepers act within minutes.** Verify each fix round quickly and in writing, and say plainly when a site is ready for Dinis.

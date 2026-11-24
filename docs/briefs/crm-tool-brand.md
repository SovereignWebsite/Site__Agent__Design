# Brand brief: SovereignWeb.site CRM

For a.crm.design (account A), who builds it, with crm.dev.a. Asked by Dinis in crm.dev.a's session at about 13:30 UTC, 24 November 2026: "cool logos and branding for this SovereignWeb.site CRM" (relayed by maestro.b). It goes with the five page designs in the [CRM brief](crm-tool.html), and design.b.rounds judges it in the same rounds.

## What it must say in one look
Your contacts, in your own vault: kept by you, followed up on time. The brand should feel calm and trustworthy, like a well-kept address book, not loud like a sales tool.

## The name
"SovereignWeb.site CRM", written exactly so in the wordmark. The short form, on the favicon and phone header, is the mark alone.

## Deliverables
1. **The mark:** a symbol that works at 16 px (favicon), 32 px (header) and 512 px (share card). It is one-colour first, then coloured.
2. **The wordmark:** the name set in the system font stack (no third-party fonts; CSP 'self'), with the mark beside it, in horizontal and stacked forms.
3. **Colours:** one accent, one ink and one paper, each with a dark-mode pair, as --sws-* tokens so they work with the components' token contract. All text pairs at 4.5:1 or more, and the accent on paper at 3:1 or more for icons.
4. **The favicon:** an SVG plus a 32 px PNG fallback, readable on light and dark browser tabs.
5. **The share card:** 1200x630 JPEG under 150 KB with the mark, the name and one line (for example "Your contacts, in your own vault"). It replaces the seed card. If the live site is in demo mode, the card says nothing that suggests real customers.
6. **One page of usage:** clear space, minimum size, what not to do, all on the tool's own site at /brand/.

## Three directions for the mark
a.crm.design draws all three, small and large, and Dinis picks one with the page designs.
1. **The key card:** an index card whose corner is cut as a key's bit, for the vault and the contact in one shape.
2. **The follow-up:** a loop arrow closing on a dot, for the next step done on time. It fits The Day.
3. **The ring:** a keyring holding three tags, for several vaults per person (personal, RiskMandate, summit), with the QR hand-over in mind.

## Fit with the five page designs
The brand stays the same across all five designs. Only the page layout changes, as the family layer does on every site (guidelines 2). Each design takes the brand's tokens and does not invent its own accent.

## Checks before it ships
- [ ] The mark reads at 16 px in one colour; no gradients or fine lines lost at small sizes
- [ ] Contrast measured for every text pair, light and dark
- [ ] The share card passes the pipeline's share-card check (1200x630, every og: and twitter: tag)
- [ ] No third-party font, script or image; everything is served from the site
- [ ] The name is never shortened to something that suggests an official product of another company
- [ ] security.b: nothing in the files beyond the drawing (no embedded scripts in SVG)

## Cost
Recorded with the CRM tool's rounds in ratings.json.

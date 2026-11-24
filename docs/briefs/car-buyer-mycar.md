# Site brief: Car buyer, My car and five more creative designs

For b.site.car-buyer@SWS, keeper of car-buyer.tool.sovereignweb.site (Site__Tool__Car-Buyer). Asked for by Dinis on 24 November 2026: "much more creative designs", and a My car section for someone who has just bought a car. Checked against the repository at c4bde3f (dev): site/mycar/ (plate, next steps, question box, vault panel), site/not-yet/, site/designs/, and design rounds 1 to 12 on this site.

## Who it is for
Someone who has just bought a used car in the UK and wants it legal on the road this week, without reading five official sites. They come back once or twice more: when the logbook arrives, and before the first MOT.

## The one action
Put in the plate, then do the next step on the list. On every design, the first screen of My car shows the plate and the single next step with its official link.

## My car: what the section needs, in every design
1. **The plate as a plate.** Draw the registration as a UK number plate: yellow rear or white front, black characters, a heavy condensed system font (no third-party fonts). It is the hero of the page. Make it a display only, never an official-looking document.
2. **One next step first.** Before the full list, show "Next: [step]" with its official link and a Done button. The list follows, with done steps folded away and the count left.
3. **The question box, labelled honestly.** Keep the current wording: it finds the matching step, it is not an AI model, and Speak may send sound to the browser maker. Put the honesty line directly under the box, not in a paragraph below.
4. **The vault, simple first.** The first screen says only "Keep this in a private vault: [Set one up]". Making a key, sealed codes, QR pictures and the access token go behind that button, in the order a person meets them. Today the panel shows all of them at once, which is the hardest part of the page. "No vault open" becomes a state of the panel, not a line of text.
5. **Draft notice and sources stay**, as now. The open list (/not-yet/) is linked from My car as "What we cannot do yet".

## Five more creative designs
Each rebuilds every page, My car included, around its idea, and each idea comes from the world of owning a car. One stays plain (guidelines 2a). Dinis chose the Road atlas map (d10298e), so it goes furthest.

1. **Road atlas (taken furthest).** Buying is the route to the junction; My car is the road after it, with junctions for tax, insurance, the logbook slip and the MOT date, each a sign you pass when done. The vault is the glovebox in the map key. The question box is "Ask the way". It is the one to show a friend.
2. **Service book (the Logbook, made bolder).** The owner's service book: each step is a stamp box, empty until done, then stamped with the date in a rubber-stamp style drawn in CSS or SVG. The plate goes on the inside cover. The vault is the plastic wallet at the back of the book.
3. **Dashboard (new, replacing the MOT certificate).** The instrument cluster: each legal step not done is a warning light (tax, insurance, MOT), lit in the dashboard's amber, and it goes out when done. Each light also carries its word and an icon, never colour alone. The question box is the voice button on the steering wheel, and the plate sits on the dash. The MOT results become a gauge per test item.
4. **Tax disc (the Windscreen card, made bolder).** The windscreen view: every step is a round paper disc in a holder, as the old tax disc was, with the date on its rim. The plate runs across the bottom. Say in one line that paper tax discs ended in 2014 and this is only a picture.
5. **Forecourt (plain).** Kept as the calm, printable, one-column reference and the default, as the reviews asked. My car is a plain checklist with the plate above it.

## Checklist (design and security together)
- [ ] Every design shows the plate and the single next step on My car's first phone screen
- [ ] Warning lights, stamps and discs carry words and icons, never colour alone; axe clean in all five, light and dark
- [ ] The plate drawing cannot be mistaken for an official document; nothing suggests DVLA or DVSA made the site
- [ ] Vault: nothing contacts dev.send.sgraph.ai until the person presses a button; the token is used once and never stored; keys never leave the browser
- [ ] No step, date or rule invented: each names its official source and the date it was read
- [ ] Under 8,000 px on a phone per page; the wayfinder (guidelines 2b); the keeper's area current
- [ ] security.b: reviewed (the vault panel and the vendored libraries)

## Cost
Recorded under car-buyer.tool in ratings.json with each round.

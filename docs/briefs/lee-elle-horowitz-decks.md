# Lee-Elle Horowitz: the two guided-tour decks

For b.site.lee-elle-horowitz@SWS, 25 November 2026, at Dinis's word in its session: "can you ask the designer agent to help here (since pic2 looks very vanilla)". Looked at: /tour/your-site/ (13 slides) and /tour/behind-the-scenes/ (8 slides) at v0.1.21 (c7a7205), at 1280 x 720, with Dinis's comments as the keeper recorded them ([learnings](https://github.com/SovereignWebsite/Site__Artist__Lee-Elle-Horowitz/blob/dev/site/factory/dinis-cruz/account-b/learnings.md)).

## Why it looks vanilla
Almost every slide is the same layout: a small label, a heading and two lines on the left, and one screenshot on the right, on the same cream card. Thirteen slides of one layout read as one slide thirteen times. A deck about five designs should look designed itself. There is also a defect: on the behind-the-scenes deck the slides render at about a third of the stage's width at 1280 px.

## Eight layouts, not one
Build each slide from one of these, and never use the same layout twice in a row.
1. **Cover.** Full-bleed: her photo through the alef (as on the Alef-bet first screen), her name huge, one line. Nothing else.
2. **Statement.** One sentence, very large (80 to 100 px), on the colour of the design it introduces. For a turn in the story ("Six ways to say who you are").
3. **Collage.** Three to five live screenshots of one design, overlapping: the phone first screen, the desktop page, one detail cropped tight (the letter wall, a chat bubble, the curtain). Device frames are drawn in CSS: a phone outline and a laptop outline. This is Dinis's "more meat".
4. **Why.** The design's reasoning in three parts, each tied to her: the idea, why it is right for Lee-Elle, and what of hers it draws. Big numbers or letters as markers; a collage beside it.
5. **Side by side.** All six phone first screens in a row, at the same size, each with its name. It shows at a glance that they differ.
6. **Mirror.** Split down the middle: English on the left, the same section in Hebrew on the right, mirrored. It is the Hebrew slide.
7. **Graph.** For the team: agents as a linked graph (who asked, who built, who reviewed), each node with its role and a link to its area. It replaces a grid of boxes.
8. **Close.** Dark, with a grid of what we can do, each item with a thumbnail from her own site as proof.

## Each design slide wears its own design
The deck itself should show the range: the slide for Alef-bet uses Alef-bet's colours and type, the Stage slide is dark with gold, the Notebook slide is ruled paper, and so on. The deck's own furniture (page number, arrows, the "Guided tour" label) stays the same throughout.

## The reasoning, design by design
Say why each choice connects to her, in her words where possible. A starting point, for the keeper to check against her text:
- **Alef-bet:** a language starts with its letters, and parents want to see where a child begins. It draws on the alphabet, her photo and the nine lesson types.
- **Conversation:** her method is conversation ("rather than simply memorising vocabulary"), so the page talks. It draws on her approach and the questions parents ask.
- **Three tenses:** past, present and future is how she teaches grammar, and her own story fits it (South Africa, Israel, the UK). It draws on her background and the student's goal.
- **The stage:** she trained at the Guildford School of Acting, and music and audition preparation belong on a stage. It draws on her BA and the music section.
- **Notebook:** the plain, printable page, for a parent who wants the facts. It draws on the lesson list and the format.
- **Ivrit:** the whole site in Hebrew, for Hebrew-speaking families. It draws on everything, translated, and marked unchecked until she checks it.

## The close: "what we can do"
Dinis: "these are sites to demo what we can do", and "you have Hebrew on every single of these sites, which is also crazy powerful". The close should state, as facts with proof from her site:
- six designs from one person's text, each its own idea;
- two languages, including a full right-to-left Hebrew version;
- Hebrew in every design;
- her files on her own GitHub, hers to keep;
- changes by talking to her AI;
- an admin page, these guided tours and their PDFs.

Claim only what is live. If any design does not carry Hebrew yet, say "Hebrew in every design" only once it is true.

## Behind the scenes
- **The team as a graph**, not boxes: request, sites.b, factory.b, the keeper, design.b, design.b.rounds, security.b, each linked.
- **The pipeline as a line diagram:** push, checks, version, live, with her real version number.
- **The checks as a scoreboard:** axe results, the phone length and her design rounds' ratings, as numbers.
- **The maturity ladder**, M0 to M8, with her site's marker on its current level and the next step named. It is the clearest single picture of "where this is going".

## Type, colour and print
- Slide type: display 64 to 100 px in the site's serif, body at least 24 px, and no more than 30 words of body text on a slide. Hebrew uses the Hebrew system stack.
- Colour from the site's own tokens. Each design slide takes that design's tokens.
- For the PDF: no drop shadows (they print as grey bands); use a 1 px border and a solid offset block instead. Use a 16:9 page with no margins, one slide per page, and keep each slide's background in print (print-color-adjust: exact).
- Screenshots come from the same script as the chooser (tools/designs/thumbs.mjs), refreshed whenever a design changes.

## Checks
- [ ] No layout used twice in a row; every design slide has a collage
- [ ] Every claim on the close is live today
- [ ] The behind-the-scenes slides fill the stage at 1280 x 720
- [ ] The PDF prints without grey bands, one slide per page, with the file name for sharing (learnings 11)
- [ ] axe clean on both decks, light and dark; the arrows and the keys work

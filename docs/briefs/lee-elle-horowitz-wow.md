# Lee-Elle Horowitz: the wow pass

For b.site.lee-elle-horowitz@SWS, 25 November 2026, at Dinis's word in its session: "one more go at making them more WOW factor". Looked at: the live /designs/ (all five, at 390 and 1366 px) and the [first brief](lee-elle-horowitz.html), whose rules all still hold: her words only, single Hebrew letters only until she checks, system fonts, nothing from other hosts, axe clean in light and dark, under 8,000 px on a phone.

## First, what holds all five back: they open the same way
On a phone, every design opens with the same four things in the same order: the draft box, the heading "Private Hebrew Tuition with Lee-Elle Horowitz", four pills (children, London, Zoom, DBS) and the button. The idea of each design only starts below that, and in four of the five her photo is not on the first screen at all. A parent scrolling past sees one page five times. Three changes, in every design:
1. **The draft notice becomes one slim line** across the top ("Draft: not yet approved by Lee-Elle"), not a boxed paragraph.
2. **The four pills move below the first screen**, as one line of facts.
3. **Her photo is on the first phone screen** in every design, used the way that design uses it (below).

Motion: CSS only, a few hundred milliseconds, never looping, and none at all under prefers-reduced-motion.

## The two or three boldest changes per design

### 1. Alef-bet (the lead)
- **The photo through the letter.** A huge alef fills the first screen, with her photo seen through the letter's shape (background-clip: text, with her photo as the background, served from the site). Her name and the one line of service sit beside it. This is the image a parent remembers.
- **A wall of 22 letters.** The alphabet as a full-width grid of large letters, set right to left. Each letter shows its English name on hover or focus (Alef, Bet, Gimel and so on), which is fact, not her words. Each section of the page then opens on its own letter from that wall.
- **The letters arrive.** On first view, the wall fills in letter by letter, in a quick right-to-left wave.

### 2. Conversation
- **No hero: start talking.** The first screen is the chat itself. The visitor's bubble ("Hello! Who will be teaching me?") is there, then a typing indicator, then her reply with her photo as the avatar. The bubbles appear as you scroll.
- **The facts as quick replies.** Children, London, Zoom and DBS become reply chips under her message, as in a messaging app. Tapping one shows her answer from her own text.
- **The action is the reply box.** "Ask about lessons" sits at the bottom of the screen as the message field, and stays there.

### 3. Three tenses
- **Three screens, swiped.** Past, present and future are three full-height panels, swiped sideways on a phone (scroll snap) and side by side on a desktop, each in its own colour.
- **One photo, three treatments.** Past is her photo in sepia, with Israel and Guildford; present is in full colour, with lessons today; future is an empty frame marked "you", with the goal and the button.
- **"was, is, will be" as the headline.** The three words, at a size that fills the width, are the hero. Drop the long heading above them.

### 4. The stage
- **A spotlight.** A dark stage fills the first screen, with a pool of light (a radial gradient) on her photo, and her name in gold above it like a poster.
- **The curtain.** Two velvet curtains (CSS) draw back on load, once. Under reduced motion they are simply open.
- **The bill and a ticket.** "Act one: Hebrew", "Act two: music and audition preparation" set as a playbill, and the button as a perforated ticket stub, "Ask about lessons".

### 5. Notebook
- **The cover is the first screen.** The navy exercise book cover, full-screen, with the label filled in (Name: Lee-Elle Horowitz, Subject: Hebrew, Also: Music). Opening it, by a tap or by scrolling, shows the first ruled page.
- **Her photo taped in.** A small photo on the ruled page, slightly turned, with two strips of tape. The lesson types are ticked in red pen in the margin.
- **Fix the alphabet direction.** The alphabet line currently runs left to right (round 2). Set it with dir="rtl", so alef sits on the right.

### 6. Ivrit (the whole page in Hebrew)
Added at Dinis's word in the keeper's session ("can you actually make one of the designs to be in full hebrew?"). For this design that overrides the letters-only rule; the rule still holds for the other five.
- **Mirror the layout, not just the text.** With `dir="rtl"` on the html element and logical CSS throughout, everything should flip: her photo, the navigation and the button sit on the start side, which is the right. Check that no left or right value is left in its stylesheet.
- **Hebrew as the display type.** The heading in large Hebrew letters is the hero, in the Hebrew system stack at a weight and size no other design uses, with her photo beside it. This design should look like it was made in Tel Aviv, not translated from London.
- **The "not yet checked" notice stays at the top** in Hebrew and English, until she has read and corrected the translation. It is not the home design, and it is not shown to her as finished. Her correction moves it on (docs/hebrew-to-check.md).

The switcher now reads "Six designs": keep five as the set rated for M3 and M4, and treat Ivrit as a sixth, judged the same way.

## Then
Build the shared three first (one tag), then one design per tag, Alef-bet first. design.b.rounds judges each tag with "Would you book a Hebrew lesson for your child here?" and the look score; the aim is a 4 on Alef-bet, which takes the site to M4.

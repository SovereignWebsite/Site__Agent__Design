# sovereignwebsite.ai: a.design's design direction for the restyle

For website.a, keeper of sovereignwebsite.ai, 25 November 2026, 13:40 UTC, from Dinis Cruz's request as website.a relayed it: the main site should look as professional as the creative brief he supplied (ivory, ink navy, cobalt, a large serif headline, a fictional architecture studio, "North Studio", as the worked example, five designs for one brief, a clean comparison table). This is a direction to build from in plain HTML and CSS, not a finished design; website.a builds it, and it is not published until sites.a and I have seen it. Looked at first: the live home (axe clean on all four widths and schemes) and SovereignWebsite__Website dev **faf0d10**. [The home on a phone today, light and dark](img/sovereignwebsite-ai-2026-11-25-now-phone.jpg); [on a desktop](img/sovereignwebsite-ai-2026-11-25-now-desk.jpg).

## Why it reads as unprofessional today
1. **On a phone, about 200 px of navigation comes before the headline**: the family bar on two lines, then eleven site links on four lines, then the language switch. A professional studio site shows its promise first.
2. **"This home page is design 1 of five"** sits under the buttons on the live home. design.b's guidelines rule out scaffolding on a live page.
3. **The offer is a dashed coupon** (a dashed terracotta border with a shadow). It reads as a voucher, not a studio's price.
4. **Terracotta and cream** are warm but domestic; the brief asks for ivory, ink and cobalt, which read as calm and expert.

## Tokens
Every colour pair below is measured (WCAG ratio in brackets); all pass AA for body text, most AAA. System fonts only, so nothing is loaded from elsewhere.

```css
:root {
  /* colour, light */
  --bg: #FAF7F0;        /* ivory */
  --surface: #FFFFFF;
  --ink: #14213D;       /* ink navy: on --bg 14.9:1 */
  --muted: #4A5568;     /* on --bg 7.0:1 */
  --accent: #1D4ED8;    /* cobalt: on --bg 6.3:1; white on it 6.7:1 */
  --accent-soft: #E8EEFC;
  --line: #E4DED2;      /* hairlines only, never text */
  --band: #14213D;      /* the dark bands (Hub, footer): ivory on it 14.9:1 */
  --band-accent: #8AB0FF; /* cobalt on the dark band: 7.4:1 */
}
@media (prefers-color-scheme: dark) { :root {
  --bg: #0E1526; --surface: #16203A;
  --ink: #F3EFE6;       /* on --bg 15.9:1, on --surface 14.1:1 */
  --muted: #B8C0D0;     /* on --bg 10.0:1 */
  --accent: #8AB0FF;    /* on --bg 8.4:1; --bg on it 8.4:1 for buttons */
  --accent-soft: #1B2A4E; --line: #26324F; --band: #16203A; --band-accent: #8AB0FF;
}}
/* type */
--serif: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
--sans: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
h1: var(--serif) 600, clamp(2.4rem, 8vw, 4.75rem), line-height 1.04, letter-spacing -0.02em
h2: var(--serif) 600, clamp(1.6rem, 4.5vw, 2.5rem), line-height 1.15
h3: var(--sans) 600, 1.15rem
body: var(--sans) 400, 1.0625rem, line-height 1.6; small 0.875rem
kicker: var(--sans) 600, 0.78rem, uppercase, letter-spacing 0.12em, colour --accent
/* space: a 4 px step */
--s1 4px; --s2 8px; --s3 12px; --s4 16px; --s5 24px; --s6 32px; --s7 48px; --s8 64px; --s9 96px
section padding: --s8 on a phone, --s9 on a desktop; side gutter 16 px on a phone, 24 px above 48rem
--max: 72rem (page); --text: 40rem (reading measure)
/* shape */
radius 8px for cards and inputs; buttons 8px (not pills); hairline 1px var(--line); no shadows except a 0 1px 2px on cards
buttons: solid cobalt with white text, 48 px high on a phone; the second button is an ink outline
```

## 1. The main site: home, pricing, how it works
**Header, every page.** Logo and "Sovereign Website" on the left; on a desktop five links: How it works, Examples, Prices, Hub, and a cobalt button "Request a website". On a phone: the logo, then one "Menu" button (a `details` element, no script) and the "Request" button, on one line, 56 px high. The family links stay (this is our own organisation site) but in one line at the very top on a desktop, and inside the menu on a phone. The language switch goes into the footer and the menu.

**Home, in order.**
1. **Hero**: kicker "Sovereign Website"; the serif headline (keep the words: "Your website. Built by agents, owned by you."); one sentence; buttons "Request a website" and "See five designs for one brief". On a desktop the right half shows the **North Studio** strip: five small phone screenshots of one fictional brief in five designs, captioned "North Studio is a fictional architecture studio, made to show the five designs." On a phone the strip follows the buttons and scrolls sideways.
2. **Prices band**: two plain cards side by side (stacked on a phone), **£50** and **£500**, each with its name, what it includes as three short lines, and "Promotional price, set by Dinis Cruz on (date)". Take the inclusions from pricing.html as it stands; write nothing new about them. No dashed borders.
3. **Four promises**, as a row of four short items with a thin cobalt rule above each (one column on a phone).
4. **How it works**: three numbered steps, the number in the serif at 3rem.
5. **Examples** (section 5 below), **the Hub block** (section 4), **the comparison teaser**: the first four rows of the table with "See the full comparison".
6. **Footer**: the dark band, ivory text, columns of links, the language switch, the version line.

**Pricing page**: the two cards at the top, then "What you own" and "What it costs later" as two short lists, then the comparison table in full. **How it works**: the three steps expanded, each with one screenshot from a real round (the London Agentics picker is the best example).

## 2. The sector page template (one per kind of person)
Built to be the link in an email to someone who is not technical, so its first screen answers three questions: what is this, what does it cost, what do I do.
1. **Hero**: kicker "For artists" (or "For professionals", and so on); headline "A website of your own, for your work"; one sentence; the price line ("£50 or £500, promotional"); one button "Yes, I would like one", linking to the request page with the kind filled in (request.html?for=artist).
2. **A sample**: one large phone screenshot of a fictional site for that kind of person, labelled "A fictional example" in the caption, never a real person without their consent.
3. **Three things you get**, each one line, the same three on every sector page so they stay honest.
4. **How it works**, the three steps in one line each.
5. **The button again**, and "Questions? Write to (address)".
The page stays under 2,500 px on a phone, so the whole pitch fits a short scroll from an email.

## 3. The comparison table
Columns: **Sovereign Website**, and then **kinds** of provider rather than brand names: "Website builder subscription", "Freelance designer", "Agency". Rows: who owns the files; can you move it elsewhere; monthly fee; how many designs you see; who keeps it updated; what happens if you stop paying. Every cell for the other columns needs a source or a plain "usually", and no cell may state a named company's terms unless sourced with the date read. On a phone: the first column sticky, a "Swipe for more" line, or each row as a small card with the four answers stacked. Ticks and crosses always with a word ("Yes", "No"), never colour alone.

## 4. The Hub block
A full-width dark band (--band), ivory text: kicker "The Hub"; one headline sentence; one sentence on what the Hub is, taken from hub.sovereignweb.site's own words; a cobalt-on-navy button "Open the Hub" (--band-accent). On a desktop, a small drawing on the right: dots for sites gathered in groups, drawn in SVG with width, height and plain fills set, so it holds without CSS. It appears on the home and at the end of every sector page.

## 5. The examples section
A grid of five cards (two per row on a phone, three or five on a desktop), each a real phone screenshot of a live, public site we keep, with its kind as the label, not the person's name: "An author's book site", "A sports coach", "A funding tool", "A community chapter", "A company proposal". Use only sites whose owners have agreed to be shown; ask sites.a which. Each card links to the live site. Screenshots made by script at build time, sized with width and height (the picker standard, section 4a).

## 6. The request-a-website page
A single column, 40rem wide, in three short steps with numbered headings:
1. **About you**: name, email.
2. **Your site**: what kind (a row of choice cards: Artist, Professional profile, Small business, Organisation, Something else), what it is for (a text box), do you have a domain (yes, no, not sure).
3. **The price**: two choice cards, £50 or £500, with the same three lines as the home.
Then one cobalt button and a line on what happens next. Labels above fields, 48 px fields, errors in words beside the field. **Do not ship a form that looks as if it sends when it does not.** Until Dinis decides, either make the button open an email with the answers filled in (a mailto link, which sends nothing by itself) or use the sealed request lane that sites.agents.sovereignweb.site/request/ already runs. That choice is Dinis's.

## Five directions to build, and the rounds
sites.a asked, at 13:20 UTC, for five directions with rounds and the picker at the top. The tokens and the six layouts above are the content and the floor every direction keeps (the same words, prices, sections, the North Studio example labelled fictional, the one action "Request a website" on every first screen). The five then differ in **structure**, not only colour:
1. **Studio** (the brief itself): ivory, ink and cobalt, the serif headline, the North Studio strip beside it, everything above in this page. The calm, expert one.
2. **The Brief**: the site as one printable document: numbered sections, a contents list in the margin on a desktop, no cards, the comparison table as the centrepiece. The plain one design.b's guidelines ask for.
3. **Five Designs**: the site's own method as its structure: the hero is the five North Studio designs side by side at full width, you tap one and the page below re-colours into it. Dark first. The "wow" one.
4. **Ownership**: a timeline of what you hold, from request to hand-over to moving it elsewhere, each step with its proof (the files, the history, the address). For the sceptical reader.
5. **The Hub**: the home as a map of real sites by group (from the examples and hub.sovereignweb.site), with "Yours could sit here" as the action. For the reader who wants to see others first.
Rounds as on every other site: website.a builds round 1 on /designs/ with the picker at the top of every page (the Choose a design standard), I review each round against the standard and the brief, sites.a sees it too, and Dinis picks on the live site.

## Check first
- Prices: my first screenshot (about 13:25 UTC) still showed "£0 to £500"; by 13:45 the live home showed "£50 or £500", as on dev faf0d10. Nothing to do, but keep the screenshots in this page in mind as taken before that deploy.
- Remove "This home page is design 1 of five" from the live home now; it does not need the restyle.
- "North Studio" is labelled fictional wherever it appears, including image alt text.
- The five designs: the site chose design 1 on 20 November. Build the five directions above as a new round on /designs/, following the Choose a design standard, so Dinis picks on the live site rather than any replacing design 1 unseen.
- axe clean, light and dark, at 390 and 1366 px; the home under 8,000 px on a phone; no em dashes; tools/check.sh before every push.

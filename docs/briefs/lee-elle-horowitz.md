# Site brief: Lee-Elle Horowitz (lee-elle-horowitz.artist.sovereignweb.site)

For b.site.lee-elle-horowitz@SWS, its keeper, 25 November 2026. Source: b.maestro's [first customer sites brief](https://github.com/SovereignWebsite/Site__Agent__Maestro/blob/dev/site/factory/dinis-cruz/account-b/briefs/2026-11-25-first-customer-sites.md), Site 1, with her own text. Dinis: "you can name her". This is one of the first two customer sites, which validate the workflow, so it should reach M4 (the level of Emily's and Grace's sites) before it is shown to her.

## Who the site is for
Parents looking for a Hebrew tutor for a child growing up in the UK, and adults starting or rebuilding their Hebrew. Most arrive on a phone, from a recommendation, and decide in a minute whether she is the right teacher.

## The one action
**Ask about lessons.** It uses the /send/ lane (security.b cleared, a.factory d60ffb9) as an enquiry form once it is wired. Until then, the button says "Enquiries open soon" and is not a dead link. No phone number or email address appears unless she chooses to publish one.

## Words and sources
- Her supplied text only, lightly edited for the web. No invented qualifications, prices, testimonials or pupils.
- Hebrew is the main service, and music is a smaller second section (singing, trombone, beginner guitar, musical theatre and audition preparation), never equal billing.
- **Any Hebrew on the page beyond single letters is checked by her before it is published.** Until then, use only the alphabet, her name if she gives its Hebrew spelling, and words she supplies. A wrong Hebrew word on a Hebrew tutor's site costs her trust.
- Photos: only the Spotlight photos Dinis gives you, each with alt text and the credit Spotlight shows. No stock photos.
- A draft notice until she approves the site (M5).

## Five ideas from her world
Each rebuilds the page around its idea, Hebrew first and music second; five colour skins of one layout do not count.
1. **Alef-bet.** The page as an alphabet chart. Each section opens with a large Hebrew letter (alef for About, bet for Beginners, and so on), and the lesson types are letter tiles. It is the most visual, and the one for parents.
2. **Conversation.** The page as a dialogue, her approach made visible: each section is an exchange, with English on the left and its Hebrew on the right, set right-to-left. The Hebrew must be words she supplies or checks. Lesson types are "what you will be able to say".
3. **Three tenses.** Past, present and future, the way she teaches grammar. The past is her story (South Africa, Israel, Guildford); the present is lessons today, in person in London or online; the future is the student's goal, with the action button.
4. **The stage.** From her acting training: a theatre programme. The cover is her photo and name, the Hebrew lessons are the main bill, music and audition preparation are the second half, and her BA from the Guildford School of Acting is in the biography. It is the natural home for the music section.
5. **Notebook.** The plain, printable page: a ruled exercise book, one column, for a parent who wants the facts.

## Hebrew right to left, and fonts with no outside loading
- The page stays left-to-right English. Each Hebrew word or phrase is marked `lang="he" dir="rtl"`, inline inside `bdi` or as its own block. Never mirror the whole page.
- Use CSS logical properties (margin-inline-start, padding-inline-end, text-align: start), so a Hebrew block lays out correctly without special cases.
- System fonts only, with a Hebrew-capable stack: `"Noto Sans Hebrew", "Arial Hebrew", "Segoe UI", Arial, sans-serif` for sans, and `"Noto Serif Hebrew", "David", "Times New Roman", serif` for serif. Check the letters render on iOS Safari, Android Chrome and Windows Edge before a design is shown.
- Large display letters (Alef-bet) are text, not images, so screen readers read them, with an English label beside each.
- Avoid niqqud (vowel points) unless she asks for them; they render unevenly in system fonts.

## The /start/ page
Written for her, not for visitors: what the site is, how to choose her design (one tap per design), how to send changes, text and new photos (the /send/ lane), what she can change herself later, and who looks after the site (the keeper's area). It is plain and short, with no jargon about Git.

## Checklist (design and security together)
- [ ] Hebrew first, music second, in every design
- [ ] No Hebrew beyond letters and her own words until she has checked it
- [ ] No contact details until she chooses; the enquiry goes through /send/ only
- [ ] Spotlight photos only, credited, with alt text; nothing loaded from outside the site
- [ ] Hebrew marked with lang and dir, and logical CSS; axe clean in all five, light and dark; under 8,000 px on a phone
- [ ] The wayfinder (guidelines 2b), share card, /start/, /agents/, /admin/, llms.txt; the keeper's area current
- [ ] security.b: the /send/ form reviewed

## Cost
Recorded in ratings.json under the site, with each round.

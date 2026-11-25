# Learnings

- A five-design brief before the build works: Suno reached five real ideas in one round; Car Buyer, built first as colour skins, took five rounds.
- A checklist pass is not a good site (Kate, 20 Nov). Level 4 needs the wow check.
- Check the signed record before acting, and act on the latest one: ask 14 first read as approval, then the next record made it a review item, so RiskMandate went back from M5 to M4.
- Never hide git's push output: two commits once sat unpushed behind a rejected push.
- A site created outside design registration falls through the cracks (Donna Freed). Register at M1, at launch.
- Placeholders like `<account>` in Markdown become raw HTML tags and fail html-validate (it broke two deploys on 24 Nov). Write them in backticks or as [name], and run html-validate with the CI config before every push.
- A wow idea can break a phone: swiped panels hid Three tenses' content and failed axe (Lee-Elle round 3). Check a new interaction against axe and the phone before briefing it as the bold change.

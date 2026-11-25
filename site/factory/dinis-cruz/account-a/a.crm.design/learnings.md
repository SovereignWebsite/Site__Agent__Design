# a.crm.design: learnings

- Check the whole built site before pushing, not only your own pages: the deploy validates every page, including each agent's area page built from its markdown. Twice a bare word in angle brackets in now.md (and then in the note warning about it) failed the deploy for everyone.
- The org-wide axe can change under you (best-practice rules arrived on 25 Nov). Run tools/check.sh, which reads the current .github/ci/axe.mjs, every time.
- The deploy adds a version chip to every footer; a muted footer colour made it fail contrast. Style it where it lands.
- Test a patch on the live page itself (Playwright route that swaps style.css), not only on a copy: real data, real classes, real rules you must outrank.
- Specificity bites when you restyle someone else's markup: an existing #me + .mode rule beat mine; a state class beat the signature-check class. Check the computed result, not the rule.
- Never use display:flex on a summary you want to keep its disclosure triangle (a.crm.studio's catch).
- In a flex box a br is ignored: two lines sit side by side.
- On a phone the app's rule that every input is 44 px tall pushed radio buttons out of line; hold them at their size inside their tiles.
- A full-size screenshot shrunk into a hero cannot be read; crop it to the part that tells the story.
- Write times only from date -u; an estimated time is an invented fact.
- When a permission check refuses something (add_repo), say so to Dinis and carry on another way; do not work around it.
- Agents' session ids in a repository go stale; route through the maestro when a message does not arrive.

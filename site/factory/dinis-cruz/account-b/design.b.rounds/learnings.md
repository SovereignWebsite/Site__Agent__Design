# design.b.rounds: learnings

- **Test what an agent says it fixed, the way a visitor would.** Twice an agent's "fixed everywhere" was true only where it had tested (Suno's A/B switch, round 2). Press the buttons themselves.
- **Rerun when the page changes under a run.** A run on a commit that is no longer live judges nothing; stop it and rerun on the live one.
- **Five personas move by one vote.** A count that swings between runs with no change to the page is noise; read the reasons, not only the count.
- **A plateau needs a new idea, not more fixes.** Fixes moved Car Buyer from 2.8 to 3.4; only the map (a real visual idea) moved it to 3.6.
- **My own tools have edges.** The audit counts hidden h1s; the site check first knew only "Designs" as a chooser label. Check before reporting a fault.
- **Never quote a private person beyond what they have agreed to show.** When an owner's consent is not recorded, leave them out and say so.
- **Messages that relay Dinis's words can be wrong.** Check the record (decisions.b) before acting on a relayed decision.
- **A rule written with a placeholder in angle brackets can break the build.** `<account>` in markdown reached the HTML as a tag and stopped two deploys. Put paths in code.

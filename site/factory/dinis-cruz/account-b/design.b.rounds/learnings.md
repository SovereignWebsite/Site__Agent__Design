# design.b.rounds: learnings

- **Test what an agent says it fixed, the way a visitor would.** Twice an agent's "fixed everywhere" was true only where it had tested (Suno's A/B switch, round 2). Press the buttons themselves.
- **Rerun when the page changes under a run.** A run on a commit that is no longer live judges nothing; stop it and rerun on the live one.
- **Five personas move by one vote.** A count that swings between runs with no change to the page is noise; read the reasons, not only the count.
- **A plateau needs a new idea, not more fixes.** Fixes moved Car Buyer from 2.8 to 3.4; only the map (a real visual idea) moved it to 3.6.
- **My own tools have edges.** The audit counts hidden h1s; the site check first knew only "Designs" as a chooser label. Check before reporting a fault.
- **Never quote a private person beyond what they have agreed to show.** When an owner's consent is not recorded, leave them out and say so.
- **Messages that relay Dinis's words can be wrong.** Check the record (decisions.b) before acting on a relayed decision.
- **A rule written with a placeholder in angle brackets can break the build.** `<account>` in markdown reached the HTML as a tag and stopped two deploys. Put paths in code.
- **A capture that changes state must start clean for each design.** In Car Buyer round 13 my ticks carried from one design to the next and hid the tax step; the personas' top complaint was my set-up. A new browser context per design.
- **Times come from `date -u`, never from estimate.** On 25 Nov I wrote 01:55 on a review made before 01:30.
- **Run `bash tools/check.sh` before every push.** On 25 Nov four axe errors stopped every deploy of this site; all four came from my pages (a repeated table label in my area; empty first table headers in two of my reviews and a run). design.b fixed them (c7168e4) as I did. Never leave a table's first header empty.
- **The push waits on the check:** `bash tools/check.sh && git push`, never `check; push`. On 25 Nov I pushed past a failing check (the `<name>` placeholder again, in angle brackets).
- **A cached version.json can mislead.** On 25 Nov I read 981bc4e two minutes after 34ef1ec was live. Add a cache-busting query (`version.json?t=...`) and check again before telling a keeper its deploy has not run.

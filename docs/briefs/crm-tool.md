# Site brief: the CRM tool (crm.tool.sovereignweb.site/app/)

For crm.dev.a@AgentiCCells.dinis, via maestro.b and a.maestro, 24 November 2026. Dinis, in crm.dev.a's session at about 12:40 UTC: "we needed 5 designs for this. Very important." Looked at: v0.1.3 (20d5f07), desktop and phone. crm.dev.a builds the one Dinis picks; design.b.rounds judges them (tracked as R15).

## Who the site is for
A small team (today Dinis, Angela and the agents) following up the people they met, starting with the Web Summit contacts. They come back every day, so it must be fast to scan and quick to act in.

## The one action
"Log an action" (or send the waiting draft) on the company that needs it most today. Every design puts the next thing due on its first screen.

## What every design keeps
- The same pages: lead board, company (Activity and "Log an action"), follow-ups, contacts, import, open or start a vault, requests.
- **Demo mode** as a fixed, unmissable band on every page in every design ("Synthetic demo: everything here is made up"), never only a word in a corner.
- **The vault switcher** (personal, RiskMandate, summit CRM) in the same place in every design, always showing which vault is open, with the QR hand-over one step from it.
- "Overdue", "draft waiting" and "no reply for N days" shown by words and shape, never by colour alone.
- Static, CSP 'self' plus dev.send.sgraph.ai, system fonts only, phone and desktop, axe clean light and dark, plain British English.

## Five directions
Each rebuilds the pages around its idea; five colour skins of today's table do not count.

1. **The Board.** A pipeline wall: one column per stage (New, Talking, Proposal, Customer), each company a card showing who owns it, the next step and its date. Overdue cards carry a folded corner. On a phone the columns become swipeable tabs with a count on each. The company page is the card turned over. Best for seeing the whole pipeline at once.
2. **The Day.** A desk diary: the first screen is today, then this week, listing what is due, overdue and waiting for a reply, each line with its one action button. Companies are reached from the diary, not the other way round. Best for "what do I do this morning?", and the strongest on a phone.
3. **The Thread.** Built like an inbox: each company is a conversation, newest activity first, with the threads, notes and logged actions in one timeline. "Log an action" is the reply box at the bottom, and a waiting draft sits there ready to send. Best for people who live in email, and it fits the Email Cell.
4. **The Map.** Who knows whom: the first screen is a map of the companies grouped by where they came from (the summit, introductions, inbound), each person linked to their company and to whoever on the team met them. The lead board is a list beside the map. Best for the summit follow-up and for showing provenance.
5. **The Ledger.** The dense, keyboard-first table for heavy use: sortable columns, j and k to move, one key to log an action, filters as words in the URL so a view can be shared. It prints cleanly. The plain, fast version (guidelines 2a).

## Recommendation
Build **The Day** first: it answers the daily question and works on a phone. Build **The Board** second: it is the one people expect from a CRM, and it suits a demo to a client. Dinis chooses the home design after seeing all five.

## Checklist (design and security together)
- [ ] Demo band on every page in every design; synthetic data only at reserved example domains
- [ ] The vault switcher shows the open vault on every page; keys never leave the browser; QR hand-over unchanged
- [ ] CSP unchanged: 'self' plus dev.send.sgraph.ai; no third-party fonts or scripts
- [ ] Status by words and shape, never colour alone; 44 px targets; axe clean in all five, light and dark
- [ ] Phone: the one action within the first screen in every design
- [ ] The wayfinder (guidelines 2b) and the agent's area
- [ ] security.b: reviewed

## Cost
Recorded in ratings.json under crm.tool once its rounds start.

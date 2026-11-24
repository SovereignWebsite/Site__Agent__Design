/* Design 3 of 5, The Thread: built like an inbox. Each company is a conversation, newest activity first; its
   emails, notes and logged actions in one timeline; Log an action is the reply box, with a waiting draft ready in it.
   a.crm.design, 24 Nov 2026. */
(function () {
  'use strict';
  const { keyTag, D, esc, days, fmt, longDate, plural, company, person, stageName, sourceName, status, badges, byUrgency, dayList, say } = window.CRM;
  const lastAt = (c) => c.activity.reduce((m, a) => (a.at > m ? a.at : m), '0');
  const needsYou = (c) => c.stage !== 'parked' && (days(c.due) >= 0 || c.draft || c.repliedOn);
  const when = (at) => { const n = days(at); return n === 0 ? 'Today' : n === 1 ? 'Yesterday' : fmt(at); };

  function row(c, open) {
    const a = c.activity[0]; const st = status(c)[0];
    return `<li class="conv${needsYou(c) ? ' needs' : ''}${open ? ' open' : ''}"><a href="#/company/${c.id}"${open ? ' aria-current="true"' : ''}>
      <span class="from"><b>${esc(c.name)}</b><time datetime="${lastAt(c)}">${when(lastAt(c))}</time></span>
      <span class="subj">${c.draft ? `<span class="pre">Draft:</span> ${esc(c.draft.subject)}` : esc(c.next)}</span>
      <span class="snip">${a.dir === 'in' ? '<span class="pre">They wrote:</span> ' : ''}${esc(a.text)}</span>
      ${st ? `<span class="flag"><span class="st ${st.cls}">${esc(st.text)}</span></span>` : ''}</a></li>`;
  }
  function list(items, label, open) {
    return `<nav class="convs" aria-label="${esc(label)}"><ol>${items.map((c) => row(c, c.id === open)).join('') || '<li class="none">Nothing here.</li>'}</ol></nav>`;
  }
  const filters = (cur) => `<p class="filters" role="group" aria-label="Show">${[['inbox', 'All'], ['inbox/needs', 'Needs you'], ['inbox/waiting', 'Waiting on them'], ['inbox/mine', 'Mine']].map(([h, l]) => `<a href="#/${h}"${cur === h ? ' aria-current="true"' : ''}>${l}</a>`).join('')}</p>`;
  const byRecent = (l) => [...l].sort((a, b) => (lastAt(b) > lastAt(a) ? 1 : lastAt(b) < lastAt(a) ? -1 : 0));

  function inbox(which) {
    const all = byRecent(D.companies);
    const pick = { needs: all.filter(needsYou), waiting: all.filter((c) => c.noReplySince), mine: all.filter((c) => c.owner === 'you') }[which] || all;
    const n = all.filter(needsYou).length;
    return { title: 'Inbox', html: `<div class="split"><section class="pane-list" aria-labelledby="ib-h"><div class="list-head"><h1 id="ib-h" tabindex="-1">Inbox</h1><p class="note">${plural(n, 'conversation')} need you · newest activity first</p>${filters(which ? `inbox/${which}` : 'inbox')}</div>${list(pick, 'Conversations')}</section>
      <section class="pane-read empty-read" aria-label="Reading pane"><p>Choose a conversation.</p><p class="note">The most urgent: <a href="#/company/${byUrgency(all.filter(needsYou))[0].id}">${esc(byUrgency(all.filter(needsYou))[0].name)}</a>.</p></section></div>` };
  }

  // The thread: one timeline, oldest at the top as in a mail thread, the reply box at the bottom.
  function thread(id) {
    const c = company(id); if (!c) return inbox();
    const msgs = [...c.activity].reverse();
    const intro = c.introducedBy ? company(c.introducedBy) : null;
    const kinds = D.kinds.map((k) => `<option${k === 'Email' ? ' selected' : ''}>${k}</option>`).join('');
    return { title: c.name, html: `<div class="split reading"><section class="pane-list" aria-label="Conversations"><div class="list-head"><p class="h-like">Inbox</p>${filters('inbox')}</div>${list(byRecent(D.companies), 'Conversations', c.id)}</section>
      <section class="pane-read" aria-labelledby="t-h">
        <p class="back"><a href="#/inbox">‹ Inbox</a></p>
        <header class="t-head"><h1 id="t-h" tabindex="-1">${esc(c.name)}</h1>
          <p class="t-meta">${esc(stageName(c.stage))} · ${esc(person(c.owner))} · ${c.people.map((p) => `${esc(p.name)} ${keyTag(p, c)}`).join(' ')} · <span class="note">${esc(c.domain)}</span></p>
          <p class="t-meta">${badges(c)}</p>
          <p class="t-next"><span><b>Next:</b> ${esc(c.next)}, due <time datetime="${c.due}">${fmt(c.due, true)}</time></span> <a class="btn${c.draft ? ' warn' : ''} jump" href="#/company/${c.id}/${c.draft ? 'draft' : 'log'}">${c.draft ? 'Review and send' : 'Log an action'} ↓</a></p></header>
        <ol class="msgs">
          <li class="sys">${esc(sourceName(c.source))}${c.metBy ? `, met by ${esc(person(c.metBy))}` : ''}${intro ? `, introduced through <a href="#/company/${intro.id}">${esc(intro.name)}</a>` : ''}</li>
          ${msgs.map((a) => `<li class="msg ${a.dir === 'in' ? 'in' : 'out'}${a.kind !== 'Email' ? ' logged' : ''}${a.fresh ? ' fresh' : ''}"><p class="m-meta"><b>${a.dir === 'in' ? esc(c.people[0].name) : esc(person(a.by))}</b> · ${esc(a.kind)} · <time datetime="${a.at}">${fmt(a.at, true)}</time></p><p>${esc(a.text)}</p></li>`).join('')}
        </ol>
        <form class="reply form" id="log" data-thread="${c.id}" aria-labelledby="r-h">
          <h2 id="r-h">${c.draft ? '<span class="st st-draft">Draft waiting</span> Reply, ready to send' : 'Log an action'}</h2>
          <div class="row"><label>What kind<select name="kind">${kinds}</select></label><label>With<select name="who">${c.people.map((p) => `<option>${esc(p.name)}</option>`).join('')}</select></label></div>
          ${c.draft ? `<p class="note">To ${esc(c.draft.to)} · "${esc(c.draft.subject)}" · drafted by the CRM agent; read it before it goes.</p>` : ''}
          <label id="draft">${c.draft ? 'The message' : 'What happened'}<textarea name="text" rows="${c.draft ? 7 : 3}" required${c.draft ? '' : ' placeholder="Write what you did or said; it goes on the thread"'}>${c.draft ? esc(c.draft.body) : ''}</textarea></label>
          <details class="nextstep"><summary>Next step: ${esc(c.next)}, ${fmt(c.due, true)}</summary><div class="row"><label>Next step<input name="next" value="${esc(c.next)}"></label><label>Due<input type="date" name="due" value="${esc(c.due)}"></label></div></details>
          <p class="send-row">${c.draft ? '<button class="btn warn" type="submit" name="act" value="send">Send it (demo)</button> <button class="btn quiet" type="submit" name="act" value="log">Log as a note instead</button>' : '<button class="btn" type="submit" name="act" value="log">Add to the thread</button>'} <span class="note">Demo: kept in this tab.</span></p>
        </form>
      </section></div>` };
  }
  // The reply box handles both sending the draft and logging an action.
  document.addEventListener('submit', (ev) => {
    const f = ev.target; if (!f.dataset.thread) return; ev.preventDefault();
    const c = company(f.dataset.thread); const v = Object.fromEntries(new FormData(f)); const act = ev.submitter ? ev.submitter.value : 'log';
    if (act === 'send' && c.draft) {
      c.activity.unshift({ at: D.today, kind: 'Email', dir: 'out', by: 'you', text: `Sent "${c.draft.subject}"${v.text !== c.draft.body ? ' (edited)' : ''}.`, fresh: true });
      const subj = c.draft.subject; delete c.draft; c.next = `Hear back about "${subj}"`; c.due = '2026-11-27'; c.noReplySince = D.today;
      say(`Sent to ${c.name} (demo).`); window.CRM.refresh(`Sent to ${c.name}. In the demo nothing leaves this tab.`);
    } else {
      c.activity.unshift({ at: D.today, kind: act === 'log' && c.draft ? 'Note' : v.kind, dir: 'out', by: 'you', text: `${v.who}: ${v.text}`, fresh: true });
      if (v.next) c.next = v.next; if (v.due) c.due = v.due; delete c.repliedOn;
      say(`Added to the ${c.name} thread (demo).`); window.CRM.refresh(`Added to the ${c.name} thread. In the demo it stays in this tab.`);
    }
  }, true);

  function today() {
    const { now, week, waiting } = dayList();
    const sec = (id, h, l) => `<section aria-labelledby="${id}"><h2 id="${id}" class="grp">${h} <span class="n">${l.length}</span></h2>${list(l, h)}</section>`;
    return { title: 'Today', html: `<div class="single"><div class="list-head"><h1 tabindex="-1">Today</h1><p class="note">${longDate(D.today)}: the conversations that need you, most urgent first.</p></div>
      ${sec('td-now', 'Needs you today', now)}${sec('td-week', 'Later this week', week)}${sec('td-wait', 'Waiting on them', waiting)}</div>` };
  }
  function followUps() {
    const live = byUrgency(D.companies.filter((c) => c.stage !== 'parked'));
    return { title: 'Follow-ups', html: `<div class="single"><div class="list-head"><h1 tabindex="-1">Follow-ups</h1><p class="note">Every conversation with a next step, by when it is due: like snoozed mail coming back.</p></div>
      <ol class="fu">${live.map((c) => `<li><time datetime="${c.due}">${days(c.due) > 0 ? `<b>${plural(days(c.due), 'day')} late</b>` : fmt(c.due, true)}</time><a href="#/company/${c.id}"><b>${esc(c.name)}</b> ${esc(c.next)}</a>${badges(c)}</li>`).join('')}</ol></div>` };
  }
  function board() {
    return { title: 'Lead board', html: `<div class="single"><div class="list-head"><h1 tabindex="-1">Lead board</h1><p class="note">The conversations as folders, one per stage.</p></div>
      ${D.stages.map((s) => { const l = byRecent(D.companies.filter((c) => c.stage === s.id)); return `<details class="folder"${s.id !== 'parked' ? ' open' : ''}><summary><span>${esc(s.name)}</span> <span class="n">${l.length}</span></summary>${list(l, s.name)}</details>`; }).join('')}</div>` };
  }
  function contacts() {
    const all = D.companies.flatMap((c) => c.people.map((p) => ({ ...p, c }))).sort((a, b) => a.name.localeCompare(b.name));
    const groups = {}; all.forEach((p) => { (groups[p.name[0]] = groups[p.name[0]] || []).push(p); });
    return { title: 'Contacts', html: `<div class="single"><div class="list-head"><h1 tabindex="-1">Contacts</h1><p class="note">An address book: ${plural(all.length, 'person')}.</p></div>
      ${Object.keys(groups).sort().map((k) => `<h2 class="letter">${k}</h2><ul class="abook">${groups[k].map((p) => `<li><a href="#/company/${p.c.id}"><b>${esc(p.name)}</b> <span>${esc(p.role)}, ${esc(p.c.name)}</span></a><span class="mail">${keyTag(p, p.c)} ${esc(p.email)}</span></li>`).join('')}</ul>`).join('')}</div>` };
  }
  function more() {
    return { title: 'More', html: `<div class="single"><div class="list-head"><h1 tabindex="-1">More</h1></div><ul class="more"><li><a href="#/follow-ups">Follow-ups<span>every next step by date</span></a></li><li><a href="#/import">Import<span>contacts from a spreadsheet</span></a></li><li><a href="#/vault">Vaults<span>open, start, or hand one to your phone</span></a></li><li><a href="#/requests">Requests<span>ask the CRM's keeper</span></a></li><li><a href="#/you">You<span>your name and this browser's key</span></a></li></ul></div>` };
  }

  window.CRM.start({ design: 'The Thread', home: 'inbox', navOf: { company: 'inbox', 'follow-ups': 'more' }, pages: { inbox, company: thread, today, 'follow-ups': followUps, board, contacts, more } });
})();

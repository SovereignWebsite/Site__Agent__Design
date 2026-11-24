/* Design 1 of 5, The Day: a desk diary. The first screen is today; companies are reached from the diary.
   a.crm.design, 24 Nov 2026. */
(function () {
  'use strict';
  const { D, esc, days, fmt, longDate, plural, company, person, stageName, sourceName, badges, byUrgency, dayList, actionButton, logForm, draftBox } = window.CRM;

  // One diary line: when, who, what, its one action.
  function line(c, opts) {
    const o = opts || {}; const late = days(c.due);
    const when = late > 0 ? `<b>${plural(late, 'day')}</b> late` : late === 0 ? '<b>Today</b>' : `<b>${fmt(c.due, true)}</b>`;
    return `<li class="entry${late > 0 && c.stage !== 'parked' ? ' late' : ''}">
      <p class="when">${when}</p>
      <div class="what">
        <h3><a href="#/company/${c.id}">${esc(c.name)}</a></h3>
        <p class="next">${esc(c.next)}</p>
        <p class="meta">${badges(c)} <span class="who">${esc(person(c.owner))}</span></p>
      </div>
      <div class="act">${o.noAction ? '' : actionButton(c)}</div>
    </li>`;
  }
  const summary = (list) => {
    const n = (k) => list.filter((c) => window.CRM.status(c).some((s) => s.k === k)).length;
    const parts = [[n('overdue'), 'overdue'], [n('today'), 'due today'], [n('draft'), n('draft') === 1 ? 'draft waiting' : 'drafts waiting'], [n('replied'), n('replied') === 1 ? 'reply to answer' : 'replies to answer']].filter(([k]) => k);
    return parts.map(([k, w]) => `<b>${k}</b> ${w}`).join(', ');
  };
  const mineOnly = (list, who) => (who === 'mine' ? list.filter((c) => c.owner === 'you') : list);
  const scope = (who, base) => `<p class="scope" role="group" aria-label="Whose">
      <a href="#/${base}" ${who !== 'mine' ? 'aria-current="true"' : ''}>Everyone</a><a href="#/${base}/mine" ${who === 'mine' ? 'aria-current="true"' : ''}>Mine</a></p>`;

  function today(who) {
    const { now, week, waiting } = dayList();
    const n = mineOnly(now, who), w = mineOnly(week, who), wait = mineOnly(waiting, who);
    return { title: 'Today', html: `<div class="page-head"><p class="eyebrow">Today</p><h1 tabindex="-1">${longDate(D.today)}</h1>
      <p class="tally">${summary(n) || 'Nothing due. A quiet day.'}</p>${scope(who, 'today')}</div>
      <section class="diary" aria-labelledby="h-now"><h2 id="h-now">Do today <span class="count">${n.length}</span></h2>
        <ol class="entries">${n.map((c) => line(c)).join('') || '<li class="empty">Nothing for today.</li>'}</ol></section>
      <div class="later">
        <section class="diary" aria-labelledby="h-week"><h2 id="h-week">The rest of the week</h2>
          ${w.length ? `<ol class="entries small">${w.map((c) => line(c)).join('')}</ol>` : '<p class="empty">Nothing else this week.</p>'}</section>
        <section class="diary waiting" aria-labelledby="h-wait"><h2 id="h-wait">Waiting on them</h2>
          <ul class="entries small">${wait.map((c) => `<li class="entry"><div class="what"><h3><a href="#/company/${c.id}">${esc(c.name)}</a></h3><p class="meta">${badges(c)}</p></div><div class="act"><a class="btn quiet" href="#/company/${c.id}/log">Nudge</a></div></li>`).join('') || '<li class="empty">No one.</li>'}</ul></section>
      </div>` };
  }

  function followUps(who) {
    const live = byUrgency(mineOnly(D.companies.filter((c) => c.stage !== 'parked'), who));
    const groups = [['Overdue', (c) => days(c.due) > 0], ['Today', (c) => days(c.due) === 0], ['Tomorrow', (c) => days(c.due) === -1], ['This week', (c) => days(c.due) < -1 && days(c.due) >= -7], ['Later', (c) => days(c.due) < -7]];
    return { title: 'Follow-ups', html: `<div class="page-head"><p class="eyebrow">The agenda</p><h1 tabindex="-1">Follow-ups</h1><p class="tally">Every open next step, by date. ${plural(live.length, 'company')}.</p>${scope(who, 'follow-ups')}</div>
      ${groups.map(([g, f]) => { const l = live.filter(f); return l.length ? `<section class="diary" aria-labelledby="g-${g.replace(/\s/g, '')}"><h2 id="g-${g.replace(/\s/g, '')}">${g} <span class="count">${l.length}</span></h2><ol class="entries">${l.map((c) => line(c)).join('')}</ol></section>` : ''; }).join('')}` };
  }

  function board() {
    return { title: 'Lead board', html: `<div class="page-head"><p class="eyebrow">Every company</p><h1 tabindex="-1">Lead board</h1>
      <p class="stage-tally">${D.stages.map((s) => `<a href="#/board/x/st-${s.id}">${esc(s.name)} <b>${D.companies.filter((c) => c.stage === s.id).length}</b></a>`).join('')}</p></div>
      ${D.stages.map((s) => { const l = byUrgency(D.companies.filter((c) => c.stage === s.id)); return `<section class="diary" id="st-${s.id}" aria-labelledby="bh-${s.id}"><h2 id="bh-${s.id}">${esc(s.name)} <span class="count">${l.length}</span></h2><ol class="entries small">${l.map((c) => line(c)).join('')}</ol></section>`; }).join('')}` };
  }

  function companyPage(id, sub) {
    const c = company(id); if (!c) return today();
    const by = {}; c.activity.forEach((a) => { (by[a.at] = by[a.at] || []).push(a); });
    const intro = c.introducedBy ? company(c.introducedBy) : null;
    return { title: c.name, html: `<p class="crumb"><a href="#/today">Today</a> / ${esc(c.name)}</p>
      <div class="page-head company"><p class="eyebrow">${esc(stageName(c.stage))} · ${esc(person(c.owner))}</p><h1 tabindex="-1">${esc(c.name)}</h1>
        <p class="meta">${badges(c)}</p></div>
      <div class="co-grid">
        <section class="next-box" aria-labelledby="h-next"><h2 id="h-next">Next: ${esc(c.next)}</h2><p class="due">Due <time datetime="${c.due}">${fmt(c.due, true)}</time></p>
          ${c.draft ? `<div id="draft">${draftBox(c)}</div>` : ''}
          <div id="log"><h3>Log an action</h3>${logForm(c)}</div></section>
        <section class="diary activity" aria-labelledby="h-act"><h2 id="h-act">Activity</h2>
          ${Object.keys(by).sort().reverse().map((d) => `<h3 class="day-h"><time datetime="${d}">${fmt(d, true)}</time></h3><ul class="log">${by[d].map((a) => `<li class="${a.fresh ? 'fresh' : ''}"><span class="kind">${esc(a.kind)}${a.dir === 'in' ? ', they wrote' : ''}</span> ${esc(a.text)} <span class="who">${esc(person(a.by))}</span></li>`).join('')}</ul>`).join('')}</section>
        <section class="side" aria-labelledby="h-ppl"><h2 id="h-ppl">People</h2>
          <ul class="people">${c.people.map((p) => `<li><b>${esc(p.name)}</b><br>${esc(p.role)}<br><a href="mailto:${esc(p.email)}">${esc(p.email)}</a></li>`).join('')}</ul>
          <h2>Where from</h2><p>${esc(sourceName(c.source))}${c.metBy ? `, met by ${esc(person(c.metBy))}` : ''}${intro ? `, introduced through <a href="#/company/${intro.id}">${esc(intro.name)}</a>` : ''}.</p>
          <p class="note">${esc(c.domain)}</p></section>
      </div>` };
  }

  function contacts() {
    const all = D.companies.flatMap((c) => c.people.map((p) => ({ ...p, c }))).sort((a, b) => a.name.localeCompare(b.name));
    return { title: 'Contacts', html: `<div class="page-head"><p class="eyebrow">Everyone you follow up</p><h1 tabindex="-1">Contacts</h1><p class="tally">${plural(all.length, 'person')} at ${plural(D.companies.length, 'company')}.</p></div>
      <ul class="cards">${all.map((p) => { const last = p.c.activity[0]; return `<li><h2><a href="#/company/${p.c.id}">${esc(p.name)}</a></h2><p>${esc(p.role)}, ${esc(p.c.name)}</p><p class="note">Last contact <time datetime="${last.at}">${fmt(last.at, true)}</time> · <a href="mailto:${esc(p.email)}">${esc(p.email)}</a></p></li>`; }).join('')}</ul>` };
  }

  function more() {
    return { title: 'More', html: `<div class="page-head"><h1 tabindex="-1">More</h1></div>
      <ul class="more-list"><li><a href="#/import">Import contacts <span>from a spreadsheet</span></a></li><li><a href="#/vault">Open or start a vault <span>and hand one to your phone</span></a></li><li><a href="#/requests">Requests <span>ask the CRM's keeper</span></a></li><li><a href="#/you">You <span>your name and this browser's key</span></a></li></ul>` };
  }

  window.CRM.start({ design: 'The Day', home: 'today', navOf: { company: 'today' }, pages: { today, 'follow-ups': followUps, board: (a, s) => board(a, s), company: companyPage, contacts, more } });
})();

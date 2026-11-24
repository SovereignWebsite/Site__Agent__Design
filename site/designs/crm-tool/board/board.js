/* Design 2 of 5, The Board: a pipeline wall. One column per stage, each company a card; overdue cards carry a
   folded corner; the company page is the card turned over. On a phone the columns become tabs with counts.
   a.crm.design, 24 Nov 2026. */
(function () {
  'use strict';
  const { keyTag, D, $, $$, esc, days, fmt, longDate, plural, company, person, stageName, sourceName, status, badges, byUrgency, dayList, actionButton, logForm, draftBox, say } = window.CRM;
  const LIVE = ['new', 'contacted', 'talking', 'proposal', 'won'];
  const initials = (id) => (id === 'you' ? 'You' : person(id).replace(/\s*\(demo\)/, '').split(/\s+/).map((w) => w[0]).join('').slice(0, 2));

  function card(c, opts) {
    const o = opts || {}; const late = c.stage !== 'parked' && days(c.due) > 0;
    const next = LIVE[LIVE.indexOf(c.stage) + 1];
    return `<li class="card${late ? ' late' : ''}${c.draft ? ' drafted' : ''}">
      <div class="card-top"><span class="owner" title="${esc(person(c.owner))}"><span class="vh">Owner: </span>${esc(initials(c.owner))}</span>
        <h3><a href="#/company/${c.id}">${esc(c.name)}</a></h3></div>
      <p class="next">${esc(c.next)}</p>
      <p class="due">${late ? `<b>Was due ${fmt(c.due, true)}</b>` : `Due ${fmt(c.due, true)}`}</p>
      <p class="tags">${badges(c)}</p>
      ${o.noAction ? '' : `<div class="card-act">${actionButton(c)}${next && !o.noMove ? `<button type="button" class="btn quiet move" data-move="${c.id}" aria-label="Move ${esc(c.name)} to ${esc(stageName(next))}">To ${esc(stageName(next))} ›</button>` : ''}</div>`}
    </li>`;
  }

  function columns(cols, label) {
    return `<div class="tabs" role="tablist" aria-label="${esc(label)}">${cols.map((col, i) => `<button type="button" role="tab" id="tab-${col.id}" aria-controls="col-${col.id}" aria-selected="${i === 0}" tabindex="${i === 0 ? 0 : -1}">${esc(col.name)} <span class="n">${col.items.length}</span></button>`).join('')}</div>
      <div class="wall">${cols.map((col, i) => `<section class="col${i === 0 ? ' shown' : ''}" id="col-${col.id}" role="tabpanel" aria-labelledby="tab-${col.id} h-${col.id}">
        <h2 id="h-${col.id}">${esc(col.name)} <span class="n">${col.items.length}</span>${col.note ? ` <span class="col-note">${esc(col.note)}</span>` : ''}</h2>
        <ol class="cards">${col.items.map((c) => card(c, col.opts)).join('') || '<li class="none">Nothing here.</li>'}</ol></section>`).join('')}</div>`;
  }

  function board() {
    const cols = LIVE.map((s) => ({ id: s, name: stageName(s), items: byUrgency(D.companies.filter((c) => c.stage === s)) }));
    const late = D.companies.filter((c) => c.stage !== 'parked' && days(c.due) > 0).length;
    const parked = D.companies.filter((c) => c.stage === 'parked');
    return { title: 'Lead board', html: `<div class="head"><h1 tabindex="-1">Lead board</h1>
      <p class="sum">${plural(D.companies.length - parked.length, 'company')} in play · <span class="st st-overdue">${late} overdue</span> with a folded corner · overdue first in each column</p></div>
      ${columns(cols, 'Stages')}
      <details class="parked"><summary>Parked <span class="n">${parked.length}</span></summary><ol class="cards">${parked.map((c) => card(c, { noMove: true })).join('')}</ol></details>` };
  }

  function today() {
    const { now, week, waiting } = dayList();
    const cols = [{ id: 'now', name: 'Do today', items: now }, { id: 'week', name: 'This week', items: week }, { id: 'wait', name: 'Waiting on them', items: waiting, opts: { noMove: true } }];
    return { title: 'Today', html: `<div class="head"><h1 tabindex="-1">Today</h1><p class="sum">${longDate(D.today)}. The cards that need you, most urgent at the top.</p></div>${columns(cols, 'Today')}` };
  }

  function followUps() {
    const live = byUrgency(D.companies.filter((c) => c.stage !== 'parked'));
    const cols = [['late', 'Overdue', (c) => days(c.due) > 0], ['today', 'Today', (c) => days(c.due) === 0], ['week', 'This week', (c) => days(c.due) < 0 && days(c.due) >= -7], ['later', 'Later', (c) => days(c.due) < -7]]
      .map(([id, name, f]) => ({ id, name, items: live.filter(f), opts: { noMove: true } }));
    return { title: 'Follow-ups', html: `<div class="head"><h1 tabindex="-1">Follow-ups</h1><p class="sum">The same cards, laid out by when the next step is due.</p></div>${columns(cols, 'When')}` };
  }

  // The card turned over: the front (as on the board) beside the back (everything else).
  function companyPage(id) {
    const c = company(id); if (!c) return board();
    const intro = c.introducedBy ? company(c.introducedBy) : null;
    return { title: c.name, html: `<p class="crumb"><a href="#/board">Lead board</a> › ${esc(stageName(c.stage))} › ${esc(c.name)}</p>
      <div class="turned">
        <section class="face front" aria-labelledby="f-h"><p class="face-label">The card</p>
          <div class="card big${c.stage !== 'parked' && days(c.due) > 0 ? ' late' : ''}"><div class="card-top"><span class="owner">${esc(initials(c.owner))}</span><h1 id="f-h" tabindex="-1">${esc(c.name)}</h1></div>
            <p class="stage-line">${esc(stageName(c.stage))} · owned by ${esc(person(c.owner))}</p>
            <p class="next"><b>Next:</b> ${esc(c.next)}</p><p class="due">Due ${fmt(c.due, true)}</p><p class="tags">${badges(c)}</p>
            <dl class="mini"><dt>Where from</dt><dd>${esc(sourceName(c.source))}${intro ? `, through <a href="#/company/${intro.id}">${esc(intro.name)}</a>` : ''}</dd><dt>Met by</dt><dd>${esc(person(c.metBy))}</dd><dt>Domain</dt><dd>${esc(c.domain)}</dd></dl>
            <h2 class="sm">People</h2><ul class="ppl">${c.people.map((p) => `<li><b>${esc(p.name)}</b>, ${esc(p.role)} ${keyTag(p, c)}<br><a href="mailto:${esc(p.email)}">${esc(p.email)}</a></li>`).join('')}</ul>
          </div></section>
        <section class="face back" aria-labelledby="b-h"><p class="face-label">Turned over</p><h2 id="b-h" class="vh">The back of the card</h2>
          ${c.draft ? `<div id="draft">${draftBox(c)}</div>` : ''}
          <div id="log" class="log-box"><h2>Log an action</h2>${logForm(c, { rows: 2 })}</div>
          <h2>Activity</h2><ol class="acts">${c.activity.map((a) => `<li class="${a.fresh ? 'fresh' : ''}${a.dir === 'in' ? ' in' : ''}"><p class="a-meta"><time datetime="${a.at}">${fmt(a.at, true)}</time> · ${esc(a.kind)}${a.dir === 'in' ? ' · <b>they wrote</b>' : ''} · ${esc(person(a.by))}</p><p>${esc(a.text)}</p></li>`).join('')}</ol>
        </section></div>` };
  }

  function contacts() {
    const all = D.companies.flatMap((c) => c.people.map((p) => ({ ...p, c }))).sort((a, b) => a.name.localeCompare(b.name));
    return { title: 'Contacts', html: `<div class="head"><h1 tabindex="-1">Contacts</h1><p class="sum">${plural(all.length, 'person')}, as a stack of business cards.</p></div>
      <ul class="bizcards">${all.map((p) => `<li><h2><a href="#/company/${p.c.id}">${esc(p.name)}</a></h2><p>${esc(p.role)} ${keyTag(p, p.c)}</p><p class="co">${esc(p.c.name)} <span class="stage">${esc(stageName(p.c.stage))}</span></p><p><a href="mailto:${esc(p.email)}">${esc(p.email)}</a></p></li>`).join('')}</ul>` };
  }

  function more() {
    return { title: 'More', html: `<div class="head"><h1 tabindex="-1">More</h1></div><ul class="tiles"><li><a href="#/import"><b>Import</b><span>contacts from a spreadsheet</span></a></li><li><a href="#/vault"><b>Vaults</b><span>open, start, or hand one to your phone</span></a></li><li><a href="#/requests"><b>Requests</b><span>ask the CRM's keeper</span></a></li><li><a href="#/you"><b>You</b><span>your name and this browser's key</span></a></li></ul>` };
  }

  // Tabs on a phone (one column at a time); every column shows on a wide screen.
  function wire() {
    const tabs = $$('[role=tab]'); if (!tabs.length) return;
    const pick = (t, focus) => { tabs.forEach((x) => { const on = x === t; x.setAttribute('aria-selected', String(on)); x.tabIndex = on ? 0 : -1; document.getElementById(x.getAttribute('aria-controls')).classList.toggle('shown', on); }); if (focus) t.focus(); };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => pick(t));
      t.addEventListener('keydown', (e) => { const k = { ArrowRight: 1, ArrowLeft: -1 }[e.key]; if (k) { e.preventDefault(); pick(tabs[(i + k + tabs.length) % tabs.length], true); } });
    });
  }
  document.addEventListener('click', (e) => {
    const b = e.target.closest('[data-move]'); if (!b) return;
    const c = company(b.dataset.move); const to = LIVE[LIVE.indexOf(c.stage) + 1]; if (!to) return;
    c.stage = to; c.activity.unshift({ at: D.today, kind: 'Note', dir: 'out', by: 'you', text: `Moved to ${stageName(to)}.`, fresh: true });
    say(`${c.name} moved to ${stageName(to)}. Demo: nothing written.`); window.CRM.refresh(`${c.name} moved to ${stageName(to)}. In the demo it stays in this tab.`);
  });

  window.CRM.start({ design: 'The Board', home: 'board', navOf: { company: 'board' }, after: wire, pages: { board, today, 'follow-ups': followUps, company: companyPage, contacts, more } });
})();

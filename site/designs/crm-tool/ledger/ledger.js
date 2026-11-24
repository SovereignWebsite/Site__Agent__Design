/* Design 5 of 5, The Ledger: the dense, keyboard-first table. Sortable columns; j and k to move, Enter to open,
   l to log an action, d for a waiting draft, / to filter; filters and sort as words in the address, so a view can be
   shared; prints cleanly. a.crm.design, 24 Nov 2026. */
(function () {
  'use strict';
  const { D, $, $$, esc, days, fmt, longDate, plural, company, person, stageName, sourceName, status, badges, actionButton, logForm, draftBox, say } = window.CRM;
  const short = (id) => person(id).replace(/\s*\(demo\)/, '');
  const last = (c) => c.activity.reduce((m, a) => (a.at > m ? a.at : m), '0');
  const COLS = [
    ['name', 'Company', (c) => c.name.toLowerCase()], ['stage', 'Stage', (c) => D.stages.findIndex((s) => s.id === c.stage)],
    ['owner', 'Owner', (c) => short(c.owner)], ['next', 'Next step', (c) => c.next.toLowerCase()], ['due', 'Due', (c) => c.due],
    ['state', 'State', (c) => -(status(c).length ? 10 - ['overdue', 'today', 'draft', 'replied', 'noreply'].indexOf(status(c)[0].k) : 0)], ['last', 'Last contact', (c) => last(c)], ['source', 'From', (c) => c.source]
  ];
  // The view lives in the address: #/ledger/owner:you+stage:proposal+state:overdue+sort:-due
  function parse(q) {
    const v = { owner: '', stage: '', state: '', from: '', sort: 'due', text: '' };
    (q || '').split('+').filter(Boolean).forEach((w) => { const [k, x] = decodeURIComponent(w).split(':'); if (x !== undefined && k in v) v[k] = x; else v.text += (v.text ? ' ' : '') + decodeURIComponent(w); });
    return v;
  }
  const words = (v) => ['owner', 'stage', 'state', 'from'].filter((k) => v[k]).map((k) => `${k}:${v[k]}`).concat(v.sort !== 'due' ? [`sort:${v.sort}`] : []).concat(v.text ? v.text.split(' ') : []).join(' ');
  const toHash = (base, s) => `#/${base}/${s.trim().split(/\s+/).filter(Boolean).map((w) => encodeURIComponent(w).replace(/%3A/gi, ':')).join('+')}`;
  function rows(v) {
    let l = D.companies.filter((c) => (!v.owner || c.owner === v.owner) && (!v.stage || c.stage === v.stage) && (!v.from || c.source === v.from) && (!v.state || status(c).some((s) => s.k === v.state)) && (!v.text || (c.name + ' ' + c.next + ' ' + c.people.map((p) => p.name).join(' ')).toLowerCase().includes(v.text.toLowerCase())));
    const desc = v.sort.startsWith('-'); const col = COLS.find((x) => x[0] === v.sort.replace('-', '')) || COLS[4];
    l.sort((a, b) => { const x = col[2](a), y = col[2](b); return (x < y ? -1 : x > y ? 1 : 0) * (desc ? -1 : 1); });
    return l;
  }

  function table(base, q, title, lead) {
    const v = parse(q); const l = rows(v); const sortKey = v.sort.replace('-', ''); const desc = v.sort.startsWith('-');
    const sortLink = (k) => { const nv = { ...v, sort: sortKey === k && !desc ? `-${k}` : k }; return toHash(base, words(nv) || ' '); };
    const quick = [['', 'All'], ['state:overdue', 'Overdue'], ['state:today', 'Due today'], ['state:draft', 'Drafts'], ['state:replied', 'Replied'], ['owner:you', 'Mine']];
    return `<div class="l-head"><h1 tabindex="-1">${esc(title)}</h1><p class="note">${lead} ${plural(l.length, 'row')}.</p>
      <form class="filter" data-filter="${base}" role="search"><label for="f-q">Filter</label><input id="f-q" name="q" value="${esc(words(v))}" spellcheck="false" autocomplete="off" placeholder="owner:you stage:proposal state:overdue, or any word"><button class="btn" type="submit">Apply</button></form>
      <p class="quick">${quick.map(([w, t]) => `<a href="${toHash(base, w || ' ')}"${words(v) === w ? ' aria-current="true"' : ''}>${t}</a>`).join('')}<span class="keys" aria-hidden="true"><kbd>j</kbd><kbd>k</kbd> move · <kbd>Enter</kbd> open · <kbd>l</kbd> log · <kbd>d</kbd> draft · <kbd>/</kbd> filter</span></p></div>
      <div class="tbl-wrap"><table class="ledger"><caption class="vh">${esc(title)}, ${l.length} rows. Keys: j and k move between rows, Enter opens, l logs an action, d opens a waiting draft.</caption>
      <thead><tr>${COLS.map(([k, t]) => `<th scope="col"${sortKey === k ? ` aria-sort="${desc ? 'descending' : 'ascending'}"` : ''}><a href="${sortLink(k)}">${t}<span class="arrow" aria-hidden="true">${sortKey === k ? (desc ? ' ▼' : ' ▲') : ''}</span></a></th>`).join('')}<th scope="col"><span class="act-h">Action</span></th></tr></thead>
      <tbody>${l.map((c) => { const late = c.stage !== 'parked' && days(c.due) > 0; return `<tr data-id="${c.id}" tabindex="-1" class="${late ? 'late' : ''}">
        <th scope="row" data-label="Company"><a href="#/company/${c.id}">${esc(c.name)}</a></th><td data-label="Stage">${esc(stageName(c.stage))}</td><td data-label="Owner">${esc(short(c.owner))}</td>
        <td data-label="Next step">${esc(c.next)}</td><td data-label="Due" class="num">${late ? '<span aria-hidden="true">▲ </span>' : ''}<time datetime="${c.due}">${c.due}</time></td>
        <td data-label="State">${badges(c) || '<span class="note">none</span>'}</td><td data-label="Last contact" class="num"><time datetime="${last(c)}">${last(c)}</time></td><td data-label="From">${esc(sourceName(c.source).replace('Met at the summit', 'Summit').replace('Came to us', 'Inbound'))}</td><td class="act">${actionButton(c, 'mini')}</td></tr>`; }).join('') || `<tr><td colspan="${COLS.length + 1}">No rows match. <a href="#/${base}">Clear the filter</a>.</td></tr>`}</tbody></table></div>`;
  }
  const ledger = (q) => ({ title: 'Ledger', html: table('ledger', q, 'Ledger', 'Every company in one table. Sort by any column; the address keeps the view.') });
  const today = (q) => ({ title: 'Today', html: table('today', q === undefined ? 'state:today' : q, `Today, ${longDate(D.today)}`, 'Start with the overdue and due-today rows; change the filter for the rest.') });
  const followUps = (q) => ({ title: 'Follow-ups', html: table('follow-ups', q === undefined ? 'sort:due' : q, 'Follow-ups', 'Every next step, soonest first.') });

  function record(id, sub) {
    const c = company(id); if (!c) return ledger();
    const intro = c.introducedBy ? company(c.introducedBy) : null;
    const ids = rows(parse('')).map((x) => x.id); const i = ids.indexOf(id);
    return { title: c.name, html: `<div class="rec"><p class="crumb"><a href="#/ledger">Ledger</a> › ${esc(c.name)} <span class="pn">${i > 0 ? `<a href="#/company/${ids[i - 1]}" rel="prev">‹ Previous</a>` : ''}${i < ids.length - 1 ? `<a href="#/company/${ids[i + 1]}" rel="next">Next ›</a>` : ''}</span></p>
      <h1 tabindex="-1">${esc(c.name)}</h1><p class="meta">${badges(c)}</p>
      <div class="rec-grid"><table class="facts-t"><caption>Record</caption><tbody>
        <tr><th scope="row">Stage</th><td>${esc(stageName(c.stage))}</td></tr><tr><th scope="row">Owner</th><td>${esc(person(c.owner))}</td></tr>
        <tr><th scope="row">Next step</th><td>${esc(c.next)}</td></tr><tr><th scope="row">Due</th><td class="num">${c.due} (${fmt(c.due, true)})</td></tr>
        <tr><th scope="row">From</th><td>${esc(sourceName(c.source))}${intro ? `, through <a href="#/company/${intro.id}">${esc(intro.name)}</a>` : ''}</td></tr><tr><th scope="row">Met by</th><td>${esc(person(c.metBy))}</td></tr>
        <tr><th scope="row">Domain</th><td><code>${esc(c.domain)}</code></td></tr>
        ${c.people.map((p, n) => `<tr><th scope="row">${n ? '' : 'People'}</th><td>${esc(p.name)}, ${esc(p.role)}, <a href="mailto:${esc(p.email)}">${esc(p.email)}</a></td></tr>`).join('')}</tbody></table>
        <section class="rec-act" aria-labelledby="la-h">${c.draft ? `<div id="draft">${draftBox(c)}</div>` : ''}<div id="log"><h2 id="la-h">Log an action <kbd aria-hidden="true">l</kbd></h2>${logForm(c, { rows: 2 })}</div></section></div>
      <table class="acts-t"><caption>Activity, newest first</caption><thead><tr><th scope="col">Date</th><th scope="col">Kind</th><th scope="col">Way</th><th scope="col">By</th><th scope="col">What</th></tr></thead>
        <tbody>${c.activity.map((a) => `<tr class="${a.fresh ? 'fresh' : ''}"><td class="num"><time datetime="${a.at}">${a.at}</time></td><td>${esc(a.kind)}</td><td>${a.dir === 'in' ? 'In' : 'Out'}</td><td>${esc(short(a.by))}</td><td>${esc(a.text)}</td></tr>`).join('')}</tbody></table></div>` };
  }
  function contacts() {
    const all = D.companies.flatMap((c) => c.people.map((p) => ({ ...p, c }))).sort((a, b) => a.name.localeCompare(b.name));
    return { title: 'Contacts', html: `<div class="l-head"><h1 tabindex="-1">Contacts</h1><p class="note">${plural(all.length, 'person')}.</p></div><div class="tbl-wrap"><table class="ledger"><caption class="vh">Contacts</caption><thead><tr><th scope="col">Name</th><th scope="col">Role</th><th scope="col">Company</th><th scope="col">Email</th><th scope="col">Last contact</th></tr></thead>
      <tbody>${all.map((p) => `<tr><th scope="row" data-label="Name">${esc(p.name)}</th><td data-label="Role">${esc(p.role)}</td><td data-label="Company"><a href="#/company/${p.c.id}">${esc(p.c.name)}</a></td><td data-label="Email"><a href="mailto:${esc(p.email)}">${esc(p.email)}</a></td><td data-label="Last contact" class="num">${last(p.c)}</td></tr>`).join('')}</tbody></table></div>` };
  }
  function more() {
    return { title: 'More', html: `<div class="l-head"><h1 tabindex="-1">More</h1></div><table class="ledger more-t"><caption class="vh">More pages</caption><tbody><tr><th scope="row"><a href="#/import">Import</a></th><td>contacts from a CSV</td></tr><tr><th scope="row"><a href="#/vault">Vaults</a></th><td>open, start, hand to a phone by QR</td></tr><tr><th scope="row"><a href="#/requests">Requests</a></th><td>ask the CRM's keeper</td></tr><tr><th scope="row"><a href="#/you">You</a></th><td>your name and this browser's key</td></tr></tbody></table>` };
  }

  // Keys: only when not typing in a field.
  let sel = -1;
  const mark = (i, focus) => { const trs = $$('table.ledger tbody tr[data-id]'); if (!trs.length) return; sel = Math.max(0, Math.min(trs.length - 1, i)); trs.forEach((t, n) => { t.classList.toggle('sel', n === sel); if (n === sel) t.setAttribute('aria-current', 'true'); else t.removeAttribute('aria-current'); }); if (focus) trs[sel].focus(); };
  document.addEventListener('keydown', (e) => {
    if (e.ctrlKey || e.metaKey || e.altKey || e.target.closest('input,textarea,select')) return;
    const tr = $$('table.ledger tbody tr[data-id]')[sel]; const onRec = /^#\/company\//.test(location.hash);
    if (e.key === 'j') { e.preventDefault(); mark(sel + 1, true); }
    else if (e.key === 'k') { e.preventDefault(); mark(sel - 1, true); }
    else if (e.key === 'Enter' && tr && e.target === tr) { location.hash = `#/company/${tr.dataset.id}`; }
    else if (e.key === 'l') { e.preventDefault(); if (tr) location.hash = `#/company/${tr.dataset.id}/log`; else if (onRec) { const f = $('#log textarea'); if (f) f.focus(); } }
    else if (e.key === 'd') { const id = tr ? tr.dataset.id : onRec && location.hash.split('/')[2]; const c = id && company(id); if (c && c.draft) { e.preventDefault(); location.hash = `#/company/${id}/draft`; } else if (c) say('No draft waiting on this one.'); }
    else if (e.key === '/') { const f = $('#f-q'); if (f) { e.preventDefault(); f.focus(); f.select(); } }
  });
  document.addEventListener('submit', (e) => { const f = e.target; if (!f.dataset.filter) return; e.preventDefault(); location.hash = toHash(f.dataset.filter, f.q.value || ' '); });
  document.addEventListener('click', (e) => { const tr = e.target.closest('table.ledger tbody tr[data-id]'); if (tr && !e.target.closest('a')) mark($$('table.ledger tbody tr[data-id]').indexOf(tr), false); });

  window.CRM.start({ design: 'The Ledger', home: 'ledger', navOf: { company: 'ledger', board: 'ledger' }, after: () => { sel = -1; }, pages: { ledger, board: ledger, today, 'follow-ups': followUps, company: record, contacts, more } });
})();

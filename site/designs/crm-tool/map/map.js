/* Design 4 of 5, The Map: who knows whom. The first screen maps the companies by where they came from (the summit,
   introductions, came to us), each linked to whoever on the team met them, and introductions linked company to
   company. The lead board is a list beside the map. The wires are drawn over the page; the same facts are in words
   on every node, so nothing depends on the drawing. a.crm.design, 24 Nov 2026. */
(function () {
  'use strict';
  const { keyTag, D, $, $$, esc, days, fmt, longDate, plural, company, person, stageName, sourceName, status, badges, byUrgency, dayList, actionButton, logForm, draftBox } = window.CRM;
  const TEAM = D.team.filter((t) => t.id !== 'agent');
  const short = (id) => person(id).replace(/\s*\(demo\)/, '');

  function node(c) {
    const st = status(c)[0]; const intro = c.introducedBy ? company(c.introducedBy) : null;
    return `<li class="node${c.stage === 'parked' ? ' parked' : ''}" id="n-${c.id}" data-met="${c.metBy}" data-intro="${c.introducedBy || ''}">
      <a href="#/company/${c.id}"><b>${esc(c.name)}</b><span class="how">Met by ${esc(short(c.metBy))}${intro ? `, through ${esc(intro.name)}` : ''}</span>
      <span class="ppl">${c.people.map((p) => `${esc(p.name)}${p.key === 'verified' ? ' (verified key)' : ''}`).join(', ')}</span>${st ? `<span class="st ${st.cls}">${esc(st.text)}</span>` : ''}</a></li>`;
  }
  function map() {
    const regions = D.sources.map((s) => ({ ...s, items: D.companies.filter((c) => c.source === s.id) }));
    const side = byUrgency(D.companies.filter((c) => c.stage !== 'parked'));
    return { title: 'Map', html: `<div class="map-page">
      <section class="map-wrap" aria-labelledby="m-h"><div class="m-head"><h1 id="m-h" tabindex="-1">Who knows whom</h1>
        <p class="note">${plural(D.companies.length, 'company')}, by where they came from. A solid line: who on the team met them. A dashed line: an introduction. Choose a person on the left to light up their part of the map.</p></div>
        <div class="map" id="map"><svg class="wires" id="wires" aria-hidden="true" focusable="false"></svg>
          <div class="team"><h2 class="vh">The team</h2><ul>${TEAM.map((t) => `<li><button type="button" class="person" id="p-${t.id}" data-who="${t.id}" aria-pressed="false"><span class="dot">${esc(short(t.id)[0])}</span>${esc(short(t.id))}<span class="cnt">${plural(D.companies.filter((c) => c.metBy === t.id).length, 'company')}</span></button></li>`).join('')}</ul></div>
          <div class="regions">${regions.map((r) => `<section class="region r-${r.id}" aria-labelledby="rg-${r.id}"><h2 id="rg-${r.id}">${esc(r.name)} <span class="n">${r.items.length}</span></h2><ul>${r.items.map(node).join('')}</ul></section>`).join('')}</div>
        </div></section>
      <aside class="side-board" aria-labelledby="sb-h"><h2 id="sb-h">Lead board, most urgent first</h2>
        <ol>${side.map((c) => `<li><a href="#/company/${c.id}"><b>${esc(c.name)}</b><span>${esc(stageName(c.stage))} · ${esc(c.next)}</span></a>${badges(c)}</li>`).join('')}</ol>
        <p><a href="#/board">The full lead board</a></p></aside></div>` };
  }

  // Draw the wires once the nodes are laid out; again on resize. Hidden on a phone (CSS), where the words carry it.
  function wire() {
    const svg = $('#wires'), m = $('#map'); if (!svg || !m) return;
    const draw = () => {
      while (svg.firstChild) svg.firstChild.remove();
      const box = m.getBoundingClientRect(); svg.setAttribute('viewBox', `0 0 ${box.width} ${box.height}`); svg.setAttribute('width', box.width); svg.setAttribute('height', box.height);
      if (getComputedStyle(svg).display === 'none') return;
      const pt = (el, side) => { const r = el.getBoundingClientRect(); return { x: (side === 'r' ? r.right : side === 'l' ? r.left : r.left + r.width / 2) - box.left, y: r.top + r.height / 2 - box.top }; };
      const path = (d, cls, who) => { const p = document.createElementNS('http://www.w3.org/2000/svg', 'path'); p.setAttribute('d', d); p.setAttribute('class', cls); if (who) p.dataset.who = who; svg.append(p); };
      D.companies.forEach((c) => {
        const n = document.getElementById(`n-${c.id}`), t = document.getElementById(`p-${c.metBy}`); if (!n || !t) return;
        const a = pt(t, 'r'), b = pt(n, 'l'); const mx = (a.x + b.x) / 2;
        path(`M${a.x} ${a.y} C${mx} ${a.y} ${mx} ${b.y} ${b.x} ${b.y}`, `met w-${c.metBy}`, c.metBy);
        if (c.introducedBy) { const f = document.getElementById(`n-${c.introducedBy}`); if (f) { const s = pt(f, 'r'), e = pt(n, 'r'); const bend = Math.max(s.x, e.x) + 28; path(`M${s.x} ${s.y} C${bend} ${s.y} ${bend} ${e.y} ${e.x} ${e.y}`, 'intro'); } }
      });
    };
    draw(); window.onresize = draw;
    $$('.person').forEach((b) => b.addEventListener('click', () => {
      const on = b.getAttribute('aria-pressed') !== 'true';
      $$('.person').forEach((x) => x.setAttribute('aria-pressed', 'false')); b.setAttribute('aria-pressed', String(on));
      m.classList.toggle('focus', on); $$('.node', m).forEach((n) => n.classList.toggle('lit', on && n.dataset.met === b.dataset.who));
      $$('path.met', svg).forEach((p) => p.classList.toggle('lit', on && p.dataset.who === b.dataset.who));
      window.CRM.say(on ? `${short(b.dataset.who)} met ${$$('.node.lit', m).length} companies; they are highlighted.` : 'Showing everyone.');
    }));
  }

  function companyPage(id) {
    const c = company(id); if (!c) return map();
    const intro = c.introducedBy ? company(c.introducedBy) : null;
    const introduced = D.companies.filter((x) => x.introducedBy === c.id);
    return { title: c.name, html: `<div class="co"><p class="crumb"><a href="#/map">Map</a> › ${esc(sourceName(c.source))} › ${esc(c.name)}</p>
      <h1 tabindex="-1">${esc(c.name)}</h1><p class="meta">${esc(stageName(c.stage))} · owned by ${esc(person(c.owner))} · ${badges(c)}</p>
      <section class="trail" aria-labelledby="tr-h"><h2 id="tr-h">How we know them</h2>
        <ol class="chain"><li><span class="k">Where</span>${esc(sourceName(c.source))}</li><li><span class="k">Met by</span>${esc(person(c.metBy))}</li>${intro ? `<li><span class="k">Through</span><a href="#/company/${intro.id}">${esc(intro.name)}</a></li>` : ''}<li class="here"><span class="k">Company</span>${esc(c.name)}</li><li><span class="k">People</span>${c.people.map((p) => `${esc(p.name)}, ${esc(p.role)}`).join('; ')}</li></ol>
        ${introduced.length ? `<p>They introduced us to ${introduced.map((x) => `<a href="#/company/${x.id}">${esc(x.name)}</a>`).join(', ')}.</p>` : ''}</section>
      <div class="co-cols"><section class="act-box" aria-labelledby="nx-h"><h2 id="nx-h">Next: ${esc(c.next)}</h2><p class="note">Due ${fmt(c.due, true)}</p>
        ${c.draft ? `<div id="draft">${draftBox(c)}</div>` : ''}<div id="log"><h3>Log an action</h3>${logForm(c, { rows: 2 })}</div></section>
        <section aria-labelledby="ac-h"><h2 id="ac-h">Activity</h2><ol class="acts">${c.activity.map((a) => `<li class="${a.fresh ? 'fresh' : ''}"><p class="note"><time datetime="${a.at}">${fmt(a.at, true)}</time> · ${esc(a.kind)}${a.dir === 'in' ? ' · they wrote' : ''} · ${esc(person(a.by))}</p><p>${esc(a.text)}</p></li>`).join('')}</ol>
          <h2>People</h2><ul class="ppl-list">${c.people.map((p) => `<li><b>${esc(p.name)}</b>, ${esc(p.role)} ${keyTag(p, c)}<br><a href="mailto:${esc(p.email)}">${esc(p.email)}</a></li>`).join('')}</ul></section></div></div>` };
  }

  const rowList = (l) => `<ol class="rows">${l.map((c) => `<li><div><a href="#/company/${c.id}"><b>${esc(c.name)}</b></a><p>${esc(c.next)} · <span class="note">met by ${esc(short(c.metBy))}${c.introducedBy ? `, through ${esc(company(c.introducedBy).name)}` : ''}</span></p><p>${badges(c)}</p></div>${actionButton(c)}</li>`).join('') || '<li>Nothing here.</li>'}</ol>`;
  function today() {
    const { now, week } = dayList();
    return { title: 'Today', html: `<div class="co"><h1 tabindex="-1">Today</h1><p class="note">${longDate(D.today)}. Each line says how we know them.</p><h2>Do today</h2>${rowList(now)}<h2>Later this week</h2>${rowList(week)}</div>` };
  }
  function followUps() {
    const live = D.companies.filter((c) => c.stage !== 'parked').sort((a, b) => (a.due < b.due ? -1 : 1));
    return { title: 'Follow-ups', html: `<div class="co"><h1 tabindex="-1">Follow-ups</h1><p class="note">Every next step by date.</p><ol class="rows">${live.map((c) => `<li><div><p class="note"><time datetime="${c.due}">${fmt(c.due, true)}</time></p><a href="#/company/${c.id}"><b>${esc(c.name)}</b></a><p>${esc(c.next)}</p><p>${badges(c)}</p></div>${actionButton(c)}</li>`).join('')}</ol></div>` };
  }
  function board() {
    return { title: 'Lead board', html: `<div class="co"><h1 tabindex="-1">Lead board</h1>${D.stages.map((s) => { const l = byUrgency(D.companies.filter((c) => c.stage === s.id)); return `<h2>${esc(s.name)} <span class="n">${l.length}</span></h2>${rowList(l)}`; }).join('')}</div>` };
  }
  function contacts() {
    return { title: 'Contacts', html: `<div class="co"><h1 tabindex="-1">Contacts</h1><p class="note">Grouped by who on the team met them.</p>${TEAM.map((t) => { const cs = D.companies.filter((c) => c.metBy === t.id); return `<h2>Met by ${esc(person(t.id))}</h2><ul class="ppl-list cols">${cs.flatMap((c) => c.people.map((p) => `<li><a href="#/company/${c.id}"><b>${esc(p.name)}</b></a>, ${esc(p.role)} ${keyTag(p, c)}<br>${esc(c.name)} · <span class="note">${esc(p.email)}</span></li>`)).join('')}</ul>`; }).join('')}</div>` };
  }
  function more() {
    return { title: 'More', html: `<div class="co"><h1 tabindex="-1">More</h1><ul class="rows more"><li><a href="#/follow-ups"><b>Follow-ups</b></a></li><li><a href="#/import"><b>Import contacts</b></a></li><li><a href="#/vault"><b>Open or start a vault</b></a></li><li><a href="#/requests"><b>Requests</b></a></li><li><a href="#/you"><b>You</b></a></li></ul></div>` };
  }

  window.CRM.start({ design: 'The Map', home: 'map', navOf: { company: 'map', 'follow-ups': 'more' }, after: (name) => { window.onresize = null; if (name === 'map' || !name) requestAnimationFrame(wire); }, pages: { map, company: companyPage, today, 'follow-ups': followUps, board, contacts, more } });
})();

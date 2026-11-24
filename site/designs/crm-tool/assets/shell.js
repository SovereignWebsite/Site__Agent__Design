/* The shared shell for the five CRM design prototypes: helpers, the router, the vault switcher, logging an action,
   sending a waiting draft, and the pages every design shares in content (vault, import, requests, You).
   Nothing is written anywhere: every change lives in this tab until it is reloaded. a.crm.design, 24 Nov 2026. */
(function () {
  'use strict';
  const D = window.CRM_DATA;
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => [...(r || document).querySelectorAll(s)];
  const esc = (s) => String(s == null ? '' : s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const day = (s) => Date.UTC(+s.slice(0, 4), +s.slice(5, 7) - 1, +s.slice(8, 10)) / 864e5;
  const days = (from, to) => day(to || D.today) - day(from);
  const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const DOW = ['Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed'];
  const LONG = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday'];
  const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  const longDate = (s) => `${LONG[((day(s) % 7) + 7) % 7]} ${+s.slice(8, 10)} ${MONTHS[+s.slice(5, 7) - 1]} ${s.slice(0, 4)}`;
  const fmt = (s, withDay) => { const d = day(s); const t = `${+s.slice(8, 10)} ${MON[+s.slice(5, 7) - 1]}`; return withDay ? `${DOW[((d % 7) + 7) % 7]} ${t}` : t; };
  const plural = (n, w) => `${n} ${w}${n === 1 ? '' : 's'}`;
  const company = (id) => D.companies.find((c) => c.id === id);
  const person = (id) => (D.team.find((t) => t.id === id) || { name: id }).name;
  const stageName = (id) => (D.stages.find((s) => s.id === id) || { name: id }).name;
  const sourceName = (id) => (D.sources.find((s) => s.id === id) || { name: id }).name;

  // Status: each one in words, with a shape from brand.css. Ordered most urgent first.
  function status(c) {
    const out = []; const late = days(c.due);
    if (c.stage !== 'parked' && late > 0) out.push({ k: 'overdue', cls: 'st-overdue', text: `Overdue ${plural(late, 'day')}` });
    if (late === 0) out.push({ k: 'today', cls: 'st-today', text: 'Due today' });
    if (c.draft) out.push({ k: 'draft', cls: 'st-draft', text: 'Draft waiting' });
    if (c.repliedOn) { const n = days(c.repliedOn); out.push({ k: 'replied', cls: 'st-replied', text: n === 0 ? 'They replied today' : n === 1 ? 'They replied yesterday' : `They replied ${n} days ago` }); }
    if (c.noReplySince) out.push({ k: 'noreply', cls: 'st-noreply', text: `No reply for ${plural(days(c.noReplySince), 'day')}` });
    return out;
  }
  const badges = (c) => status(c).map((s) => `<span class="st ${s.cls}">${esc(s.text)}</span>`).join(' ');
  const urgency = (c) => (c.stage === 'parked' ? 1e4 : 0) - Math.max(0, days(c.due)) * 10 + days(D.today, c.due) * 5 - (c.draft ? 8 : 0) - (c.repliedOn ? 6 : 0);
  const byUrgency = (list) => [...list].sort((a, b) => urgency(a) - urgency(b));
  // The day's list: overdue, due today, drafts and replies waiting on us; then the rest of the week.
  function dayList() {
    const live = D.companies.filter((c) => c.stage !== 'parked');
    const now = byUrgency(live.filter((c) => days(c.due) >= 0 || c.draft || c.repliedOn));
    const week = byUrgency(live.filter((c) => !now.includes(c) && days(D.today, c.due) <= 7));
    const waiting = live.filter((c) => c.noReplySince);
    return { now, week, waiting };
  }
  // The one action for a company, as a button: send the draft, answer a reply, or log what was done.
  function actionButton(c, cls) {
    if (c.draft) return `<a class="btn warn ${cls || ''}" href="#/company/${c.id}/draft">Review and send</a>`;
    if (c.repliedOn) return `<a class="btn ${cls || ''}" href="#/company/${c.id}/log">Answer ${esc(c.people[0].name.split(' ')[0])}</a>`;
    return `<a class="btn ${cls || ''}" href="#/company/${c.id}/log">Log an action</a>`;
  }

  // Forms every design uses: log an action, the waiting draft.
  function logForm(c, opts) {
    const o = opts || {};
    return `<form class="form log" data-log="${c.id}" aria-label="Log an action on ${esc(c.name)}">
      <div class="row">
        <label>What kind<select name="kind">${D.kinds.map((k) => `<option>${k}</option>`).join('')}</select></label>
        <label>With<select name="who">${c.people.map((p) => `<option>${esc(p.name)}</option>`).join('')}</select></label>
      </div>
      <label>What happened<textarea name="text" rows="${o.rows || 3}" required placeholder="For example: called Mira, she wants the proposal by Friday"></textarea></label>
      <div class="row">
        <label>Next step<input name="next" value="${esc(c.next)}"></label>
        <label>Due<input name="due" type="date" value="${esc(c.due)}"></label>
      </div>
      <p><button class="btn" type="submit">${esc(o.button || 'Log it')}</button> <span class="note">Demo: kept in this tab only, nothing is written.</span></p>
    </form>`;
  }
  function draftBox(c) {
    if (!c.draft) return '';
    return `<section class="draft-box" aria-labelledby="draft-h-${c.id}">
      <h3 id="draft-h-${c.id}"><span class="st st-draft">Draft waiting</span> ${esc(c.draft.subject)}</h3>
      <p class="note">To ${esc(c.draft.to)}. Drafted by the CRM agent from the last call; read it before it goes.</p>
      <label>The message<textarea name="body" rows="7" data-body="${c.id}">${esc(c.draft.body)}</textarea></label>
      <p><button class="btn warn" type="button" data-send="${c.id}">Send it (demo)</button> <button class="btn quiet" type="button" data-discard="${c.id}">Not now</button></p>
    </section>`;
  }

  // The pages every design shares in content; each design dresses them in its own layout.
  function vaultPage(arg) {
    const pick = D.vaults.find((v) => v.id === arg);
    return { title: 'Open or start a vault', html: `<h1 tabindex="-1">Open or start a vault</h1>
      <p class="lead">Your CRM lives in a vault that only you hold the key to. Its key is used in this browser and never sent to this site.</p>
      <section class="panel" aria-labelledby="v-open"><h2 id="v-open">Your vaults</h2>
        <ul class="vault-list">${D.vaults.map((v) => `<li${v.id === 'demo' ? ' class="on"' : ''}><span><b>${esc(v.name)}</b> <span class="note">${esc(v.note)}</span></span>${v.id === 'demo' ? '<span class="st st-today">Open now</span>' : `<a class="btn quiet" href="#/vault/${v.id}">Open</a>`}</li>`).join('')}</ul>
        ${pick && pick.id !== 'demo' ? `<form class="form" data-fake="vault" aria-label="Open ${esc(pick.name)}"><h3>Open ${esc(pick.name)}</h3><label>Its vault key<input name="key" type="password" autocomplete="off" spellcheck="false"></label><p><button class="btn" type="submit">Open ${esc(pick.name)}</button> <span class="note">Prototype: no vault opens here.</span></p></form>` : ''}
      </section>
      <section class="panel" aria-labelledby="v-new"><h2 id="v-new">Start a new vault</h2>
        <p>Makes an empty, encrypted CRM vault with your access token, marked as yours. You see its key once: keep it safe.</p>
        <form class="form" data-fake="new" aria-label="Start a new vault"><label>Name it<input name="name" placeholder="For example: Summit CRM"></label><p><button class="btn" type="submit">Start the vault</button></p></form>
      </section>
      <section class="panel" id="qr" aria-labelledby="v-qr"><h2 id="v-qr">Hand a vault to your phone</h2>
        <ol class="steps"><li>On this computer, choose the vault and show its QR code.</li><li>On your phone, open this CRM, then You, then "Scan a vault".</li><li>The key goes across by the camera only: no message, no email.</li></ol>
        <div class="qr-box" role="img" aria-label="Where the QR code appears">The QR code appears here. The demo has no key to hand over.</div>
      </section>` };
  }
  function importPage() {
    return { title: 'Import contacts', html: `<h1 tabindex="-1">Import contacts</h1>
      <p class="lead">One line per person or company in a spreadsheet, saved as CSV. Only <b>company</b> is required; empty cells stay empty.</p>
      <ol class="steps"><li><a href="#/import">Download the template</a> <span class="note">(prototype: no file)</span></li><li>Fill it in: only people you have a reason to keep in touch with.</li><li>Drop it here, check what will be added, then add it.</li></ol>
      <form class="form panel" data-fake="import" aria-label="Import a CSV"><label>CSV file<input type="file" name="csv" accept=".csv,text/csv"></label><label>Or paste it<textarea name="text" rows="5" spellcheck="false">company,domain,person,email,met_at
Example Ltd,example.com,Sam Example,sam@example.com,summit</textarea></label><p><button class="btn" type="submit">Check what will be added</button></p></form>
      <p class="note">Companies already here are matched by domain, then name; people by email. Nothing already here is changed.</p>` };
  }
  function requestsPage() {
    return { title: 'Requests', html: `<h1 tabindex="-1">Requests</h1>
      <p class="lead">Ask the agent that builds this CRM for a feature, a fix or an answer. Your request is signed by this browser and sealed so only the keeper can read it.</p>
      <p class="done"><b>Not contacts' details.</b> Requests reach the keeper, not your vault.</p>
      <form class="form panel" data-fake="request" aria-label="Send a request"><label>Kind<select name="kind"><option>A feature</option><option>A question</option><option>Something is wrong</option><option>A workflow</option><option>An idea</option></select></label><label>What you would like<textarea name="text" rows="4"></textarea></label><p><button class="btn" type="submit">Sign, seal and send</button></p></form>
      <h2>Answers</h2><ul class="answers">${D.requests.map((r) => `<li><p class="note"><time datetime="${r.at}">${fmt(r.at, true)}</time> · ${esc(r.kind)}</p><p>${esc(r.text)}</p><p><b>Keeper:</b> ${esc(r.answer)}</p></li>`).join('')}</ul>` };
  }
  function youPage() {
    const mine = D.companies.filter((c) => c.owner === 'you');
    return { title: 'You', html: `<h1 tabindex="-1">You</h1>
      <p class="lead">In the demo you are "You". In your own vault, your name goes on every action you log.</p>
      <section class="panel" aria-labelledby="y-me"><h2 id="y-me">This browser</h2>
        <dl class="facts"><dt>Your name</dt><dd>You (demo)</dd><dt>This browser's key</dt><dd><code>sha256:demo-0000</code> (made up)</dd><dt>Locked with</dt><dd>No passkey in the demo</dd><dt>Companies you own</dt><dd>${mine.length}</dd></dl>
      </section>
      <section class="panel" aria-labelledby="y-v"><h2 id="y-v">Vaults on this browser</h2><p>${D.vaults.length - 1} kept here, plus the demo. <a href="#/vault">Open or start a vault</a>, or <a href="#/vault/demo/qr">scan one from another device</a>.</p>
        <p><button class="btn quiet" type="button" data-fake-btn="logout">Log out of this browser</button> <span class="note">removes the keys kept here; the vaults are not touched.</span></p></section>` };
  }

  // Live announcements for screen readers, and the demo's in-tab changes.
  function say(msg) { const l = $('#live'); if (l) { l.textContent = ''; setTimeout(() => { l.textContent = msg; }, 30); } }
  let render = () => {};
  document.addEventListener('submit', (ev) => {
    const f = ev.target;
    if (f.dataset.log) {
      ev.preventDefault(); const c = company(f.dataset.log); const v = Object.fromEntries(new FormData(f));
      c.activity.unshift({ at: D.today, kind: v.kind, dir: 'out', by: 'you', text: `${v.who}: ${v.text}`, fresh: true });
      if (v.next) c.next = v.next; if (v.due) c.due = v.due; delete c.repliedOn; if (v.kind !== 'Note') delete c.noReplySince;
      say(`Logged on ${c.name}. Demo: nothing written.`); render(true, `Logged on ${c.name}. In the demo it stays in this tab.`);
    } else if (f.dataset.fake) {
      ev.preventDefault(); say('Prototype: this does nothing yet.');
      const p = f.querySelector('.fake-msg') || Object.assign(document.createElement('p'), { className: 'done fake-msg', role: 'status' });
      p.textContent = 'Prototype: nothing happens here. In the live CRM this step is real.'; f.append(p);
    }
  });
  document.addEventListener('click', (ev) => {
    const t = ev.target.closest('[data-send],[data-discard],[data-fake-btn]'); if (!t) return;
    if (t.dataset.send) { const c = company(t.dataset.send); const body = $(`[data-body="${c.id}"]`); c.activity.unshift({ at: D.today, kind: 'Email', dir: 'out', by: 'you', text: `Sent "${c.draft.subject}"${body && body.value !== c.draft.body ? ' (edited)' : ''}.`, fresh: true }); delete c.draft; say(`Sent to ${c.name} (demo).`); render(true, `Sent to ${c.name}. In the demo nothing leaves this tab.`); }
    if (t.dataset.discard) { say('Kept the draft for later.'); location.hash = `#/company/${t.dataset.discard}`; }
    if (t.dataset.fakeBtn) say('Prototype: this does nothing yet.');
  });

  // The vault switcher: same place, same words, in all five designs.
  function switcher() {
    const b = $('#vault-btn'), pop = $('#vault-pop'); if (!b) return;
    const close = (focus) => { pop.hidden = true; b.setAttribute('aria-expanded', 'false'); if (focus) b.focus(); };
    b.addEventListener('click', () => { const open = pop.hidden; pop.hidden = !open; b.setAttribute('aria-expanded', String(open)); if (open) { const a = $('a', pop); if (a) a.focus(); } });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !pop.hidden) close(true); });
    document.addEventListener('click', (e) => { if (!pop.hidden && !e.target.closest('.vault-switch')) close(false); });
    pop.addEventListener('click', (e) => { if (e.target.closest('a')) close(false); });
  }

  // The router: #/page/arg/sub. Each design passes its own pages; the shared ones fill the gaps.
  function start(opts) {
    const pages = Object.assign({ vault: vaultPage, import: importPage, requests: requestsPage, you: youPage }, opts.pages);
    const main = $('#main');
    render = (keep, notice) => {
      const [name, arg, sub] = (location.hash.replace(/^#\/?/, '').split('#')[0] || opts.home).split('/');
      const fn = pages[name] || pages[opts.home];
      const r = fn(arg, sub);
      main.innerHTML = (notice ? `<p class="done" role="status">${esc(notice)}</p>` : '') + r.html;
      document.title = `${r.title}: ${opts.design}, SovereignWeb.site CRM (prototype)`;
      const navOf = Object.assign({ import: 'more', vault: 'more', requests: 'more', you: 'more' }, opts.navOf);
      const cur = navOf[name] || (pages[name] ? name : opts.home);
      $$('[data-nav]').forEach((a) => { if (a.dataset.nav === cur) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); });
      if (opts.after) opts.after(name, arg, sub);
      if (!keep) { const h = $('h1', main); if (h && window.__crmRouted) h.focus(); window.scrollTo(0, 0); }
      window.__crmRouted = true;
      const target = sub && document.getElementById(sub); if (target) { target.scrollIntoView(); const f = target.querySelector('textarea,input,select'); if (f) f.focus(); }
    };
    window.addEventListener('hashchange', () => render(false));
    switcher(); render(false);
  }

  window.CRM = { D, $, $$, esc, days, fmt, longDate, plural, company, person, stageName, sourceName, status, badges, byUrgency, dayList, actionButton, logForm, draftBox, say, start };
})();

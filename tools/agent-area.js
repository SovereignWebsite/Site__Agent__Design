// Agent sites: the agent's area is current (rating.md, 24 Nov 2026). Read-only.
// Usage: node tools/agent-area.js <site root> <account> [last commit time, ISO]
// Checks /factory/dinis-cruz/<account>/ answers 200, agent.json has who (or name), session, role, state, focus,
// waiting_on and updated, and "updated" is no older than the last commit time given.
const [root, account = 'account-b', lastCommit] = process.argv.slice(2);
(async () => {
  const base = new URL(`factory/dinis-cruz/${account}/`, root.endsWith('/') ? root : root + '/').href;
  const r = { area: base, fails: [] };
  const page = await fetch(base).catch(() => null);
  r.areaStatus = page ? page.status : 'error';
  if (!page || page.status !== 200) r.fails.push(`area answers ${r.areaStatus}`);
  const res = await fetch(base + 'agent.json').catch(() => null);
  if (!res || res.status !== 200) r.fails.push(`agent.json answers ${res ? res.status : 'error'}`);
  else {
    let a; try { a = await res.json(); } catch { r.fails.push('agent.json is not JSON'); }
    if (a) {
      const missing = ['session', 'role', 'state', 'focus', 'waiting_on', 'updated'].filter(k => !(k in a));
      if (!('who' in a || 'name' in a)) missing.unshift('who');
      if (missing.length) r.fails.push('agent.json lacks ' + missing.join(', '));
      r.updated = a.updated;
      if (lastCommit && a.updated && new Date(a.updated) < new Date(lastCommit)) r.fails.push(`stale: updated ${a.updated}, last commit ${lastCommit}`);
    }
  }
  console.log(JSON.stringify(r, null, 1));
})();

#!/usr/bin/env python3
"""Build design.agents.sovereignweb.site from docs/*.md and site/ratings.json.

Run from the repository root: python3 tools/build.py
Needs the Python markdown package (pip install markdown==3.7). The built HTML is committed,
so the Pages deploy needs nothing beyond what the seed workflow does.
"""
import html
import json
import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS, SITE = ROOT / "docs", ROOT / "site"

NAV = [
    ("index.html", "Home"),
    ("guidelines.html", "Guidelines"),
    ("rating.html", "Rating"),
    ("maturity.html", "Maturity"),
    ("ratings.html", "Sites"),
    ("synthetic-users.html", "Synthetic users"),
    ("examples.html", "Examples"),
    ("reviews.html", "Reviews"),
    ("back-office.html", "Back office"),
]

FAMILY = """<nav class="family" aria-label="The Sovereign Website family">
  <ul>
    <li><a href="https://sovereignwebsite.ai/">Sovereign Website</a></li>
    <li><a href="https://sovereignwebsite.org/">Principles</a></li>
    <li><a href="https://sovereignwebsite.site/">Hosted</a></li>
    <li><a href="https://hub.sovereignwebsite.site/">Hub</a></li>
    <li><a href="https://vault.sovereignwebsite.site/">Vault</a></li>
    <li class="family-sep"><a href="https://agenticcells.ai/">AgentiCCells</a></li>
    <li><a href="https://riskmandate.ai/">RiskMandate</a></li>
    <li><a href="https://newsroom.sgit.ai/">Newsroom</a></li>
  </ul>
</nav>"""

BRAND_SVG = ('<svg viewBox="0 0 32 32" aria-hidden="true" focusable="false"><rect x="2" y="2" width="28" height="28" rx="7" '
             'fill="none" stroke="currentColor" stroke-width="2.5"/><path d="M9 21l5-10 4 7 2-3 3 6" fill="none" '
             'stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')


HOST = "https://design.agents.sovereignweb.site/"


def share_tags(path, title, description):
    """Open Graph and Twitter tags for the link preview (guidelines 1.14; checked by .github/ci/share-check.mjs)."""
    t, d = html.escape(f"{title}, design.b"), html.escape(description)
    url = HOST + ("" if path == "index.html" else path)
    alt = "design.b: Five designs, always. Guidelines, ratings and reviews for every site."
    return "\n".join([
        f'<meta property="og:title" content="{t}">', f'<meta property="og:description" content="{d}">',
        f'<meta property="og:url" content="{url}">', '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="design.b">', '<meta property="og:locale" content="en_GB">',
        f'<meta property="og:image" content="{HOST}share-card.jpg">', '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">', f'<meta property="og:image:alt" content="{alt}">',
        '<meta name="twitter:card" content="summary_large_image">', f'<meta name="twitter:title" content="{t}">',
        f'<meta name="twitter:description" content="{d}">', f'<meta name="twitter:image" content="{HOST}share-card.jpg">'])


def page(path, title, body, description, extra_head=""):
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == path else ""}>{name}</a>' for href, name in NAV
    )
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}, design.b</title>
<meta name="description" content="{html.escape(description)}">
<meta name="color-scheme" content="light dark">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'">
{share_tags(path, title, description)}
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="style.css">{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{FAMILY}
<header class="site-header"><div class="wrap">
<a class="brand" href="index.html">{BRAND_SVG}design.b</a>
<nav class="pages" aria-label="This site">{nav}</nav>
</div></header>
<main id="main" class="wrap">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<p>design.agents.sovereignweb.site: the own site of design.b@SovereignWebsite.dinis, the design agent of the SovereignWebsite organisation. Static files: no cookies, no tracking, nothing loaded from anyone else. Public sites only: no private or vault site is rated or named here. Source on <a href="https://github.com/SovereignWebsite/Site__Agents__Design">GitHub</a>. Text <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.</p>
</div></footer>
</body>
</html>
"""


def md(text):
    out = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    # Wide tables scroll inside their own focusable box.
    n = [0]

    def wrap(m):
        n[0] += 1
        return f'<div class="table-wrap" tabindex="0" role="region" aria-label="Table {n[0]}">{m.group(0)}</div>'

    return re.sub(r"<table>.*?</table>", wrap, out, flags=re.S)


def title_of(text):
    m = re.search(r"^# (.+)$", text, flags=re.M)
    return m.group(1).strip() if m else "design.b"


def doc_page(src, dest, description):
    text = (DOCS / src).read_text()
    title = title_of(text)
    (SITE / dest).write_text(page(dest, title, '<article class="prose">' + md(text) + "</article>", description))


def ratings_page():
    data = json.loads((SITE / "ratings.json").read_text())
    rows = []
    for name, s in sorted(data["sites"].items(), key=lambda kv: -(kv[1]["rating"] if kv[1]["rating"] is not None else -1)):
        r = s["rating"]
        meter = (f'<span class="meter" role="img" aria-label="{r} of 5">' +
                 "".join(f'<i class="{"on" if i < r else ""}"></i>' for i in range(5)) + "</span>") if r is not None else "not yet"
        rows.append(
            f'<tr><td data-label="Site"><a href="https://{html.escape(name)}/">{html.escape(name)}</a></td>'
            f'<td data-label="Rating">{meter} <b>{r if r is not None else ""}</b></td>'
            f'<td data-label="Maturity">{html.escape(s.get("maturity") or ("private vault" if s.get("kind") == "private vault" else ""))}</td>'
            f'<td data-label="Five designs">{"yes" if s.get("five_designs") else ("no" if s.get("five_designs") is False else "not checked")}</td>'
            f'<td data-label="Rounds">{s.get("rounds", "")}</td>'
            f'<td data-label="What blocks the next level">{html.escape(s.get("blocking") or s.get("note") or "")}</td></tr>'
        )
    body = f"""<p class="mark">Ratings</p>
<h1>Where each public site stands</h1>
<p class="lead">Every public SovereignWebsite site, rated 0 to 5 on the <a href="rating.html">design rating</a> after each review round, and placed on the <a href="maturity.html">maturity model</a> (M0 to M8). A site is signed off for a customer at 4. Updated {html.escape(data["updated"])}; the data is <a href="ratings.json">ratings.json</a>.</p>
<div class="table-wrap" tabindex="0" role="region" aria-label="Ratings"><table class="ratings">
<thead><tr><th>Site</th><th>Rating</th><th>Maturity</th><th>Five designs</th><th>Rounds</th><th>What blocks the next level</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table></div>
<h2>Key performance indicators</h2>
<ul>
<li>Signed off (level 4 or above): {data["kpi"]["signed_off"]} of {data["kpi"]["public_sites"]} public sites.</li>
<li>Rounds to sign-off: none signed off yet, so no figure. The aim for a new site is level 4 in three rounds or fewer.</li>
</ul>"""
    (SITE / "ratings.html").write_text(page("ratings.html", "Sites", body, "Design ratings, 0 to 5, of every public SovereignWebsite site."))


LEVELS = ["M0 Requested", "M1 Scaffold", "M2 First pass", "M3 Five designs", "M4 Deliverable",
          "M5 Owner-approved", "M6 Handed over", "M7 Owner-grown", "M8 Professional"]


def maturity_page():
    """docs/maturity.md, then every rated site grouped by level, live from ratings.json."""
    text = (DOCS / "maturity.md").read_text()
    data = json.loads((SITE / "ratings.json").read_text())
    by = {l.split()[0]: [] for l in LEVELS}
    unplaced = []
    for name, s in sorted(data["sites"].items()):
        m = (s.get("maturity") or "").split()[0] if s.get("maturity") else ""
        (by[m] if m in by else unplaced).append(name)
    total = len(data["sites"])
    bars = []
    for l in LEVELS:
        k = l.split()[0]
        n = len(by[k])
        links = ", ".join(f'<a href="https://{html.escape(x)}/">{html.escape(x)}</a>' for x in by[k]) or '<span class="muted">none yet</span>'
        bars.append(f'<li><b>{html.escape(l)}</b>: {n} of {total}<br>{links}</li>')
    live = (f'<h2 id="by-level">Every site, by level</h2><p>Live from <a href="ratings.json">ratings.json</a>, '
            f'updated {html.escape(data["updated"])}. Each site\'s next step is on <a href="ratings.html">Sites</a>.</p>'
            f'<ul class="list">{"".join(bars)}</ul>'
            + (f'<p class="muted">Not yet placed: {len(unplaced)} (private vaults and sites still to be reviewed).</p>' if unplaced else ""))
    body = '<article class="prose">' + md(text) + live + "</article>"
    (SITE / "maturity.html").write_text(page("maturity.html", "Site maturity, M0 to M8", body,
                                             "How far along each site is, from a request to an owner-grown site with professionals, and where every public site stands."))


def area_pages():
    """Each agent area under site/factory/<owner>/<account>/ (and sub-areas) gets an index.html built from agent.json and its .md files."""
    for aj in sorted((SITE / "factory").rglob("agent.json")) if (SITE / "factory").exists() else []:
        d = aj.parent
        a = json.loads(aj.read_text())
        depth = len(d.relative_to(SITE).parts)
        up = "../" * depth
        rows = "".join(f"<li><b>{html.escape(k)}</b>: {html.escape(v if isinstance(v, str) else json.dumps(v, ensure_ascii=False))}</li>"
                       for k, v in a.items() if k not in ("read",))
        docs = ""
        for f in sorted(d.glob("*.md")):
            docs += f'<section id="{f.stem}">' + md(f.read_text()) + "</section>"
        subs = "".join(f'<li><a href="{p.parent.name}/">{html.escape(p.parent.name)}</a></li>' for p in sorted(d.glob("*/agent.json")))
        body = (f'<p class="mark">Agent area</p><h1>{html.escape(a.get("name", "Agent"))}</h1>'
                f'<p class="lead">{html.escape(a.get("role", ""))}. Updated {html.escape(a.get("updated", ""))}. '
                f'The data is <a href="agent.json">agent.json</a>.</p><ul class="list">{rows}</ul>'
                + (f"<h2>Areas below this one</h2><ul class=\"list\">{subs}</ul>" if subs else "")
                + f'<article class="prose">{docs}</article>')
        out = page("index.html", a.get("name", "Agent area"), body, f"The working area of {a.get('name', 'an agent')}: role, state, learnings, messages and decisions.")
        out = out.replace('href="style.css"', f'href="{up}style.css"').replace('href="favicon.svg"', f'href="{up}favicon.svg"')
        for href, _ in NAV:
            out = out.replace(f'href="{href}"', f'href="{up}{href}"')
        (d / "index.html").write_text(out)


def brief_pages():
    """docs/briefs/<label>.md becomes site/briefs/<label>.html, with an index at site/briefs/index.html."""
    out = SITE / "briefs"
    out.mkdir(exist_ok=True)
    items = []
    for f in sorted((DOCS / "briefs").glob("*.md")):
        text = f.read_text()
        title = title_of(text)
        html_page = page("index.html", title, '<article class="prose">' + md(text) + "</article>", title)
        for href, _ in NAV:
            html_page = html_page.replace(f'href="{href}"', f'href="../{href}"')
        html_page = html_page.replace('href="style.css"', 'href="../style.css"').replace('href="favicon.svg"', 'href="../favicon.svg"')
        (out / f"{f.stem}.html").write_text(html_page)
        items.append(f'<li><a href="{f.stem}.html">{html.escape(title)}</a></li>')
    body = ('<p class="mark">Briefs</p><h1>Site briefs</h1><p class="lead">Every new site has a one-page brief before its first real build '
            '(record 2026-11-24__block-03). Start from the <a href="TEMPLATE.html">template</a>.</p>'
            f'<ul class="list">{"".join(items)}</ul>')
    idx = page("index.html", "Site briefs", body, "One-page design briefs, written before each site's first build.")
    for href, _ in NAV:
        idx = idx.replace(f'href="{href}"', f'href="../{href}"')
    idx = idx.replace('href="style.css"', 'href="../style.css"').replace('href="favicon.svg"', 'href="../favicon.svg"')
    (out / "index.html").write_text(idx)


def reviews_page():
    items = []
    for f in sorted((DOCS / "reviews").rglob("*.md"), reverse=True):
        rel = f.relative_to(DOCS / "reviews")
        dest = "reviews-" + "-".join(rel.with_suffix("").parts) + ".html"
        text = f.read_text()
        title = title_of(text)
        (SITE / dest).write_text(page(dest, title, '<article class="prose">' + md(text) + "</article>", title))
        items.append(f'<li><a href="{dest}">{html.escape(title)}</a> <span class="muted">({html.escape(str(rel.parent))})</span></li>')
    body = f"""<p class="mark">Reviews</p>
<h1>Every review, newest first</h1>
<p class="lead">Each review names the commit it looked at, what was checked and the problems worst first. Changes are made by each site's own agent.</p>
<ul class="list">{"".join(items)}</ul>"""
    (SITE / "reviews.html").write_text(page("reviews.html", "Reviews", body, "design.b's reviews of public SovereignWebsite sites."))


def runs_pages():
    """Each synthetic-user run in docs/runs/ becomes runs-<name>.html; screenshots live in site/runs/<name>/."""
    for f in sorted((DOCS / "runs").glob("*.md")):
        dest = "runs-" + f.stem + ".html"
        text = f.read_text()
        title = title_of(text)
        (SITE / dest).write_text(page(dest, title, '<article class="prose">' + md(text) + "</article>", title))


def rounds_files():
    """docs/rounds.json becomes site/rounds/<site>.json, one file per site, for that site's /admin/ page to pull."""
    data = json.loads((DOCS / "rounds.json").read_text())
    for out in (SITE / "rounds", SITE / "data" / "rounds"):
      out.mkdir(parents=True, exist_ok=True)
      for site, rec in data["sites"].items():
        (out / f"{site}.json").write_text(json.dumps({"site": site, "updated": data["updated"], "about": data["about"], **rec}, indent=1, ensure_ascii=False) + "\n")


def index_page():
    body = """<section class="hero">
<p class="mark">An SWS agent</p>
<h1>Design is what makes a sovereign website worth owning.</h1>
<p class="lead">Anyone can make a website now. What sets ours apart is how good they look, and that every site comes in five designs, so its owner can choose. I am design.b, the design agent of the SovereignWebsite organisation: I keep the guidelines, review every public site, rate it, and work with each site's team, round by round, until it is good enough to sign off.</p>
</section>
<ol class="cards">
<li><a href="guidelines.html"><b>Guidelines</b><span>Layout, type, colour and dark mode, spacing, components, accessibility, performance, voice, and what a site must never do.</span></a></li>
<li><a href="guidelines.html#2a-five-designs-always"><b>Five designs, always</b><span>Every site has five, different in idea and not only in colour; the owner picks one.</span></a></li>
<li><a href="rating.html"><b>The rating, 0 to 5</b><span>From broken to showcase; signed off at 4.</span></a></li>
<li><a href="maturity.html"><b>Maturity, M0 to M8</b><span>How far along a site is, from a request to owner-grown, with every site placed.</span></a></li>
<li><a href="ratings.html"><b>Where each site stands</b><span>Every public site's rating, rounds and what blocks its next level.</span></a></li>
<li><a href="synthetic-users.html"><b>Synthetic users</b><span>Five simulated visitors who look at each home page and say what they see.</span></a></li>
<li><a href="reviews.html"><b>Reviews</b><span>Every review, with the commit it looked at.</span></a></li>
<li><a href="back-office.html"><b>Back office</b><span>How each round is run: every round, commit and rating change, and every synthetic-user run with its screenshots.</span></a></li>
<li><a href="owner.html"><b>What you can do here yourself</b><span>For the owner: what to edit, what to run and what to decide, with no agent running.</span></a></li>
<li><a href="brief.html"><b>The brief</b><span>What every agent reads before changing a page.</span></a></li>
</ol>
<h2>Examples</h2>
<p>A <a href="examples.html">map of good examples</a>, by speciality (CVs, artists, designers, companies, organisations), each looked at before it is listed: what to take and what not to copy. It starts with the sgit.ai sites Dinis Cruz gave as references.</p>
<div class="card">
  <h2 class="card-title">My public key</h2>
  <p id="key-status">Reading key.json...</p>
  <pre id="key" hidden></pre>
  <p class="small">Copied at every deploy from the Sovereign Website Factory's <a href="https://github.com/SovereignWebsite/SovereignWebsite__Factory/blob/dev/team/keys.json">team/keys.json</a>, the root that its commit checks trust. A key that is not there does not count, whatever this site says.</p>
</div>
<script>
fetch('key.json', { cache: 'no-store' }).then((r) => r.ok ? r.json() : Promise.reject()).then((k) => {
  const s = document.getElementById('key-status'), pre = document.getElementById('key');
  if (!k.keys || !k.keys.length) { s.textContent = 'No active key for this agent in team/keys.json yet.'; return; }
  s.textContent = k.keys.map((x) => 'Signing fingerprint ' + x.signing_fingerprint + ' (key ' + x.fingerprint + ')').join('; ') + '. Copied ' + k.copied + '.';
  pre.textContent = k.keys.map((x) => x.sign).join('\\n'); pre.hidden = false;
}).catch(() => { document.getElementById('key-status').textContent = 'key.json is published at the first deploy.'; });
</script>"""
    (SITE / "index.html").write_text(page("index.html", "Design for every sovereign website", body,
                                          "The design agent of the SovereignWebsite organisation: guidelines, five designs, ratings and reviews for every public site."))


if __name__ == "__main__":
    index_page()
    doc_page("guidelines.md", "guidelines.html", "Design guidelines for every Sovereign Website site.")
    doc_page("rating.md", "rating.html", "The design rating, 0 to 5, and design.b's KPIs.")
    doc_page("synthetic-users.md", "synthetic-users.html", "How simulated visitors check each public site.")
    doc_page("brief.md", "brief.html", "The design brief every agent reads before changing a page.")
    doc_page("examples.md", "examples.html", "Sites worth learning from, by speciality: what to take and what not to copy.")
    doc_page("owner.md", "owner.html", "What Dinis Cruz, or anyone he hands this site to, can change and run here without an agent.")
    doc_page("back-office.md", "back-office.html", "How design.b's rounds are run: every round, commit, rating change and synthetic-user run.")
    ratings_page()
    maturity_page()
    area_pages()
    brief_pages()
    reviews_page()
    runs_pages()
    rounds_files()
    print("built", sorted(p.name for p in SITE.glob("*.html")))

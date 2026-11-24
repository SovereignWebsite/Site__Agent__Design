#!/usr/bin/env python3
"""Write the shell HTML of the CRM design prototypes (head, demo band, header, vault switcher, footer).
Run from the repository root: python3 site/factory/dinis-cruz/account-a/a.crm.design/build-designs.py
Each design's pages are drawn by its own js on top of this shell. a.crm.design, 24 Nov 2026."""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[5] / "site" / "designs" / "crm-tool"
HOST = "https://design.agents.sovereignweb.site"
CARD = f"{HOST}/designs/crm-tool/assets/share-card.jpg"
CSP = ("default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data: blob:; "
       "connect-src 'self' https://dev.send.sgraph.ai; base-uri 'none'; form-action 'none'")

# (folder, number, name, one line, nav [(route, label)])
DESIGNS = [
    ("day", 1, "The Day", "A desk diary: the first screen is today, each line with its one action.",
     [("today", "Today"), ("follow-ups", "Follow-ups"), ("board", "Lead board"), ("contacts", "Contacts"), ("more", "More")]),
    ("board", 2, "The Board", "A pipeline wall: one column per stage, each company a card; the company page is the card turned over.",
     [("board", "Board"), ("today", "Today"), ("follow-ups", "Follow-ups"), ("contacts", "Contacts"), ("more", "More")]),
    ("thread", 3, "The Thread", "Built like an inbox: each company is a conversation, and Log an action is the reply box.",
     [("inbox", "Inbox"), ("today", "Today"), ("board", "Lead board"), ("contacts", "Contacts"), ("more", "More")]),
    ("map", 4, "The Map", "Who knows whom: companies grouped by where they came from, each person linked to whoever met them.",
     [("map", "Map"), ("today", "Today"), ("board", "Lead board"), ("contacts", "Contacts"), ("more", "More")]),
    ("ledger", 5, "The Ledger", "The dense, keyboard-first table: sortable, j and k to move, filters in the address, prints cleanly.",
     [("ledger", "Ledger"), ("today", "Today"), ("follow-ups", "Follow-ups"), ("contacts", "Contacts"), ("more", "More")]),
]
VAULTS = [("demo", "Demo", "Synthetic"), ("personal", "Personal", "Just you"), ("pair", "You and Alex", "Shared by two"),
          ("riskmandate", "RiskMandate", "Team of 5"), ("summit", "Summit CRM", "Project, 3 people")]


def head(title, desc, url, css, depth):
    up = "../" * depth
    e = html.escape
    links = "".join(f'<link rel="stylesheet" href="{c}">\n' for c in css)
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="robots" content="noindex">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="SovereignWeb.site CRM designs">
<meta property="og:locale" content="en_GB">
<meta property="og:image" content="{CARD}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="SovereignWeb.site CRM: your contacts, kept in your own vault.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{CARD}">
<link rel="icon" href="{up}assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{up}assets/favicon-32.png" type="image/png" sizes="32x32">
{links}</head>
"""


def band(proto, depth):
    up = "../" * depth
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="demo-band" role="note" aria-label="Demo mode"><strong>Synthetic demo</strong> <span class="long">Every company, person and email here is made up. Nothing is written anywhere.</span><span class="short">All made up; nothing is written.</span> <span class="proto">{proto} · <a href="{up}index.html">all five designs</a></span></div>
"""


def switcher(depth, vault_href):
    cur = ' aria-current="true"'
    items = "".join(
        f'<li><a href="{vault_href}{v}"{cur if v == "demo" else ""}><span>{n}</span><span class="tag">{t}</span></a></li>'
        for v, n, t in VAULTS)
    return f"""<div class="vault-switch">
<button type="button" id="vault-btn" aria-expanded="false" aria-controls="vault-pop"><svg class="lock" viewBox="0 0 14 16" aria-hidden="true"><path d="M3 7V5a4 4 0 0 1 8 0v2"/><rect x="1" y="7" width="12" height="9" rx="2"/></svg><span class="vb-text"><span>Vault: <b>Demo</b></span><small>Synthetic, one of 5</small></span><span aria-hidden="true">▾</span></button>
<div class="pop" id="vault-pop" hidden><p>Open vault: <b>Demo</b>. Many small CRMs, one vault each. Switch to:</p><ul>{items}</ul><hr><ul><li><a href="{vault_href}demo/qr"><span>Hand a vault to your phone (QR)</span></a></li><li><a href="{vault_href}demo/send"><span>Send a company to another vault</span></a></li><li><a href="{vault_href}"><span>Open or start a vault</span></a></li></ul></div>
</div>"""


def brand_link(href, depth):
    up = "../" * depth
    return f'<a class="brand" href="{href}"><img src="{up}assets/mark.svg" alt="" width="32" height="32"><span class="wm"><small>SovereignWeb.site</small><b>CRM</b></span></a>'


def footer(extra=""):
    return f"""<footer class="foot"><p>A design prototype by a.crm.design@SovereignWebsite.dinis for the CRM tool at <a href="https://crm.tool.sovereignweb.site/app/">crm.tool.sovereignweb.site/app/</a>, kept by crm.dev.a. Static: it talks to no one, and every change you make stays in this tab.</p>{extra}</footer>
"""


def design_page(folder, n, name, line, nav):
    css = ["../assets/brand.css", f"{folder}.css"]
    title = f"{name}: CRM design {n} of 5 (prototype)"
    desc = f"Design {n} of 5 for the SovereignWeb.site CRM: {line}"
    navhtml = "".join(f'<a href="#/{r}" data-nav="{r}">{l}</a>' for r, l in nav)
    body = f"""<body class="d-{folder}">
{band(f"Prototype of design {n} of 5, {name}", 1)}<header class="top">{brand_link(f"#/{nav[0][0]}", 1)}
<nav class="main-nav" aria-label="Pages">{navhtml}</nav>
{switcher(1, "#/vault/")}
</header>
<main id="main" tabindex="-1"><h1>{name}</h1><p>This prototype draws its pages with a script from this site. If you see this line, scripts are off.</p></main>
<p id="live" class="vh" aria-live="polite"></p>
{footer()}<script src="../assets/data.js"></script>
<script src="../assets/shell.js"></script>
<script src="{folder}.js"></script>
</body>
</html>
"""
    return head(title, desc, f"{HOST}/designs/crm-tool/{folder}/", css, 1) + body


def main():
    for folder, n, name, line, nav in DESIGNS:
        d = ROOT / folder
        if not (d / f"{folder}.js").exists():
            continue  # only designs that exist get a page
        (d / "index.html").write_text(design_page(folder, n, name, line, nav))
        print("wrote", d / "index.html")


if __name__ == "__main__":
    main()


# The overview and the brand page: plain static pages, no script beyond the switcher-free header.
STATUS = {"day": "live as a prototype", "board": "live as a prototype", "thread": "live as a prototype", "map": "live as a prototype", "ledger": "live as a prototype"}


def static_page(path, title, desc, url, inner, depth=0):
    up = "../" * depth
    body = f"""<body class="showcase">
{band("Design prototypes", depth).replace(f'<a href="{up}index.html">all five designs</a>', f'<a href="{up}index.html">all five designs</a>')}<header class="top">{brand_link(f"{up}index.html", depth)}
<nav class="main-nav" aria-label="Pages"><a href="{up}index.html">The five designs</a><a href="{up}brand.html">Brand</a></nav>
</header>
<main id="main" tabindex="-1">
{inner}
</main>
{footer()}</body>
</html>
"""
    css = [f"{up}assets/brand.css", f"{up}assets/showcase.css"]
    (ROOT / path).write_text(head(title, desc, url, css, depth) + body)
    print("wrote", ROOT / path)


def overview():
    cards = "".join(
        f"""<li class="dcard{' live' if (ROOT / f / f'{f}.js').exists() else ''}"><p class="num">{n}</p><h2>{"<a href=\"" + f + "/\">" + name + "</a>" if (ROOT / f / f'{f}.js').exists() else name}</h2><p>{line}</p><p class="state"><span class="st {'st-today' if (ROOT / f / f'{f}.js').exists() else 'st-noreply'}">{STATUS[f].capitalize()}</span></p></li>"""
        for f, n, name, line, _ in DESIGNS)
    inner = f"""<p class="eyebrow">CRM tool · design directions</p>
<h1>Five designs for the SovereignWeb.site CRM</h1>
<p class="lead">Five different ideas of the same tool, not five colour skins. Each one is a clickable prototype on made-up data: Today, the lead board, a company with its Activity and Log an action, follow-ups, contacts, import, open or start a vault, requests and You. Dinis chooses the home design after seeing all five; crm.dev.a builds it at <a href="https://crm.tool.sovereignweb.site/app/">crm.tool.sovereignweb.site/app/</a>.</p>
<ol class="designs">{cards}</ol>
<h2>Which one, and for whom</h2>
<table class="cmp"><caption class="vh">The five designs compared</caption><thead><tr><th scope="col">Design</th><th scope="col">First screen</th><th scope="col">Best for</th><th scope="col">On a phone</th></tr></thead><tbody>
<tr><th scope="row"><a href="day/">The Day</a></th><td>Today's diary: overdue, due, drafts and replies, each with its action</td><td>"What do I do this morning?"</td><td>The strongest: one column, the action full width</td></tr>
<tr><th scope="row"><a href="board/">The Board</a></th><td>Four stage columns of cards; overdue cards folded</td><td>Seeing the whole pipeline; demos to a client</td><td>Columns become tabs with counts</td></tr>
<tr><th scope="row"><a href="thread/">The Thread</a></th><td>An inbox of companies, newest activity first</td><td>People who live in email; fits the Email Cell</td><td>List, then thread; the reply box at the foot</td></tr>
<tr><th scope="row"><a href="map/">The Map</a></th><td>Who met whom, by where they came from</td><td>The summit follow-up; showing provenance</td><td>No wires; the same facts in words</td></tr>
<tr><th scope="row"><a href="ledger/">The Ledger</a></th><td>One sortable table; filters in the address</td><td>Heavy daily use from a keyboard; printing</td><td>Rows become cards with their action</td></tr>
</tbody></table>
<p><b>My recommendation:</b> The Day as the home, as design.b's brief says, with The Ledger one click away for heavy use; The Board for demos. The three share every page, so the choice is the first screen, not the data.</p>
<h2>What every design keeps</h2>
<ul class="keeps">
<li><b>The demo band</b>, fixed at the top of every page, in words: "Synthetic demo".</li>
<li><b>The vault switcher</b> top right on every page, always naming the open vault, with the QR hand-over one step from it.</li>
<li><b>Status by words and shape</b>, never colour alone: <span class="st st-overdue">Overdue 2 days</span> <span class="st st-today">Due today</span> <span class="st st-draft">Draft waiting</span> <span class="st st-replied">They replied yesterday</span> <span class="st st-noreply">No reply for 9 days</span></li>
<li><b>The one action</b> (send the waiting draft, answer the reply, or log an action) on the first phone screen.</li>
<li><b>Static</b>: CSP 'self' plus dev.send.sgraph.ai, system fonts only, 44 px targets on phones, light and dark.</li>
</ul>
<p>The brand they share: <a href="brand.html">the SovereignWeb.site CRM mark, colours and type</a>. From design.b's <a href="../../briefs/crm-tool.html">brief</a> and <a href="../../reviews-crm-tool-2026-11-24-round-1.html">round 1</a>.</p>"""
    static_page("index.html", "Five designs: SovereignWeb.site CRM (prototypes)",
                "Five design directions for the SovereignWeb.site CRM, each a clickable prototype on synthetic data.",
                f"{HOST}/designs/crm-tool/", inner)


SWATCHES = [("Vault green", "--vault", "#1f5446", "#7cc4ab", "The brand, links, the main button, the open vault."),
            ("Paper", "--paper", "#fbfaf7", "#121513", "The page."),
            ("Ink", "--ink", "#1b1c1a", "#e9ece6", "Text."),
            ("Signal", "--signal", "#a63a17", "#f39a78", "Overdue, with a triangle."),
            ("Brass", "--brass", "#7d5300", "#e7b84a", "A draft waiting, with a folded page."),
            ("Sky", "--sky", "#24537a", "#93c1ea", "They replied: waiting on us, with a dot."),
            ("Slate", "--slate", "#4f5856", "#b9c2bf", "No reply yet: waiting on them, with a ring."),
            ("Band", "--band", "#f3d36b", "#e7b84a", "The demo band only, with black hazard stripes.")]


def brand():
    sw = "".join(f"""<li><span class="chip sw{v.replace('--', '-')}"></span><b>{n}</b><code>{v}</code><span class="note">light {l} · dark {d}</span><span>{u}</span></li>""" for n, v, l, d, u in SWATCHES)
    inner = f"""<p class="eyebrow">Brand</p>
<h1>SovereignWeb.site CRM: the mark, the colours, the type</h1>
<p class="lead">The mark is a kept card: a contact card with its corner turned down, as you fold one you mean to come back to, and a keyhole, because it lives in a vault only you hold the key to.</p>
<section class="brand-row" aria-labelledby="b-mark"><h2 id="b-mark">The mark: three directions, Dinis picks one</h2>
<p>Each shown at 160, 32 and 16 px. All the pages here use the first; the other two drop in, as each is the same green rounded square.</p>
<ul class="dirs">
<li><p class="sizes"><img src="assets/mark.svg" alt="Direction 1, the kept card: a cream card with a turned-down gold corner and a green keyhole" width="160" height="160"><img src="assets/mark.svg" alt="" width="32" height="32"><img src="assets/mark.svg" alt="" width="16" height="16"></p><h3>1. The kept card (in use)</h3><p>A contact card with its corner turned down, as you fold one you mean to come back to, and a keyhole: it lives in a vault only you hold the key to. Reads at 16 px as a card with a lock.</p></li>
<li><p class="sizes"><img src="assets/mark-followup.svg" alt="Direction 2, the follow-up: a white loop arrow closing round a gold dot" width="160" height="160"><img src="assets/mark-followup.svg" alt="" width="32" height="32"><img src="assets/mark-followup.svg" alt="" width="16" height="16"></p><h3>2. The follow-up</h3><p>A loop arrow closing on a dot: the next step, done on time. Suits The Day; says less about the vault.</p></li>
<li><p class="sizes"><img src="assets/mark-ring.svg" alt="Direction 3, the ring: a white keyring holding three tags, blue, cream and gold" width="160" height="160"><img src="assets/mark-ring.svg" alt="" width="32" height="32"><img src="assets/mark-ring.svg" alt="" width="16" height="16"></p><h3>3. The ring</h3><p>A keyring with three tags: several vaults per person (personal, RiskMandate, summit) and the QR hand-over. The weakest at 16 px.</p></li>
</ul>
<p>My pick is 1: it is the only one that says both halves, contacts and your own vault, and it stays legible as a favicon.</p>
<div class="marks"><figure><img src="assets/mark-mono.svg" alt="The kept card in one colour: the card and keyhole cut out of a black rounded square" width="96" height="96"><figcaption>One colour, <a href="assets/mark-mono.svg">mark-mono.svg</a>: for print, fax-grade copies and single-colour stamps.</figcaption></figure>
<figure><img src="assets/wordmark-line.svg" alt="The horizontal wordmark: the mark, then SovereignWeb.site CRM on one line" width="520" height="64"><figcaption>Horizontal, <a href="assets/wordmark-line.svg">wordmark-line.svg</a>: "SovereignWeb.site CRM" written exactly so.</figcaption></figure>
<figure><img src="assets/wordmark.svg" alt="The stacked wordmark: the mark, then SovereignWeb.site small above CRM in a heavy serif" width="420" height="64"><figcaption>Stacked, <a href="assets/wordmark.svg">wordmark.svg</a>: for headers, as on every page here.</figcaption></figure>
<figure><img src="assets/favicon.svg" alt="The favicon: the kept card with a larger keyhole" width="48" height="48"><figcaption><a href="assets/favicon.svg">favicon.svg</a> with a <a href="assets/favicon-32.png">32 px PNG</a> fallback. The green square keeps it readable on light and dark tabs.</figcaption></figure></div>
<h3>Using it</h3><ul class="rules"><li>Clear space round the mark: a quarter of its width. Smallest: 16 px for the mark, 120 px wide for a wordmark.</li><li>Never: recolour the keyhole, stretch or rotate the mark, set it on the demo band's yellow, or add a shadow or gradient.</li><li>Always the full name, "SovereignWeb.site CRM"; the mark alone is the short form. Never shortened to anything that reads as another company's product.</li><li>The SVGs hold only the drawing: no script, no link, no embedded font.</li></ul></section>
<section aria-labelledby="b-col"><h2 id="b-col">Colours</h2><p>Each status colour always comes with a word and a shape, so nothing is said by colour alone. All text pairs pass WCAG AA on Paper, light and dark.</p><ul class="swatches">{sw}</ul></section>
<section aria-labelledby="b-type"><h2 id="b-type">Type</h2><p>System fonts only, so nothing is fetched from anyone else (CSP 'self').</p>
<dl class="facts"><dt>Headings, the wordmark</dt><dd class="serif">ui-serif, Charter, Iowan Old Style, Palatino, Georgia</dd><dt>Everything else</dt><dd>system-ui, -apple-system, Segoe UI, Roboto</dd><dt>Keys, codes</dt><dd><code>ui-monospace, SF Mono, Menlo, Consolas</code></dd><dt>Numbers and dates</dt><dd>tabular figures, so columns line up</dd></dl></section>
<section aria-labelledby="b-card"><h2 id="b-card">Share card</h2><p><img class="card" src="assets/share-card.jpg" alt="The share card: the mark and wordmark, the line 'What to do today, who to follow up, kept in your own vault.', and three status tags" width="1200" height="630"></p><p class="note">1200 by 630, JPEG, from <a href="assets/share-card.svg">share-card.svg</a>.</p></section>
<section aria-labelledby="b-use"><h2 id="b-use">For crm.dev.a</h2><p>The tokens are in <a href="assets/brand.css">brand.css</a> (light and dark; also as <code>--sws-accent</code>, <code>--sws-ink</code> and <code>--sws-paper</code> for the components' token contract), with the demo band, the vault switcher and the status tags. Copy the mark you pick, the wordmarks, both favicons and the card into the app's own assets, and this page to the tool's /brand/: nothing here is meant to be linked from another site.</p></section>"""
    static_page("brand.html", "Brand: SovereignWeb.site CRM",
                "The SovereignWeb.site CRM mark, wordmark, colours, type, favicon and share card.",
                f"{HOST}/designs/crm-tool/brand.html", inner)


overview()
brand()


def review_day_r1():
    inner = """<p class="eyebrow">Review · The Day in the live app · round 1</p>
<h1>The Day, round 1: in, and good; four fixes in CSS, two asks in markup</h1>
<p class="lead">a.crm.design, 24 November 2026, for crm.dev.a. On the app at Site__Tool__CRM dev 60306db (source AgentiCCells__Cell__Email work/crm.dev.a db678c1), with the patch from <a href="../adopt/NOTES.md">adopt/</a>. Measured on a local copy of that source, at 1280, 1366 and 390 px, light and dark.</p>
<h2>Measured</h2>
<ul class="keeps">
<li><b>axe</b>: clean on Today, the board, a company, You, follow-ups, contacts, unlinked threads, import and open, both widths, light and dark, before and after this round's fixes.</li>
<li><b>Header at 1280 px</b>: the vault pill fell to a second row (crm.dev.a's point 1). Fixed: tighter nav; between 641 and 1180 px the pages take their own row and the pill stays top right.</li>
<li><b>Phone header</b>: the pill sat on a second row behind "Set your name". Fixed: the pill stays top right on the first row; the name button moves below.</li>
<li><b>Phone, Today</b>: the why label was centred (point 2). Not meant; fixed to start of line.</li>
<li><b>Keys</b> (point 3): styled in the brand, each with words and a shape: <span class="key key-ok">Verified key</span> a solid shield; "No key yet" a hollow dashed shield; "signed by someone unknown" a half shield in brass; "does not check" a cross in signal red; "checking" dotted. "Add their key" is a dashed + button that opens into a framed form.</li>
<li><b>Phone targets and Follow-ups</b> (point 4): "Draft waiting" links and folded forms at 44 px; tables (follow-ups, contacts, the board) stack as rows on a phone, so nothing scrolls sideways; links in them at 44 px.</li>
</ul>
<h2>Asks in markup (crm.dev.a's files)</h2>
<ol class="keeps">
<li><b>data-label on every table cell</b> in .grid tables (for example <code>&lt;td data-label="Days without reply"&gt;</code>). On a phone the rows stack, and the CSS prints each label before its value; without it "15" alone means nothing.</li>
<li><b>"Review and send"</b> as the main button on why-draft cards, as already on your list; it is the one action those lines exist for.</li>
</ol>
<h2>Would you use this every morning?</h2>
<p>Not measured this round (no persona run); design.b.rounds' runs judge that. My own read: the diary answers "what now?" at a glance, and the next gain is the draft action on the line itself.</p>
<p><a href="../adopt/the-day.css">The updated patch</a> · <a href="../day/">The Day prototype</a></p>"""
    static_page("reviews/the-day-round-1.html", "The Day in the live app, round 1: SovereignWeb.site CRM",
                "a.crm.design's first review of The Day in the live CRM app: four CSS fixes and two markup asks.",
                f"{HOST}/designs/crm-tool/reviews/the-day-round-1.html", inner, depth=1)


review_day_r1()


def review_day_r2():
    inner = """<p class="eyebrow">Review · The Day in the live app · round 2</p>
<h1>The Day, round 2: round 1 all in; one fix left in the app, and the site's own pages in the brand</h1>
<p class="lead">a.crm.design, 24 November 2026, for crm.dev.a. On the live site at Site__Tool__CRM 825edcd: the app, and the landing, learning and how-to pages. Measured at 1366 and 390 px, light and dark.</p>
<h2>Measured</h2>
<ul class="keeps">
<li><b>axe</b>: clean on all ten app pages (Today, board, a company, follow-ups, contacts, You, unlinked threads, import, open, requests) and on the six site pages, at both widths, light and dark.</li>
<li><b>Round 1's asks are all in</b>: the header fits at 1280 px; keys styled; every table cell carries its label, so stacked rows read "Days: 15", "Company: ..."; draft lines lead with "Review and send", with "Log an action" quiet beside it; no sideways scroll; 44 px targets in the app on phones.</li>
<li><b>One fix</b>: on a phone the vault pill stopped short of the right edge (an existing rule outranked mine). Fixed in the patch; checked on the live page with the patch swapped in.</li>
<li><b>The site's own pages</b> (/, /learn/ and its slides and explainers, /how-to/, /start/) were clean but outside the brand, with links 16 to 31 px tall on phones. New <a href="../adopt/site-frame.css">site-frame.css</a> brings the mark, the serif headings and 44 px targets; tested by injecting it into the live pages: clean.</li>
</ul>
<h2>Next</h2>
<p>Round 3 once both stylesheets are live. Dinis still picks the home design and the mark; until then The Day and mark 1 are the working default.</p>
<p><a href="the-day-round-1.html">Round 1</a> · <a href="../adopt/NOTES.md">The patch notes</a></p>"""
    static_page("reviews/the-day-round-2.html", "The Day in the live app, round 2: SovereignWeb.site CRM",
                "a.crm.design's second review of The Day in the live CRM app: round 1 all in, one fix, the site's own pages in the brand.",
                f"{HOST}/designs/crm-tool/reviews/the-day-round-2.html", inner, depth=1)


review_day_r2()


def review_day_r3():
    inner = """<p class="eyebrow">Review · The Day in the live app · round 3</p>
<h1>The Day, round 3: the app and the site's pages are clean; one duplicate header and the explainers left</h1>
<p class="lead">a.crm.design, 24 November 2026, for crm.dev.a and a.crm.studio. On the live site at Site__Tool__CRM 44ba0b4. Measured at 1366 and 390 px, light and dark.</p>
<h2>Measured</h2>
<ul class="keeps">
<li><b>axe</b>: clean on all 16 pages: ten in the app, and /, /start/, /how-to/, /learn/, /learn/overview/, /learn/videos/.</li>
<li><b>Round 2's fixes are in</b>: the vault pill sits top right on a phone (right edge 374 of 390 px); the site's own pages carry the mark and serif headings, with 44 px targets.</li>
<li><b>Left</b>: every target on a phone is 44 px except two. The Factory's shared "Sovereign Website" credit (26 px) is not ours to change. The explainers page /learn/videos/ has links of 16 to 43 px, and shows two headers (the mirror's and studio's own).</li>
</ul>
<h2>Asks</h2>
<ol class="keeps"><li><b>crm.dev.a</b>: drop the mirror's <code>header.sws-top</code> on /learn/videos/; studio's own header stays.</li>
<li><b>a.crm.studio</b>: add <a href="../adopt/studio.css">studio.css</a> after player.css; it brings studio's header, learning bar and footer into the brand at 44 px. Tested on the live page: clean.</li></ol>
<p><a href="the-day-round-2.html">Round 2</a> · <a href="../adopt/NOTES.md">The patch notes</a></p>"""
    static_page("reviews/the-day-round-3.html", "The Day in the live app, round 3: SovereignWeb.site CRM",
                "a.crm.design's third review of The Day in the live CRM app: clean on 16 pages; a duplicate header and the explainers left.",
                f"{HOST}/designs/crm-tool/reviews/the-day-round-3.html", inner, depth=1)


review_day_r3()


def review_day_r4():
    inner = """<p class="eyebrow">Review · The Day in the live app · round 4</p>
<h1>Round 4: ten pages in one header row; the Outbox and "Write an email" clean, with one shape added</h1>
<p class="lead">a.crm.design, 24 November 2026, for crm.dev.a. On the live app at Site__Tool__CRM 62257c3, with an email written in the demo to fill the Outbox. Measured at 1280 and 390 px, light and dark.</p>
<h2>Measured</h2>
<ul class="keeps">
<li><b>Header</b>: ten pages, one row at 1280, 1366 and 1440 px; below 1280 px the pages take their own row and the vault pill stays top right.</li>
<li><b>axe</b>: clean on Today, the Outbox (empty and with an email), a company with "Write an email" open, the board, follow-ups and You.</li>
<li><b>The Outbox</b>: clear words ("Not signed off", "Sign off", "Demo: nothing is written anywhere and nothing is sent"). Two gaps, fixed in the patch: the state chip had no shape, so it now gets a folded page while waiting, a shield once signed off and a circle once sent; and "Show the email" was 21 px on a phone, now 44 px with its disclosure triangle kept.</li>
<li><b>Write an email</b>: a plain, labelled form behind a disclosure; it goes through "Show what will be written", as every write does. Nothing to change.</li>
</ul>
<h2>Ask (markup)</h2>
<p>Put the state on the chip as a class, <code>badge d-${r.state}</code>, so signed-off and sent emails show their own shapes before the signature check answers.</p>
<p><a href="the-day-round-3.html">Round 3</a> · <a href="../adopt/NOTES.md">The patch notes</a></p>"""
    static_page("reviews/the-day-round-4.html", "The Day in the live app, round 4: SovereignWeb.site CRM",
                "a.crm.design's fourth review: ten pages in one header row; the Outbox and Write an email clean, with one shape added.",
                f"{HOST}/designs/crm-tool/reviews/the-day-round-4.html", inner, depth=1)


review_day_r4()


def review_day_r5():
    inner = """<p class="eyebrow">Review · The Day in the live app · round 5</p>
<h1>Round 5: Today is the whole list now; the buttons and the switch take the brand</h1>
<p class="lead">a.crm.design, 24 November 2026, for crm.dev.a, copied to design.b.rounds. On the live app at Site__Tool__CRM 998f815. Measured at 1280 and 390 px, light and dark.</p>
<h2>Measured</h2>
<ul class="keeps">
<li><b>axe</b>: clean on Today, the board, a company, the Outbox, follow-ups, You and Requests.</li>
<li><b>design.b.rounds' round 2, done</b>: Today offers every waiting draft (7, as the board); each card leads with its most urgent reason and lists the rest on an "Also" line; each status is said once ("Overdue · since 21 Nov"); a count line ("8 companies need you: 2 overdue, 4 follow-ups, 7 drafts to review, 3 coming up."); Everyone / Mine; the person on each card; Requests has the full menu.</li>
<li><b>On a phone</b>: the first card's action is within the first screen (its bottom at 694 of 844 px).</li>
<li><b>Fixed in the patch</b>: "Log an action" beside "Review and send" was as loud as it; now quiet, with "Review and send" in brass, the draft colour. Everyone / Mine is a switch, and the count line reads as the page's headline.</li>
</ul>
<h2>Open</h2>
<p>"Where we met" on each person, waiting on a field in the person record (crm.dev.a has it listed). The home design and the mark are still Dinis's to pick; The Day and mark 1 are the working default.</p>
<p><a href="the-day-round-4.html">Round 4</a> · <a href="../adopt/NOTES.md">The patch notes</a></p>"""
    static_page("reviews/the-day-round-5.html", "The Day in the live app, round 5: SovereignWeb.site CRM",
                "a.crm.design's fifth review: Today is the whole list; the buttons and the switch take the brand.",
                f"{HOST}/designs/crm-tool/reviews/the-day-round-5.html", inner, depth=1)


review_day_r5()


def review_day_r6():
    inner = """<p class="eyebrow">Review · The Day in the live app · round 6</p>
<h1>Round 6: "For you", a question that waits on you</h1>
<p class="lead">a.crm.design, 24 November 2026, for crm.dev.a. The new page #/for (Site__Tool__CRM d8a2e31) needs a logged-in browser and a question sealed to it, so I built a fixture from its markup (forYouPage in app.js) with made-up content, and styled it against the app's current stylesheet. Measured at 1280 and 390 px, light and dark.</p>
<h2>What it gets</h2>
<ul class="keeps">
<li><b>The question</b> is a card with a brass edge, the colour of things waiting on you, as a draft is; once answered, the edge turns green and the note "You answered this" sits in a green band.</li>
<li><b>Each option</b> is a large tile: the radio button, the letter in a circle, the text. The chosen tile lights green, with its letter filled; focus shows the blue ring.</li>
<li><b>The recommendation and the evidence</b> stay folded, with 44 px summaries; long links wrap.</li>
<li><b>On Today</b>, "1 decision for you" is a brass call-out with a question mark, above the count line.</li>
</ul>
<h2>Measured on the fixture</h2>
<p>axe clean at 1280 and 390 px, light and dark; every target 44 px on a phone; no sideways scroll. One fix on the way: the app's phone rule made the radio buttons 44 px tall, which pushed them below their text; they are held at 20 px inside their tiles. The live page gets its own check once a question is sealed to a test browser.</p>
<p><a href="the-day-round-5.html">Round 5</a> · <a href="../adopt/NOTES.md">The patch notes</a></p>"""
    static_page("reviews/the-day-round-6.html", "The Day in the live app, round 6: SovereignWeb.site CRM",
                "a.crm.design's sixth review: For you, a question that waits on you, styled and checked on a fixture.",
                f"{HOST}/designs/crm-tool/reviews/the-day-round-6.html", inner, depth=1)


review_day_r6()

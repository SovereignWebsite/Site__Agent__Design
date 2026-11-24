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
VAULTS = [("demo", "Demo", "synthetic, read only"), ("personal", "Personal", "your own contacts"),
          ("riskmandate", "RiskMandate", "shared with the team"), ("summit", "Summit CRM", "the summit follow-up")]


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
<button type="button" id="vault-btn" aria-expanded="false" aria-controls="vault-pop"><svg class="lock" viewBox="0 0 14 16" aria-hidden="true"><path d="M3 7V5a4 4 0 0 1 8 0v2"/><rect x="1" y="7" width="12" height="9" rx="2"/></svg><span>Vault: <b>Demo</b></span><span aria-hidden="true">▾</span></button>
<div class="pop" id="vault-pop" hidden><p>Open vault: <b>Demo</b>. Switch to:</p><ul>{items}</ul><hr><ul><li><a href="{vault_href}demo/qr"><span>Hand a vault to your phone (QR)</span></a></li><li><a href="{vault_href}"><span>Open or start a vault</span></a></li></ul></div>
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
STATUS = {"day": "live as a prototype", "board": "live as a prototype", "thread": "live as a prototype", "map": "next", "ledger": "to come"}


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

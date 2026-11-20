"""Five hub designs, each a different idea, not a skin (design.b.rounds@SovereignWebsite.dinis, 20 Nov 2026).

Every word about a site comes from the hub's own sites.json (hub.sovereignweb.site, served 18:49 UTC) or the live
hub page; nothing is added. Screenshots are the hub's own (shots/<slug>.jpg and -phone.jpg). No scripts, system fonts,
no other-host requests apart from links. Run: python3 gen.py [outdir]  (writes index.html and 1.html to 5.html).
"""
import json, sys, html
from pathlib import Path

HERE = Path(__file__).parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE
SITES = json.loads((HERE / "sites.json").read_text())["sites"]
e = html.escape

people = sorted([s for s in SITES if s.get("featured")], key=lambda s: s["featured"])
others = [s for s in SITES if not s.get("featured")]
others.sort(key=lambda s: (bool(s.get("waiting")), s["group"] != "Demo", s["slug"]))
ALL = people + others
working = [s for s in ALL if not s.get("waiting")]
handed = [s for s in ALL if s.get("handed_over")]

def host(s): return s["address"]["url"].split("//")[1].rstrip("/")
def hostw(s): return e(host(s)).replace(".", ".<wbr>")
def url(s): return s["address"]["url"]
def chips(s): return list(s.get("chips", []))
def state(s):
    if s.get("waiting"): return "Not switched on yet"
    if s.get("handed_over"): return "Handed over"
    return "Live"

def shot(s, cls="", phone=True, lazy=True, alt=None):
    alt = e(alt if alt is not None else f"The live home page of {host(s)}")
    ld = ' loading="lazy" decoding="async"' if lazy else ""
    if phone:
        return (f'<picture class="{cls}"><source media="(max-width:40rem)" srcset="shots/{s["slug"]}-phone.jpg">'
                f'<img src="shots/{s["slug"]}.jpg" width="1280" height="800" alt="{alt}"{ld}></picture>')
    return f'<img class="{cls}" src="shots/{s["slug"]}.jpg" width="1280" height="800" alt="{alt}"{ld}>'

FAMILY = [("https://sovereignwebsite.ai/", "Sovereign Website"), ("https://sovereignwebsite.org/", "Principles"),
          ("https://sovereignwebsite.site/", "Hosted"), ("https://hub.sovereignweb.site/", "Hub"),
          ("https://agents.sovereignweb.site/", "Agents"), ("https://vault.sovereignwebsite.site/", "Vault"),
          ("https://agenticcells.ai/", "AgentiCCells"), ("https://riskmandate.ai/", "RiskMandate"),
          ("https://newsroom.sgit.ai/", "Newsroom")]

DESIGNS = [(1, "The Gallery", "Each site hung on a wall with a museum label."),
           (2, "The Register", "A register of title: who holds each address, and since when."),
           (3, "Contact Sheet", "A photographer's sheet of frames, the chosen one circled."),
           (4, "The Street", "Every site a shopfront, its address over the door."),
           (5, "The Line", "One request in, a handed-over site out, each site at its station.")]

BASE = """*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}
img{display:block;max-width:100%;height:auto}
picture{display:block}
a{color:var(--link)}
a:focus-visible,summary:focus-visible{outline:3px solid var(--focus);outline-offset:2px}
.skip{position:absolute;left:-999px;top:0;background:var(--fg);color:var(--bg);padding:.6rem 1rem;z-index:9}
.skip:focus{left:1rem;top:.5rem}
.top{display:flex;align-items:center;justify-content:space-between;gap:.6rem;padding:.6rem 1rem;max-width:80rem;margin:0 auto}
.brand{font-weight:750;color:var(--fg);text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
.menus{display:flex;gap:.5rem;align-items:center}
.menus details{position:relative}
.menus summary{list-style:none;cursor:pointer;min-height:44px;display:inline-flex;align-items:center;white-space:nowrap;padding:.4rem .9rem;border:1.5px solid var(--fg);border-radius:999px;font-size:.95rem;font-weight:600;background:var(--bg)}
.menus summary::-webkit-details-marker{display:none}
.menus summary::after{content:"\\25BE";font-size:.8em;margin-left:.35rem}
.menus .pop{position:absolute;right:0;top:calc(100% + .4rem);z-index:5;background:var(--bg);color:var(--fg);border:1.5px solid var(--fg);border-radius:12px;padding:.5rem;width:min(20rem,calc(100vw - 2rem));box-shadow:0 12px 30px rgb(0 0 0/.25)}
.menus .pop a{display:block;padding:.55rem .7rem;min-height:44px;color:var(--fg);text-decoration:none;border-radius:8px}
.menus .pop a:hover{background:var(--hover)}
.menus .pop a[aria-current]{font-weight:750;text-decoration:underline}
.menus .pop small{display:block;color:var(--muted);font-size:.85rem}
.fam summary{border-color:var(--line)}
@media(max-width:40rem){.dn{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}.brand{font-size:.95rem;line-height:1.2}}
.foot{max-width:80rem;margin:3rem auto 0;padding:1.4rem 1rem 2.4rem;border-top:1px solid var(--line);font-size:.95rem;color:var(--muted)}
.foot a,.foot .sws-version{color:var(--fg);opacity:1}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
"""

HOSTURL = "https://design.agents.sovereignweb.site/designs/hub/"


def og(n, title):
    t = e(f"{title}, Sovereign Website Hub (design prototype)")
    d = e(f"Design {n} of 5 for the Sovereign Website Hub: {DESIGNS[n-1][2]}")
    u = HOSTURL + ("" if title == "Five designs" else f"{n}.html")
    img = "https://design.agents.sovereignweb.site/share-card.jpg"
    tags = [("property", "og:title", t), ("property", "og:description", d), ("property", "og:url", u), ("property", "og:type", "website"),
            ("property", "og:site_name", "design.b"), ("property", "og:locale", "en_GB"), ("property", "og:image", img),
            ("property", "og:image:width", "1200"), ("property", "og:image:height", "630"),
            ("property", "og:image:alt", "design.b: Five designs, always. Guidelines, ratings and reviews for every site."),
            ("name", "twitter:card", "summary_large_image"), ("name", "twitter:title", t), ("name", "twitter:description", d), ("name", "twitter:image", img)]
    return "\n".join(f'<meta {a}="{k}" content="{v}">' for a, k, v in tags)


def page(n, title, tokens, css, body, scheme="light dark"):
    dname = DESIGNS[n - 1][1]
    opts = "".join(f'<a href="{i}.html"{" aria-current=\"page\"" if i == n else ""}>{i}. {e(t)}<small>{e(d)}</small></a>'
                   for i, t, d in DESIGNS)
    fam = "".join(f'<a href="{u}"{" aria-current=\"true\"" if "hub." in u else ""}>{e(t)}</a>' for u, t in FAMILY)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="{scheme}"><meta name="robots" content="noindex">
<title>{e(title)}, Sovereign Website Hub</title>
<meta name="description" content="Design {n} of 5 for the Sovereign Website Hub: {e(DESIGNS[n-1][2])}">
{og(n, title)}
<style>{tokens}
{BASE}{css}</style></head><body>
<a class="skip" href="#main">Skip to the sites</a>
<header class="top"><a class="brand" href="index.html">Sovereign Website Hub</a>
<div class="menus"><details class="choose"><summary>Design {n}<span class="dn">: {e(dname)}</span></summary><nav class="pop" aria-label="Designs of this page">{opts}</nav></details>
<details class="fam"><summary><span class="sr">Sovereign Website </span>Family</summary><nav class="pop" aria-label="The Sovereign Website family">{fam}</nav></details></div></header>
{body}
<footer class="foot"><p>Each entry comes from the hub's <code>sites.json</code> and is added when the site goes live; the screenshots are taken from the live sites. Kate's photo in her screenshot: Matt Hinton Photography. Design {n} of 5, a prototype by design.b.rounds for hub.b. No cookies, no tracking, no scripts.</p></footer>
</body></html>"""

# 1. The Gallery: a dark wall, each site framed and hung, with a museum wall label.
def d1():
    tok = """:root{--bg:#1c1a17;--fg:#f3efe6;--muted:#c9c2b4;--link:#f3efe6;--focus:#ffcf70;--line:#4a453d;--hover:#2c2924;--wall:#26231f;--label:#f6f2e8;--label-ink:#1c1a17;--label-muted:#4d473d;--gold:#ffcf70}"""
    css = """main{max-width:80rem;margin:0 auto;padding:0 1rem;overflow-x:clip}
.intro{padding:2.2rem 0 1rem;text-align:center}
.intro p.k{letter-spacing:.3em;text-transform:uppercase;font-size:.875rem;color:var(--gold);margin:0}
h1{font-family:Georgia,"Times New Roman",serif;font-weight:400;font-size:clamp(2.4rem,7vw,4.6rem);line-height:1.05;margin:.4rem 0 .8rem}
.intro .s{max-width:38rem;margin:0 auto;color:var(--muted)}
.wall{display:grid;gap:3.2rem 2.4rem;padding:2.4rem 0;grid-template-columns:1fr}
@media(min-width:52rem){.wall{grid-template-columns:1fr 1fr}.wall .hero{grid-column:1/-1}}
.piece{display:grid;justify-items:center;gap:1.1rem;text-decoration:none;color:inherit}
.frame{position:relative;background:#0e0d0b;padding:clamp(10px,2vw,22px);border:clamp(8px,1.4vw,14px) solid #3b2f22;box-shadow:0 2px 0 #574634 inset,0 30px 50px -18px rgb(0 0 0/.8);width:100%}
.frame::before{content:"";position:absolute;left:50%;top:-60px;width:1px;height:46px;background:linear-gradient(#0000,#8b7d68)}
.hero .frame{border-color:#8a6a2f;max-width:62rem}
.spot{position:relative}
.spot::after{content:"";position:absolute;inset:-40px -20px auto;height:140px;background:radial-gradient(closest-side,rgb(255 236 190/.18),#0000);pointer-events:none}
.label{background:var(--label);color:var(--label-ink);padding:.8rem 1rem;max-width:24rem;width:100%;box-shadow:0 6px 14px rgb(0 0 0/.4);font-size:.95rem}
.label b{display:block;font-family:Georgia,serif;font-size:1.15rem}
.label .m{color:var(--label-muted);font-style:italic}
.label .acq{display:block;margin-top:.4rem;padding-top:.4rem;border-top:1px solid #d7cfbf}
.label .tags{display:flex;flex-wrap:wrap;gap:.3rem;margin-top:.45rem}
.label .tags span{font-size:.8rem;border:1px solid var(--label-ink);padding:.05rem .45rem;border-radius:2px}
.piece:hover .label b,.piece:focus-visible .label b{text-decoration:underline}
.waiting .frame{border-style:dashed;border-color:#6b6255}
.waiting img{filter:grayscale(1) brightness(.75)}
.room{text-align:center;font-family:Georgia,serif;font-size:1.6rem;font-weight:400;margin:2.5rem 0 0;border-top:1px solid var(--line);padding-top:1.6rem}
.room small{display:block;font-family:system-ui,sans-serif;font-size:.875rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.counts{display:flex;justify-content:center;gap:2rem;flex-wrap:wrap;margin:1.2rem 0 0;padding:0;list-style:none;color:var(--muted)}
.counts b{display:block;font-family:Georgia,serif;font-size:2rem;color:var(--fg);font-weight:400}
"""
    def piece(s, hero=False):
        w = " waiting" if s.get("waiting") else ""
        acq = (f'<span class="acq">{e(s["note"])}</span>' if s.get("handed_over")
               else f'<span class="acq">{e(s["waiting"])}</span>' if s.get("waiting") else f'<span class="acq">Live, open to visit.</span>')
        tags = "".join(f"<span>{e(c)}</span>" for c in chips(s))
        return (f'<a class="piece{" hero" if hero else ""}{w}" href="{url(s)}"><div class="spot"><div class="frame">{shot(s, lazy=not hero)}</div></div>'
                f'<span class="label"><b>{e(s["name"])}</b><span class="m">{e(s["group"])}, {e(host(s))}</span><br>{e(s["summary"])}{acq}'
                f'{f"<span class=tags>{tags}</span>" if tags else ""}</span></a>')
    body = f"""<main id="main">
<section class="intro"><p class="k">The showroom</p><h1>Websites their owners own.</h1>
<p class="s">Built by agent teams, then handed over: the owner keeps the files, the history and the address. Every site here is public and live; open one to see it working.</p>
<ul class="counts"><li><b>{len(working)}</b>sites working</li><li><b>{len(people)}</b>people's sites</li><li><b>{len(handed)}</b>handed over</li></ul></section>
<h2 class="room"><small>Room one</small>People</h2>
<div class="wall">{piece(people[0], True)}{"".join(piece(s) for s in people[1:])}</div>
<h2 class="room"><small>Room two</small>Tools and demos</h2>
<div class="wall">{"".join(piece(s) for s in others)}</div>
</main>"""
    return page(1, "The Gallery", tok, css, body, "dark")

# 2. The Register: a register of title, the strongest form of "the owner keeps the address".
def d2():
    tok = """:root{--bg:#f4f0e6;--fg:#1d2a24;--muted:#4b544f;--link:#0d5a3f;--focus:#b3261e;--line:#c9c1ae;--hover:#e9e3d4;--paper:#fbf8f1;--seal:#9e2a1f;--rule:#1d2a24}
@media(prefers-color-scheme:dark){:root{--bg:#121714;--fg:#e9e5da;--muted:#b4b9b3;--link:#7fd6ae;--focus:#ff8a7a;--line:#39423d;--hover:#1c2420;--paper:#18201c;--seal:#ff8a7a;--rule:#e9e5da}}"""
    css = """main{max-width:60rem;margin:0 auto;padding:0 1rem}
.cover{border:3px double var(--rule);background:var(--paper);padding:clamp(1.2rem,4vw,2.6rem);margin:1.4rem 0 2rem;text-align:center}
.cover .k{font-variant:small-caps;letter-spacing:.18em;font-size:1rem;margin:0}
h1{font-family:Georgia,"Times New Roman",serif;font-size:clamp(2.2rem,6.5vw,3.8rem);line-height:1.06;margin:.5rem 0 .8rem;font-weight:700}
.cover .s{max-width:36rem;margin:0 auto 1rem}
.tally{display:inline-grid;grid-auto-flow:column;gap:1.6rem;border-top:1px solid var(--line);padding-top:.8rem;font-size:.95rem;color:var(--muted)}
.tally b{display:block;font-family:Georgia,serif;font-size:1.8rem;color:var(--fg)}
h2{font-family:Georgia,serif;font-size:1.5rem;margin:2.4rem 0 .4rem;border-bottom:2px solid var(--rule);padding-bottom:.3rem;display:flex;justify-content:space-between;gap:1rem;align-items:baseline;flex-wrap:wrap}
h2 small{font-family:system-ui,sans-serif;font-size:.9rem;font-weight:400;color:var(--muted)}
.title{display:grid;gap:1rem;background:var(--paper);border:1px solid var(--line);border-left:6px solid var(--rule);padding:1.1rem;margin:1rem 0;position:relative}
@media(min-width:46rem){.title{grid-template-columns:15rem 1fr}}
.title .no{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.875rem;color:var(--muted)}
.title h3{font-family:Georgia,serif;font-size:1.35rem;margin:.1rem 0 .5rem}
.title dl{display:grid;grid-template-columns:max-content 1fr;gap:.25rem .9rem;margin:0 0 .6rem;font-size:.95rem}
.title dt{color:var(--muted);font-variant:small-caps;letter-spacing:.06em}
.title dd{margin:0;overflow-wrap:anywhere}
.title .shot{border:1px solid var(--line)}
.title p{margin:0 0 .6rem}
.go{display:inline-flex;align-items:center;min-height:44px;font-weight:650}
.seal{position:absolute;right:.8rem;top:.8rem;width:5.2rem;height:5.2rem;border:3px solid var(--seal);color:var(--seal);border-radius:50%;display:grid;place-items:center;text-align:center;font-size:.72rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;line-height:1.15;transform:rotate(-12deg);background:var(--paper)}
.has-seal h3{padding-right:5.6rem}
.pending{border-left-style:dashed}
.pending .shot{filter:grayscale(1)}
@media print{.top,.foot{display:none}.title{break-inside:avoid}}
"""
    def title(s, i):
        seal = f'<span class="seal" aria-hidden="true">Handed<br>over</span>' if s.get("handed_over") else ""
        held = (f'{e(s["handed_over"][8:].lstrip("0"))} November 2026, by its owner' if s.get("handed_over") else "SovereignWebsite, until handed over")
        rows = [("Address", f'<a href="{url(s)}">{hostw(s)}</a>'), ("Kind", e(s["group"])), ("Held", held), ("Status", e(state(s)))]
        if s.get("repository"): rows.append(("Files", f'<a href="{s["repository"]["url"]}">{e(s["repository"]["url"].split("github.com/")[1])}</a>'))
        if chips(s): rows.append(("Designs", e(", ".join(chips(s)))))
        dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
        note = f"<p><b>{e(s['waiting'])}</b></p>" if s.get("waiting") else ""
        cls = " has-seal" if seal else (" pending" if s.get("waiting") else "")
        return (f'<article class="title{cls}" aria-labelledby="t-{s["slug"]}">{seal}<div>{shot(s, "shot", phone=False, alt="")}</div><div>'
                f'<span class="no">Entry {i:02d}</span><h3 id="t-{s["slug"]}">{e(s["name"])}</h3><dl>{dl}</dl><p>{e(s["summary"])}</p>{note}'
                f'<a class="go" href="{url(s)}">Visit {hostw(s)} &rarr;</a></div></article>')
    body = f"""<main id="main">
<section class="cover"><p class="k">The register of title</p><h1>Websites their owners own.</h1>
<p class="s">Built by agent teams, then handed over: the owner keeps the files, the history and the address. Every site here is public and live; open one to see it working.</p>
<div class="tally"><span><b>{len(working)}</b>sites working</span><span><b>{len(people)}</b>people's sites</span><span><b>{len(handed)}</b>handed over</span></div></section>
<h2>Part A: People <small>{len(people)} entries</small></h2>
{"".join(title(s, i + 1) for i, s in enumerate(people))}
<h2>Part B: Tools and demos <small>{len(others)} entries</small></h2>
{"".join(title(s, i + 1 + len(people)) for i, s in enumerate(others))}
</main>"""
    return page(2, "The Register", tok, css, body)

# 3. Contact Sheet: the frames on a strip; five designs, the owner circles one.
def d3():
    tok = """:root{--bg:#141414;--fg:#f2f2f0;--muted:#c4c4c0;--link:#f2f2f0;--focus:#ffd400;--line:#3a3a38;--hover:#222;--sheet:#0a0a0a;--edge:#ffb000;--grease:#ff4d3d}"""
    css = """main{max-width:80rem;margin:0 auto;padding:0 1rem}
.head{display:grid;gap:1rem;padding:1.6rem 0 1.2rem;border-bottom:1px solid var(--line)}
@media(min-width:56rem){.head{grid-template-columns:1.3fr 1fr;align-items:end}}
.head .k{font-family:ui-monospace,Menlo,Consolas,monospace;color:var(--edge);font-size:.9rem;margin:0;letter-spacing:.08em}
h1{font-size:clamp(2.4rem,7.5vw,5rem);line-height:.98;letter-spacing:-.03em;margin:.3rem 0 0;font-weight:800}
.head p{margin:0;color:var(--muted)}
.counts{font-family:ui-monospace,Menlo,Consolas,monospace;color:var(--edge);margin-top:.6rem!important}
.sheet{background:var(--sheet);margin:1.8rem 0;padding:1rem 0 1.2rem;border-radius:4px}
.sheet h2{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.95rem;font-weight:600;color:var(--edge);margin:0 1rem .7rem;letter-spacing:.1em;text-transform:uppercase}
.strip{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,19rem),1fr));gap:0;padding:22px 0;position:relative;background:#050505}
.strip::before,.strip::after{content:"";position:absolute;left:0;right:0;height:22px;background:radial-gradient(circle at 50% 50%,#2a2a28 0 4px,#0000 4.5px) 0 0/22px 22px repeat-x}
.strip::before{top:0}.strip::after{bottom:0}
.frame{position:relative;display:block;padding:14px;color:var(--fg);text-decoration:none}
.pic{position:relative;display:block}
.frame .num{position:absolute;left:4px;bottom:4px;font:700 .8rem ui-monospace,Menlo,Consolas,monospace;color:var(--edge);background:#000c;padding:.1rem .35rem}
.frame img{border:1px solid #222}
.frame figcaption{padding:.6rem .2rem 0;font-size:.95rem}
.frame figcaption b{display:block;font-size:1.05rem}
.frame figcaption span{color:var(--muted)}
.frame figure{margin:0}
.pick .pic::before{content:"";position:absolute;inset:-10px -6px;border:4px solid var(--grease);border-radius:48% 52% 45% 55%/55% 45% 55% 45%;transform:rotate(-2deg);pointer-events:none;z-index:2}
.pick .mark{position:absolute;right:6px;top:4px;z-index:3;font:800 1rem/1 "Marker Felt","Comic Sans MS",cursive;color:#fff;background:var(--grease);padding:.25rem .5rem;transform:rotate(4deg)}
.x img{filter:grayscale(1) contrast(.8) brightness(.6)}
.x .cross{position:absolute;inset:0;pointer-events:none;background:linear-gradient(to top right,#0000 calc(50% - 2px),var(--grease) calc(50% - 2px) calc(50% + 2px),#0000 calc(50% + 2px))}
.x .mark{position:absolute;right:6px;top:4px;font:700 .85rem ui-monospace,monospace;background:#000;color:#fff;border:1px solid var(--grease);padding:.15rem .4rem}
.frame:hover figcaption b,.frame:focus-visible figcaption b{text-decoration:underline}
.chip{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.8rem;color:var(--edge)}
.how{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.95rem;color:var(--muted);border-left:3px solid var(--edge);padding-left:1rem;max-width:44rem}
"""
    n = [0]
    def frame(s):
        n[0] += 1
        cls, mark = "", ""
        if s.get("handed_over"): cls, mark = " pick", '<span class="mark">Handed over</span>'
        elif s.get("waiting"): cls, mark = " x", '<span class="cross" aria-hidden="true"></span><span class="mark">Not switched on yet</span>'
        c = " &middot; ".join(e(x) for x in chips(s))
        return (f'<a class="frame{cls}" href="{url(s)}"><figure><span class="pic">{shot(s)}<span class="num" aria-hidden="true">{n[0]:02d}A</span>{mark}</span>'
                f'<figcaption><b>{e(s["name"])}</b><span>{e(s["group"])} &middot; {hostw(s)}</span>{f"<br><span class=chip>{c}</span>" if c else ""}</figcaption></figure></a>')
    body = f"""<main id="main">
<section class="head"><div><p class="k">ROLL 01 &middot; THE SHOWROOM</p><h1>Websites their owners own.</h1></div>
<div><p>Built by agent teams, then handed over: the owner keeps the files, the history and the address. Every site here is public and live; open one to see it working.</p>
<p class="counts">{len(working)} sites working &middot; {len(people)} people's sites &middot; {len(handed)} handed over</p></div></section>
<section class="sheet" aria-labelledby="s1"><h2 id="s1">Strip 1: People</h2><div class="strip">{"".join(frame(s) for s in people)}</div></section>
<section class="sheet" aria-labelledby="s2"><h2 id="s2">Strip 2: Tools and demos</h2><div class="strip">{"".join(frame(s) for s in others)}</div></section>
<p class="how">How a site is made: one request; an agent team builds it; five designs to choose from; the owner chooses one; handed over to the owner's GitHub. <a href="https://pipeline-demo.sovereignweb.site/">See it run: the pipeline demo</a>.</p>
</main>"""
    return page(3, "Contact Sheet", tok, css, body, "dark")

# 4. The Street: each site a shopfront; the address is the sign over the door.
def d4():
    tok = """:root{--bg:#e9eef2;--fg:#15202b;--muted:#46525e;--link:#0b4f8a;--focus:#c2410c;--line:#b9c3cc;--hover:#dbe3ea;--sky:#cfe0ee;--road:#2d333a;--road-ink:#f3f4f6;--awning1:#0f6e4f;--awning2:#ffffff;--brick:#f7f3ec;--sign:#15202b;--sign-ink:#fff}
@media(prefers-color-scheme:dark){:root{--bg:#0d1218;--fg:#e8edf2;--muted:#aab4be;--link:#8cc8ff;--focus:#ffa76b;--line:#2c3742;--hover:#16202a;--sky:#141d27;--road:#05080b;--road-ink:#e8edf2;--awning1:#1f8a64;--awning2:#0d1218;--brick:#17202a;--sign:#e8edf2;--sign-ink:#0d1218}}"""
    css = """main{padding:0}
.sky{background:linear-gradient(var(--sky),var(--bg));padding:2rem 1rem 1rem}
.sky>div{max-width:80rem;margin:0 auto}
.sky .k{font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:.875rem;margin:0;color:var(--muted)}
h1{font-size:clamp(2.4rem,7vw,4.6rem);line-height:1;letter-spacing:-.02em;margin:.4rem 0 .7rem;font-weight:800;max-width:16ch}
.sky p{max-width:40rem}
.street{max-width:80rem;margin:0 auto;padding:0 1rem}
.street h2{font-size:1rem;letter-spacing:.14em;text-transform:uppercase;margin:2rem 0 0;color:var(--muted)}
.row{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,22rem),1fr));gap:0 1rem;align-items:end}
.shop{display:block;text-decoration:none;color:var(--fg);margin-top:1.6rem}
.sign{display:block;background:var(--sign);color:var(--sign-ink);font:700 clamp(.85rem,2.4vw,.95rem)/1.2 ui-monospace,Menlo,Consolas,monospace;padding:.55rem .7rem;text-align:center;overflow-wrap:anywhere;border-radius:4px 4px 0 0}
.awning{height:22px;background:repeating-linear-gradient(90deg,var(--awning1) 0 24px,var(--awning2) 24px 48px);clip-path:polygon(0 0,100% 0,97% 100%,3% 100%);border-bottom:2px solid var(--awning1)}
.front{background:var(--brick);border:2px solid var(--line);border-top:0;padding:12px;display:grid;gap:.7rem}
.window{border:6px solid var(--fg);border-radius:2px;background:#000;position:relative}
.window::after{content:"";position:absolute;inset:0;background:linear-gradient(115deg,rgb(255 255 255/.22),#0000 35%);pointer-events:none}
.plate b{display:block;font-size:1.15rem}
.plate span{color:var(--muted);font-size:.95rem}
.door{display:inline-flex;align-items:center;min-height:44px;padding:.4rem .9rem;border:2px solid var(--fg);border-radius:999px;font-weight:700;justify-self:start}
.shop:hover .door,.shop:focus-visible .door{background:var(--fg);color:var(--bg)}
.board{display:inline-block;background:#0f6e4f;color:#fff;font-weight:800;font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;padding:.15rem .5rem;margin-right:.3rem}
.board.alt{background:var(--fg);color:var(--bg)}
.shut .window img{filter:grayscale(1) brightness(.6)}
.shut .awning{background:repeating-linear-gradient(90deg,#6b7480 0 24px,var(--awning2) 24px 48px);border-color:#6b7480}
.shut .door{border-style:dashed}
.kerb{height:10px;background:#9aa3ab;margin-top:0}
.road{background:var(--road);color:var(--road-ink);padding:1.2rem 1rem;position:relative}
.road::before{content:"";position:absolute;left:0;right:0;top:50%;height:4px;background:repeating-linear-gradient(90deg,#f4c542 0 40px,#0000 40px 80px);opacity:.9}
.road ul{list-style:none;margin:0 auto;padding:0;max-width:80rem;display:flex;flex-wrap:wrap;gap:1rem 2.4rem;position:relative}
.road li{background:var(--road);padding:0 .5rem;font-size:.95rem}
.road b{font-size:1.6rem;margin-right:.3rem}
"""
    def shop(s):
        b = ""
        if s.get("handed_over"): b += '<span class="board">Handed over</span>'
        for c in chips(s): b += f'<span class="board alt">{e(c)}</span>'
        door = "Not switched on yet" if s.get("waiting") else "Walk in &rarr;"
        sub = f"{e(s['waiting'])}" if s.get("waiting") else e(s["summary"])
        return (f'<a class="shop{" shut" if s.get("waiting") else ""}" href="{url(s)}"><span class="sign">{hostw(s)}</span><span class="awning" aria-hidden="true"></span>'
                f'<span class="front"><span class="window">{shot(s, alt="")}</span><span class="plate"><b>{e(s["name"])}</b><span>{e(s["group"])}. {sub}</span></span>'
                f'{f"<span>{b}</span>" if b else ""}<span class="door">{door}</span></span></a>')
    body = f"""<main id="main">
<section class="sky"><div><p class="k">The showroom</p><h1>Websites their owners own.</h1>
<p>Built by agent teams, then handed over: the owner keeps the files, the history and the address. Every site here is public and live; open one to see it working.</p></div></section>
<section class="street" aria-labelledby="p-h"><h2 id="p-h">People's sites</h2><div class="row">{"".join(shop(s) for s in people)}</div></section>
<div class="kerb" aria-hidden="true"></div>
<section class="road" aria-label="On this street"><ul><li><b>{len(working)}</b>sites working</li><li><b>{len(people)}</b>people's sites</li><li><b>{len(handed)}</b>handed over</li></ul></section>
<section class="street" aria-labelledby="t-h"><h2 id="t-h">Tools and demos</h2><div class="row">{"".join(shop(s) for s in others)}</div></section>
<div class="kerb" aria-hidden="true"></div>
</main>"""
    return page(4, "The Street", tok, css, body)

# 5. The Line: the pipeline from the hub's own "How a site is made", each site placed at the station it has reached.
def d5():
    tok = """:root{--bg:#fafafa;--fg:#111;--muted:#4a4a4a;--link:#0040c1;--focus:#e4002b;--line:#d4d4d4;--hover:#efefef;--belt:#111;--hi:#ffd60a;--hi-ink:#111;--done:#0b7a43}
@media(prefers-color-scheme:dark){:root{--bg:#0b0b0b;--fg:#f2f2f2;--muted:#b8b8b8;--link:#8fb4ff;--focus:#ff6b81;--line:#2e2e2e;--hover:#191919;--belt:#f2f2f2;--hi:#ffd60a;--hi-ink:#111;--done:#4fd18b}}"""
    css = """main{max-width:80rem;margin:0 auto;padding:0 1rem}
.k{font-weight:800;font-size:.875rem;letter-spacing:.16em;text-transform:uppercase;margin:1.6rem 0 0}
h1{font-size:clamp(2.4rem,8vw,5.4rem);line-height:.95;letter-spacing:-.035em;margin:.3rem 0 .8rem;font-weight:900;max-width:14ch}
.lede{max-width:40rem;font-size:1.1rem}
.counts{display:flex;gap:.6rem;flex-wrap:wrap;list-style:none;padding:0;margin:1rem 0 0}
.counts li{border:2px solid var(--fg);padding:.3rem .7rem;font-weight:700}
.line{list-style:none;margin:2.4rem 0;padding:0;display:grid;gap:0;counter-reset:st}
@media(min-width:60rem){.line{grid-template-columns:repeat(5,1fr)}}
.st{position:relative;padding:1rem 1rem 1.2rem 3.4rem;border-left:4px solid var(--belt);counter-increment:st}
@media(min-width:60rem){.st{border-left:0;border-top:4px solid var(--belt);padding:2.4rem .8rem 1rem}}
.st::before{content:counter(st);position:absolute;left:-1.25rem;top:.9rem;width:2.3rem;height:2.3rem;border-radius:50%;background:var(--bg);border:4px solid var(--belt);display:grid;place-items:center;font-weight:900}
@media(min-width:60rem){.st::before{left:.8rem;top:-1.35rem}}
.st h2{font-size:1.1rem;margin:0 0 .6rem;line-height:1.2}
.st.end{border-color:var(--done)}
.st.end::before{background:var(--done);color:var(--bg);border-color:var(--done)}
.here{list-style:none;padding:0;margin:0;display:grid;gap:.6rem}
.card{display:block;color:var(--fg);text-decoration:none;border:2px solid var(--fg);background:var(--bg)}
.card b{display:block;padding:.45rem .6rem 0}
.card span{display:block;padding:0 .6rem .5rem;font-size:.9rem;color:var(--muted)}
.card:hover,.card:focus-visible{background:var(--hi);color:var(--hi-ink)}
.card:hover span,.card:focus-visible span{color:var(--hi-ink)}
.card.big{border-width:3px;border-color:var(--done)}
.card.big b{font-size:1.2rem}
.empty{font-size:.9rem;color:var(--muted);margin:0}
.side{border-top:4px solid var(--belt);padding-top:1rem;margin-top:2rem}
.side h2{font-size:1.4rem;margin:0 0 .4rem}
.side .row{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,17rem),1fr));gap:1rem;margin-top:1rem}
.side .card.off{border-style:dashed}
.side .card.off img{filter:grayscale(1)}
.card .tag{display:inline-block;background:var(--hi);color:var(--hi-ink);font-weight:800;font-size:.8rem;padding:.05rem .4rem;margin:0 .6rem .5rem}
"""
    def card(s, big=False, off=False):
        t = "".join(f'<span class="tag">{e(c)}</span>' for c in chips(s))
        extra = f'<span>{e(s["waiting"])}</span>' if s.get("waiting") else f'<span>{e(host(s))}</span>'
        return (f'<a class="card{" big" if big else ""}{" off" if off else ""}" href="{url(s)}">{shot(s, alt="", lazy=not big)}<b>{e(s["name"])}</b>{extra}'
                f'{f"<span style=padding:0>{t}</span>" if t else ""}</a>')
    at_five = [s for s in people if not s.get("handed_over") and "Five designs" in chips(s)]
    st = [("One request", '<p class="empty">Every site starts here: one request, from its owner.</p>'),
          ("An agent team builds it", '<p class="empty">A team of agents writes it, checks it and puts it live.</p>'),
          ("Five designs to choose from", "<ul class=here>" + "".join(f"<li>{card(s)}</li>" for s in at_five) + "</ul>"),
          ("The owner chooses one", '<p class="empty">The owner picks the design they want to keep.</p>'),
          ("Handed over to the owner's GitHub", "<ul class=here>" + "".join(f"<li>{card(s, big=True)}</li>" for s in handed) + "</ul>")]
    line = "".join(f'<li class="st{" end" if i == 4 else ""}"><h2>{t}</h2>{c}</li>' for i, (t, c) in enumerate(st))
    body = f"""<main id="main">
<p class="k">The showroom</p><h1>Websites their owners own.</h1>
<p class="lede">Built by agent teams, then handed over: the owner keeps the files, the history and the address. Every site here is public and live; open one to see it working.</p>
<ul class="counts"><li>{len(working)} sites working</li><li>{len(people)} people's sites</li><li>{len(handed)} handed over</li></ul>
<ol class="line" aria-label="How a site is made, with each person's site where it stands">{line}</ol>
<section class="side" aria-labelledby="td"><h2 id="td">Tools and demos</h2><p>Built the same way. <a href="https://pipeline-demo.sovereignweb.site/">See it run: the pipeline demo</a>.</p>
<div class="row">{"".join(card(s, off=bool(s.get("waiting"))) for s in others)}</div></section>
</main>"""
    return page(5, "The Line", tok, css, body)

INDEX_CSS = """main{max-width:70rem;margin:0 auto;padding:0 1rem}
h1{font-size:clamp(2rem,5vw,3rem);margin:1.4rem 0 .4rem}
.designs{list-style:none;padding:0;display:grid;gap:1.2rem;grid-template-columns:repeat(auto-fill,minmax(min(100%,19rem),1fr))}
.designs a{display:block;border:2px solid var(--fg);padding:1rem;color:var(--fg);text-decoration:none;min-height:44px}
.designs a:hover,.designs a:focus-visible{background:var(--hover)}
.designs b{display:block;font-size:1.2rem}
"""
IDX_TOK = """:root{--bg:#fff;--fg:#111;--muted:#4a4a4a;--link:#0040c1;--focus:#e4002b;--line:#d4d4d4;--hover:#f0f0f0}
@media(prefers-color-scheme:dark){:root{--bg:#0b0b0b;--fg:#f2f2f2;--muted:#b8b8b8;--link:#8fb4ff;--focus:#ff6b81;--line:#2e2e2e;--hover:#1a1a1a}}"""

def index():
    items = "".join(f'<li><a href="{i}.html"><b>{i}. {e(t)}</b>{e(d)}</a></li>' for i, t, d in DESIGNS)
    body = f"""<main id="main"><h1>Five designs for the hub</h1>
<p>Five ideas from the hub's own world, not five colour schemes of one layout. Every word about a site comes from the hub's <code>sites.json</code>. Prototypes for hub.b; Dinis chooses.</p>
<ul class="designs">{items}</ul></main>"""
    return page(1, "Five designs", IDX_TOK, INDEX_CSS, body).replace("Design 1: The Gallery</summary>", "Choose a design</summary>").replace(' aria-current="page"', "", 1)

OUT.mkdir(parents=True, exist_ok=True)
for i, f in enumerate([d1, d2, d3, d4, d5], 1):
    (OUT / f"{i}.html").write_text(f())
(OUT / "index.html").write_text(index())
print("wrote", OUT)

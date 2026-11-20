"""Shared shell for the five Kate Curtis-Evans designs (design.c, 20 Nov 2026).
Family bar, skip link, footer and photo credit copied from the live page at 28823d2;
family links raised to 24 px targets. Every sentence in the designs is from the live page."""

FAMILY = """<nav class="family" aria-label="The Sovereign Website family">
  <ul>
    <li><a href="https://sovereignwebsite.ai/">Sovereign Website</a></li>
    <li><a href="https://sovereignwebsite.org/">Principles</a></li>
    <li><a href="https://sovereignwebsite.site/" aria-current="true">Hosted</a></li>
    <li><a href="https://hub.sovereignweb.site/">Hub</a></li>
    <li><a href="https://agents.sovereignweb.site/">Agents</a></li>
    <li><a href="https://vault.sovereignwebsite.site/">Vault</a></li>
    <li class="family-sep"><a href="https://agenticcells.ai/">AgentiCCells</a></li>
    <li><a href="https://riskmandate.ai/">RiskMandate</a></li>
    <li><a href="https://newsroom.sgit.ai/">Newsroom</a></li>
  </ul>
</nav>"""

BASE_CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{color-scheme:light dark}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:1.0625rem/1.62 var(--sans);overflow-wrap:break-word}
img{max-width:100%;height:auto;display:block}
figure{margin:0}
a{color:var(--link,var(--accent))}
:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.skip{position:absolute;left:-999px;top:0}
.skip:focus{left:1rem;top:1rem;background:var(--bg);color:var(--fg);padding:.5rem .8rem;z-index:9}
.family{font-size:.875rem;border-bottom:1px solid var(--line)}
.family ul{list-style:none;margin:0 auto;padding:.15rem 1rem;display:flex;flex-wrap:wrap;gap:0 .9rem;max-width:72rem}
.family a{color:var(--muted);text-decoration:none;display:inline-block;min-height:24px;line-height:24px}
.family a:hover,.family a:focus-visible{color:var(--fg);text-decoration:underline}
.family .family-sep{margin-left:auto}@media (max-width:40rem){.family .family-sep{margin-left:0}}
.site-foot{font-size:.9rem;color:var(--muted);padding:2rem 1rem 3rem;max-width:68rem;margin:0 auto}
.site-foot p{margin:0 0 .5rem}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
"""

SANS = 'system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif'
SERIF = '"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif'
MONO = 'ui-monospace,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace'

PHOTO_ALT = "Black and white photo of Kate at her desk, smiling on the phone, with her dog resting its head against her."
def photo(cls="photo", sizes="(min-width:56rem) 32rem, 100vw", lazy=False):
    return (f'<figure class="{cls}"><img src="img/kate-at-desk.webp" srcset="img/kate-at-desk-640.webp 640w, img/kate-at-desk.webp 1280w" '
            f'sizes="{sizes}" width="1280" height="882"{" loading=\"lazy\"" if lazy else ""} alt="{PHOTO_ALT}">'
            f'<figcaption>Photo: Matt Hinton Photography</figcaption></figure>')

LI = "https://www.linkedin.com/in/kate-curtis-evans/"
AG = "https://audio-genius.com/"

FOOT = """<footer class="site-foot">
  <p>Photo of Kate at her desk by Matt Hinton Photography. Everything on this page comes from Kate's own LinkedIn profile and posts.</p>
  <p>No cookies, no tracking. A sovereign website, made with the <a href="https://sovereignwebsite.org/">open pattern</a>. Source: <a href="https://github.com/SovereignWebsite/Site__Founder__Kate-Curtis-Evans">github.com/SovereignWebsite/Site__Founder__Kate-Curtis-Evans</a>.</p>
  <p>Design {n} of 5, {name}. <a href="index.html">All five designs</a>.</p>
</footer>"""

def page(n, name, title, tokens, css, body, desc=None):
    desc = desc or ("Kate Curtis-Evans, practising legal transcriber and founder of Audio Genius, "
                    "legal transcription and workflow built by a transcriber, for transcription professionals.")
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<style>
{tokens}
:root{{--sans:{SANS};--serif:{SERIF};--mono:{MONO}}}
{BASE_CSS}
{css}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{FAMILY}
{body}
{FOOT.format(n=n, name=name)}
</body>
</html>
"""

from shell import *

TOK = """:root{--bg:#ffffff;--fg:#111111;--muted:#4a4a4a;--accent:#8f2f1c;--line:#cfcfcf}
@media (prefers-color-scheme:dark){:root{--bg:#141414;--fg:#eeeeee;--muted:#b3b3b3;--accent:#f09a7a;--line:#3a3a3a}}"""

CSS = """
main{max-width:42rem;margin:0 auto;padding:1.5rem 1rem 1rem}
h1{font-family:var(--serif);font-size:clamp(2rem,6vw,2.8rem);line-height:1.08;margin:0 0 .3rem}
.role{margin:0 0 .8rem;font-weight:600}
.lede{font-family:var(--serif);font-size:1.2rem;line-height:1.4;margin:0 0 1rem}
.contacts{display:flex;flex-wrap:wrap;gap:.3rem 1.5rem;margin:0 0 1rem;padding:.6rem 0;border-top:1.5px solid var(--fg);border-bottom:1px solid var(--line);list-style:none}
.contacts a{display:inline-block;min-height:24px}
h2{font-size:.95rem;letter-spacing:.1em;text-transform:uppercase;margin:1.6rem 0 .5rem;padding-bottom:.25rem;border-bottom:1px solid var(--line)}
p{margin:0 0 .7rem}
dl{display:grid;grid-template-columns:auto 1fr;gap:.25rem 1rem;margin:0}
dt{font-weight:700;font-variant-numeric:tabular-nums}
dd{margin:0}
.src{color:var(--muted);font-size:.9rem}
ul{margin:0;padding-left:1.1rem}
li{margin:0 0 .35rem}
.print{margin:1.5rem 0 0}
@media print{
  .family,.skip,.print,.site-foot p:last-child{display:none}
  :root{--bg:#fff;--fg:#000;--muted:#333;--accent:#000;--line:#999}
  body{font-size:10.5pt;line-height:1.45}
  main{max-width:none;padding:0}
  h2{break-after:avoid}
  a{color:#000;text-decoration:none}
  .contacts a::after{content:" (" attr(href) ")";font-size:9pt}
  @page{margin:16mm}
}
"""

BODY = f"""<main id="main">
<h1>Kate Curtis&#8209;Evans</h1>
<p class="role">Founder, Audio Genius. Based in the United Kingdom.</p>
<p class="lede">A practising legal transcriber who built a live transcription platform without knowing how to code. Now looking for a technical co-founder.</p>
<ul class="contacts"><li><a href="{LI}">LinkedIn: linkedin.com/in/kate-curtis-evans</a></li><li><a href="{AG}">audio-genius.com</a></li></ul>

<h2>Wanted: a technical co-founder</h2>
<p>To own the technical scope, the build, integration and implementation: moving to a tech stack built for regulated data and getting certifications like Cyber Essentials in place. Ideally someone with legal tech or regulated-industry experience.</p>
<p>Kate brings the vision for the platform, direct access to users, research and results, and a strategy for expanding into corporates and organisations.</p>
<p>Why now: the platform Kate built Audio Genius on will not let her fork a test site from the live one, and gives her limited control over hosting and other parts of the build. She wants to own how it scales.</p>

<h2>Audio Genius</h2>
<p>An ASR-powered legal transcription and workflow platform designed around human-led transcription. The technology does the heavy lifting, but the professional keeps control. Security, confidentiality and responsible data handling are fundamental, not features to bolt on later. Kate has stopped adding new features on purpose so that privacy and data protection come first.</p>

<h2>Where it stands, in Kate's words</h2>
<dl>
  <dt>50</dt><dd>testers in a 90-day beta</dd>
  <dt>34,000</dt><dd>minutes of audio transcribed since launch in September</dd>
  <dt>1,200</dt><dd>website visits, with no paid advertising as yet</dd>
</dl>
<p style="margin-top:.6rem">Paying users; not one of those who signed up at the end of the beta has left. Bootstrapped and pre-seed.</p>
<p class="src">Figures exactly as Kate stated them in her LinkedIn post looking for a technical co-founder, as given to this site on 20 November 2026.</p>

<h2>Experience</h2>
<dl>
  <dt>Nov 2025 to now</dt><dd>Founder, Audio Genius</dd>
  <dt>Mar 2021 to now</dt><dd>Transcription Specialist (Legal and Professional)</dd>
  <dt>2022 to now</dt><dd>Legal Transcriber, eScribers</dd>
  <dt>2021 to 2022</dt><dd>Freelance Transcriber, Ubiqus</dd>
  <dt>1992 to 1996</dt><dd>BA in European Business Studies, Brunel University of London</dd>
</dl>

<h2>Also open to</h2>
<ul>
  <li>Law firms and agencies exploring secure transcription and workflow technology.</li>
  <li>Transcribers and legal professionals who want to help shape the technology they will actually use.</li>
  <li>Investors interested in vertical SaaS built from genuine domain expertise.</li>
  <li>LegalTech, speech technology and security partners.</li>
</ul>
<p class="print">This page prints on one or two sheets of A4.</p>
</main>"""

open('../designs/5.html', 'w').write(page(5, "The Brief", "The Brief, Kate Curtis-Evans", TOK, CSS, BODY))

IDX_CSS = """
main{max-width:56rem;margin:0 auto;padding:2rem 1rem}
h1{font-family:var(--serif);font-size:clamp(2rem,6vw,3rem);line-height:1.1;margin:0 0 .6rem}
.designs{list-style:none;padding:0;margin:1.5rem 0;display:grid;gap:1rem}
.designs li{border:1px solid var(--line);border-radius:8px;padding:1rem}
.designs h2{font-family:var(--serif);font-size:1.4rem;margin:0 0 .3rem}
.designs p{margin:0}
"""
DESIGNS = [
  ("../index.html", "1. The Workflow Board (the home page)", "Audio Genius manages transcription work, so Kate's own work is a board: delivered, in progress, on hold on purpose, and one open job, the technical co-founder."),
  ("1.html", "2. The Transcript", "The page as a legal transcript, the document Kate produces every day: a cover sheet, numbered turns, Q and A, her own words verbatim, the beta figures as Exhibit A."),
  ("2.html", "3. The Edit Window", "Designed dark first, as a transcription editor: a waveform, her roles as tracks on a timeline drawn to the year, each section a segment with its label."),
  ("newsroom.html", "4. The Newsroom", "Her founder story told as a news feature: the specialist who became a founder. A headline, a standfirst, the lead photo, the story with her quote pulled out, and the figures in an at-a-glance box."),
  ("5.html", "5. The Brief", "Plain and printable for people in a hurry: the ask, the product, the figures and her record on one or two sheets of A4."),
]
IDX = f"""<main id="main">
<h1>Five designs for Kate Curtis&#8209;Evans</h1>
<p>Each is an idea from Kate's own world that rebuilds the page. Every word on them is from her own LinkedIn profile and posts, as on the live page.</p>
<ol class="designs">{''.join(f'<li><h2><a href="{h}">{t}</a></h2><p>{d}</p></li>' for h, t, d in DESIGNS)}</ol>
</main>"""
open('../designs/index.html', 'w').write(page("index", "the index", "Five designs, Kate Curtis-Evans", TOK, IDX_CSS, IDX).replace("<p>Design index of 5, the index. <a href=\"index.html\">All five designs</a>.</p>\n", ""))

from shell import *

# Designed dark first: dark is the default, light is the variant.
TOK = """:root{--bg:#0f1115;--panel:#171a20;--panel2:#1e222a;--fg:#e9e7e2;--muted:#a6abb4;--accent:#7fd6c7;--accent-ink:#06201c;--amber:#f2b35b;--line:#2c313b;--clip:#24423d}
@media (prefers-color-scheme:light){:root{--bg:#eef0f3;--panel:#ffffff;--panel2:#f6f7f9;--fg:#15171b;--muted:#4b505a;--accent:#0b6b5d;--accent-ink:#fff;--amber:#8a5200;--line:#d3d7de;--clip:#cfe9e4}}"""

CSS = """
main{max-width:72rem;margin:0 auto;padding:0 1rem}
.top{display:grid;gap:1.5rem;padding:2rem 0 1.5rem}
@media (min-width:56rem){.top{grid-template-columns:1.1fr 1fr;align-items:center;padding:3.5rem 0 2rem;gap:3rem}}
.eyebrow{font-family:var(--mono);font-size:.875rem;color:var(--accent);margin:0 0 .6rem}
h1{font-weight:750;font-size:clamp(2.4rem,7vw,4rem);line-height:1.02;letter-spacing:-.02em;margin:0 0 .8rem}
.lede{font-size:clamp(1.15rem,2.4vw,1.4rem);line-height:1.45;margin:0 0 1rem}
.btns{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.2rem}
.btn{display:inline-flex;align-items:center;min-height:44px;padding:.55rem 1rem;border-radius:6px;font-weight:650;text-decoration:none;border:1.5px solid var(--accent)}
.btn.main{background:var(--accent);color:var(--accent-ink)}
.photo{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:.5rem}
.photo img{border-radius:4px;filter:grayscale(1)}
.photo figcaption{font-family:var(--mono);font-size:.875rem;color:var(--muted);padding:.4rem .2rem 0}
.wave{display:block;width:100%;height:56px;color:var(--accent);opacity:1}
/* tracks: a multitrack timeline of Kate's years, drawn to the year */
.tracks{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:1rem;margin:1rem 0 2.5rem}
.tracks h2,.seg h2{font-family:var(--mono);font-size:.875rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 .8rem}
.ruler,.track{display:grid;grid-template-columns:minmax(7rem,11rem) 1fr;gap:.8rem;align-items:center}
.ruler .axis{display:grid;grid-template-columns:repeat(6,1fr);font-family:var(--mono);font-size:.875rem;color:var(--muted);border-bottom:1px solid var(--line);padding-bottom:.2rem}
.track{padding:.45rem 0;border-bottom:1px solid var(--line)}
.track:last-child{border-bottom:0}
.track .lab{font-size:.95rem;line-height:1.3}
.track .lab small{display:block;font-family:var(--mono);font-size:.875rem;color:var(--muted)}
.lane{position:relative;height:28px;background:repeating-linear-gradient(90deg,transparent 0 calc(100%/6 - 1px),var(--line) calc(100%/6 - 1px) calc(100%/6))}
.clip{position:absolute;top:3px;bottom:3px;left:calc(var(--s)/72*100%);right:calc((72 - var(--e))/72*100%);background:var(--clip);border:1.5px solid var(--accent);border-radius:4px}
.clip.now::after{content:"";position:absolute;right:-1px;top:-6px;bottom:-6px;border-right:2px solid var(--amber)}
.early{font-size:.95rem;color:var(--muted);margin:.8rem 0 0}
@media (max-width:34rem){.ruler,.track{grid-template-columns:1fr}.ruler .lab{display:none}}
/* segments */
.seg{display:grid;gap:.4rem 2rem;padding:1.6rem 0;border-top:1px solid var(--line)}
@media (min-width:56rem){.seg{grid-template-columns:11rem 1fr}}
.seg .chip{font-family:var(--mono);font-size:.875rem;color:var(--accent)}
.seg .txt{max-width:42rem}
.seg .txt p{margin:0 0 .8rem}
.seg h3{font-size:clamp(1.4rem,3.4vw,1.9rem);line-height:1.2;margin:0 0 .7rem}
blockquote{margin:1rem 0;padding:1rem 1.1rem;background:var(--panel);border-left:4px solid var(--amber);border-radius:4px;font-size:1.2rem;line-height:1.45}
blockquote footer{font-size:.9rem;color:var(--muted);margin-top:.4rem}
.meters{display:grid;gap:.8rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,13rem),1fr));margin:.4rem 0 1rem;padding:0;list-style:none}
.meters li{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:.9rem 1rem}
.meters b{display:block;font-family:var(--mono);font-size:clamp(2rem,6vw,2.6rem);line-height:1.1;color:var(--accent);font-weight:600}
.src{font-size:.9rem;color:var(--muted)}
.pair{display:grid;gap:.8rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,16rem),1fr));margin:.8rem 0}
.pair div{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:.8rem 1rem}
.pair h4{margin:0 0 .3rem;font-size:1rem}
.open{list-style:none;padding:0;margin:0;display:grid;gap:.6rem}
.open li{background:var(--panel2);border:1px solid var(--line);border-radius:6px;padding:.6rem .9rem}
.open strong{display:block}
.speaker{display:inline-block;font-family:var(--mono);font-size:.875rem;border:1px solid var(--amber);color:var(--amber);border-radius:999px;padding:0 .6rem;margin-bottom:.4rem}
"""

WAVE = """<svg class="wave" viewBox="0 0 600 56" preserveAspectRatio="none" aria-hidden="true" focusable="false"><g fill="currentColor">""" + "".join(
    f'<rect x="{i*6}" y="{28-h}" width="3" height="{2*h}" rx="1.5"/>' for i, h in enumerate(
        [3,6,10,14,8,5,12,20,24,16,9,6,4,8,13,18,22,25,19,11,7,5,3,6,9,15,21,17,12,8,4,3,5,10,16,23,26,20,13,9,6,4,7,12,18,14,9,5,3,4,8,14,20,24,18,12,7,4,3,5,9,13,17,21,16,10,6,4,3,6,11,16,22,19,13,8,5,3,4,7,12,18,23,20,14,9,6,4,3,5,8,12,15,11,7,4,3,5,8,4])) + "</g></svg>"

# months from Jan 2021 (0) to Dec 2026 (72); "now" is November 2026 (71)
def track(label, sub, s, e, now=False):
    return f'<div class="track"><div class="lab">{label}<small>{sub}</small></div><div class="lane" aria-hidden="true"><span class="clip{" now" if now else ""}" style="--s:{s};--e:{e}"></span></div></div>'

BODY = f"""<main id="main">
<header class="top">
  <div>
    <p class="eyebrow">Founder, Audio Genius</p>
    <h1>Kate Curtis&#8209;Evans</h1>
    <p class="lede">A practising legal transcriber who built a live transcription platform without knowing how to code.</p>
    {WAVE}
    <p>Audio Genius is legal transcription and workflow management, built by a transcriber, for transcription professionals. Kate is based in the United Kingdom and is now looking for a technical co-founder.</p>
    <div class="btns"><a class="btn main" href="{LI}">Message Kate on LinkedIn</a><a class="btn" href="{AG}">Visit audio-genius.com</a></div>
  </div>
  {photo()}
</header>
<section class="tracks" aria-labelledby="tr-h">
  <h2 id="tr-h">Six years of legal transcription, as tracks</h2>
  <div class="ruler"><span class="lab"></span><div class="axis" aria-hidden="true"><span>2021</span><span>2022</span><span>2023</span><span>2024</span><span>2025</span><span>2026</span></div></div>
  {track("Freelance Transcriber, Ubiqus", "2021 to 2022", 0, 24)}
  {track("Transcription Specialist (Legal and Professional)", "Mar 2021 to now", 2, 71, True)}
  {track("Legal Transcriber, eScribers", "2022 to now", 12, 71, True)}
  {track("Founder, Audio Genius", "Nov 2025 to now", 58, 71, True)}
  <p class="early">Before that: a BA in European Business Studies at Brunel University of London, 1992 to 1996. Tracks are drawn to the year; the amber line is now.</p>
</section>

<section class="seg" aria-labelledby="s1"><p class="chip">Her story</p><div class="txt">
  <h3 id="s1">Built by someone who does the work</h3>
  <p>Kate has spent six years transcribing for legal professionals across the UK, and she still does the work every day. She kept seeing the same problem: most transcription technology is built for organisations processing audio, or for people capturing their own meetings. Very little of it is designed around the person producing the finished transcript from someone else's audio, with multiple speakers, difficult recordings, exacting standards, confidentiality requirements and deadline pressure.</p>
  <p>So she built what she wanted to use herself, with no outside funding and no traditional tech background. She taught herself to build with vibe coding and AI tools, and learnt to test properly before anything goes live.</p>
  <blockquote><span class="speaker">Kate</span><br>&ldquo;I'm not a tech founder guessing at what professional transcribers need. I am one, and that's the difference.&rdquo;<footer>Kate, on her LinkedIn profile</footer></blockquote>
</div></section>

<section class="seg" aria-labelledby="s2"><p class="chip">The product</p><div class="txt">
  <h3 id="s2">Audio Genius</h3>
  <p>Audio Genius is an ASR-powered legal transcription and workflow platform designed around human-led transcription. The technology does the heavy lifting, but the professional keeps control. Because legal audio can hold highly sensitive information, Kate treats security, confidentiality and responsible data handling as fundamental, not features to bolt on later.</p>
  <p>It is being developed with feedback from real transcription professionals, and some of the best ideas for the platform have come directly from the people testing it.</p>
</div></section>

<section class="seg" aria-labelledby="s3"><p class="chip">Where it stands</p><div class="txt">
  <h3 id="s3">In Kate's words</h3>
  <ul class="meters">
    <li><b>50</b>testers in a 90-day beta</li>
    <li><b>34,000</b>minutes of audio transcribed since launch in September</li>
    <li><b>1,200</b>website visits, from Google, social media and elsewhere, with no paid advertising as yet</li>
  </ul>
  <p>It now has paying users, and not one of those who signed up at the end of the beta has left. They use it every day. Audio Genius is bootstrapped and pre-seed.</p>
  <p class="src">Figures exactly as Kate stated them in her LinkedIn post looking for a technical co-founder, as given to this site on 20 November 2026.</p>
</div></section>

<section class="seg" aria-labelledby="s4"><p class="chip">Foundations first</p><div class="txt">
  <h3 id="s4">The part nobody sees</h3>
  <p>Kate has stopped adding new features on purpose, including a legal glossary and template uploads she was looking forward to building. What comes first is the part nobody sees: privacy and data protection, working through what the platform holds and how long it keeps it, one decision at a time.</p>
</div></section>

<section class="seg" aria-labelledby="s5"><p class="chip">Wanted</p><div class="txt">
  <h3 id="s5">A technical co-founder</h3>
  <p>The platform Kate built Audio Genius on will not let Kate fork a test site from the live one, and gives her limited control over hosting and other parts of the build. She wants to own how it scales. The next stage is moving to a tech stack built for regulated data and getting certifications like Cyber Essentials in place. That is the work she wants a partner to own, ideally someone with legal tech or regulated-industry experience.</p>
  <div class="pair"><div><h4>What Kate brings</h4>The vision for the platform, direct access to users, research and results, and a strategy for expanding into corporates and organisations.</div><div><h4>What the co-founder would own</h4>The technical scope, the build, integration and implementation.</div></div>
  <p>If that is you, message her. If you know who it is, send her an introduction.</p>
  <p><a class="btn main" href="{LI}">Message Kate on LinkedIn</a></p>
</div></section>

<section class="seg" aria-labelledby="s6"><p class="chip">Also open to</p><div class="txt">
  <h3 id="s6">Collaborations, partnerships and investment</h3>
  <ul class="open">
    <li><strong>Law firms and agencies</strong>Exploring secure transcription and workflow technology for in-house teams and freelancer networks.</li>
    <li><strong>Transcribers and legal professionals</strong>Who want to help shape the technology they will actually use.</li>
    <li><strong>Investors</strong>Interested in vertical SaaS built from genuine domain expertise and a clearly identified industry problem.</li>
    <li><strong>Partners</strong>LegalTech, speech technology and security partners who understand the technical and compliance challenges of handling professional and legal audio.</li>
  </ul>
</div></section>

<section class="seg" aria-labelledby="s7"><p class="chip">Get in touch</p><div class="txt">
  <h3 id="s7">Kate would love to connect</h3>
  <p>She is building Audio Genius publicly and sharing what she learns along the way, from transcription and ASR to product development, security, LegalTech and becoming a software founder without a traditional technology background.</p>
  <div class="btns"><a class="btn main" href="{LI}">LinkedIn</a><a class="btn" href="{AG}">audio-genius.com</a></div>
</div></section>
</main>"""

open('../designs/2.html', 'w').write(page(2, "The Edit Window", "The Edit Window, Kate Curtis-Evans", TOK, CSS, BODY))

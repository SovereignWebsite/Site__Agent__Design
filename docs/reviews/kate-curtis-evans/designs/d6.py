from shell import *

# The Newsroom: Kate's founder story told as a news feature. Every sentence is from the live page;
# the headline and standfirst only restate those facts. No byline, no invented dateline.
TOK = """:root{--bg:#fbfaf7;--fg:#141414;--muted:#4f4d48;--accent:#a3271b;--accent-ink:#fff;--line:#d8d4cb;--rule:#141414;--box:#f1ede4}
@media (prefers-color-scheme:dark){:root{--bg:#111111;--fg:#efede8;--muted:#b0ada5;--accent:#ff8f7d;--accent-ink:#1d0703;--line:#333230;--rule:#efede8;--box:#1b1a19}}"""

CSS = """
main{max-width:70rem;margin:0 auto;padding:0 1rem}
.mast{display:flex;flex-wrap:wrap;justify-content:space-between;gap:.2rem 1rem;border-bottom:3px double var(--rule);padding:1rem 0 .5rem;margin-bottom:1.6rem;font-family:var(--mono);font-size:.875rem;letter-spacing:.08em;text-transform:uppercase}
.mast strong{font-family:var(--serif);font-size:1.2rem;letter-spacing:.02em;text-transform:none}
.kicker{font-size:.875rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin:0 0 .6rem}
h1{font-family:var(--serif);font-weight:700;font-size:clamp(2.3rem,7.5vw,4.8rem);line-height:1.02;letter-spacing:-.015em;margin:0 0 1rem;max-width:18ch}
.stand{font-family:var(--serif);font-size:clamp(1.2rem,2.6vw,1.55rem);line-height:1.4;margin:0 0 1rem;max-width:40rem}
.who{font-size:.95rem;color:var(--muted);margin:0 0 1.4rem;border-top:1px solid var(--line);padding-top:.6rem}
.who b{color:var(--fg)}
.lead{margin:0 0 2rem}
.lead figcaption{font-size:.9rem;color:var(--muted);margin-top:.4rem;border-bottom:1px solid var(--line);padding-bottom:.5rem}
.lead img{filter:grayscale(1)}
.paper{display:grid;gap:2rem}
@media (min-width:58rem){.paper{grid-template-columns:1fr 19rem;gap:3rem}}
.story{max-width:42rem}
.story p{margin:0 0 1rem}
.story>p:first-of-type::first-letter{font-family:var(--serif);float:left;font-size:4.2rem;line-height:.85;padding:.35rem .5rem 0 0;font-weight:700;color:var(--accent)}
.story h2{font-family:var(--serif);font-size:clamp(1.35rem,3.2vw,1.7rem);line-height:1.2;margin:2rem 0 .6rem}
.pull{margin:1.8rem 0;padding:1rem 0;border-top:3px solid var(--rule);border-bottom:1px solid var(--rule);font-family:var(--serif);font-size:clamp(1.4rem,3.4vw,1.9rem);line-height:1.3}
.pull footer{font-family:var(--sans);font-size:.9rem;color:var(--muted);margin-top:.6rem}
.side{display:grid;gap:1.2rem;align-content:start}
.box{background:var(--box);border-top:4px solid var(--accent);padding:1rem}
.box h2{font-size:.875rem;letter-spacing:.12em;text-transform:uppercase;margin:0 0 .7rem}
.box p{margin:0 0 .7rem}
.nums{list-style:none;margin:0;padding:0;display:grid;gap:.7rem}
.nums b{display:block;font-family:var(--serif);font-size:2rem;line-height:1.05}
.src{font-size:.9rem;color:var(--muted)}
.cv{list-style:none;margin:0;padding:0}
.cv li{padding:.4rem 0;border-top:1px solid var(--line)}
.cv span{display:block;font-size:.9rem;color:var(--muted)}
.btn{display:inline-flex;align-items:center;min-height:44px;padding:.55rem 1rem;font-weight:650;text-decoration:none;border:1.5px solid var(--accent);border-radius:2px}
.btn.main{background:var(--accent);color:var(--accent-ink)}
.btns{display:flex;flex-wrap:wrap;gap:.6rem}
.open{list-style:none;margin:0;padding:0;display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,14rem),1fr));border-top:3px double var(--rule);padding-top:1rem}
.open strong{display:block;font-family:var(--serif);font-size:1.1rem}
.end{border-top:1px solid var(--line);margin:2.5rem 0;padding-top:1.2rem;max-width:42rem}
"""

BODY = f"""<main id="main">
<p class="mast"><strong>Founder stories</strong><span>From Kate's own profile and posts</span></p>
<article>
<header>
  <p class="kicker">Specialist to founder</p>
  <h1>The legal transcriber who built her own platform</h1>
  <p class="stand">Kate Curtis&#8209;Evans still transcribes for legal professionals every day. With no outside funding and no traditional tech background, she built Audio Genius, and now she is looking for a technical co-founder.</p>
  <p class="who"><b>Kate Curtis&#8209;Evans</b>, Founder, Audio Genius. Based in the United Kingdom.</p>
</header>
{photo(cls="lead", sizes="(min-width:70rem) 68rem, 100vw")}
<div class="paper">
  <div class="story">
    <p>Kate has spent six years transcribing for legal professionals across the UK, and she still does the work every day. She kept seeing the same problem: most transcription technology is built for organisations processing audio, or for people capturing their own meetings. Very little of it is designed around the person producing the finished transcript from someone else's audio, with multiple speakers, difficult recordings, exacting standards, confidentiality requirements and deadline pressure.</p>
    <p>So she built what she wanted to use herself. She taught herself to build with vibe coding and AI tools, and learnt to test properly before anything goes live.</p>
    <blockquote class="pull">&ldquo;I'm not a tech founder guessing at what professional transcribers need. I am one, and that's the difference.&rdquo;<footer>Kate, on her LinkedIn profile</footer></blockquote>
    <h2>The product</h2>
    <p>Audio Genius is an ASR-powered legal transcription and workflow platform designed around human-led transcription. The technology does the heavy lifting, but the professional keeps control. Because legal audio can hold highly sensitive information, Kate treats security, confidentiality and responsible data handling as fundamental, not features to bolt on later.</p>
    <p>It is being developed with feedback from real transcription professionals, and some of the best ideas for the platform have come directly from the people testing it. It now has paying users, and not one of those who signed up at the end of the beta has left. They use it every day.</p>
    <h2>Foundations first</h2>
    <p>Kate has stopped adding new features on purpose, including a legal glossary and template uploads she was looking forward to building. What comes first is the part nobody sees: privacy and data protection, working through what the platform holds and how long it keeps it, one decision at a time.</p>
    <h2>Wanted: a technical co-founder</h2>
    <p>The platform Kate built Audio Genius on will not let Kate fork a test site from the live one, and gives her limited control over hosting and other parts of the build. She wants to own how it scales. The next stage is moving to a tech stack built for regulated data and getting certifications like Cyber Essentials in place. That is the work she wants a partner to own, ideally someone with legal tech or regulated-industry experience.</p>
    <p>Kate brings the vision for the platform, direct access to users, research and results, and a strategy for expanding into corporates and organisations. The co-founder would own the technical scope, the build, integration and implementation.</p>
    <p>If that is you, message her. If you know who it is, send her an introduction.</p>
    <p class="btns"><a class="btn main" href="{LI}">Message Kate on LinkedIn</a><a class="btn" href="{AG}">Visit audio-genius.com</a></p>
  </div>
  <aside class="side" aria-label="At a glance">
    <section class="box" aria-labelledby="n-h"><h2 id="n-h">Where it stands, in Kate's words</h2>
      <ul class="nums">
        <li><b>50</b>testers in a 90-day beta</li>
        <li><b>34,000</b>minutes of audio transcribed since launch in September</li>
        <li><b>1,200</b>website visits, from Google, social media and elsewhere, with no paid advertising as yet</li>
      </ul>
      <p class="src" style="margin-top:.8rem">Bootstrapped and pre-seed. Figures exactly as Kate stated them in her LinkedIn post looking for a technical co-founder, as given to this site on 20 November 2026.</p>
    </section>
    <section class="box" aria-labelledby="cv-h"><h2 id="cv-h">Her record</h2>
      <ul class="cv">
        <li>Founder, Audio Genius<span>Nov 2025 to now</span></li>
        <li>Transcription Specialist (Legal and Professional)<span>Mar 2021 to now</span></li>
        <li>Legal Transcriber, eScribers<span>2022 to now</span></li>
        <li>Freelance Transcriber, Ubiqus<span>2021 to 2022</span></li>
        <li>BA in European Business Studies, Brunel University of London<span>1992 to 1996</span></li>
      </ul>
    </section>
  </aside>
</div>
</article>
<section aria-labelledby="open-h" style="margin-top:2.5rem">
  <h2 id="open-h" class="kicker">Also open to collaborations, partnerships and investment</h2>
  <ul class="open">
    <li><strong>Law firms and agencies</strong>Exploring secure transcription and workflow technology for in-house teams and freelancer networks.</li>
    <li><strong>Transcribers and legal professionals</strong>Who want to help shape the technology they will actually use.</li>
    <li><strong>Investors</strong>Interested in vertical SaaS built from genuine domain expertise and a clearly identified industry problem.</li>
    <li><strong>Partners</strong>LegalTech, speech technology and security partners who understand the technical and compliance challenges of handling professional and legal audio.</li>
  </ul>
</section>
<section class="end" aria-labelledby="c-h">
  <h2 id="c-h" style="font-family:var(--serif);margin:0 0 .5rem">Kate would love to connect</h2>
  <p>She is building Audio Genius publicly and sharing what she learns along the way, from transcription and ASR to product development, security, LegalTech and becoming a software founder without a traditional technology background.</p>
  <p class="btns"><a class="btn main" href="{LI}">LinkedIn</a><a class="btn" href="{AG}">audio-genius.com</a></p>
</section>
</main>"""

open('newsroom.html', 'w').write(page(6, "The Newsroom", "The Newsroom, Kate Curtis-Evans", TOK, CSS, BODY).replace("Design 6 of 5, The Newsroom.", "Design: The Newsroom."))

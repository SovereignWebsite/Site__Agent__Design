from shell import *

TOK = """:root{--bg:#f2f0eb;--card:#ffffff;--fg:#1d1c1a;--muted:#55524b;--accent:#2b5a87;--accent-ink:#fff;--line:#dcd8cf;--edge:#8b877d;--hold:#7a4b00;--done:#2f6b3a}
@media (prefers-color-scheme:dark){:root{--bg:#151619;--card:#1f2126;--fg:#ecebe8;--muted:#aaa79f;--accent:#8db9e8;--accent-ink:#0b1a2a;--line:#33363d;--edge:#7d8089;--hold:#f0b866;--done:#8fd19c}}"""

CSS = """
main{max-width:80rem;margin:0 auto;padding:0 1rem}
.head{display:grid;gap:1.2rem;padding:2rem 0 1.5rem;align-items:center}
@media (min-width:56rem){.head{grid-template-columns:1fr 22rem;padding:3rem 0 2rem;gap:3rem}}
.counts{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:.5rem}
.counts a{display:flex;align-items:center;min-height:44px;padding:.4rem .8rem;background:var(--card);border:1px solid var(--edge);border-radius:8px;text-decoration:none;color:var(--fg);font-weight:650}
.counts li:last-child a{border:2px dashed var(--accent);color:var(--accent)}
.eyebrow{font-size:.875rem;font-weight:650;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);margin:0 0 .5rem}
h1{font-family:var(--serif);font-weight:700;font-size:clamp(2.3rem,6.5vw,3.6rem);line-height:1.05;margin:0 0 .7rem}
.lede{font-family:var(--serif);font-size:clamp(1.15rem,2.4vw,1.4rem);line-height:1.4;margin:0 0 .8rem;max-width:36rem}
.btns{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem}
.btn{display:inline-flex;align-items:center;min-height:44px;padding:.55rem 1rem;border-radius:8px;font-weight:650;text-decoration:none;border:1.5px solid var(--accent)}
.btn.main{background:var(--accent);color:var(--accent-ink)}
.photo img{border-radius:10px}
.photo figcaption{font-size:.875rem;color:var(--muted);margin-top:.35rem}
.boardh{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:.4rem 1rem;border-top:1px solid var(--line);padding-top:1.4rem}
h2{font-family:var(--serif);font-size:clamp(1.45rem,3.6vw,2rem);line-height:1.2;margin:0}
.boardh p{margin:0;color:var(--muted);font-size:.95rem}
.board{display:grid;gap:1rem;margin:1rem 0 2.5rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,17rem),1fr));align-items:start}
.lane{background:color-mix(in srgb,var(--card) 45%,var(--bg));border:1px solid var(--line);border-radius:12px;padding:.7rem}
.lane h3{display:flex;justify-content:space-between;font-size:.95rem;letter-spacing:.06em;text-transform:uppercase;margin:.2rem .3rem .7rem}
.lane h3 span{font-weight:500;color:var(--muted);letter-spacing:0}
.cards{list-style:none;margin:0;padding:0;display:grid;gap:.6rem}
.card{background:var(--card);border:1px solid var(--edge);border-radius:8px;padding:.7rem .8rem;font-size:.98rem;line-height:1.45}
.card b{display:block;font-size:1rem;margin-bottom:.15rem}
.tag{display:inline-block;font-size:.875rem;font-weight:650;border:1.5px solid currentColor;border-radius:999px;padding:0 .5rem;margin-bottom:.35rem}
.t-done{color:var(--done)}.t-hold{color:var(--hold)}.t-run{color:var(--accent)}.t-open{color:var(--fg)}
.when{display:block;color:var(--muted);font-size:.9rem;margin-top:.2rem}
.card.wanted{border:2px dashed var(--accent);padding:1rem}
.card.wanted b{font-family:var(--serif);font-size:1.4rem}
.card.wanted p{margin:.5rem 0}
.card .n{display:block;font-family:var(--serif);font-size:1.8rem;font-weight:700;line-height:1.1}
.below{display:grid;gap:2rem;border-top:1px solid var(--line);padding:2rem 0}
@media (min-width:56rem){.below{grid-template-columns:1fr 1fr;gap:3rem}}
.below p{margin:0 0 .9rem;max-width:40rem}
blockquote{margin:1rem 0;padding-left:1rem;border-left:3px solid var(--accent);font-family:var(--serif);font-size:1.25rem;line-height:1.45}
blockquote footer{font-family:var(--sans);font-size:.9rem;color:var(--muted)}
.src{font-size:.9rem;color:var(--muted)}
.contact{border-top:1px solid var(--line);padding:2rem 0 2.5rem;max-width:44rem}
"""

def card(tag, tcls, title, text="", when="", extra=""):
    return f'<li class="card"><span class="tag {tcls}">{tag}</span><b>{title}</b>{text}{f"<span class=when>{when}</span>" if when else ""}{extra}</li>'

BODY = f"""<main id="main">
<header class="head">
  <div>
    <p class="eyebrow">Founder, Audio Genius</p>
    <h1>Kate Curtis&#8209;Evans</h1>
    <p class="lede">A practising legal transcriber who built a live transcription platform without knowing how to code.</p>
    <p>Audio Genius is legal transcription and workflow management, built by a transcriber, for transcription professionals. Kate is based in the United Kingdom and is now looking for a technical co-founder.</p>
    <div class="btns"><a class="btn main" href="#wanted">The open job: technical co-founder</a><a class="btn" href="{AG}">Visit audio-genius.com</a></div>
  </div>
  <ul class="counts" aria-label="The board at a glance"><li><a href="#lane-done">Delivered 4</a></li><li><a href="#lane-run">In progress 4</a></li><li><a href="#lane-hold">On hold 2</a></li><li><a href="#wanted">Unassigned 2</a></li></ul>
</header>

<section aria-labelledby="board-h">
<div class="boardh"><h2 id="board-h">Kate's work, as a workflow board</h2><p>Audio Genius manages transcription work. Here is Kate's own.</p></div>
<div class="board">
  <div class="lane" id="lane-done"><h3>Delivered <span>4</span></h3><ul class="cards">
    {card("Delivered","t-done","BA in European Business Studies","Brunel University of London.","1992 to 1996")}
    {card("Delivered","t-done","Freelance Transcriber, Ubiqus","","2021 to 2022")}
    {card("Delivered","t-done","A 90-day beta",'<span class="n">50</span>testers.')}
    {card("Delivered","t-done","Launch in September",'<span class="n">34,000</span>minutes of audio transcribed since.')}
  </ul></div>
  <div class="lane" id="lane-run"><h3>In progress <span>4</span></h3><ul class="cards">
    {card("Every day","t-run","Transcription Specialist (Legal and Professional)","Secure, human-led transcription for legal and professional clients, with confidential handling: no AI tools used for sensitive material.","Mar 2021 to now")}
    {card("Every day","t-run","Legal Transcriber, eScribers","Professional legal transcription focused on accuracy, consistency and careful handling of sensitive material.","2022 to now")}
    {card("In progress","t-run","Founder, Audio Genius","A secure transcription workspace designed to support professional transcription workflows. It now has paying users, and not one of those who signed up at the end of the beta has left.","Nov 2025 to now")}
    {card("Comes first","t-run","Foundations: privacy and data protection","Working through what the platform holds and how long it keeps it, one decision at a time.")}
  </ul></div>
  <div class="lane" id="lane-hold"><h3>On hold, on purpose <span>2</span></h3><ul class="cards">
    {card("On hold","t-hold","Legal glossary","A feature Kate was looking forward to building.")}
    {card("On hold","t-hold","Template uploads","Paused so that the part nobody sees comes first.")}
  </ul></div>
  <div class="lane" id="wanted"><h3>Unassigned <span>2</span></h3><ul class="cards">
    <li class="card wanted"><span class="tag t-open">Open</span><b>Technical co-founder</b>
      <p>The platform Kate built Audio Genius on will not let Kate fork a test site from the live one, and gives her limited control over hosting and other parts of the build. She wants to own how it scales.</p>
      <p><strong>Kate brings</strong> the vision for the platform, direct access to users, research and results, and a strategy for expanding into corporates and organisations.</p>
      <p><strong>The co-founder would own</strong> the technical scope, the build, integration and implementation. Ideally someone with legal tech or regulated-industry experience.</p>
      <p><a class="btn main" href="{LI}">Message Kate on LinkedIn</a></p>
      <p class="src">If you know who it is, send her an introduction.</p></li>
    {card("Waiting for the co-founder","t-open","A stack for regulated data","Moving to a tech stack built for regulated data and getting certifications like Cyber Essentials in place.")}
  </ul></div>
</div>
</section>

<section class="below" aria-labelledby="story-h">
  <div>
    {photo(sizes="(min-width:56rem) 30rem, 100vw", lazy=True)}
    <h2 id="story-h" style="margin-top:1.2rem">Built by someone who does the work</h2>
    <p>Kate has spent six years transcribing for legal professionals across the UK, and she still does the work every day. She kept seeing the same problem: most transcription technology is built for organisations processing audio, or for people capturing their own meetings. Very little of it is designed around the person producing the finished transcript from someone else's audio, with multiple speakers, difficult recordings, exacting standards, confidentiality requirements and deadline pressure.</p>
    <p>So she built what she wanted to use herself, with no outside funding and no traditional tech background. She taught herself to build with vibe coding and AI tools, and learnt to test properly before anything goes live.</p>
    <blockquote>&ldquo;I'm not a tech founder guessing at what professional transcribers need. I am one, and that's the difference.&rdquo;<footer>Kate, on her LinkedIn profile</footer></blockquote>
  </div>
  <div>
    <h2>Audio Genius</h2>
    <p>Audio Genius is an ASR-powered legal transcription and workflow platform designed around human-led transcription. The technology does the heavy lifting, but the professional keeps control. Because legal audio can hold highly sensitive information, Kate treats security, confidentiality and responsible data handling as fundamental, not features to bolt on later.</p>
    <p>It is being developed with feedback from real transcription professionals, and some of the best ideas for the platform have come directly from the people testing it. It has had 1,200 website visits, from Google, social media and elsewhere, with no paid advertising as yet. Audio Genius is bootstrapped and pre-seed.</p>
    <p class="src">Figures exactly as Kate stated them in her LinkedIn post looking for a technical co-founder, as given to this site on 20 November 2026.</p>
  </div>
</section>

<section aria-labelledby="req-h">
<div class="boardh"><h2 id="req-h">Incoming requests Kate welcomes</h2><p>Collaborations, partnerships and investment.</p></div>
<div class="board"><ul class="cards" style="display:contents">
  {card("Welcome","t-open","Law firms and agencies","Exploring secure transcription and workflow technology for in-house teams and freelancer networks.")}
  {card("Welcome","t-open","Transcribers and legal professionals","Who want to help shape the technology they will actually use.")}
  {card("Welcome","t-open","Investors","Interested in vertical SaaS built from genuine domain expertise and a clearly identified industry problem.")}
  {card("Welcome","t-open","Partners","LegalTech, speech technology and security partners who understand the technical and compliance challenges of handling professional and legal audio.")}
</ul></div>
</section>

<section class="contact" aria-labelledby="c-h">
  <h2 id="c-h">Kate would love to connect</h2>
  <p>She is building Audio Genius publicly and sharing what she learns along the way, from transcription and ASR to product development, security, LegalTech and becoming a software founder without a traditional technology background.</p>
  <div class="btns"><a class="btn main" href="{LI}">LinkedIn</a><a class="btn" href="{AG}">audio-genius.com</a></div>
</section>
</main>"""

open('../designs/3.html', 'w').write(page(3, "The Workflow Board", "The Workflow Board, Kate Curtis-Evans", TOK, CSS, BODY))

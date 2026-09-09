# -*- coding: utf-8 -*-
from build import page

PAGE_BODIES = {}

ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_PHONE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M6.6 10.8C8 13.6 10.4 16 13.2 17.4L15.4 15.2C15.7 14.9 16.1 14.8 16.5 14.9C17.7 15.3 19 15.5 20.3 15.5C20.9 15.5 21.3 15.9 21.3 16.5V20.3C21.3 20.9 20.9 21.3 20.3 21.3C10.7 21.3 2.7 13.3 2.7 3.7C2.7 3.1 3.1 2.7 3.7 2.7H7.5C8.1 2.7 8.5 3.1 8.5 3.7C8.5 5 8.7 6.3 9.1 7.5C9.2 7.9 9.1 8.3 8.8 8.6L6.6 10.8Z" stroke="#F9F9F9" stroke-width="1.6"/></svg>'
ICON_MAIL = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M3 6.5L12 13L21 6.5" stroke="#F9F9F9" stroke-width="1.6" stroke-linecap="round"/><rect x="3" y="4.5" width="18" height="15" rx="2" stroke="#F9F9F9" stroke-width="1.6"/></svg>'
ICON_PIN = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 21C12 21 19 14.6 19 9.8C19 5.9 15.9 3 12 3C8.1 3 5 5.9 5 9.8C5 14.6 12 21 12 21Z" stroke="#F9F9F9" stroke-width="1.6"/><circle cx="12" cy="9.6" r="2.6" stroke="#F9F9F9" stroke-width="1.6"/></svg>'

def word_spans(text, base_delay=0):
    words = text.split(" ")
    out = []
    for i, w in enumerate(words):
        out.append(f'<span class="hero-word"><span style="animation-delay:{base_delay + i*70}ms">{w}</span></span>')
    return " ".join(out)

# =========================================================
# HOME
# =========================================================
index_body = f"""
<section class="hero">
  <div class="hero-media">
    <video autoplay muted loop playsinline poster="assets/img/hero-poster.jpg">
      <source src="assets/video/hero-loop.webm" type="video/webm">
      <source src="assets/video/hero-loop.mp4" type="video/mp4">
    </video>
  </div>
  <button class="video-toggle" aria-label="Zaustavi/pokreni video"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><rect x="6" y="4" width="4" height="16" rx="1" fill="#F9F9F9"/><rect x="14" y="4" width="4" height="16" rx="1" fill="#F9F9F9"/></svg></button>
  <div class="hero-inner container">
    <span class="eyebrow">Od 1994.</span>
    <h1>{word_spans("Mjesto gdje nastaju borci")}</h1>
    <p class="lede">Klub SV. Matej nudi jedinstven pristup treninzima kickboxinga, MMA-a i ženske rekreacije. Kombiniramo dugogodišnju tradiciju i stručnost s modernim metodama, pružajući iskustvo koje jača tijelo i duh.</p>
    <div class="hero-actions">
      <a href="#programi" class="btn btn-primary">Pogledaj termine treninga</a>
    </div>
  </div>
  <div class="scroll-cue"><i></i></div>
</section>

<div class="marquee">
  <div class="marquee-track">
    <span>DISCIPLINA <b>&bull;</b> SNAGA <b>&bull;</b> ZAJEDNIŠTVO <b>&bull;</b> POŠTOVANJE <b>&bull;</b> POBJEDNIČKI MENTALITET <b>&bull;</b> OD 1994. <b>&bull;</b></span>
    <span aria-hidden="true">DISCIPLINA <b>&bull;</b> SNAGA <b>&bull;</b> ZAJEDNIŠTVO <b>&bull;</b> POŠTOVANJE <b>&bull;</b> POBJEDNIČKI MENTALITET <b>&bull;</b> OD 1994. <b>&bull;</b></span>
  </div>
</div>

<section>
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Tko smo mi</span>
        <h2 style="margin-top:.8rem;">Više od 30 godina gradimo sportaše i karakter</h2>
        <p class="text-body" style="margin-top:1.2rem;">Kickboxing klub Sveti Matej osnovan je 1994. godine od strane Dragana Majkića, vrhunskog i iznimno iskusnog trenera s bogatim međunarodnim rezultatima. Naš klub je mjesto gdje se razvijaju snaga, samopouzdanje i pobjednički mentalitet, bez obzira trenirate li rekreativno ili natjecateljski.</p>
        <a href="o-nama.html" class="btn btn-ghost" style="margin-top:1.6rem;">Više o nama {ARROW}</a>
        <div class="stats">
          <div class="stat"><b data-count="1994" data-suffix="">0</b><span>Godina osnutka</span></div>
          <div class="stat"><b data-count="30" data-suffix="+">0</b><span>Godina iskustva</span></div>
        </div>
      </div>
      <div class="reveal figure-frame" style="transition-delay:120ms;width:114%;margin:-2rem -8% 0 auto;">
        <img src="assets/img/team-group-lg.jpg" alt="Članovi kluba KBK Sveti Matej okupljeni u dvorani">
      </div>
    </div>
  </div>
</section>

<section id="programi" style="background:var(--black-2);border-top:1px solid rgba(249,249,249,.08);border-bottom:1px solid rgba(249,249,249,.08);">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Naši treninzi</span>
      <h2>Trening za svaki uzrast i cilj</h2>
      <p class="lede">Od prvih koraka u borilačkim sportovima do natjecateljske pripreme, odaberi trening koji ti odgovara.</p>
    </div>
    <div class="prog-grid stagger">
      <a class="prog-card reveal" style="--i:0" href="kickboxing-djeca.html">
        <span class="tag">7 – 15 godina</span>
        <img src="assets/img/card-djeca-lg.jpg" alt="Kickboxing trening za djecu i mlađe kadete">
        <div class="body">
          <span>Kickboxing</span>
          <h3>Djeca i mlađi kadeti</h3>
          <span class="arrow">Saznaj više {ARROW}</span>
        </div>
      </a>
      <a class="prog-card reveal" style="--i:1" href="kickboxing-16.html">
        <span class="tag">16+ godina</span>
        <img src="assets/img/card-16-lg.jpg" alt="Kickboxing trening za starije kadete, juniore i seniore">
        <div class="body">
          <span>Kickboxing</span>
          <h3>Stariji kadeti, juniori i seniori</h3>
          <span class="arrow">Saznaj više {ARROW}</span>
        </div>
      </a>
      <a class="prog-card reveal" style="--i:2" href="mma.html">
        <span class="tag">16+ godina</span>
        <img src="assets/img/card-mma-lg.jpg" alt="MMA sparing trening">
        <div class="body">
          <span>MMA</span>
          <h3>Stariji kadeti, juniori i seniori</h3>
          <span class="arrow">Saznaj više {ARROW}</span>
        </div>
      </a>
      <a class="prog-card reveal" style="--i:3" href="zenska-rekreacija.html">
        <span class="tag">Svi uzrasti</span>
        <img src="assets/img/card-zenska-lg.jpg" alt="Ženska rekreacija trening">
        <div class="body">
          <span>Rekreacija</span>
          <h3>Ženska rekreacija</h3>
          <span class="arrow">Saznaj više {ARROW}</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section id="raspored">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Raspored treninga</span>
      <h2>Tjedni raspored svih treninga</h2>
      <p class="lede">Dođi isprobati trening besplatno. Pronađi termin koji ti odgovara.</p>
    </div>
    <div class="week-grid stagger">
      <div class="week-card reveal" style="--i:0">
        <div class="wc-head"><h4>Kickboxing 7–15</h4><span class="pill">Djeca</span></div>
        <ul data-schedule="kb-djeca">
          <li><span>Ponedjeljak</span><b>20:00h</b></li>
          <li><span>Srijeda</span><b>20:00h</b></li>
          <li><span>Petak</span><b>20:00h</b></li>
        </ul>
        <a href="kickboxing-djeca.html" class="btn btn-ghost">Detalji treninga</a>
      </div>
      <div class="week-card reveal" style="--i:1">
        <div class="wc-head"><h4>Kickboxing 16+</h4><span class="pill">Juniori/seniori</span></div>
        <ul>
          <li><span>Pon / Sri / Pet</span><b>21:00h</b></li>
          <li><span>Utorak / Četvrtak</span><b>20:00h</b></li>
          <li><span>Subota</span><b>po dogovoru</b></li>
        </ul>
        <a href="kickboxing-16.html" class="btn btn-ghost">Detalji treninga</a>
      </div>
      <div class="week-card reveal" style="--i:2">
        <div class="wc-head"><h4>MMA</h4><span class="pill">16+</span></div>
        <ul>
          <li><span>Utorak</span><b>21:00h</b></li>
          <li><span>Četvrtak</span><b>21:00h</b></li>
          <li><span>Subota</span><b>po dogovoru</b></li>
        </ul>
        <a href="mma.html" class="btn btn-ghost">Detalji treninga</a>
      </div>
      <div class="week-card reveal" style="--i:3">
        <div class="wc-head"><h4>Ženska rekreacija</h4><span class="pill">Svi uzrasti</span></div>
        <ul>
          <li><span>Ponedjeljak</span><b>19:00h</b></li>
          <li><span>Srijeda</span><b>19:00h</b></li>
          <li><span>Petak</span><b>19:00h</b></li>
        </ul>
        <a href="zenska-rekreacija.html" class="btn btn-ghost">Detalji treninga</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Iz dvorane</span>
      <h2>Rad, disciplina i zajedništvo</h2>
    </div>
    <div class="gallery reveal">
      <img src="assets/img/gallery-4038-md.jpg" alt="Trening u dvorani" loading="lazy">
      <img src="assets/img/pads-sparring-md.jpg" alt="Sparing na labavicama" loading="lazy">
      <video src="assets/video/gallery-c0190.mp4" poster="assets/img/gallery-c0190-poster.jpg" autoplay muted loop playsinline></video>
      <img src="assets/img/gallery-00962-md.jpg" alt="Boksačke rukavice" loading="lazy">
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div>
      <h2>Spreman/na za <span class="accent">prvi trening</span>?</h2>
      <p>Javi nam se telefonom ili e-mailom. Dogovaramo besplatan probni termin za sve treninge.</p>
    </div>
    <a href="#kontakt" class="btn btn-ghost">Kontaktiraj nas {ARROW}</a>
  </div>
</section>

<section id="kontakt">
  <div class="container">
    <div class="contact-grid">
      <div class="reveal">
        <span class="eyebrow">Kontakt</span>
        <h2 style="margin-top:.8rem;">Stojimo Vam na raspolaganju za sva Vaša pitanja</h2>
        <div class="contact-list">
          <div class="contact-item"><span class="ic">{ICON_PHONE}</span><div><small>Telefon</small><a href="tel:+385993130725">+385 99 3130 725</a></div></div>
          <div class="contact-item"><span class="ic">{ICON_MAIL}</span><div><small>E-mail</small><a href="mailto:majk1@net.hr">majk1@net.hr</a></div></div>
          <div class="contact-item"><span class="ic">{ICON_PIN}</span><div><small>Adresa</small><span>Vozišće 5, 51216 Viškovo</span></div></div>
        </div>
      </div>
      <div class="reveal map-frame" style="transition-delay:120ms;">
        <iframe src="https://www.google.com/maps?q=Vozi%C5%A1%C4%87e%205,%2051216%20Vi%C5%A1kovo&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Lokacija kluba na karti"></iframe>
      </div>
    </div>
  </div>
</section>
"""

page(
    title="KBK Sveti Matej Viškovo · Kickboxing, MMA i ženska rekreacija",
    desc="Kickboxing klub Sveti Matej u Viškovu od 1994. godine. Treninzi kickboxinga, MMA-a i ženske rekreacije za djecu, mlade i odrasle. Pridruži se timu!",
    slug="index.html",
    active="index.html",
    body=index_body,
    og_image="assets/img/heavybag-action-lg.jpg",
)
PAGE_BODIES["index.html"] = index_body
print("index built")

# =========================================================
# O NAMA
# =========================================================
onama_body = f"""
<section class="mini-hero">
  <div class="mini-hero-bg"><img src="assets/img/hero-onama-lg.jpg" alt=""></div>
  <div class="mini-hero-inner container">
    <span class="eyebrow">O klubu</span>
    <h1 style="font-size:clamp(2.4rem,7vw,4.4rem);margin-top:.7rem;">O nama</h1>
    <p class="lede" style="margin-top:1rem;">Kickboxing klub Sveti Matej nije samo klub: to je zajednica koja stvara pobjednike u sportu i životu.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Naša priča</span>
        <h2 style="margin-top:.8rem;">Mjesto gdje nastaju borci</h2>
        <p class="text-body" style="margin-top:1.2rem;">Kickboxing klub Sveti Matej osnovan je 1994. godine od strane Dragana Majkića, vrhunskog i iznimno iskusnog trenera s bogatim međunarodnim rezultatima. Njegovo nemjerljivo iskustvo i predanost sportu oblikovali su klub kao sinonim za kvalitetu, disciplinu i vrhunski rad.</p>
        <p class="text-body" style="margin-top:1rem;">Više od 30 godina gradimo sportaše i karakter. Naš klub je mjesto gdje se razvijaju snaga, samopouzdanje i pobjednički mentalitet, bez obzira trenirate li rekreativno ili natjecateljski.</p>
      </div>
      <div class="reveal figure-frame" style="transition-delay:120ms;">
        <img src="assets/img/pads-sparring-lg.jpg" alt="Sparing trening u dvorani kluba">
      </div>
    </div>
  </div>
</section>

<section style="background:var(--black-2);border-top:1px solid rgba(249,249,249,.08);border-bottom:1px solid rgba(249,249,249,.08);">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Naš tim</span>
      <h2>Stručni tim s vrhunskim borilačkim iskustvom</h2>
    </div>
    <div class="coach-grid stagger">
      <div class="coach-card reveal" style="--i:0">
        <div class="coach-avatar">DM</div>
        <div>
          <h4>Dragan Majkić</h4>
          <span class="role">Osnivač</span>
          <p class="text-body">Osnovao je klub 1994. godine. Nadzire sve treninge i osobno vodi žensku rekreaciju, fokusirajući se na fleksibilnost, kondiciju i zabavu.</p>
        </div>
      </div>
      <div class="coach-card reveal" style="--i:1">
        <div class="coach-avatar">ZM</div>
        <div>
          <h4>Zoran Majkić</h4>
          <span class="role">Glavni trener &middot; Kickboxing</span>
          <p class="text-body">Borac sa svjetskim rezultatima. Vodi sve treninge kickboxinga, kombinirajući tehniku i kondiciju za zdrav i aktivan život.</p>
        </div>
      </div>
      <div class="coach-card reveal" style="--i:2">
        <div class="coach-avatar">RB</div>
        <div>
          <h4>Roko Benić</h4>
          <span class="role">Trener &middot; Djeca i mlađi kadeti</span>
          <p class="text-body">Državni prvak u K1 i low kick disciplini, osvajač bronce na Svjetskom prvenstvu u Abu Dhabiju. Uz Zorana Majkića vodi najmlađe članove, radeći na tehnici, snazi i koordinaciji.</p>
        </div>
      </div>
      <div class="coach-card reveal" style="--i:3">
        <div class="coach-avatar">MK</div>
        <div>
          <h4>Manuel Karić</h4>
          <span class="role">Trener &middot; MMA</span>
          <p class="text-body">Bivši profesionalni MMA borac. Vodi MMA treninge za napredne borce i natjecatelje, razvijajući izdržljivost i mentalnu otpornost.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split rev">
      <div class="reveal">
        <img src="assets/img/dvorana-lg.jpg" alt="Dvorana kluba KBK Sveti Matej">
      </div>
      <div class="reveal" style="transition-delay:120ms;">
        <span class="eyebrow">Dvorana</span>
        <h2 style="margin-top:.8rem;">Prostor za rad, disciplinu i razvoj</h2>
        <p class="text-body" style="margin-top:1.2rem;">Naša dvorana predstavlja središte rada, discipline i sportskog razvoja. Prostor je osmišljen tako da zadovolji potrebe kako rekreativaca, tako i vrhunskih natjecatelja, uz naglasak na sigurnost, funkcionalnost i kvalitetu treninga. Opremljena je suvremenom opremom koja omogućuje razvoj snage, izdržljivosti, tehnike i kondicije.</p>
        <p class="text-body" style="margin-top:1rem;">Treninzi se odvijaju pod stručnim vodstvom, u poticajnoj atmosferi koja potiče napredak, zajedništvo i sportski duh. Ovo je mjesto gdje se stvaraju borci, ali i ljudi kroz rad, poštovanje i kontinuirano pomicanje vlastitih granica.</p>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--black-2);border-top:1px solid rgba(249,249,249,.08);">
  <div class="container">
    <div class="section-head reveal center">
      <span class="eyebrow center">Naše vrijednosti</span>
      <h2>Snažni. Fokusirani. Motivirajući. Profesionalni.</h2>
    </div>
    <ul class="value-list reveal">
      <li><span class="num">01</span><b>Disciplina</b></li>
      <li><span class="num">02</span><b>Poštovanje</b></li>
      <li><span class="num">03</span><b>Upornost</b></li>
      <li><span class="num">04</span><b>Zajedništvo</b></li>
      <li><span class="num">05</span><b>Strast</b></li>
    </ul>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div>
      <h2>Postani <span class="accent">dio priče</span></h2>
      <p>Bilo da želite naučiti borilačke vještine, poboljšati kondiciju ili se rekreirati, imamo trening za vas.</p>
    </div>
    <a href="index.html#kontakt" class="btn btn-ghost">Kontaktiraj nas {ARROW}</a>
  </div>
</section>
"""

page(
    title="O nama · KBK Sveti Matej Viškovo",
    desc="Kickboxing klub Sveti Matej osnovan je 1994. godine. Upoznajte našu priču, trenere i dvoranu u Viškovu.",
    slug="o-nama.html",
    active="o-nama.html",
    body=onama_body,
    og_image="assets/img/hero-onama-lg.jpg",
)
PAGE_BODIES["o-nama.html"] = onama_body
print("o-nama built")

# =========================================================
# PROGRAM PAGE TEMPLATE
# =========================================================
def program_page(slug, nav_active, title_html, age_range, eyebrow, hero_img, lede,
                  coach_name, coach_role, coach_bio, schedule_rows, focus_items,
                  crosslinks, desc, og_image, hero_pos="50% 50%"):
    sched_html = ""
    for i, (day, time, sub) in enumerate(schedule_rows):
        day_key = {
            "Ponedjeljak":"ponedjeljak","Utorak":"utorak","Srijeda":"srijeda",
            "Četvrtak":"cetvrtak","Petak":"petak","Subota":"subota","Nedjelja":"nedjelja"
        }.get(day, "")
        sub_html = f"<small>{sub}</small>" if sub else ""
        sched_html += f"""<div class="schedule-row" data-day="{day_key}">
          <div class="day">{day}{sub_html}</div>
          <div class="time">{time}</div>
        </div>\n"""

    focus_html = ""
    for i, (n, h, p) in enumerate(focus_items):
        focus_html += f"""<div class="focus-item reveal" style="--i:{i}">
          <span class="n">{n}</span><h4>{h}</h4><p>{p}</p>
        </div>\n"""

    cross_html = ""
    for href, label in crosslinks:
        cross_html += f'<a class="crosslink" href="{href}">{label} {ARROW}</a>\n'

    body = f"""
<section class="mini-hero">
  <div class="mini-hero-bg"><img src="assets/img/{hero_img}-lg.jpg" alt="" style="object-position:{hero_pos};"></div>
  <div class="mini-hero-inner container">
    <span class="eyebrow">{eyebrow}</span>
    <div class="age-badge">Uzrast: <b>{age_range}</b></div>
    <h1 style="font-size:clamp(2.2rem,6.4vw,4rem);">{title_html}</h1>
    <p class="lede" style="margin-top:1rem;">{lede}</p>
    <div class="hero-actions" style="margin-top:1.6rem;">
      <a href="index.html#kontakt" class="btn btn-primary">Prijavi se na trening</a>
      <a href="#raspored" class="btn btn-ghost">Pogledaj raspored</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Vodi trening</span>
        <h2 style="margin-top:.8rem;">{coach_name}</h2>
        <span class="pill" style="margin-top:.9rem;display:inline-flex;">{coach_role}</span>
        <p class="text-body" style="margin-top:1.2rem;">{coach_bio}</p>
        <div class="focus-grid stagger">
          {focus_html}
        </div>
      </div>
      <div class="reveal" id="raspored" style="transition-delay:120ms;">
        <span class="eyebrow">Raspored</span>
        <h3 style="margin:.8rem 0 1.2rem;">Termini treninga</h3>
        <div class="schedule">
          {sched_html}
        </div>
        <p class="text-body" style="margin-top:1rem;font-size:.82rem;">Svi termini održavaju se u dvorani kluba, Vozišće 5, Viškovo. Prvi dolazak najavite telefonom ili e-mailom.</p>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--black-2);border-top:1px solid rgba(249,249,249,.08);border-bottom:1px solid rgba(249,249,249,.08);">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Ostali treninzi</span>
      <h2>Istraži i druge treninge kluba</h2>
    </div>
    <div class="crosslinks reveal">
      {cross_html}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <div>
      <h2>Dođi na <span class="accent">besplatan probni trening</span></h2>
      <p>Javi nam se telefonom ili e-mailom i rezerviraj svoj termin.</p>
    </div>
    <a href="index.html#kontakt" class="btn btn-ghost">Kontaktiraj nas {ARROW}</a>
  </div>
</section>
"""
    page(title=title_html.replace("<br>"," ") + " · KBK Sveti Matej", desc=desc, slug=slug, active=slug, body=body, og_image=og_image)
    PAGE_BODIES[slug] = body
    print(slug, "built")


ALL_LINKS = [
    ("kickboxing-djeca.html", "Kickboxing · Djeca i mlađi kadeti"),
    ("kickboxing-16.html", "Kickboxing · Stariji kadeti, juniori, seniori"),
    ("mma.html", "MMA · 16+"),
    ("zenska-rekreacija.html", "Ženska rekreacija"),
]

def others(exclude):
    return [x for x in ALL_LINKS if x[0] != exclude]

program_page(
    slug="kickboxing-djeca.html",
    nav_active="kickboxing-djeca.html",
    title_html="Kickboxing djeca i mlađi kadeti",
    age_range="7 – 15 godina",
    eyebrow="Kickboxing",
    hero_img="hero-djeca",
    lede="Prvi koraci u kickboxingu: kroz igru i disciplinu djeca grade motoriku, samopouzdanje i poštovanje prema sportu.",
    coach_name="Zoran Majkić",
    coach_role="uz borca i trenera Roka Benića",
    coach_bio="Zoran Majkić, glavni trener kickboxinga, uz borca i trenera Roka Benića (državni prvak u K1 i low kick disciplini te osvajač bronce na Svjetskom prvenstvu u Abu Dhabiju) vodi najmlađe članove kluba, fokusirajući se na tehniku, snagu i koordinaciju.",
    schedule_rows=[("Ponedjeljak","20:00h",""),("Srijeda","20:00h",""),("Petak","20:00h","")],
    focus_items=[
        ("01","Tehnika i koordinacija","Osnove udaraca rukama i nogama kroz vježbe prilagođene dječjem uzrastu."),
        ("02","Disciplina i poštovanje","Izgradnja radnih navika, fokusa i poštovanja prema treneru i suigračima."),
        ("03","Igra i zabava","Motivirajuće vježbe koje grade ljubav prema sportu i timski duh."),
    ],
    crosslinks=others("kickboxing-djeca.html"),
    desc="Kickboxing za djecu i mlađe kadete (7-15 godina) u Viškovu. Tehnika, disciplina i zabava pod vodstvom Roka Benića i Zorana Majkića.",
    og_image="assets/img/gear-flatlay-lg.jpg",
)

program_page(
    slug="kickboxing-16.html",
    nav_active="kickboxing-16.html",
    title_html="Kickboxing stariji kadeti, juniori i seniori",
    age_range="16+ godina",
    eyebrow="Kickboxing",
    hero_img="hero-16",
    lede="Trening za sve koji žele napredovati: od rekreativaca do natjecatelja. Tehnika, kondicija i mentalna snaga u ravnoteži.",
    coach_name="Zoran Majkić",
    coach_role="Glavni trener kickboxinga",
    coach_bio="Zoran Majkić, borac sa svjetskim rezultatima, vodi sve treninge kickboxinga za starije kadete, juniore i seniore, kombinirajući tehniku i kondiciju za zdrav i aktivan život.",
    schedule_rows=[("Ponedjeljak","21:00h",""),("Utorak","20:00h",""),("Srijeda","21:00h",""),("Četvrtak","20:00h",""),("Petak","21:00h",""),("Subota","po dogovoru","")],
    focus_items=[
        ("01","Tehnika i snaga","Napredne kombinacije udaraca i sparing pod nadzorom trenera."),
        ("02","Kondicija","Visokointenzivni treninzi za snagu, izdržljivost i eksplozivnost."),
        ("03","Natjecateljski duh","Priprema za natjecanja uz mentorstvo borca sa svjetskim rezultatima."),
    ],
    crosslinks=others("kickboxing-16.html"),
    desc="Kickboxing za starije kadete, juniore i seniore (16+) u Viškovu. Trening pod vodstvom Zorana Majkića.",
    og_image="assets/img/heavybag-action-lg.jpg",
)

program_page(
    slug="mma.html",
    nav_active="mma.html",
    title_html="MMA stariji kadeti, juniori i seniori",
    age_range="16+ godina",
    eyebrow="MMA",
    hero_img="hero-mma",
    hero_pos="50% 18%",
    lede="Mixed Martial Arts za sve, od rekreativaca do natjecatelja: izdržljivost, tehnika i mentalna otpornost na najvišoj razini.",
    coach_name="Manuel Karić",
    coach_role="Bivši profesionalni MMA borac",
    coach_bio="Manuel Karić, bivši profesionalni MMA borac, vodi MMA treninge za napredne borce i natjecatelje, razvijajući izdržljivost i mentalnu otpornost.",
    schedule_rows=[("Utorak","21:00h",""),("Četvrtak","21:00h",""),("Subota","po dogovoru","")],
    focus_items=[
        ("01","Udaranje i hrvanje","Integracija kickboxinga, boksa i borbe u parteru."),
        ("02","Mentalna otpornost","Simulacija natjecateljskog pritiska kroz kontrolirani sparing."),
        ("03","Kondicijska priprema","Eksplozivnost i izdržljivost potrebna za MMA natjecanja."),
    ],
    crosslinks=others("mma.html"),
    desc="MMA trening za napredne borce i natjecatelje (16+) u Viškovu, pod vodstvom Manuela Karića.",
    og_image="assets/img/pads-sparring-lg.jpg",
)

program_page(
    slug="zenska-rekreacija.html",
    nav_active="zenska-rekreacija.html",
    title_html="Ženska rekreacija",
    age_range="Svi uzrasti",
    eyebrow="Rekreacija",
    hero_img="hero-zenska",
    lede="Trening osmišljen za žene svih dobi i razina pripremljenosti: fleksibilnost, kondicija i dobra energija u ženskom društvu.",
    coach_name="Dragan Majkić",
    coach_role="Osnivač kluba",
    coach_bio="Dragan Majkić, osnivač kluba, nadzire sve treninge i osobno vodi žensku rekreaciju, fokusirajući se na fleksibilnost, kondiciju i zabavu.",
    schedule_rows=[("Ponedjeljak","19:00h",""),("Srijeda","19:00h",""),("Petak","19:00h","")],
    focus_items=[
        ("01","Fleksibilnost","Dinamično istezanje i tehnika kroz kontrolirane pokrete."),
        ("02","Kondicija bez pritiska","Tempo prilagođen svima, bez natjecateljskog pritiska."),
        ("03","Druženje i motivacija","Trening u pozitivnoj grupi koja se međusobno podržava."),
    ],
    crosslinks=others("zenska-rekreacija.html"),
    desc="Ženska rekreacija u Viškovu za sve uzraste: fleksibilnost, kondicija i druženje pod vodstvom Dragana Majkića.",
    og_image="assets/img/gloves-hanging-lg.jpg",
)


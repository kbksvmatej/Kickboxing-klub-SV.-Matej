# -*- coding: utf-8 -*-
import os

SITE = "https://kbk.svmatej.hr/"
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAGES = [
    ("index.html", "Početna"),
    ("o-nama.html", "O nama"),
    ("kickboxing-djeca.html", "Kickboxing 7–15"),
    ("kickboxing-16.html", "Kickboxing 16+"),
    ("mma.html", "MMA"),
    ("zenska-rekreacija.html", "Ženska rekreacija"),
]

NAV_ITEMS = [
    ("index.html", "Početna"),
    ("__KB_DROPDOWN__", "Kickboxing"),
    ("mma.html", "MMA"),
    ("zenska-rekreacija.html", "Ženska rekreacija"),
    ("o-nama.html", "O nama"),
]

def head(title, desc, slug, og_image="assets/img/team-portrait-lg.jpg"):
    canonical = SITE + ("" if slug == "index.html" else slug)
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:locale" content="hr_HR">
<meta name="theme-color" content="#141413">
<link rel="icon" type="image/png" href="assets/img/logo-black.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
"""

def nav(active):
    def cls(href):
        return " active" if href == active else ""
    kb_active = active in ("kickboxing-djeca.html", "kickboxing-16.html")
    items = []
    for href, label in NAV_ITEMS:
        if href == "__KB_DROPDOWN__":
            items.append(f"""<li class="has-dropdown">
              <a href="kickboxing-16.html" class="{'active' if kb_active else ''}">Kickboxing</a>
              <div class="dropdown"><ul>
                <li><a href="kickboxing-djeca.html">Djeca i mlađi kadeti <small style="display:block;color:var(--white-faint);font-weight:500;text-transform:none;">7–15 godina</small></a></li>
                <li><a href="kickboxing-16.html">Stariji kadeti, juniori, seniori <small style="display:block;color:var(--white-faint);font-weight:500;text-transform:none;">16+ godina</small></a></li>
              </ul></div>
            </li>""")
        else:
            items.append(f'<li><a href="{href}" class="{cls(href)}">{label}</a></li>')
    items_html = "\n".join(items)

    return f"""<nav class="site-nav">
  <a href="index.html" class="brand">
    <img src="assets/img/logo-white.png" alt="KBK Sveti Matej logo">
  </a>
  <ul class="nav-links">
    {items_html}
  </ul>
  <a href="index.html#kontakt" class="btn btn-primary nav-cta">Postani član</a>
  <button class="hamburger" aria-label="Izbornik" aria-expanded="false">
    <span></span><span></span><span></span>
  </button>
</nav>
<div class="mobile-menu">
  <a href="index.html">Početna</a>
  <a href="kickboxing-djeca.html">Kickboxing 7–15</a>
  <a href="kickboxing-16.html">Kickboxing 16+</a>
  <a href="mma.html">MMA</a>
  <a href="zenska-rekreacija.html">Ženska rekreacija</a>
  <a href="o-nama.html">O nama</a>
  <div class="mm-foot">
    <a href="index.html#kontakt" class="btn btn-primary">Postani član</a>
    <a href="tel:+385993130725" style="font-weight:700;">+385 99 3130 725</a>
  </div>
</div>"""

def footer():
    return """<footer>
  <div class="container">
    <div class="foot-top">
      <a href="index.html" class="foot-brand"><img src="assets/img/logo-white.png" alt="KBK Sveti Matej logo">KBK Sveti Matej</a>
      <ul class="foot-links">
        <li><a href="index.html">Početna</a></li>
        <li><a href="kickboxing-djeca.html">Kickboxing 7–15</a></li>
        <li><a href="kickboxing-16.html">Kickboxing 16+</a></li>
        <li><a href="mma.html">MMA</a></li>
        <li><a href="zenska-rekreacija.html">Ženska rekreacija</a></li>
        <li><a href="o-nama.html">O nama</a></li>
        <li><a href="index.html#kontakt">Kontakt</a></li>
      </ul>
    </div>
    <div class="foot-bottom">
      <span>&copy; <span id="year"></span> Kickboxing klub SV. Matej · Vozišće 5, 51216 Viškovo</span>
      <span>Mjesto gdje nastaju borci od 1994.</span>
    </div>
  </div>
</footer>
<button class="back-to-top" aria-label="Povratak na vrh">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 19V5M12 5L5 12M12 5L19 12" stroke="#141413" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
</button>
<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
<script src="js/main.js"></script>"""

def page(title, desc, slug, active, body, og_image=None):
    kwargs = {}
    if og_image: kwargs["og_image"] = og_image
    html = f"""<!doctype html>
<html lang="hr">
<head>
{head(title, desc, slug, **kwargs)}
</head>
<body>
{nav(active)}
{body}
{footer()}
</body>
</html>"""
    with open(os.path.join(OUT, slug), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", slug)

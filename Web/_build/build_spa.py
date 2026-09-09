# -*- coding: utf-8 -*-
"""Builds a single self-contained HTML file (SPA) for the Artifact tool.
Reuses the exact page bodies from build_pages.py, rewrites internal links to
hash routes, inlines all images/video as data: URIs, and swaps the Google Maps
iframe for an outbound link (iframes to arbitrary hosts are blocked in the
artifact sandbox)."""
import re, os, base64, mimetypes, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_pages  # noqa: E402  (runs the production build + populates PAGE_BODIES)

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_DIR = "/tmp/spa-assets"
OUT_FILE = "/home/claude/spa/kbk-artifact.html"

PAGE_BODIES = build_pages.PAGE_BODIES
CSS = open(os.path.join(SITE_ROOT, "css", "style.css"), encoding="utf-8").read()

ROUTE_ORDER = ["index", "kickboxing-djeca", "kickboxing-16", "mma", "zenska-rekreacija", "o-nama"]
ROUTE_TITLE = {
    "index": "Početna",
    "kickboxing-djeca": "Kickboxing 7-15",
    "kickboxing-16": "Kickboxing 16+",
    "mma": "MMA",
    "zenska-rekreacija": "Ženska rekreacija",
    "o-nama": "O nama",
}

# ---------- asset inlining ----------
def data_uri(path):
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return f"data:{mime};base64,{b64}"

ASSET_CACHE = {}
def inline_assets(html):
    def repl(m):
        rel = m.group(1)  # e.g. assets/img/foo-lg.jpg or assets/video/hero-loop.mp4
        fname = os.path.basename(rel)
        if fname not in ASSET_CACHE:
            local = os.path.join(ASSET_DIR, fname)
            if not os.path.exists(local):
                raise SystemExit(f"missing optimized asset for SPA: {fname}")
            ASSET_CACHE[fname] = data_uri(local)
        return f'"{ASSET_CACHE[fname]}"'
    return re.sub(r'"(assets/(?:img|video)/[a-zA-Z0-9_.\-]+)"', repl, html)

# ---------- link rewriting ----------
SLUG_MAP = {
    "index.html": "index",
    "o-nama.html": "o-nama",
    "kickboxing-djeca.html": "kickboxing-djeca",
    "kickboxing-16.html": "kickboxing-16",
    "mma.html": "mma",
    "zenska-rekreacija.html": "zenska-rekreacija",
}

def rewrite_links(html):
    # href="index.html#kontakt"  -> href="#/index/kontakt"
    def repl_with_anchor(m):
        page, anchor = m.group(1), m.group(2)
        route = SLUG_MAP.get(page, page.replace(".html", ""))
        return f'href="#/{route}/{anchor}"'
    html = re.sub(r'href="([a-z0-9-]+\.html)#([a-zA-Z0-9]+)"', repl_with_anchor, html)

    # href="mma.html" -> href="#/mma"
    def repl_plain(m):
        page = m.group(1)
        route = SLUG_MAP.get(page, page.replace(".html", ""))
        return f'href="#/{route}"'
    html = re.sub(r'href="([a-z0-9-]+\.html)"', repl_plain, html)
    return html

def drop_webm(html):
    return re.sub(r'\s*<source src="assets/video/hero-loop\.webm" type="video/webm">\n?', "\n", html)

# ---------- Google Maps iframe -> outbound link (iframes to external hosts are blocked) ----------
def fix_map(html):
    pattern = re.compile(r'<div class="reveal map-frame"[^>]*>\s*<iframe[^>]*></iframe>\s*</div>', re.S)
    replacement = (
        '<a class="reveal map-frame" style="transition-delay:120ms;display:flex;align-items:center;'
        'justify-content:center;text-align:center;padding:2rem;background:var(--black-3);text-decoration:none;" '
        'href="https://www.google.com/maps?q=Vozi%C5%A1%C4%87e%205,%2051216%20Vi%C5%A1kovo" target="_blank" rel="noopener">'
        '<span><span class="pill" style="margin-bottom:1rem;">Vozišće 5, 51216 Viškovo</span>'
        '<br><span style="font-weight:800;text-transform:uppercase;letter-spacing:.06em;font-size:.85rem;">'
        'Otvori na Google Karte &rarr;</span></span></a>'
    )
    return pattern.sub(replacement, html)

# ---------- build shared nav / footer (hash-based) ----------
def nav_spa(active_route):
    def cls(route):
        return " active" if route == active_route else ""
    kb_active = active_route in ("kickboxing-djeca", "kickboxing-16")
    items = [
        f'<li><a href="#/index" class="{cls("index")}" data-route-link>Početna</a></li>',
        f'''<li class="has-dropdown">
          <a href="#/kickboxing-16" class="{'active' if kb_active else ''}" data-route-link>Kickboxing</a>
          <div class="dropdown"><ul>
            <li><a href="#/kickboxing-djeca" data-route-link>Djeca i mlađi kadeti <small style="display:block;color:var(--white-faint);font-weight:500;text-transform:none;">7–15 godina</small></a></li>
            <li><a href="#/kickboxing-16" data-route-link>Stariji kadeti, juniori, seniori <small style="display:block;color:var(--white-faint);font-weight:500;text-transform:none;">16+ godina</small></a></li>
          </ul></div>
        </li>''',
        f'<li><a href="#/mma" class="{cls("mma")}" data-route-link>MMA</a></li>',
        f'<li><a href="#/zenska-rekreacija" class="{cls("zenska-rekreacija")}" data-route-link>Ženska rekreacija</a></li>',
        f'<li><a href="#/o-nama" class="{cls("o-nama")}" data-route-link>O nama</a></li>',
    ]
    items_html = "\n".join(items)
    return f"""<nav class="site-nav">
  <a href="#/index" class="brand" data-route-link>
    <img src="assets/img/logo-white.png" alt="KBK Sveti Matej logo">
  </a>
  <ul class="nav-links">
    {items_html}
  </ul>
  <a href="#/index/kontakt" class="btn btn-primary nav-cta" data-route-link>Postani član</a>
  <button class="hamburger" aria-label="Izbornik" aria-expanded="false">
    <span></span><span></span><span></span>
  </button>
</nav>
<div class="mobile-menu">
  <a href="#/index" data-route-link>Početna</a>
  <a href="#/kickboxing-djeca" data-route-link>Kickboxing 7–15</a>
  <a href="#/kickboxing-16" data-route-link>Kickboxing 16+</a>
  <a href="#/mma" data-route-link>MMA</a>
  <a href="#/zenska-rekreacija" data-route-link>Ženska rekreacija</a>
  <a href="#/o-nama" data-route-link>O nama</a>
  <div class="mm-foot">
    <a href="#/index/kontakt" class="btn btn-primary" data-route-link>Postani član</a>
    <a href="tel:+385993130725" style="font-weight:700;">+385 99 3130 725</a>
  </div>
</div>"""

def footer_spa():
    return """<footer>
  <div class="container">
    <div class="foot-top">
      <a href="#/index" class="foot-brand" data-route-link><img src="assets/img/logo-white.png" alt="KBK Sveti Matej logo">KBK Sveti Matej</a>
      <ul class="foot-links">
        <li><a href="#/index" data-route-link>Početna</a></li>
        <li><a href="#/kickboxing-djeca" data-route-link>Kickboxing 7–15</a></li>
        <li><a href="#/kickboxing-16" data-route-link>Kickboxing 16+</a></li>
        <li><a href="#/mma" data-route-link>MMA</a></li>
        <li><a href="#/zenska-rekreacija" data-route-link>Ženska rekreacija</a></li>
        <li><a href="#/o-nama" data-route-link>O nama</a></li>
        <li><a href="#/index/kontakt" data-route-link>Kontakt</a></li>
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
</button>"""

# ---------- assemble ----------
sections_html = []
for slug_key, route in [("index.html","index"), ("kickboxing-djeca.html","kickboxing-djeca"),
                         ("kickboxing-16.html","kickboxing-16"), ("mma.html","mma"),
                         ("zenska-rekreacija.html","zenska-rekreacija"), ("o-nama.html","o-nama")]:
    body = PAGE_BODIES[slug_key]
    body = rewrite_links(body)
    body = fix_map(body)
    body = drop_webm(body)
    sections_html.append(f'<div class="route-page" data-route="{route}" hidden>\n{body}\n</div>')

nav_html = nav_spa("index")
foot_html = footer_spa()
nav_html = rewrite_links(nav_html)  # no-op safety, already hash-based
all_html = nav_html + "\n<main>\n" + "\n".join(sections_html) + "\n</main>\n" + foot_html
all_html = inline_assets(all_html)

JS = r"""
(function(){
  "use strict";
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var ROUTES = ["index","kickboxing-djeca","kickboxing-16","mma","zenska-rekreacija","o-nama"];
  var pages = {};
  ROUTES.forEach(function(r){ pages[r] = document.querySelector('.route-page[data-route="'+r+'"]'); });

  var nav = document.querySelector(".site-nav");
  var menu = document.querySelector(".mobile-menu");
  var burger = document.querySelector(".hamburger");

  function closeMenu(){
    if(menu){ menu.classList.remove("is-open"); }
    if(burger){ burger.classList.remove("is-open"); burger.setAttribute("aria-expanded","false"); }
    document.body.style.overflow = "";
  }

  function setActiveLinks(route){
    document.querySelectorAll("[data-route-link]").forEach(function(a){
      var href = a.getAttribute("href") || "";
      var m = href.match(/^#\/([a-z0-9-]+)/);
      var r = m ? m[1] : null;
      var isKbChild = (route === "kickboxing-djeca" || route === "kickboxing-16");
      if(r === route || (href.indexOf("kickboxing-16") !== -1 && isKbChild && a.closest(".has-dropdown"))){
        a.classList.add("active");
      } else {
        a.classList.remove("active");
      }
    });
  }

  function initRevealAndCounters(scope){
    var revealEls = scope.querySelectorAll(".reveal");
    if("IntersectionObserver" in window && !reduceMotion){
      var io = new IntersectionObserver(function(entries){
        entries.forEach(function(entry){
          if(entry.isIntersecting){ entry.target.classList.add("is-visible"); io.unobserve(entry.target); }
        });
      }, {threshold:.16, rootMargin:"0px 0px -8% 0px"});
      revealEls.forEach(function(el){ el.style.setProperty("--i", el.dataset.i || 0); io.observe(el); });
    } else {
      revealEls.forEach(function(el){ el.classList.add("is-visible"); });
    }

    function animateCount(el){
      var target = parseFloat(el.dataset.count);
      var suffix = el.dataset.suffix || "";
      if(reduceMotion || isNaN(target)){ el.textContent = target + suffix; return; }
      var start = null, dur = 1200;
      function step(ts){
        if(!start) start = ts;
        var p = Math.min(1, (ts - start) / dur);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(target * eased) + suffix;
        if(p < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }
    var counters = scope.querySelectorAll("[data-count]");
    if("IntersectionObserver" in window){
      var cio = new IntersectionObserver(function(entries){
        entries.forEach(function(entry){
          if(entry.isIntersecting){ animateCount(entry.target); cio.unobserve(entry.target); }
        });
      }, {threshold:.6});
      counters.forEach(function(c){ cio.observe(c); });
    } else {
      counters.forEach(animateCount);
    }

    var dayNames = ["nedjelja","ponedjeljak","utorak","srijeda","cetvrtak","petak","subota"];
    var today = dayNames[new Date().getDay()];
    scope.querySelectorAll("[data-day]").forEach(function(row){
      if(row.dataset.day === today && !row.querySelector(".today-pill")){
        row.classList.add("is-today");
        var pill = document.createElement("span");
        pill.className = "today-pill";
        pill.textContent = "Danas";
        var dayLabel = row.querySelector(".day");
        if(dayLabel) dayLabel.appendChild(pill);
      }
    });

    var heroVideo = scope.querySelector(".hero-media video");
    var videoToggle = scope.querySelector(".video-toggle");
    var ICON_PAUSE = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><rect x="6" y="4" width="4" height="16" rx="1" fill="#F9F9F9"/><rect x="14" y="4" width="4" height="16" rx="1" fill="#F9F9F9"/></svg>';
    var ICON_PLAY = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M7 4L20 12L7 20V4Z" fill="#F9F9F9"/></svg>';
    if(heroVideo){
      if(reduceMotion){ heroVideo.pause(); heroVideo.removeAttribute("autoplay"); }
      else { heroVideo.play().catch(function(){}); }
      if(videoToggle && !videoToggle.dataset.bound){
        videoToggle.dataset.bound = "1";
        var playing = !reduceMotion;
        videoToggle.addEventListener("click", function(){
          if(playing){ heroVideo.pause(); } else { heroVideo.play().catch(function(){}); }
          playing = !playing;
          videoToggle.innerHTML = playing ? ICON_PAUSE : ICON_PLAY;
        });
        videoToggle.innerHTML = playing ? ICON_PAUSE : ICON_PLAY;
      }
    }
  }

  function showRoute(route, anchor){
    if(!pages[route]) route = "index";
    ROUTES.forEach(function(r){ if(pages[r]) pages[r].hidden = (r !== route); });
    setActiveLinks(route);
    closeMenu();
    if(anchor){
      requestAnimationFrame(function(){
        var el = document.getElementById(anchor);
        if(el) el.scrollIntoView({behavior: reduceMotion ? "auto" : "smooth", block:"start"});
      });
    } else {
      window.scrollTo(0,0);
    }
    initRevealAndCounters(pages[route]);
  }

  function parseHash(){
    var h = location.hash.replace(/^#\/?/, "");
    var parts = h.split("/").filter(Boolean);
    return {route: parts[0] || "index", anchor: parts[1] || null};
  }

  window.addEventListener("hashchange", function(){
    var p = parseHash();
    showRoute(p.route, p.anchor);
  });

  document.addEventListener("click", function(e){
    var a = e.target.closest('a[href^="#/"]');
    if(a){
      var href = a.getAttribute("href");
      if(location.hash === href){
        var p = parseHash();
        showRoute(p.route, p.anchor);
      }
      closeMenu();
    }
  });

  function onScroll(){
    if(!nav) return;
    if(window.scrollY > 24) nav.classList.add("is-scrolled");
    else nav.classList.remove("is-scrolled");
    var btt = document.querySelector(".back-to-top");
    if(btt){
      if(window.scrollY > 700) btt.classList.add("is-visible");
      else btt.classList.remove("is-visible");
    }
  }
  document.addEventListener("scroll", onScroll, {passive:true});

  if(burger && menu){
    burger.addEventListener("click", function(){
      var open = menu.classList.toggle("is-open");
      burger.classList.toggle("is-open", open);
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
  }

  var backToTop = document.querySelector(".back-to-top");
  if(backToTop){
    backToTop.addEventListener("click", function(){
      window.scrollTo({top:0, behavior: reduceMotion ? "auto" : "smooth"});
    });
  }

  document.getElementById("year") && (document.getElementById("year").textContent = new Date().getFullYear());

  var p0 = parseHash();
  showRoute(p0.route, p0.anchor);
  onScroll();
})();
"""

TITLE = "KBK Sveti Matej — Kickboxing, MMA i ženska rekreacija"

page_out = f"""<title>{TITLE}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
{CSS}
main{{ display:block; }}
[hidden]{{ display:none !important; }}
</style>
{all_html}
<script>
{JS}
</script>
"""

os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write(page_out)

size_mb = os.path.getsize(OUT_FILE) / (1024*1024)
print(f"wrote {OUT_FILE} ({size_mb:.2f} MB)")

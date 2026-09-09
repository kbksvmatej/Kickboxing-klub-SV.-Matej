/* KBK Sveti Matej — shared site behaviour */
(function(){
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- nav scroll state ---------- */
  var nav = document.querySelector(".site-nav");
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
  onScroll();

  /* ---------- mobile menu ---------- */
  var burger = document.querySelector(".hamburger");
  var menu = document.querySelector(".mobile-menu");
  if(burger && menu){
    burger.addEventListener("click", function(){
      var open = menu.classList.toggle("is-open");
      burger.classList.toggle("is-open", open);
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    menu.querySelectorAll("a").forEach(function(a){
      a.addEventListener("click", function(){
        menu.classList.remove("is-open");
        burger.classList.remove("is-open");
        document.body.style.overflow = "";
      });
    });
  }

  /* ---------- active nav link ---------- */
  var here = (location.pathname.split("/").pop() || "index.html");
  document.querySelectorAll(".nav-links a, .mobile-menu a").forEach(function(a){
    var href = a.getAttribute("href");
    if(href === here || (here === "" && href === "index.html")) a.classList.add("active");
  });

  /* ---------- scroll reveal ---------- */
  var revealEls = document.querySelectorAll(".reveal");
  if("IntersectionObserver" in window && !reduceMotion){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, {threshold:.16, rootMargin:"0px 0px -8% 0px"});
    revealEls.forEach(function(el, i){
      el.style.setProperty("--i", el.dataset.i || 0);
      io.observe(el);
    });
  } else {
    revealEls.forEach(function(el){ el.classList.add("is-visible"); });
  }

  /* ---------- count-up stats ---------- */
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
  var counters = document.querySelectorAll("[data-count]");
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

  /* ---------- highlight today's schedule rows ---------- */
  var dayNames = ["nedjelja","ponedjeljak","utorak","srijeda","cetvrtak","petak","subota"];
  var today = dayNames[new Date().getDay()];
  document.querySelectorAll("[data-day]").forEach(function(row){
    if(row.dataset.day === today){
      row.classList.add("is-today");
      var pill = document.createElement("span");
      pill.className = "today-pill";
      pill.textContent = "Danas";
      var dayLabel = row.querySelector(".day");
      if(dayLabel && !dayLabel.querySelector(".today-pill")) dayLabel.appendChild(pill);
    }
  });

  /* ---------- back to top ---------- */
  var backToTop = document.querySelector(".back-to-top");
  if(backToTop){
    backToTop.addEventListener("click", function(){
      window.scrollTo({top:0, behavior: reduceMotion ? "auto" : "smooth"});
    });
  }

  /* ---------- hero video: pause on reduced motion, allow manual toggle ---------- */
  var ICON_PAUSE = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><rect x="6" y="4" width="4" height="16" rx="1" fill="#F9F9F9"/><rect x="14" y="4" width="4" height="16" rx="1" fill="#F9F9F9"/></svg>';
  var ICON_PLAY = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M7 4L20 12L7 20V4Z" fill="#F9F9F9"/></svg>';
  var heroVideo = document.querySelector(".hero-media video");
  var videoToggle = document.querySelector(".video-toggle");
  if(heroVideo){
    if(reduceMotion){ heroVideo.pause(); heroVideo.removeAttribute("autoplay"); }
    if(videoToggle){
      var playing = !reduceMotion;
      videoToggle.addEventListener("click", function(){
        if(playing){ heroVideo.pause(); } else { heroVideo.play(); }
        playing = !playing;
        videoToggle.innerHTML = playing ? ICON_PAUSE : ICON_PLAY;
      });
      videoToggle.innerHTML = playing ? ICON_PAUSE : ICON_PLAY;
    }
  }

  /* ---------- subtle hero parallax (desktop, motion allowed) ---------- */
  var heroMedia = document.querySelector(".hero-media");
  if(heroMedia && !reduceMotion && window.matchMedia("(pointer:fine)").matches){
    document.addEventListener("scroll", function(){
      var y = window.scrollY;
      if(y < window.innerHeight){
        heroMedia.style.transform = "translateY(" + (y * 0.28) + "px)";
      }
    }, {passive:true});
  }
})();

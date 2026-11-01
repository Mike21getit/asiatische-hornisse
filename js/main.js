/* Asiatische Hornisse – Seitenlogik (ohne Abhängigkeiten)
   Navigation/Reveal übernommen von der Fotografie-Seite, plus mailto-Formular. */
(function () {
  'use strict';
  var root = document.documentElement;
  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  /* ---------- Navigation ---------- */
  var header = $('.site-header');
  var toggle = $('.menu-toggle');
  var menu = $('#nav-menu');

  function onScroll() { header.classList.toggle('is-scrolled', window.scrollY > 40); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  function setMenu(open) {
    root.classList.toggle('menu-open', open);
    document.body.classList.toggle('no-scroll', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
  }
  toggle.addEventListener('click', function () { setMenu(!root.classList.contains('menu-open')); });
  $$('a', menu).forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && root.classList.contains('menu-open')) { setMenu(false); toggle.focus(); }
  });
  window.matchMedia('(min-width: 1101px)').addEventListener('change', function (m) { if (m.matches) setMenu(false); });

  // Aktiven Navigationspunkt markieren
  var navLinks = $$('.nav-links a');
  if ('IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        navLinks.forEach(function (a) { a.classList.toggle('is-active', a.getAttribute('href') === '#' + en.target.id); });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    navLinks.forEach(function (a) {
      var id = (a.getAttribute('href') || '').slice(1);
      var s = id && document.getElementById(id); if (s) spy.observe(s);
    });
  }

  /* ---------- Scroll-Reveal ---------- */
  var reveals = $$('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* ---------- Anfrage-Formular -> E-Mail-Programm (kein Server) ---------- */
  var form = $('#anfrage');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = form.elements;
      var to = form.getAttribute('data-mailto');
      var subject = (f.anliegen.value || 'Anfrage') + ' – ' + (f.ort.value || 'Ort folgt');
      var lines = [
        'Anliegen: ' + f.anliegen.value,
        'Name: ' + f.name.value,
        'Telefon: ' + f.telefon.value,
        'Ort / Adresse des Fundes: ' + f.ort.value,
        'Wo befindet sich das Nest? ' + f.lage.value,
        'Geschätzte Höhe: ' + f.hoehe.value,
        '',
        'Beschreibung:',
        f.nachricht.value,
        '',
        '(Fotos bitte aus sicherem Abstand aufnehmen und als Anhang beifügen.)'
      ];
      window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
    });
  }

  /* ---------- Lightbox für die Galerie (angepasst von der Fotografie-Seite) ---------- */
  (function () {
    var box = $('#lightbox'), links = $$('#gallery a');
    if (!box || !links.length) return;
    var img = $('.lb-img', box), counter = $('.lb-counter', box), title = $('.lb-title', box);
    var btnClose = $('.lb-close', box), btnPrev = $('.lb-prev', box), btnNext = $('.lb-next', box);
    var index = 0, opener = null, token = 0, cache = {};
    var list = links.map(function (a) {
      var t = $('img', a);
      return { src: a.getAttribute('href'), w: +a.dataset.w, h: +a.dataset.h, cap: a.dataset.caption || '', alt: t ? t.alt : '' };
    });
    function preload(i) {
      var it = list[(i + list.length) % list.length];
      if (cache[it.src]) return;
      var p = new Image(); p.decoding = 'async'; p.src = it.src; cache[it.src] = p;
    }
    function show(i) {
      index = (i + list.length) % list.length;
      var it = list[index], my = ++token;
      counter.textContent = (index + 1) + ' / ' + list.length;
      title.textContent = it.cap; img.alt = it.alt;
      box.classList.add('is-loading'); img.classList.add('is-loading');
      var loader = cache[it.src] || new Image(); cache[it.src] = loader;
      var finish = function () {
        if (my !== token) return;
        img.src = it.src; img.width = it.w; img.height = it.h;
        img.classList.remove('is-loading'); box.classList.remove('is-loading');
      };
      if (loader.complete && loader.naturalWidth) finish();
      else { loader.onload = finish; loader.onerror = finish; if (!loader.src) loader.src = it.src; }
      preload(index + 1); preload(index - 1);
    }
    function open(i, from) {
      opener = from || null; box.hidden = false;
      document.body.classList.add('no-scroll');
      requestAnimationFrame(function () { box.classList.add('is-open'); });
      show(i); btnClose.focus();
    }
    function close() {
      if (box.hidden) return;
      box.classList.remove('is-open'); document.body.classList.remove('no-scroll');
      setTimeout(function () { box.hidden = true; img.removeAttribute('src'); }, 300);
      if (opener) opener.focus({ preventScroll: true });
    }
    links.forEach(function (a, i) {
      a.addEventListener('click', function (e) {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
        e.preventDefault(); open(i, a);
      });
    });
    btnClose.addEventListener('click', close);
    btnPrev.addEventListener('click', function () { show(index - 1); });
    btnNext.addEventListener('click', function () { show(index + 1); });
    box.addEventListener('click', function (e) { if (e.target === box || e.target.classList.contains('lb-stage')) close(); });
    document.addEventListener('keydown', function (e) {
      if (box.hidden) return;
      if (e.key === 'Escape') { e.preventDefault(); close(); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); show(index - 1); }
      else if (e.key === 'ArrowRight') { e.preventDefault(); show(index + 1); }
      else if (e.key === 'Tab') {
        var f = [btnClose, btnPrev, btnNext], pos = f.indexOf(document.activeElement);
        e.preventDefault(); f[(pos + (e.shiftKey ? -1 : 1) + f.length) % f.length].focus();
      }
    });
    var sx = 0, sy = 0, tracking = false;
    box.addEventListener('touchstart', function (e) {
      if (e.touches.length !== 1) { tracking = false; return; }
      tracking = true; sx = e.touches[0].clientX; sy = e.touches[0].clientY;
    }, { passive: true });
    box.addEventListener('touchmove', function (e) {
      if (!tracking || e.touches.length !== 1) return;
      var dx = e.touches[0].clientX - sx;
      if (Math.abs(dx) > Math.abs(e.touches[0].clientY - sy)) img.style.transform = 'translateX(' + dx * 0.4 + 'px)';
    }, { passive: true });
    box.addEventListener('touchend', function (e) {
      if (!tracking) return;
      tracking = false; img.style.transform = '';
      var t = e.changedTouches[0], dx = t.clientX - sx, dy = t.clientY - sy;
      if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.3) show(index + (dx < 0 ? 1 : -1));
      else if (dy > 90 && Math.abs(dy) > Math.abs(dx) * 1.5) close();
    });
  })();

  /* Nur ein Video gleichzeitig abspielen */
  $$('.case-videos video').forEach(function (v, i, all) {
    v.addEventListener('play', function () { all.forEach(function (o) { if (o !== v) o.pause(); }); });
  });

  var y = $('#year'); if (y) y.textContent = new Date().getFullYear();
})();

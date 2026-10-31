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

  var y = $('#year'); if (y) y.textContent = new Date().getFullYear();
})();

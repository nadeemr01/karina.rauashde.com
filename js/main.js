(function () {
  var d = document, root = d.documentElement;

  // Nav: hairline once the page scrolls
  var nav = d.querySelector('.gnav');
  function onScroll() { if (nav) nav.classList.toggle('is-scrolled', window.scrollY > 4); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobile menu
  var btn = d.querySelector('.menu-btn');
  function setMenu(open) {
    root.classList.toggle('menu-open', open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.setAttribute('aria-label', open ? btn.dataset.close : btn.dataset.open);
  }
  if (btn) {
    btn.addEventListener('click', function () { setMenu(!root.classList.contains('menu-open')); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && root.classList.contains('menu-open')) { setMenu(false); btn.focus(); } });
    d.querySelectorAll('.menu a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    window.matchMedia('(min-width: 834px)').addEventListener('change', function (m) { if (m.matches) setMenu(false); });
  }

  // Reveal blocks as they enter the viewport
  var els = d.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('is-in'); });
  }

  // Remember the language the visitor picked (stops the auto-redirect on English pages)
  d.querySelectorAll('a[hreflang]').forEach(function (a) {
    a.addEventListener('click', function () {
      try { localStorage.setItem('lang', a.getAttribute('hreflang')); } catch (e) {}
    });
  });

  // Treatments: highlight the category in view
  var seg = d.querySelectorAll('.seg a');
  if (seg.length && 'IntersectionObserver' in window) {
    var byId = {};
    seg.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        seg.forEach(function (a) { a.removeAttribute('aria-current'); });
        var a = byId[e.target.id];
        if (a) {
          a.setAttribute('aria-current', 'true');
          var bar = a.parentNode;
          if (bar.scrollWidth > bar.clientWidth) bar.scrollTo({ left: a.offsetLeft - 24, behavior: 'smooth' });
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    d.querySelectorAll('.cat').forEach(function (s) { so.observe(s); });
  }

  // Levitating portrait leans toward the cursor (desktop only)
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (fine && !reduce) {
    d.querySelectorAll('.stage').forEach(function (stage) {
      var area = stage.closest('section') || stage;
      var raf = 0, tx = 0, ty = 0;
      area.addEventListener('pointermove', function (e) {
        var r = stage.getBoundingClientRect();
        tx = Math.max(-1, Math.min(1, (e.clientX - (r.left + r.width / 2)) / r.width));
        ty = Math.max(-1, Math.min(1, (e.clientY - (r.top + r.height / 2)) / r.height));
        if (!raf) raf = requestAnimationFrame(function () {
          stage.style.setProperty('--px', tx.toFixed(3));
          stage.style.setProperty('--py', ty.toFixed(3));
          raf = 0;
        });
      });
      area.addEventListener('pointerleave', function () {
        stage.style.setProperty('--px', 0);
        stage.style.setProperty('--py', 0);
      });
    });
  }
})();

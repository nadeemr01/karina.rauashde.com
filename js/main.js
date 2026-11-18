(function () {
  var d = document;

  // Header: solid background once the page scrolls
  var header = d.querySelector('.site-header');
  function onScroll() { header.classList.toggle('is-scrolled', window.scrollY > 12); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Reveal sections as they enter the viewport
  var els = d.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('is-in'); });
  }

  // Remember the language the visitor picked (stops the auto-redirect on the English page)
  d.querySelectorAll('.lang a').forEach(function (a) {
    a.addEventListener('click', function () {
      try { localStorage.setItem('lang', a.getAttribute('hreflang')); } catch (e) {}
    });
  });

  // Portrait follows the cursor slightly (desktop only)
  var stage = d.querySelector('.stage');
  var hero = d.querySelector('.hero');
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (stage && hero && fine && !reduce) {
    var raf = 0, tx = 0, ty = 0;
    hero.addEventListener('pointermove', function (e) {
      var r = stage.getBoundingClientRect();
      tx = Math.max(-1, Math.min(1, (e.clientX - (r.left + r.width / 2)) / r.width));
      ty = Math.max(-1, Math.min(1, (e.clientY - (r.top + r.height / 2)) / r.height));
      if (!raf) raf = requestAnimationFrame(function () {
        stage.style.setProperty('--px', tx.toFixed(3));
        stage.style.setProperty('--py', ty.toFixed(3));
        raf = 0;
      });
    });
    hero.addEventListener('pointerleave', function () {
      stage.style.setProperty('--px', 0);
      stage.style.setProperty('--py', 0);
    });
  }
})();

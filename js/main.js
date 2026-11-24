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
  // Results: filter by treatment (also from a #lips-style link) and open photos full-screen
  var cases = Array.prototype.slice.call(d.querySelectorAll('.case'));
  var filterBtns = d.querySelectorAll('.seg-filter button');
  function applyFilter(cat) {
    filterBtns.forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.filter === cat ? 'true' : 'false'); });
    cases.forEach(function (li) {
      li.hidden = cat !== 'all' && li.dataset.cat !== cat;
      if (!li.hidden) li.classList.add('is-in');
    });
  }
  filterBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      applyFilter(b.dataset.filter);
      try { history.replaceState(null, '', b.dataset.filter === 'all' ? location.pathname : '#' + b.dataset.filter); } catch (e) {}
    });
  });
  if (filterBtns.length && location.hash) {
    var h = location.hash.slice(1);
    if (d.querySelector('.seg-filter [data-filter="' + h + '"]')) applyFilter(h);
  }

  var lb = d.querySelector('.lb');
  if (lb && typeof lb.showModal === 'function') {
    var media = lb.querySelector('.lb-media'), cap = lb.querySelector('figcaption'), cur = null;
    var shown = function () { return cases.filter(function (li) { return !li.hidden; }); };
    var show = function (li) {
      cur = li;
      var frame = li.querySelector('.case-frame').cloneNode(true);
      var img = frame.querySelector('img');
      img.removeAttribute('loading');
      media.style.setProperty('--ar', img.getAttribute('width') / img.getAttribute('height'));
      media.replaceChildren(frame);
      var list = shown();
      cap.innerHTML = '';
      cap.appendChild(d.createTextNode(li.querySelector('h2').textContent));
      var sub = d.createElement('span');
      sub.textContent = li.querySelector('.case-cap p').textContent + ' · ';
      var count = d.createElement('bdi');
      count.dir = 'ltr';
      count.textContent = (list.indexOf(li) + 1) + ' / ' + list.length;
      sub.appendChild(count);
      cap.appendChild(sub);
    };
    var step = function (dir) {
      var list = shown(), i = list.indexOf(cur);
      if (i < 0) return;
      show(list[(i + dir + list.length) % list.length]);
    };
    cases.forEach(function (li) {
      li.querySelector('.case-media').addEventListener('click', function (e) {
        e.preventDefault();
        show(li);
        lb.showModal();
      });
    });
    lb.querySelector('.lb-close').addEventListener('click', function () { lb.close(); });
    lb.querySelector('.lb-prev').addEventListener('click', function () { step(-1); });
    lb.querySelector('.lb-next').addEventListener('click', function () { step(1); });
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target.classList.contains('lb-fig')) lb.close(); });
    lb.addEventListener('keydown', function (e) {
      var rtl = root.dir === 'rtl';
      if (e.key === 'ArrowRight') step(rtl ? -1 : 1);
      if (e.key === 'ArrowLeft') step(rtl ? 1 : -1);
    });
    var x0 = null;
    lb.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 50) step((dx < 0) !== (root.dir === 'rtl') ? 1 : -1);
    });
    lb.addEventListener('close', function () { if (cur) cur.querySelector('.case-media').focus(); });
  }
})();

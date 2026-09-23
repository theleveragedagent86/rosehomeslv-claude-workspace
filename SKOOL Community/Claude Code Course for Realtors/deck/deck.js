/* Deck runtime: keyboard nav, slide counter, progress bar.
   Arrow keys / space / j,k / PageUp,PageDown / Home,End advance.
   Trackpad and mouse wheel keep working normally, CSS snap catches them.

   Scrolling is animated here with requestAnimationFrame rather than
   scroll-behavior:smooth. Native smooth scrolling is unreliable inside a
   scroll-snap-type:mandatory container: the snap engine cancels the
   animation and the scroll never lands. */
(function () {
  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var bar = document.querySelector('.progress > i');
  var cur = document.querySelector('.hud .cur');
  var tot = document.querySelector('.hud .tot');
  if (!slides.length) return;

  var root = document.documentElement;
  var pad = function (n) { return String(n).padStart(2, '0'); };
  var reduce = matchMedia('(prefers-reduced-motion: reduce)');

  if (tot) tot.textContent = pad(slides.length);

  var index = 0;
  var animating = false;

  function paint() {
    if (cur) cur.textContent = pad(index + 1);
    if (bar) bar.style.transform = 'scaleX(' + ((index + 1) / slides.length) + ')';
  }

  /* Keep the counter honest when the user scrolls by hand. */
  var io = new IntersectionObserver(function (entries) {
    if (animating) return;
    entries.forEach(function (e) {
      if (e.isIntersecting && e.intersectionRatio >= 0.5) {
        var i = slides.indexOf(e.target);
        if (i > -1 && i !== index) { index = i; paint(); }
      }
    });
  }, { threshold: [0.5] });
  slides.forEach(function (s) { io.observe(s); });

  /* ---- fit-to-screen -------------------------------------------------
     Slides are exactly 100vh. Any slide whose content is taller than the
     space between the paddings gets zoomed down until it fits, so nothing
     is ever cut off the bottom no matter what size Ryan records at.
     The .hint arrow is absolutely positioned and stays out of the wrapper
     so it keeps its own size. .cue is excluded too, defensively: cues are
     display:none in deck.css and must never affect the fit measurement. */
  var MIN_ZOOM = 0.58;

  slides.forEach(function (s) {
    var box = document.createElement('div');
    box.className = 'fitbox';
    Array.prototype.slice.call(s.children).forEach(function (c) {
      if (!c.classList.contains('cue') && !c.classList.contains('hint')) box.appendChild(c);
    });
    s.insertBefore(box, s.firstChild);
    s.fitbox = box;
  });

  function fit() {
    slides.forEach(function (s) {
      var box = s.fitbox;
      box.style.zoom = '';
      var cs = getComputedStyle(s);
      var avail = s.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
      var natural = box.scrollHeight;
      /* avail can be 0 in a background/hidden tab, where the viewport
         collapses. Zooming off that measurement would shrink everything. */
      if (avail <= 0 || !natural || natural <= avail) return;
      box.style.zoom = Math.max(MIN_ZOOM, avail / natural);
    });
  }

  fit();

  var fitTimer;
  window.addEventListener('resize', function () {
    clearTimeout(fitTimer);
    fitTimer = setTimeout(function () { fit(); go(index); }, 120);
  });

  /* Webfonts land after first layout and change the measurements. */
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);

  function easeOutCubic(t) { return 1 - Math.pow(1 - t, 3); }

  function scrollToY(to, done) {
    var from = window.scrollY;
    var delta = to - from;
    if (Math.abs(delta) < 2) { done(); return; }

    if (reduce.matches) { root.scrollTop = to; done(); return; }

    /* Snap fights an in-flight animation, so hold it off until we land. */
    root.style.scrollSnapType = 'none';
    animating = true;

    var dur = Math.min(620, 260 + Math.abs(delta) * 0.18);
    var t0 = performance.now();

    (function step(now) {
      var p = Math.min(1, (now - t0) / dur);
      root.scrollTop = from + delta * easeOutCubic(p);
      if (p < 1) { requestAnimationFrame(step); }
      else {
        root.scrollTop = to;
        root.style.scrollSnapType = '';
        animating = false;
        done();
      }
    })(t0);
  }

  function go(n) {
    var next = Math.max(0, Math.min(slides.length - 1, n));
    if (next === index && window.scrollY === slides[next].offsetTop) return;
    index = next;
    paint();
    scrollToY(slides[index].offsetTop, function () { paint(); });
  }

  var NEXT = { ArrowDown: 1, ArrowRight: 1, PageDown: 1, ' ': 1, Spacebar: 1, j: 1, J: 1 };
  var PREV = { ArrowUp: 1, ArrowLeft: 1, PageUp: 1, k: 1, K: 1 };

  document.addEventListener('keydown', function (ev) {
    if (ev.metaKey || ev.ctrlKey || ev.altKey) return;
    var t = ev.target;
    if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;

    if (NEXT[ev.key]) { ev.preventDefault(); go(index + 1); }
    else if (PREV[ev.key]) { ev.preventDefault(); go(index - 1); }
    else if (ev.key === 'Home') { ev.preventDefault(); go(0); }
    else if (ev.key === 'End') { ev.preventDefault(); go(slides.length - 1); }
  });

  /* Deep-link and refresh-safe: ?s=7 opens on slide 7. */
  var q = parseInt((location.search.match(/[?&]s=(\d+)/) || [])[1], 10);
  if (q >= 1 && q <= slides.length) {
    index = q - 1;
    root.scrollTop = slides[index].offsetTop;
  }

  paint();
})();

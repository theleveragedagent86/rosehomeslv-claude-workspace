/* Title size steps by character count so nothing ever reaches a third line.
   Runs again after the fonts land, because the first pass measures Arial. */
(function () {
  function size(el) {
    var n = el.textContent.trim().length;
    el.classList.remove("cov__title--md", "cov__title--sm");
    if (n > 34) el.classList.add("cov__title--sm");
    else if (n > 17) el.classList.add("cov__title--md");
  }
  function fit() {
    document.querySelectorAll(".cell").forEach(function (cell) {
      var c = cell.querySelector(".cov");
      if (c) c.style.transform = "scale(" + cell.clientWidth / 1600 + ")";
    });
  }
  function run() { document.querySelectorAll(".cov__title").forEach(size); fit(); }
  run();
  addEventListener("resize", fit);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(run);
})();

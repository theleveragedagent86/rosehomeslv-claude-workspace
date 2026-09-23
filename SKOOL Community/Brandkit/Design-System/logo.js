/* <la-logo variant="lockup|wordmark|monogram|accent|favicon" inverse no-tagline>
   for plain HTML. Renders INLINE svg into a shadow root on purpose: an
   <img src="logo.svg"> is an isolated document that cannot load Barlow and
   silently falls back to Arial, and a light-DOM write breaks React trees that
   mount this element. */
(() => {
  const HEAD = 'font-family="Barlow, Helvetica Neue, Arial, sans-serif" font-weight="800"';
  const SUB = 'font-family="Raleway, Helvetica Neue, Arial, sans-serif" font-weight="600"';
  const TAGLINE = "Automating 80% of the job that sucks";

  const mono = (bg, ink, rule) => `<rect width="96" height="96" fill="${bg}"/>
<text x="48" y="40" ${HEAD} font-size="42" letter-spacing="-1.34" fill="${ink}" text-anchor="middle" dominant-baseline="central">LA</text>
<rect x="30" y="64" width="36" height="6" fill="${rule}"/>`;

  const build = {
    monogram: (i) => ({ vb: "0 0 96 96", body: i ? mono("#000000", "#FFFFFF", "#1768E5") : mono("#FFFFFF", "#050E3D", "#1768E5") }),
    accent: () => ({ vb: "0 0 96 96", body: mono("#1768E5", "#FFFFFF", "#FFFFFF") }),
    favicon: () => ({ vb: "0 0 32 32", body: `<rect width="32" height="32" fill="#000000"/>
<text x="16" y="15" ${HEAD} font-size="19" letter-spacing="-0.6" fill="#FFFFFF" text-anchor="middle" dominant-baseline="central">LA</text>
<rect x="9" y="25" width="14" height="3" fill="#5B9BFF"/>` }),
    wordmark: (i, tag) => ({ vb: tag ? "0 0 440 116" : "0 0 440 68", body: `<text x="0" y="42" ${HEAD} font-size="54" letter-spacing="-1.51" fill="${i ? "#FFFFFF" : "#050E3D"}" dominant-baseline="central">Leveraged Agent</text>` + (tag ? `
<rect x="0" y="86" width="56" height="4" fill="${i ? "#5B9BFF" : "#0B3FA8"}"/>
<text x="72" y="89" ${SUB} font-size="16" letter-spacing="0.16" fill="${i ? "#9AA3BC" : "#55627F"}" dominant-baseline="central">${TAGLINE}</text>` : "") }),
    lockup: (i, tag) => ({ vb: tag ? "0 0 380 96" : "0 0 296 96", body: `${i ? mono("#000000", "#FFFFFF", "#1768E5") : mono("#FFFFFF", "#050E3D", "#1768E5")}
<text x="124" y="30" ${HEAD} font-size="34" letter-spacing="-0.95" fill="${i ? "#FFFFFF" : "#050E3D"}" dominant-baseline="central">Leveraged</text>
<text x="124" y="58" ${HEAD} font-size="34" letter-spacing="-0.95" fill="${i ? "#FFFFFF" : "#050E3D"}" dominant-baseline="central">Agent</text>` + (tag ? `
<text x="124" y="88" ${SUB} font-size="13" letter-spacing="0.13" fill="${i ? "#9AA3BC" : "#55627F"}" dominant-baseline="central">${TAGLINE}</text>` : "") }),
  };

  /* Authored viewBoxes are generous on purpose. Once Barlow has loaded, measure
     the real ink and tighten the box to it, so the mark never carries dead space
     that would push it off centre. Also publishes the true aspect ratio on the
     host, so a placement only ever needs to set a width. */
  const fit = (svg, host) => {
    const apply = () => {
      let b;
      try { b = svg.getBBox(); } catch (e) { return; }
      if (!b || !b.width || !b.height) return;
      svg.setAttribute("viewBox", `${b.x} ${b.y} ${b.width} ${b.height}`);
      host.style.aspectRatio = `${b.width} / ${b.height}`;
    };
    apply();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(apply);
  };

  class LaLogo extends HTMLElement {
    connectedCallback() { this.render(); }
    static get observedAttributes() { return ["variant", "inverse", "no-tagline"]; }
    attributeChangedCallback() { if (this.isConnected) this.render(); }
    render() {
      const v = this.getAttribute("variant") || "lockup";
      const { vb, body } = (build[v] || build.lockup)(this.hasAttribute("inverse"), !this.hasAttribute("no-tagline"));
      const root = this.shadowRoot || this.attachShadow({ mode: "open" });
      root.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}" role="img" aria-label="Leveraged Agent" style="display:block;width:100%;height:100%">${body}</svg>`;
      this.style.display = "block";
      fit(root.firstChild, this);
    }
  }
  if (!customElements.get("la-logo")) customElements.define("la-logo", LaLogo);
})();

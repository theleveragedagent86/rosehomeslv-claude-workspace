/* ============================================================
   Rose Homes LV — CMA report renderer (vanilla)
   Builds every page from window.CMA_DATA. No build step.
   ============================================================ */
(function () {
  const D = window.CMA_DATA;
  const $doc = document.getElementById('doc');

  /* ---------- formatting ---------- */
  const fmt = (n) => '$' + Math.round(n).toLocaleString('en-US');
  const fmtShort = (n) => {
    if (n == null || n === '') return '—';
    if (n >= 1e6) return '$' + (n / 1e6).toFixed(2).replace(/\.?0+$/, '') + 'M';
    return '$' + Math.round(n / 1000) + 'K';
  };
  const ppsfOf = (c) => c.ppsf || Math.round((c.soldPrice || c.listPrice) / c.sqft);
  const priceOf = (c) => c.soldPrice || c.listPrice;
  const mean = (arr) => arr.reduce((a, b) => a + b, 0) / arr.length;
  const statusClass = (s) => ({ Active: 'active', Pending: 'pending', Sold: 'sold' }[s] || 'active');

  /* ---------- icons (Lucide-style, 1.75 stroke) ---------- */
  const IC = {
    phone: '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
    mail: '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 5L2 7"/>',
    pin: '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    globe: '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20Z"/>',
    home: '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
    briefcase: '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
    handshake: '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    'trending-up': '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>',
    clock: '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    id: '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M15 8h2M15 12h2M7 16h10"/>',
    megaphone: '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
    calendar: '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    key: '<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6"/><path d="m15.5 7.5 3 3L22 7l-3-3"/>',
    camera: '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/>',
  };
  const icon = (name) =>
    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">${IC[name] || ''}</svg>`;

  /* ---------- chrome ---------- */
  const wordmark = () =>
    `<div class="wm"><span class="wm-name">Rose Homes<b>LV</b></span><span class="wm-sub">Las Vegas · ${D.agent.name}</span></div>`;

  const head = (tag) =>
    `<div class="pg-head">${wordmark()}<div class="pg-tag"><span class="r"></span><span class="t">${tag}</span></div></div>`;

  const foot = (num) =>
    `<div class="pg-foot">
       <div class="ft-l"><img src="assets/rose-mark.svg" alt=""><span><b>${D.agent.name}</b> · Rose Homes LV</span></div>
       <div class="ft-r"><span>${D.agent.phone}</span><span>·</span><span>${D.agent.email}</span>${num ? `<span class="ft-num">${num}</span>` : ''}</div>
     </div>`;

  /* ---------- page factory ---------- */
  let pageNo = 0;
  const addPage = (html, opts = {}) => {
    const sec = document.createElement('section');
    sec.className = 'page' + (opts.cls ? ' ' + opts.cls : '');
    sec.dataset.role = opts.role || 'content';
    if (opts.label) sec.dataset.screenLabel = opts.label;
    sec.innerHTML = html;
    $doc.appendChild(sec);
    return sec;
  };
  const contentPage = (tag, label, mainHtml) => {
    pageNo += 1;
    const num = String(pageNo).padStart(2, '0');
    addPage(`${head(tag)}<div class="pg-main">${mainHtml}</div>${foot(num)}`, { label });
  };

  /* ============================================================
     1 — COVER
     ============================================================ */
  function cover() {
    const a = D.agent, s = D.subject;
    addPage(`
      <div class="cover brackets">
        <div class="cv-top">${wordmark()}
          <div class="pg-tag"><span class="r"></span><span class="t">Comparative Market Analysis</span></div>
        </div>
        <div class="cv-body">
          <div class="cv-prepared">Prepared for ${D.report.preparedFor}</div>
          <h1 class="cv-title">Comparative<br>Market Analysis</h1>
          <div class="cv-addr">${s.address}, ${s.cityStateZip}</div>
        </div>
        <div class="cv-hero"><image-slot id="${s.photoSlot}" shape="rect" fit="cover"${s.defaultPhoto ? ` src="${s.defaultPhoto}"` : ''} placeholder="Drop the subject property's hero photo"></image-slot></div>
        <div class="cv-foot">
          <div class="hs"><img src="${a.headshot}" alt="${a.name}"></div>
          <div class="agentcard">
            <div class="ac-name">${a.name}</div>
            <div class="ac-meta">${a.title} · License ${a.license} · Brokered by ${a.brokerage}</div>
            <div class="ac-grid">
              <div>${icon('phone')}${a.phone}</div>
              <div>${icon('mail')}${a.email}</div>
              <div>${icon('pin')}${a.address}</div>
              <div>${icon('globe')}${a.web}</div>
            </div>
          </div>
        </div>
      </div>`, { role: 'cover', cls: 'page--bleed', label: 'Cover' });
  }

  /* ============================================================
     2 — LISTINGS MAP
     ============================================================ */
  function mapStreets() {
    // stylized, abstract Las Vegas-style grid — hairlines + two gold arterials
    let h = '';
    for (let i = 1; i < 13; i++) { const y = (i * 640) / 13; h += `<line class="grid" x1="0" y1="${y}" x2="1000" y2="${y}"/>`; }
    for (let i = 1; i < 17; i++) { const x = (i * 1000) / 17; h += `<line class="grid" x1="${x}" y1="0" x2="${x}" y2="640"/>`; }
    return `<svg class="streets" viewBox="0 0 1000 640" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
      ${h}
      <polyline points="0,470 320,395 600,250 1000,40" fill="none" stroke="var(--pg-gold)" stroke-width="2" opacity="0.5"/>
      <polyline points="150,0 230,300 300,640" fill="none" stroke="var(--pg-gold)" stroke-width="2" opacity="0.4"/>
      <polyline points="705,0 765,640" fill="none" stroke="var(--pg-gold)" stroke-width="1.5" opacity="0.28"/>
    </svg>`;
  }
  function pin(p, label, kind) {
    return `<div class="pin ${kind}" style="left:${p.x}%;top:${p.y}%">
        <div class="bubble">${label}</div><div class="stem"></div>
      </div>`;
  }
  function legendItem(kind, text) {
    return `<span class="status ${kind}"><span class="mk"></span><span class="tx">${text}</span></span>`;
  }
  function mapPage() {
    pageNo += 1;
    const s = D.subject;
    const pins = D.comps.map((c) => pin(c.pin, fmtShort(priceOf(c)), statusClass(c.status))).join('') +
      pin(s.pin, 'Subject', 'subject');
    const main = `
      <div class="sec-title" style="margin-bottom:14px">
        <span class="eyebrow gold">Listings Map</span>
        <h1 class="h1">${s.address}</h1>
        <div class="body muted" style="margin-top:-4px">${s.beds} Bed · ${s.baths} Bath · ${s.sqft.toLocaleString()} Sqft, plus the six closest comparables.</div>
      </div>
      <div class="mapwrap">
        <div class="map-stage">${mapStreets()}${pins}</div>
        <div class="maplegend">
          ${legendItem('active', 'Active')}${legendItem('pending', 'Pending')}${legendItem('sold', 'Sold')}
          <span class="status subject" style="margin-left:auto"><span class="mk" style="background:var(--pg-fg);border-color:var(--pg-fg)"></span><span class="tx">Subject Property</span></span>
        </div>
      </div>`;
    addPage(`${head('Listings Map')}<div class="pg-main">${main}</div>${foot(String(pageNo).padStart(2, '0'))}`, { label: 'Listings Map' });
  }

  /* ============================================================
     3 — COMPARABLES TABLE
     ============================================================ */
  function compsTable() {
    const rows = D.comps.map((c) => `
      <tr>
        <td class="addr">
          <div class="a1">${c.address}</div>
          <div class="a2">${c.cityStateZip} · ${c.type}</div>
          <div style="margin-top:6px"><span class="status ${statusClass(c.status)}"><span class="mk"></span><span class="tx">${c.status}</span></span></div>
        </td>
        <td class="num">${c.beds} / ${c.baths}</td>
        <td class="num">${c.sqft.toLocaleString()}</td>
        <td class="price">${fmtShort(c.listPrice)}</td>
        <td class="num">${c.soldPrice ? fmtShort(c.soldPrice) : '—'}</td>
        <td class="num">$${ppsfOf(c)}</td>
        <td class="num">${c.lotSize}</td>
        <td class="num">${c.dom}</td>
      </tr>`).join('');

    const prices = D.comps.map(priceOf);
    const main = `
      <div class="sec-title" style="margin-bottom:18px">
        <span class="eyebrow gold">Comparables</span>
        <h1 class="h1">Six nearby homes, measured against yours.</h1>
      </div>
      <table class="ctable">
        <thead><tr>
          <th>Address &amp; Status</th><th>Bed / Bath</th><th>Sq Ft</th>
          <th>List</th><th>Sold</th><th>$/Sq Ft</th><th>Lot Size</th><th>DOM</th>
        </tr></thead>
        <tbody>${rows}</tbody>
      </table>
      <div class="summary-strip">
        <div class="cell"><span class="label">Average list</span><div class="v">${fmtShort(mean(D.comps.map((c) => c.listPrice)))}</div></div>
        <div class="cell"><span class="label">Average $/Sq Ft</span><div class="v">$${Math.round(mean(D.comps.map(ppsfOf)))}</div></div>
        <div class="cell"><span class="label">Average DOM</span><div class="v">${Math.round(mean(D.comps.map((c) => c.dom)))}</div></div>
        <div class="cell"><span class="label">Price range</span><div class="v">${fmtShort(Math.min(...prices))}–${fmtShort(Math.max(...prices))}</div></div>
      </div>`;
    contentPage('Comparables', 'Comparables Table', main);
  }

  /* ============================================================
     4 — PER-PROPERTY PAGES
     ============================================================ */
  function featureRows(f) {
    return Object.keys(f).map((k) => `<div class="feat-row"><div class="fk">${k}</div><div class="fv">${f[k]}</div></div>`).join('');
  }
  function propertyPage(c, i) {
    const thumbs = Array.from({ length: 3 }).map((_, j) =>
      `<image-slot id="comp-${i}-ph-${j}" shape="rect" fit="cover"${c.gallery && c.gallery[j] ? ` src="${c.gallery[j]}"` : ''} placeholder="Photo"></image-slot>`).join('');
    const main = `
      <div class="sec-title" style="margin-bottom:12px">
        <div style="display:flex;align-items:flex-end;justify-content:space-between;gap:16px">
          <div style="display:flex;flex-direction:column;gap:9px">
            <span class="eyebrow gold">Comparable 0${i + 1} · ${c.cityStateZip.split(',')[0]}</span>
            <h1 class="h1">${c.address}</h1>
          </div>
          <span class="status ${statusClass(c.status)}" style="padding-bottom:6px"><span class="mk"></span><span class="tx">${c.status}</span></span>
        </div>
      </div>

      <div class="pd-strip">
        <div class="cell"><div class="k">List Price</div><div class="v">${fmtShort(c.listPrice)}</div></div>
        <div class="cell"><div class="k">${c.soldPrice ? 'Sold Price' : 'Status'}</div><div class="v sm">${c.soldPrice ? fmtShort(c.soldPrice) : c.status}</div></div>
        <div class="cell"><div class="k">$/Sq Ft</div><div class="v">$${ppsfOf(c)}</div></div>
        <div class="cell"><div class="k">DOM</div><div class="v">${c.dom}</div></div>
        <div class="cell"><div class="k">MLS #</div><div class="v sm">${c.mls}</div></div>
        <div class="cell"><div class="k">${c.soldPrice ? 'Sold' : 'Year Built'}</div><div class="v sm">${c.soldPrice ? c.soldDate : c.yearBuilt}</div></div>
      </div>

      <div style="margin-bottom:14px"><image-slot id="comp-${i}-hero" shape="rect" fit="cover"${c.heroPhoto ? ` src="${c.heroPhoto}"` : ''} placeholder="Drop the main photo for ${c.address}" style="display:block;width:100%;height:2.15in"></image-slot></div>

      <div class="pd-cols">
        <div class="pd-left">
          <h2 class="h2" style="margin-bottom:12px">Key Detail</h2>
          <div class="pd-key">
            <div><div class="k">Bed</div><div class="v">${c.beds}</div></div>
            <div><div class="k">Bath</div><div class="v">${c.baths}</div></div>
            <div><div class="k">Sq Ft</div><div class="v">${c.sqft.toLocaleString()}</div></div>
            <div><div class="k">Lot Size</div><div class="v">${c.lotSize}</div></div>
            <div><div class="k">Year Built</div><div class="v">${c.yearBuilt}</div></div>
            <div><div class="k">Garage</div><div class="v">${c.garage}</div></div>
            <div><div class="k">HOA</div><div class="v">${c.hoa}</div></div>
            <div><div class="k">Type</div><div class="v" style="font-size:10.5px">${c.type}</div></div>
          </div>
          <div class="gallery" style="grid-template-columns:repeat(3,1fr);margin-top:16px;display:grid;gap:8px">${thumbs}</div>
        </div>
        <div class="pd-desc">
          <h2 class="h2" style="margin-bottom:8px">Property Description</h2>
          <p class="body" style="margin:0 0 14px">${c.description}</p>
          ${featureRows(c.features)}
        </div>
      </div>`;
    contentPage('Comparable Detail', c.address, main);
  }

  /* ============================================================
     5 — AVERAGE $/SQ FT CHART
     ============================================================ */
  function chartPage() {
    const W = 700, H = 372, PAD = { l: 60, r: 16, t: 14, b: 34 };
    const pts = D.comps.map((c) => ({ x: c.sqft, y: priceOf(c), s: statusClass(c.status) }));
    const subj = { x: D.subject.sqft, y: D.pricing.estimatedValue };
    const xs = pts.map((p) => p.x).concat(subj.x);
    const ys = pts.map((p) => p.y).concat(subj.y);
    const xMin = Math.floor((Math.min(...xs) - 200) / 100) * 100;
    const xMax = Math.ceil((Math.max(...xs) + 200) / 100) * 100;
    const yMin = Math.floor((Math.min(...ys) - 60000) / 100000) * 100000;
    const yMax = Math.ceil((Math.max(...ys) + 60000) / 100000) * 100000;
    const sx = (v) => PAD.l + ((v - xMin) / (xMax - xMin)) * (W - PAD.l - PAD.r);
    const sy = (v) => H - PAD.b - ((v - yMin) / (yMax - yMin)) * (H - PAD.t - PAD.b);

    // linear regression over comps
    const n = pts.length, sxm = mean(pts.map((p) => p.x)), sym = mean(pts.map((p) => p.y));
    let num = 0, den = 0;
    pts.forEach((p) => { num += (p.x - sxm) * (p.y - sym); den += (p.x - sxm) ** 2; });
    const slope = num / den, intercept = sym - slope * sxm;
    const ry1 = slope * xMin + intercept, ry2 = slope * xMax + intercept;

    // gridlines + labels
    let grid = '';
    const ySteps = 6;
    for (let i = 0; i <= ySteps; i++) {
      const v = yMin + ((yMax - yMin) / ySteps) * i;
      grid += `<line class="grid" x1="${PAD.l}" y1="${sy(v)}" x2="${W - PAD.r}" y2="${sy(v)}"/>`;
      grid += `<text class="ylab" x="${PAD.l - 8}" y="${sy(v) + 3}" text-anchor="end">${fmtShort(v)}</text>`;
    }
    const xSteps = 5;
    let xlab = '';
    for (let i = 0; i <= xSteps; i++) {
      const v = xMin + ((xMax - xMin) / xSteps) * i;
      xlab += `<text class="xlab" x="${sx(v)}" y="${H - 12}" text-anchor="middle">${Math.round(v).toLocaleString()}</text>`;
    }
    const dots = pts.map((p) => `<circle class="dot-${p.s}" cx="${sx(p.x)}" cy="${sy(p.y)}" r="6"/>`).join('');
    const subjDot = `<circle class="dot-subject" cx="${sx(subj.x)}" cy="${sy(subj.y)}" r="7.5"/>
      <text x="${sx(subj.x)}" y="${sy(subj.y) - 14}" text-anchor="middle" style="font-family:var(--rh-font-display);font-weight:700;font-size:12px;fill:var(--pg-fg)">Your home</text>`;

    const avgP = Math.round(mean(D.comps.map(ppsfOf)));
    const main = `
      <div class="sec-title" style="margin-bottom:6px">
        <span class="eyebrow gold">Average Price per Square Foot</span>
        <h1 class="h1">Comparable homes trade around <span class="gold">$${avgP}</span> a square foot.</h1>
      </div>
      <div class="chart-wrap">
        <div class="chart-legend">
          ${legendItem('active', 'Active')}${legendItem('pending', 'Pending')}${legendItem('sold', 'Sold')}
        </div>
        <svg class="chart-svg" viewBox="0 0 ${W} ${H}" preserveAspectRatio="xMidYMid meet">
          <g class="axis">${grid}${xlab}</g>
          <line class="trend" x1="${sx(xMin)}" y1="${sy(ry1)}" x2="${sx(xMax)}" y2="${sy(ry2)}"/>
          ${dots}${subjDot}
          <text class="xlab" x="${(W) / 2}" y="${H - 0}" text-anchor="middle" style="font-size:9px;fill:var(--pg-muted)"></text>
        </svg>
        <div class="body muted sm" style="text-align:center">Living area (Sq Ft) → · Price ↑ · gold line shows the price-to-size trend across the comparable set.</div>
      </div>`;
    contentPage('Price per Sq Ft', 'Price / Sq Ft', main);
  }

  /* ============================================================
     6 — ESTIMATED MARKET VALUE
     ============================================================ */
  function estimatePage() {
    const p = D.pricing, s = D.subject;
    const avgPrice = mean(D.comps.map(priceOf));
    const avgPpsf = Math.round(mean(D.comps.map(ppsfOf)));
    const subjPpsf = Math.round(p.estimatedValue / s.sqft);
    const deltaPct = Math.round(((subjPpsf - avgPpsf) / avgPpsf) * 100);
    const dirWord = deltaPct === 0 ? 'in line with' : deltaPct < 0 ? `${Math.abs(deltaPct)}% below` : `${deltaPct}% above`;
    const main = `
      <div class="sec-title" style="margin-bottom:16px">
        <span class="eyebrow gold">Estimated Market Value</span>
        <h1 class="h1" style="white-space:nowrap;max-width:none">Your home's value, and the price that sells it.</h1>
      </div>
      <div class="est-hero">
        <div class="est-band">${icon('pin')} ${s.address}, ${s.cityStateZip}</div>
        <div class="est-photo"><image-slot id="${s.photoSlot}" shape="rect" fit="cover"${s.defaultPhoto ? ` src="${s.defaultPhoto}"` : ''} placeholder="Subject property photo"></image-slot></div>
        <div class="est-figures">
          <div><span class="label">Approximate market value</span><div class="big">${fmt(p.estimatedValue)}</div></div>
          <div><span class="label">Estimated price range</span><div class="big fg">${fmt(p.rangeLow)} – ${fmt(p.rangeHigh)}</div></div>
        </div>
      </div>
      <p class="body muted sm" style="margin:14px 0 0">${p.rationale}</p>
      <h2 class="h2" style="margin:22px 0 0">Compared with the selected comps</h2>
      <div class="compare-grid">
        <div class="cell"><span class="label">Average comp price</span><div class="v">${fmtShort(avgPrice)}</div></div>
        <div class="cell"><span class="label">Average $/Sq Ft</span><div class="v">$${avgPpsf}</div></div>
        <div class="cell"><span class="label">Your $/Sq Ft</span><div class="v">$${subjPpsf}</div><div class="delta">${dirWord} the comp average</div></div>
      </div>`;
    contentPage('Estimated Value', 'Estimated Value', main);
  }

  /* ============================================================
     7 — MARKETING ACTION PLAN
     ============================================================ */
  function marketingPage() {
    const m = D.marketing;
    const beat = (b) => `<div class="lbeat"><span class="ltime">${b.time}</span><div class="lact"><b>${b.label}</b><span>${b.note}</span></div></div>`;
    const half = Math.ceil(m.launchDay.length / 2);
    const col1 = m.launchDay.slice(0, half).map(beat).join('');
    const col2 = m.launchDay.slice(half).map(beat).join('');
    const dayCard = (d) => `
      <div class="day-card">
        <div class="dc-ic">${icon(d.icon)}</div>
        <div class="dc-day">${d.day}</div>
        <div class="dc-act">${d.act}</div>
        <div class="dc-hrs">${d.hrs}</div>
      </div>`;
    const weekRow1 = m.weeklyCadence.slice(0, 4).map(dayCard).join('');
    const weekRow2 = m.weeklyCadence.slice(4).map(dayCard).join('');
    const rules = m.priceRule.rules.map((r) =>
      `<div class="r10"><div class="rn">${r.n}</div><div class="rt">${r.text}</div></div>`).join('');
    const comms = m.communication.items.map((c) =>
      `<div class="cl">${icon(c.icon)}<span>${c.text}</span></div>`).join('');
    const main = `
      <div class="sec-title" style="margin-bottom:13px">
        <span class="eyebrow gold">Marketing Action Plan</span>
        <h1 class="h1">Your launch, planned down to the hour.</h1>
      </div>
      <div class="mkt">
        <div>
          <div class="mkt-subhead">${icon('megaphone')}<span class="sh-t">Launch Day</span></div>
          <div class="launch-grid"><div class="launch-col">${col1}</div><div class="launch-col">${col2}</div></div>
        </div>
        <div>
          <div class="mkt-subhead">${icon('calendar')}<span class="sh-t">Then, Every Week</span></div>
          <div class="week-strip"><div class="week-row r1">${weekRow1}</div><div class="week-row r2">${weekRow2}</div></div>
        </div>
        <div class="mkt-band">
          <div class="band-card"><div class="bc-title">${m.priceRule.title}</div><div class="rule10">${rules}</div></div>
          <div class="band-card"><div class="bc-title">${m.communication.title}</div><div class="comms-list">${comms}</div></div>
        </div>
      </div>`;
    contentPage('Marketing Plan', 'Marketing Plan', main);
  }

  /* ============================================================
     8 — THE VALUE OF AN AGENT
     ============================================================ */
  function agentValuePage() {
    const tiles = D.agentValue.map((v) => `
      <div class="vtile">
        <div class="vt-ic">${icon(v.icon)}</div>
        <div class="vt-stat">${v.stat}</div>
        <div class="vt-title">${v.title}</div>
        <div class="vt-text">${v.text}</div>
      </div>`).join('');
    const main = `
      <div class="sec-title" style="margin-bottom:14px">
        <span class="eyebrow gold">The Value of an Agent</span>
        <h1 class="h1">Why sellers still list with a professional.</h1>
      </div>
      <p class="body muted" style="margin:0 0 18px;max-width:5.7in">A great agent is leverage, not a cost. Sharp pricing, full-market exposure, and steady negotiation lead to more money, fewer surprises, and a cleaner close than selling on your own.</p>
      <div class="vtiles">${tiles}</div>
      <div class="vbottom">
        <div class="vb-ic">${icon('trending-up')}</div>
        <div class="vb-x">
          <div class="vb-t">The data points one way.</div>
          <div class="vb-n">More buyers reached, stronger offers, and a faster sale when a professional runs the launch.</div>
        </div>
      </div>
      <p class="body muted sm" style="margin-top:12px">Figures are national averages from industry research and are provided for context.</p>`;
    contentPage('Value of an Agent', 'Value of an Agent', main);
  }

  /* ============================================================
     9 — ESTIMATED NET PROCEEDS
     ============================================================ */
  function proceedsPage() {
    const pr = D.proceeds;
    const rows = pr.costs.map((c) => {
      const amt = pr.salePrice * (c.pct / 100);
      return `<tr><td><div class="pl">${c.label}</div><div class="pn">${c.note} · ${c.pct}%</div></td><td class="r">${fmt(amt)}</td></tr>`;
    }).join('');
    const totalPct = pr.costs.reduce((a, c) => a + c.pct, 0);
    const totalCost = pr.salePrice * (totalPct / 100);
    const net = pr.salePrice - totalCost;
    const netLow = pr.salePrice * (pr.netLowPct / 100);
    const netHigh = pr.salePrice * (pr.netHighPct / 100);
    const main = `
      <div class="sec-title" style="margin-bottom:8px">
        <span class="eyebrow gold">Estimated Net Proceeds</span>
        <h1 class="h1">What you keep at a ${fmt(pr.salePrice)} sale.</h1>
      </div>
      <p class="body muted sm" style="margin:0 0 14px">In this market, sellers typically net <b class="gold">${pr.netLowPct}–${pr.netHighPct}%</b> of the final sale price, roughly <b>${fmt(netLow)}</b> to <b>${fmt(netHigh)}</b>. The line items below show one illustrative path to that range.</p>
      <table class="proceeds-table">
        <tbody>${rows}
          <tr><td><div class="pl">Total selling costs</div><div class="pn">${totalPct.toFixed(1)}% of sale price</div></td><td class="r"><b>${fmt(totalCost)}</b></td></tr>
        </tbody>
      </table>
      <div class="proceeds-eq">
        <div class="box"><div class="bl">Sale price</div><div class="bv">${fmt(pr.salePrice)}</div></div>
        <div class="op">−</div>
        <div class="box"><div class="bl">Selling costs</div><div class="bv">${fmt(totalCost)}</div></div>
        <div class="op">=</div>
        <div class="box net"><div class="bl">Net to you</div><div class="bv">${fmt(net)}</div></div>
      </div>
      <p class="body muted sm" style="margin-top:16px">${pr.note}</p>
      <div class="proceeds-aster"><p><span class="ast">*</span> Typically, the seller nets 92–95% of the final purchase price.</p></div>`;
    contentPage('Net Proceeds', 'Net Proceeds', main);
  }

  /* ============================================================
     10 — CLOSING
     ============================================================ */
  function closing() {
    const a = D.agent;
    addPage(`
      <div class="closing">
        <image-slot class="bg" id="${D.subject.photoSlot}" shape="rect" fit="cover"${D.subject.defaultPhoto ? ` src="${D.subject.defaultPhoto}"` : ''} placeholder=""></image-slot>
        <div class="scrim"></div>
        <div class="cl-inner">
          <div class="cl-photo"><img src="${a.headshot}" alt="${a.name}"></div>
          <p class="cl-note">${a.closingNote}</p>
          <hr class="rule" style="background:var(--rh-gold)">
          <div class="cl-name">${a.name}</div>
          <div class="cl-contact">
            <div>${a.phone}</div>
            <div>${a.email}</div>
            <div>${a.address}</div>
            <div>${a.web}</div>
          </div>
          <div class="cl-broker"><img src="assets/real-broker-outline.png" alt="Real Broker"><span>Brokered by ${a.brokerage}</span></div>
        </div>
      </div>`, { role: 'closing', cls: 'page--bleed', label: 'Closing' });
  }

  /* ============================================================
     BUILD
     ============================================================ */
  function build() {
    $doc.innerHTML = '';
    pageNo = 0;
    cover();
    mapPage();
    compsTable();
    D.comps.forEach((c, i) => propertyPage(c, i));
    chartPage();
    estimatePage();
    marketingPage();
    agentValuePage();
    proceedsPage();
    closing();
    applyTreatment(window.__cmaTreatment || 'mixed');
  }

  /* ---------- treatment switch ---------- */
  function applyTreatment(t) {
    window.__cmaTreatment = t;
    document.querySelectorAll('.page').forEach((pg) => {
      const role = pg.dataset.role;
      let tone;
      if (t === 'light') tone = role === 'cover' || role === 'closing' ? 'warm' : 'light';
      else if (t === 'dark') tone = 'dark';
      else tone = (role === 'cover' || role === 'closing') ? 'dark' : (role === 'content' ? 'light' : 'light');
      // mixed: cover+closing dark, content warm-white alternating? keep clean white
      pg.dataset.tone = tone === 'light' ? '' : tone;
      if (tone === 'light') pg.removeAttribute('data-tone');
    });
    // closing always renders on dark scrim regardless; cover honors tone
    document.querySelectorAll('#toolbar .seg button').forEach((b) =>
      b.classList.toggle('on', b.dataset.t === t));
  }
  window.cmaApplyTreatment = applyTreatment;

  build();
})();

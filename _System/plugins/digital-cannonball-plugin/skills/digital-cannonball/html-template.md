# HTML Template — Digital Cannonball

The HTML Generator agent uses this template to produce the final `index.html`. Replace every `{{PLACEHOLDER}}` token with actual data. No bracket tokens should remain in the output.

If a data point is missing, follow the fallback instructions in the comments next to each placeholder.

---

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Home analysis for {{ADDRESS_SHORT}}</title>
  <meta name="description" content="{{META_DESCRIPTION}}">
  <meta name="robots" content="noindex, nofollow">
  <meta property="og:title" content="Home analysis for {{ADDRESS_SHORT}}">
  <meta property="og:description" content="{{META_DESCRIPTION}}">
  <meta property="og:image" content="{{HERO_PHOTO_URL}}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Home analysis for {{ADDRESS_SHORT}}">
  <meta name="twitter:description" content="{{META_DESCRIPTION}}">
  <meta name="twitter:image" content="{{HERO_PHOTO_URL}}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

    :root {
      --coral: #FF5C4D;
      --coral-light: #FF7A6E;
      --amber: #FF8C42;
      --ink: #0a0a0a;
      --charcoal: #3a3a3a;
      --stone: #8a8680;
      --warm-gray: #9a9590;
      --border-light: rgba(10,10,10,0.1);
      --border-dark: rgba(255,255,255,0.08);
      --border-dark-strong: rgba(255,255,255,0.18);
      --bg-page: #ffffff;
      --bg-cream: #faf7f0;
      --bg-dark: #0a0a0a;
      --text-primary: #0a0a0a;
      --text-secondary: #3a3a3a;
      --text-muted: #8a8680;
      --text-on-dark: #ffffff;
      --text-on-dark-muted: rgba(255,255,255,0.55);
      --text-on-dark-body: #faf7f0;
    }

    html { scroll-behavior: smooth; }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-weight: 300;
      background: var(--bg-page);
      color: var(--text-primary);
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      min-height: 100vh;
    }

    ::selection { background: var(--coral); color: #fff; }

    .cb-display {
      font-family: 'Playfair Display', Georgia, serif;
      font-feature-settings: 'kern';
    }
    .cb-display-italic {
      font-family: 'Playfair Display', Georgia, serif;
      font-style: italic;
      font-feature-settings: 'kern';
    }
    .cb-mono {
      font-family: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
    }

    .cb-page-pad {
      padding-left: clamp(24px, 5vw, 56px);
      padding-right: clamp(24px, 5vw, 56px);
      max-width: 1140px;
      margin: 0 auto;
    }

    .cb-kicker {
      font-family: 'Inter', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--coral);
      display: inline-block;
      margin-bottom: 22px;
    }

    .cb-stat-label {
      font-family: 'Inter', sans-serif;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--stone);
      margin-bottom: 18px;
    }

    .cb-stat-number {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: clamp(32px, 4.5vw, 51px);
      font-weight: 500;
      letter-spacing: -0.03em;
      line-height: 0.95;
      color: var(--text-primary);
      font-variant-numeric: tabular-nums lining-nums;
    }

    .cb-body {
      font-family: 'Inter', sans-serif;
      font-size: 18px;
      line-height: 1.72;
      color: var(--text-secondary);
      font-weight: 300;
    }

    /* Fade-in animation */
    .cb-reveal {
      opacity: 0;
      transform: translateY(10px);
      transition: opacity 0.55s cubic-bezier(0.33, 1, 0.68, 1),
                  transform 0.55s cubic-bezier(0.33, 1, 0.68, 1);
    }
    .cb-reveal.visible {
      opacity: 1;
      transform: translateY(0);
    }
    .cb-reveal.d1 { transition-delay: 60ms; }
    .cb-reveal.d2 { transition-delay: 120ms; }
    .cb-reveal.d3 { transition-delay: 160ms; }
    .cb-reveal.d4 { transition-delay: 200ms; }
    .cb-reveal.d5 { transition-delay: 240ms; }

    /* ── Side Navigation ── */
    .cb-section-nav {
      position: fixed;
      top: 50%;
      left: clamp(4px, 1vw, 12px);
      transform: translateY(-50%);
      z-index: 50;
      display: flex;
      flex-direction: column;
      gap: 14px;
      padding: 12px 10px;
    }
    .cb-section-nav a {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      transition: opacity 280ms;
      opacity: 0.55;
    }
    .cb-section-nav a.active { opacity: 1; }
    .cb-section-nav a .dot {
      width: 14px;
      height: 2px;
      background: var(--stone);
      transition: width 360ms cubic-bezier(0.22,1,0.36,1), background 280ms;
    }
    .cb-section-nav a.active .dot {
      width: 28px;
      background: var(--coral);
    }
    .cb-section-nav a .num {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--stone);
      transition: color 280ms;
    }
    .cb-section-nav a.active .num { color: var(--coral); }

    /* ── Hero ── */
    .cb-hero-photo {
      position: relative;
      aspect-ratio: 16/9;
      background: var(--bg-cream);
      overflow: hidden;
      border-radius: 16px;
      box-shadow: 0 1px 0 rgba(10,10,10,0.04);
    }
    .cb-hero-photo img {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .cb-hero-ticker {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      border-top: 1px solid var(--ink);
      border-bottom: 1px solid var(--border-light);
    }
    .cb-hero-ticker > div {
      padding: 32px clamp(16px, 3vw, 28px);
    }
    .cb-hero-ticker > div + div {
      border-left: 1px solid var(--border-light);
    }

    /* ── Listed vs Launched ── */
    .cb-lvl-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid rgba(10,10,10,0.05);
    }

    /* ── Dark Cards ── */
    .cb-dark-card {
      background: var(--bg-dark);
      color: var(--text-on-dark);
      border: 1px solid var(--ink);
      padding: clamp(24px, 3.5vw, 36px);
      border-radius: 12px;
    }
    .cb-dark-card .card-label {
      font-family: 'Inter', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--amber);
      margin-bottom: 8px;
    }
    .cb-dark-card .card-sublabel {
      font-family: 'Playfair Display', Georgia, serif;
      font-style: italic;
      font-size: 18px;
      color: rgba(255,255,255,0.62);
      font-weight: 400;
    }

    /* ── Comp Rows ── */
    .cb-comp-row {
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 18px;
      align-items: center;
      padding: 16px 4px;
      border-bottom: 1px solid var(--border-dark);
    }
    .cb-comp-row:last-child { border-bottom: none; }
    .cb-comp-address {
      font-family: 'Inter', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: var(--text-on-dark);
      line-height: 1.35;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      letter-spacing: -0.005em;
    }
    .cb-comp-detail {
      font-family: 'Inter', sans-serif;
      font-size: 13px;
      color: var(--text-on-dark-muted);
      letter-spacing: 0.02em;
      margin-top: 5px;
      font-weight: 300;
    }
    .cb-comp-price {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 22px;
      font-weight: 500;
      color: var(--text-on-dark);
      font-variant-numeric: tabular-nums lining-nums;
      letter-spacing: -0.015em;
      white-space: nowrap;
    }

    /* ── Market Stats Grid ── */
    .cb-market-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      background: var(--bg-dark);
      border: 1px solid var(--ink);
      border-radius: 12px;
      overflow: hidden;
    }
    .cb-market-cell {
      padding: 36px 28px 32px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .cb-market-cell + .cb-market-cell {
      border-left: 1px solid rgba(255,255,255,0.1);
    }
    .cb-market-cell .stat-label {
      font-family: 'Inter', sans-serif;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--text-on-dark-muted);
    }
    .cb-market-cell .stat-value {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: clamp(38px, 4.3vw, 54px);
      font-weight: 500;
      letter-spacing: -0.035em;
      line-height: 0.95;
      color: var(--text-on-dark);
      font-variant-numeric: tabular-nums lining-nums;
    }

    /* ── Plan Section ── */
    .cb-plan-act {
      display: grid;
      grid-template-columns: clamp(70px, 10vw, 140px) 1fr;
      gap: clamp(20px, 3vw, 40px);
      align-items: start;
    }
    .cb-plan-act .act-label {
      font-family: 'Inter', sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--coral);
      padding-top: 6px;
    }
    .cb-plan-act .act-title {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: clamp(22px, 2.6vw, 32px);
      font-weight: 400;
      color: var(--text-primary);
      line-height: 1.08;
      letter-spacing: -0.02em;
      margin: 0 0 6px;
    }
    .cb-plan-act .act-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 10.5px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--stone);
      margin-bottom: 28px;
    }

    .cb-step {
      display: grid;
      grid-template-columns: 48px 1fr;
      gap: 20px;
      padding: 18px 0;
      border-bottom: 1px solid var(--border-light);
    }
    .cb-step:first-child {
      border-top: 1px solid var(--border-light);
    }
    .cb-step .step-num {
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      color: var(--stone);
      line-height: 1.5;
      padding-top: 4px;
      font-weight: 500;
    }
    .cb-step .step-title {
      font-family: 'Inter', sans-serif;
      font-size: 18px;
      font-weight: 400;
      color: var(--text-primary);
      line-height: 1.4;
      margin-bottom: 8px;
      letter-spacing: -0.005em;
    }
    .cb-step .step-body {
      font-family: 'Inter', sans-serif;
      font-size: 16px;
      color: var(--text-secondary);
      line-height: 1.65;
    }

    /* ── Callout ── */
    .cb-callout {
      border-top: 1px solid var(--ink);
      padding-top: 28px;
      display: grid;
      grid-template-columns: minmax(0, 160px) 1fr;
      gap: 32px;
      align-items: baseline;
    }
    .cb-callout .callout-label {
      font-family: 'Inter', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--coral);
    }
    .cb-callout .callout-body {
      font-family: 'Inter', sans-serif;
      font-size: 19px;
      line-height: 1.55;
      color: var(--text-primary);
      font-weight: 500;
      letter-spacing: -0.005em;
    }

    /* ── Timeline ── */
    .cb-timeline {
      position: relative;
      padding-left: 32px;
    }
    .cb-timeline::before {
      content: '';
      position: absolute;
      left: 7px;
      top: 8px;
      bottom: 8px;
      width: 1px;
      background: var(--border-light);
    }
    .cb-timeline-item {
      position: relative;
      padding-bottom: 28px;
    }
    .cb-timeline-item:last-child { padding-bottom: 0; }
    .cb-timeline-item .dot {
      position: absolute;
      left: -30px;
      top: 6px;
      width: 11px;
      height: 11px;
      border-radius: 50%;
      border: 2px solid var(--ink);
      background: #fff;
      box-shadow: 0 0 0 4px #fff;
    }
    .cb-timeline-item:first-child .dot {
      background: var(--coral);
      border-color: var(--coral);
    }
    .cb-timeline-item .tl-date {
      font-family: 'Inter', sans-serif;
      font-size: 11px;
      font-weight: 600;
      color: var(--stone);
      letter-spacing: 0.18em;
      text-transform: uppercase;
      margin-bottom: 6px;
    }
    .cb-timeline-item .tl-row {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }
    .cb-timeline-item .tl-event {
      font-family: 'Inter', sans-serif;
      font-size: 17px;
      color: var(--text-primary);
      font-weight: 400;
      letter-spacing: -0.005em;
    }
    .cb-timeline-item .tl-change-up {
      margin-left: 10px;
      font-size: 13px;
      color: var(--stone);
      font-weight: 500;
    }
    .cb-timeline-item .tl-change-down {
      margin-left: 10px;
      font-size: 13px;
      color: var(--coral);
      font-weight: 500;
    }
    .cb-timeline-item .tl-price {
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 20px;
      font-weight: 500;
      color: var(--text-primary);
      font-variant-numeric: tabular-nums lining-nums;
      letter-spacing: -0.015em;
    }

    /* ── Signature ── */
    .cb-signature-row {
      display: grid;
      grid-template-columns: auto 1fr;
      gap: clamp(24px, 3vw, 40px);
      align-items: center;
      padding: 32px 0;
      border-top: 1px solid var(--ink);
      border-bottom: 1px solid var(--border-light);
    }
    .cb-avatar {
      width: 96px;
      height: 96px;
      border-radius: 50%;
      background: var(--bg-cream);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 40px;
      color: var(--text-primary);
      font-weight: 600;
      overflow: hidden;
    }
    .cb-avatar img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 15%;
    }

    .cb-cta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-top: 32px;
    }
    .cb-cta-primary {
      display: block;
      padding: 24px 26px;
      background: var(--ink);
      color: var(--text-on-dark);
      text-decoration: none;
      transition: opacity 220ms;
    }
    .cb-cta-primary:hover { opacity: 0.85; }
    .cb-cta-secondary {
      display: block;
      padding: 22px 24px;
      background: transparent;
      color: var(--text-primary);
      border: 1px solid var(--ink);
      text-decoration: none;
      transition: background 220ms;
    }
    .cb-cta-secondary:hover { background: rgba(10,10,10,0.03); }

    /* ── Responsive ── */
    @media (max-width: 1100px) {
      .cb-section-nav { display: none !important; }
    }
    @media (max-width: 720px) {
      .cb-lvl-grid { grid-template-columns: 1fr !important; }
      .cb-market-grid { grid-template-columns: 1fr !important; }
      .cb-market-cell + .cb-market-cell {
        border-left: none;
        border-top: 1px solid rgba(255,255,255,0.1);
      }
      .cb-callout {
        grid-template-columns: 1fr !important;
        gap: 14px !important;
      }
    }
    @media (max-width: 640px) {
      .cb-plan-act { grid-template-columns: 1fr !important; gap: 14px !important; }
      .cb-signature-row { grid-template-columns: 1fr !important; text-align: left; }
      .cb-hero-photo { aspect-ratio: 4/3 !important; border-radius: 12px !important; }
    }
    @media (max-width: 560px) {
      .cb-hero-ticker {
        grid-template-columns: repeat(auto-fit, minmax(90px, 1fr)) !important;
        gap: 14px !important;
      }
    }
    @media (max-width: 400px) {
      .cb-page-pad { padding-left: 16px !important; padding-right: 16px !important; }
    }
  </style>
</head>
<body>

<!-- ═══════════════════ SIDE NAVIGATION ═══════════════════ -->
<nav aria-label="Report sections" class="cb-section-nav">
  <a href="#intro" class="active"><span class="dot"></span><span class="num">01</span></a>
  <a href="#insight-01"><span class="dot"></span><span class="num">02</span></a>
  <a href="#insight-02"><span class="dot"></span><span class="num">03</span></a>
  <a href="#insight-03"><span class="dot"></span><span class="num">04</span></a>
  <a href="#plan"><span class="dot"></span><span class="num">05</span></a>
  <a href="#contact"><span class="dot"></span><span class="num">06</span></a>
</nav>

<!-- ═══════════════════ HERO SECTION ═══════════════════ -->
<section id="hero" style="position:relative; background:var(--bg-page); color:var(--text-primary); padding:clamp(14px,2vw,24px) 0 0;">
  <div class="cb-page-pad">
    <!-- Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:clamp(18px,3vw,36px); border-bottom:1px solid var(--border-light); font-family:'Inter',sans-serif; font-size:13px; letter-spacing:0.06em; color:var(--text-primary);">
      <div style="font-weight:600;">Ryan Rose</div>
      <div style="color:var(--stone);">702-747-5921</div>
      <div style="color:var(--stone);">ryan@rosehomeslv.com</div>
      <div style="font-weight:400; text-transform:uppercase; letter-spacing:0.12em; font-size:11px; color:var(--stone);">Real Broker, LLC</div>
    </div>

    <!-- Address headline -->
    <div style="padding-top:clamp(56px,9vw,120px); padding-bottom:clamp(48px,7vw,80px); text-align:center;">
      <h1 class="cb-display" style="font-size:clamp(30px,5.1vw,72px); font-weight:500; line-height:0.98; letter-spacing:-0.025em; color:var(--text-primary); margin:0 auto; text-wrap:balance; max-width:1000px;">{{ADDRESS_SHORT}}</h1>
      <div class="cb-display-italic" style="margin-top:26px; font-size:clamp(14px,1.3vw,18px); color:var(--text-secondary); letter-spacing:0.005em; max-width:760px; line-height:1.45; margin-left:auto; margin-right:auto; font-weight:400;">{{HERO_SUBHEAD}}</div>
    </div>

    <!-- Property photo -->
    <div class="cb-hero-photo">
      <!-- FALLBACK: If {{HERO_PHOTO_URL}} is empty, use a gradient: background: linear-gradient(135deg, var(--bg-cream), #e8e4dc); -->
      <img alt="{{ADDRESS_SHORT}}" src="{{HERO_PHOTO_URL}}" onerror="this.style.display='none'; this.parentElement.style.background='linear-gradient(135deg, #faf7f0, #e8e4dc)';">
    </div>

    <!-- Stats strip -->
    <div class="cb-hero-ticker">
      <div>
        <div class="cb-stat-label">Days on market</div>
        <div class="cb-stat-number" style="display:flex; align-items:baseline; gap:10px;">
          <span>{{DAYS_ON_MARKET}}</span>
          <span class="cb-display-italic" style="font-size:0.42em; font-weight:400; color:var(--stone); letter-spacing:0; text-transform:lowercase;">days</span>
        </div>
      </div>
      <div>
        <div class="cb-stat-label">List price</div>
        <div class="cb-stat-number"><span>{{LIST_PRICE_SHORT}}</span></div>
      </div>
      <div>
        <!-- FALLBACK: If no zestimate, change label to "Est. Value" and show "N/A" -->
        <div class="cb-stat-label">{{THIRD_STAT_LABEL}}</div>
        <div class="cb-stat-number"><span>{{THIRD_STAT_VALUE}}</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════ 01 / OVERVIEW ═══════════════════ -->
<section id="intro" style="padding:clamp(72px,9vw,128px) 0; background:var(--bg-page); border-top:1px solid var(--border-light);">
  <div class="cb-page-pad">
    <div class="cb-reveal"><div class="cb-kicker">01 / Overview</div></div>

    <div class="cb-reveal d1">
      <p class="cb-display" style="font-weight:500; font-size:clamp(27px,3.5vw,45px); line-height:1.1; letter-spacing:-0.025em; color:var(--text-primary); margin:0 0 48px; text-wrap:balance;">{{OVERVIEW_LEDE}}</p>
    </div>

    <div class="cb-reveal d2">
      <p class="cb-body" style="margin:0;">{{OVERVIEW_BODY}}</p>
    </div>

    <!-- About the home -->
    <div class="cb-reveal d3" style="margin-top:64px;">
      <div class="cb-stat-label" style="margin-bottom:14px;">About the home</div>
      <p class="cb-body" style="font-size:17px; margin:0;">{{PROPERTY_DESCRIPTION}}</p>
    </div>

    <!-- Listing history timeline -->
    <div class="cb-reveal d4" style="margin-top:64px;">
      <div class="cb-kicker" style="margin-bottom:22px;">Listing history</div>
      <div class="cb-timeline">
        {{TIMELINE_ITEMS}}
        <!-- Each timeline item uses this pattern:
        <div class="cb-timeline-item">
          <span class="dot"></span>
          <div class="tl-date">MMM DD, YYYY</div>
          <div class="tl-row">
            <div class="tl-event">Event name<span class="tl-change-down">-$XXK</span></div>
            <div class="tl-price">$X.XXM</div>
          </div>
        </div>
        -->
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════ 02 / MARKETING ANALYSIS ═══════════════════ -->
<section id="insight-01" style="position:relative; padding:clamp(72px,9vw,128px) 0; background:var(--bg-page); color:var(--text-primary); border-top:1px solid var(--border-light);">
  <div class="cb-page-pad">
    <div class="cb-reveal"><div class="cb-kicker">02 / Marketing analysis</div></div>

    <div class="cb-reveal d1">
      <h2 class="cb-display" style="font-size:clamp(32px,4.3vw,58px); font-weight:500; line-height:1.02; letter-spacing:-0.025em; margin:0 0 40px; text-wrap:balance;">{{MARKETING_HEADLINE}}</h2>
    </div>

    <div class="cb-reveal d2">
      <div style="margin-bottom:48px;">
        <p class="cb-body" style="margin:0;">{{MARKETING_BODY}}</p>
      </div>
    </div>

    <!-- Listed vs Launched -->
    <div class="cb-reveal d3">
      <div style="margin:0 0 48px;">
        <div class="cb-stat-label" style="padding-bottom:0; margin-bottom:28px;">The difference between listed and launched</div>
        <div class="cb-lvl-grid">
          <!-- Left: Most Listings -->
          <div style="background:var(--bg-cream); padding:clamp(28px,4vw,48px);">
            <div style="font-family:'Inter',sans-serif; font-size:11px; font-weight:700; letter-spacing:0.22em; text-transform:uppercase; color:var(--stone); margin-bottom:28px;">MOST LISTINGS</div>
            <div style="display:flex; flex-direction:column; gap:22px;">
              {{LVL_LEFT_ITEMS}}
              <!-- Each item:
              <div style="display:flex; gap:16px;">
                <span style="width:8px; height:8px; border-radius:50%; background:var(--stone); margin-top:10px; flex-shrink:0; opacity:0.5;"></span>
                <div style="flex:1; min-width:0;">
                  <div class="cb-display" style="font-size:clamp(17px,1.7vw,21px); font-weight:500; line-height:1.25; letter-spacing:-0.01em; color:var(--text-primary); margin-bottom:6px;">Title</div>
                  <div style="font-family:'Inter',sans-serif; font-size:15px; line-height:1.6; color:var(--text-secondary); font-weight:300;">Body text</div>
                </div>
              </div>
              -->
            </div>
          </div>
          <!-- Right: Proactive Strategy -->
          <div style="background:var(--bg-dark); padding:clamp(28px,4vw,48px);">
            <div style="font-family:'Inter',sans-serif; font-size:11px; font-weight:700; letter-spacing:0.22em; text-transform:uppercase; color:var(--amber); margin-bottom:28px;">A PROACTIVE STRATEGY</div>
            <div style="display:flex; flex-direction:column; gap:22px;">
              {{LVL_RIGHT_ITEMS}}
              <!-- Each item:
              <div style="display:flex; gap:16px;">
                <span style="width:8px; height:8px; border-radius:50%; background:var(--coral); margin-top:10px; flex-shrink:0;"></span>
                <div style="flex:1; min-width:0;">
                  <div class="cb-display" style="font-size:clamp(17px,1.7vw,21px); font-weight:500; line-height:1.25; letter-spacing:-0.01em; color:var(--text-on-dark); margin-bottom:6px;">Title</div>
                  <div style="font-family:'Inter',sans-serif; font-size:15px; line-height:1.6; color:var(--text-on-dark-body); font-weight:300; opacity:0.78;">Body text</div>
                </div>
              </div>
              -->
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom line callout -->
    <div class="cb-reveal d4">
      <div class="cb-callout">
        <div class="callout-label">The bottom line</div>
        <p class="callout-body" style="margin:0;">{{MARKETING_CLOSING}}</p>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════ 03 / BUYER DEMAND ═══════════════════ -->
<section id="insight-02" style="position:relative; padding:clamp(72px,9vw,128px) 0; background:var(--bg-page); color:var(--text-primary); border-top:1px solid var(--border-light);">
  <div class="cb-page-pad">
    <div class="cb-reveal"><div class="cb-kicker">03 / Buyer demand</div></div>

    <div class="cb-reveal d1">
      <h2 class="cb-display" style="font-size:clamp(32px,4.3vw,58px); font-weight:500; line-height:1.02; letter-spacing:-0.025em; margin:0 0 40px; text-wrap:balance;">{{DEMAND_HEADLINE}}</h2>
    </div>

    <!-- Pull quote -->
    <div class="cb-reveal d2">
      <div style="margin:0 0 48px; padding:32px 0; border-top:1px solid var(--ink); border-bottom:1px solid var(--border-light);">
        <div class="cb-display-italic" style="font-size:clamp(19px,2.4vw,29px); font-weight:400; line-height:1.25; color:var(--text-primary); letter-spacing:-0.01em; text-wrap:balance;">"{{DEMAND_PULLQUOTE}}"</div>
      </div>
    </div>

    <div class="cb-reveal d3">
      <div style="margin-bottom:48px;">
        <p class="cb-body" style="margin:0;">{{DEMAND_BODY}}</p>
      </div>
    </div>

    <!-- Sold while listed card -->
    <div class="cb-reveal d4">
      <div style="display:flex; flex-direction:column; gap:56px;">
        <div class="cb-dark-card">
          <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:26px; flex-wrap:wrap; gap:12px;">
            <div>
              <div class="card-label">Sold while you sat</div>
              <div class="card-sublabel">{{LISTING_WINDOW_DATES}}</div>
            </div>
            <div style="font-family:'Inter',sans-serif; font-size:12px; letter-spacing:0.16em; text-transform:uppercase; color:var(--text-on-dark); font-weight:700;">Median sold &middot; {{COMPS_MEDIAN_PRICE}}</div>
          </div>
          <div style="border-top:1px solid var(--border-dark-strong); border-bottom:1px solid var(--border-dark);">
            {{COMP_ROWS}}
            <!-- Each comp row:
            <div class="cb-comp-row">
              <div style="min-width:0;">
                <div class="cb-comp-address" title="Full Address">Address</div>
                <div class="cb-comp-detail">X bd · X,XXX sqft · Mon DD, YYYY</div>
              </div>
              <div class="cb-comp-price">$X.XXM</div>
            </div>
            -->
          </div>
        </div>
      </div>
    </div>

    <!-- Why this matters callout -->
    <div class="cb-reveal d5" style="margin-top:48px;">
      <div class="cb-callout">
        <div class="callout-label">Why this matters</div>
        <p class="callout-body" style="margin:0;">{{DEMAND_CLOSING}}</p>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════ 04 / MARKET CONDITIONS ═══════════════════ -->
<section id="insight-03" style="position:relative; padding:clamp(72px,9vw,128px) 0; background:var(--bg-page); color:var(--text-primary); border-top:1px solid var(--border-light);">
  <div class="cb-page-pad">
    <div class="cb-reveal"><div class="cb-kicker">04 / Market conditions</div></div>

    <div class="cb-reveal d1">
      <h2 class="cb-display" style="font-size:clamp(32px,4.3vw,58px); font-weight:500; line-height:1.02; letter-spacing:-0.025em; margin:0 0 40px; text-wrap:balance;">{{MARKET_HEADLINE}}</h2>
    </div>

    <!-- Pull quote -->
    <div class="cb-reveal d2">
      <div style="margin:0 0 48px; padding:32px 0; border-top:1px solid var(--ink); border-bottom:1px solid var(--border-light);">
        <div class="cb-display-italic" style="font-size:clamp(19px,2.4vw,29px); font-weight:400; line-height:1.25; color:var(--text-primary); letter-spacing:-0.01em; text-wrap:balance;">"{{MARKET_PULLQUOTE}}"</div>
      </div>
    </div>

    <div class="cb-reveal d3">
      <div style="margin-bottom:48px;">
        <p class="cb-body" style="margin:0;">{{MARKET_BODY}}</p>
      </div>
    </div>

    <!-- 3-stat strip -->
    <div class="cb-reveal d4">
      <div class="cb-market-grid">
        <div class="cb-market-cell">
          <div class="stat-label">Year-over-year price change</div>
          <div class="stat-value">{{YOY_CHANGE}}</div>
        </div>
        <div class="cb-market-cell">
          <div class="stat-label">Median sold price</div>
          <div class="stat-value">{{MEDIAN_SOLD_PRICE}}</div>
          <div style="font-family:'Inter',sans-serif; font-size:13px; color:var(--text-on-dark-muted); font-weight:300;">{{MEDIAN_PRICE_SOURCE}}</div>
        </div>
        <div class="cb-market-cell">
          <div class="stat-label">Avg. days on market</div>
          <div class="stat-value" style="display:flex; align-items:baseline; gap:10px;">
            <span>{{AVG_DOM}}</span>
            <span class="cb-display-italic" style="font-size:0.32em; font-weight:400; color:rgba(255,255,255,0.62); letter-spacing:0;">days</span>
          </div>
        </div>
      </div>
    </div>

    <!-- What you can do with this -->
    <div class="cb-reveal d5" style="margin-top:48px;">
      <div class="cb-callout">
        <div class="callout-label">What you can do with this</div>
        <p class="callout-body" style="margin:0;">{{MARKET_CLOSING}}</p>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════ 05 / THE PLAN ═══════════════════ -->
<section id="plan" style="padding:clamp(80px,10vw,144px) 0; background:var(--bg-page); border-top:1px solid var(--border-light);">
  <div class="cb-page-pad">
    <div class="cb-reveal"><div class="cb-kicker">05 / The plan</div></div>

    <div class="cb-reveal d1">
      <h2 class="cb-display" style="font-size:clamp(38px,5.1vw,70px); font-weight:500; line-height:0.98; letter-spacing:-0.03em; margin:0 0 40px; text-wrap:balance;">{{PLAN_HEADLINE}}</h2>
    </div>

    {{PLAN_ACTS}}
    <!-- Each act block:
    <div style="padding-top:40px; padding-bottom:48px; border-top:1px solid var(--border-light);">
      <div class="cb-reveal d1">
        <div class="cb-plan-act">
          <div class="act-label">Act 01</div>
          <div>
            <h3 class="act-title">ACT TITLE</h3>
            <div class="act-tag">Act description tag line</div>
            <div>
              <div class="cb-step">
                <div class="step-num">01</div>
                <div>
                  <div class="step-title">Step title.</div>
                  <div class="step-body">Step body text.</div>
                </div>
              </div>
              ...more steps...
            </div>
          </div>
        </div>
      </div>
    </div>
    -->
  </div>
</section>

<!-- ═══════════════════ 06 / NEXT STEPS ═══════════════════ -->
<section id="contact" style="background:var(--bg-page); color:var(--text-primary); padding:clamp(80px,10vw,140px) 0 clamp(48px,6vw,80px); border-top:1px solid var(--border-light);">
  <div class="cb-page-pad">
    <div class="cb-reveal"><div class="cb-kicker">06 / Next steps</div></div>

    <div class="cb-reveal d1">
      <h2 class="cb-display" style="font-size:clamp(32px,4.3vw,58px); font-weight:500; line-height:1.02; letter-spacing:-0.025em; margin:0 0 64px; text-wrap:balance;">{{CONTACT_HEADLINE}}</h2>
    </div>

    <!-- Signature -->
    <div class="cb-reveal d2">
      <div class="cb-signature-row">
        <div class="cb-avatar">
          <img alt="Ryan Rose" src="https://www.dropbox.com/scl/fi/mta6tj7tj6y33jci10s4o/erasebg-transformed-1.png?rlkey=pmd2me4znnr3pyveozy7emrlg&st=nty9aoss&raw=1">
        </div>
        <div>
          <div style="font-family:'Inter',sans-serif; font-size:11px; font-weight:700; letter-spacing:0.14em; text-transform:uppercase; color:var(--stone); margin-bottom:10px;">Prepared by</div>
          <div class="cb-display" style="font-size:clamp(22px,2.6vw,32px); font-weight:500; line-height:1.1; letter-spacing:-0.02em; color:var(--text-primary); margin-bottom:6px;">Ryan Rose</div>
          <div style="font-family:'Inter',sans-serif; font-size:16px; color:var(--text-secondary); letter-spacing:0.005em;">Real Broker, LLC</div>
        </div>
      </div>
    </div>

    <!-- CTAs -->
    <div class="cb-reveal d3">
      <div class="cb-cta-grid">
        <a href="tel:7027475921" class="cb-cta-primary">
          <div style="font-family:'Inter',sans-serif; font-size:11px; font-weight:700; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:10px; opacity:0.85;">Call</div>
          <div class="cb-mono" style="font-size:22px; font-weight:500; letter-spacing:-0.01em;">702-747-5921</div>
        </a>
        <a href="mailto:ryan@rosehomeslv.com" class="cb-cta-secondary">
          <div style="font-family:'Inter',sans-serif; font-size:11px; font-weight:700; letter-spacing:0.14em; text-transform:uppercase; margin-bottom:8px; color:var(--stone);">Email</div>
          <div style="font-family:'Inter',sans-serif; font-size:17px; font-weight:500; word-break:break-all;">ryan@rosehomeslv.com</div>
        </a>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <div style="margin-top:clamp(64px,8vw,96px); padding:20px clamp(24px,5vw,56px); border-top:1px solid var(--border-light); display:flex; justify-content:center; font-family:'Inter',sans-serif; font-size:10px; font-weight:700; letter-spacing:0.14em; text-transform:uppercase; color:var(--stone); max-width:1140px; margin-left:auto; margin-right:auto;">
    <span>A private analysis &middot; Do not share</span>
  </div>
</section>

<!-- ═══════════════════ JAVASCRIPT ═══════════════════ -->
<script>
// Scroll-triggered reveal animations
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.15 });

document.querySelectorAll('.cb-reveal').forEach(el => observer.observe(el));

// Side navigation active state (scroll-position based)
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.cb-section-nav a');

function updateActiveNav() {
  const scrollY = window.scrollY + window.innerHeight * 0.3;
  let current = sections[0];
  sections.forEach(section => {
    if (section.offsetTop <= scrollY) current = section;
  });
  navLinks.forEach(link => link.classList.remove('active'));
  const activeLink = document.querySelector(`.cb-section-nav a[href="#${current.id}"]`);
  if (activeLink) activeLink.classList.add('active');
}

window.addEventListener('scroll', updateActiveNav, { passive: true });
updateActiveNav();
</script>

</body>
</html>
```

---

## Placeholder Reference

| Placeholder | Description | Fallback if missing |
|-------------|-------------|---------------------|
| `{{ADDRESS_SHORT}}` | Street address only (e.g., "9270 Swift Current Dr") | Required, no fallback |
| `{{META_DESCRIPTION}}` | 1-2 sentence page description for og/twitter meta | Use overview lede |
| `{{HERO_PHOTO_URL}}` | Zillow property photo URL (og:image) | JS onerror shows gradient |
| `{{HERO_SUBHEAD}}` | Italic subhead under address | Content writer generates |
| `{{DAYS_ON_MARKET}}` | Number of DOM | "N/A" |
| `{{LIST_PRICE_SHORT}}` | e.g., "$425K" or "$1.25M" | Required |
| `{{THIRD_STAT_LABEL}}` | "Zestimate" or "Est. Value" | "Est. Value" |
| `{{THIRD_STAT_VALUE}}` | Zestimate formatted | "N/A" |
| `{{OVERVIEW_LEDE}}` | Large serif opening statement | Content writer generates |
| `{{OVERVIEW_BODY}}` | Body paragraph(s) | Content writer generates |
| `{{PROPERTY_DESCRIPTION}}` | Beds/baths/sqft/type summary | Research agent extracts |
| `{{TIMELINE_ITEMS}}` | HTML string of timeline items | At least 1 item required |
| `{{MARKETING_HEADLINE}}` | Section 02 headline | Content writer generates |
| `{{MARKETING_BODY}}` | Section 02 body | Content writer generates |
| `{{LVL_LEFT_ITEMS}}` | HTML for "Most Listings" column | Content writer generates |
| `{{LVL_RIGHT_ITEMS}}` | HTML for "Proactive Strategy" column | Content writer generates |
| `{{MARKETING_CLOSING}}` | Bottom line callout text | Content writer generates |
| `{{DEMAND_HEADLINE}}` | Section 03 headline | Content writer generates |
| `{{DEMAND_PULLQUOTE}}` | Pull quote text (no outer quotes) | Content writer generates |
| `{{DEMAND_BODY}}` | Body paragraph(s) | Content writer generates |
| `{{LISTING_WINDOW_DATES}}` | e.g., "Jul 30, 2025 - Feb 8, 2026" | Research agent extracts |
| `{{COMPS_MEDIAN_PRICE}}` | e.g., "$1.80M" | Calculate from comps |
| `{{COMP_ROWS}}` | HTML string of comp rows | At least show "No comps found" |
| `{{DEMAND_CLOSING}}` | Why this matters callout | Content writer generates |
| `{{MARKET_HEADLINE}}` | Section 04 headline | Content writer generates |
| `{{MARKET_PULLQUOTE}}` | Pull quote text | Content writer generates |
| `{{MARKET_BODY}}` | Body paragraph(s) | Content writer generates |
| `{{YOY_CHANGE}}` | e.g., "+2.5%" | "N/A" |
| `{{MEDIAN_SOLD_PRICE}}` | e.g., "$425K" | "N/A" |
| `{{MEDIAN_PRICE_SOURCE}}` | e.g., "Per the MLS market report." | Omit if unavailable |
| `{{AVG_DOM}}` | e.g., "34" | "N/A" |
| `{{MARKET_CLOSING}}` | What you can do with this callout | Content writer generates |
| `{{PLAN_HEADLINE}}` | Plan section headline | Content writer generates |
| `{{PLAN_ACTS}}` | HTML string of 4 act blocks | Content writer generates steps |
| `{{CONTACT_HEADLINE}}` | e.g., "Twenty minutes. I'll bring the numbers, you bring the questions." | Content writer generates |
| `{{AGENT_AVATAR}}` | `<img>` tag or initial letter "R" | Show "R" as fallback |

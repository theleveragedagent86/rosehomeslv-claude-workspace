import fs from 'node:fs';

const FONTS = `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@800&family=Inter:wght@400;500&family=Raleway:wght@600&display=swap">`;
const BARLOW = `'Barlow','Helvetica Neue',Arial,sans-serif`;
const INTER  = `'Inter',system-ui,-apple-system,'Helvetica Neue',Arial,sans-serif`;
const RALE   = `'Raleway',system-ui,-apple-system,'Helvetica Neue',Arial,sans-serif`;

const base = `
    *,*::before,*::after { box-sizing: border-box; }
    body { margin: 0; width: 1080px; height: 1350px; overflow: hidden; }
    a { color: #1768E5; text-decoration: none; }
    a:hover { color: #0B3FA8; }
    .slide { position: relative; width: 1080px; height: 1350px;
             padding: 152px 64px 166px;
             display: flex; flex-direction: column; }
    .rail { display: flex; justify-content: space-between; align-items: baseline; gap: 24px; }
    .label { font-family: ${RALE}; font-weight: 600; font-size: 22px;
             letter-spacing: 0.15em; text-transform: uppercase; }
    .idx { font-family: ${RALE}; font-weight: 600; font-size: 20px;
           letter-spacing: 0.15em; }
    .mono { width: 64px; height: 64px; flex: 0 0 auto; }
    .footzone { display: flex; align-items: flex-end; justify-content: space-between;
                gap: 48px; }
`;

function wrap(title, css, body) {
  return `<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  ${FONTS}
  <style>${base}${css}
  </style>
</helmet>
${body}
</x-dc>
</body>
</html>
`;
}

/* ---------- Slide 1, cover ---------- */
fs.writeFileSync('Main.dc.html', wrap('cover', `
    .slide { background: #000000; }
    .eyebrow { font-family: ${RALE}; font-weight: 600; font-size: 22px;
               letter-spacing: 0.15em; text-transform: uppercase; color: #9AA3BC; }
    .core { flex: 1; display: flex; flex-direction: column; justify-content: center; }
    .numeral { font-family: ${BARLOW}; font-weight: 800; font-size: 400px;
               line-height: 0.78; letter-spacing: -0.04em; color: #5B9BFF;
               margin-left: -28px; }
    .head { font-family: ${BARLOW}; font-weight: 800; font-size: 82px;
            line-height: 0.98; letter-spacing: -0.028em; color: #FFFFFF;
            max-width: 780px; margin-top: 24px; text-wrap: balance; }
    .sub { font-family: ${INTER}; font-weight: 400; font-size: 30px;
           line-height: 1.5; color: #9AA3BC; max-width: 680px; margin-top: 32px; }
    .mark { font-family: ${BARLOW}; font-weight: 800; font-size: 34px;
            letter-spacing: -0.028em; color: #FFFFFF; }
    .rule { width: 72px; height: 5px; background: #1768E5; margin-bottom: 14px; }
`, `<div class="slide">
  <div class="rail"><div class="eyebrow">The Leveraged Agent</div></div>
  <div class="core">
    <div class="numeral">12</div>
    <div class="head">Things to automate before your next listing</div>
    <div class="sub">Photos land Tuesday. Everything else is already written.</div>
  </div>
  <div>
    <div class="rule"></div>
    <div class="mark">The Leveraged Agent</div>
  </div>
</div>`));

/* ---------- Slides 2 to 6, the list ---------- */
const LIST = [
  { n: 2, label: 'Before you ever see the house',
    items: [[1,'The seller CMA and<br>listing presentation'],
            [2,'The pre-listing prep<br>checklist and data sheet']],
    foot: 'Both are built before the appointment, not after.', panel: false },
  { n: 3, label: 'The day photos land',
    items: [[3,'MLS remarks, written<br>in your voice'],
            [4,'The vertical photo<br>tour video'],
            [5,'The listing landing page']],
    foot: 'Photos in at noon. All three live by one.', panel: false },
  { n: 4, label: 'Launch day',
    items: [[6,'Coming-soon and<br>just-listed sphere emails'],
            [7,'Neighbor letters for the<br>surrounding blocks'],
            [8,'The Meta listing ad<br>and lead form']],
    foot: 'Housing ads run Special Ad Category. No age, gender, or ZIP targeting.', panel: true },
  { n: 5, label: 'The first week',
    items: [[9,'The agent-to-agent reverse<br>prospecting broadcast'],
            [10,'The carousel and the<br>Shorts cutdowns']],
    foot: 'One shoot. Eight assets. Nothing filmed twice.', panel: false },
  { n: 6, label: 'After it goes pending',
    items: [[11,'The Friday seller report'],
            [12,'Every escrow email for<br>the next thirty days']],
    foot: 'My sellers stopped calling for updates. The update just shows up.', panel: false },
];

const listCss = `
    .slide { background: #FFFFFF; }
    .label { color: #55627F; }
    .idx { color: #9AA3BC; }
    .items { flex: 1; display: flex; flex-direction: column; justify-content: center;
             gap: 44px; padding-right: 56px; }
    .item { display: flex; gap: 30px; align-items: flex-start; }
    .num { font-family: ${BARLOW}; font-weight: 800; font-size: 96px; line-height: 0.92;
           letter-spacing: -0.03em; color: #0B3FA8; min-width: 108px; }
    .txt { font-family: ${INTER}; font-weight: 500; font-size: 56px; line-height: 1.2;
           letter-spacing: -0.012em; color: #050E3D; padding-top: 10px;
           text-wrap: pretty; }
    .hair { height: 1px; background: #E4E7EF; margin-bottom: 28px; }
    .foot { font-family: ${INTER}; font-weight: 400; font-size: 30px; line-height: 1.5;
            color: #55627F; max-width: 760px; }
    .panel { background: #F7F8FA; border-radius: 20px; padding: 36px 40px; max-width: 800px; }
    .panel .foot { max-width: none; }
`;

for (const s of LIST) {
  const items = s.items.map(([n, t]) =>
    `    <div class="item"><div class="num">${n}</div><div class="txt">${t}</div></div>`).join('\n');
  const footInner = s.panel
    ? `<div class="panel"><div class="foot">${s.foot}</div></div>`
    : `<div class="foot">${s.foot}</div>`;
  const footBlock = `  <div>${s.panel ? '' : '<div class="hair"></div>'}
    <div class="footzone">
      ${footInner}
      <img class="mono" src="monogram.png" alt="">
    </div>
  </div>`;
  const name = ['','','Phase1Prelist','Phase2Photos','Phase3Launch','Phase4Week','Phase5Pending'][s.n];
  fs.writeFileSync(`${name}.dc.html`, wrap(name, listCss, `<div class="slide">
  <div class="rail">
    <div class="label">${s.label}</div>
    <div class="idx">${String(s.n).padStart(2,'0')} / 07</div>
  </div>
  <div class="items">
${items}
  </div>
${footBlock}
</div>`));
}

/* ---------- Slide 7, the close ---------- */
fs.writeFileSync('Close.dc.html', wrap('close', `
    .slide { background: #000000; }
    .label { color: #9AA3BC; }
    .idx { color: #55627F; }
    .core { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 40px; }
    .stat { font-family: ${BARLOW}; font-weight: 800; font-size: 66px; line-height: 1.06;
            letter-spacing: -0.028em; color: #FFFFFF; max-width: 840px; }
    .hi { color: #5B9BFF; }
    .cta { align-self: flex-start; background: #1768E5; border-radius: 20px;
           padding: 38px 52px; font-family: ${BARLOW}; font-weight: 800; font-size: 46px;
           letter-spacing: -0.02em; color: #FFFFFF; margin-top: 16px; }
    .mark { font-family: ${BARLOW}; font-weight: 800; font-size: 34px;
            letter-spacing: -0.028em; color: #FFFFFF; }
    .rule { width: 72px; height: 5px; background: #1768E5; margin-bottom: 14px; }
`, `<div class="slide">
  <div class="rail">
    <div class="label">The math</div>
    <div class="idx">07 / 07</div>
  </div>
  <div class="core">
    <div class="stat">That is <span class="hi">3 to 4 hours</span> of desk work per listing.</div>
    <div class="stat">Mine takes about <span class="hi">twenty minutes</span> now.</div>
    <div class="cta">Save this before your next one.</div>
  </div>
  <div>
    <div class="rule"></div>
    <div class="mark">The Leveraged Agent</div>
  </div>
</div>`));

/* ---------- canvas.json ---------- */
const order = ['Main','Phase1Prelist','Phase2Photos','Phase3Launch','Phase4Week','Phase5Pending','Close'];
const artboards = order.map((f, i) => ({
  file: `${f}.dc.html`,
  x: (i % 4) * 1200,
  y: Math.floor(i / 4) * 1510,
  w: 1080, h: 1350,
  print: 'fixed',
}));
fs.writeFileSync('canvas.json', JSON.stringify({
  artboards,
  annotations: [
    { id: 'pattern-note', x: 0, y: -200, w: 1080,
      text: 'Pattern: Whitney Bartlette numbered-list carousel.\nCount in the cover, the list IS the deliverable, no keyword gate.\nBlack cover and close, white list slides between. That alternation is the only structural device.' },
    { id: 'install-note', x: 2400, y: 1360, w: 1080,
      text: 'Item 3 (MLS remarks) uses listing-description, which is BUILT but NOT INSTALLED per ryan-built-inventory.md. Install before this posts.' },
  ],
  launch: { view: 'canvas' },
}, null, 2));

console.log('wrote', order.length, 'artboards + canvas.json');

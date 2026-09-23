import fs from 'node:fs';

const FONTS = `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@800&family=Inter:wght@400;500&family=Raleway:wght@600&display=swap">`;
const BARLOW = `'Barlow','Helvetica Neue',Arial,sans-serif`;
const INTER  = `'Inter',system-ui,-apple-system,'Helvetica Neue',Arial,sans-serif`;
const RALE   = `'Raleway',system-ui,-apple-system,'Helvetica Neue',Arial,sans-serif`;

// Safe band: IG crops a 4:5 post to a centred 1:1 for the profile grid, trimming
// 135px top and bottom. Padding 152/64/166 keeps every slide inside it, and
// nothing is corner-pinned. See skool-carousel references/design-loop-prompt.md.
const base = `
    *,*::before,*::after { box-sizing: border-box; }
    body { margin: 0; width: 1080px; height: 1350px; overflow: hidden; }
    a { color: #1768E5; text-decoration: none; }
    a:hover { color: #0B3FA8; }
    .slide { position: relative; width: 1080px; height: 1350px;
             padding: 152px 64px 166px; display: flex; flex-direction: column; }
    .rail { display: flex; justify-content: space-between; align-items: baseline; gap: 24px; }
    .label { font-family: ${RALE}; font-weight: 600; font-size: 22px;
             letter-spacing: 0.15em; text-transform: uppercase; }
    .idx { font-family: ${RALE}; font-weight: 600; font-size: 20px; letter-spacing: 0.15em; }
    .mono { width: 64px; height: 64px; flex: 0 0 auto; }
    .monorow { display: flex; justify-content: flex-end; }
`;

const wrap = (css, body) => `<!doctype html>
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

/* ---------- Slide 1, cover ---------- */
fs.writeFileSync('Main.dc.html', wrap(`
    .slide { background: #000000; }
    .eyebrow { font-family: ${RALE}; font-weight: 600; font-size: 22px;
               letter-spacing: 0.15em; text-transform: uppercase; color: #9AA3BC; }
    .core { flex: 1; display: flex; flex-direction: column; justify-content: center; }
    .numeral { font-family: ${BARLOW}; font-weight: 800; font-size: 400px;
               line-height: 0.78; letter-spacing: -0.04em; color: #5B9BFF;
               margin-left: -28px; }
    .head { font-family: ${BARLOW}; font-weight: 800; font-size: 82px;
            line-height: 0.98; letter-spacing: -0.028em; color: #FFFFFF;
            margin-top: 24px; }
    .sub { font-family: ${INTER}; font-weight: 400; font-size: 30px;
           line-height: 1.5; color: #9AA3BC; max-width: 680px; margin-top: 32px; }
    .mark { font-family: ${BARLOW}; font-weight: 800; font-size: 34px;
            letter-spacing: -0.028em; color: #FFFFFF; }
    .rule { width: 72px; height: 5px; background: #1768E5; margin-bottom: 14px; }
`, `<div class="slide">
  <div class="rail"><div class="eyebrow">The Leveraged Agent</div></div>
  <div class="core">
    <div class="numeral">20</div>
    <div class="head">Reel hooks for<br>realtors who hate<br>being on camera</div>
    <div class="sub">Not one of these needs your face.</div>
  </div>
  <div>
    <div class="rule"></div>
    <div class="mark">The Leveraged Agent</div>
  </div>
</div>`));

/* ---------- Slides 2 to 5, the swipe file ---------- */
// Line breaks are hand-set, not left to the wrap engine, so no hook ends on an
// orphaned word. Target is roughly 33 characters a line, balanced.
const SETS = [
  { n: 2, name: 'PhotosVO', label: 'Over listing photos, voiceover only', hooks: [
    [1,  'The room that sells this house<br>is not the kitchen.'],
    [2,  'Here is what this price<br>actually buys you.'],
    [3,  'Nobody tours a house<br>because of the front door.'],
    [4,  'This one has been sitting.<br>Here is why.'],
    [5,  'The photos do not<br>show you this part.'],
  ]},
  { n: 3, name: 'ScreenRec', label: 'Over a screen recording', hooks: [
    [6,  'Watch what happened to<br>this home&rsquo;s price.'],
    [7,  'This house sold twice.<br>Look at the gap.'],
    [8,  'Three houses on this street.<br>Three different prices.'],
    [9,  'Every home in this<br>neighborhood under your number.'],
    [10, 'This listing has changed<br>price three times.'],
  ]},
  { n: 4, name: 'TextOnly', label: 'Text on black, no footage at all', hooks: [
    [11, 'Your offer was not too low.<br>It was too slow.'],
    [12, 'The inspection is not<br>where you negotiate.'],
    [13, 'Three reasons your house<br>did not sell.'],
    [14, 'You are not competing on price.<br>You are competing on terms.'],
    [15, 'Sellers, the first two<br>weeks decide everything.'],
  ]},
  { n: 5, name: 'GreenScreen', label: 'Green screen, news desk', hooks: [
    [16, 'Something changed in your<br>neighborhood this week.'],
    [17, 'One rule changed.<br>Here is who it affects.'],
    [18, 'This week&rsquo;s news, and what<br>it means for your house.'],
    [19, 'One change this month<br>affects every listing here.'],
    [20, 'Nobody in this market is<br>talking about this yet.'],
  ]},
];

const hookCss = `
    .slide { background: #FFFFFF; }
    .label { color: #55627F; }
    .idx { color: #9AA3BC; }
    .hooks { flex: 1; display: flex; flex-direction: column; justify-content: center;
             gap: 38px; }
    .hook { display: flex; gap: 30px; align-items: flex-start; }
    .num { font-family: ${BARLOW}; font-weight: 800; font-size: 60px; line-height: 1.1;
           letter-spacing: -0.03em; color: #0B3FA8; min-width: 84px; }
    .txt { font-family: ${INTER}; font-weight: 500; font-size: 48px; line-height: 1.28;
           letter-spacing: -0.012em; color: #050E3D; }
`;

for (const s of SETS) {
  const rows = s.hooks.map(([n, t]) =>
    `    <div class="hook"><div class="num">${n}</div><div class="txt">&ldquo;${t}&rdquo;</div></div>`).join('\n');
  fs.writeFileSync(`${s.name}.dc.html`, wrap(hookCss, `<div class="slide">
  <div class="rail">
    <div class="label">${s.label}</div>
    <div class="idx">${String(s.n).padStart(2,'0')} / 06</div>
  </div>
  <div class="hooks">
${rows}
  </div>
  <div class="monorow"><img class="mono" src="monogram.png" alt=""></div>
</div>`));
}

/* ---------- Slide 6, the close ---------- */
fs.writeFileSync('Close.dc.html', wrap(`
    .slide { background: #000000; }
    .label { color: #9AA3BC; }
    .idx { color: #55627F; }
    .core { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 40px; }
    .stat { font-family: ${BARLOW}; font-weight: 800; font-size: 66px; line-height: 1.06;
            letter-spacing: -0.028em; color: #FFFFFF; max-width: 860px; }
    .hi { color: #5B9BFF; }
    .cta { align-self: flex-start; background: #1768E5; border-radius: 20px;
           padding: 38px 52px; font-family: ${BARLOW}; font-weight: 800; font-size: 46px;
           letter-spacing: -0.02em; color: #FFFFFF; margin-top: 16px; }
    .mark { font-family: ${BARLOW}; font-weight: 800; font-size: 34px;
            letter-spacing: -0.028em; color: #FFFFFF; }
    .rule { width: 72px; height: 5px; background: #1768E5; margin-bottom: 14px; }
`, `<div class="slide">
  <div class="rail">
    <div class="label">The point</div>
    <div class="idx">06 / 06</div>
  </div>
  <div class="core">
    <div class="stat">The camera was never the problem.</div>
    <div class="stat">Not having <span class="hi">the first line</span> was.</div>
    <div class="cta">Save this. Use one tomorrow.</div>
  </div>
  <div>
    <div class="rule"></div>
    <div class="mark">The Leveraged Agent</div>
  </div>
</div>`));

/* ---------- canvas.json ---------- */
const order = ['Main','PhotosVO','ScreenRec','TextOnly','GreenScreen','Close'];
fs.writeFileSync('canvas.json', JSON.stringify({
  artboards: order.map((f, i) => ({
    file: `${f}.dc.html`,
    x: (i % 4) * 1200, y: Math.floor(i / 4) * 1510,
    w: 1080, h: 1350, print: 'fixed',
  })),
  annotations: [
    { id: 'pattern-note', x: 0, y: -280, w: 1080,
      text: 'Pattern: Whitney Bartlette numbered-list carousel. Count in the cover, the list IS the deliverable, no keyword gate.\nSorted by how little the format asks of you, so the lowest-effort options sit first where the objection lives.\nEvery hook is for a format where you never appear on camera: listing photos, a screen recording, text on black, green screen.' },
    { id: 'band-note', x: 2400, y: 1360, w: 1080,
      text: 'All six slides sit inside the 4:5 safe band (y 152..1184), so the set lines up on swipe and any slide survives the 1:1 profile-grid crop.\nVerify with: node ~/.claude/skills/skool-carousel/references/check-slides.mjs' },
  ],
  launch: { view: 'canvas' },
}, null, 2));

console.log('wrote', order.length, 'artboards + canvas.json');

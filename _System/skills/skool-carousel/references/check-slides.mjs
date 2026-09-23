// Render every carousel slide to PNG and measure it against the 4:5 safe band.
//
//   node check-slides.mjs                 # every *.dc.html in the cwd, alphabetical
//   node check-slides.mjs Main.dc.html Phase1.dc.html ...   # explicit carousel order
//
// Writes png/slide-NN-<Name>.png and prints a per-slide bounding box. Exits 1 if
// any text or image element falls outside the band, naming the offender.
//
// Why the band: Instagram crops a 4:5 post to a centred 1:1 for the profile grid,
// trimming 135px top and bottom. See references/design-loop-prompt.md, "Safe area".

import { chromium } from '/Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/node_modules/playwright/index.mjs';
import fs from 'node:fs';
import path from 'node:path';

const W = 1080, H = 1350;
const TOP = 135, BOT = H - 135, SIDE = 35;

const args = process.argv.slice(2);
const files = args.length
  ? args
  : fs.readdirSync('.').filter(f => f.endsWith('.dc.html')).sort();

if (!files.length) { console.error('no .dc.html files found'); process.exit(1); }
fs.mkdirSync('png', { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
let bad = 0;

for (let i = 0; i < files.length; i++) {
  const name = path.basename(files[i], '.dc.html');

  // A .dc.html is a Design Component, not a standalone page. Strip the runtime
  // shim and the x-dc/helmet wrappers so a browser can render it directly.
  const src = fs.readFileSync(files[i], 'utf8')
    .replace('<script src="./support.js"></script>', '')
    .replace('<x-dc>', '').replace('</x-dc>', '')
    .replace('<helmet>', '').replace('</helmet>', '');

  const tmp = `.check-${name}.html`;
  fs.writeFileSync(tmp, src);
  await page.goto('file://' + path.resolve(tmp), { waitUntil: 'networkidle' });
  await page.waitForTimeout(600);   // let webfonts settle before measuring

  const out = `png/slide-${String(i + 1).padStart(2, '0')}-${name}.png`;
  await page.screenshot({ path: out });

  const els = await page.evaluate(() => {
    const r = [];
    document.querySelectorAll('.slide *').forEach(el => {
      if (el.children.length) return;                       // leaf nodes only
      if (!el.textContent.trim() && el.tagName !== 'IMG') return;
      const b = el.getBoundingClientRect();
      if (!b.width || !b.height) return;
      r.push({ t: Math.round(b.top), b: Math.round(b.bottom),
               l: Math.round(b.left), r: Math.round(b.right),
               s: (el.textContent.trim() || el.tagName).slice(0, 28) });
    });
    return r;
  });
  fs.unlinkSync(tmp);

  if (!els.length) { console.log(`WARN ${name}: nothing measurable, is the root .slide?`); continue; }

  const box = [Math.min(...els.map(e => e.t)), Math.max(...els.map(e => e.b)),
               Math.min(...els.map(e => e.l)), Math.max(...els.map(e => e.r))];
  const fails = els.filter(e => e.t < TOP || e.b > BOT || e.l < SIDE || e.r > W - SIDE);
  bad += fails.length;

  console.log(`${fails.length ? 'FAIL' : 'ok  '} ${name.padEnd(16)} y ${String(box[0]).padStart(4)}..${String(box[1]).padStart(4)}  x ${String(box[2]).padStart(3)}..${box[3]}  -> ${out}`);
  fails.forEach(f => console.log(`       outside band: "${f.s}" @ y ${f.t}..${f.b} x ${f.l}..${f.r}`));
}

await browser.close();

if (bad) {
  console.log(`\n${bad} element(s) outside the safe band (y ${TOP}..${BOT}, x ${SIDE}..${W - SIDE}).`);
  console.log('Usual cause: something pinned to a corner with position:absolute.');
  console.log('Fix: slide padding 152px 64px 166px, and make it a child of the top or bottom row.');
  process.exit(1);
}
console.log(`\nall ${files.length} slides inside the band (y ${TOP}..${BOT}, x ${SIDE}..${W - SIDE}).`);

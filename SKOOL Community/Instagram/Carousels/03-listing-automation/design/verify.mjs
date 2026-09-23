import { chromium } from '/Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/node_modules/playwright/index.mjs';
import fs from 'node:fs'; import path from 'node:path';

const ORDER = ['Main','Phase1Prelist','Phase2Photos','Phase3Launch','Phase4Week','Phase5Pending','Close'];
const TOP = 135, BOT = 1215, SIDE = 35;   // 1:1 grid band + the guide's side inset

const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
let bad = 0;

for (const name of ORDER) {
  const src = fs.readFileSync(`${name}.dc.html`, 'utf8')
    .replace('<script src="./support.js"></script>','')
    .replace('<x-dc>','').replace('</x-dc>','')
    .replace('<helmet>','').replace('</helmet>','');
  const tmp = `.v-${name}.html`; fs.writeFileSync(tmp, src);
  await p.goto('file://' + path.resolve(tmp), { waitUntil: 'networkidle' });
  await p.waitForTimeout(500);

  const r = await p.evaluate(() => {
    const out = [];
    document.querySelectorAll('.slide *').forEach(el => {
      if (el.children.length) return;                 // leaves only
      if (!el.textContent.trim() && el.tagName !== 'IMG') return;
      const b = el.getBoundingClientRect();
      if (b.width === 0 || b.height === 0) return;
      out.push({ t: Math.round(b.top), b: Math.round(b.bottom),
                 l: Math.round(b.left), r: Math.round(b.right),
                 s: (el.textContent.trim() || el.tagName).slice(0, 26) });
    });
    return out;
  });
  fs.unlinkSync(tmp);

  const top = Math.min(...r.map(x => x.t)), bot = Math.max(...r.map(x => x.b));
  const left = Math.min(...r.map(x => x.l)), right = Math.max(...r.map(x => x.r));
  const fails = r.filter(x => x.t < TOP || x.b > BOT || x.l < SIDE || x.r > 1080 - SIDE);
  bad += fails.length;
  console.log(`${fails.length ? 'FAIL' : 'ok  '} ${name.padEnd(15)} y ${String(top).padStart(4)}..${String(bot).padStart(4)}  x ${String(left).padStart(3)}..${right}`);
  fails.forEach(f => console.log(`       -> ${f.s} @ y ${f.t}..${f.b} x ${f.l}..${f.r}`));
}
await b.close();
console.log(bad ? `\n${bad} element(s) outside the band` : `\nall 7 slides inside y ${TOP}..${BOT} and x ${SIDE}..${1080-SIDE}`);

import { chromium } from '/Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/node_modules/playwright/index.mjs';
import fs from 'node:fs';
import path from 'node:path';

const ORDER = ['Main','Phase1Prelist','Phase2Photos','Phase3Launch','Phase4Week','Phase5Pending','Close'];
fs.mkdirSync('png', { recursive: true });

const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });

for (let i = 0; i < ORDER.length; i++) {
  const src = fs.readFileSync(`${ORDER[i]}.dc.html`, 'utf8')
    .replace('<script src="./support.js"></script>', '')
    .replace('<x-dc>', '').replace('</x-dc>', '')
    .replace('<helmet>', '').replace('</helmet>', '');
  const tmp = `.render-${ORDER[i]}.html`;
  fs.writeFileSync(tmp, src);
  await p.goto('file://' + path.resolve(tmp), { waitUntil: 'networkidle' });
  await p.waitForTimeout(600);
  const out = `png/slide-${String(i+1).padStart(2,'0')}-${ORDER[i]}.png`;
  await p.screenshot({ path: out });
  console.log('wrote', out);
  fs.unlinkSync(tmp);
}
await b.close();

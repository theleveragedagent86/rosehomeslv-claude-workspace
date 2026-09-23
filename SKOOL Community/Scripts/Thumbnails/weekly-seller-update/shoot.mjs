import { chromium } from '/Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/node_modules/playwright/index.mjs';
const dir = process.cwd();
const b = await chromium.launch();
const p = await b.newPage({ viewport:{width:1280,height:720}, deviceScaleFactor:1 });
for (const n of process.argv.slice(2)) {
  await p.goto(`file://${dir}/${n}.html`); await p.waitForTimeout(200);
  await p.screenshot({ path:`${dir}/${n}.png` });
}
await b.close();

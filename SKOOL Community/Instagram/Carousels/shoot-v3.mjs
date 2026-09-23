import { chromium } from '/Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({ viewport:{width:1080,height:1350}, deviceScaleFactor:1 });
await p.goto('http://localhost:8091/SKOOL%20Community/Instagram/Carousels/render-v3.html',{waitUntil:'networkidle'});
await p.evaluate(()=>document.fonts.ready);
const n = await p.locator('.slide').count();
for (let i=0;i<n;i++){
  const f = `png-v3/slide-${String(i+1).padStart(2,'0')}.png`;
  await p.locator('.slide').nth(i).screenshot({ path:f });
  console.log('wrote', f);
}
await b.close();

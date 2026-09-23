import fs from 'fs';
import { chromium } from '/Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/node_modules/playwright/index.mjs';

const OUT = '/Users/ryanrose/Downloads/Claude/SKOOL Community/Brandkit';
const JOBS = [
  ['leveraged-agent-logo-dark.png',       'http://localhost:8091/SKOOL%20Community/Brandkit/leveraged-agent-logo.png'],
  ['leveraged-agent-logo-small-dark.png', 'http://localhost:8091/SKOOL%20Community/Brandkit/leveraged-agent-logo-small.png'],
];

const b = await chromium.launch();
const p = await b.newPage();
await p.goto('http://localhost:8091/', { waitUntil: 'domcontentloaded' });

for (const [file, url] of JOBS) {
  const dataUrl = await p.evaluate(async (url) => {
    const img = new Image(); img.crossOrigin = 'anonymous';
    await new Promise((res, rej) => { img.onload = res; img.onerror = rej; img.src = url; });
    const c = document.createElement('canvas');
    c.width = img.naturalWidth; c.height = img.naturalHeight;
    const ctx = c.getContext('2d', { willReadFrequently: true });
    ctx.drawImage(img, 0, 0);
    const im = ctx.getImageData(0, 0, c.width, c.height);
    const d = im.data;

    // canonical targets
    const CREAM = [0xF5, 0xF2, 0xEB];   // light ink on dark
    const DEEP  = [0x08, 0x34, 0x3E];   // dark surface
    const GOLD  = [0xE8, 0xA3, 0x3D];   // accent, unchanged on dark

    // luminance anchors measured off the source art
    const LUM_INK = 0.075;   // teal type
    const LUM_BG  = 0.94;    // cream field
    const lum = (r,g,bl) => (0.2126*r + 0.7152*g + 0.0722*bl) / 255;

    for (let i = 0; i < d.length; i += 4) {
      const r = d[i], g = d[i+1], bl = d[i+2];
      const mx = Math.max(r,g,bl), mn = Math.min(r,g,bl), dd = mx - mn;
      const l = (mx+mn)/2/255;
      const s = dd === 0 ? 0 : dd / (l > 0.5 ? (510-mx-mn) : (mx+mn));
      let h = 0;
      if (dd) { h = mx===r ? ((g-bl)/dd + (g<bl?6:0)) : mx===g ? ((bl-r)/dd+2) : ((r-g)/dd+4); h *= 60; }

      // gold stays gold: hold hue+sat, lift lightness onto the canonical gold
      if (h >= 20 && h <= 58 && s > 0.30 && l > 0.20 && l < 0.82) {
        const k = 0.72;                      // blend toward canonical gold
        d[i]   = Math.round(r*(1-k) + GOLD[0]*k);
        d[i+1] = Math.round(g*(1-k) + GOLD[1]*k);
        d[i+2] = Math.round(bl*(1-k) + GOLD[2]*k);
        continue;
      }

      // everything else rides the cream<->teal luminance axis, inverted
      let t = (lum(r,g,bl) - LUM_INK) / (LUM_BG - LUM_INK);
      t = Math.max(0, Math.min(1, t));
      const e = t*t*(3 - 2*t);               // smoothstep, keeps antialiasing clean
      d[i]   = Math.round(CREAM[0]*(1-e) + DEEP[0]*e);
      d[i+1] = Math.round(CREAM[1]*(1-e) + DEEP[1]*e);
      d[i+2] = Math.round(CREAM[2]*(1-e) + DEEP[2]*e);
    }
    ctx.putImageData(im, 0, 0);
    return c.toDataURL('image/png');
  }, url);

  fs.writeFileSync(`${OUT}/${file}`, Buffer.from(dataUrl.split(',')[1], 'base64'));
  console.log('wrote', file);
}
await b.close();

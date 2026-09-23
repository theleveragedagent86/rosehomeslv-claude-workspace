/* Renders every Leveraged Agent brand image from the v2.0 "Vector" design
   system. Run it after changing a token, the logo component, or a cover config.
   Playwright is not installed here, so it is imported by absolute path from
   hyperframes-student-kit/ (same reason render-thumbnail.mjs lives there).

     node Design-System/build-assets.mjs            # everything
     node Design-System/build-assets.mjs logos      # one group
     node Design-System/build-assets.mjs covers banner
*/
import { chromium } from '/Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/node_modules/playwright/index.mjs';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const BK = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

/* The channel banner is the only asset that carries the tagline, so it is a
   constant here rather than being buried in the markup. */
const TAGLINE = 'Automating 80% of the job that sucks';

/* Filenames frozen for drop-in compatibility: ~44 bundled copies live under
   hyperframes-student-kit/video-projects/-star-/assets/ and compositions
   reference them by these exact names. */
const CANONICAL = new Set([
  'leveraged-agent-logo', 'leveraged-agent-logo-dark',
  'leveraged-agent-logo-small', 'leveraged-agent-logo-small-dark',
]);

const groups = process.argv.slice(2);
const want = (g) => groups.length === 0 || groups.includes(g);

const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 1 });
const wrote = [];

async function load(file) {
  await page.goto('file://' + file, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(250);       // let la-logo's post-font refit settle
}

/* Frames are laid out with fractional heights (la-logo sizes itself from an
   aspect ratio), and a fractional box makes the screenshot clip round up, which
   is where stray 1025px-tall "1024px" exports come from. So pin each frame to
   the top-left at whole pixels, one at a time, before shooting it. */
async function shootAll(outFor) {
  for (const el of await page.locator('[data-export]').all()) {
    const name = await el.getAttribute('data-export');
    const out = outFor(name);
    fs.mkdirSync(path.dirname(out), { recursive: true });
    await el.evaluate((n) => {
      const r = n.getBoundingClientRect();
      n.dataset.restore = n.getAttribute('style') || '';
      n.style.cssText += ';position:fixed;top:0;left:0;z-index:9999;overflow:hidden'
        + `;width:${Math.round(r.width)}px;height:${Math.round(r.height)}px`;
    });
    await el.screenshot({ path: out, omitBackground: true });
    await el.evaluate((n) => { n.setAttribute('style', n.dataset.restore); });
    wrote.push(path.relative(BK, out));
  }
}

if (want('logos')) {
  await load(path.join(BK, 'Logos/logos.html'));
  await shootAll((n) => CANONICAL.has(n)
    ? path.join(BK, `${n}.png`)
    : path.join(BK, 'Logos', `${n}.png`));
}

if (want('banner')) {
  const src = path.join(BK, 'YouTube-Banner/banner.html');
  const tmp = path.join(BK, 'YouTube-Banner/_render-tmp.html');
  fs.writeFileSync(tmp, fs.readFileSync(src, 'utf8').replaceAll('TAGLINE_GOES_HERE', TAGLINE));
  await load(tmp);
  await shootAll(() => path.join(BK, 'leveraged-agent-youtube-banner.png'));
  fs.unlinkSync(tmp);
}

if (want('covers')) {
  const dir = path.join(BK, 'Classroom-Covers');
  const src = fs.readFileSync(path.join(dir, 'template.html'), 'utf8');
  const tmp = path.join(dir, '_render-tmp.html');
  for (const f of fs.readdirSync(path.join(dir, 'configs')).filter((f) => /^\d\d-.*\.json$/.test(f))) {
    const c = JSON.parse(fs.readFileSync(path.join(dir, 'configs', f), 'utf8'));
    // SUBTITLE first: TITLE_GOES_HERE is a substring of SUBTITLE_GOES_HERE.
    fs.writeFileSync(tmp, src
      .replaceAll('SUBTITLE_GOES_HERE', c.subtitle)
      .replaceAll('TITLE_GOES_HERE', c.title)
      .replaceAll('META_GOES_HERE', c.meta));
    await load(tmp);
    await shootAll(() => path.join(dir, f.replace(/\.json$/, '.png')));
  }
  fs.unlinkSync(tmp);
}

/* Vector masters. An <img src="logo.svg"> is an isolated document that cannot
   reach the page's webfonts, so it would silently fall back to Arial. Embedding
   the woff2 as a data URI inside each SVG is what makes these safe to hand to
   anyone. */
if (want('svg')) {
  const b64 = (f) => fs.readFileSync(path.join(BK, 'Design-System/fonts', f)).toString('base64');
  const face = (fam, wt, f) => `@font-face{font-family:'${fam}';font-weight:${wt};`
    + `src:url(data:font/woff2;base64,${b64(f)}) format('woff2')}`;
  const FONTS = face('Barlow', 800, 'barlow-800-latin.woff2')
              + face('Raleway', 600, 'raleway-400-latin.woff2');

  await load(path.join(BK, 'Logos/logos.html'));
  const variants = [
    ['logo-lockup', 'lockup', false, false], ['logo-lockup-inverse', 'lockup', true, false],
    ['logo-lockup-tagline', 'lockup', false, true], ['logo-lockup-tagline-inverse', 'lockup', true, true],
    ['logo-wordmark', 'wordmark', false, false], ['logo-wordmark-inverse', 'wordmark', true, false],
    ['logo-wordmark-tagline', 'wordmark', false, true], ['logo-wordmark-tagline-inverse', 'wordmark', true, true],
    ['logo-monogram', 'monogram', false, false], ['logo-monogram-inverse', 'monogram', true, false],
    ['logo-monogram-accent', 'accent', false, false], ['favicon', 'favicon', false, false],
  ];
  for (const [name, variant, inverse, tagline] of variants) {
    const svg = await page.evaluate(async ([variant, inverse, tagline]) => {
      const el = document.createElement('la-logo');
      el.setAttribute('variant', variant);
      if (inverse) el.setAttribute('inverse', '');
      if (!tagline) el.setAttribute('no-tagline', '');
      el.style.cssText = 'position:fixed;left:-9999px;width:800px';
      document.body.appendChild(el);
      await document.fonts.ready;
      await new Promise((r) => requestAnimationFrame(r));
      const out = el.shadowRoot.innerHTML;
      el.remove();
      return out;
    }, [variant, inverse, tagline]);
    const out = path.join(BK, 'Logos', `${name}.svg`);
    fs.writeFileSync(out, svg.replace('>', `><style>${FONTS}</style>`) + '\n');
    wrote.push(path.relative(BK, out));
  }
}

await browser.close();
for (const w of wrote) console.log('wrote', w);

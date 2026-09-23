// Renders a YouTube thumbnail from a spec JSON + a brand token file.
//
//   node render.mjs path/to/spec.json
//
// Writes three files next to the spec, named from spec.out:
//   <out>.png          2560x1440 master
//   <out>-1280.jpg     1280x720 upload file (YouTube's target, under 2MB)
//   <out>-squint.png   120px wide proof, the size YouTube actually shows in feed
//
// Playwright is not installed next to this skill, so it is resolved from whichever
// workspace project already has it. Run this from anywhere: node render.mjs <spec>.

import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const SKILL_DIR = path.dirname(fileURLToPath(import.meta.url));
const WORKSPACE = '/Users/ryanrose/Downloads/Claude';

const PLAYWRIGHT_HOSTS = [
  path.join(WORKSPACE, 'SKOOL Community/hyperframes-student-kit'),
  path.join(WORKSPACE, 'hyperframes'),
];

// playwright's entry is CommonJS, so a dynamic import can land the exports on
// the namespace or on .default depending on interop. Accept either.
const pickChromium = (mod) => mod?.chromium ?? mod?.default?.chromium;

const loadChromium = async () => {
  for (const host of PLAYWRIGHT_HOSTS) {
    try {
      const require = createRequire(path.join(host, 'package.json'));
      const found = pickChromium(await import(require.resolve('playwright')));
      if (found) return found;
    } catch { /* try the next host */ }
  }
  const found = pickChromium(await import('playwright').catch(() => null));
  if (found) return found;
  throw new Error(`playwright not found. Looked in:\n  ${PLAYWRIGHT_HOSTS.join('\n  ')}`);
};
const chromium = await loadChromium();

const MIME = {
  '.html': 'text/html', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml',
  '.json': 'application/json', '.css': 'text/css',
};

const specPath = process.argv[2];
if (!specPath) {
  console.error('Usage: node render.mjs path/to/spec.json');
  process.exit(1);
}

const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const outDir = path.dirname(path.resolve(specPath));

const brandFile = path.join(SKILL_DIR, 'brands', `${spec.brand || 'rose-homes'}.json`);
if (!fs.existsSync(brandFile)) {
  console.error(`Unknown brand "${spec.brand}". Available: ${fs.readdirSync(path.join(SKILL_DIR, 'brands')).join(', ')}`);
  process.exit(1);
}
const brand = JSON.parse(fs.readFileSync(brandFile, 'utf8'));

const templateFile = path.join(SKILL_DIR, 'templates', `${spec.template}.html`);
if (!fs.existsSync(templateFile)) {
  console.error(`Unknown template "${spec.template}". Available: ${fs.readdirSync(path.join(SKILL_DIR, 'templates')).map(f => f.replace('.html', '')).join(', ')}`);
  process.exit(1);
}

// Image paths in the spec are absolute, or relative to the spec file. Serve them
// through the local server as workspace-rooted URLs so the page can load them.
const toUrl = (p) => {
  if (!p) return null;
  const abs = path.isAbsolute(p) ? p : path.resolve(outDir, p);
  if (!fs.existsSync(abs)) throw new Error(`Image not found: ${abs}`);
  if (!abs.startsWith(WORKSPACE)) throw new Error(`Image must live under ${WORKSPACE}: ${abs}`);
  return '/' + path.relative(WORKSPACE, abs).split(path.sep).map(encodeURIComponent).join('/');
};

// Every field a template may use as an image source. Templates ignore the ones
// they do not need, so mapping them all here keeps render.mjs template-agnostic.
const IMAGE_FIELDS = ['plate', 'plateLeft', 'plateRight', 'cutout'];

const payload = { ...spec, brand };
for (const field of IMAGE_FIELDS) {
  if (spec[field]) payload[field] = toUrl(spec[field]);
}
// The stock cutout is the default subject, but only where a template asks for one.
if (!payload.cutout && spec.cutout !== false && brand.cutout) {
  payload.cutout = toUrl(path.join(SKILL_DIR, brand.cutout));
}

// Ephemeral static server rooted at the workspace. Self-contained so this does
// not depend on serve.rb already running.
const server = http.createServer((req, res) => {
  const rel = decodeURIComponent(req.url.split('?')[0]);
  const abs = path.join(WORKSPACE, rel);
  if (!abs.startsWith(WORKSPACE) || !fs.existsSync(abs) || fs.statSync(abs).isDirectory()) {
    res.writeHead(404).end('not found');
    return;
  }
  res.writeHead(200, { 'Content-Type': MIME[path.extname(abs).toLowerCase()] || 'application/octet-stream' });
  fs.createReadStream(abs).pipe(res);
});
await new Promise((r) => server.listen(0, '127.0.0.1', r));
const origin = `http://127.0.0.1:${server.address().port}`;

// Stage the template with the spec injected, inside the workspace so it is servable.
const stagePath = path.join(SKILL_DIR, '_render-tmp.html');
const html = fs.readFileSync(templateFile, 'utf8')
  .replace('/*SPEC*/null', JSON.stringify(payload));
fs.writeFileSync(stagePath, html);
const stageUrl = origin + '/' + path.relative(WORKSPACE, stagePath).split(path.sep).map(encodeURIComponent).join('/');

const browser = await chromium.launch();
try {
  const page = await browser.newPage({
    viewport: { width: 1280, height: 720 },
    deviceScaleFactor: 2,
  });
  const problems = [];
  page.on('pageerror', (e) => problems.push(`js: ${e.message}`));
  page.on('requestfailed', (r) => problems.push(`asset: ${r.url()}`));

  await page.goto(stageUrl, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(200);

  const masterPath = path.join(outDir, `${spec.out}.png`);
  await page.screenshot({ path: masterPath });

  const uploadPath = path.join(outDir, `${spec.out}-1280.jpg`);
  await page.screenshot({ path: uploadPath, type: 'jpeg', quality: 88, scale: 'css' });

  // Squint proof: let the browser downscale the real bitmap the way a feed does.
  const squintPath = path.join(outDir, `${spec.out}-squint.png`);
  const masterUrl = origin + '/' + path.relative(WORKSPACE, masterPath).split(path.sep).map(encodeURIComponent).join('/');
  const proof = await browser.newPage({ viewport: { width: 120, height: 68 } });
  await proof.setContent(
    `<body style="margin:0"><img src="${masterUrl}" style="width:120px;height:68px;display:block"></body>`,
  );
  await proof.waitForLoadState('networkidle');
  await proof.screenshot({ path: squintPath });

  const kb = Math.round(fs.statSync(uploadPath).size / 1024);
  console.log(`master  ${masterPath}`);
  console.log(`upload  ${uploadPath} (${kb} KB)`);
  console.log(`squint  ${squintPath}`);
  if (kb > 2048) console.warn(`WARNING: upload file is ${kb} KB, over YouTube's 2MB limit`);
  if (problems.length) console.warn('WARNING:\n  ' + problems.join('\n  '));
} finally {
  await browser.close();
  fs.unlinkSync(stagePath);
  server.close();
}

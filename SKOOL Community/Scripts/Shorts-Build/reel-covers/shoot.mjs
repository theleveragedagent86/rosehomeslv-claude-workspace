// node reel-covers/shoot.mjs [wsu|oh ...]  -> <set folder>/covers/cover-NN.png (1080x1920)
import { createRequire } from "module"; import path from "path"; import url from "url"; import fs from "fs";
const require = createRequire(import.meta.url);
const { chromium } = require("/Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/node_modules/playwright");
const here = path.dirname(url.fileURLToPath(import.meta.url));
const DIRS = { wsu: "weekly-seller-update", oh: "open-house-lead-automation" };
const sets = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(DIRS);
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
for (const set of sets) {
  const out = path.join(here, "..", DIRS[set], "covers"); fs.mkdirSync(out, { recursive: true });
  for (let n = 1; ; n++) {
    await p.goto(url.pathToFileURL(path.join(here, "cover.html")).href + `?set=${set}&n=${n}`);
    if (!(await p.evaluate((n) => document.getElementById("h").innerHTML.length > 0, n))) break;
    await p.evaluate(() => document.fonts.ready);
    const fs_ = await p.evaluate(() => window.fit());
    await p.screenshot({ path: path.join(out, `cover-${String(n).padStart(2, "0")}.png`) });
    console.log(set, n, fs_);
  }
}
await b.close();

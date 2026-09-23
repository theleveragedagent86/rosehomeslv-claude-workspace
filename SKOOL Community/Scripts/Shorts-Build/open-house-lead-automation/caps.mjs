// Renders caption states (tmp/<n>_caps.json) to transparent 1080x1920 PNGs in Barlow 800.
import { createRequire } from "module";
import fs from "fs"; import path from "path"; import url from "url";
const require = createRequire(import.meta.url);
const { chromium } = require("/Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/node_modules/playwright");
const here = path.dirname(url.fileURLToPath(import.meta.url));
const n = process.argv[2];
const states = JSON.parse(fs.readFileSync(path.join(here, "tmp", `${n}_caps.json`), "utf8"));
const outDir = path.join(here, "tmp", `caps${n}`); fs.mkdirSync(outDir, { recursive: true });
const fonts = url.pathToFileURL(path.join(here, "../../../Brandkit/Design-System/fonts/fonts.css")).href;
const html = `<!doctype html><html><head><link rel="stylesheet" href="${fonts}"><style>
html,body{margin:0;width:1080px;height:1920px;background:transparent}
#c{position:absolute;left:60px;right:60px;transform:translateY(-50%);text-align:center;
 font-family:Barlow;font-weight:800;font-size:84px;line-height:1.02;letter-spacing:-0.01em;text-transform:uppercase;color:#fff;
 -webkit-text-stroke:14px #000;paint-order:stroke fill;text-shadow:0 6px 18px rgba(0,0,0,.45)}
#c b{color:#5B9BFF;font-weight:800}
</style></head><body><div id="c"></div></body></html>`;
const tmpHtml = path.join(outDir, "cap.html"); fs.writeFileSync(tmpHtml, html);
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto(url.pathToFileURL(tmpHtml).href);
await page.evaluate(() => document.fonts.load("800 84px Barlow"));
for (let i = 0; i < states.length; i++) {
  await page.evaluate(([h, y]) => { const c = document.getElementById("c"); c.innerHTML = h; c.style.top = y + "px"; }, [states[i].html, states[i].y]);
  await page.screenshot({ path: path.join(outDir, `${String(i).padStart(4, "0")}.png`), omitBackground: true });
}
await page.evaluate(() => { document.getElementById("c").innerHTML = ""; });
await page.screenshot({ path: path.join(outDir, "blank.png"), omitBackground: true });
await browser.close();
console.log("caps", n, states.length);

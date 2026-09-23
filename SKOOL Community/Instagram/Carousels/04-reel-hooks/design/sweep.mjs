// How large can the hook type actually go? Sweep font size and find where a
// hand-set two-line hook starts spilling to three, i.e. where the line breaks break.
import { chromium } from '/Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/node_modules/playwright/index.mjs';

const HOOKS = [
  'This listing went live in<br>twenty minutes.',
  'Three things I fix before<br>the photographer leaves.',
  'The room that sells this house<br>is not the kitchen.',
  'Nobody tours a house<br>because of the front door.',
  'Watch me write MLS remarks<br>in forty seconds.',
  'Every email my client gets for<br>thirty days, already written.',
  'I typed one line.<br>This is what came out.',
  'Here is the file that<br>replaced my Sunday.',
  'You are not bad at content.<br>You are bad at starting.',
  'Three to four hours per listing.<br>That was me.',
  'If you have an SOP,<br>you already have a skill.',
  'I do not film more. I film once.',
  'Your county just changed<br>something you should know about.',
  'Four headlines this week<br>that touch your buyers.',
  'I read the news so your<br>clients do not have to.',
  'Nobody in this market is<br>talking about this yet.',
];

const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });

for (const [size, numW, gap] of [[44,76,28],[46,80,28],[48,84,30],[50,88,30],[52,92,30],[56,96,30]]) {
  const textW = 952 - numW - gap;
  const html = `<html><head><meta charset="utf-8">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@500&display=swap">
  <style>body{margin:0;width:1080px}
  .t{width:${textW}px;font-family:'Inter',system-ui,sans-serif;font-weight:500;
     font-size:${size}px;line-height:1.28;letter-spacing:-0.012em}</style></head>
  <body>${HOOKS.map(h => `<div class="t">&ldquo;${h}&rdquo;</div>`).join('')}</body></html>`;
  await p.setContent(html, { waitUntil: 'networkidle' });
  await p.waitForTimeout(400);

  const r = await p.evaluate((s) => {
    const lh = s * 1.28;
    return [...document.querySelectorAll('.t')].map(e =>
      Math.round(e.getBoundingClientRect().height / lh));
  }, size);

  const intended = HOOKS.map(h => h.includes('<br>') ? 2 : 1);
  const over = r.map((n, i) => n > intended[i] ? i + 1 : 0).filter(Boolean);
  console.log(`${String(size).padStart(2)}px  text col ${textW}px  lines ${r.join(',')}` +
              (over.length ? `   SPILLS: hooks ${over.join(', ')}` : '   clean'));
}
await b.close();

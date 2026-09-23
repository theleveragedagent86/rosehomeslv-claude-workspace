# Reel covers (shared template)

Standalone Instagram Reel cover graphics, 1080x1920, Leveraged Agent Vector brand. Title graphics, never video frames.

- `cover.html?set=<id>&n=<N>`: titles + sublines live in the `SETS` object. Accent word = `<em>`.
- Odd N = black, even N = white, so the profile grid alternates when posted in order.
- All type sits inside y 340 to 1580, so the grid's 3:4 crop keeps the title. The title auto-fits (max 166px).
- `node shoot.mjs` renders every set; `node shoot.mjs oh` renders one. Output goes to `../<set folder>/covers/cover-NN.png`.

Sets: `wsu` = weekly-seller-update, `oh` = open-house-lead-automation. To add a video: add a set to `SETS` and a folder to `DIRS` in shoot.mjs.

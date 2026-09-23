---
name: listing-video
description: Use when someone asks to make a listing video, listing reel, property video, photo tour video, or a vertical short-form video from listing photos for Instagram Reels, TikTok, or YouTube Shorts. Free local alternative to Dundy AI / Calico AI.
---

# Listing Video

Turns 8 to 10 listing photos into a 1080x1920 reel. Default layout: photos move in the top half, the bottom half is pure black for Ryan's green-screen talking head. Local ffmpeg, no AI credits, no upload.

Renderer: `/Users/ryanrose/Downloads/Claude/_System/tools/listing-video/listing_video.py`
Full flag reference: the `README.md` beside it.

The script is deliberately dumb and deterministic. **Curation is your job**, not the script's. A
listing folder holds 90+ photos and most of them are duplicate angles of an empty room.

## Steps

### 1. Find the photos

Listings live in `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Clients/Listings/<Address>/Listing Photos/`.
Photos are usually one level deeper in a `<address>_web_vNN/` folder.

If the user names a listing, use it. If not, list the folders and ask which one.

### 2. Actually look at the photos before choosing

Do not pick by filename. Filenames like `dsc05435.jpg` say nothing, and adjacent numbers are
usually near-identical angles of the same room.

Build a contact sheet, then read it. Use `/usr/bin/python3`; the Homebrew `python3` first on PATH has no Pillow.

```python
from PIL import Image, ImageDraw
from pathlib import Path
src = Path("<listing photos folder>")
files = sorted(p for p in src.iterdir() if p.suffix.lower() in (".jpg", ".jpeg", ".png"))
cols, cw, ch = 8, 260, 190
sheet = Image.new("RGB", (cols*cw, ((len(files)+cols-1)//cols)*(ch+22)), (20,20,20))
d = ImageDraw.Draw(sheet)
for i, f in enumerate(files):
    im = Image.open(f); im.thumbnail((cw-8, ch-8))
    x, y = (i % cols)*cw, (i//cols)*(ch+22)
    sheet.paste(im, (x+4, y+4))
    d.text((x+6, y+ch+2), f"{i}: {f.stem[:26]}", fill=(230,230,230))
sheet.save("contact_sheet.png")
```

Write it to the scratchpad, Read it, then choose.

### 3. Choose 8 to 10 in tour order

More than 10 makes the reel too long for the format. The arc that works:

1. **Hero** — best exterior. A twilight drone shot if one exists, since it stops the scroll.
2. Second exterior or front entry
3. Entry / foyer
4. Main living space
5. Kitchen (the shot that sells the house, give it two slots if it's strong)
6. Primary bedroom
7. Primary bath
8. Backyard, ideally twilight, as the closer

Rules:
- Never two near-identical angles of the same room.
- Skip anything with visible clutter, trash cans, or photographer artifacts.
- Skip aerial neighborhood shots and any photo with burned-in labels or arrows.
- Prefer photos with a window or light source; empty white walls read as dead space.

### 4. Render

```bash
cd "<listing photos folder>"
python3 "/Users/ryanrose/Downloads/Claude/_System/tools/listing-video/listing_video.py" \
  --photos hero.jpg two.jpg three.jpg ... \
  --out "<listing folder>/Social Posts/<slug>-reel-9x16.mp4"
```

Output goes in the listing's `Social Posts/` folder. Run `--dry-run` first if the user wants to
review the shot plan.

### 5. Verify before handing it over

Do not just report success. Extract frames and look at them:

```bash
for t in 0.4 3.4 6.4 9.4 12.4 15.4 18.4 21.0; do
  ffmpeg -v error -y -ss $t -i "<out.mp4>" -frames:v 1 "g_$t.png"
done
```

Tile them into one strip, Read it, and check: every room reads clearly in the top panel and the
bottom half is solid black on every frame.

Add `--layout full` only if Ryan asks for a full-screen version with no green-screen area.

Then send the MP4 with SendUserFile.

## Fixing a shot that looks wrong

Pass a manifest instead of `--photos` to override any individual photo:

```json
[
  {"path": "hero.jpg", "treatment": "crop", "motion": "push", "seconds": 3.0},
  {"path": "living.jpg", "treatment": "blur", "motion": "pull"}
]
```

- `treatment`: ignored in split layout (always full-bleed in the top panel). In `--layout full`,
  `crop` = full-bleed, `blur` = 4:5 card on a blurred fill.
- `motion`: `push`, `pull`, `pan_left`, `pan_right`, `pan_up`, `pan_down`. Horizontal pans only have
  real travel on full-bleed landscape shots.

## Out of scope

No music, no captions, no end card, by design. Ryan delivers the CTA himself on camera. If the user wants any of those, add them in their editor, or say so
rather than silently adding a track.

# listing-video

Turns 8 to 10 listing photos into a vertical short-form reel. Free, local, no AI credits.
The open-source stand-in for Dundy AI / Calico AI's "photos to listing video" feature.

## Output

`1080x1920 · 30fps · H.264 / yuv420p (tv range) · silent AAC track · faststart MP4`

**Default layout (`split`):** photos move in the top 1080x960. The bottom 1080x960 is pure black,
for a green-screen talking head composited in the editor. No music, captions, or end card; the CTA
is delivered on camera.

`--layout full` fills the whole 9:16 frame with photos instead.

## Requirements

`ffmpeg` + `ffprobe` (`brew install ffmpeg`) and Python 3. No Python packages needed.

## Use

```bash
python3 listing_video.py --photos hero.jpg exterior.jpg entry.jpg ... --out reel-9x16.mp4
```

`--dry-run` prints the shot plan (treatment, motion, duration per photo) without rendering.

## How the motion works

- **Pans** use ffmpeg's `crop` filter with a moving window across an oversized source. Not `zoompan`:
  pre-cropping to the panel shape and then panning with `zoompan` barely moves.
- **Push/pull** use `zoompan`.
- Everything renders at 4x and downscales, because both filters quantize their window to whole
  input pixels and a 1080-wide source visibly stutters while moving.
- Which pans are offered depends on the photo vs the panel: wider than the panel pans sideways,
  taller pans vertically, a near match only zooms.
- In split mode a 3:2 photo in the 9:8 panel keeps 75% of its width, so whole rooms read clearly.

## Full layout only

Photos are 3:2 and the frame is 9:16, so full layout mixes two treatments:
- **crop** — full-bleed, pans sideways across the room.
- **blur** — every 3rd shot, and anything wider than 2.0: a 4:5 card on a blurred, darkened copy.
  Keeps ~83% of the room's width. A plain 3:2 pillarbox only covers ~40% of the screen, so that is
  deliberately not used.

## Notes

- Source JPEGs are full-range; the export converts explicitly to limited range, otherwise phones
  play it back washed out.
- `--manifest photos.json` overrides `motion` / `seconds` (and `treatment` in full layout) per photo.

## Flags

| Flag | Default | What it does |
|---|---|---|
| `--layout` | `split` | `split` = photos top, black bottom. `full` = photos fill frame |
| `--seconds` | 2.6 | Seconds per photo |
| `--transition` | `fade` | Any xfade name, or `cut` for hard cuts |
| `--pan-range` | 0.8 split / 0.5 full | Fraction of available travel a pan covers |
| `--zoom` | 1.12 | Push/pull extent |
| `--blur-every` | 3 | Full layout: every Nth shot gets the blurred-fill card (0 disables) |
| `--fit` | `auto` | Full layout: force `crop` or `blur` for every shot |

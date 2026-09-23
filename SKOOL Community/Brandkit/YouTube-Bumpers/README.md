# YouTube Bumpers, The Leveraged Agent

Branded video assets used on **every YouTube upload**. Rendered from HTML with [hyperframes](https://hyperframes.heygen.com), so the source is version controlled and re-renderable instead of living in a video editor.

**These are for YouTube only. Do not put them on Skool lessons.** See "Why not Skool" at the bottom.

| File | Runtime | What it is |
|---|---|---|
| `renders/bumper.mp4` | 3.0s | Intro sting. Accent rule draws, wordmark rises, both retract and land on black. |
| `renders/bumper-9x16.mp4` | 3.0s | Same sting at 1080x1920, stacked wordmark. Source `compositions/bumper-vertical.html`. The end tag on Reels / Shorts, where it goes LAST, not after a hook. |
| `renders/like-subscribe.mov` | 6.0s | **Transparent overlay, mid-roll.** Like and Subscribe chips slide in over your footage, the thumb gets pressed, they slide out. |
| `renders/like-subscribe-end.mov` | 20.0s | **Transparent overlay, the ending.** Same chips, plus the wordmark panel in the top half. No exit, the video cuts on it. |

All 1920x1080 (except bumper-9x16.mp4, 1080x1920), 30 fps, silent. Lay your own music under them.

**There is no full-frame end card.** It was built, then deleted on 2026-08-24. The outro is now an overlay on Ryan's own footage, because a talking human holds attention where a static card bleeds it. Do not rebuild one without a reason.

**The renders are not in git.** The workspace `.gitignore` excludes `*.mp4` and `*.mov` to keep `Final Videos/` out, and that catches these too. That is fine: the HTML sources are committed, the render is deterministic, and rebuilding everything takes about 90 seconds.

## The two overlays

Both are **ProRes 4444, `yuva444p12le`, real alpha**. Drop one on the video track above your footage and it composites straight over the picture. No green screen, no keying, no blend mode.

Each chip carries its own surface and a real drop shadow, because the footage underneath is an unknown brightness. Both have been checked over a light background and a dark one, not just over black.

**`like-subscribe.mov`, 6s, mid-roll.** Chips only, bottom left, 96px in and 132px up. That keeps them clear of YouTube's progress bar and the player controls in the bottom right. Fully transparent by the last frame, so it leaves no residue on the timeline.

**`like-subscribe-end.mov`, 20s, the ending.** Adds the wordmark in the top half, left aligned. It holds for the full 20 seconds with no exit animation, because your video ends on it. The subscribe chip pulses at 2.9s, 8.4s and 14.2s so a frame grabbed at second 14 is not a frozen picture.

**Ryan approved the wordmark panel by name on 2026-08-24. Do not strip it.** Two alternatives were built and are dead: a soft full-bleed radial scrim, which read as a giant dark oval over light footage, and bare white type with a dark keyline, which he did not want.

**What he did reject is motion during the hold.** An earlier ending drifted the panel slowly upward across the 20 seconds and he rejected it outright. Everything now animates in and then holds dead still, apart from the three subscribe pulses. Do not add drift, float, or a breathing loop.

**75.6% of the frame is fully transparent**, measured off the alpha channel. The panel, the two chips and their soft drop shadows are the only things painted. Every corner and the dead centre read alpha 0.

**Where to put the mid-roll one.** Twice in a 12 minute video is the ceiling:

1. **Right after the first win lands**, silent, no verbal ask. Peak goodwill, and the viewer has just been given something.
2. **On the closing subscribe line** (that is where the 20s ending version starts).

Never put either in the first 30 seconds, and never pause your delivery for one.

**If your editor will not import ProRes 4444**, re-render as an RGBA PNG sequence instead:

```bash
npx hyperframes@latest render . -c compositions/like-subscribe.html -o renders/like-subscribe-frames --format png-sequence --fps 30
```

A WebM alternative was tried and **rejected**: hyperframes' WebM path and a hand-rolled `libvpx-vp9 -pix_fmt yuva420p` transcode both decoded back as fully opaque, which would paint a black box over the footage. Do not re-add a WebM without checking the decoded alpha first, with the command under "Verifying alpha".

## Where they go in the edit

**The bumper does not go at 0:00.** A logo animation in the first three seconds is the single most reliable way to lose a cold viewer. It goes **after the hook**, once the viewer has decided to stay.

```
0:00   hook, cold, no branding
0:35   BUMPER, 3s
0:38   the video
       ...
4:35   like-subscribe.mov, 6s, silent, over the shot
       ...
11:45  like-subscribe-end.mov, 20s, over your close
12:05  end
```

## The left column is load bearing

**Everything in the ending overlay lives in the left column, on purpose.** Measured extents, at 1920x1080:

| Element | x | y |
|---|---|---|
| Wordmark panel | 96 to 880 | 244 to 464 |
| Like + Subscribe chips | 96 to 693 | 832 to 947 |

Measured off the alpha channel of the actual render, not off the CSS. That leaves **everything right of x=880 completely clear**, plus the whole band between the panel and the chips. That empty right side is where YouTube's clickable end screen cards go. Do not spread these elements across the frame or there is nowhere to put the cards.

### What this costs you at shoot time

> **For the last 20 seconds, keep yourself in the RIGHT half of the frame.** The overlay owns the left. If you are centred or framed left, the wordmark panel lands on your shoulder or your face.

Note this reverses the earlier guidance, from back when the outro was a separate full-frame card.

Keep rolling about eight seconds past your final word. Cutting on the last syllable makes the video feel broken and gives the cards nowhere to live.

**In Studio, Editor, End screen:** set the elements to the **last 20 seconds** and put the two video or playlist cards in the right half, clear of your face. YouTube's own Subscribe element is optional here, since the chip already makes the ask visually; if you want a clickable one, the gap at roughly x 750 to 900, y 850 to 960, just right of the chips, is free.

## Re-rendering

```bash
cd "/Users/ryanrose/Downloads/Claude/SKOOL Community/Brandkit/YouTube-Bumpers"
npx hyperframes@latest render . -c compositions/bumper.html -o renders/bumper.mp4 --fps 30 --quality high
npx hyperframes@latest render . -c compositions/bumper-vertical.html -o renders/bumper-9x16.mp4 --fps 30 --quality high
npx hyperframes@latest render . -c compositions/like-subscribe.html -o renders/like-subscribe.mov --format mov --fps 30 --quality high
npx hyperframes@latest render . -c compositions/like-subscribe-end.html -o renders/like-subscribe-end.mov --format mov --fps 30 --quality high
```

`--format mov` is what turns on alpha. Without it you get an opaque black frame and the overlay is useless.

The two overlays share their chip markup and CSS by copy, not by import. **If you restyle a chip, change it in both files.**

### Verifying alpha

Never trust `ffprobe` alone here. Decode the alpha channel and read actual pixels, one spot that should be empty and one that should be solid:

```bash
ffmpeg -v error -i renders/like-subscribe.mov -vf "select=eq(n\,64),format=rgba,alphaextract,crop=8:2:0:0" -fps_mode passthrough -frames:v 1 -f rawvideo -pix_fmt gray - | xxd | head -1
```

Top left corner must come back `0000…` (transparent). Sampling inside the Subscribe pill at `crop=8:2:500:880` must come back `ffff…` (opaque).

## Design notes, so a future edit does not break the brand

- **Palette is Vector v2.0, inverted side.** True black ground, white ink, `#9AA3BC` secondary, `#5B9BFF` accent as text and as hairlines. `#1768E5` is the fill value and is **too dark to use as a line on black**, which is why every rule here is `#5B9BFF`.
- **The Subscribe chip is `#1768E5` fill with white on it.** That is the canonical 5.06:1 accent-on pairing, and a solid accent block is the one thing guaranteed to read over unknown footage. The Like chip stays a dark surface so the two do not compete.
- **The wordmark sits on a panel, and Ryan picked that.** It matches the chip surface exactly, `rgba(6,10,26,0.93)` with a `#2A3550` hairline, so the left column reads as one object. The alternatives are on the dead list above. Bare white type was measured as close to unreadable over a `#F2EFE9` background, which is the whole reason the wordmark needs a surface of some kind.
- **Nothing moves during the hold.** Entrance animations only, plus the three subscribe pulses. This was a direct correction, not a preference.
- **Typographic wordmark, no logo file.** Every logo PNG in `../` is still v1 cream and teal artwork and is off-palette under Vector. When the logos are regenerated, both the bumper and the ending can use the real mark.
- **The grain layer in the bumper is not decoration.** Radial gradients on true black band into visible ovals once H.264 quantises them. The fixed-seed SVG noise at 5% dithers that away. The overlays have no grain because they have no gradient to dither.
- **`immediateRender: false` on the tap ring is load bearing, in both overlays.** GSAP's `fromTo` defaults it to true, which stamps the from-state at build time and leaves the ring visible from frame 0. It was caught that way once already.
- Only `transform` and `opacity` are animated, so the capture stays cheap and seek accurate.
- No `Math.random()` or `Date.now()` anywhere. Renders must be identical on re-run.

## Why not Skool

A bumper and a subscribe ask both assume a stranger who has to be converted. On Skool everyone is already inside, there is nothing to subscribe to, and the community link is the page they are already on.

Worse, it costs the binge watcher. Fourteen lessons times a 3 second sting is 42 seconds of logo animation for someone working through the course in order.

**Skool lessons open cold on the deck title slide and close on the last slide of the deck.** That is already built.

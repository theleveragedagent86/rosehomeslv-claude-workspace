# Optional images for the Relocation hub

**You do not need these.** The page is finished and publishable exactly as it is.
The hero is text on navy on purpose, so it does not look like a clone of the
New Construction hub, and the communities grid reuses the 6 images already on
the CDN. This file is only here for later, if you want to add art.

Higgsfield MCP needs re-authorization before I can generate anything. Reauthorize
it in claude.ai connector settings, then tell me to run these.

---

## Image rules for this site (learned the hard way)

- **No desert.** No saguaro cactus (that is Arizona, not Nevada). No red sandstone
  unless the shot is specifically far-west Summerlin near Red Rock.
- Correct backdrops: Spring Mountains, McCullough Range, Sheep Range / Gass Peak,
  Exploration Peak.
- Show the kind of homes that actually exist here: stucco, tile or flat roof,
  desert-modern or Spanish-Mediterranean, two-car garage, low-water front yard
  with real landscaping.
- No people with visible faces. No signage, no logos, no readable text.
- Photoreal, natural light, wide angle, no HDR halo, no fisheye.
- Export target: 900 x 672 JPEG, quality 82.
  `sips -s format jpeg -s formatOptions 82 --resampleHeightWidth 672 900 in.png --out out.jpg`
  (height first, then width, that argument order is not a typo)

---

## 1. Hero (only if you want to move away from the flat navy)

Target: 2400 x 1000, then crop.

> Wide cinematic photograph of a residential Las Vegas valley neighborhood at
> golden hour, shot from a slight elevation. Rows of newer stucco homes with tile
> roofs, mature street trees, wide streets. The Spring Mountains sit on the
> horizon in soft haze. Warm low sun, long shadows, calm and welcoming. No people,
> no cars in focus, no signage, no text. Photoreal, natural color, wide angle lens,
> no HDR.

If you use this, the hero copy has to sit on a dark overlay or it will not be
readable. Tell me and I will add the overlay CSS, do not just drop the image in.

## 2. "Pick the commute first" band

Target: 1600 x 900.

> Photograph looking down a wide Las Vegas valley arterial road in early morning,
> residential walls and landscaped medians on both sides, mountains ahead in the
> distance. Light traffic, soft morning light. No readable signage, no logos,
> no people. Photoreal, natural color.

## 3. "What changes when you become a Nevadan"

Target: 1600 x 1200 vertical-ish.

> Photograph of the front of a newer single story Las Vegas home in the late
> afternoon, stucco with a tile roof, two car garage, low-water front yard with
> real plants and decorative rock, small covered entry. Neighboring homes softly
> out of focus. No people, no address numbers, no signage. Photoreal, natural color.

## 4. Missing community cards (Skye Canyon, Centennial Hills, North Las Vegas)

These 3 already have images on the CDN and they are fine. Only regenerate them
if you decide the current ones look too desert-heavy. Prompts and the full
regeneration procedure live in `../img/REGEN-PROMPTS.md`.

---

## After generating

1. Commit to `theleveragedagent86/rhlv-site-images` under a new `relocation/` folder.
2. Purge the jsDelivr cache for each file:
   `https://purge.jsdelivr.net/gh/theleveragedagent86/rhlv-site-images@main/relocation/<filename>`
3. Byte-compare the CDN copy against the local file before you trust it. jsDelivr
   has served a stale image before.
4. Give me the URLs and I will wire them into `ALL-IN-ONE-relocation.html` with
   the right overlay and alt text. Do not paste raw `<img>` tags into the page,
   the card and hero markup have specific classes.

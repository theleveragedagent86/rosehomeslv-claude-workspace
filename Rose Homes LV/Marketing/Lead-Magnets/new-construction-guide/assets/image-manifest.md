# Image manifest

Every photograph the guide and its landing page need, what it is for, and the exact prompt that
produced it. Generated with Higgsfield `nano_banana_2`. This file ships standalone so art can be
regenerated in a second pass without rebuilding anything else.

## Rules every image obeys

- **No people.** Fair housing. No figures, no silhouettes, no hands, nothing that reads as a person.
- **No identifiable community.** No entry monuments, no builder signage, no recognizable model home
  or subdivision. The guide is builder-agnostic and must not appear to endorse or depict one.
- **No text of any kind** rendered inside the image. No logos, no street signs, no billboards.
- **Clark County geography only.** Mojave desert, the valley basin, the surrounding ranges. Never
  Pahrump, Mesquite or Boulder City, and never a landscape that reads as another state.
- **Mojave, spelled out.** The model's default "desert" is Sonoran, so the first pass put saguaro
  cactus in two images and returned Utah canyon country with junipers for the Summerlin inset.
  Saguaro does not grow within 200 miles of Las Vegas. Every prompt now names the allowed plants and
  forbids the wrong desert explicitly. See the Mojave block below.
- **Print-honest.** Restrained contrast, no HDR halos, no oversaturation. The palette runs navy and
  sunset already; a photograph that arrives oversaturated fights the page instead of sitting in it.
- **Every image is reviewed against the three rules above before it ships.** The review column is
  not decorative. An unreviewed image does not go in the guide.

## Resolution policy

A full-bleed Letter page is 8.5in wide. At 300dpi that is 2550px. The relocation-guide photos this
set replaced were 896x1200, about **105dpi at full-bleed**, which is fine on screen and visibly soft
in print.

**Everything except the cover was generated free** under Ryan's 3-day Unlimited Marketplace pass,
which is a **web-app entitlement the MCP connector cannot see**: `models_explore` reports
`unlim: {available: false}` and still preflights 2k at 2 credits while the same account generates
free in the browser. Two constraints come with it. **4k is not included**, only 1k and 2k carry the
Unlimited badge. And unlimited runs are **strictly one generation at a time** on the standard queue,
so they cannot be batched; submitting a second while one is running is silently rejected. Expect
90 to 180 seconds per image.

2k delivers better than its name suggests:

| Request | Delivered | At full-bleed Letter | Credits |
|---|---|---|---|
| 21:9 at 2k | 3168x1344 | 373 dpi | free on unlimited, else 2 |
| 4:3 at 2k | 2400x1792 | 282 dpi | free on unlimited, else 2 |
| 3:2 at 4k | 5056x3392 | 595 dpi | 3, never free |

The 4:3 insets sit small inside a page rather than bleeding, so 282 dpi is comfortable there. Only
the cover needed 4k, and it is the one image that cost credits.

## The set

All fifteen are generated, installed and reviewed. Three were regenerated once for the Mojave
problem, noted in the review column.

| ID | File | Where | Aspect | Installed | Reviewed |
|---|---|---|---|---|---|
| IMG-01 | `cover.jpg` | p1 cover, full bleed top | 3:2 | 3060x2053, 360dpi | **pass** |
| IMG-02 | `open-front.jpg` | Block 1 opener band, p2 | 21:9 | 3168x1344, 373dpi | **pass on redo.** First pass had saguaro on the far ridge |
| IMG-03 | `open-path-a.jpg` | Block 2 opener band, p6 | 21:9 | 3168x1344, 373dpi | **pass.** Joshua trees, Red Rock escarpment, correct Mojave |
| IMG-04 | `open-path-b.jpg` | Block 3 opener band, p10 | 21:9 | 3168x1344, 373dpi | **pass on redo.** First pass was Sonoran, saguaro throughout, read as Phoenix |
| IMG-05 | `open-path-c.jpg` | Block 4 opener band, p14 | 21:9 | 3168x1344, 373dpi | **pass** |
| IMG-06 | `open-core.jpg` | Block 5 opener band, p18 and p19 | 21:9 | 3168x1344, 373dpi | **pass.** Best of the set |
| IMG-07 | `open-areas.jpg` | Block 6 opener band, p28 | 21:9 | 3168x1344, 373dpi | **pass** |
| IMG-08 | `open-builders.jpg` | Block 7 opener band, p32 | 21:9 | 3168x1344, 373dpi | **pass** |
| IMG-09 | `open-snapshot.jpg` | Block 8 opener band, p36 | 21:9 | 3168x1344, 373dpi | **pass.** Strip skyline in haze, a landmark not a community |
| IMG-10 | `open-back.jpg` | Block 9 opener band, p38 | 21:9 | 3168x1344, 373dpi | **pass** |
| IMG-11 | `area-summerlin.jpg` | p28, inset | 4:3 | 2400x1792, 282dpi | **pass on redo.** First pass was Utah canyon country with junipers |
| IMG-12 | `area-northwest.jpg` | p29, inset | 4:3 | 2400x1792, 282dpi | **pass** |
| IMG-13 | `area-henderson.jpg` | p30, inset | 4:3 | 2400x1792, 282dpi | **pass** |
| IMG-14 | `area-north-lv.jpg` | p31, inset | 4:3 | 2400x1792, 282dpi | **pass** |
| IMG-15 | `hero.jpg` | landing page hero | 4:3 | 2400x1792, 282dpi | **pass.** Same composition family as the cover |

**Cost: 3 credits, all of it the cover.** The other fourteen plus three regenerations were free.

No image in the set contains a person, a vehicle, signage, a logo, rendered text, or an identifiable
community. That gate passed on the first pass for all fourteen; the three redos were geography, not
fair housing.

## Alt text, canonical

**`assemble.py` writes these into the guide and overwrites whatever a fragment carried.** Alt text is
single-sourced here for the same reason citation numbers are generated: nine of the fifteen images
appear on more than one page, three chapter writers each authored their own wording for the same file,
and the guide would have shipped one photograph described three different ways.

Written 2026-07-29 against the installed files, not against the prompts, and checked line by line
against the three rules at the top of this file. **No person, no signage, no house number, no
identifiable community appears in any of them**, because none appears in any image.

Describe what is in the frame and stop. These are atmospheric section openers, not evidence, and a
screen reader user gains nothing from an adjective.

| File | Alt text |
|---|---|
| `cover.jpg` | Red sandstone ledges in the foreground at blue hour, the Las Vegas valley below filled with the first city lights, a distant mountain range under deep indigo sky with a narrow amber band above the ridgeline. |
| `open-front.jpg` | An empty graded building pad at first light, bare compacted caliche soil with survey stakes and string lines, a low rocky ridge in the middle distance under a pale cool sky. |
| `open-path-a.jpg` | The Las Vegas basin seen from high on a mountain road at mid morning, the whole valley flat to a far range, joshua trees and creosote in the foreground, clear dry air. |
| `open-path-b.jpg` | Established desert suburban rooftops in warm late afternoon light, tile roofs and mature landscaping receding toward a bare rocky mountain range, shot long so no single house is the subject. |
| `open-path-c.jpg` | New stick framing against open sky at golden hour, raw lumber studs and roof trusses over plywood sheathing, desert ground and a distant ridge beyond. |
| `open-core.jpg` | The Las Vegas valley at dusk from a low ridge, dense city lights spreading to the horizon under deep blue sky, the last warm light on the mountains at the right edge. |
| `open-areas.jpg` | The Las Vegas valley at midday from the west, red rock formations in the foreground, the basin and its far mountain wall under a bright dry sky. |
| `open-builders.jpg` | A residential construction site at overcast noon, banded lumber and roof tile stacked on pallets beside concrete foundation forms on flat desert ground, in muted even light. |
| `open-snapshot.jpg` | The Las Vegas skyline at long distance in flat morning light, heat haze compressing the towers against a pale sky, open desert in the foreground. |
| `open-back.jpg` | The Mojave desert at sunrise, low warm light raking across sand and creosote, a quiet mountain range on the horizon. |
| `area-summerlin.jpg` | A steep red sandstone escarpment rising straight out of a flat open desert floor in late afternoon light, layered red and cream cliff faces catching warm side light, creosote and yucca on the ground below. |
| `area-northwest.jpg` | Open high desert in clear morning light, joshua trees and pale gravel flats running toward a long dry mountain range on the northern horizon. |
| `area-henderson.jpg` | Rolling desert terrain in early evening light, low hills stepping up toward a dark isolated peak, warm side light raking across the slopes. |
| `area-north-lv.jpg` | A flat open desert basin at midday, creosote flats running out to a long mountain range on the northern horizon under a high bright sky. |
| `hero.jpg` | Red sandstone in the foreground at sunset with the Las Vegas valley spread out behind it under a coral and gold sky. |

## Job IDs

Masters are not kept in the repo. The job ID re-downloads the original PNG at full resolution if a
larger crop is ever needed. The URL pattern is

```
https://d8j0ntlcm91z4.cloudfront.net/user_3DYyD34wiFmRXwmvikBAeEkPzhE/hf_<YYYYMMDD>_<HHMMSS>_<job-id>.png
```

| ID | Job | Stamp |
|---|---|---|
| IMG-01 | `5b02a136-c4a3-4c3f-ac5a-bda450d41650` | 20260729_062825 |
| IMG-02 | `b5441f2e-841e-4367-9090-d2972dd7750c` | 20260729_174137 |
| IMG-03 | `cc3e85f0-dc7e-4b16-b44f-4187cd5dfd09` | 20260729_154711 |
| IMG-04 | `1dc6bdef-7682-4522-b735-935619632746` | 20260729_174750 |
| IMG-05 | `34d715f7-05a1-46d0-9889-077ca865b6cc` | 20260729_154742 |
| IMG-06 | `0b65a342-a468-4568-bee0-9e18f8e058cc` | 20260729_154747 |
| IMG-07 | `b5200c38-f3dc-43b9-8dbd-fd630067fbce` | 20260729_155026 |
| IMG-08 | `d770030d-2fcc-4582-82c7-960eeabc3c5d` | 20260729_155318 |
| IMG-09 | `da6b5986-689b-4227-91a7-e824fde79798` | 20260729_155614 |
| IMG-10 | `55fde4dd-d3f0-41e0-a7b3-03add3f47917` | 20260729_170421 |
| IMG-11 | `05485432-2857-40fb-8944-368319b9a001` | 20260729_175340 |
| IMG-12 | `004a7bc5-e978-463c-953d-0f5eaf0dd859` | 20260729_171251 |
| IMG-13 | `acff7aaa-5368-4248-9045-c1d00310410e` | 20260729_171745 |
| IMG-14 | `b36e3e05-1f38-4092-9a8e-a884344a4b60` | 20260729_172335 |
| IMG-15 | `4a470c12-99d6-443b-bb3a-c538b3425225` | 20260729_172905 |

The superseded first passes for IMG-02, IMG-04 and IMG-11 are `ba490a4f-f43f-4704-a75e-69bf2b4683df`,
`46c2f4e3-773e-472a-a4b1-c2f0d123cd43` and `e9a74965-b7e7-4d6e-89fd-be033828a96c`. Kept only so the
Mojave failure is reproducible; do not install them.

Note the model field on every job reads `nano_banana_flash`. The request is `nano_banana_2`; the
server routes it internally. That is expected, not a wrong model.

## Prompt formula

Every prompt is built the same way, so the set looks like one photographer shot it:

1. **Shot type and subject.** "Wide documentary photograph of ..."
2. **Foreground anchor.** Sandstone, desert scrub, graded pad, framing lumber. Something with texture
   close to the lens, because a band crop that is all sky is dead space.
3. **Light.** Named explicitly: blue hour, low sun, overcast noon. This is what keeps the set coherent.
4. **The Mojave block**, on any prompt where plants or terrain are visible. "Mojave desert only:
   creosote bush, joshua tree, yucca and low desert scrub. Absolutely no saguaro cactus and no
   Sonoran desert plants." For a red rock subject add "no juniper, no pine, no green canyon
   vegetation, no mesas and no canyon country," which is what pulled the Summerlin inset out of Utah.
5. **The exclusion block, verbatim every time.** "Absolutely no people, no cars, no signage, no logos,
   no text of any kind, no identifiable buildings or subdivisions."
6. **The print block, verbatim every time.** "Natural available light, restrained contrast, no HDR
   halos, no oversaturation, fine detail suitable for large format print."

Keeping blocks 5 and 6 word for word across the set is the whole trick. Rewriting them per image is
how a set drifts. Block 4 is the one that has to be tuned to the subject, because the wrong desert
is a different failure in a rooftop shot than in a cliff shot.

**Never trust "desert" to mean Mojave.** Left unqualified the model reaches for Sonoran: saguaro,
palo verde, Tucson mountains. Nobody in Las Vegas will read that as Las Vegas, and it is the single
most likely thing to go wrong in a regeneration pass.

## Prompts

**IMG-01, cover.** Wide documentary photograph of the Las Vegas valley at blue hour, seen from a red
sandstone ridge in the near foreground. The basin below is filled with the fine grain of city lights
just coming on; a distant mountain range sits on the horizon under a deep indigo twilight sky with a
narrow warm amber band low above the ridgeline. Desert scrub and layered sandstone in the foreground.
*(+ exclusion block, + print block)*

**IMG-02, front matter.** Wide documentary photograph of an empty graded residential pad at first
light, compacted caliche soil with survey stakes and string lines, a low bare rocky Mojave desert
ridge in the middle distance, pale cool morning sky. *(+ Mojave block, + blocks)*

**IMG-03, path A, relocators.** Wide documentary photograph of the Las Vegas basin from high on a
mountain road at mid morning, the whole valley laid out flat to a far range, Joshua trees and
creosote in the foreground, clear dry air, long view. *(+ blocks)*

**IMG-04, path B, move-up.** Wide documentary photograph of established desert-suburban rooftops in
warm late afternoon light, tile roofs and mature landscaping receding toward a bare rocky Mojave
mountain range, shot long so no individual house is the subject. Southern Nevada only: palms,
creosote and low desert scrub. *(+ Mojave block, + blocks)*

**IMG-05, path C, first new build.** Wide documentary photograph of new stick framing against an open
sky at golden hour, raw lumber studs and trusses, plywood sheathing, desert ground and a distant
ridge beyond. *(+ blocks)*

**IMG-06, core.** Wide documentary photograph of the Las Vegas valley at dusk from a low ridge, dense
city lights spreading to the horizon under a deep blue sky, the last warm light on the mountains at
the right edge. *(+ blocks)*

**IMG-07, areas.** Wide documentary photograph of the Las Vegas valley at midday from the west, red
rock formations in the foreground, the basin and its far mountain wall under a bright dry sky.
*(+ blocks)*

**IMG-08, builders.** Wide documentary photograph of a residential construction site at overcast
noon, stacks of banded lumber and roof tile on pallets, concrete foundation forms, flat desert
ground, muted even light. *(+ blocks)*

**IMG-09, market snapshot.** Wide documentary photograph of the Las Vegas skyline at long distance in
clear flat morning light, heat haze compressing the towers against a pale sky, desert foreground.
*(+ blocks)*

**IMG-10, back matter.** Wide documentary photograph of the Mojave desert at sunrise, low warm light
raking across sand and creosote, a quiet mountain range on the horizon, calm and open. *(+ blocks)*

**IMG-11 to IMG-14, area insets.** Same formula, one per area, differentiated only by terrain and
time of day.

- **Summerlin.** A steep red Aztec sandstone escarpment rising straight out of a flat open Mojave
  desert floor in late afternoon light, layered red and cream cliff faces catching warm side light,
  creosote and yucca scrub on the flat ground below, bare rock and open sky. Absolutely no juniper,
  no pine, no green canyon vegetation, no mesas and no canyon country. *(+ blocks)* The negatives
  are load-bearing: without them this comes back as Utah.
- **Northwest.** Open high desert in clear morning light, joshua trees and pale gravel flats running
  toward a long dry mountain range on the northern horizon. *(+ blocks)*
- **Henderson.** Rolling desert terrain in early evening light, low hills stepping up toward a dark
  isolated peak, warm side light raking across the slopes. *(+ blocks)*
- **North Las Vegas.** A flat open desert basin at midday, creosote flats running to a long mountain
  range on the northern horizon, high bright dry sky. *(+ blocks)*

**IMG-15, landing hero.** Same composition family as IMG-01, framed 4:3 so the crop holds at
375px wide.

## Regenerating this set

Because unlimited is a browser-only entitlement, a refresh runs through the Higgsfield web app, not
the MCP connector. The loop that works:

1. `higgsfield.ai/ai/image?model=nano-banana-2`, then set model Nano Banana 2, the aspect for that
   image, quality **2K**, count 1, and switch **Unlimited on**. The button should read "Unlimited"
   with no credit price. If it reads "Generate 2", the toggle is off and you are about to spend.
2. **The toggle resets to off on every page load.** Check it before each submit, not once at the start.
3. Paste the prompt, submit, and **wait for the tile to finish before submitting the next one.**
   Unlimited serializes to one job at a time and silently drops anything sent while one is running.
4. Harvest with `show_generations` on the MCP side rather than scraping the page: the in-page image
   URLs are signed and come back redacted, while `show_generations` returns clean CloudFront URLs
   plus the prompt each one used, which is also how you confirm nothing was dropped.
5. Convert to JPEG q90 progressive on install. A 3168px PNG is about 9MB and the guide carries nine.

## Vector artwork, not photography

The valley orientation map is **not** a photograph and not a real street map. It is SVG-10 in
`outline/guide-outline.md`, hand-built as an abstract schematic. Pahrump, Mesquite and Boulder City
are not drawn. If a flat illustrated treatment is wanted instead, `recraft_v4_1` in `vector` mode
accepts an explicit palette of up to ten hex values, which should be taken from
`build/design-system.md` rather than invented.

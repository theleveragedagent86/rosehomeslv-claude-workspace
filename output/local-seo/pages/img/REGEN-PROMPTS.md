# New Construction page — image regeneration prompts

Replaces the 6 community card images. **Hero and design-center images stay**, they are fine.

## Why these are being replaced

The current cards are generic "Southwest desert" stock look: red sandstone mesas, tan-on-tan
palette, hazy sunset, and **saguaro cactus**. Saguaros do not grow in Nevada, they are a Sonoran
Desert / Arizona plant. A local buyer or agent spots that instantly and it makes the page look
fake. Red sandstone is only correct for far-west Summerlin near Red Rock, not Henderson or
North Las Vegas.

## Global style block (prepend to every prompt)

```
Photorealistic real estate photography, new construction production homes in the Las Vegas
valley, Nevada. Shot on a full frame camera, 24mm, eye level from the street, natural daylight,
clear deep blue sky, crisp shadows. Architecture: stucco in white, greige, warm grey or
charcoal, low pitch concrete tile roof or flat modern parapet roofline, black or bronze window
frames, stacked stone or smooth plaster accent columns, two and three car garages facing the
street, wide broom finish concrete or paver driveways, paver walkways, block privacy walls
between rear yards, full sidewalks and streetlights.

Landscaping: decomposed granite and drip irrigation, Mexican fan palms, olive trees, desert
willow, red yucca, lantana, rosemary, African sumac, small strips of artificial turf. No front
lawns (Nevada restricts turf on new builds).

NEGATIVE / do not include: saguaro cactus, red sandstone mesas or buttes, Sedona or Monument
Valley rock formations, tumbleweeds, open raw desert, adobe or pueblo architecture, terracotta
Spanish tile with tan stucco, orange or pink hazy sunset, dust haze, cowboy or Old West
elements, palm-lined resort boulevard, the Las Vegas Strip, casinos, neon.
```

## Per-image prompts

**community-summerlin.jpg** (900x672)
> Contemporary desert-modern two-story homes on a Summerlin street in west Las Vegas. Clean
> horizontal massing, white and charcoal stucco, flat parapet rooflines, black window frames,
> mature street trees, a landscaped trail entrance. Far background: the grey-brown Spring
> Mountains ridgeline, softly hazed by distance, low in frame. Red Rock escarpment may appear
> small and distant on the far left only.

**community-henderson.jpg** (900x672)
> A Henderson master-planned community street in the southeast valley, Inspirada or Cadence
> style. Mix of single-story and two-story homes, warm white and grey stucco, low pitch tile
> roofs, stone accent columns. A real green neighborhood park with grass and a shade structure
> visible down the street. Background: the low brown McCullough Range, no dramatic rock.

**community-skye-canyon.jpg** (900x672)
> Modern farmhouse new construction in Skye Canyon, far northwest Las Vegas. White board and
> batten and white stucco, dark charcoal standing seam metal roof accents, black windows, black
> coach lights, covered front porches. Higher elevation, cooler light, slightly cooler color
> temperature. Background: the Sheep Range and Gass Peak, grey-brown, distant.

**community-centennial-hills.jpg** (900x672)
> An established Centennial Hills street in northwest Las Vegas. Wide street, two-story stucco
> homes in soft beige and grey with low pitch tile roofs, mature Mexican fan palms and African
> sumac, sidewalks, block walls. Settled and lived-in, not brand new dirt. Background: low
> grey-brown foothills, mostly sky.

**community-mountains-edge.jpg** (900x672)
> A Mountain's Edge street in southwest Las Vegas. Two-story homes, greige and white stucco,
> stone veneer entries, three car garages, paver driveways. A neighborhood park with a walking
> path visible. Background: Exploration Peak, a rounded brown hill, not a cliff.

**community-north-las-vegas.jpg** (900x672)
> A newer North Las Vegas subdivision, entry-level product. Flat terrain, denser lots, two-story
> homes in white, light grey and tan stucco, two car garages, small front yards in decomposed
> granite with young trees. Some homes still framed in the background. Background: flat horizon
> with distant low mountains, big open sky.

## After generating

1. Save into this folder with the **same filenames** (the page hotlinks them by name).
2. Push to `theleveragedagent86/rhlv-site-images` under `new-construction/`.
3. jsDelivr caches by tag. `@main` should pick up new commits within minutes, but if the old
   images persist, purge at `https://purge.jsdelivr.net/gh/theleveragedagent86/rhlv-site-images@main/new-construction/<filename>`.
4. No HTML change needed if filenames match.

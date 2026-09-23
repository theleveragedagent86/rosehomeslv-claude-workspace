# Recon: Ken Pozek "Moving to Orlando" Relocation Guide

Handoff notes for another session. This documents the **reference asset** Ryan wants to
model a Las Vegas relocation guide on, plus how it was reverse-engineered.

Reference URL: https://www.pozek.com/relocation-guide-digital/
Actual source file (the flipbook just renders this PDF):
`https://www.pozek.com/uploads/agent-1/Relocation.Guide.Single/Pozek_Orlando_Guide-New_Update-R16.pdf`

---

## What it actually is

- A **43-page relocation magazine**, delivered on the site as a JavaScript page-flip
  viewer (PDF.js style) and also directly downloadable. The "digital guide viewer" is
  not a custom CMS thing — it is literally a PDF.
- **Built in Adobe InDesign 21.2 (Mac)**, exported as **print-grade PDF/X-1:2001, CMYK**,
  page size **599.4 x 774 pt (~8.32 x 10.75")** portrait, **~22.6 MB**.
- Internal InDesign title: **"Pozek Orlando Guide-Jan 2026 NEW.indd"**. Public filename
  ends in **"R16"** = 16th revision. This is a long-iterated, roughly-annual print piece
  that is also published digitally.
- Cover title: **"MOVING TO ORLANDO — your guide to relocating to greater Orlando."**
  (This exact naming convention was mirrored for the LV build.)

---

## Full page-by-page structure (43 pp)

**Front / brand (1-3)**
- p1  Cover: big display type over an illustrated sunset skyline + flat pastel map motif.
- p2  Welcome letter from Ken Pozek (headshot + signature).
- p3  Signature flex: **"The Official Real Estate Team of the Orlando Magic"** — full team
      photo, NBA co-brand lockup.

**Practical relocation logistics (4-12)** — the "why Florida / how to move" half:
- p4  Florida vs. Other States (no state income tax, weather, cost of living)
- p5  Toll Roads (SunPass + a toll quick-reference table)
- p6  Counties (illustrated overview map)
- p7  Employment Opportunities / major employers  *(+ MATEK Mortgage ad)*
- p8  Employment + education *(Park Maitland School)*
- p9  K-12 Schools (broken out by county)
- p10 **Central Florida Moving Checklist** (8 / 6 / 4 / 2 weeks before -> moving day ->
      after; orange infographic layout)
- p11 Airports (MCO, "60M+ passengers a year")
- p12 DMV & Voting (license, vehicle registration, voter reg + "pro tips")

**Area-by-area tour (13-41)** — organized county -> neighborhood:
- p13 Southport Station ad (financial advisor)
- p14 Downtown Orlando illustrated orientation map
- p15 Downtown Orlando (history, high-rises)
- p16 Stadiums & Arenas
- p17 Lake Eola & Thornton Park
- p18 The Milk District
- p19 Ivanhoe Village / College Park
- p20 Art & Science Centers
- p21 CFBI Building Inspectors ad (full page)
- p22 Winter Park & Maitland
- p23 **West Orange County** divider (illustrated map)
- p24 Winter Garden
- p25 Windermere
- p26 **Central Orange County** divider (illustrated map)
- p27 Walt Disney World Resort
- p28 Dr. Phillips
- p29 MetroWest & Millenia
- p30 SeaWorld Orlando
- p31 **East Orange County** divider (illustrated map)
- p32 Lake Nona
- p33 **Osceola County** divider map (Celebration, Kissimmee, Poinciana)
- p34 St. Cloud
- p35 Celebration
- p36 **Lake County** divider map (Mount Dora, Clermont, etc.)
- p37 Minneola, Groveland & Montverde
- p38 **Seminole County** divider map (Sanford, Lake Mary, Oviedo)
- p39 Sanford, Apopka & Natural Springs
- p40 **Polk County** divider map (Davenport, Winter Haven, Lakeland)
- p41 Nearby Adventures (day trips: Gulf beaches, Space Coast, St. Augustine)

**Back (42-43)**
- p42 PARKS Title ad (title company)
- p43 Back cover: illustrated dusk-skyline + pozek.com

---

## The content model (the reusable engine)

Every neighborhood page runs the **same Q&A template**:
- Bold area name + one-line tagline (e.g. "Lakeside Living at its Finest")
- Short intro paragraph
- 2-4 colored Q&A subheads, reused across the book:
  - **"What is [area]'s history?"**
  - **"Where do people hang out?"**
  - **"How can I stay active?"**
  - **"What makes this area unique?"** / **"Are there any notable residents?"**
- A colored callout box: **"Why do locals love it here?"**
- 1-2 photos (usually one aerial + one lifestyle shot)

The book is cleanly split into a **logistics half** (taxes, tolls, schools, airports,
DMV, moving checklist, jobs, healthcare) and a **geography half** (county-by-county,
~20 neighborhoods).

---

## Imagery & design system

Two visual systems interwoven:
1. **Real photography** — aerial/drone shots of neighborhoods, lakes, downtown; landmark
   photos (Disney gate, SeaWorld globe, stadiums); nature/lifestyle (heron at sunset,
   Milk District murals); team + headshots.
2. **Custom flat-vector illustrated maps** — pastel, playful county maps dotted with icons
   (gators, cows, oranges, palms, flamingos, labeled highways). These are the **section
   dividers** and orientation maps. NOTE: these are hand-illustrated cartoon maps, not
   real street maps.

- **Palette:** bright, sunny — aqua/teal, coral/orange, sky blue, sunshine yellow, magenta
  accents. Friendly / tourism-brochure-meets-magazine, **not** a luxury look.
- **Type:** bold condensed sans for area titles; clean multi-column magazine body; colored
  caps for the Q&A subheads; pull quotes; spread-style page numbers ("26 moving to orlando 27").
- **Layout:** consistent per-neighborhood template (above). Full-bleed photo bands + tinted
  callout boxes.

---

## Monetization

The guide is **sponsor-funded**. Full-page advertiser slots are baked in:
- MATEK Mortgage (lender)
- CFBI (building inspector)
- PARKS Title (title company)
- Southport Station (financial advisor)
- Park Maitland School

So it doubles as a partner/referral revenue vehicle, not just a lead magnet.

---

## How the LV build compares (current state)

The Las Vegas version already built in this folder:
- `guide.html` — 16-page InDesign-equivalent built in HTML/CSS, rendered to PDF via
  headless Chrome, then sliced to PNGs with pdftoppm.
- `Rose-Homes-LV-Moving-to-Las-Vegas.pdf` — the finished 16-page guide.
- `index.html` — a Pozek-style flipbook web page (arrows, fullscreen lightbox, Download PDF).
- `pages/page-01..16.png` — flipbook images.
- `assets/img/` — AI-generated photo backgrounds (nano_banana) + a real OpenStreetMap-based
  valley map (`vegas-map.png`, built by `build_map.py`, brand-tinted).

**LV brand (differs from Pozek):** navy `#1C2333`, champagne gold `#C9A86E`, warm off-white
`#F7F5F0`; Playfair Display + Montserrat + Inter. Luxury, not sunny-tourism.

**LV 16-page order:** Cover · Note from Ryan · Why People Move Here · The Valley at a Glance ·
Cost of Living · Why Nevada Is Tax-Friendly · Weather & Outdoors · Summerlin ·
Henderson & Green Valley · Centennial Hills & Skye Canyon · More Areas (real map, compass) ·
Schools · Life in the Valley · Big League Las Vegas · Move-to-Vegas Checklist · Let's Connect.

### Gap vs. Pozek (what to add to reach ~40 pp depth)
- **Logistics pages Pozek has that LV is thin/missing on:** a dedicated DMV / vehicle
  registration / utilities page (LV has a lighter checklist), an Employers & Economy page,
  a Healthcare page, an Airport (Harry Reid) page. (LV already has a moving checklist.)
- **Neighborhood depth:** Pozek dedicates a full page per neighborhood using the Q&A
  template. LV currently groups communities. To match, expand each LV community
  (Summerlin, Henderson, Green Valley, Centennial Hills, Skye Canyon, Southern Highlands,
  Mountain's Edge, Inspirada, Lake Las Vegas, North Las Vegas, Boulder City, Downtown/Arts
  District, Spring Valley, The Lakes) into its own Q&A page.
- **Credibility flex:** Pozek = "Official team of the Orlando Magic." LV equivalent to
  develop: a Golden Knights / Aces / Raiders or community tie, Real Broker scale, or
  local production stats.
- **Optional monetization:** 3-5 LV advertiser slots (lender, title, inspector, insurance).

---

## How the recon was done (repeatable)

1. The page shell hid the guide behind a JS PDF viewer, so a plain fetch only returned
   "Loading guide...". Opened the live page in the in-app browser and read the **network
   requests** — that surfaced the real PDF URL (`...Pozek_Orlando_Guide-New_Update-R16.pdf`).
2. `curl` the PDF, then `pdfinfo` for specs, `pdftotext -layout` for the text/structure map,
   and `pdftoppm -r 42` + a PIL contact-sheet script to eyeball every page's imagery/layout.

Factual content figures (taxes, page counts, etc.) describe the source; do not reproduce its
copy verbatim — this file is a structural/design brief, not a copy of the guide.

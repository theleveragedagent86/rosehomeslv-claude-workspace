# Direction 3, Sunset Geometric. Design tokens.

Round three, directed. Direction 5's sunset palette, direction 1's page architecture, direction 5's
dissolving photo header. **The differentiator is type: no serif anywhere in the system.**

Every ratio below was computed in Python from sRGB relative luminance with
`(L1 + 0.05) / (L2 + 0.05)`, rounded to two decimals. Nothing here is asserted.
**54 pairs, zero FAIL, worst normal text 4.68, worst overall 3.63.**

Em-dashes in this file: zero.

---

## 1. Palette

### 1a. The sunset family, carried straight over from direction 5

| token | hex | role |
|---|---|---|
| `--sunset` | `#D24018` | the loud one. The refusal panel, numeral circles, running head chips, folios 19 and 21, the landing button, the accent line under every section headline. Carries white text at 4.68. |
| `--clay` | `#9E3A1F` | sunset at text weight. Every question subhead, the lead hit line, table row headers, the NOT FOUND token, the ribbon type, the map card label. This is the small-text workhorse. |
| `--coral` | `#E9714A` | secondary block. The Henderson chip and the homeowners insurance block. **Ink text only.** White on coral is 3.03 and is banned. |
| `--ochre` | `#EFA00B` | desert sun. The credibility band, every glyph square, the assessment note in the diagram. **Ink text only, and never a bare fill on paper.** |
| `--agave` | `#166A62` | the cool note that stops the page going all-orange. The Clark County chip, the beltway, the value prop 2 icon tile. Light text only. |
| `--agave-d` | `#0F4F49` | agave at text weight. The escrow bracket, every superscript source numeral, the Matured token, the 215 shield. |
| `--dusk` | `#4A2B52` | the deep block. Table header bands, the phone card, folio 20, the principal and interest block, the value prop 3 icon tile, the button focus ring. |

### 1b. Paper and ink

| token | hex | role |
|---|---|---|
| `--paper` | `#FBF6ED` | the guide paper. Full bleed on all three guide pages and on the cover panel. |
| `--cream` | `#FDF8F1` | brightest paper. The landing hero ground, reverse type on dusk and ink, and the refusal ribbon tag. |
| `--white` | `#FFFFFF` | reverse type on sunset, clay, agave and agave-d. The phone number pills. |
| `--ink` | `#2B1D23` | a warm plum black, never a neutral black. All body prose, the soft close strip, the wordmark and brokerage pills. |
| `--muted` | `#6B584E` | inline attributions, figure captions, folio notes, table captions, landing microcopy. |

### 1c. Tints and rules

| token | hex | role |
|---|---|---|
| `--tint-clay` | `#F3E6D6` | table zebra, the prepayment card, the checklist panel, value prop 3. |
| `--tint-coral` | `#FBE2D6` | the "any with none at all" card and value prop 1. |
| `--tint-agave` | `#DCEBE7` | the developer method card and value prop 2. |
| `--rule` | `#977C61` | warm brown hairline. The page foot rule, phone pill borders, landing dividers. 3.63 on paper. |
| `--rule-strong` | `#7C6349` | load-bearing outlines. Checkbox squares, every diagram block, the ochre and coral chip inset rules. 5.22 on paper. |

**There is no neutral gray anywhere in this system.** Every rule, every shadow tint and every muted
value is warm. That is a large part of why a palette with this much saturation still reads friendly.

### Colour rules that must not be broken

1. **White or cream type never sits on `--coral` or `--ochre`.** Both fail AA in reverse: 3.03 and 2.16.
2. **`--ochre` is never type on light paper** (2.01) and never a bare fill on paper either. Where an
   ochre or coral shape must sit on paper it carries a `--rule-strong` inset rule, which reads 5.22
   against the paper and does the boundary work the fill cannot.
3. **`--sunset` is never small text.** It computes 4.35 on paper and 4.43 on cream. It is allowed only
   at 18pt and up, or 14pt bold and up, where the AA threshold is 3.00. Small text uses `--clay`.
4. **`--clay`, `--agave` and `--muted` are grayscale twins** (91, 95 and 92). They may never be used
   to distinguish two things from each other. They belong to different components.
5. **The three tints are grayscale identical** (231, 232, 232). Same rule. Each tint card also opens
   with a coloured square glyph and a worded label, so meaning lives in the words.
6. **Nothing is encoded by colour alone.** The `NOT FOUND` token carries the literal words, a hollow
   square glyph and a clay left rule. The retired token carries the literal word Matured or Paid off,
   a **filled** square glyph and an agave-d left rule. Hollow versus filled survives a laser printer.

---

## 2. Computed WCAG contrast, every pair actually used

AA thresholds: 4.50 for normal text, 3.00 for text at 18pt or 14pt bold and up, 3.00 for non-text
graphics per WCAG 1.4.11.

| fg | bg | fg hex | bg hex | where | size and weight | needs | ratio | verdict |
|---|---|---|---|---|---|---|---|---|
| `--ink` | `--paper` | `#2B1D23` | `#FBF6ED` | body prose, numbered list, table cell on odd rows | 9.5pt / 400 | 4.5 | **14.97** | PASS |
| `--ink` | `--paper` | `#2B1D23` | `#FBF6ED` | answer line, the declarative line under every question subhead | 15pt / 700 | 4.5 | **14.97** | PASS |
| `--ink` | `--paper` | `#2B1D23` | `#FBF6ED` | section headline | 31pt / 800 | 3.0 | **14.97** | PASS |
| `--ink` | `--paper` | `#2B1D23` | `#FBF6ED` | pull line, Same master plan | 23pt / 800 | 3.0 | **14.97** | PASS |
| `--clay` | `--paper` | `#9E3A1F` | `#FBF6ED` | question subhead and opener eyebrow | 8.6pt / 800 caps | 4.5 | **6.34** | PASS |
| `--clay` | `--paper` | `#9E3A1F` | `#FBF6ED` | lead hit line, Often that somebody is you | 14.5pt / 700 | 4.5 | **6.34** | PASS |
| `--clay` | `--paper` | `#9E3A1F` | `#FBF6ED` | table row header and the NOT FOUND token | 8pt / 800, 5.9pt / 800 caps | 4.5 | **6.34** | PASS |
| `--sunset` | `--paper` | `#D24018` | `#FBF6ED` | opener accent line, LARGE TEXT ONLY | 19pt / 700 | 3.0 | **4.35** | PASS |
| `--sunset` | `--paper` | `#D24018` | `#FBF6ED` | pull accent and cover title accent, LARGE TEXT ONLY | 23pt and 36pt / 800 | 3.0 | **4.35** | PASS |
| `--agave-d` | `--paper` | `#0F4F49` | `#FBF6ED` | agave question subhead, superscript source numeral, escrow bracket label | 8.6pt caps, 6.2pt / 800 | 4.5 | **8.73** | PASS |
| `--muted` | `--paper` | `#6B584E` | `#FBF6ED` | inline attribution, figure caption, folio note, table caption | 6.6pt to 7.4pt / 600 | 4.5 | **6.23** | PASS |
| `--rule` | `--paper` | `#977C61` | `#FBF6ED` | foot rule, phone pill border | non text | 3.0 | **3.63** | PASS |
| `--rule-strong` | `--paper` | `#7C6349` | `#FBF6ED` | outline on every diagram block, checkbox squares, ochre and coral chip rules | non text | 3.0 | **5.22** | PASS |
| `--ink` | `--tint-clay` | `#2B1D23` | `#F3E6D6` | clay card body, checklist step, table cell on even rows | 8.2pt to 9.4pt / 400 | 4.5 | **13.13** | PASS |
| `--clay` | `--tint-clay` | `#9E3A1F` | `#F3E6D6` | table row header and NOT FOUND token on zebra rows | 8pt / 800 | 4.5 | **5.55** | PASS |
| `--agave-d` | `--tint-clay` | `#0F4F49` | `#F3E6D6` | superscript source numeral inside a clay card | 6.2pt / 800 | 4.5 | **7.65** | PASS |
| `--muted` | `--tint-clay` | `#6B584E` | `#F3E6D6` | attribution inside a clay card | 7.4pt / 600 | 4.5 | **5.46** | PASS |
| `--rule-strong` | `--tint-clay` | `#7C6349` | `#F3E6D6` | checkbox square outline | non text | 3.0 | **4.57** | PASS |
| `--ink` | `--tint-agave` | `#2B1D23` | `#DCEBE7` | developer method card body | 9.4pt / 400 | 4.5 | **13.11** | PASS |
| `--agave-d` | `--tint-agave` | `#0F4F49` | `#DCEBE7` | superscript inside the agave card | 6.2pt / 800 | 4.5 | **7.64** | PASS |
| `--ink` | `--tint-coral` | `#2B1D23` | `#FBE2D6` | no SID card body | 8.5pt / 400 | 4.5 | **13.01** | PASS |
| `--clay` | `--tint-coral` | `#9E3A1F` | `#FBE2D6` | no SID card subhead | 8.6pt / 800 caps | 4.5 | **5.51** | PASS |
| `--agave-d` | `--tint-coral` | `#0F4F49` | `#FBE2D6` | superscript inside the coral card | 6.2pt / 800 | 4.5 | **7.58** | PASS |
| `--white` | `--sunset` | `#FFFFFF` | `#D24018` | refusal body and headline, numeral circles, running head chip, folio 19 and 21 | 9.2pt / 400 and up | 4.5 | **4.68** | PASS |
| `--clay` | `--cream` | `#9E3A1F` | `#FDF8F1` | refusal ribbon type | 7.4pt / 800 caps | 4.5 | **6.45** | PASS |
| `--cream` | `--sunset` | `#FDF8F1` | `#D24018` | refusal ribbon tag against the refusal panel | non text | 3.0 | **4.43** | PASS |
| `--ink` | `--ochre` | `#2B1D23` | `#EFA00B` | credibility band, every ochre glyph square | 9.6pt / 800 | 4.5 | **7.45** | PASS |
| `--ink` | `--coral` | `#2B1D23` | `#E9714A` | Henderson chip, homeowners insurance block | 8.4pt / 800 caps | 4.5 | **5.32** | PASS |
| `--cream` | `--dusk` | `#FDF8F1` | `#4A2B52` | phone card body and heading, running head chip, principal and interest block | 8.2pt / 400 and up | 4.5 | **11.30** | PASS |
| `--ochre` | `--dusk` | `#EFA00B` | `#4A2B52` | ochre glyph square on the phone card | non text | 3.0 | **5.52** | PASS |
| `--white` | `--dusk` | `#FFFFFF` | `#4A2B52` | folio 20 | 15pt / 800 | 3.0 | **11.94** | PASS |
| `--cream` | `--ink` | `#FDF8F1` | `#2B1D23` | soft close body, brokerage pill, wordmark pill, special assessment block | 7.4pt to 9.2pt | 4.5 | **15.26** | PASS |
| `--ochre` | `--ink` | `#EFA00B` | `#2B1D23` | soft close emphasis, assessment note, sun and ridge mark | 8pt / 800 | 4.5 | **7.45** | PASS |
| `--agave` | `--paper` | `#166A62` | `#FBF6ED` | Clark County chip fill against the cover panel | non text | 3.0 | **5.96** | PASS |
| `--white` | `--agave` | `#FFFFFF` | `#166A62` | Clark County chip type, value prop 2 icon | 8.4pt / 800 caps | 4.5 | **6.42** | PASS |
| `--ink` | `--cream` | `#2B1D23` | `#FDF8F1` | hero headline, subhead, nav wordmark | 15px to 18px, 42pt display | 4.5 | **15.26** | PASS |
| `--sunset` | `--cream` | `#D24018` | `#FDF8F1` | hero headline accent phrase, LARGE TEXT ONLY | 42pt / 800 | 3.0 | **4.43** | PASS |
| `--muted` | `--cream` | `#6B584E` | `#FDF8F1` | microcopy and trust detail | 12.5px to 13px / 500 | 4.5 | **6.35** | PASS |
| `--clay` | `--cream` | `#9E3A1F` | `#FDF8F1` | map card label | 10px / 800 caps | 4.5 | **6.45** | PASS |
| `--white` | `--sunset` | `#FFFFFF` | `#D24018` | hero eyebrow chip and button label | 11px and 17px / 800 | 4.5 | **4.68** | PASS |
| `--ink` | `--tint-coral` | `#2B1D23` | `#FBE2D6` | value prop 1 card | 13px / 400 | 4.5 | **13.01** | PASS |
| `--ink` | `--tint-agave` | `#2B1D23` | `#DCEBE7` | value prop 2 card | 13px / 400 | 4.5 | **13.11** | PASS |
| `--ink` | `--tint-clay` | `#2B1D23` | `#F3E6D6` | value prop 3 card | 13px / 400 | 4.5 | **13.13** | PASS |
| `--rule` | `--cream` | `#977C61` | `#FDF8F1` | nav divider and trust divider | non text | 3.0 | **3.70** | PASS |
| `--dusk` | `--cream` | `#4A2B52` | `#FDF8F1` | button focus ring | non text | 3.0 | **11.30** | PASS |
| `--white` | `--agave-d` | `#FFFFFF` | `#0F4F49` | 215 shield in the valley map | 8px / 800 | 4.5 | **9.40** | PASS |
| `--white` | `--clay` | `#FFFFFF` | `#9E3A1F` | 15 shield in the valley map | 8px / 800 | 4.5 | **6.82** | PASS |
| `--dusk` | `--paper` | `#4A2B52` | `#FBF6ED` | Henderson chip in the valley map | 8px / 800 | 4.5 | **11.09** | PASS |
| `--ink` | `--paper` | `#2B1D23` | `#FBF6ED` | The Strip chip in the valley map | 8px / 800 | 4.5 | **14.97** | PASS |
| `--ink` | computed composite | `#2B1D23` | `#E9E4DC` | page 19 headline in the fade, worst case a BLACK photograph | 31pt / 800 | 3.0 | **12.74** | PASS |
| `--ink` | computed composite | `#2B1D23` | `#E9E4DC` | page 19 deck in the fade, worst case a BLACK photograph | 12pt / 500 | 4.5 | **12.74** | PASS |
| `--clay` | computed composite | `#9E3A1F` | `#E9E4DC` | page 19 eyebrow in the fade, worst case a BLACK photograph | 8.6pt / 800 caps | 4.5 | **5.39** | PASS |
| `--sunset` | computed composite | `#D24018` | `#E9E4DC` | page 19 accent line in the fade, worst case a BLACK photograph, LARGE ONLY | 19pt / 700 | 3.0 | **3.70** | PASS |
| `--cream` | computed composite | `#FDF8F1` | `#61534F` | landing photo caption, worst case a WHITE photograph under the lightest tone stop then the scrim | 12px / 800 caps | 4.5 | **6.95** | PASS |

**Result: 54 pairs, 0 FAIL.** The tightest normal-text pair in the whole system is white on
`--sunset` at **4.68**, which carries the refusal callout body, the numeral circles, the running head
chips, two folios, the landing eyebrow chip and the landing button label. The tightest pair of any
kind is `--rule` on `--paper` at **3.63**, a decorative hairline.

### How the two photographic composites were computed

Type over a photograph cannot be asserted, so both were computed against the worst photograph that
could sit underneath.

- **Page 19 header.** The opener is one alpha ramp, not a blend mode: dusk 0.42 at the top, clay 0.16
  at the middle, then paper stops rising to 1.0 at 90 percent. Type begins at 272px on a 320px block,
  which is 85 percent, where the paper stop interpolates to **0.9286**. The worst case underneath is a
  **pure black** photograph, so the composite is paper at 0.9286 over `#000000`, which resolves to
  `#E9E4DC`. Ink on that is 12.74, clay is 5.39, sunset is 3.70.
- **Landing photo caption.** The hero photo carries a three-stop multiply tone and a 0.74 ink scrim.
  The worst case is a **pure white** photograph under the *lightest* tone stop, ochre at 0.20, which
  multiplies to `#FCECCE`; the scrim then resolves the composite to `#61534F`. Cream on that is 6.95.

If either ramp is ever softened, recompute. The scrim was set at 0.74 rather than 0.62 because 0.62
computed to 5.09 and left no margin.

### Measured, considered, and rejected

| pair | ratio | verdict |
|---|---|---|
| `--ochre` on `--sunset` | 2.16 | rejected as the refusal ribbon. Replaced with a `--cream` tag at 4.43 carrying clay type at 6.45. |
| `--ochre` on `--paper` | 2.01 | rejected as a bare fill. Ochre shapes on paper carry a `--rule-strong` inset rule. |
| `--coral` on `--paper` | 2.82 | same rejection, same fix. |
| `--white` on `--coral` | 3.03 | rejected. Coral takes ink type only. |
| `--white` on `--ochre` | 2.16 | rejected. Ochre takes ink type only. |
| `--sunset` on `--paper` | 4.35 | rejected for any text under 18pt. Large display only. |
| `--cream` on `--sunset` | 4.43 | rejected as small text on the refusal panel. Body there is pure white at 4.68. |
| `--agave` on `--tint-agave` | 5.22 | passes, but rejected anyway. `--agave-d` at 7.64 is used instead so the superscripts hold at 6.2pt. |

---

## 3. Type

**One Google Fonts request:**

```html
<link href="https://fonts.googleapis.com/css2?family=Karla:wght@300..800&family=Syne:wght@400..800&display=swap" rel="stylesheet">
```

```css
--display: "Syne", "Trebuchet MS", "Helvetica Neue", sans-serif;
--text:    "Karla", "Helvetica Neue", Arial, sans-serif;
```

- **Syne, 700 and 800.** A geometric display face with genuinely odd bones: a flat-shouldered `a`, a
  wide `w`, a `g` that closes into an oval. Set at 21pt and up with tracking from -0.02em to -0.034em
  it reads as a screen-printed poster, not as a UI font. Nobody in Las Vegas real estate is using it.
- **Karla, 400 to 800.** A grotesque with slightly quirky proportions, a tall x-height and open
  apertures. It holds at 5.9pt inside a table token and still looks warm at 9.5pt in body prose.

**The split is semantic.** Syne says the thing. Karla explains the thing. A reader learns in one page
that anything set in Syne is a claim and anything set in Karla is the evidence for it.

**There is no serif and no italic in this system.** Syne ships no italic, so emphasis is carried by
weight, by caps, and by colour, never by slant. Where direction 5 would set an italic phrase in clay,
this direction sets a separate line in sunset at display size.

### Guide scale, points, print 1 to 1

| role | face | size / leading | tracking | notes |
|---|---|---|---|---|
| cover title | Syne 800 caps | 36 / 1.00 | -0.032em | accent phrase in `--sunset` |
| cover eyebrow | Karla 800 caps | 8.6 / 1.0 | 0.22em | |
| cover subtitle | Karla 400 | 12.4 / 1.45 | 0 | |
| cover byline name | Syne 700 | 21 / 1.0 | -0.02em | |
| credibility band | Karla 800 | 9.6 / 1.3 | 0.005em | on the ochre band that bleeds off the left edge |
| edition block | Karla 600 | 7.8 / 1.55 | 0 | label line 8pt / 800 caps in clay |
| compliance line | Karla 500 | 7.4 / 1.5 | 0 | |
| section headline | Syne 800 | 31 / 1.02 | -0.030em | sits in the photo fade |
| headline accent line | Syne 700 | 19 / 1.14 | -0.024em | `--sunset`, large text only |
| deck | Karla 500 | 12 / 1.45 | 0 | |
| question subhead | Karla 800 caps | 8.6 / 1.2 | 0.15em | preceded by an 8.5pt coloured square |
| answer line | Syne 700 | 15 / 1.14 | -0.02em | small variant 12.6 |
| lead hit line | Syne 700 | 14.5 / 1.16 | -0.022em | `--clay` |
| pull line | Syne 800 | 23 / 1.02 | -0.034em | accent phrase in `--sunset`, set full measure, never in a column |
| refusal headline | Syne 800 | 21 / 1.04 | -0.028em | reversed on the sunset panel |
| refusal ribbon | Karla 800 caps | 7.4 / 1.0 | 0.18em | clay on a cream tag |
| body prose | Karla 400 | 9.5 / 1.50 | 0 | the floor. Nothing in prose goes below it. |
| numbered list | Karla 400 | 9.5 / 1.45 | 0 | numeral 9.4 / 800 in a 16pt filled circle |
| card body | Karla 400 | 9.4 / 1.44 | 0 | 8.5 in the narrowest card |
| checklist step | Karla 400 | 8.2 / 1.36 | 0 | |
| callout and phone body | Karla 400 | 8.2 / 1.38 | 0 | |
| phone number | Syne 700 | 11.6 / 1.16 | -0.02em | tabular numerals |
| soft close | Karla 400 | 9.2 / 1.45 | 0 | emphasis in ochre 800 |
| table caption | Karla 700 | 6.6 / 1.28 | 0 | |
| table column head | Karla 800 caps | 6.2 / 1.0 | 0.05em | |
| table cell | Karla 400 | 8 / 1.2 | 0 | tabular numerals |
| table row head | Karla 800 | 8 / 1.2 | 0 | |
| status token | Karla 800 caps | 5.9 / 1.0 | 0.04em | |
| inline attribution | Karla 600 | 7.4 / 1.42 | 0.015em | |
| superscript source numeral | Karla 800 | 6.2 / 1.0 | 0.02em | `--agave-d` |
| running head chip | Karla 800 caps | 7.4 / 1.0 | 0.18em | |
| folio | Syne 800 | 15 / 1.0 | -0.02em | in a 0.48in by 0.40in tile |
| figure caption | Karla 600 | 7.2 / 1.38 | 0 | |
| diagram labels | Karla 800 | 8 to 10 | 0 to 1.2 | |

### Landing scale, px and container query units

| role | face | size |
|---|---|---|
| eyebrow chip | Karla 800 caps | 11, 0.16em |
| H1 | Syne 800 | `clamp(34px, 4.4cqw, 56px)` / 1.02, -0.032em |
| subhead | Karla 400 | `clamp(15px, 1.35cqw, 18px)` / 1.58, max 36em |
| value prop heading | Syne 700 | 15 / 1.25, -0.015em |
| value prop body | Karla 400 | 13 / 1.55 |
| button | Karla 800 | 17 |
| microcopy | Karla 600 | 13 |
| trust detail | Karla 500 | 12.5 / 1.6 |
| brokerage pill | Karla 800 caps | 10 to 11, 0.14em to 0.15em |
| map card label | Karla 800 caps | 10, 0.17em |

---

## 4. Spacing, geometry, shape

**Spacing scale, points, guide.** 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18. Nothing between.
**Spacing scale, px, landing.** 8, 10, 12, 13, 14, 16, 18, 19, 24, 26.

**Radii.** Roundness plus colour volume is what carries the warmth, since there is no serif to do it.

| token | value | used on |
|---|---|---|
| `--r-xs` | 3pt | table header corners |
| `--r-sm` | 6pt | phone number pills |
| `--r-md` | 10pt | every tinted card, the soft close strip |
| `--r-lg` | 16pt | the refusal panel |
| `--r-xl` | 26pt | the cover panel top corners |
| pill | 999px | every chip, every running head, every numeral circle, the landing button |

The only square corners in the whole direction are the four bands of the cover seam ribbon, the
folio tiles, and the small glyph squares in the question subheads. Everything else is round.

**Page geometry.** Trim 8.5in by 11in. Side margin `--pad` is 0.55in. Foot is 48px.

Every full-bleed edge is set in **whole CSS pixels, never inches**, because a fractional element
height makes Chrome antialias the boundary and leaves a visible hairline seam where the photograph
meets the page paper. That bug was hit here and fixed here.

| element | value | inches |
|---|---|---|
| cover photo | 536px | 5.583 |
| cover seam ribbon | 16px at `bottom:557px` | 0.167 |
| cover panel | 557px | 5.802 |
| page 19 opener photo | 320px | 3.333 |
| page 19 text block top | 272px | 2.833, which is 85 percent down the photo |
| running head band, pages 20 and 21 | 52px | 0.542 |
| page foot | 48px | 0.500 |

**Measured fit at build.** Measured over CDP after `document.fonts.ready` and after every image
resolved `decode()`, taking the lowest bottom edge of any leaf content element against the top of the
foot rule. The print column was measured a second time with `Emulation.setEmulatedMedia: print`, so it
is the real 10.96in box and not arithmetic.

| page | slack at 11in | slack at the 10.96in print box |
|---|---|---|
| cover | 34 | 34 |
| 19 | 58 | 54 |
| 20 | 55 | 51 |
| 21 | 41 | 37 |

Zero clipped elements on any page. Page 21 is now the tight one. Page 20 has the densest ink but the
most predictable height, because the refusal panel and the checklist panel are both fixed two-column
blocks that do not reflow.

**Shadow.** None on paper. On the landing panel only: the button carries a hard `0 6px 0 var(--clay)`
offset plus a clay-tinted drop, and cards carry `rgba(43,29,35,.20)`. No neutral gray shadow anywhere.

---

## 5. Print rules

```css
@page { size: letter; margin: 0; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
@media print { .page { height: 10.96in; } .stage { line-height: 0; } .rail { line-height: normal; } }
```

### The specificity rule, read this before adding a component

The base prose rule is `.gp p`, which is specificity **(0,1,1)** and uses the `font` shorthand. Any
paragraph component selected by a single class is **(0,1,0)**, loses to it, and gets its size, weight
and family silently reset to 9.5pt Karla 400. That is not a visible failure. It is a quiet flattening
of the entire display hierarchy, and the first build of this direction shipped with seven components
in that state: `.q`, `.hit`, `.attr`, `.pull`, `.op-eyebrow`, `.op-line` and `.op-deck`. The pull line
was authored at 23pt Syne 800 and was rendering at 9.5pt Karla 400.

**Every paragraph component in the guide is therefore scoped `.gp .name`, which is (0,2,0) and wins.**
Components that are not paragraphs (`.a` on an `h2`, `.figcap` on a `figcaption`, `.nlist .t` and
`.chk .t` on spans) are unaffected and are left at one class.

Do not trust the eye on this. The only reliable check is to read `getComputedStyle` for every
component and compare it against the type scale in section 3. That probe is what caught it.

- `break-inside: avoid` and `page-break-inside: avoid` on `.card`, `.refuse`, `.tbl-wrap`,
  `table.sid`, `.fig`, `.chk li`, `.nlist li`, `.close`, `.prop`.
- `thead { display: table-header-group }` on both halves of the paired district table, plus a fixed
  `table-layout` with an explicit `<colgroup>` so the two halves keep identical column widths.
- **No `position: fixed` anywhere in the file.** Verified by reading the parsed stylesheet: 0 matches.
- **No `position: absolute` inside any `li::before`.** Verified: 0 matches. Every bullet, numeral and
  checkbox is a flexbox row with a real `<span>` marker.
- 10.96in rather than 11in in print, because at exactly 11in Chrome pushes a sub-pixel sliver onto the
  next sheet and emits a blank page after every guide page. The preview rig's `line-height` is also
  zeroed in print for the same reason.
- Every `<img>` carries real alt text. Both inline SVGs carry `role="img"`, `<title>` and `<desc>`,
  and the diagram's `<desc>` describes the argument, not the shapes. Both tables carry `<caption>`,
  `<th scope="col">` and `<th scope="row">`.

### Grayscale, a home laser printer

| token | hex | luminance equivalent gray |
|---|---|---|
| `--cream` | `#FDF8F1` | 249 |
| `--paper` | `#FBF6ED` | 246 |
| `--tint-clay` | `#F3E6D6` | 232 |
| `--tint-agave` | `#DCEBE7` | 232 |
| `--tint-coral` | `#FBE2D6` | 231 |
| `--ochre` | `#EFA00B` | 176 |
| `--coral` | `#E9714A` | 148 |
| `--rule` | `#977C61` | 129 |
| `--sunset` | `#D24018` | 116 |
| `--rule-strong` | `#7C6349` | 103 |
| `--agave` | `#166A62` | 95 |
| `--muted` | `#6B584E` | 92 |
| `--clay` | `#9E3A1F` | 91 |
| `--dusk` | `#4A2B52` | 55 |
| `--ink` | `#2B1D23` | 33 |

**What survives.** The refusal panel at 116 against paper at 246 is still the loudest object on the
spread in monochrome, which is the whole point of the design. The dusk table header at 55 still reads
as a header band. Sunset at 116, coral at 148 and ochre at 176 are 30-plus levels apart, so the
payment diagram keeps five distinguishable layers with no hue at all, and every block additionally
carries a `--rule-strong` outline and its own worded label.

**What does not.** `--clay` at 91, `--muted` at 92 and `--agave` at 95 are within four levels of each
other and are not separable in monochrome. That is why they are never used to encode a difference: the
NOT FOUND token and the Matured token are told apart by a hollow square versus a filled square and by
their literal words, not by clay versus agave. The three tints all flatten to 231 or 232 and are
likewise never used in the same component.

### Ink

Naive GCR conversion, for a rough sense of coverage on a digital duplex run.

| token | hex | C | M | Y | K | total area coverage |
|---|---|---|---|---|---|---|
| `--cream` | `#FDF8F1` | 0 | 2 | 5 | 1 | 8% |
| `--paper` | `#FBF6ED` | 0 | 2 | 6 | 2 | 10% |
| `--tint-agave` | `#DCEBE7` | 6 | 0 | 2 | 8 | 16% |
| `--tint-clay` | `#F3E6D6` | 0 | 5 | 12 | 5 | 22% |
| `--tint-coral` | `#FBE2D6` | 0 | 10 | 15 | 2 | 27% |
| `--rule` | `#977C61` | 0 | 18 | 36 | 41 | 95% |
| `--muted` | `#6B584E` | 0 | 18 | 27 | 58 | 103% |
| `--rule-strong` | `#7C6349` | 0 | 20 | 41 | 51 | 112% |
| `--dusk` | `#4A2B52` | 10 | 48 | 0 | 68 | 126% |
| `--coral` | `#E9714A` | 0 | 52 | 68 | 9 | 129% |
| `--ochre` | `#EFA00B` | 0 | 33 | 95 | 6 | 134% |
| `--ink` | `#2B1D23` | 0 | 33 | 19 | 83 | 135% |
| `--agave` | `#166A62` | 79 | 0 | 8 | 58 | 145% |
| `--agave-d` | `#0F4F49` | 81 | 0 | 8 | 69 | 158% |
| `--sunset` | `#D24018` | 0 | 70 | 89 | 18 | 177% |
| `--clay` | `#9E3A1F` | 0 | 63 | 80 | 38 | 181% |

Nothing clears 190 percent, so no page risks set-off or slow drying on a digital duplex run.

**Honest coverage estimate.** This is the heaviest of the three panels I would ship. The paper flood
alone is about 10 percent across all 39 pages. Page 20 adds the refusal panel at roughly 22 percent of
the page area at 177 percent coverage, plus the diagram and the checklist panel, so call page 20
**28 to 32 percent** average coverage. Page 19 is lighter at **20 to 24 percent** because the top
third is a photograph. Page 21 lands around **24 percent**, most of it the table zebra.

**Economy override, one rule:**

```css
:root { --paper:#FFFFFF; --cream:#FFFFFF; --tint-clay:#FFFFFF; --tint-coral:#FFFFFF; --tint-agave:#FFFFFF; }
.card { border:1pt solid var(--rule-strong); }
```

That removes the paper flood and all three tint fills, which is roughly **40 percent of the toner**,
and every ratio in the table above still passes because white is lighter than paper in every pair.
The cards keep their identity through the rule and their coloured glyph square. The refusal panel and
the photography are deliberately left alone: they are the two things a reader remembers.

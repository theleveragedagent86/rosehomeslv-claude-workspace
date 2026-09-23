# Design decision

**Chosen: `direction-3-geometric-orange-dialed-back` (round 6).** Ryan, 2026-07-28.

Reference render: [design/direction-3-geometric-orange-dialed-back/preview.html](direction-3-geometric-orange-dialed-back/preview.html).
That file is the visual contract. Where this document and the render disagree, the render wins,
and this document gets corrected.

## What the choice actually is

Six rounds narrowed one variable at a time. The winner is the accumulation of every step:

| Element | Comes from | Settled in |
|---|---|---|
| Page architecture | round 3 `direction-3-sunset-geometric` | round 5 |
| Palette family | round 3 `direction-6-navy-sunset`, lifted brand navy plus sunset | round 3 |
| Typefaces | Bodoni Moda display, Archivo text | round 4 |
| Cover title treatment | mixed case at 46pt, not the original caps at 36pt | round 6 |
| Orange level | dialed back, structure navy, orange kept only where it means something | round 6 |
| Card tint | one tint, `#FBEFD3` | round 6 |

## The path here, for anyone reading this later

1. **Analytical.** Rejected. "Too analytical and robotic." The brief was wrong, not the craft.
2. **Warm, Pozek-inspired.** Ryan picked pieces rather than a whole.
3. **Directed.** Those pieces plus brand-navy variants. Verdict: this layout, that palette, that type.
4. **Type.** One layout, five typeface pairings. Verdict: Bodoni Moda and Archivo.
5. **Layout.** One pairing, both layouts. Verdict: too much orange in both.
6. **Less orange.** Both layouts at two strengths. Verdict: geometric, dialed back.

## What is now frozen

Everything in [../build/design-system.md](../build/design-system.md). Chapter writers may use only
the classes listed there. No writer invents a class, a color, or a type size.

## What is explicitly not frozen

- **Photography.** The preview borrows four images from the relocation guide at 896x1200, roughly
  105 dpi at full-bleed Letter. Soft in print. The shipping guide needs art regenerated at 4k.
- **The cost diagram's rungs.** Navy, coral, ochre and cream in a descending ramp. The ramp carries
  meaning and is not part of the one-card-tint rule.
- **Page budget.** SID and LID takes three pages, not two. Confirmed across rounds 2, 3 and 6.

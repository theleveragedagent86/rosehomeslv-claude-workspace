# Literata and DM Sans

> Sturdier and squarer than Spectral. Reads solid rather than elegant.

## Why this pairing

Literata was drawn for the Google Play book reader, so it is a serif engineered for sustained reading rather than for a masthead. Slab-ish serifs give the headlines more physical weight. DM Sans is geometric and neutral underneath it.

## What changed from round 3

Nothing except the two typefaces and the tracking and weight adjustments they need.
Same copy, same page architecture, same page budget, same contrast pairs. If one of
these reads better than another, the difference is typography and nothing else.

## Tracking

The base file tracks display type tight, between -.018em and -.034em, which suits the
heavy grotesque it was drawn for. A serif at 54pt does not want that. Every display
selector here is `calc(base + .018em)`, so the relative hierarchy the base
established survives while the absolute tracking loosens to what this face wants.

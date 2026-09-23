# Source Serif 4 and Public Sans

> The plainest option. Nothing about the type asks for attention.

## Why this pairing

Source Serif 4 and Public Sans are both open source faces designed for documents people have to trust, and Public Sans is literally the US federal design system face. If the guide should read as a public record rather than as marketing, this is the pairing that does it.

## What changed from round 3

Nothing except the two typefaces and the tracking and weight adjustments they need.
Same copy, same page architecture, same page budget, same contrast pairs. If one of
these reads better than another, the difference is typography and nothing else.

## Tracking

The base file tracks display type tight, between -.018em and -.034em, which suits the
heavy grotesque it was drawn for. A serif at 54pt does not want that. Every display
selector here is `calc(base + .018em)`, so the relative hierarchy the base
established survives while the absolute tracking loosens to what this face wants.

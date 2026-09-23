# Tokens, Newsreader and Figtree

Layout and palette are inherited from direction 6 of round 3, unchanged. The only tokens this variant
sets are the two typefaces and the tracking delta that makes them sit correctly at
display size.

| Token | Value |
|---|---|
| `--display` | Newsreader |
| `--text` | Figtree |
| `--dtrack` | .014em, added to every display tracking value |
| display weight, large | 700 |
| display weight, medium | 600 |

## Palette, identical across round 4

| Token | Hex | Role |
|---|---|---|
| `--paper` | #F7F5F0 | the ground everywhere |
| `--paper-2` | #EDE9E0 | second surface, table zebra |
| `--ink` | #1C2436 | navy black, all body text |
| `--muted` | #5F5A52 | warm gray, attributions |
| `--navy-500` | #375498 | the spotlight peak |
| `--navy-700` | #2C3F6B | base of the lit panel |
| `--navy-950` | #141A27 | deep edge |
| `--sunset` | #D24018 | saturated fill, never text on paper |
| `--sunset-d` | #B8360F | text weight sunset, 5.39 on paper |
| `--ochre` | #EFA00B | fill only, carries ink at 7.16 |
| `--gold` | #D8BB84 | lifted gold, text only on navy-900 and darker |

Contrast pairs were computed in round 3 against `--navy-500`, the lightest point of the
spotlight, which is the worst case. Changing the typeface does not change any of them.

# CLAUDE.md — _Rebel Hockey

Ryan's son's youth ice hockey team. **Ryan is a coach**, not a vendor. This is personal, not a
business: none of the Rose Homes LV brand rules, contact blocks, or CTA conventions apply here.
Audience is team parents and 8-year-olds.

## The team

| | |
|---|---|
| **Name** | Rebels |
| **Division** | 8U Mite League |
| **Kit** | Head-to-toe **red**, and the jersey is **blank** — no chest letter, number, or crest |
| **Rink** | City National Arena, Summerlin (the schedule's "CNA Surface" column) |
| **Surfaces used** | Ghost Energy Rink B, Summerlin Hosp. Rink A |
| **Coaches** | Ryan Rose, Kane Osmars |
| **Ice share** | The Rebels' slot always lists **Rebels / Oil Kings** vs **IceDogs / Hitmen**. On game days the Rebels play all three of the other teams sharing the sheet. |

Any mascot or player artwork must match the real kit: solid red jersey with **nothing on the
chest**, red gloves, red pants, red socks, black skates.

## Chosen marks (locked Aug 2026)

Both live in `Logos/FINAL/`. Everything else under `Logos/` is a rejected or alternate concept.

- **Patches / primary crest** → `patch-crest-roundel.svg` (+ `.png`). The circular
  "REBELS HOCKEY / LAS VEGAS" roundel. Vector, so it scales to embroidery.
  **Its outer ring is black** — on a dark background it needs a light keyline and a red glow
  or it disappears. See the `.crest` rule in `Team Graphics/schedule.html`.
- **Shirt logos / secondary** → `shirt-mascot-skating.png` (4K) and
  `shirt-mascot-skating-1200.png` (web-size copy the poster uses). Frontier scout in a red
  jersey, skating. Raster only; a shop can digitize from the 4K file.

## Trademark guardrail

The scout/frontiersman concepts were inspired by UNLV's Rebels but are **original artwork**, not
copies of UNLV's marks. UNLV retired its *Hey Reb!* mascot in 2020 over its Confederate-era
origins (the school's first mascot was a Confederate wolf named Beauregard); the Rebels name was
kept. Do not trace UNLV artwork, do not put "UNLV" on anything, and keep all Rebels art clear of
Confederate imagery.

## Privacy

`Roster & Schedule Source/8U Rebels.xlsx` holds **kids' names, jersey numbers, dates of birth,
and parent emails and phone numbers.** Coach names alone are fine; Ryan's cell is deliberately off
the posters.

The roster poster carries **name, jersey number, and position only** — no DOB, no email, no phone,
no jersey size. That is the line: fine inside a team group chat, and it stays fine if a parent
forwards it. **Never add a contact column.** If a roster ever needs to go somewhere public
(a website, a league page, social), cut it back to first name and last initial first.

## Rebuilding a poster

Everything in `Team Graphics/` shares one design system: same tokens, same 1080x1920 frame, same
header (roundel + season line + big Anton word + year rule + stat strip), same row cards, same
footer (mascot + rink + coaches + note). **To add a new poster, copy the closest existing one and
swap the rows** — do not invent a second visual language.

The red accent means "the thing that stands out": game rows on the schedule, the goalie on the
roster. Keep exactly one such meaning per poster.

```bash
cd "/Users/ryanrose/Downloads/Claude/_Rebel Hockey" && python3 -m http.server 8135
```

Then, in a second shell:

```bash
cd "/Users/ryanrose/Downloads/Claude/_Rebel Hockey" && "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 --window-size=1080,1920 --virtual-time-budget=9000 --screenshot="Team Graphics/Rebels-8U-August-2026-schedule.png" "http://localhost:8135/Team%20Graphics/schedule.html"
```

Output is 2160x3840 (1080x1920 at 2x), sized for texting to parents.

**Gotchas, all learned the hard way:**

- The poster is tuned to land at **exactly 1920px tall**. Any change to type size, padding, or
  the number of rows requires re-measuring total height and re-trimming. To measure, drop a
  throwaway `measure.html` in the served root that iframes the poster, waits on
  `document.fonts.ready`, and prints section heights, then read it with Chrome's `--dump-dom`.
- Mascot cutouts get a white keyline via a **CSS drop-shadow chain**. Keep it to roughly
  **13 passes or fewer** and point it at a **downscaled (~1200-1500px) PNG**, not a 4K one.
  More passes or bigger bitmaps push a single headless render past five minutes. One page per
  Chrome invocation.
- **`timeout` does not exist on macOS.** It exits 127 and the command silently never runs, so
  you end up reviewing a stale render. Use the Bash tool's own timeout.
- The Higgsfield background remover **deletes detached elements**, not just background. It ate
  the "LAS VEGAS 8U" subtext under one wordmark. Keep the white-background original whenever
  the art has text or a banner floating clear of the main subject.
- Recraft vector output arrives as SVG with a full-canvas white `<rect>` as the first path and a
  `0 0 2048 2048` viewBox. Strip that rect and crop the viewBox to the real bounds (get them
  from `svg.getBBox()` in a headless page) or the logo renders tiny inside a big empty square.
  The `-t.svg` files in the concept folders are already stripped and cropped.

## Emailing the parents

**The Gmail MCP cannot create drafts with attachments.** The schema exposes an `attachments`
field, but the call fails and the tool's own description confirms it is unsupported. Separately,
the poster PNGs are 3+ MB each, which is far past what can be base64'd through a tool call
anyway. So the workflow is: create the draft with body and recipients programmatically, then
Ryan drags the files in from `Email Attachments/` before sending. Keep all four staged there so
it is one multi-select drag.

Recipient list comes from the roster xlsx. Exclude Ryan's own address and `soaresn43@gmail.com`
(listed beside Ryan's name in the league sheet's coach block but unattributed, possibly a league
typo). `hcannata8@aol.com` covers both Adams brothers, so seven addresses cover nine players.

The season-opening email follows the template Ryan wrote for the Ice Wolves: welcome, who the
coaches are with their kid named in parens, team color, first practice block, attachments,
a light line about development and winning, and the after-game snack ask.

## August 2026 schedule (as rendered)

3 games, 4 practices. Games are the red rows.

| Date | Time | Surface | Type |
|---|---|---|---|
| Sun Aug 9 | 10:00–10:50 AM | Ghost Energy B | Practice |
| Tue Aug 11 | 5:30–6:20 PM | Ghost Energy B | Practice |
| Sun Aug 16 | 9:40–10:30 AM | Ghost Energy B | **Game** |
| Tue Aug 18 | 5:10–6:00 PM | Ghost Energy B | Practice |
| Sun Aug 23 | 2:20–3:10 PM | Ghost Energy B | **Game** |
| Tue Aug 25 | 5:10–6:00 PM | Ghost Energy B | Practice |
| Sun Aug 30 | 4:20–5:10 PM | Summerlin Hosp. A | **Game** |

Source is `Roster & Schedule Source/8U August Schedule.xlsx`, which stores dates as Excel serials
and times as day fractions. The Rebels are always the **first slot of each day**.

## Sept–Dec 2026 schedule (as rendered)

Source is `Roster & Schedule Source/8U First Half Season Schedule.pdf` (league-wide, all four
teams, Aug 16 – Dec 29). Columns are Date | Day | Start | End | Arena | Home Team | Away Team.
**Read the Rebels off the team columns, not the row position** — unlike the August sheet, the
Rebels' slot is not always first once September starts. Their line always reads Home
`IceDogs / Hitmen` vs Away `Rebels / Oil Kings`. Filtering on that gives 29 sessions:
11 games, 17 practices, 1 Holiday Skate.

Everything is Ghost Energy Rink B unless noted.

| Date | Time | Type |
|---|---|---|
| Tue Sep 1 | 6:10–7:00 PM | Practice |
| Sun Sep 13 | 2:30–3:20 PM **(Summerlin Hosp. A)** | **Game** |
| Tue Sep 15 | 6:10–7:00 PM | Practice |
| Sun Sep 20 | 2:40–3:30 PM | **Game** |
| Tue Sep 22 | 6:10–7:00 PM | Practice |
| Sun Sep 27 | 5:00–5:50 PM | **Game** |
| Sun Oct 4 | 3:40–4:30 PM | **Game** |
| Tue Oct 6 | 7:10–8:00 PM | Practice |
| Tue Oct 13 | 7:10–8:00 PM | Practice |
| **Fri Oct 16** | 7:00–7:50 PM **(America First Center, Rink 2)** | **Game** |
| Tue Oct 20 | 7:10–8:00 PM | Practice |
| Sun Oct 25 | 6:00–6:50 PM | **Game** |
| Tue Oct 27 | 5:10–6:00 PM | Practice |
| Tue Nov 3 | 5:20–6:10 PM | Practice |
| Tue Nov 17 | 5:10–6:00 PM | Practice |
| **Fri Nov 20** | 5:40–6:30 PM **(Summerlin Hosp. A)** | **Game** |
| Tue Nov 24 | 6:10–7:00 PM | Practice |
| Tue Dec 1 | 6:10–7:00 PM | Practice |
| Tue Dec 8 | 6:10–7:00 PM | Practice |
| Tue Dec 15 | 6:10–7:00 PM | Practice |
| Sun Dec 20 | 4:10–5:00 PM | **Game** |
| Mon Dec 21 | 3:00–4:30 PM | Holiday Skate |
| Sat Dec 26 | 1:40–2:30 PM | Practice |
| Tue Dec 29 | 7:10–8:00 PM | Practice |

**Two dates were moved by the league after this table was first built** (Adam Miller, CNA
Hockey Director, emails of Aug 26 and Sep 10 2026). Sunday Oct 18 became **Friday Oct 16 at
America First Center in Henderson, Rink 2, 7:00 PM** because of an NHL event; Sunday Nov 22
became **Friday Nov 20 at CNA Rink A, 5:40 PM**. Oct 16 is the only session of the season not
at City National Arena, so the footer's flat "City National Arena" line needs a caveat on any
poster that covers it. Both are already corrected in `season.html` and `stats.html`.

Irregularities worth keeping in the footnotes: no ice Sept 6/8; October practices sit at 7:10 PM
through Oct 20 then drop back to 5:10; November is light (no ice Nov 8, 10, 15, or 29); Dec 21 is
a Monday Holiday Skate running 90 minutes instead of the usual 50, and Dec 26 is a Saturday.

**The Holiday Skate gets an icy blue, not red.** Red stays reserved for "game" so each poster keeps
exactly one red meaning. See `.row.holiday` / `.badge.hol` in `schedule-december.html`.

**Row count varies by month (4 in Nov, 7 in Oct and Dec), so the monthly posters add**
`main{ justify-content:center; gap:Npx }` **and** `.row{ flex:1 1 auto; max-height:196px }`. Rows
share the leftover space so every month fills the same 1920 frame, and the cap stops a light month
turning into four huge slabs. The gap is **8px at 7+ rows, 12px otherwise** — at 12px, October's
three game rows (each carrying the extra `vs` line) pushed the poster to 1939.

## Concept-number mapping

The contact sheets number concepts **continuously across all four sets** (01-06 set A, 07-11
set B, 12-17 set C, 18-22 set D), but filenames kept their original generation-batch index. So
"#3 Roundel" is the file `05-roundel-*`, and "#15 In Jersey" is `23-skating-*`. If Ryan refers to
a concept by number, read it off the contact sheet, not the filename.

---

## Folder Map — keep this current

```
_Rebel Hockey/
├── CLAUDE.md                        # this file
├── Roster & Schedule Source/        # league source files (the roster .xlsx has PII)
│                                    #   8U Rebels.xlsx, 8U August Schedule.xlsx,
│                                    #   8U First Half Season Schedule.pdf (Aug 16 – Dec 29)
├── Email Attachments/               # the 4 parent-email files in one place, for drag-and-drop
├── Logos/
│   ├── FINAL/                       # the two chosen marks — use these
│   ├── Concepts - Set A (Red Black White)/    # 6 concepts, incl. the roundel
│   ├── Concepts - Set B (Scarlet Gray)/       # 5 UNLV-flavored concepts
│   ├── Concepts - Set C (Frontier Scout)/     # 6 cartoon-scout concepts, incl. the shirt mascot
│   └── Concepts - Set D (Wordmark Lockups)/   # mascot in front of a REBELS block wordmark
└── Team Graphics/                   # every parent-facing poster, one design system
    ├── schedule.html                          # August source, 1080x1920
    ├── Rebels-8U-August-2026-schedule.png     # export, 2160x3840
    ├── schedule-september.html                # Sept–Dec sources, all 1080x1920,
    ├── schedule-october.html                  #   derived from schedule.html
    ├── schedule-november.html
    ├── schedule-december.html
    ├── Rebels-8U-September-2026-schedule.png  # exports, 2160x3840
    ├── Rebels-8U-October-2026-schedule.png
    ├── Rebels-8U-November-2026-schedule.png
    ├── Rebels-8U-December-2026-schedule.png
    ├── season.html                            # whole first half on one sheet, two
    │                                          #   columns, 1080x2332 (not the 1920 frame)
    ├── Rebels-8U-First-Half-Season-2026-schedule.png   # export, 2160x4664
    ├── roster.html                            # source, 1080x1920
    ├── Rebels-8U-2026-roster.png              # export, 2160x3840
    └── stats.html                             # parent-facing box score / season stats
                                               #   page, responsive (not a poster)
```

`stats.html` is the one file here that is **not** a poster. It is a responsive web page for
parents, styled on the ESPN NHL box score table using the same type stack. It is **published at
https://www.rosehomeslv.com/8u-rebels-stats** through the Lofty CMS landing-page builder, so it
runs a **light theme on white** (Lofty's page wrapper forces a white ground and the old dark
palette broke); display text uses a black-to-grey `background-clip:text` fade instead of the
posters' white-to-silver one. Season totals sit up top as the main view; below them one
`<details>` per game date, **all collapsed by default**, opens to that session's per-game box
scores. **All 11 game days of the first half, Aug 16 through Dec 20, are already listed**, pulled
from the same First Half Season Schedule that feeds `season.html`; the ones not yet played open to
"Not yet played". When a game day is played, replace that block's `.tbd` div with a `.day-body`
of game tables and update the season totals above. Skaters carry
G / A / PTS / TOI; Ari (#5) is the goalie and carries GA / GAA / GF / GFA instead. TOI is the session's
ice split evenly among the skaters who dressed that day, so it is 7:00 per game with eight skaters
and 8:00 with seven. A kid who misses a day does not get his GP or TOI bumped, and the kids who
did play absorb the missing minutes. Games are 14:00 (two lines of four splitting the ice), and Ari plays all of it, so his TOI is 14:00 per game he dresses for and 0 for a game he misses. Stats come off the whiteboard
photos Ryan shoots after each game (the board is wiped between games, so each photo is one game,
not a running total). The crest is hotlinked from a public assets repo,
`https://raw.githubusercontent.com/theleveragedagent86/rebels-8u-assets/main/crest.png`, because a
relative `../Logos/FINAL/` path 404s once the HTML is pasted into Lofty. That absolute URL means
`file:///` now works, but the `rebel-hockey` launch config on port 8135 is still the cleaner
preview. Names are first name + jersey number only, same privacy line as the roster poster, and
that line matters more here because the page is genuinely public.

`season.html` is the one poster off the 1080x1920 frame: 29 sessions will not fit, so it runs
1080x2332 in two columns with October straddling the break. It uses the same tokens and the same
header/footer, with denser rows and a `.where` line in **gold** on the two Summerlin Hospital
dates. Render it with `--window-size=1080,2332`.

Each `Concepts - *` folder keeps its own `contact-sheet.html` / `.png` comparison board plus the
source art and `-transparent.png` cutouts. Set D also has `lockup.html`, which composites a
mascot over an SVG wordmark and is driven by query params: `?m=<file>&h=<px>&dx=&dy=`.

**Maintenance rule:** When you add, remove, move, or rename anything here, update this map **and**
the Folder Map in the root [CLAUDE.md](../CLAUDE.md) in the same change. If you rename anything in
`Logos/FINAL/`, update the `src` paths in **every** file in `Team Graphics/` — they all reference
`../Logos/FINAL/`. Never leave a Folder Map stale.

# CLAUDE.md, Claude Code Course for Realtors

## What this folder is

**Ryan's flagship course build for The Leveraged Agent.** A single Skool classroom course tile containing a Level 0 through Level 10 ladder, plus three short bonus drops.

This is **Ryan's own product**. It is not the Jack Roberts archive. The archive at [`../Jack Roberts AI Course/`](../Jack%20Roberts%20AI%20Course/) was used for structure and sequencing only. None of Jack's copy, scripts, prompts or slides appear here, and none should.

## The design decisions, already made, do not re-litigate

| Decision | Answer |
|---|---|
| How many classroom tiles | **One.** Everything lives in this single course. Not ten modules. |
| Structure | **Level 0 to Level 10**, plus bonus drops outside the numbering |
| Carried artifact | **The Business Brain folder.** Every level adds a layer to the same folder. |
| Primary tool | **Claude Code**, throughout, no browser-Claude fallback path |
| Where Cowork appears | Bonus drop B1 only, for scheduled routines and browser work |
| Jack's "website" level becomes | **Landing Pages** |
| Named CLAUDE.md framework | **BROKER**: Business, Range, Output, Keep out, Escalation, Results |

Ryan confirmed all of these on 2026-08-24.

## Files

| File | What it is |
|---|---|
| [COURSE-MAP.md](COURSE-MAP.md) | one-page index of every level, runtime and artifact. **Start here.** |
| [COURSE-ARCHITECTURE.md](COURSE-ARCHITECTURE.md) | the ladder, why the order works, what it replaces, runtime discipline |
| [LESSON-TEMPLATE.md](LESSON-TEMPLATE.md) | the 9-block Skool description template with rules per block |
| [DELIVERY-PLAYBOOK.md](DELIVERY-PLAYBOOK.md) | the on-camera template: opening beats, ritual, teaching loop, close |
| `<NN>-Level-N-<Name>/README.md` | per level: the paste-ready Skool description, then production notes |
| `<NN>-Level-N-<Name>/SCRIPT.md` | the word-for-word teleprompter read, with deck cues and Claude Code demo cues. Levels 0 and 1 only so far |
| [deck/](deck/) | the localhost scrolling decks Ryan presents from while recording |
| [YouTube/](YouTube/) | the cut-down YouTube versions of the levels. Different audience, different script |
| [Instagram/](Instagram/) | Reels scripts and captions, 12 per level, plus the carousel build-drops. Top of the funnel, feeds the YouTube cuts |

## How a lesson README is laid out

Two halves, separated by a rule:

1. **Skool description (paste-ready)**, copy this straight into the Skool lesson. Follows the 9-block template exactly.
2. **Production notes (not for Skool)**, what to say on camera, where the win goes, what to leave in the cut, the exact closing line into the next level.

Never paste the production notes into Skool.

## The recording deck

Levels 0 and 1 each have a **teleprompter script** (`SCRIPT.md`) and a matching **scrolling deck** served from localhost. Ryan reads the script, advances the deck, and cuts to a live Claude Code window when the script says to.

Serve the workspace first, then open the deck:

```bash
ruby "/Users/ryanrose/Downloads/Claude/serve.rb"
```

- Level 0: `http://localhost:8091/SKOOL%20Community/Claude%20Code%20Course%20for%20Realtors/deck/level-0.html`
- Standalone voice video: `http://localhost:8091/SKOOL%20Community/Claude%20Code%20Course%20for%20Realtors/deck/voice.html`
- Level 1: `http://localhost:8091/SKOOL%20Community/Claude%20Code%20Course%20for%20Realtors/deck/level-1.html`
- YouTube Level 0: `http://localhost:8091/SKOOL%20Community/Claude%20Code%20Course%20for%20Realtors/deck/yt-level-0.html`

**How they line up.** Every script carries three cue markers, all set off by heavy rules. `━━━ DECK · N ━━━` means advance to that slide number. `━━━ ▶ CLAUDE CODE ━━━` means stop presenting and switch to the live window. `━━━ ◀ BACK TO DECK · N ━━━` means come back. Level 0 has 8 slides and no demos. Level 1 has 19 slides and 6 demos, cued after slides 4, 7, 10, 12, 13 and 14.

**The YouTube cuts use the same cue system and their own decks.** `deck/yt-level-0.html` is 13 slides and belongs to `YouTube/YT-Level-0-Context-Block.md`. It is a **different deck from `level-0.html`**, not a trimmed one: the Skool deck's spine is the L1 to L10 ladder, which a cold viewer has no use for. Its switch marker is `━━━ ▶ AI CHAT ━━━`, since that video has no Claude Code in it at all. Two things about it that are deliberate and easy to undo by accident: **slide 1 carries no `.hint`**, because unlike a Skool deck it is on screen at 0:00 of the recording and a "scroll or press space" nudge would ship into the video, same leak category as a director cue; and **the two listing descriptions on slides 1 and 9 are placeholder copy about an invented house**, to be replaced with real output from one of Ryan's own listings before shooting.

Its closing slide also carries a new `.endsafe` class from `deck.css`, which pushes that slide's content past x 940 so the 20 second ending overlay's wordmark panel does not land on the headline if Ryan cuts back to the deck instead of staying on camera. Only a YouTube deck's final slide should ever get it. There is no overlay on a Skool lesson, so it does not belong there.

**Director cues live in `SCRIPT.md` and never on a slide.** Level 1's deck used to carry six on-screen "switch to Claude Code" banners. Ryan had them removed on 2026-08-25: the deck is what the student sees, and a stage direction on it is a leak. `deck.css` now has `.cue{ display:none !important; }` as a standing guard, so if a cue block is ever pasted into a deck again it stays invisible instead of shipping into a recording. Do not restyle it back into something visible.

**Driving it.** Arrow keys, space, PageUp/PageDown, j/k, Home and End all move one slide. `?s=7` opens straight on slide 7, which is how you pick up a re-shoot. The HUD top right shows level and position, the bar across the top is progress.

**The palette is Vector v2.0, inverted side.** True black `#000000` ground, white ink, `#9AA3BC` secondary, and `#5B9BFF` for the accent as text or hairline, which is the canonical value the brand specifies for accent on black. Fills use `#1768E5`. This is night mode by way of the brand's own inverted surface, not a separate dark theme. Three values are derived rather than canonical, because the brand defines only true black for the inverted surface and a deck needs cards to lift off the ground: `--bg-2` `#080D22`, `--bg-sunk` `#04061A`, `--line` `#1C2647`. All three are the ink navy `#050E3D` pulled down in value, so no new hue enters the system. If the brand palette ever moves, edit the `:root` block in `deck.css` and nothing else.

**Two things to leave alone in the deck code.** `deck.css` deliberately has no `scroll-behavior:smooth`. Inside a `scroll-snap-type:mandatory` container that makes every programmatic scroll animate, the snap engine cancels the animation, and the arrow keys silently stop working. The smooth scroll is animated from `deck.js` instead. Separately, slides are `height:100vh` and `deck.js` zooms any slide whose content would overflow, so nothing is ever cut off the bottom at whatever size Ryan records at. Verified at 1920x1080 and 1440x900.

## YouTube is a different product

[YouTube/](YouTube/) holds the funnel versions of these levels. **They are not the same scripts and must not be treated as the same scripts.** Skool teaches a system to someone who already joined. YouTube has to earn a stranger's attention, land one complete win, and make the connected version the thing they want next.

Rules that hold across every YouTube cut:

- **Open cold on a finished result**, never on a course map. Level 0's Skool script is unusable on YouTube as written: it references levels, the community and "what you signed up for," none of which mean anything to a cold viewer. It was rebuilt on 2026-08-25 rather than cut down. The YouTube version keeps Level 0's **job**, the diagnosis that AI writes generically because you never told it who you are, throws away the ladder, and lands a Context Block the viewer pastes into whatever AI they already have. No install, which makes it the cheapest entry point in the funnel.
- **The two free videos must not teach the same thing.** Level 0's video teaches a 4-part paste block. **BROKER belongs to Level 1's video** and is not named in Level 0's. The paste block dies when the tab closes, and that is the honest reason to go build the folder.
- **8 to 14 minutes.** Under 6 reads as a teaser and does not buy enough authority for someone to join a paid community.
- **One complete artifact per video**, genuinely working on its own. What stays paid is the connected folder, not a crippled free version. Say that out loud rather than gating something arbitrary.
- **One soft mention mid-video**, at the goodwill peak right after the first win, and the real ask only after the payoff lands.
- **The 3 second bumper goes after the hook, not at 0:00.** The subscribe ask is a **transparent overlay** that rides over the recorded footage: a 6 second mid-roll cut, silent, when the first win lands, and a 20 second ending cut that adds the wordmark and runs to the end. **There is no full-frame end card**, it was deleted. The last 20 seconds stay on camera, and Ryan frames himself in the **RIGHT half** because the overlay owns the left column and YouTube's clickable cards go right. All three assets live in [`../../Brandkit/YouTube-Bumpers/`](../../Brandkit/YouTube-Bumpers/). None of them go on Skool.

## Instagram is the top of the funnel

[Instagram/](Instagram/) holds 12 Reels per level. They feed the YouTube cuts, which feed the community. Rules:

- **The five archetypes are the house set**, carried over from the older `../../Scripts/Lesson-N-Instagram-Shorts.md` files: Teaser, Quick Win, Before/After, Hot Take, Math. Reels 6 through 12 are per-level extensions.
- **Caption style follows `../../Scripts/Instagram-Reel-Captions.md`, not the `Lesson-4-Instagram-Shorts.md` generation.** The Lesson-4 files are full of em-dashes, which the workspace rule forbids. Reel-Captions is the corrected style: no em-dashes, four hashtags, and the standing close, "link in bio. Community's called The Leveraged Agent."
- **Two fields were added to the house format:** a **Hook text** line, the words burned into the first frame, because a reel is decided before the first sentence finishes; and a **Bio link** line, since Level 0 reels mostly point at the free YouTube video and Level 1 reels split between the video and the community.
- **The two sets are a ladder and must not blur.** Level 0's reels sell a paste block and never mention BROKER, Claude Code or a folder. Level 1's sell the folder. If a Level 1 reel would work word for word as a Level 0 reel, it is the wrong reel.
- **Every number in a Math reel is Ryan's to confirm before posting.** The arithmetic is sound but the inputs are claims about his own workflow, not verifiable facts.

## Working rules

- **No em-dashes.** Workspace rule, applies to every word in this folder including the paste-ready descriptions.
- **Never fabricate.** No invented prices, commission splits, MLS rules, statutes or program details. Anything unknown is marked `NOT FOUND, add before publish`.
- **Runtime discipline is real.** No level over 46 minutes. No idea over two minutes. Runtime declines as the ladder advances. See COURSE-ARCHITECTURE.md.
- **Compliance is Ryan's own jurisdiction.** He is licensed in Nevada. Level 9 gives frameworks and questions, never legal answers for other states. Keep it that way.
- **Every level ships its transcript as a `.txt` attachment.** Highest-leverage habit in the whole system, do not drop it.

## What this replaces

| Existing file in `../` | Disposition |
|---|---|
| `Module-0-Start-Here.md` | Retired. Content redistributed into Levels 1, 2 and 4. |
| `Module-1-Listing-Launch-Package.md` | Compressed into Level 5. |
| `Module-2-AI-Transaction-Coordinator.md` | Compressed into Level 6. |
| `Module-Open-Houses.md` + 5 lesson posts | Become bonus drop B2. Lesson posts stay usable as written follow-ups. |
| Planned Module 3 (social/content) | Becomes bonus drop B3. |

**Those files have not been deleted.** They are still in `../` and should stay there until the new ladder is recorded and live.

## Status

Architecture, description template, delivery playbook and all 14 lesson descriptions are **written**. **Level 0 and Level 1 also have finished teleprompter scripts and working decks.** Nothing is recorded. Open items:

- Scripts and decks exist for Levels 0 and 1 only. Level 4 has a partial script (voice section only, no deck). Levels 2 through 10 and the bonus drops still need both
- YouTube cuts exist for Levels 0 and 1 only, and only Level 0 has a YouTube deck
- Reels exist for Levels 0 and 1 only, 24 total. Levels 2 through 10 and the bonus drops have none
- The two listing descriptions in `deck/yt-level-0.html` are placeholder copy and must be regenerated from one of Ryan's real listings before that video is shot
- Level 0's YouTube description needs the Level 1 video URL pasted in once that one is live, in both the description and the end screen
- Every `NOT FOUND, add before publish` link needs a real URL
- Slide images referenced as `images/*.png` do not exist yet
- Attachment files referenced in each level do not exist yet, they get built as each level is recorded
- Launch dates are `[DATE]` placeholders
- Ryan needs to pick his fixed greeting and ritual line from the candidates in DELIVERY-PLAYBOOK.md

---

## Folder Map, keep this current

```
Claude Code Course for Realtors/
├── CLAUDE.md                         this file
├── COURSE-MAP.md                     one-page index, start here
├── COURSE-ARCHITECTURE.md            the ladder and why it is ordered this way
├── LESSON-TEMPLATE.md                the 9-block Skool description template
├── DELIVERY-PLAYBOOK.md              the on-camera delivery template
├── YouTube/                          the funnel cuts. One per level, rebuilt for cold traffic,
│   ├── YT-Level-0-Context-Block.md   8:45. Level 0's DIAGNOSIS, not its course map. No install.
│   │                                 Free win is a 4-part paste block. BROKER is NOT taught here
│   └── YT-Level-1-Setup.md           12:35. NOT the Skool script, see the diff table in the file
├── Instagram/                        Reels. 12 per level, 130-160 words each, ~60s
│   ├── Reels-Level-0.md              12 reels for the Context Block. Read this file's header
│   │                                 first, Level 1's format rules refer back to it
│   ├── Reels-Level-1.md              12 reels for the Business Brain. Names BROKER and
│   │                                 Claude Code; the Level 0 set deliberately does not
│   └── Carousels-Build-Drops.md      10 carousel build-drops, 8 slides + 1 keyword each.
│                                     Format reverse-engineered from the Kristi Jencks
│                                     teardown; carousels convert, reels only reach
├── deck/                             localhost presentation decks, Vector v2.0 inverted (true black)
│   ├── deck.css                      shared styling, do not add scroll-behavior:smooth
│   ├── deck.js                       keyboard nav, progress HUD, fit-to-screen zoom
│   ├── level-0.html                  8 slides, Skool
│   ├── level-1.html                  19 slides, Skool, no on-screen cues (they live in SCRIPT.md)
│   ├── voice.html                    10 slides, STANDALONE 4:45 voice video. No .hint on slide 1.
│   │                                 Slides 4-5 show stand-in samples; slide 9 side B = held-out
│   │                                 email, side A = Brain's pre-run draft
│   └── yt-level-0.html               13 slides, YOUTUBE. Not a cut of level-0.html. No .hint on
│                                     slide 1 (it is on screen at 0:00). Listing copy on slides
│                                     1 and 9 is PLACEHOLDER, swap in a real listing before shooting
├── 00-Level-0-Start-Here/            4-5 min, the map, no software. README.md + SCRIPT.md
├── 01-Level-1-Foundation-Setup/      40-45 min, longest level, Business Brain v1. README.md + SCRIPT.md
├── 02-Level-2-Landing-Pages/         32-36 min, first visible win, live URL
├── 03-Level-3-Power-Features/        32-36 min, skills and commands
├── 04-Level-4-Memory-System/         32-36 min, voice, farm data, client history. README.md +
│                                     SCRIPT.md (PARTIAL: only Part 4, the voice section 09:50-16:00,
│                                     is written; no deck yet) + voice-extraction.md (the 5-prompt
│                                     attachment the voice section reads out loud) +
│                                     SCRIPT-Voice-Standalone.md (4:45 self-contained cut of the
│                                     voice section, director version) + TELEPROMPTER-Voice-
│                                     Standalone.md (words + cues only, read this on camera) +
│                                     demo-voice-samples/ (20 FICTIONAL stand-in samples + 1 held-out
│                                     blind-test email + voice.md + the slide 9 draft, by Claude in Ryan's voice, no real
│                                     client data goes on camera). Deck = deck/voice.html
├── 05-Level-5-Listing-Launch/        38-42 min, absorbs old Module 1
│   └── Weekly-Seller-Update-Prompt/  attachment set: weekly-seller-update-plan-prompt.md (paste into
│                                     Plan Mode, builds the weekly seller report + email system, from
│                                     29 Amber Rock) + how-to-use.html -> How-to-Use-the-Weekly-Seller-
│                                     Update-Builder.pdf (2-page Vector quick-start) + logo.svg
├── 06-Level-6-Transactions/          38-42 min, absorbs old Module 2
├── 07-Level-7-Build-Anything/        22-26 min, the method, no new tools
├── 08-Level-8-Design-Systems/        22-26 min, brand.md and design tokens
├── 09-Level-9-Compliance/            18-22 min, shortest core level
├── 10-Level-10-Scale/                25-28 min, business only, no software
├── B1-Bonus-Cowork-Automations/      8-10 min, scheduled routines + browser
├── B2-Bonus-Open-Houses/             8-10 min, absorbs old Open Houses module
└── B3-Bonus-Content-Engine/          8-10 min, absorbs planned Module 3
```

**Maintenance rule:** When you add, remove, move or rename anything here, update this Folder Map **and** the Folder Map in [`../CLAUDE.md`](../CLAUDE.md) in the same change. Never leave either stale.

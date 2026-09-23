# CLAUDE.md — Jack Roberts AI Course (competitor course archive)

## What this folder is

A **complete local archive of Jack Roberts' "🤖 Claude Code Course"**, captured 2026-08-23 from his Skool community **AI Automations by Jack** (`skool.com/aiautomationsbyjack`, classroom id `af686ad3`).

**This is reference material, not Ryan's product.** Nothing in here is Leveraged Agent content. It is a competitor teardown kept so Ryan can copy the *structure and flow* of Jack's onboarding and level ladder for real estate agents.

## Why it exists (read this before doing anything here)

Ryan is **rebuilding the onboarding system inside The Leveraged Agent Skool community**. He likes how Jack flows a student from "I just joined" through to "I built a thing", and he wants to make videos that follow almost exactly that flow, aimed at real estate agents instead of general automators.

So when you are asked to work with this folder, the job is almost always one of:

1. **Find how Jack does X** (opens a lesson, sequences a level, structures resources, handles setup tedium) so Ryan can mirror it.
2. **Translate a Jack level into a real estate agent equivalent** for The Leveraged Agent.
3. **Pull an exact quote, timestamp list, or attachment** out of the archive.

Start at [COURSE-MAP.md](COURSE-MAP.md). It indexes every lesson, every external link, and every attachment in one place.

## What was captured, and what was not

| Section | Lessons | Captured |
|---|---|---|
| Start here | 2 | Yes |
| 🦸 Claude | 14 | Yes, in full |
| 🥇 Hermes Agent | 9 | Yes, in full |
| 📚 Archive | 16 | **No, deliberately skipped** |
| 🏆 Certification | 2 | **No, deliberately skipped** |

**25 lessons, about 10h 20m of video, 33 attachments, 25 in-description images, 47 external links.** Every lesson has a full transcript.

Ryan explicitly said not to touch Archive or Certification. Do not go back for them unless he asks.

## How each lesson folder is laid out

Every lesson is its own folder, and everything about that lesson lives inside it. Nothing is pooled.

```
<section>/<NN>-<Lesson-Name>/
├── README.md        the lesson itself: title, Skool URL, video length, Jack's full
│                    written description converted to markdown (timestamps included),
│                    a table of every external link, a table of every attachment
├── transcript.md    full word-for-word transcript, broken into readable paragraphs
├── attachments/     the actual downloaded files, original filenames preserved
└── images/          the images Jack embedded in the description, downloaded locally
                     and rewritten to relative paths so README.md renders offline
```

**Read `README.md` first for any lesson.** It is the single entry point and it tells you what else is in the folder.

### Transcript sources

- **22 lessons** ship Jack's own `transcript` attachment (a `.txt`). Those are in `attachments/` and also promoted to `transcript.md`.
- **3 lessons** had no transcript attached: `00-Start-Here/00-What-you-ll-learn`, `00-Start-Here/01-Your-Pathway`, and `01-Claude/11-Claude-Code-Hermes-OS`. Their `transcript.md` was recovered from the video's auto-generated English captions and is labelled as such in the file header. Treat those three as slightly less exact than the rest.

### A note on the big attachments

Five Hermes slide decks are self-contained HTML files in the 3.6 to 4.4 MB range because every image is inlined. `Hermes Masterclass - Chapter 3.zip` and the two `.zip` skill bundles in `01-Claude/08-Level-8-Design-Systems/attachments/` are real zips. Open the HTML decks in a browser, they are full presentations.

## Working rules for this folder

- **Jack's words are source material. Do not edit them.** `README.md` descriptions and `transcript.md` files are verbatim captures. They contain em-dashes and Jack's own voice. That is correct and must stay. The workspace no-em-dash rule applies to **anything you write**, not to what he wrote.
- **Never publish, repost, or repurpose Jack's copy as Leveraged Agent content.** Structure and sequencing are fair to learn from. His actual scripts, slides, and prompt text are his.
- **Anything Ryan builds from this goes in the parent `SKOOL Community/` folder, not here.** Keep the archive clean and unmodified so it stays a reliable reference.
- Affiliate links in the resource tables are Jack's affiliate links. Do not present them as recommendations.

## The shape Ryan is copying

The high-level structure worth knowing without opening anything:

- **A 2-lesson "Start here"** that is pure orientation, 8 minutes total, no software touched. "What you'll learn" then "Your Pathway".
- **Then a numbered level ladder, Level 0 through Level 10**, where Level 0 is a 4-minute map of the whole thing and Level 1 is the long setup lesson (46 minutes, the longest in the course).
- **A second track (Hermes Agent, Level 0 to Level 8)** that reuses the identical Level 0-to-N naming, so a student who finished one track already knows how the next one is shaped.
- **Bonus "OS" lessons** appended to the main track (`Voice OS`, `Design OS`, `Claude Code + Hermes OS`) that are short, 5 to 10 minutes, and sit outside the numbered ladder.
- **Every level has a timestamp list in the description**, plus attached transcript, plus links to the exact tools used.

Two structural teardowns of the craft behind this live in [TEARDOWN-Claude-Section.md](TEARDOWN-Claude-Section.md) and [TEARDOWN-Hermes-Section.md](TEARDOWN-Hermes-Section.md).

---

## Folder Map — keep this current

```
Jack Roberts AI Course/
├── CLAUDE.md                        this file
├── COURSE-MAP.md                    master index: every lesson, link, and attachment
├── TEARDOWN-Claude-Section.md       structural analysis of the 14-lesson Claude track
├── TEARDOWN-Hermes-Section.md       structural analysis of the 9-lesson Hermes track
├── 00-Start-Here/                   2 lessons, the pure-orientation intro (8m total)
│   ├── 00-What-you-ll-learn/        3m01s, captions-sourced transcript
│   └── 01-Your-Pathway/             5m43s, captions-sourced transcript
├── 01-Claude/                       14 lessons, 5h38m, the Claude Code masterclass
│   ├── 00-Level-0-Start-Here/       through
│   ├── 10-Level-10-Making-SSS/      the numbered Level 0-10 ladder
│   ├── 11-Claude-Code-Hermes-OS/    bonus, captions-sourced transcript
│   ├── 12-Voice-OS/                 bonus
│   └── 13-Design-OS/                bonus
├── 02-Hermes-Agent/                 9 lessons, 3h23m, Level 0-8, build a personal AI agent
│   ├── 00-Level-0-Start-Here/       through
│   └── 08-Level-8-Make-Money-with-Hermes/
└── _assets/
    ├── manifest.json                machine-readable index of all 25 lessons
    └── raw-capture/                 the untouched JSON pulled off Skool before it was
                                     split into folders. jack-lessons.json = every lesson's
                                     raw TipTap description, resource list and video meta.
                                     jack-files-ALL.json = every attachment's bytes. Keep
                                     these, they let the whole tree be rebuilt from scratch.
```

**Maintenance rule:** When you add, remove, move, or rename anything in this folder, update this Folder Map **and** the Folder Map in [`../CLAUDE.md`](../CLAUDE.md) (SKOOL Community) in the same change. If anything moves out of the SKOOL Community tree entirely, also update the root [`../../CLAUDE.md`](../../CLAUDE.md). Never leave a Folder Map stale.

# Claude Code Course for Realtors: Course Architecture

**Working title:** Claude Code Course for Realtors
**Format:** ONE classroom course tile in Skool. Not ten tiles. Everything lives inside this one course, the way Jack Roberts runs his.
**Structure:** Level 0 through Level 10, plus short bonus drops appended at the end.
**Primary tool:** Claude Code throughout. Claude Cowork appears only where Ryan actually uses it, which is scheduled automations and browser work, and it gets its own bonus drop.
**Carried artifact:** the **Business Brain** folder.

Modeled on the structural teardown in [`../Jack Roberts AI Course/TEARDOWN-Claude-Section.md`](../Jack%20Roberts%20AI%20Course/TEARDOWN-Claude-Section.md). Structure and sequencing only. None of Jack's copy, scripts or slides are reused.

---

## The one rule that makes this work

**Every level upgrades something the student already owns.** Nothing is a standalone exercise. That single decision is why Jack's students finish and why module-based courses stall out. The thing they own is the Business Brain.

| Level | What gets added to the Business Brain |
|---|---|
| 1 | The folder itself, `CLAUDE.md`, identity, farm areas, price bands, brokerage rules |
| 2 | A `pages/` directory and a live landing page |
| 3 | A `skills/` directory with their first custom commands |
| 4 | Real memory: voice profile from their own past writing, past client roster, closed-deal history, a searchable market wiki |
| 5 | A `listings/` directory and the one-command launch |
| 6 | A `transactions/` directory and the AI TC |
| 7 | Whatever they build on their own, using the method |
| 8 | A `brand/` directory with their design system |
| 9 | Permission tiers, a compliance file, a locked-down setup |
| 10 | Nothing new. Level 10 is the argument for why the whole folder was worth building. |

At Level 10 the Business Brain **is** their business. That is the payoff, and it is the thing they cannot get anywhere else.

---

## The ladder

| # | Level | Runtime | Capability unlocked | Artifact state after |
|---|---|---|---|---|
| 0 | Start Here | 4-5 min | A map, and permission to feel behind | none |
| 1 | Foundation + Setup | 40-45 min | A working machine plus three throwaway wins | Business Brain v1 exists |
| 2 | Landing Pages | 32-36 min | A live URL they can text to a client today | First page shipped |
| 3 | Power Features | 32-36 min | Claude working without them sitting there | First custom skill |
| 4 | Memory System | 32-36 min | It sounds like them and knows their market | Brain that remembers |
| 5 | Listing Launch | 38-42 min | A full listing launch on one command | `listings/` live |
| 6 | Transactions | 38-42 min | Deals run themselves for 15 min a day | AI TC live |
| 7 | Build Anything | 22-26 min | A method instead of a tool | Their own workflow |
| 8 | Design Systems | 22-26 min | Work that looks expensive | Brand system |
| 9 | Compliance | 18-22 min | Permission to run this on real client data | Locked-down setup |
| 10 | Scale | 25-28 min | Knowing where the leverage actually is | The argument |

**Core ladder total: roughly 5 hours 10 minutes across 11 videos.** For reference, Jack's Claude ladder is 5h 16m across 11.

### Bonus drops (outside the numbered ladder, 5-10 min each)

| Drop | Runtime | Why it exists |
|---|---|---|
| B1: Cowork Automations | 8-10 min | Scheduled routines and browser tasks. The one place Cowork earns its keep. |
| B2: Open Houses | 8-10 min | Absorbs the existing Open Houses module as a lead-gen system. |
| B3: Content Engine | 8-10 min | Absorbs the planned social/content module. |

These are retention content, not curriculum. Short, high-delight, and they let Ryan ship something new without touching the ladder.

---

## Why this order and not another

**Environment before output.** Level 1 runs 45 minutes and produces no listing, no page and no revenue. That is deliberate. The bet is that setup abandonment, not boredom, is what kills onboarding. Three small wins get handed out *inside* Level 1 so nobody sits through 45 minutes on faith.

**Visible win at Level 2, not Level 1.** A live landing page on a real domain is the first thing a student can show another agent. It arrives at minute 46 of the course, not minute 300.

**Automation only after manual.** Skills and sub-agents (Level 3) come after a full manual build (Level 2). You cannot automate a workflow you have never done by hand, and a student who automates too early automates the wrong thing.

**Memory after skills.** Level 4 is implemented *as* skills learned in Level 3. Reverse them and Level 4 has no delivery mechanism.

**Revenue work after memory.** Listing Launch (5) and Transactions (6) are the levels that make money, and both depend on the Brain knowing their voice, their farm and their past clients. Running them at Level 2 would produce generic output and teach the student that AI writing sounds like AI writing.

**Method after tools.** Level 7 works only because there are six levels of worked examples behind it. It is the level that makes the course outlive Ryan's lesson list.

**Compliance late, but before money.** Level 9 is retro-applied to everything built in 1 through 8. It has to come after there is an attack surface, and before Level 10 tells them to run this on client data at volume.

**Money last, with zero new software.** Level 10 introduces no tools. It works only because the student now owns something demonstrable.

### Difficulty jumps to watch

- **Level 0 to 1.** Five minutes to forty-five, and from nothing to terminal, folders, permissions and connectors. Biggest cliff in the course. Every mitigation Ryan has goes here.
- **Level 3 to 4.** Abstract for the first time. Nothing visibly ships. Needs the strongest in-lesson wins.
- **Level 5 to 6.** Transactions is the densest technical level: dates, deadlines, documents, multiple parties, real liability.

### Deliberate cool-downs

Never two hard levels back to back. Level 7 is philosophy right after Transactions. Level 10 is pure business right after Compliance. The three bonus drops sit at the end as low-effort, high-delight content.

---

## Where the wins land

Every level needs a moment where something visibly works. Jack plants one roughly every 8 minutes in the early levels.

| Level | The win |
|---|---|
| 1 | Desktop cleaned up by prompt. A folder built by prompt. A real email drafted in their own words. Three of them, before minute 30. |
| 2 | A live URL on a domain they own, purchased on camera. |
| 3 | A repeated 20-minute task collapsed into one word, built from scratch in about two minutes. |
| 4 | Asking the Brain a question about a client from eight months ago and getting the right answer. |
| 5 | A full listing launch package generated on one command while Ryan talks over it. |
| 6 | An inspection response objection letter drafted from a real PDF in under a minute. |
| 7 | A workflow Ryan has never taught, built live from a student-style request. |
| 8 | Side by side of a stock listing graphic and the branded version. |
| 9 | A red-team pass that finds something real in Ryan's own setup, left in the cut. |
| 10 | No software win. Status instead: you are the agent who finished this. |

---

## What this replaces

| Existing | Disposition |
|---|---|
| `Module-0-Start-Here.md` (9 lessons, Day 1-7) | **Retired.** Its content is redistributed into Levels 1, 2 and 4. The Day 1-7 framing goes away. |
| `Module-1-Listing-Launch-Package.md` (10 lessons) | **Compressed into Level 5.** The 10-lesson detail becomes timestamps and an attached prompt pack, not 10 videos. |
| `Module-2-AI-Transaction-Coordinator.md` (10 lessons) | **Compressed into Level 6.** Same treatment. |
| `Module-Open-Houses.md` (5 lessons) | **Becomes bonus drop B2.** Existing lesson posts and scripts stay usable. |
| Planned Module 3 (social/content) | **Becomes bonus drop B3.** |

A note on compression, because it is the part that feels wrong until you see it work: Jack's Level 2 covers competitive research, a design brief, three parallel builds, deployment, a domain purchase and a critic pass. That is easily ten lessons of material. It is one 36-minute video with 19 timestamps. The depth does not disappear, it moves into the timestamp list and the attachments. Students re-watch a single 90-second step rather than hunting a lesson.

---

## Runtime discipline

Rules taken from the pacing data in the Jack teardown, and worth enforcing:

- **No level over 46 minutes.** Even the setup level.
- **No idea over two minutes.** Beat density should land between 60 and 115 seconds per timestamp entry.
- **Runtime declines as the ladder advances.** Scaffolding thins out on purpose. If Level 9 runs longer than Level 4, something is wrong.
- **The compliance level is the shortest core level.** Compress the medicine.
- **The money level carries no new software.** Do not pad the pitch.

---

## Naming and placement in Skool

- One course tile: **Claude Code Course for Realtors**.
- Lessons named `Level 0: Start Here`, `Level 1: Foundation + Setup`, and so on, so a student always knows where they are without opening anything.
- Bonus drops named `Cowork OS`, `Open House OS`, `Content OS`, sitting below Level 10 and outside the numbering, which signals "extra" without saying it.
- No gating between levels. Jack does not gate, and the ladder gates itself: Level 4 is useless without Level 3's skills.

---

## Files in this folder

| File | What it is |
|---|---|
| `COURSE-ARCHITECTURE.md` | this file |
| `LESSON-TEMPLATE.md` | the 9-block Skool description template, blank, with the rules for each block |
| `DELIVERY-PLAYBOOK.md` | the on-camera template: the opening beats, the ritual, the demo pattern, the close |
| `<NN>-Level-N-<Name>/README.md` | the finished, paste-ready Skool description for that level |

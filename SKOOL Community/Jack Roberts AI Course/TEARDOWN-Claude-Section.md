# Claude Section: Structural Teardown

Source: [`01-Claude/`](01-Claude/) (14 lessons) and [`00-Start-Here/`](00-Start-Here/) (2 lessons). Runtimes and resource lists taken from each lesson's `README.md`. Craft observations taken from close reads of the Level 0, 1, 2, 4, 8 and 10 transcripts, with 3, 5, 6, 7, 9, 11, 12 and 13 read for openings, frameworks and handoffs.

---

## 1. The Level Ladder

| # | Lesson | Runtime | Capability unlocked | New tools introduced |
|---|---|---|---|---|
| 0 | Level 0: Start Here | 4m 34s | A map of the journey and permission to skip around | none |
| 1 | Level 1: Foundation + Setup | 45m 56s | A working machine, plus three throwaway wins | Claude desktop, Anti-Gravity, terminal, GitHub, connectors, CLAUDE.md |
| 2 | Level 2: Website Masterclass | 35m 45s | A live URL on a domain you own | Firecrawl, 21st.dev, CodePen, OpenAI image API, GitHub, Vercel, 2 skills |
| 3 | Level 3: Power Features | 33m 46s | Claude working without you present | Skills, marketplaces, routines, custom MCP, sub-agents, plugins |
| 4 | Level 4: Memory System | 37m 22s | Persistence across sessions and machines | Obsidian, Karpathy RAG, Pinecone, NotebookLM, Granola |
| 5 | Level 5: Hermes Agent | 30m 37s | The brain leaves the desk (phone access) | Docker, Hermes, Telegram BotFather, soul.md, Pantheon |
| 6 | Level 6: Apps | 32m 56s | The website becomes a product that takes money | Supabase, auth, Stripe, Resend, Beehiiv, OpenRouter |
| 7 | Level 7: Build Anything | 23m 54s | A method instead of a tool | Apify, Anymail Finder, Apollo |
| 8 | Level 8: Design Systems | 25m 19s | Work that looks expensive | Open Design, Power Design, brand extraction skill, Krea, Spline, Coolors |
| 9 | Level 9: Compliance and Maintenance | 19m 29s | Permission to take client money safely | GitLeaks, Semgrep, Trivy, Sentry, red team prompt |
| 10 | Level 10: Making $$$ | 27m 01s | Conversion of skill into revenue | none |
| 11 | Claude Code + Hermes OS | 9m 39s | Proprietary dashboard, exclusivity payoff | the OS zip |
| 12 | Voice OS | 5m 32s | Voice layer on Hermes | Whisper, OpenAI Realtime, ElevenLabs |
| 13 | Design OS | 6m 46s | Local image pipeline with cost tracking | Higgsfield, Krea, OpenRouter |

### Why this order works

**Environment before output.** Nothing gets built until the machine is set up and one disposable win has already landed. Level 1 spends 46 minutes on install, plans, permissions, context, connectors and folder structure, and gives away three small wins inside that time (desktop cleanup, a Google Drive folder created by prompt, a Granola meeting extracted into a formatted HTML brief). By the time Level 2 starts, the student has already seen the tool touch their real life.

**One artifact carried through six levels.** The website built in Level 2 is the spine of the course. Level 6 adds email capture, auth and Stripe to it. Level 8 redesigns it and swaps in a 4K video loop. Level 9 uses it as the red team target. Level 10 turns it into the free trojan horse offer. Nothing is a standalone exercise.

**Capability before autonomy.** Routines, sub-agents and critic loops (Level 3) only arrive after the student has manually done a full build (Level 2). Automation gets introduced when there is finally something worth automating.

**Memory after skills, not before.** Level 4 is implemented entirely *as* skills and routines learned in Level 3 (`obsidian wrap-up`, `pinecone wrap-up`, `obsidian ask`, a daily meeting sync routine). Reversing 3 and 4 would break the build.

**Mobility after memory.** Hermes (Level 5) is only valuable because there is a Level 4 brain to query from a phone. The whole second half of Level 5 is plugging Hermes into the Obsidian vault and NotebookLM from Level 4.

**Money last, with zero new software.** Level 10 introduces no tools at all. It is pure business framing, and it only works because the student now owns a demonstrable artifact.

### Difficulty jumps

- **Level 0 to 1.** 4 minutes to 46 minutes, and from zero software to terminal, GitHub, API keys and MCP URLs. This is the largest cliff in the section.
- **Level 4 to 5.** Docker, images versus containers, Telegram BotFather, whitelisting a user ID, model authentication. The README's own timestamps show 06:03 through 11:33 is nothing but Docker.
- **Level 5 to 6.** Databases, row-level security, Supabase CLI login through the terminal, Stripe sandbox products, DNS-verified email sending. Densest technical level in the section.

### Where he gives a win

- **Level 1, roughly minute 26.** Desktop cleanup, then a Google Drive folder, then a meeting summary pulled from Granola and written into Drive as formatted HTML. Three visible results before the student has built anything real.
- **Level 2.** A live Vercel URL plus a purchased custom domain, on camera, including the checkout.
- **Level 3, roughly minute 7.** A working Bitly skill built from scratch in about two minutes, tested live, link clicked.
- **Level 4.** The Obsidian graph view populating with nodes as the wiki indexes.
- **Level 8.** A side by side of the original site and his rebuild, with the claim that his version is better.
- **Level 10.** No software win at all. He substitutes status: the reward for reaching Level 10 is being told you are the kind of person who reached Level 10.

### Deliberate cool-downs

He never runs two hard levels back to back. Level 7 is philosophy and reading immediately after Level 6's database work. Level 10 is pure business immediately after Level 9's security material. The three OS bonus lessons (9, 5 and 6 minutes) sit at the end as low-effort, high-delight retention content.

---

## 2. Lesson Anatomy

The repeatable template, verified across Levels 1, 2, 3, 4, 5, 6, 7, 8, 9 and 10.

### The first 30 seconds: five fixed beats, in order

1. **Fixed greeting to a named identity.** "Hey there beautiful AI automator." Variants: "How you doing beautiful automator" (Level 0), "Howdy there beautiful AI automates" (Level 2). It never changes and it never gets explained.
2. **Level number and subject in one clause.** "and welcome to level eight, well, we're gonna be talking about design systems."
3. **Spoken agenda as a run-on list of "I'm going to show you X."** Level 1 lists ten items in about 40 seconds. Level 3 lists ten. Level 4 lists four. It is deliberately breathless, not organized.
4. **The promise as an end-state capability, not a topic.** Level 2: by the end you go "from zero to having a published website that you can send people through." Level 6: "we can build essentially apps in less than 60 minutes."
5. **A physical ritual instruction.** Grab a coffee, lock in, phone on do not disturb. Present in Levels 0, 1, 3, 5, 6, 7, 9 and 10.

There is no cold open, no results montage, no "in this video" cut-away, and no music-bed intro. He is talking within the first second of every lesson.

### How he frames the promise

The promise is always framed as **capability transfer plus scarcity**, never as information. Two moves repeat:

- **Status delta.** Level 3: skills are "the difference between a joe and a pro." Level 5: after this "you're going to be so far ahead of people, they're going to be like a dot looking back." Level 4 closes on the same device, telling the student they now know more about memory systems than most AI experts.
- **Exclusivity stamp.** He asserts, per lesson, that the material is not published anywhere else. Level 2 calls the hacks "a complete community exclusive." Level 4 says the memory system "is not live anywhere else." Level 8 says the brand extraction skill is "available nowhere in the world, except for this community." Levels 11, 12 and 13 lean on this almost exclusively.

He also frames the promise against **a named enemy**, stated in the first two minutes:

| Level | The enemy |
|---|---|
| 2 | Building websites without knowing what already works |
| 3 | Burning tokens on the wrong model, and messy mid-conversation refactors |
| 4 | Context rot forcing a choice between forgetting and degrading |
| 7 | Derivative reasoning, automating processes that should not exist |
| 9 | Shipping to production with no guardrails |
| 10 | Throwing AI at problems that are not the constraint |

### Demo versus theory sequencing

The unit of a Jack lesson is roughly 90 seconds: **concept with an analogy, then live demo, then start the next concept while the demo runs, then return to the result.**

He never waits in silence. The transitions are explicit and verbal:

- Level 2: "whilst that's happening I want to show you another cool little hack"
- Level 3: "whilst this is working in the background I want to come over and really touch on the next power feature"
- Level 8: "so while this is working in the background, let's go through this"
- Level 1: "we'll let it do that work in the background"

Every level opens with **one conceptual frame carried by an analogy before any software is touched**:

| Level | Opening frame |
|---|---|
| 1 | The model is Tony Stark, the IDE is the Iron Man suit |
| 2 | Power law: find what is already working and extract it |
| 3 | Skills are the difference between minor and major leagues |
| 4 | Three levels of memory, and memory solves the context problem |
| 5 | The AI chief of staff, traced from Siri to now |
| 6 | Probabilistic models versus deterministic data structures |
| 7 | First principles, from Aristotle to Descartes to Musk |
| 8 | Design is code, and AI is bad at design unless you codify it |
| 9 | Risk appetite, and systems that fall apart like a cheap suitcase |
| 10 | Theory of constraints, illustrated with a Lamborghini engine |

Theory is never longer than about three minutes before a screen share resumes. Levels 7, 9 and 10 are the theory-heaviest and are also the three shortest core levels, which is not a coincidence.

### How he handles install and setup tedium

His most distinctive craft move, and the one most worth stealing.

1. **He delegates the install to the AI on camera rather than narrating steps.** Level 1: he types into Anti-Gravity, asking it to install Claude Code and any dependencies required to run it. Level 8: "hey, dude, I want you to run the application." Level 12: he tells the student to go back to Claude and ask it to wire up a local open-source voice model, because the instructions are already in the OS file. This kills the version-drift support burden and teaches the meta-skill at the same time.
2. **He breaks his own working setup to show the failure path.** In Level 1 he deletes his functioning Firecrawl connector on camera specifically so he can demonstrate what to do when the tool you want is not in the connector list. He then refuses to just hand over the MCP URL, invoking teach-a-man-to-fish, and shows the student how to ask a chat model for it instead.
3. **He narrates the waiting.** "Give that a hot second," "give that a heart beautiful second." Dead air during installs and generations gets filled with the next concept or with commentary on the output.
4. **He pre-labels optional steps and prices them.** Level 1 on the YouTube API: you do not have to do this, it is a very specific use case. Level 2 on the OpenAI image key: not required, but if you want to take it to a new level. Level 12 gives free-local versus roughly five to ten cents a minute paid. This removes the point where a student stalls on an unnecessary step.
5. **He normalizes failure before anything can break.** Level 11: it is completely normal for the OS not to detect a specific setup. The Start Here lessons give the escape hatch up front: screenshot the problem, paste it into a model with your desired objective, ask for a step-by-step fix, or post in the community.
6. **He shows real friction rather than editing it out.** Level 4's NotebookLM authentication fails twice on camera and he retries. Level 2 pauses for DNS propagation and he says so.

### How he ends

Four beats, in order, in every core level:

1. **Recap phrased as accomplishment, not summary.** Level 1: "taking a step back, what have we done? We've installed it, we've done to the interface... you've effectively set up the entire foundation."
2. **Status conferral.** Level 4 tells the student they are now ahead of nearly everyone on the planet on memory systems. Level 10 tells them they could be drinking beers in a pub and instead they are here.
3. **Next level named with a specific payoff**, often with a visual teaser. Level 7 closes by showing a design-system website and noting it was one-shot, which is the setup for Level 8. Level 5 closes by naming exactly what Level 6 covers: architecture, sign-in flows, email, backend, payments.
4. **Coffee ritual plus a fixed sign-off.** "I'll catch you inside the next beautiful module."

### How he hands off

The handoff is a **dependency claim**, not a tease. Level 2 opens by stating the course design out loud: each level adds onto the existing thing, so it all bolts together. Level 6 opens by pointing back at the Level 2 website as the thing being upgraded. Level 8 reuses the Level 2 GitHub-to-Vercel flow without re-teaching it. Level 11's OS is presented as the visual surface of the Level 4 memory system and the Level 5 Hermes agent. Skipping a level costs you the artifact for the next one.

---

## 3. Hook and Promise Language

Short verbatim fragments, attributed.

**Openers and identity**
1. "Hey there beautiful AI automator" (universal open, every level)
2. "if you can imagine it you can almost certainly build it" (Level 0)
3. "put it on do not disturb and put it out of the room" (Level 0)
4. "I hope you got that coffee ready because we're going to lock in" (Level 3)

**Concept hooks**
5. "the environment is the Ironman suits" (Level 1)
6. "a 200 IQ individual that also has amnesia" (Level 1, on the context window)
7. "one task, one window" (Level 1, restated in Level 3)
8. "skills are the difference between a joe and a pro" (Level 3)
9. "let's not use a bazooka to open a door" (Level 3, on model choice)
10. "we don't need Albert Einstein to mop our floors" (Level 3, reused in Level 11)
11. "the best memory system is the one that you use" (Level 4)
12. "if you don't instruct it properly, it will eat crayons" (Level 8, on AI and design)
13. "design, we need to understand now, is code" (Level 8)
14. "it can fall apart like a $2 suitcase" (Level 9)
15. "everything's downstream of media" (Level 10)
16. "where attention goes, money flows" (Level 10)
17. "everything else is a recommendation" (Level 7, on constraints)
18. "you're going to get paid to pitch your products" (Level 10, on the paid audit)

**Re-motivation and transitions**
19. "whilst that's happening I want to show you another cool little hack" (Level 2)
20. "give that a hot second" (used across Levels 1, 2, 4, 8 as the wait-filler)
21. "grab that coffee and I'll catch you inside the next beautiful module" (Level 1 close, near-identical in Levels 5, 7, 8, 9)

---

## 4. Teaching Devices

### Named frameworks

| Device | Where | What it is |
|---|---|---|
| **BALLAST** | Level 1 (41:28 to 45:38) | The CLAUDE.md framework: Brief, Loop, Architect, Ship, plus a behavior block of "think before coding, simplicity first, surgical changes, goal-driven execution." Hard cap of 200 words per file. |
| **The 5-8 folder system** | Level 1 (41:28), restated Level 4 (03:59) | Ask any model to organize everything you do into five to eight thematic buckets, then create those as desktop folders, one CLAUDE.md each. He is explicit: more than eight means you need to simplify. |
| **Three levels of memory** | Level 4 (01:42) | Short term = the instructions-for-Claude field. Mid term = the 5-8 folders plus a project operating manual. Long term = Obsidian wiki plus Pinecone vectors. |
| **Three-step website system** | Level 2 | Competitive intelligence, then a design brief (`best-principles.md`), then deploy. |
| **Three connection levels** | Level 1 (27:19 to 41:28), restated Level 3 (20:54) | Built-in connector, then custom MCP URL, then API key, then CLI. Stated rule of thumb: wherever possible go for the CLI, it is the most token efficient. |
| **Three permission modes** | Level 1 (06:14 and 17:56) | Ask First, Accept Edits, Bypass. Mapped to trust level and task type, with Accept Edits as the daily default. |
| **5-Step Engineering Protocol** | Level 7 (04:50) | Question every requirement (each must carry a person's name), delete the part or process (if you do not add 10 percent back later you did not delete enough), simplify and optimize only after deletion, accelerate cycle time, then automate. Attributed to Isaacson 2023 and Musk. |
| **20 Universal Design Rules / Power Design** | Level 8 (03:59) | His own GitHub repo. Includes glanceable-in-three-seconds white space and a 1.67 golden-ratio relationship between type sizes. |
| **12 Rules / Commandments of security** | Level 9 (02:49 to 08:00) | API keys never in chat, env vars, service roles, RLS, MFA, dependency audits, tool poisoning, sandboxed LLM inputs, fixed spend caps, data residency, webhook verification. |
| **Theory of Constraints** | Level 10 (01:12) | Goldratt 1984. One bottleneck at a time. |
| **More, Better, New** | Level 10 (03:39) | Double the volume of what already works, only then improve quality, only then open a new channel. |
| **The Money Loop** | Level 10 | Find the constraint, more, better, new, apply AI, measure, receive a bigger constraint. Explicitly framed as never-ending. |
| **Audit, Build, Retain** | Level 10 (18:23 to 22:06) | A paid $1k to $3k diagnostic, then a $10k+ build, then a retainer. |
| **BLAST framework** | Level 6 (spoken at 00:37) | Mentioned once by name for app building. Not developed on camera the way BALLAST is in Level 1. The name collision with BALLAST is unresolved in the material. |

### Recurring metaphors

- **Tony Stark and the Iron Man suit** (Level 1). Model versus environment.
- **200 IQ genius with amnesia** (Level 1). The context window.
- **Willy Wonka's emporium** (Level 1 for the connector store, Level 7 for the Apify scraper store). Reused verbatim across levels.
- **Universal remote control** (Level 1 and Level 3). MCP.
- **The cards and the wrapper** (Level 3). API is the raw cards, MCP is the thing around them that organizes and filters.
- **Google Drive plus Facebook for developers** (Level 1). GitHub.
- **Game saved state** (Level 2). Version control.
- **Albert Einstein mopping floors, a bazooka to open a door** (Level 3, reused Level 11). Model selection economics.
- **Excel on steroids** (Level 6 description). Supabase.
- **Cards on a bookshelf with a secretary** (Level 4). Chunking, retrieval and semantic search, illustrated with searching for "cloak" and retrieving "garb" and "garment."
- **The Lamborghini engine** (Level 10). One engine per day makes tire throughput irrelevant.
- **The BMW diagnostic** (Level 10). Why a paid audit sells the bigger job.
- **Michael Jordan** (Your Pathway on missed shots, Level 3 on practice).
- **Autopilot versus taking the cockpit**, and **the city versus the plumbing** (Your Pathway). Anti-Gravity versus n8n.

### Rules of thumb he repeats

- One task, one window (Level 1, Level 3).
- Your first prompt is the most important prompt. If it took five prompts, ask for the prompt back and start a fresh session (Level 3, 14:10).
- Effort level: extra high, not max, because max overthinks and loops (Level 1, 24:14).
- Keep CLAUDE.md under 200 words (Level 1).
- Principle of minimal access: a routine gets only the connectors it needs (Level 3, 17:05, reinforced in Level 9).
- Never ship code without external review by a different model (Level 3, 30:24).
- Sub-agents only when the context is genuinely shared, otherwise use separate conversations (Level 3).
- If you want to see it, use Obsidian. If you want to store and recall it by meaning, use Pinecone (Level 4).
- Start on Pro, upgrade to Max when you hit the wall (Level 1, 15:31).
- Start and end frames, and 4K not 720, for looping video assets (Level 8, 17:53).
- Under 100k a month, run one business, not five (Level 10).
- People prefer a mediocre response quickly to an excellent one five days later (Level 9, incident comms).

### Repeatable prompt patterns he teaches by name

- **"My stated intention is..."** (Level 1). Prefacing a task with intent to reduce permission friction and misfires.
- **The judging matrix prompt** (Level 2, pasted verbatim in the README). Make the model build its own scoring rubric for competitors, then find what the top five share that the bottom five do not.
- **The critical critic prompt** (Level 2). Fresh browser, "act as a critically challenging individual," return critical, high, medium, low, and do not invent problems that do not exist.
- **The bucket prompt** (Level 4). Organize my life into five to eight thematic buckets.
- **The bottleneck prompt** (Level 7 close). This is what I am trying to achieve, ask me questions to clarify my intentions, this is my desired outcome, how should I think about the problem.
- **The red team prompt** (Level 9). A senior offensive security engineer persona auditing a live repo. Shipped as a Notion page.
- **The crystal ball question** (Level 10). If one thing were true in three months, what would make everything else irrelevant?

---

## 5. Resource and Attachment Pattern

### Per-lesson description structure (Levels 1 through 10, consistent)

1. Optional launch date line (Levels 4 through 10).
2. One to three **slide images from the deck**, embedded at the very top, showing the framework diagram for that level.
3. **Timestamp block** headed with a stopwatch emoji, 15 to 25 entries.
4. **"Hey, in this video, you're gonna learn:"** Five to nine emoji-led bullets, each written as a bolded capability plus a "by doing X" clause. These map one to one to the frameworks in the video.
5. **"In this video, Jack covers:"** Three paragraphs in a fixed shape: the problem, the named system, the practical implementation steps.
6. **"Who this is for:"** Exactly two personas, usually one technical and one commercial.
7. **Linked resources table.**
8. **Downloaded attachments table.**

Level 0 has only timestamps plus one link. Level 11 has no written description at all. Levels 12 and 13 follow the full structure minus the personas depth.

### What he attaches

- **Every single Level 0 through 10 lesson ships the raw transcript as a downloadable `.txt`** named after the lesson (`Level 1.txt`, `Making $$$.txt`, `Design Systems.txt`). Sizes range from 5 KB (Level 0) to 54 KB (Level 1).
- **Real working assets on four lessons only:**
  - Level 4: `NotebookLMSkill.md` (22 KB)
  - Level 5: the same NotebookLM skill, re-attached rather than cross-linked
  - Level 8: `Jupiter website.html` (31 KB, a finished example site), `outlier-research-engine.zip` (22 KB), `design-language-skill.zip` (12 KB)
- **Levels 11, 12, 13** carry the exclusive OS as a downloadable zip described in-video rather than as a repo, explicitly because a zip cannot be forked outside the community.

### What he links out to

| Category | Examples |
|---|---|
| Free GitHub repos | anthropics/skills, VoltAgent, obra/superpowers, ComposioHQ, open-design, power-design, claude-seo, ui-ux-pro-max-skill, Hermes Agent, Karpathy's Obsidian gist |
| Free tools | Claude download, view-page-source, CodePen, 21st.dev, Obsidian Web Clipper, YouTube-to-NotebookLM extension, Docker docs |
| Notion pages holding long prompts and templates | Universal CLAUDE.md Protocol and 5-8 CORE Memory System (L1), Project's Operating Manual and Pinecone Memory System (L4), soul.md Hermes template and Hermes NotebookLM Skill (L5), Level 09 Red Team Yourself (L9) |
| Affiliate or owned links | Glaido (his own startup), Firecrawl, Granola, Apify, Anymail Finder, Apollo |
| Persistent course link | "Claude Curriculum" vercel app, repeated on Levels 0, 1 and 2 |
| Owned utility | aiwithjack.com, used in Level 3 and Level 4 as both a demo of a Pinecone-backed chat and a support channel |

Level 6 and Level 10 have **no linked resources table at all**. Both are levels where the deliverable is a process rather than a tool.

### How the resources reinforce the video

- **Long prompts live in Notion, short prompts live in the description, so the video never gets paused for transcription.** Level 2's competitor-research prompt is pasted verbatim in the lesson description as a code block, and he says on camera that he grabbed it from Glaido and that you can copy it and swap the business and geography.
- **The learn-bullets are written from the framework, not the timeline.** They function as a post-watch checklist, which is why they are phrased as capabilities.
- **Attachments are for things that must be executed rather than read.** Skills as zips, a finished site as HTML, transcripts as searchable text. He does not attach slide decks, even though he mentions on camera that the deck itself was built with a Claude skill he wrote.
- **He repeats "I'll put it down below" constantly in the audio**, which converts the description from a footer into an in-video component.

---

## 6. Pacing Data

### Runtimes

**Section total: 5h 38m 36s across 14 Claude lessons.**
Levels 0 through 10 only: **5h 16m 39s across 11 lessons, mean 28m 47s.**

Arc across the ladder:

```
L0   4:34  ▏
L1  45:56  ████████████████████████
L2  35:45  ███████████████████
L3  33:46  █████████████████
L4  37:22  ███████████████████
L5  30:37  ████████████████
L6  32:56  █████████████████
L7  23:54  ████████████
L8  25:19  █████████████
L9  19:29  ██████████
L10 27:01  ██████████████
```

Bonus tier: 9:39, 5:32, 6:46.

### What the pacing implies about his format

- **Two distinct formats, not one.** A "level" is 19 to 46 minutes. A "drop" is 5 to 10 minutes. The drops (Hermes OS, Voice OS, Design OS) are proprietary-asset walkthroughs, not teaching, and they exist for retention rather than curriculum.
- **Heavily front-loaded.** Level 1 alone is 14.5 percent of the entire Claude section. Levels 1 and 2 together are 26 percent. He spends a quarter of the course before the student has any autonomy, which is a bet that setup abandonment is the real churn point.
- **Runtime declines as competence is assumed.** After the Level 4 peak, the trend is 37, 31, 33, 24, 25, 19, 27. Scaffolding thins out deliberately.
- **The hard-sell level is short.** Level 10, the monetization level, is 27 minutes with zero software. He does not pad the pitch.
- **The least fun level is the shortest.** Level 9, compliance, is 19m 29s, and he acknowledges it on camera as everybody's favorite chapter, sarcastically. He compresses the medicine.
- **He never crosses 46 minutes.** Even the setup level stops before an hour.

### Beat density (from the timestamp blocks)

| Level | Chapters | Runtime | Seconds per beat |
|---|---|---|---|
| 1 | 25 | 45m 56s | 110 |
| 2 | 19 | 35m 45s | 113 |
| 3 | 21 | 33m 46s | 96 |
| 4 | 21 | 37m 22s | 107 |
| 6 | 20 | 32m 56s | 99 |
| 8 | 22 | 25m 19s | 69 |
| 9 | 20 | 19m 29s | 58 |
| 13 | 13 | 6m 46s | 31 |

**No idea gets more than about two minutes.** The shorter the lesson, the tighter the beats. Level 9 changes topic roughly every minute for 20 straight minutes. The timestamps are granular enough to be used as a table of contents for re-watching a single 90-second step, which is exactly how people consume setup content.

---

## 7. What He Does That Most Course Creators Don't

Fourteen concrete, stealable moves.

1. **He ships the raw transcript as a downloadable file on every lesson.** Not a caption file, an attached `.txt` a student can drop into Claude. This makes the lesson searchable, re-promptable and re-usable as source material. Present on all eleven ladder lessons plus Voice OS and Design OS.

2. **He delegates install tedium to the AI on camera instead of narrating it.** Level 1 has him telling Anti-Gravity to install Claude Code and its dependencies. Level 8 has him telling Claude to run an Electron app. Level 12 has him telling the student to hand the local voice server setup back to Claude. This eliminates the "my OS looks different" support load and teaches the meta-skill in the same breath.

3. **He deliberately breaks his own working setup to teach the failure path.** In Level 1 he deletes his functioning Firecrawl connector on camera so he can demonstrate what to do when the connector you want does not exist. He then refuses to hand over the MCP URL and instead shows you how to ask a chat model to find it.

4. **He builds three versions of the same deliverable in parallel and throws two away on screen.** Level 2 runs three terminals with three different design strategies into three folders, then evaluates all three out loud and deletes two. Most creators show one build that works. This makes taste the deliverable rather than code, and it teaches parallel agents through use rather than explanation.

5. **He has the AI grade its own output, and states it as a non-negotiable.** Level 2's "act as a critically challenging individual" prompt on a fresh browser. Level 3's cross-model critic loop where Codex or Gemini reviews Claude's work. He states he never ships code without external review.

6. **He labels optional steps as optional and prices them.** Level 1 on the YouTube API, Level 2 on the OpenAI image key, Level 12 on free-local versus paid voice. Every place a student could stall on an unnecessary purchase or setup, he removes the pressure explicitly.

7. **One artifact is carried through six levels.** The Level 2 website becomes the Level 6 app, the Level 8 redesign, the Level 9 red team target and the Level 10 lead magnet. Every level upgrades something the student already owns rather than starting a new toy project.

8. **Long prompts live outside the video and he says so on camera.** The Level 2 competitor-research prompt is in the description as a copy block. Level 1's CLAUDE.md protocol, Level 4's operating manual and Pinecone system, Level 5's soul.md, and Level 9's red team prompt all live in Notion. Nobody has to pause and transcribe.

9. **He pre-normalizes failure and names the support path before anything can break.** The Start Here lessons hand over a universal troubleshooting loop up front: screenshot the problem, state the desired objective, paste it into a model, ask for a step-by-step fix. Level 11 says outright that it is completely normal for the OS not to detect a given setup.

10. **He assigns homework with a deliverable.** Level 9 tells you to red team every production repo you have with the shared prompt. Level 7 assigns a specific article to read and frames it as the highest-ROI ten to fifteen minutes of reading you will do all year.

11. **Cost is first-class curriculum, not an afterthought.** Plan choice is reframed as the cheapest employee you will ever hire. Model-selection economics get their own segment in Level 3. `/context` is taught as a monitoring habit. Spend caps get a rule in Level 9. The Design OS shows the price of a generation before you commit and tracks spend across four providers. Most AI courses never tell a student what a workflow costs to run.

12. **He gives away the working internal systems he actually uses, and quantifies the build effort.** The IG Outliers Lab in Level 10 is the tool he genuinely runs weekly. Level 8's brand extraction skill is described as two days of work. The OS lessons are described as days and days of building. Proof-of-work functions as both credibility and a demonstration of what the skills produce at the far end.

13. **He shows real friction rather than editing it out.** NotebookLM auth fails twice on camera in Level 4 and he retries. Level 2 stalls on DNS propagation and he says so and moves on. Level 8 admits a video generation took four or five attempts and shows the bad ones bugging out.

14. **Every close names the next level's specific payoff, often with a visual teaser rather than a topic list.** Level 7 ends by showing a finished design-system website and pointing out it was one-shot, which is the entire argument for watching Level 8.

---

## Gaps and Things Not Present in the Material

Stated explicitly so nothing here is inferred as fact:

- **No quizzes, worksheets, checklists, templates-to-fill, or submitted assignments** anywhere in the Claude section. There are exactly two verbal homework items: read the High Agency article (Level 7) and red team your production repos (Level 9).
- **No slide decks are attached**, despite the decks being visible in every lesson and Jack stating in Level 8 that the deck was generated by a Claude skill he built.
- **Level 11 (Claude Code + Hermes OS) has no written description at all.** Its transcript was recovered from video captions, not attached by Jack.
- **Levels 6 and 10 have no linked resources table.**
- **The two Start Here lessons are not an intro to the Claude section.** Both explicitly welcome the viewer to "chapter two" on AI automations, and both discuss Anti-Gravity and n8n as the two technologies to be learned. They belong to a wider course structure, not to the Claude ladder.
- **The "BLAST framework" named in Level 6's audio is never developed on camera**, unlike BALLAST in Level 1. Whether these are the same framework is not resolved in the material.
- **No prerequisites list, no up-front total runtime disclosure to students, and no completion certificate** appear anywhere.
- **There is no watch-time, completion-rate, or drop-off data** in these files. All pacing analysis above comes from the `Video length` field in each README, nothing more.

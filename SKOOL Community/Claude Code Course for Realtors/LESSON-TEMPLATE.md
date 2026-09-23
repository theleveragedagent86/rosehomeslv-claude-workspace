# Lesson Description Template

The 9-block structure that goes under every video in Skool. Same order, every level, no exceptions. Reverse-engineered from Jack Roberts' lesson descriptions, rewritten for this course.

The point of a fixed template is that after two lessons a student knows exactly where to look for the timestamp they want, and Ryan never has to decide what a description should contain.

---

## The blocks, in order

### 1. Launch date

```
📆 Launch date: 14th September 2026
```

One line. Signals the course is alive and being added to. Skip it on Level 0.

### 2. Slide image

One to three images pulled straight from the deck, embedded at the very top, before any text. Always the framework diagram for that level, never a decorative stock photo. This is the thing that shows in the Skool feed preview, so it is doing double duty as a thumbnail.

### 3. Inline copyable content (only when short)

The actual prompt, template or checklist, pasted as text so a student can copy it without watching. **Short prompts go here. Long prompts go in an attached `.md` and get linked in block 8.** Nobody should ever pause the video to transcribe.

### 4. Timestamps

```
⏱️ Timestamps
00:00 – Welcome & What You're Building
02:15 – Why Your Farm Data Belongs in the Brain
...
```

- 15 to 25 entries per level.
- Format is `MM:SS – Title Case Beat Name`, en dash, not a hyphen.
- Target 60 to 115 seconds per entry. If a gap runs past two minutes, the beat is too big, split it.
- Granular enough that a student can re-watch one 90-second step without hunting. This is how setup content is actually consumed.

### 5. `Hey, in this video, you're gonna learn:`

Five to nine bullets. Each one is built the same way:

> **emoji** + **bolded capability, phrased as an action** + a `by/using/to [mechanism]` clause + the payoff

Example, correct:

> 🗂️ **Build Your Business Brain in Under 10 Minutes** by creating five to eight thematic folders on your desktop with a `CLAUDE.md` in each, so Claude stops asking who you are every single session.

Example, wrong:

> 🗂️ **Folder Structure** - we'll go over how to organize your files.

Rules:
- **Capability, never topic.** "Build X so you can Y", not "an overview of X".
- Write them from the framework, not the timeline. They are a post-watch checklist, not a summary.
- The mechanism clause is what makes it feel specific instead of like marketing.

### 6. `In this video, Ryan covers:`

Exactly three paragraphs, fixed shape. Do not add a fourth.

1. **The problem, named as an enemy.** Not "we'll talk about memory" but the specific thing that is costing them. Every level has one and it should be stated in the first two minutes of the video too.
2. **The system, named and bolded.** Give it a name they can repeat to another agent. `**The Business Brain**`, `**The One-Command Launch**`, `**The Four Permission Tiers**`.
3. **The practical implementation steps.** Concrete nouns. What folders, what files, what tools, in what order.

### 7. `Who this is for:`

Exactly two personas, each with a bolded lead-in. One should be the working agent, one should be the team lead or the agent building something bigger. Two, not three, not five.

```
- **Solo agents doing 6 to 20 deals a year** who are the marketing department, the TC and the showing agent, and need the admin half of that to run without them.

- **Team leads and rainmakers** who want a system their agents can actually run, not another tool nobody logs into.
```

### 8. Resources

Every link gets an emoji prefix. Group them loosely: free tools, then templates, then anything of Ryan's.

```
| Resource | Link |
|---|---|
| 🧠 Business Brain Starter Kit | ... |
| 📄 CLAUDE.md Template | ... |
```

### 9. Attachments

**Every single level ships its raw transcript as a downloadable `.txt`**, named after the level (`Level 1.txt`). This is the single highest-leverage habit in Jack's whole setup: it makes the lesson searchable and re-promptable, and students drop it straight into Claude.

Beyond the transcript, attach only things that must be **executed**, not read. Skills, prompt packs, templates, starter folders. Do not attach the slide deck.

---

## The two rules underneath the template

**Long prompts live outside the video.** Attached `.md` or linked. The video never gets paused for transcription.

**Say "I'll put it down below" on camera, constantly.** That single line converts the description from a footer nobody reads into a component of the lesson. It is the reason the template is worth filling out properly.

---

## Blank template, copy this

```markdown
📆 Launch date: [DATE]

![framework-slide](image.png)

[Optional: short copyable prompt or checklist]

⏱️ Timestamps
00:00 – [Beat]
00:00 – [Beat]

#### Hey, in this video, you're gonna learn:

[emoji] **[Capability as an action]** by [mechanism], so [payoff].

[emoji] **[Capability as an action]** by [mechanism], so [payoff].

#### In this video, Ryan covers:

[The problem, named as an enemy, and what it costs them.]

[The system, **named and bolded**, and what it does.]

[The practical implementation steps, in order, with concrete nouns.]

#### Who this is for:

- **[Persona 1, the working agent]** who [situation] and needs [outcome].

- **[Persona 2, the builder or team lead]** who [situation] and wants [outcome].
```

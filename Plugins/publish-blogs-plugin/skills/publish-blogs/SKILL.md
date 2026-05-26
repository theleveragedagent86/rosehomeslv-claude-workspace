---
name: publish-blogs
description: Use when someone asks to post, publish, or upload blog posts to Lofty, the Lofty CMS, or the Rose Homes LV website. Can automatically publish via browser automation in Cowork or output a manual checklist in CLI mode.
argument-hint: "file path, folder, or blog number"
---

## What This Skill Does

Publishes blog post content to the Lofty CMS using a multi-agent team that ensures every field is entered correctly before publishing. When browser tools are available (Claude Cowork), agents handle browser automation with built-in verification. When no browser tools are available (Claude Code CLI), it outputs a step-by-step copy-paste checklist.

**Website:** www.rosehomeslv.com
**Blog Index:** www.rosehomeslv.com/blogs
**Lofty CMS Blog Dashboard:** https://cms.lofty.com/cmsnew/blog

**Supporting files in this skill directory:**
- [prep-agent.md](prep-agent.md) — Prep Agent instructions (data extraction and validation)
- [publisher-agent.md](publisher-agent.md) — Publisher Agent instructions (browser automation with field verification)
- [qa-agent.md](qa-agent.md) — QA Agent instructions (full audit before publishing)

---

## Architecture

You are the **Manager**. You orchestrate three specialized agents:

1. **Prep Agent** (1 instance per session) — Reads all blog files and SEO packages, validates every field is present, and returns structured post data. Catches missing data before we touch the browser.
2. **Publisher Agents** (up to 3 parallel per wave) — Each opens its own browser tab, enters data into Lofty field by field with verification after each field. Does not move to the next field until the current one is confirmed correct.
3. **QA Agents** (1 per post, up to 3 parallel per wave) — After all fields are entered, walks through the post's tab and verifies every field matches the expected data. Reports pass or fail with specifics.

**Parallel publishing:** Posts are processed in waves of up to 3 posts at a time. Each Publisher Agent works in its own dedicated browser tab simultaneously. After all Publishers in a wave finish, QA Agents verify all posts in the wave in parallel. This cuts publishing time by up to 3x.

**You never interact with the browser yourself.** You orchestrate, pass data between agents, and make publish/fix decisions based on QA results.

---

## Workflow

### Step 0: Initialize

Determine what to publish from `$ARGUMENTS` or the conversation:

- **If a folder name is given** (e.g., "Green Valley"): Look for blog files in `/Users/ryanrose/Downloads/Claude/Claude Blogs/[folder name]/`
- **If a file path is given**: Read that specific file
- **If a blog number or range is given** (e.g., "start with post 36"): Find the matching files in the specified folder
- **If blog content is already in the conversation** (e.g., from a blog-writer session): Use that content directly
- **If unclear**: Ask the user what to publish

**Check if browser tools are available** (navigate, click, type, screenshot, javascript_tool, or computer use tools). If yes, use **Mode A** (agents). If no, use **Mode B** (manual checklist — skip to the Mode B section at the bottom).

---

### Step 1: Spawn Prep Agent

Read the file `prep-agent.md` from this skill directory.

Use the **Agent tool** to spawn a single `general-purpose` sub-agent:

```
You are a Prep Agent for the publish-blogs system.

[FULL CONTENTS OF prep-agent.md]

=== FILES TO PROCESS ===

[List of blog file paths and SEO package file paths to read]

=== COMMUNITY NAME ===

[The neighborhood/community name for the Category field]

Extract and validate all post data. Return the structured output for every post.
```

Wait for the Prep Agent to complete. Store its output as `PREP_DATA`.

**If the Prep Agent reports any MISSING or INVALID fields:** Stop and show the user what's missing. Do not proceed until all data is complete.

**If all posts pass validation:** Display a brief summary (post count, titles) and immediately proceed to Step 2.

---

### Step 2: Publish Posts in Parallel Waves

Process posts in waves of up to 3 posts at a time. Each Publisher Agent works in its own browser tab simultaneously.

Read the files `publisher-agent.md` and `qa-agent.md` from this skill directory. Store their contents for reuse across all waves.

#### 2a: Spawn Publisher Agents (parallel)

For each post in the current wave (up to 3), spawn a Publisher Agent using the Agent tool. **Spawn ALL publishers for the wave in a single response** (parallel Agent tool calls):

```
You are a Publisher Agent for the publish-blogs system.

[FULL CONTENTS OF publisher-agent.md]

=== TAB ASSIGNMENT ===

You are Publisher [1/2/3] in this wave. Open a NEW browser tab for your work.
Tab label: "Post [N] - [short title]"

=== POST DATA ===

Title: [exact title]
HTML Body: [full prepared HTML — no H1, no JSON-LD]
Slug: [exact slug]
Category: [community name]
Meta Title: [exact meta title]
Meta Keywords: [exact keywords]
Meta Description: [exact meta description]

Open a new browser tab, navigate to Lofty, create a new post, and enter all fields. Verify each field after entering it. Do NOT click Post Now — the QA Agent will verify first.
```

Wait for ALL Publisher Agents in the wave to complete.

**If any Publisher Agent reports field entry failures:** Spawn a new Publisher Agent for just that post's failed fields. Allow up to 2 retries per field.

#### 2b: Spawn QA Agents (parallel)

After all Publishers in the wave finish, spawn QA Agents for all posts in the wave simultaneously. **Spawn ALL QA agents in a single response:**

```
You are a QA Agent for the publish-blogs system.

[FULL CONTENTS OF qa-agent.md]

=== TAB ASSIGNMENT ===

Switch to the browser tab labeled "Post [N] - [short title]" to verify this post.

=== EXPECTED DATA ===

Title: [exact title]
Slug: [exact slug]
Category: [community name]
Meta Title: [exact meta title]
Meta Keywords: [exact keywords]
Meta Description: [exact meta description]

The Publisher Agent has entered all fields in this tab. Verify every field matches the expected data exactly. Report pass or fail for each field.
```

Wait for ALL QA Agents to complete.

#### 2c: Process QA Results

For each post in the wave:

**If QA passes (all fields correct):**
- Spawn a Publisher Agent to switch to that post's tab and click **Post Now**
- If a confirmation dialog appears, click **OK**
- Verify the post published (look for success message or return to blog list)
- Handle slug conflicts if Post Now silently fails (see Slug Conflict Handling below)
- Report: **"Published [X]/[total]: [Post Title]"**

**If QA fails (one or more fields wrong):**
- Spawn a new Publisher Agent to switch to that post's tab and fix ONLY the failed fields
- Then spawn a QA Agent to re-verify that post
- Allow up to 2 QA cycles per post
- If still failing after 2 cycles, pause and ask the user for help

**Post Now agents for passing posts can be spawned in parallel** — up to 3 at a time.

#### 2d: Wave Complete — Continue

After all posts in the wave are published:

1. Display a wave progress summary:
```
Wave [X] complete: Published [N] posts (posts [start]-[end])
Total progress: [completed]/[total] posts
```

2. **Immediately proceed to the next wave.** Do NOT ask the user for permission.

3. Close completed tabs if the browser has too many open (more than 6 tabs).

---

### Step 3: Final Report

After all posts are published, display:

```
All done! Published [total] posts:
1. [Title 1] — slug: [slug1]
2. [Title 2] — slug: [slug2]
...

All fields verified by QA before publishing.
```

---

## Slug Conflict Handling

If clicking "Post Now" has no visible effect (no success message, no error, page stays the same), the slug already exists.

1. Click the **Settings** tab
2. Click the URL Slug field, press **Ctrl+A**
3. Retype the slug with `1` appended (e.g., `luxury-homes-green-valley` becomes `luxury-homes-green-valley1`)
4. Click **Post Now** again
5. If still no effect, try `2`, then `3`, and so on up to `5`
6. If all fail, pause and ask the user

---

## Mode B: Manual Checklist (CLI, no browser)

When browser tools are not available, output a clearly formatted checklist for each post.

The Prep Agent still runs to extract and validate all data. Then output:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PUBLISH: [Post Title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ ] 1. Click "+ Add New" to create a new blog post

[ ] 2. TITLE FIELD — paste:
[exact title text]

[ ] 3. SOURCE CODE HTML — click the </> icon, then paste:
[full HTML body — no H1, no JSON-LD]

[ ] 4. Click SAVE in the source code modal

[ ] 5. Click the SETTINGS tab, then set:
    URL Slug (Ctrl+A first): [slug]
    Category: [neighborhood name]

[ ] 6. Click the SEO tab, then for each field:
    (Use Ctrl+A to select all text before typing/pasting)

    Meta Title — paste:
    [meta title]

    Meta Keywords — paste:
    [keywords]

    Meta Description — paste:
    [meta description]

[ ] 7. REVIEW all fields before publishing:
    - Click Content tab: verify title and body
    - Click Settings tab: verify slug and category
    - Click SEO tab: verify meta title, keywords, description

[ ] 8. Click POST NOW to publish

[ ] 9. If a confirmation dialog appears, click OK

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

After the checklist, include:

> **If nothing happens when you click Post Now:** The URL slug already exists.
> Append `1` to the end of the slug (e.g., `southern-highlands-parks` becomes `southern-highlands-parks1`) and try again.

If publishing a batch:
- Output the checklist for Post 1 first
- After the checklist, ask: "Ready for Post 2?"
- Continue one at a time until all posts are published

---

## Error Handling

- **Prep Agent finds missing data:** Stop and report to user. Never publish with incomplete data.
- **Publisher Agent can't enter a field:** Retry up to 2 times. If still failing, report to user.
- **QA Agent finds mismatches:** Re-enter failed fields and re-verify. Max 2 cycles per post.
- **Login required:** Pause and ask the user to log in, then resume.
- **Post Now silently fails:** Slug conflict — append number and retry.
- **Page unresponsive:** Navigate back to dashboard and start the post over.

---

## Browser Automation Notes

- **Ctrl+A before typing/pasting** into any field that has default content. Lofty pre-fills SEO fields with template variables that must be fully replaced.
- **The source code editor is a modal.** You must click Save inside the modal before it closes. Do not try to interact with Settings or SEO tabs while the modal is open.
- **Settings and SEO are tabs** on the same page as the post editor. They do not navigate away.
- **After publishing**, the page returns to the blog list.

---

## File Naming Conventions

Blog files may use either naming pattern:
- `post[N]-[slug].html` (from blog-writer skill)
- `blog-[N]-[topic].html` (legacy format)

SEO packages may use either naming pattern:
- `seo-package-batch[N].md` (from blog-writer skill)
- `seo-package-batch-[N].txt` (legacy format)

The Prep Agent handles both formats automatically.

---

## Notes

- The HTML body must NOT contain the `<h1>` title tag — Lofty adds this from the Title field
- The HTML body must NOT contain `<script type="application/ld+json">` blocks
- Category = the neighborhood/community name (e.g., "Summerlin", "Henderson", "Green Valley")
- Blog files are stored in `/Users/ryanrose/Downloads/Claude/Claude Blogs/[Community Name]/`
- SEO packages are stored alongside blog files

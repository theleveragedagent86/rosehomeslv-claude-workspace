---
name: ig-engage
description: Use when someone asks to engage on Instagram, comment on Instagram posts, run Instagram engagement, do daily Instagram routine, or comment on Vegas Instagram accounts.
model: sonnet
---

## What This Skill Does

Automates daily Instagram community engagement for Ryan Rose's personal brand. Visits target Vegas local accounts, comments on posts, likes posts and top comments, and replies to top comments. The goal is brand awareness through genuine community participation, not self-promotion.

**Supporting files on disk (read these at session start):**
- `/Users/ryanrose/.claude/skills/ig-engage/target-accounts.md` -- curated account list
- `/Users/ryanrose/.claude/skills/ig-engage/comment-guidelines.md` -- writing rules, tone, examples
- `/Users/ryanrose/.claude/skills/ig-engage/CLAUDE.md` -- detailed browser automation playbook

---

## Writing Rules -- NON-NEGOTIABLE

These apply to EVERY comment and reply without exception:

1. **NO EM-DASHES EVER.** Not one. Use commas, periods, or "and" instead.
2. **Natural and conversational.** Sound like a real person, not a bot or a brand.
3. **Never self-promote.** Never mention Rose Homes LV, real estate services, or any business.
4. **Never salesy.** No pitches, no CTAs, no "DM me for details."
5. **Adaptive tone.** Match the energy and vibe of the post you are commenting on.
6. **Keep it short.** 1-3 sentences for comments. Instagram is not Reddit.
7. **Vegas-specific when relevant.** Use neighborhood names, local details, insider tips.
8. **Genuine value.** Every comment should add something: a local tip, helpful info, genuine compliment, or shared experience.

---

## Content Guardrails -- SKIP THESE ENTIRELY

Before engaging with any post, screen the caption and context. **SKIP the post entirely** (no likes, no comments, nothing) if it touches:

- **Political content:** Elections, political figures, policy debates, left vs right, government criticism or praise
- **LGBTQ+ content:** Any LGBTQ+ topics, Pride events, related discussions
- **Highly controversial or divisive subjects:** Culture war topics, heated social debates
- **Religious content that could be polarizing**

**When in doubt, skip.** It is always better to skip a post than to engage with something that could be misread. Move to the next post silently.

---

## Session Start Checklist

1. Read `/Users/ryanrose/.claude/skills/ig-engage/target-accounts.md` for the current account list
2. Read `/Users/ryanrose/.claude/skills/ig-engage/comment-guidelines.md` for writing guidance
3. Detect browser tools availability:
   - Check for: `navigate`, `click`, `type`, `screenshot`, `browser_navigate`, `browser_click`, `browser_type`, `browser_snapshot`, `javascript_tool`, or computer use tools
   - If any browser tools found: **Mode A (Full Automation)**
   - If no browser tools found: **Mode B (Manual Checklist)**
4. Proceed with the appropriate mode below

---

## Mode A -- Full Automation

### Step 1: Open Instagram

1. Navigate to `https://www.instagram.com`
2. Verify you are logged in (look for profile icon, home feed, or username in the navigation)
3. If not logged in, **pause** and tell the user: "Please log into Instagram. Let me know when you're ready."

### Step 2: Pick Target Accounts

1. Read target-accounts.md
2. Select 10 accounts for this session
3. Rotate accounts across sessions so you do not visit the same ones every day
4. Prioritize high-priority accounts first, then fill remaining slots from standard rotation
5. If `$ARGUMENTS` specifies an account or number, use that instead

### Step 3: Engage on Recent Posts

**Target: 20-40 posts total across all selected accounts.**

For each target account:
1. Navigate to their profile page (`https://www.instagram.com/[handle]/`)
2. Open their most recent posts one by one

For each post:

**a. Screen the content**
- Read the post caption and any visible context
- Apply the guardrails above
- If flagged: skip entirely, move to next post

**b. If safe, engage in this order:**

1. **Like the post** (click the heart icon)
2. **Scroll to comments and read the top 10-15 visible comments**
3. **Like the top 5-10 comments** (click heart on each)
4. **Write and post a value-add comment:**
   - Read the post caption carefully
   - Write a 1-3 sentence comment that adds genuine value
   - Match the tone of the post (see comment-guidelines.md for examples)
   - Type the comment in the comment box and submit
   - Verify the comment appears
5. **Reply to 1-2 comments** on every post with an active comment section
   - This is a standard part of engagement, not optional
   - Look for comments asking questions, sharing opinions, or making observations worth responding to
   - Keep replies to 1-2 sentences. Match the tone of the original commenter.
   - Target: at least 1 reply per post (aim for replies on 75%+ of posts engaged)
   - Only skip replies if the comment section is empty, disabled, or there is truly nothing worth responding to
   - Click "Reply" under the comment, type your reply, submit
   - Verify the reply appears

**c. Pacing**
- Wait 5-15 seconds between each action (like, comment, reply)
- This mimics natural human behavior and avoids rate limits

**d. Report after each post:**
```
Post [X]/[total] engaged
Account: @[handle]
Topic: [brief description]
Comment: "[what you wrote]"
Reply: "[reply text, or 'none' if skipped with reason]"
```

### Step 4: Summary Report

After the session, output:
```
Session complete:
- Accounts visited: [X]
- Posts engaged: [Y]
- Posts skipped (guardrails): [Z]
- Comments posted: [A]
- Replies posted: [B]
- Likes given: [C] (posts + comments)
```

---

## Mode B -- Manual Checklist

If no browser tools are available, output a checklist the user can follow manually:

1. List the 10 target accounts for today (rotated from the full list)
2. For each account:
   - Visit their profile
   - Open 3-5 recent posts
   - For each post: like the post, like top comments, leave a value-add comment, and reply to 1-2 comments in the thread
3. Remind the user of the guardrails (skip political, LGBTQ+, controversial)
4. Include 2-3 example comments for different post types (food, events, scenic)
5. Target: 20-40 posts total, with replies on at least 75% of posts

---

## Browser Automation Notes

### Instagram Comment Box
- Look for the comment input field (usually a textarea or contenteditable div near the bottom of the post)
- If the comment box says "Add a comment..." click it to activate
- Type the comment text, then press Enter or click the "Post" button
- Verify the comment appears in the comment section after posting

### Instagram Like Button
- Heart icon on the post itself (below the image/video)
- Small heart icon next to each comment
- Click to toggle. Verify the heart turns red/filled.

### Navigation
- Profile pages: `https://www.instagram.com/[handle]/`
- Individual posts: Click on the post thumbnail from the profile grid
- Back to profile: Use browser back or navigate directly

### Common Issues
- **Rate limiting:** If Instagram shows "Try Again Later" or similar, stop immediately. Report to user and end session.
- **Login expired:** If redirected to login page, pause and ask user to log in.
- **Comments disabled:** Some posts have comments turned off. Skip these.
- **Private accounts:** Cannot engage with private accounts. Skip and move to next.

---

## Important Rules

- **NEVER use em-dashes in any comment or reply.** Use commas, periods, or "and".
- **NEVER mention Rose Homes LV or real estate services** in any comment.
- **NEVER comment on political, LGBTQ+, or controversial posts.** Skip them entirely.
- **ALWAYS verify** that comments and replies were actually posted before moving on.
- **ALWAYS wait 5-15 seconds** between actions to avoid rate limits.
- **ALWAYS adapt your tone** to match the post you are commenting on.

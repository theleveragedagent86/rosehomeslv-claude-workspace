---
name: responder-comments
description: Use when someone asks to engage on first responder Instagram posts, run the daily community presence routine, comment on Vegas military/police/fire/healthcare worker posts, or build community relationships with Las Vegas first responders.
model: sonnet
disable-model-invocation: true
---

## What This Skill Does

Automates daily Instagram community presence engagement for Brian Esposito with first responders in Las Vegas, Henderson, and Clark County. Visits target accounts (military, veterans, police, fire/EMS, healthcare), likes posts and top comments, and writes warm, genuine 1-2 sentence community-presence comments. The goal is building authentic neighbor-level relationships in the Vegas first responder community, NOT recruiting clients or pitching mortgages.

This skill operates @espohomeloans on the same daily volume as the lender-comments skill (10-25 posts per session). The two skills together should not exceed roughly 30 posts/day combined to stay under Instagram's natural-engagement thresholds.

**Supporting files (read these at session start):**
- `./skills/responder-comments/target-accounts.md` -- curated first responder target list
- `./skills/responder-comments/references/comment-guidelines.md` -- writing rules, tone, examples
- `./skills/responder-comments/references/browser-playbook.md` -- detailed browser automation playbook

---

## The Goal: Community Presence, Not Conversion

This skill is fundamentally different from `lender-comments`. The goal here is NOT to pitch, recruit, or convert. The goal is for Brian to show up as a recognizable community member who genuinely appreciates first responders. The implicit business benefit (top-of-mind when they need a VA loan or hero program someday, or when their family asks for a referral) is downstream and indirect. **Never reach for it in a comment.**

Brian's community credibility comes from:
- 28+ years in Las Vegas
- Founder of Par for the Cure ($1.6M+ raised over 20 years for breast cancer research)
- Former PGA TOUR / TPC Head Golf Pro
- Community member, not service provider

---

## Writing Rules -- NON-NEGOTIABLE

These apply to EVERY comment and reply without exception:

1. **NO EM-DASHES EVER.** Not one. Use commas, periods, or "and" instead.
2. **Maximum 2 sentences.** 1-2 sentences, hard cap. If you can say it in one sentence, use one.
3. **Never mention being a lender or mortgages.** Never. Not subtle, not implicit, not through Nations Lending. This is community presence, not lead generation.
4. **Never self-promote.** No "DM me," "follow me," "check me out," no CTAs of any kind.
5. **Never pitch services.** This includes VA loans, hero programs, first-time buyer products, anything mortgage-related.
6. **Genuine gratitude, never performative.** "Thank you for your service" is fine when sincere. Avoid empty phrases.
7. **Neighbor voice, not service voice.** Speak as a 28-year Vegas community member, not as a business professional.
8. **Vegas-specific when relevant.** Reference local context (department names, neighborhoods, local events) authentically.
9. **Acknowledge specifics.** If they posted about a specific call, training, or person, reference it. Generic comments fall flat.
10. **Warm but understated.** Match their tone. A line-of-duty memorial post is not the place for emoji.

---

## Content Guardrails -- SKIP THESE ENTIRELY

Before engaging with any post, screen the caption and context. **SKIP the post entirely** (no likes, no comments, nothing) if it touches:

- **Political content:** Police reform debates, military policy, immigration enforcement debates, election content, partisan framing
- **LGBTQ+ content:** Pride events, related discussions
- **Highly controversial or divisive subjects:** Use of force debates, vaccine mandates, mask debates, etc.
- **Religious content that could be polarizing**
- **Active line-of-duty death / officer down posts:** Skip entirely. Not a place for an outsider's comment unless Brian personally knew them. The risk of looking opportunistic is too high.
- **Active critical incident posts:** Active shooter, mass casualty events. Wait until the incident is fully resolved and the department has posted official messaging.
- **Negative or venting posts:** Posts complaining about the public, the department, the job. Not a place to engage.
- **Posts under 2 hours old with no engagement:** Wait for organic activity.

**Special note on patriotic content:** Memorial Day, Veterans Day, 9/11 anniversaries, and similar are GOOD posts to engage on if the framing is genuine remembrance, not partisan. If a post references "real Americans," "the left," or political framing, skip it.

**When in doubt, skip.** The downside of a misread comment from a mortgage lender on a first responder post is significant. Move silently to the next post.

---

## Engagement Themes (what types of posts are best)

These are the posts where Brian's voice fits most naturally:

- **Community service / outreach:** Toys for Tots, food drives, school visits, community events
- **Routine on-duty content:** Training drills, equipment maintenance, K9 highlights, calls handled professionally
- **Personal milestones:** Promotions, retirements, graduation from academy, work anniversaries
- **Charity / giving back:** Department fundraisers, local nonprofits, hero programs, fallen-officer memorial fundraisers
- **Family / human-side content:** Kids visiting the firehouse, dog adoptions from K9 program, personal stories
- **Patriotic remembrance (non-political framing):** Memorial Day genuine remembrance, Flag Day, 9/11 anniversaries with respectful framing
- **Local Vegas community pride:** Posts about specific neighborhoods, community events, mutual aid

---

## Session Start Checklist

1. Read `./skills/responder-comments/target-accounts.md` for the current account list
2. Read `./skills/responder-comments/references/comment-guidelines.md` for writing guidance
3. Detect browser tools availability:
   - Check for: `browser_navigate`, `browser_click`, `browser_type`, `browser_snapshot`, or similar Playwright MCP tools
   - If browser tools found: proceed with automation below
   - If no browser tools found: **STOP.** Tell the user: "Playwright MCP is not connected. Check the plugin's MCP configuration or see the setup guide in references/playwright-setup.md."
4. Proceed with automation

---

## Automation Flow

### Step 1: Open Instagram

1. Navigate to `https://www.instagram.com`
2. Verify you are logged in as @espohomeloans
3. If not logged in, **pause** and tell the user: "Please log into Instagram. Let me know when you're ready."

### Step 2: Pick Target Accounts

1. Read target-accounts.md
2. Select 3-5 accounts for this session
3. Rotate accounts across sessions so you do not visit the same ones every day
4. Aim for variety: mix at least 2 different responder categories per session (e.g., not all police)
5. If `$ARGUMENTS` specifies an account or number, use that instead

### Step 3: Engage on Recent Posts

**Target: 10-25 posts total across all selected accounts.** Combined with `lender-comments` daily run, total Instagram engagement should stay around 30 posts/day.

For each target account:
1. Navigate to their profile page (`https://www.instagram.com/[handle]/`)
2. Open their most recent posts one by one (3-6 posts per account)

For each post:

**a. Screen the content**
- Read the post caption and any visible context
- Apply the guardrails above. First responder posts trip guardrails more often than LO posts. Be liberal with skipping.
- If flagged: skip entirely, move to next post

**b. If safe, engage in this order:**

1. **Like the post**
2. **Read the top 10-15 visible comments** (do NOT auto-like all of them like the lender skill does, since responder posts have a wider tonal range. Only like comments that are clearly aligned with the post tone.)
3. **Like 3-5 of the most genuine top comments** (lower than lender skill's 5-10)
4. **Write and post a 1-2 sentence community-presence comment:**
   - Read the post caption carefully
   - Acknowledge something specific
   - Match the tone (somber for memorials, warm for milestones, casual for routine content)
   - Type the comment in the comment box and submit
   - Verify the comment appears
5. **Reply to 1 top comment maximum** — only if you have something genuinely additive. Replying on first responder posts is high-risk; default is no reply.

**c. Pacing**
- Wait 5-15 seconds between each action
- Wait 10-20 seconds between posts
- Wait 30-60 seconds between accounts

**d. Report after each post:**
```
Post [X]/[total] engaged
Account: @[handle] ([category])
Topic: [brief description]
Comment: "[what you wrote]"
```

### Step 4: Save Session Log

Save a markdown log to `output/responder-comments/YYYY-MM-DD.md`:

```markdown
# Responder Comments Session -- [date]

## Summary
- Accounts visited: [X]
- Posts engaged: [Y]
- Posts skipped (guardrails): [Z]
- Comments posted: [A]
- Replies posted: [B]
- Likes given: [C]

## Detail

### @[handle] -- [category]
1. **Post:** [brief description]
   - Comment: "[what you wrote]"
   - Skipped: [no, or reason]
```

### Step 5: Print Summary

```
Session complete:
- Accounts visited: [X]
- Posts engaged: [Y]
- Posts skipped (guardrails): [Z]
- Comments posted: [A]
- Replies posted: [B]
- Likes given: [C]
- Log saved: output/responder-comments/YYYY-MM-DD.md
```

---

## Rate Limit Protocol

If Instagram shows any of these, **STOP THE SESSION IMMEDIATELY:**
- "Try Again Later"
- "Action Blocked"
- Comments fail to post multiple times
- Redirected to a "verify your identity" page
- Page refreshes unexpectedly

Save progress to the daily log, report to Brian, and do not continue. Wait at least 24 hours before the next session.

---

## Important Rules

- **NEVER use em-dashes** in any comment or reply.
- **NEVER mention mortgages, lending, Nations Lending, or any business** in any comment.
- **NEVER pitch VA loans, hero programs, or any product** even when the post directly relates.
- **NEVER use phrases that sound like a service provider** ("happy to help," "let me know if I can assist").
- **ALWAYS skip line-of-duty death posts** unless Brian personally knew them.
- **ALWAYS skip political/controversial posts** even when from target accounts.
- **ALWAYS verify** comments and replies posted before moving on.
- **ALWAYS save the session log** before ending, even if cut short.

---
name: lender-comments
description: Use when someone asks to engage on competitor lender Instagram posts, run the daily IG engagement routine, comment on Vegas mortgage loan officer posts, or execute the value-provided marketing routine.
model: sonnet
disable-model-invocation: true
---

## What This Skill Does

Automates daily Instagram engagement for Brian Esposito's recruiting brand. Visits target competitor mortgage loan officer accounts in Las Vegas, Henderson, and Clark County, likes posts and top comments, writes value-add comments, and optionally replies to top comments. The goal is name recognition with competitor LOs through genuine value, not self-promotion. Brian is a Branch Manager at Nations Lending (NMLS #1535781).

**Supporting files (read these at session start):**
- `./skills/lender-comments/target-accounts.md` -- curated LO target list
- `./skills/lender-comments/references/comment-guidelines.md` -- writing rules, tone, examples
- `./skills/lender-comments/references/browser-playbook.md` -- detailed browser automation playbook

---

## Writing Rules -- NON-NEGOTIABLE

These apply to EVERY comment and reply without exception:

1. **NO EM-DASHES EVER.** Not one. Use commas, periods, or "and" instead.
2. **Natural and conversational.** Sound like a real industry peer, not a bot or a brand.
3. **Never self-promote.** Never mention Nations Lending, Brian's branch, recruiting, "join my team," "DM me," "check me out," or "follow me."
4. **Never salesy.** No pitches, no CTAs, no calls to action of any kind.
5. **Never bash competitors.** Never criticize or undermine the lender or their company.
6. **Never quote rates or pricing.** No specific interest rates, APRs, or pricing claims. Compliance risk.
7. **Warm professional peer crossed with mentor.** Confident industry insight with approachable, encouraging energy.
8. **Maximum 2 sentences.** 1-2 sentences, hard cap. Lead with insight or a real question, not generic praise. If you can say it in one sentence, use one.
9. **Vegas-specific when relevant.** Use neighborhood names, local market details, insider knowledge.
10. **Genuine value.** Every comment should add something: mortgage insight, market context, leadership perspective, or shared experience.

---

## Content Guardrails -- SKIP THESE ENTIRELY

Before engaging with any post, screen the caption and context. **SKIP the post entirely** (no likes, no comments, nothing) if it touches:

- **Political content:** Elections, political figures, policy debates, left vs right, government criticism or praise
- **LGBTQ+ content:** Any LGBTQ+ topics, Pride events, related discussions
- **Highly controversial or divisive subjects:** Culture war topics, heated social debates
- **Religious content that could be polarizing**
- **Posts quoting specific interest rates or APRs:** Compliance risk if Brian responds with numbers
- **Posts from Nations Lending colleagues:** Exclude all Nations Lending accounts entirely
- **Negative or venting posts:** Posts where commenting could backfire or look opportunistic
- **Posts less than 2 hours old with no engagement:** Wait for organic activity first

**When in doubt, skip.** It is always better to skip a post than to engage with something that could be misread. Move to the next post silently.

---

## Value Theme Rotation

Pick whichever theme fits the post naturally. Do not force a theme that does not match:

- **Loan product expertise:** DPA, VA (especially breaking the myth of VA lending), FHA, bond programs, niche products
- **Team culture and leadership:** Coaching LOs, building a team, branch culture, mindset, the daily grind
- **Vegas market knowledge:** Neighborhoods, inventory trends, Henderson vs Summerlin vs North Las Vegas dynamics
- **Client service philosophy:** Communication, closing on time, borrower experience, referral partnerships
- **Golf credibility:** When relevant, Brian is a former PGA TOUR / TPC Head Golf Pro. Use naturally, never force it.

---

## Session Start Checklist

1. Read `./skills/lender-comments/target-accounts.md` for the current account list
2. Read `./skills/lender-comments/references/comment-guidelines.md` for writing guidance
3. Detect browser tools availability:
   - Check for: `browser_navigate`, `browser_click`, `browser_type`, `browser_snapshot`, or similar Playwright MCP tools
   - If browser tools found: proceed with automation below
   - If no browser tools found: **STOP.** Tell the user: "Playwright MCP is not connected. Check the plugin's MCP configuration or see the setup guide in references/playwright-setup.md."
4. Proceed with automation

---

## Automation Flow

### Step 1: Open Instagram

1. Navigate to `https://www.instagram.com`
2. Verify you are logged in (look for profile icon, home feed, or username in the navigation)
3. If not logged in, **pause** and tell the user: "Please log into Instagram. Let me know when you're ready."

### Step 2: Pick Target Accounts

1. Read target-accounts.md
2. Select 3-5 accounts for this session
3. Rotate accounts across sessions so you do not visit the same ones every day
4. If `$ARGUMENTS` specifies an account or number, use that instead

### Step 3: Engage on Recent Posts

**Target: 10-25 posts total across all selected accounts.**

For each target account:
1. Navigate to their profile page (`https://www.instagram.com/[handle]/`)
2. Open their most recent posts one by one (3-6 posts per account)

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
   - Write a 1-2 sentence comment (hard cap at 2) that adds genuine value
   - Match Brian's voice (see comment-guidelines.md for examples)
   - Type the comment in the comment box and submit
   - Verify the comment appears
5. **Reply to 1-2 top comments** if there is something genuine to add
   - Only reply if it makes sense. Do not force replies.
   - Click "Reply" on the comment, type your reply, submit
   - Verify the reply appears

**c. Pacing**
- Wait 5-15 seconds between each action (like, comment, reply)
- Wait 10-20 seconds between posts
- Wait 30-60 seconds between accounts
- This mimics natural human behavior and avoids rate limits

**d. Report after each post:**
```
Post [X]/[total] engaged
Account: @[handle]
Topic: [brief description]
Comment: "[what you wrote]"
```

### Step 4: Save Session Log

Save a markdown log to `output/lender-comments/YYYY-MM-DD.md` with this format:

```markdown
# Lender Comments Session -- [date]

## Summary
- Accounts visited: [X]
- Posts engaged: [Y]
- Posts skipped (guardrails): [Z]
- Comments posted: [A]
- Replies posted: [B]
- Likes given: [C] (posts + comments)

## Detail

### @[handle] -- [company name]
1. **Post:** [brief description]
   - Comment: "[what you wrote]"
   - Replies: [any replies, or "none"]
   - Skipped: [no, or reason]
```

### Step 5: Print Summary

After saving the log, also print a summary to the terminal:

```
Session complete:
- Accounts visited: [X]
- Posts engaged: [Y]
- Posts skipped (guardrails): [Z]
- Comments posted: [A]
- Replies posted: [B]
- Likes given: [C] (posts + comments)
- Log saved: output/lender-comments/YYYY-MM-DD.md
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

- **NEVER use em-dashes in any comment or reply.** Use commas, periods, or "and".
- **NEVER mention Nations Lending** in any comment or reply.
- **NEVER mention recruiting, joining a team, or anything about Brian's branch.**
- **NEVER quote specific interest rates or APRs.**
- **NEVER bash a competitor lender or their work.**
- **NEVER comment on political, LGBTQ+, or controversial posts.** Skip them entirely.
- **ALWAYS verify** that comments and replies were actually posted before moving on.
- **ALWAYS wait 5-15 seconds** between actions to avoid rate limits.
- **ALWAYS save the session log** before ending, even if the session was cut short.

---
name: ig-research
description: Use when someone asks to find Instagram accounts to engage with, research Vegas Instagram accounts, discover local Vegas Instagram pages, or update the Instagram target account list.
disable-model-invocation: true
---

## What This Skill Does

Researches and curates a list of active Vegas-specific Instagram accounts for the `/ig-engage` skill to target. Uses web search to discover popular local accounts, then saves them to a structured file that the engagement skill reads.

---

## Steps

### 1. Read the Existing Account List

Check if `/Users/ryanrose/.claude/skills/ig-engage/target-accounts.md` exists and read it. Note which accounts are already listed so you do not duplicate them.

### 2. Research Vegas Instagram Accounts

Use WebSearch with varied search terms to find active Vegas community and local accounts:

**Search terms to use (vary each session):**
- "popular Las Vegas Instagram accounts to follow"
- "best Vegas local Instagram pages"
- "Las Vegas food Instagram accounts"
- "Vegas community Instagram pages"
- "Las Vegas events Instagram accounts"
- "things to do Las Vegas Instagram"
- "Las Vegas lifestyle bloggers Instagram"
- "Vegas local influencers Instagram"
- "Henderson Nevada Instagram accounts"
- "Summerlin Las Vegas Instagram"

### 3. Evaluate Each Account

For each account found, assess:

- **Active?** Must post at least a few times per month
- **Engagement?** Should have meaningful comment sections (not just bot comments)
- **Safe?** Must NOT be primarily political, LGBTQ+ focused, or controversial (these would get skipped by the engagement skill anyway, so no point adding them)
- **Local?** Must be Vegas-specific or have strong Vegas local following
- **Public?** Must be a public account (private accounts cannot be engaged with)

### 4. Categorize and Document

For each qualifying account, record:

| Field | Description |
|-------|-------------|
| Handle | Instagram @handle |
| Category | community/local, food/dining, events/entertainment, lifestyle, or news/media |
| Description | Brief description of what the account posts about |
| Notes | Any relevant info (posting frequency, engagement level, specific focus) |

### 5. Update the Target Accounts File

Update `/Users/ryanrose/.claude/skills/ig-engage/target-accounts.md`:

- Add new accounts to the Active Accounts table
- Do NOT remove existing accounts unless the user asks
- Keep the file format consistent (markdown table)
- Update the "Last updated" date at the top

### 6. Report Results

Output a summary:
```
Research complete:
- Accounts already in list: [X]
- New accounts found: [Y]
- Total accounts now: [Z]

New additions:
- @[handle] (category) -- [brief description]
- @[handle] (category) -- [brief description]
...
```

---

## Seed Accounts

These accounts are pre-loaded in the target list:

- **@realvegaslocals** -- Popular Vegas locals community account

---

## Target Account Mix

Aim for a balanced list across categories:

- **Community/Local:** 5-8 accounts (core engagement targets)
- **Food/Dining:** 3-5 accounts (high engagement, easy to comment on)
- **Events/Entertainment:** 3-5 accounts (timely content, good for tips)
- **Lifestyle:** 2-4 accounts (scenic content, local culture)
- **News/Media:** 2-3 accounts (thoughtful engagement opportunities)

**Total target: 15-25 accounts** for healthy daily rotation.

---

## Notes

- This skill uses WebSearch which costs API calls. Run it occasionally (weekly or when you want fresh accounts), not daily.
- If `$ARGUMENTS` is provided, use it as an additional search focus (e.g., `/ig-research Henderson food accounts`).
- The engagement skill reads the output file automatically, so no further action is needed after updating.
- Always verify that the accounts you find are real and active before adding them.

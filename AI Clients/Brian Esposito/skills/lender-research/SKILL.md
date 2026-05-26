---
name: lender-research
description: Use when someone asks to research competitor mortgage lenders, find new Las Vegas loan officers to engage with, refresh the target accounts list, or discover Vegas mortgage LOs on Instagram.
model: sonnet
disable-model-invocation: true
---

## What This Skill Does

Discovers and maintains Brian Esposito's target account list for the `/lender-comments` Instagram engagement skill. Searches for competitor mortgage loan officers in Las Vegas, Henderson, and Clark County, Nevada. Verifies they have active Instagram accounts and adds them to the curated target list. Run this monthly or whenever the target list feels stale.

**Target list location:** `~/.claude/skills/lender-comments/target-accounts.md`

---

## MMI Production Data Integration

Brian has access to the MMI platform and can export production-ranked lists of LOs in his market. When an MMI export is provided:

1. Accept the file (PDF or Excel)
2. Parse LO names, companies, and production volumes
3. Filter to the **$2M-$10M production sweet spot**
   - Under $2M: too new, not a strong recruiting target
   - Over $10M: likely self-sufficient, less likely to move
   - $2M-$10M: producing enough to be worth recruiting, likely need support to scale further
4. Use those names as the **primary research source** for finding Instagram accounts
5. MMI-sourced LOs get priority placement in the target list

---

## Research Process

### Step 1: Check for MMI Export

Ask Brian: "Do you have an MMI production export to start with, or should I research from scratch?"

- If MMI file provided: parse it first, extract $2M-$10M producers, then proceed to Step 2 to find their Instagram accounts
- If no MMI file: proceed directly to Step 2 using web research

### Step 2: Search for Competitor LOs

Search these sources for Vegas-area mortgage loan officers at companies **other than Nations Lending:**

**Primary sources:**
- NMLS Consumer Access (https://www.nmlsconsumeraccess.org) -- search by state NV, filter by city (Las Vegas, Henderson, North Las Vegas, Boulder City, Summerlin)
- Google searches: "Las Vegas mortgage loan officer Instagram," "Henderson lender Instagram," "[company name] Las Vegas loan officer"
- Instagram search: search for mortgage-related terms + Vegas/Henderson/Clark County

**Company sites to check for local LO rosters:**
Rocket, UWM, loanDepot, CrossCountry Mortgage, Guild Mortgage, Fairway Independent, Supreme Lending, Movement Mortgage, Cardinal Financial, AmeriSave, Atlantic Bay, Barrett Financial Group, Benchmark Mortgage, PrimeLending, Cornerstone Home Lending, Nations Direct, Evergreen Home Loans, Homebridge Financial, NewAmerican Funding, Finance of America, Guaranteed Rate, Home Point Capital, Mr. Cooper, Pennymac, Sierra Pacific, Stearns Lending, Caliber Home Loans

**Note:** Academy Lending is gone. Do not include.

**Secondary sources:**
- Local Vegas real estate agent podcasts and blogs (LOs often get mentioned)
- Mortgage industry Facebook groups for Las Vegas
- Local real estate event attendee lists

### Step 3: Verify Each Candidate

For each LO found, verify ALL of the following before adding to the list:

- [ ] Active Vegas / Henderson / Clark County presence (not just licensed in NV but located elsewhere)
- [ ] Has a public business Instagram account (not just personal)
- [ ] Posts at least monthly (not abandoned)
- [ ] Is NOT at Nations Lending
- [ ] Is NOT already on the target list
- [ ] Is NOT on Brian's exclude list

### Step 4: Update Target Accounts

Add verified accounts to `~/.claude/skills/lender-comments/target-accounts.md` with this format:

| Handle | Name | Company | Production Tier | Category | Notes |
|--------|------|---------|----------------|----------|-------|
| @handle | Full Name | Company Name | $XM (if from MMI) or "Unknown" | Category | Content themes, posting frequency, tone |

**Categories:**
- **Retail LO** -- Individual loan officers at competing companies
- **Branch Manager** -- Branch managers and team leads (peer-to-peer)
- **Independent Broker** -- Independent mortgage brokers
- **Wholesale AE** -- Account executives who interact with retail LOs
- **Emerging Voice** -- Newer LOs building their following

### Step 5: Report

After updating the list, print a summary:

```
Target List Update Complete:
- New accounts added: [X]
- Accounts verified and kept: [Y]
- Accounts removed (inactive/moved/joined Nations): [Z]
- Total active accounts: [A]
- Sources: [MMI export / web research / both]

New additions:
- @handle -- Name, Company, Category, Production Tier
```

---

## Maintenance

When running this skill on an existing target list:

1. Check each existing account: still active? Still posting? Still at the same company? Still in Vegas?
2. Remove accounts that are: inactive (no posts in 60+ days), moved out of Vegas, joined Nations Lending, or flagged by Brian
3. Add new accounts to replace removed ones
4. Rebalance categories so the list has good variety

---

## Guardrails

- **NEVER add Nations Lending accounts.** Always verify company before adding.
- **NEVER add accounts that primarily post political, controversial, or sensitive content.**
- **Prioritize $2M-$10M producers** when MMI data is available.
- **Target 20-30 active accounts total** for good daily rotation.
- **Always verify Instagram accounts exist and are public** before adding.

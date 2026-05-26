---
name: responder-research
description: Use when someone asks to research Las Vegas first responders, find new military/police/fire/healthcare accounts on Instagram, refresh the responder target list, or discover Vegas first responder Instagram accounts.
model: sonnet
disable-model-invocation: true
---

## What This Skill Does

Discovers and maintains Brian Esposito's target account list for the `/responder-comments` skill. Searches for individual Vegas-area first responders (military/veterans, police, fire/EMS, healthcare) on Instagram. Verifies they have active public accounts and adds them to the target list.

**No MMI equivalent for this audience.** Unlike the lender-research skill, there is no centralized production/employer database for first responders. Discovery is entirely from Instagram bio searches, hashtag mining, and following department accounts to find individuals who post personally.

**Target list location:** `./skills/responder-comments/target-accounts.md`

---

## Research Process

### Step 1: Mine Department / Institutional Accounts

Start with the agency list in `target-accounts.md`. For each Vegas-area agency:

1. Visit the agency's Instagram (@lvmpd, @clarkcountyfd, @nellisafb, etc.)
2. Look at who they tag in posts (often individual personnel)
3. Check who comments regularly on their posts (often other personnel from the same department)
4. Click into those individual accounts and verify they qualify

### Step 2: Hashtag Mining

Search Instagram for these hashtags and filter for Vegas/Henderson/Clark County geography:

**Police / Law Enforcement:**
- #lvmpd, #hendersonpd, #vegaspolice, #clarkcounty, #thinblueline (geo filter to Vegas)

**Fire / EMS:**
- #vegasfire, #vegasff, #clarkcountyfire, #hendersonfire, #lvfr, #firefighter (geo filter)

**Military / Veterans:**
- #nellisafb, #nellisairforce, #nvguard, #nationalguard (geo filter), #vetlife (geo filter)

**Healthcare:**
- #vegasnurse, #vegashealthcare, #umclasvegas, #vegasrn, #vegasdoctor, #nurselife (geo filter)

### Step 3: Bio Keyword Search

On Instagram, search for accounts with these terms in their bios:

- "LVMPD," "Henderson PD," "Metro," "NLV PD," "CCSD PD"
- "CCFD," "Henderson Fire," "LVFR," "NLVFD," "AMR Vegas"
- "USAF Nellis," "Air Force Nellis," "Nevada Guard," "VFW [local post]"
- "RN Vegas," "Sunrise Hospital," "UMC," "Henderson Hospital"
- "Vegas firefighter," "Vegas paramedic," "Vegas veteran," "Vegas nurse"

### Step 4: Verify Each Candidate

For each first responder found, verify ALL of the following before adding to the list:

- [ ] Confirmed Vegas / Henderson / Clark County area presence (not just Nevada or USA)
- [ ] Public Instagram account (not private)
- [ ] Posts at least monthly (active, not abandoned)
- [ ] Posts mix of work + community content (not just personal lifestyle)
- [ ] Does NOT primarily post political or activist content
- [ ] Comments are enabled on most posts
- [ ] Not on Brian's exclude list

### Step 5: Update Target Accounts

Add verified accounts to `./skills/responder-comments/target-accounts.md` with this format:

| Handle | Name | Agency / Branch | Category | Notes |
|--------|------|-----------------|----------|-------|
| @handle | Full Name (if public) | Department/Branch | Category | Posting frequency, content themes, tone |

**Categories:**
- **Military / Veterans**
- **Police / Law Enforcement**
- **Fire / EMS**
- **Healthcare**

### Step 6: Report

After updating the list, print a summary:

```
Responder Target List Update Complete:
- New accounts added: [X]
  - Military/Veterans: [count]
  - Police/Law Enforcement: [count]
  - Fire/EMS: [count]
  - Healthcare: [count]
- Accounts verified and kept: [Y]
- Accounts removed (inactive/moved/political shift): [Z]
- Total active accounts: [A]

New additions:
- @handle -- Name, Agency, Category
```

Aim for **20-30 total active accounts**, with rough balance across all four categories (5-8 per category).

---

## Maintenance

When running this skill on an existing target list:

1. Check each existing account: still active? Still posting? Still in Vegas? Still apolitical?
2. Remove accounts that are: inactive (no posts in 60+ days), moved out of Vegas, shifted to primarily political content, or flagged by Brian
3. Add new accounts to maintain category balance
4. Keep the four categories roughly balanced

---

## Guardrails

- **NEVER add accounts that primarily post political, activist, or controversial content.**
- **NEVER add accounts from out-of-state first responders** (not local relevance for Brian).
- **Skip institutional / PR-only accounts.** This list is for individual humans, not department releases.
- **Verify Instagram accounts are public and active** before adding.
- **Aim for category balance** -- don't end up with 25 police accounts and 2 nurses.

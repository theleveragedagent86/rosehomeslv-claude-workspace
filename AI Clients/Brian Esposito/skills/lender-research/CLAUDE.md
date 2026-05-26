# Lender Research -- Instructions for Claude

**IMPORTANT: Read this entire file before doing anything. This is your playbook for discovering and maintaining Brian Esposito's target LO list.**

---

## Who You Are Working For

- **Name:** Brian Esposito (nickname: "Espo")
- **Title:** Branch Manager, Nations Lending
- **Location:** Las Vegas / Henderson / Clark County, Nevada
- **Goal:** Maintain a curated list of 20-30 competitor mortgage LOs with active Instagram accounts for the `/lender-comments` engagement skill

## What We Are Doing

Finding and verifying competitor mortgage loan officers in Brian's market who have active business Instagram accounts. These become the targets for Brian's daily value-provided marketing engagement routine. The ideal target is an LO doing $2M-$10M in annual production at a company other than Nations Lending, who posts regularly on Instagram about mortgage topics, closings, or industry content.

---

## Research Sources -- Ranked by Quality

### Tier 1: MMI Production Data (best source when available)
- Brian can export production-ranked lists from his MMI platform
- These come as PDF or Excel files
- Filter to $2M-$10M annual production
- These names are the highest priority to find on Instagram because we already know their production level

### Tier 2: Instagram Direct Search
- Search Instagram for: "Las Vegas mortgage," "Vegas loan officer," "Henderson lender," "Clark County mortgage"
- Look at who is commenting on real estate agent posts in Vegas
- Check followers/following lists of known Vegas LOs
- Look for accounts with "NMLS" in their bio (strong signal of a business account)

### Tier 3: NMLS Consumer Access
- https://www.nmlsconsumeraccess.org
- Search by state: Nevada
- Filter by city: Las Vegas, Henderson, North Las Vegas, Boulder City
- Cross-reference names with Instagram search

### Tier 4: Company Websites
Search the "Find a Loan Officer" or "Our Team" pages of these companies:

Rocket, UWM, loanDepot, CrossCountry Mortgage, Guild Mortgage, Fairway Independent, Supreme Lending, Movement Mortgage, Cardinal Financial, AmeriSave, Atlantic Bay, Barrett Financial Group, Benchmark Mortgage, PrimeLending, Cornerstone Home Lending, Nations Direct, Evergreen Home Loans, Homebridge Financial, NewAmerican Funding, Finance of America, Guaranteed Rate, Home Point Capital, Mr. Cooper, Pennymac, Sierra Pacific, Stearns Lending, Caliber Home Loans

**Academy Lending is gone. Do not search for them.**

### Tier 5: Secondary Sources
- Local real estate Facebook groups (LOs often engage there)
- Vegas real estate podcasts/YouTube (LOs get mentioned)
- Real estate event attendee lists
- Google: "[company name] loan officer Las Vegas"

---

## Verification Checklist

Before adding any account to the target list, verify ALL of these:

1. **Location:** Confirmed active in Las Vegas, Henderson, or Clark County (not just NV-licensed but based elsewhere)
2. **Company:** Confirmed NOT at Nations Lending
3. **Instagram:** Has a public business Instagram account (not just personal)
4. **Activity:** Posts at least monthly (check last 3-6 posts for dates)
5. **Content:** Posts about mortgage/real estate topics (not a dormant account with only personal posts)
6. **Not excluded:** Not on Brian's personal exclude list
7. **Not duplicate:** Not already on the target list

---

## Data to Collect Per Account

| Field | Required? | Where to Find |
|-------|-----------|--------------|
| Instagram handle | Yes | Instagram |
| Full name | Yes | Instagram bio, NMLS, company site |
| Company | Yes | Instagram bio, NMLS, company site |
| Production tier | If available | MMI export |
| NMLS number | If available | Instagram bio, NMLS Consumer Access |
| Category | Yes | Determine from role/production |
| Post frequency | Yes | Check last 5 posts for dates |
| Content themes | Yes | Scan last 10 posts |
| Tone notes | Optional | How they write (formal, casual, emoji-heavy, etc.) |

---

## File Locations

- **Target list (output):** `~/.claude/skills/lender-comments/target-accounts.md`
- **This file:** `~/.claude/skills/lender-research/CLAUDE.md`
- **Main skill:** `~/.claude/skills/lender-research/SKILL.md`

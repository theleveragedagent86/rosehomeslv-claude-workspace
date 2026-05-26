# Lender Research Weekly Schedule -- Paste into Cowork Scheduler

Use this as the prompt when setting up a scheduled task in Cowork for Brian Esposito's weekly target-list refresh.

---

## Schedule Settings

- **Frequency:** Weekly
- **Day/Time:** Pick a low-engagement slot (Sunday evening or Monday morning recommended, e.g., Monday 8:00 AM PT, before the daily comments routine runs)

---

## Prompt to Paste

Run the weekly lender research refresh routine.

STEP 1 -- READ CURRENT TARGET LIST
Read the current target accounts list from the lender-engagement plugin at ./skills/lender-comments/target-accounts.md. Note total count, categories, and any accounts flagged in previous runs.

STEP 2 -- AUDIT EXISTING ACCOUNTS
For each account currently on the list, verify:
- Instagram account is still public and active (posted in the last 60 days)
- Still located in Las Vegas, Henderson, North Las Vegas, Boulder City, or Summerlin
- Still at the same company (not moved to Nations Lending)
- Not posting primarily political, LGBTQ+, controversial, or sensitive content
Flag for removal: inactive (no posts in 60+ days), moved out of Vegas, joined Nations Lending, or content drift toward off-limits topics.

STEP 3 -- DISCOVER NEW CANDIDATES
Search for 3-5 new Vegas-area competitor LOs to fill any gaps. Use:
- Instagram search for mortgage-related terms plus Vegas/Henderson/Clark County
- Google searches: "Las Vegas mortgage loan officer Instagram," "Henderson lender Instagram"
- Company rosters from the competitor list in the lender-research skill (Rocket, UWM, loanDepot, CrossCountry, Guild, Fairway, Supreme, Movement, Cardinal, etc.)
- Skip Nations Lending and Academy Lending (Academy is gone)
If Brian has dropped a fresh MMI export this week, use it as the primary source and prioritize the $2M-$10M production band.

STEP 4 -- VERIFY EACH NEW CANDIDATE
For each candidate, confirm ALL of the following before adding:
- Active Vegas / Henderson / Clark County presence (not just NV-licensed)
- Public business Instagram account (not personal)
- Posts at least monthly
- Not at Nations Lending
- Not already on the target list
- Not posting primarily off-limits content (political, LGBTQ+, controversial)

STEP 5 -- UPDATE TARGET LIST
Edit ./skills/lender-comments/target-accounts.md:
- Remove flagged accounts from Step 2
- Add verified new accounts from Step 4 in the existing table format: | Handle | Name | Company | Production Tier | Category | Notes |
- Keep total between 20-30 active accounts
- Rebalance categories (Retail LO, Branch Manager, Independent Broker, Wholesale AE, Emerging Voice) for good rotation variety
- No em-dashes anywhere in the file

STEP 6 -- SAVE LOG AND REPORT
Save a refresh log to output/lender-research/YYYY-MM-DD.md with: accounts audited, accounts removed (with reasons), new candidates evaluated, new accounts added, total active count.
Also print a summary:
- Accounts audited: [X]
- Removed (inactive/moved/joined Nations/content drift): [Y]
- New accounts added: [Z]
- Total active accounts: [A]
- Source: MMI export / web research / both
- New additions: @handle -- Name, Company, Category, Production Tier
```

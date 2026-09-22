# Responder Research Weekly Schedule -- Paste into Cowork Scheduler

Use this as the prompt when setting up a scheduled task in Cowork for Brian Esposito's weekly first-responder target-list refresh.

**Important:** This run discovers and verifies *individual* first responder accounts by browsing Instagram, so it must run in Cowork with the `playwright-instagram` MCP connected and @espohomeloans logged in. The CLI alone cannot do it. Schedule it in a low-engagement slot (before the daily responder-comments routine), and at a different time than the lender-research run so the account is not browsing all day.

---

## Schedule Settings

- **Frequency:** Weekly (biweekly is fine if the list is already healthy)
- **Day/Time:** Low-engagement slot, e.g., Sunday evening or Monday 8:00 AM PT, before the daily comments routine runs

---

## Prompt to Paste

```
Run the weekly first responder research refresh routine.

STEP 0 -- CONFIRM BROWSER
Confirm the Playwright Instagram tools are connected and @espohomeloans is logged in. If browser tools are not available, STOP and tell me, since individual accounts cannot be discovered or verified from web search alone.

STEP 1 -- READ CURRENT TARGET LIST
Read the current target accounts from the first-responder-engagement plugin at ./skills/responder-comments/target-accounts.md. Note the total count, the balance across the four categories (Military/Veterans, Police, Fire/EMS, Healthcare), and any accounts flagged in previous runs. Remember: this is the FIRST RESPONDER list. Never merge it with the lender list, and if any mortgage or real estate account is on it, remove that account.

STEP 2 -- AUDIT EXISTING ACCOUNTS
For each account currently on the list, verify:
- Instagram account is still public and active (posted in the last 60 days)
- Still located in Las Vegas, Henderson, North Las Vegas, Boulder City, or Clark County
- Still mixing work and community content, not drifting to mostly lifestyle, fitness, or memes
- Not shifting to primarily political, activist, endorsement, or controversial content
Flag for removal: inactive (no posts in 60+ days), moved out of the Vegas area, comments turned off, or content drift toward political/off-limits topics. Apply this strictly to the union and association accounts (@clarkcountyfirefighters, @hendersonpff, @lasvegasfirefighters and similar), which sometimes post endorsements or labor-dispute content.

STEP 3 -- DISCOVER NEW INDIVIDUALS
Find 3-5 new individual first responders to fill gaps. Discovery is by browsing, not by inventing handles. Use, in order:
- Mine the verified seed accounts already in target-accounts.md (the official, unit, association, and charity accounts). On each, look at who they tag in posts and who comments regularly, then click into those individual accounts.
- Hashtag mining with a Vegas/Henderson/Clark County geo filter: #lvmpd #vegaspolice #thinblueline, #vegasfire #vegasff #clarkcountyfire #hendersonfire #lvfr, #nellisafb #nellisstrong #nvguard, #vegasnurse #vegasrn #umclasvegas #vegashealthcare.
- Bio keyword search: "Las Vegas police officer," "Henderson firefighter," "Vegas paramedic," "Nellis airman," "Vegas veteran," "Vegas nurse," "RN UMC," "Sunrise nurse," "LVMPD," "CCFD," "LVFR," "USAF Nellis."
Prioritize HEALTHCARE individuals (nurses, doctors, frontline workers). That is the biggest gap, since hospital corporate accounts are easy but individuals are not.

STEP 4 -- VERIFY EACH NEW CANDIDATE
For each candidate, confirm ALL of the following before adding:
- Confirmed Vegas / Henderson / Clark County area presence (not just Nevada or USA)
- Public Instagram account, not private
- Posts at least monthly (last few posts within 60 days)
- Mixes work and community content, not 100% lifestyle and not 100% political takes
- Does NOT primarily post political, activist, or controversial content
- Comments are enabled on most posts
- Is a real first responder, not someone using the title as a brand persona (Google the name if unsure)
- Not already on the list, and not on the exclude list

STEP 5 -- UPDATE TARGET LIST
Edit ./skills/responder-comments/target-accounts.md:
- Remove the accounts flagged in Step 2 (note the reason).
- Add each verified new individual under the correct category section, matching the existing table structure for that section (Handle, Name if public, Agency/Branch, Type or Category, Notes with posting frequency, content themes, and tone).
- Keep the four categories roughly balanced (aim 5-8 individuals each, 20-30 total).
- No em-dashes anywhere in the file. Use commas, periods, or "and".

STEP 6 -- SAVE LOG AND REPORT
Save a refresh log to output/responder-research/YYYY-MM-DD.md with: accounts audited, accounts removed (with reasons), new candidates evaluated, new accounts added, and the per-category counts.
Also print a summary:
- Accounts audited: [X]
- Removed (inactive/moved/comments off/political drift): [Y]
- New accounts added: [Z]
  - Military/Veterans: [count]
  - Police/Law Enforcement: [count]
  - Fire/EMS: [count]
  - Healthcare: [count]
- Total active accounts: [A]
- New additions: @handle -- Name, Agency, Category
```

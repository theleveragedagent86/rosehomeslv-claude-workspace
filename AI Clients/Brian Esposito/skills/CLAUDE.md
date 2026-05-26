# Brian Esposito -- Claude Code Project Instructions

## Who This Is For

Brian J. Esposito, Branch Manager at Nations Lending, Las Vegas, NV (NMLS #1535781). Former PGA TOUR / TPC Head Golf Professional. 28+ years in Las Vegas. Founder of Par for the Cure (501c3, $1.6M+ raised over 20 years for breast cancer research).

Instagram: @espohomeloans (business account only)

## Available Skills

### /lender-comments (daily engagement engine)
- **What it does:** Automates daily Instagram engagement on competitor mortgage LO posts in Vegas/Henderson/Clark County
- **How to run:** Type "run lender-comments" or "/lender-comments"
- **Requires:** Playwright MCP connected (see Playwright_MCP_Setup.md)
- **Output:** Session log saved to `output/lender-comments/YYYY-MM-DD.md` + terminal summary
- **Trigger phrases:** "engage on lender posts," "run daily IG routine," "comment on Vegas LOs," "value-provided marketing"

### /lender-research (target list builder)
- **What it does:** Discovers and verifies competitor LOs with active Instagram accounts, updates the target list
- **How to run:** Type "run lender-research" or "/lender-research"
- **Input:** Optionally provide an MMI production export (PDF or Excel) for $2M-$10M sweet spot targeting
- **Output:** Updates `~/.claude/skills/lender-comments/target-accounts.md`
- **Trigger phrases:** "find new LOs," "refresh target list," "research competitor lenders," "update target accounts"

## Key Rules (Apply to All Skills)

1. Never use em-dashes in any output. Use commas, periods, or "and."
2. Never mention Nations Lending in any Instagram comment or reply.
3. Never self-promote, recruit, or use CTAs in comments.
4. Never quote specific interest rates or APRs in comments.
5. Never bash competitor lenders or their work.
6. Skip all political, LGBTQ+, religious, or controversial posts entirely.
7. When in doubt, skip the post.

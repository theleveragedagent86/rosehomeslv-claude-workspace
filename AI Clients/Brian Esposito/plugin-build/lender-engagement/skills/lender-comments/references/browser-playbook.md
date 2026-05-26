# Lender Comments -- Browser Automation Playbook

**IMPORTANT: Read this entire file before doing anything. This is your playbook.**

---

## Who You Are Working For

- **Name:** Brian Esposito (nickname: "Espo")
- **Title:** Branch Manager, Nations Lending
- **NMLS:** 1535781
- **Instagram Account:** @espohomeloans (business account only)
- **Location:** Las Vegas / Henderson / Clark County, Nevada
- **Goal:** Build name recognition with competitor mortgage loan officers through genuine value-add engagement, so they organically reach out about joining Brian's branch

## What We Are Doing

Building Brian's presence in the Instagram comment sections of competitor mortgage LOs across Vegas, Henderson, and Clark County. The strategy is value-provided marketing: show up consistently with tight 1-2 sentence comments (hard cap at 2) that demonstrate mortgage expertise, leadership perspective, and Vegas market knowledge. This is NOT about selling, pitching, or overtly recruiting. It is about becoming a recognized name in the local mortgage community so that LOs start reaching out on their own.

Brian's voice is warm professional peer crossed with mentor. Think confident industry insight with approachable, encouraging energy. He is a former PGA TOUR / TPC Head Golf Pro (TPC Canyons and TPC Deere Run, home of the John Deere Classic), founder of Par for the Cure (breast cancer research nonprofit, $1.6M+ raised over 20 years), and has been in Las Vegas for 28+ years.

---

## Target Accounts

The full curated list lives in `./skills/lender-comments/target-accounts.md`. This file is maintained by the `/lender-research` skill.

**Account categories we target:**
- Individual loan officers at competing mortgage companies (primary focus)
- Branch managers and team leaders at other companies (peer-to-peer)
- Emerging LOs building their following ($2M-$10M production sweet spot)

**We do NOT target:**
- Nations Lending accounts (colleagues, not competitors)
- Political accounts or political commentators
- Accounts that primarily post controversial content
- LOs doing $20M+ in production (unlikely recruiting targets, already self-sufficient)
- Accounts with very low engagement or no recent posts (inactive)

---

## Technical Notes for Browser Automation

### Instagram UI Patterns

**Post Page Elements:**
- Heart icon (like button): Below the image, left side. Click to like. Turns red when liked.
- Comment input: Below the post, usually says "Add a comment..." Click to activate.
- Post button: Appears after typing in the comment field. Click to submit.
- Comment hearts: Small heart icon to the right of each comment. Click to like.
- Reply link: "Reply" text below each comment. Click to open a reply field.

**Profile Page Elements:**
- Post grid: Thumbnails of recent posts in a 3-column grid
- Click any thumbnail to open the full post in a modal or new view
- Scroll down to load more posts if needed

### Comment Box Interaction

1. Find the comment input (look for "Add a comment..." placeholder text)
2. Click the input field to activate it
3. Type the comment text
4. Click the "Post" button (or press Enter on some views)
5. Wait 2-3 seconds for the comment to submit
6. Verify: Your comment should appear in the comment section

**If the comment box does not activate:**
- Try clicking directly on the text "Add a comment..."
- Try using tab to focus into the field
- Try scrolling the comment section to load the input
- If it still does not work, the post may have comments disabled. Skip it.

### Reply to Comments

1. Find the comment you want to reply to
2. Click "Reply" below that comment
3. A reply input should appear, pre-filled with @username
4. Type your reply after the @mention
5. Click "Post" or press Enter
6. Verify the reply appears nested under the original comment

### Verification After Each Action

- **After liking:** Heart icon should be filled/red
- **After commenting:** Your comment text should appear in the comment section
- **After replying:** Your reply should appear nested under the parent comment
- If verification fails, try once more. If it fails again, skip and move on.

### Navigation Between Posts

- After engaging with a post, go back to the profile grid
- Open the next post
- If using a modal view, close the modal and click the next thumbnail
- If on a dedicated post page, navigate back to the profile URL

### Key Playwright MCP Tools Used

- **browser_navigate** -- Go to a URL
- **browser_snapshot** -- Read the page content via accessibility tree (fast, no screenshots needed)
- **browser_click** -- Click elements on the page
- **browser_type** -- Type text into input fields
- **browser_screenshot** -- Take a visual screenshot (backup if snapshot is unclear)
- **browser_tab_list / browser_tab_new / browser_tab_select** -- Manage browser tabs

### Instagram-Specific Browser Notes

- **Always verify after posting:** Take a snapshot to confirm your comment text appears
- **Comments disabled:** Some posts turn off comments. If you cannot find a comment input, skip the post.
- **Rate limits:** Instagram is aggressive with rate limiting. If you see "Try Again Later" or any error, stop immediately.
- **Modal views:** Instagram often opens posts in a modal overlay. Interact within the modal, then close it to return to the grid.
- **Infinite scroll:** Profile grids load more posts as you scroll. Only engage with the first 6-9 posts visible (most recent).

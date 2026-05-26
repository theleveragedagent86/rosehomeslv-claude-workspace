# Playwright MCP Setup for Lender Comments Skill

**Purpose:** Enable the `/lender-comments` skill to comment, like, and reply on Instagram via browser automation.

**Status:** Not yet configured

---

## Prerequisites

- **Node.js 18+** must be installed (`node --version` to check)
- **npm** must be available (`npm --version` to check)
- **Claude Code CLI** must be installed

---

## Step 1: Add Playwright MCP to Claude Code

Run this command in your terminal **before** starting Claude Code:

```bash
claude mcp add playwright-instagram -- npx @playwright/mcp@latest --user-data-dir ~/.cache/playwright-instagram-profile
```

**What this does:**
- Installs the official Microsoft Playwright MCP server
- `--user-data-dir` saves your Instagram login between sessions so you don't have to log in every time
- Configuration is saved to `~/.claude.json` and persists across sessions

**Alternative: Global scope** (works from any directory):

```bash
claude mcp add --scope user playwright-instagram -- npx @playwright/mcp@latest --user-data-dir ~/.cache/playwright-instagram-profile
```

---

## Step 2: Verify Installation

1. Start Claude Code: `claude`
2. Type `/mcp` and look for `playwright-instagram` in the list
3. You should see ~25 tools available including navigation, clicking, typing, screenshots, etc.

---

## Step 3: Log Into Instagram (First Time Only)

On your first session after setup:

1. Tell Claude: **"Use playwright-instagram to open a browser to https://www.instagram.com/accounts/login/"**
2. A visible Chrome window will open with the Instagram login page
3. **Log in manually** with your Instagram credentials (@espohomeloans account)
4. If 2FA is enabled, complete the 2FA challenge manually
5. Tell Claude: **"I'm logged in, you can continue"**
6. Because of `--user-data-dir`, your login cookies persist between sessions

---

## Step 4: Test It

Ask Claude to run a simple test:

> "Use the playwright-instagram MCP to navigate to https://www.instagram.com and take a snapshot of the page"

If it works, you should see your Instagram home feed content in the accessibility tree output.

---

## How the Lender Comments Skill Uses Playwright

Once Playwright MCP is connected, the `/lender-comments` skill can:

| Action | How It Works |
|--------|-------------|
| **Open profiles** | Navigate to `https://www.instagram.com/[handle]/` |
| **Open posts** | Click on post thumbnails in the profile grid |
| **Read post captions** | Take accessibility snapshots to read text content |
| **Like posts** | Click the heart icon below the post image |
| **Like comments** | Click the small heart icon next to each comment |
| **Post comments** | Click "Add a comment..." field, type text, click "Post" |
| **Reply to comments** | Click "Reply" under a comment, type reply, submit |
| **Read comments** | Take accessibility snapshots of the comment section |

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

---

## Troubleshooting

### "Playwright tools not showing up"
- Make sure you ran `claude mcp add` before starting Claude Code (not during)
- Restart Claude Code after adding the MCP
- Run `/mcp` to check if playwright-instagram appears in the server list

### "Browser doesn't open"
- Make sure Node.js 18+ is installed
- Try running `npx @playwright/mcp@latest` directly in terminal to see errors
- On Mac, you may need to allow Chromium in System Settings > Privacy & Security

### "Not logged into Instagram"
- The `--user-data-dir` flag saves cookies, but sessions expire
- Instagram sessions may expire more frequently than other sites (especially with 2FA)
- If logged out, tell Claude to navigate to instagram.com/accounts/login/ and log in manually again

### "Comment won't post"
- Some posts have comments disabled. Skip them.
- Check if the comment input field is actually a contenteditable div
- Try clicking directly on the "Add a comment..." text
- If the "Post" button is grayed out, make sure text was typed into the field

### "Rate limited / Action Blocked"
- This means Instagram detected automated behavior
- **Stop the session immediately.** Do not continue.
- Wait at least 24 hours before trying again
- Consider increasing the wait time between actions (15-30 seconds)
- Reduce the number of posts per session (try 5-10 instead of 10-25)

### "Tool timeout"
- Default action timeout is 5 seconds, navigation timeout is 60 seconds
- Instagram pages can be slow to load. You can increase timeouts:
  ```bash
  claude mcp add playwright-instagram -- npx @playwright/mcp@latest --user-data-dir ~/.cache/playwright-instagram-profile --timeout-action 10000 --timeout-navigation 90000
  ```

---

## Configuration Reference

The MCP config is stored in `~/.claude.json` under the mcpServers key. The entry looks like:

```json
{
  "mcpServers": {
    "playwright-instagram": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--user-data-dir",
        "~/.cache/playwright-instagram-profile"
      ]
    }
  }
}
```

You can also add it manually to `~/.claude.json` if the CLI command doesn't work.

---

*This file is a setup guide only. It does not modify the lender-comments skill itself.*

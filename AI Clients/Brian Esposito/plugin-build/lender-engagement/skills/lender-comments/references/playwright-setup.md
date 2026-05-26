# Playwright MCP Setup for Lender Engagement Plugin

**Purpose:** Enable the `/lender-comments` skill to comment, like, and reply on Instagram via browser automation.

---

## Prerequisites

- **Node.js 18+** must be installed (`node --version` to check)
- **npm** must be available (`npm --version` to check)
- **Claude Code** must be installed

---

## Setup

The plugin's `plugin.json` already includes the Playwright MCP server configuration. When you install this plugin, the MCP server is registered automatically.

If you need to add it manually instead, run:

```bash
claude mcp add --scope user playwright-instagram -- npx @playwright/mcp@latest --user-data-dir ~/.cache/playwright-instagram-profile
```

### Verify Installation

1. Start Claude Code: `claude`
2. Type `/mcp` and look for `playwright-instagram` in the list
3. You should see ~25 tools available including navigation, clicking, typing, screenshots, etc.

---

## Log Into Instagram (First Time Only)

On your first session after setup:

1. Tell Claude: **"Use playwright-instagram to open a browser to https://www.instagram.com/accounts/login/"**
2. A visible Chrome window will open with the Instagram login page
3. **Log in manually** with your @espohomeloans Instagram credentials
4. If 2FA is enabled, complete the 2FA challenge manually
5. Tell Claude: **"I'm logged in, you can continue"**
6. Because of `--user-data-dir`, your login cookies persist between sessions

---

## Test It

Ask Claude to run a simple test:

> "Use the playwright-instagram MCP to navigate to https://www.instagram.com and take a snapshot of the page"

If it works, you should see your Instagram home feed content in the accessibility tree output.

---

## Troubleshooting

### "Playwright tools not showing up"
- Restart Claude Code after installing the plugin
- Run `/mcp` to check if playwright-instagram appears in the server list

### "Browser doesn't open"
- Make sure Node.js 18+ is installed
- Try running `npx @playwright/mcp@latest` directly in terminal to see errors
- On Mac, you may need to allow Chromium in System Settings > Privacy & Security

### "Not logged into Instagram"
- The `--user-data-dir` flag saves cookies, but sessions expire
- If logged out, tell Claude to navigate to instagram.com/accounts/login/ and log in manually again

### "Comment won't post"
- Some posts have comments disabled. Skip them.
- Try clicking directly on the "Add a comment..." text
- If the "Post" button is grayed out, make sure text was typed into the field

### "Rate limited / Action Blocked"
- **Stop the session immediately.** Do not continue.
- Wait at least 24 hours before trying again
- Consider increasing the wait time between actions (15-30 seconds)
- Reduce the number of posts per session (try 5-10 instead of 10-25)

### "Tool timeout"
- Instagram pages can be slow to load. You can increase timeouts by re-adding the MCP with longer timeouts:
  ```bash
  claude mcp add playwright-instagram -- npx @playwright/mcp@latest --user-data-dir ~/.cache/playwright-instagram-profile --timeout-action 10000 --timeout-navigation 90000
  ```

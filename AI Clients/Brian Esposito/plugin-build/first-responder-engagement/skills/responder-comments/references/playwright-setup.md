# Playwright MCP Setup for First Responder Engagement Plugin

**Purpose:** Enable the `/responder-comments` skill to comment, like, and reply on Instagram via browser automation.

**Note:** This plugin uses the SAME Playwright MCP server (`playwright-instagram`) as the `lender-engagement` plugin. If you already installed that plugin, the MCP is already configured and you can skip to the verification step.

---

## Prerequisites

- **Node.js 18+** must be installed (`node --version` to check)
- **npm** must be available (`npm --version` to check)
- **Claude Code** must be installed

---

## Setup

The plugin's `plugin.json` includes the Playwright MCP server configuration. When you install this plugin, the MCP server is registered automatically (or reused if the lender-engagement plugin is also installed).

If you need to add it manually:

```bash
claude mcp add --scope user playwright-instagram -- npx @playwright/mcp@latest --user-data-dir ~/.cache/playwright-instagram-profile
```

### Verify Installation

1. Start Claude Code: `claude`
2. Type `/mcp` and look for `playwright-instagram` in the list
3. You should see ~25 tools available

---

## Log Into Instagram (First Time Only)

**If you already logged in for the lender-engagement plugin, you do NOT need to log in again.** Both plugins share the same `--user-data-dir`, which means the same Instagram session.

If this is your first plugin install:

1. Tell Claude: "Use playwright-instagram to open a browser to https://www.instagram.com/accounts/login/"
2. Log in manually with your @espohomeloans credentials
3. Complete 2FA if enabled
4. Tell Claude: "I'm logged in, you can continue"

---

## Test It

> "Use the playwright-instagram MCP to navigate to https://www.instagram.com and take a snapshot of the page"

If you see your Instagram home feed, you're set.

---

## Troubleshooting

Same as the lender-engagement plugin. See that plugin's `playwright-setup.md` for detailed troubleshooting steps. The two plugins share the same browser session, so any issue with one affects the other.

### Plugin-specific note

If you're running both plugins in the same day, the combined activity load matters. If you hit a rate limit on either plugin, both should pause for at least 24 hours before resuming.

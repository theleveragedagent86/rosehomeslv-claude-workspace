#!/bin/zsh
# ONE-TIME setup: log @rosehomeslv into the automation browser profile that the
# scheduled run uses. Run this once (and again only if Instagram logs you out).
#
# What happens: a real Chromium window opens on Instagram's login page, using the
# SAME profile directory the cron reads. Log into @rosehomeslv (handle any 2FA),
# then CLOSE the browser window. The session is saved to the profile.
# A small "Playwright Inspector" recorder window also opens, just ignore/close it.
#
# Run with:  zsh scripts/login-once.sh

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
PROF="/Users/ryanrose/.cache/playwright-instagram-profile"
mkdir -p "$PROF"

echo "Opening Instagram login in the automation profile ($PROF) ..."
echo "Log into @rosehomeslv, then close the browser window to save the session."
npx --yes playwright@latest codegen --user-data-dir="$PROF" "https://www.instagram.com/accounts/login/"
echo "Done. If you logged in and closed the window, the session is now saved for the cron."

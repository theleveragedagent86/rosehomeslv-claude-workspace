#!/usr/bin/env python3
"""
Publish the 7 missing expired listing posts to Lofty CMS.

Usage:
    python3 publish-missing-7.py
    python3 publish-missing-7.py --tab 4
    python3 publish-missing-7.py --yes          # skip confirmation

This is a thin wrapper around publish.py that targets only
posts 1, 8, 9, 10, 11, 12, 13 from the EXPIRED LISTINGS folder
with category "EXPIRED LISTINGS".
"""

import subprocess
import sys

POSTS = "1,8,9,10,11,12,13"
FOLDER = "EXPIRED LISTINGS"
CATEGORY = "EXPIRED LISTINGS"

# Pass through --tab and --yes flags
extra_args = []
for arg in sys.argv[1:]:
    extra_args.append(arg)

cmd = [
    sys.executable,
    "/Users/ryanrose/Downloads/Claude/publish-blogs-plugin/publish.py",
    FOLDER,
    "--posts", POSTS,
    "--category", CATEGORY,
] + extra_args

print(f"Publishing 7 missing posts: {POSTS}")
print(f"Folder: {FOLDER}")
print(f"Category: {CATEGORY}")
print(f"Command: {' '.join(cmd)}\n")

sys.exit(subprocess.call(cmd))

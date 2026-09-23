# Weekly Seller Update: clipped Reels / Shorts

12 vertical clips cut from the RAW footage of the Weekly Seller Update recording (Sept 17 2026). Ryan's own words, not the re-record scripts in `../../Weekly-Seller-Update-Instagram-Shorts.md`. Captions to paste are in `../../Weekly-Seller-Update-Instagram-Reel-Captions.md`.

Output: `SKOOL Community/Final Videos/Weekly-Seller-Update-Reel-NN-*.mp4` (1080x1920, 30fps, -14 LUFS, git-ignored).

| # | Reel | Cut from (camera time) | Length |
|---|---|---|---|
| 01 | My Sellers Get This Every Friday | 0:00 intro + 2:17 "30 days, 21 showings, 5,500 views" | 58s |
| 02 | Pick The Tone Before AI Writes It | 1:37 to 2:17 | 43s |
| 03 | One Command, One Paste, Publish | 18:42 + 20:43 paste into Lofty | 37s |
| 04 | You're Using AI Backwards | 14:04 + 9:05 + 11:12 | 58s |
| 05 | The Listing Appointment Promise | 20:53 to end | 65s |
| 06 | Where Every Online View Comes From | 2:30 to 3:14 | 47s |
| 07 | Showing Feedback In The Right Tone | 3:14 to 3:54 | 44s |
| 08 | Show Your Seller The Work | 3:54 to 4:53 | 62s |
| 09 | Talk, Don't Type Your Prompt | 5:36 to 6:08 | 35s |
| 10 | Read The Plan Before You Build | 12:39 to 13:28 | 52s |
| 11 | Make It Your Brand | 15:24 to 15:57 (report B-roll) | 36s |
| 12 | Why I Let Claude Run Without Asking | 16:11 to 17:15 | 66s |

Every clip ends on `Brandkit/YouTube-Bumpers/renders/bumper-9x16.mp4` (3s, silent).

**Layout:** screen on top 1080x1000, face below 1080x920, word-by-word captions on the seam in Barlow 800 with the active word in #5B9BFF. The first 40s of Reel 1 is face only (no screen was recording yet).

**Privacy:** the synced screen in Reel 4's third segment showed an offer amount and a buyer's name, and Reel 5's synced screen showed the same Claude reply. Both use clean B-roll instead (the plan workflow, the report scroll). Re-check any new segment for offer amounts, buyer names or seller contact info before shipping.

**Rebuild:** `python3 build.py` (all) or `python3 build.py 3 7` (some, keyed by reel number). Needs the three raw files in `~/Downloads` and Playwright from `hyperframes-student-kit`. `words.json` = whisper small.en word timestamps; screen offsets (cam minus screen) scr1 49.52s, scr2 723.09s. Local ffmpeg has no libass/drawtext, so `caps.mjs` renders caption PNGs with Playwright and they are overlaid through an ffconcat track.

**Reel covers:** `covers/cover-01.png` to `cover-12.png` (1080x1920), standalone title graphics, not video frames, built by the shared `../reel-covers/` template (see its README).

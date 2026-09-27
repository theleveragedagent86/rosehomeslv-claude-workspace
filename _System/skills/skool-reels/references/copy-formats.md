# Copy formats

Reference files: `SKOOL Community/Scripts/Weekly-Seller-Update-Instagram-Reel-Captions.md`,
`Shorts-Build/YOUTUBE-SHORTS-METADATA.md`, `Shorts-Build/POSTING-SCHEDULE.md`. Match them.

## IG captions: `Scripts/<Series>-Instagram-Reel-Captions.md`

Header: title, `## The Leveraged Agent | @the.leveraged.agent | <Module>`, one-paragraph intro, a **Rules for this set** list (the real numbers allowed in this set, named), then `---`.

Per reel:
```
### Reel N | <file>.mp4
**Length:** 58s
**Clip:** <one line on what's on screen>

<Title Case Headline>

<hook line>

<short paragraphs, 1 to 3 sentences each>

<pivot line, e.g. "Here is why this matters more than people think.">

<perspective>

<one closing question>

The full walkthrough is on my YouTube, and the complete setup is inside The Leveraged Agent. Link in bio.
```
250 to 400 words. No hashtags, no emojis, no em dashes. Matches what Ryan says in that clip.

## YouTube Shorts metadata: append to `YOUTUBE-SHORTS-METADATA.md`

```
## <Series> NN, `<file>.mp4`

**Title** (NN chars)
<45 chars or fewer, one hook, no ALL CAPS>

**Description**
<2 to 3 sentence hook body>

Full build is inside The Leveraged Agent, my Skool community for real estate agents.
Join: https://www.skool.com/the-leveraged-agent
Instagram: https://www.instagram.com/the.leveraged.agent

#Shorts #realestateagent #claudecode #aiforrealestate #theleveragedagent

**Tags** (NNN chars)
<comma list, under 500 chars including commas, same block for the whole series>
```
Canonical Skool URL is `skool.com/the-leveraged-agent` (not the -7674 one).

`yt_manifest.json` = list of `{file (absolute), title, description, tags[], publishAt "YYYY-MM-DDTHH:MM:SS-07:00"}` parsed from the .md in schedule order. Check no `.mp4.mp4`.

## Posting schedule: `POSTING-SCHEDULE.md`

Current rules (research in `YOUTUBE-POSTING-TIMES-RESEARCH.md` and `SKOOL Community/Instagram/Posting-Times-Research.md`):
- Posting days Mon, Tue, Wed, Sat, Sun. Skip Thu, Fri.
- **IG**: 5:00am PT + evening peak (Mon/Sat 5:15pm, Tue/Wed/Sun 6:15pm).
- **YouTube**: same pairs at 9:00am and 2:00pm PT (3 to 7am Shorts did 0.87x, 2 to 5pm did 1.10x).
- Two series run side by side, one reel of each per day, and the series in the morning slot flips every 3 posting days.
- Start after the last slot already booked. Before planning IG, check nothing is already posted (see /skool-shorts-schedule).

Ask Ryan for the start date if it is not obvious; never invent one.

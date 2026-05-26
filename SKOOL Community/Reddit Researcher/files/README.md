# Reddit Real Estate AI Demand Research

A multi-agent Claude Code pipeline that mines Reddit for real estate AI demand signals and turns them into a prioritized content strategy for a Skool community and YouTube channel.

## What It Does

1. Deploys dedicated Research Agents across 5-10 real estate subreddits
2. Each agent searches exhaustively using a keyword matrix and extracts structured post data — including a `me_too_count` of how many commenters expressed the same need
3. A QA Agent validates every post for authenticity, relevance, and accurate categorization
4. A Topic Synthesizer counts demand volume per category and produces two ranked priority lists:
   - **Skool Modules** — ranked by demand x solution gap (what to build first)
   - **YouTube Videos** — ranked by demand x frustration (what to film first)

## Quick Start

```bash
cd reddit-research-agents
claude
```

Then say:
```
Read task-prompt.md and execute the full pipeline. 
Use subagents for each Research Agent, the QA Agent, and the Topic Synthesizer. 
You are the Manager Agent.
```

## What You Get

| File | What It Is |
|------|-----------|
| `output/reddit-ai-demand-report.md` | The full report: demand leaderboard, Skool blueprint, YouTube calendar, category deep dives, top 25 posts |
| `output/raw-posts.json` | Every post found across all subreddits |
| `output/scored-posts.json` | QA-validated posts with demand scores |
| `output/by-subreddit/*.json` | Raw data per subreddit |
| `output/run-log.md` | Execution log |

## Customizing

**Add/remove subreddits:** Edit `references/subreddits.md`
**Change search terms:** Edit `references/keywords.md`
**Adjust time range:** Edit the Manager's search parameters in `task-prompt.md`
**Change minimum post target:** Default is 50 qualified posts. Adjust in `task-prompt.md`

## File Structure

```
reddit-research-agents/
├── SKILL.md                  ← Skill definition (for Claude Code skill system)
├── task-prompt.md            ← The orchestration prompt (feed this to Claude Code)
├── README.md                 ← This file
└── references/
    ├── subreddits.md         ← Target subreddits (3 tiers)
    └── keywords.md           ← Search keyword matrix
```

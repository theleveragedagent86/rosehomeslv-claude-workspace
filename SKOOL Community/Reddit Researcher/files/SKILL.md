---
name: reddit-research-agents
description: Spawn a multi-agent research pipeline that mines Reddit real estate and proptech subreddits for posts where users are asking about AI solutions for specific tasks (MLS entry, blog creation, lead outreach, follow-up automation, CRM workflows, etc.). Deploys dedicated Research Agents per subreddit for deeper coverage, a QA Agent for validation, and a Topic Synthesizer that counts demand volume and ranks pain points for Skool community module planning and YouTube content prioritization. Use this skill whenever the user wants to research Reddit for real estate AI demand signals, find pain points realtors are discussing, discover what AI tools agents are asking about, compile market intelligence from Reddit threads, plan content strategy based on actual demand, or prioritize which topics to build courses or videos around. Also triggers for "what are realtors struggling with", "find me Reddit posts about AI for real estate", "research proptech demand on Reddit", or "what should I build my Skool community around."
---

# Reddit Real Estate AI Demand Research — Multi-Agent Pipeline

This skill orchestrates a multi-agent system via Claude Code to mine Reddit for posts where real estate professionals are asking about AI solutions for specific workflow tasks, then synthesizes findings into a demand-ranked content strategy.

## Architecture

```
                    ┌──────────────────────┐
                    │    MANAGER AGENT     │
                    │  Orchestrates all    │
                    │  agents, merges      │
                    │  data, gap-fills     │
                    └──────────┬───────────┘
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
   ┌────────▼────────┐ ┌──────▼──────┐ ┌────────▼────────┐
   │ RESEARCH AGENTS │ │  QA AGENT   │ │ TOPIC SYNTH     │
   │ (1 per subreddit)│ │ Validate &  │ │ Count demand,   │
   │                  │ │ score posts │ │ rank for Skool  │
   │ r/realtors       │ │             │ │ + YouTube       │
   │ r/RealEstateTech │ └─────────────┘ └─────────────────┘
   │ r/RealEstateAg.. │
   │ r/realestate     │
   │ r/CommercialRE   │
   │ + Secondary/     │
   │   Tertiary as    │
   │   needed         │
   └──────────────────┘
```

**Why one Research Agent per subreddit:**
Each sub has different posting culture, terminology, and audience mix. r/RealEstateTechnology is almost entirely tool discussion. r/realestate mixes consumers and agents. r/CommercialRealEstate has completely different workflow pain points. Dedicated agents can adapt search strategy and filter criteria per community.

## Key Innovation: me_too_count

The most valuable metric in this pipeline is `me_too_count` — the number of commenters on a post who express the same need ("same", "I need this too", "following", "+1"). This captures demand volume beyond just the original poster and is the primary input to the demand scoring formula.

## Key Innovation: Demand Score Formula

```
demand_score = (post_count x 2) + total_me_too_count + (avg_comments x 0.5)
```

This produces a single number per category that answers: "How many real people are actively asking about this?"

## Output: Two Ranked Priority Lists

The Topic Synthesizer produces:

**LIST A — "BUILD THIS FIRST" (Skool Modules)**
Ranked by: demand_score x solution_gap
Highest demand + least existing solutions = build first

**LIST B — "FILM THIS FIRST" (YouTube Videos)**
Ranked by: demand_score x frustration_index
Highest demand + most frustrated people = most clickable content

## How to Run

See `task-prompt.md` for the complete orchestration prompt. In Claude Code:

```bash
cd reddit-research-agents
claude
> Read task-prompt.md and execute the full pipeline using subagents.
```

## Reference Files

- `references/subreddits.md` — 15+ target subreddits in three priority tiers
- `references/keywords.md` — Intent signal x task domain keyword matrix

## Output Files

```
output/
├── reddit-ai-demand-report.md    ← Main deliverable with demand leaderboard,
│                                    Skool blueprint, YouTube calendar
├── raw-posts.json                ← All posts from all Research Agents
├── scored-posts.json             ← QA-validated and scored posts
├── by-subreddit/                 ← Per-subreddit raw data
│   ├── realtors.json
│   ├── RealEstateTechnology.json
│   ├── RealEstateAgents.json
│   ├── realestate.json
│   └── CommercialRealEstate.json
└── run-log.md                    ← Execution log with per-agent stats
```

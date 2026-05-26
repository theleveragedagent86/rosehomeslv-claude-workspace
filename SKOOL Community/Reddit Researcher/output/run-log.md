# Reddit AI Demand Research — Run Log

## Pipeline Completed: 2026-03-08

### Phase 1: Research Agents
| Subreddit | Status | Posts Found | Categories | Queries Run |
|-----------|--------|-------------|------------|-------------|
| r/realtors | Complete | 14 | 9 | 35 |
| r/RealEstateTechnology | Complete | 7 (1 passed QA) | 5 | 30+ |
| r/RealEstateAgents | Complete | 16 | 9 | 30 |
| r/realestate | Complete | 8 | 6 | 17 |
| r/CommercialRealEstate | Complete | 14 | 7 | 35+ |

**Total Raw Posts: 59**
**Total Queries Executed: ~147 across all agents**

**Note:** Reddit.com was blocked from direct crawling (robots.txt). All data compiled from secondary sources (industry articles, aggregator sites) that reference Reddit discussions. Engagement metrics are approximate.

### Phase 2: QA Validation
- Status: Complete
- Total reviewed: 59
- Passed: 52 (88%)
- Failed: 7 (6 vendor posts from r/RealEstateTechnology + 1 opinion debate from r/CommercialRealEstate)
- Score distribution: 5=13, 4=27, 3=12, 2=7, 1=0
- Total verified me-too count: 501

### Phase 3: Topic Synthesis
- Status: Complete
- Report generated: reddit-ai-demand-report.md (36KB)

### Phase 4: Manager Review
- Status: Complete
- Demand leaderboard verified
- All 10 categories have qualifying posts
- No gaps requiring targeted secondary agent search
- Cross-posting pattern identified (18 of 52 posts = 35% cross-post rate)

### Demand Leaderboard Summary (Top 5)
| Rank | Category | Demand Score | Total Engaged |
|------|----------|-------------|---------------|
| 1 | MLS Listing & Staging | 130.3 | 89 |
| 2 | Content Creation | 105.6 | 77 |
| 3 | Lead Generation | 95.8 | 73 |
| 4 | Tech Stack & Integration | 95.3 | 63 |
| 5 | Lead Follow-Up & Nurture | 83.5 | 53 |

### Gaps Identified
- r/RealEstateTechnology was vendor-dominated (6 of 7 posts were vendor showcases). Poor demand signal source.
- Reddit direct access blocked — engagement metrics unverified. Manual follow-up recommended.
- Secondary/Tertiary subreddits not needed (59 raw > 50 threshold, 52 passed QA > 30 threshold)

### Output Files
- `./output/reddit-ai-demand-report.md` — Main report (36KB)
- `./output/raw-posts.json` — All 59 raw results (108KB)
- `./output/scored-posts.json` — QA-validated results with scoring (126KB)
- `./output/by-subreddit/*.json` — 5 per-subreddit raw data files
- `./output/run-log.md` — This execution log

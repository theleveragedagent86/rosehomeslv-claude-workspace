# What Ryan has actually built and runs

Ground truth for the "Ryan built it?" column in the translation matrix. Sourced from installed skills in `~/.claude/skills/` and installed plugins in `~/.claude/plugins/marketplaces/local-desktop-app-uploads/` as of 2026-08-03. These are running systems, not plans.

**Rule: a matrix row may only be marked "built" if it maps to something on this list.** Anything else is BUILD QUEUE or DROP. Ryan's credibility with agents rests on "I run this in a real Vegas brokerage," not "I watched a video about it."

## Lead capture and conversion

| System | Skill | Saraev analog |
|---|---|---|
| Comparative market analysis, buyer side | `cma` | client deliverable automation |
| Seller CMA / listing presentation | `seller-cma` | proposal SaaS |
| Expired listing pipeline, email pull to mailing list | `expired-workflow` | lead scraping |
| Agent-to-agent reverse prospecting broadcasts | `reverse-prospecting` | cold email outreach |
| Weekly client-facing seller performance report | `weekly-update` | client retention / reporting |

## Content engine

| System | Skill | Saraev analog |
|---|---|---|
| Blog posts, Vegas neighborhood content | `blog-writer` | content automation |
| Publish to Lofty CMS | `publish-blogs`, `publish-buyer-guide`, `publish-landing-page` | publishing pipeline |
| Weekly local news video scripts, green screen | `local-news` | faceless content system |
| Long-form YouTube, research to script to build prompt | `yt-long`, `youtube-manager` | YouTube automation |
| Local SEO audits and page generation | `local-seo` | SEO productization |
| New construction community research and buyer guides | `new-construction` | niche research system |
| Listing marketing plans, emails, neighbor letters | `listing-marketing` | offer/deliverable stack |
| Listing and property video from photos | `listing-video` | video automation |

## Social distribution

| System | Skill / plugin | Saraev analog |
|---|---|---|
| Instagram carousels, Coffee and Contracts templates | `ig-carousel` | carousel content system |
| Instagram engagement routine on Vegas accounts | `ig-engage` | the N8N Instagram parasite system |
| Instagram target account discovery | `ig-research` | lead scraping |
| Meta / Instagram listing ads, lead forms to Lofty | `ig-ads` | paid acquisition |
| Inbound DM to followers and likers, inbound comments | `inbound-dm-followers`, `inbound-dm-likes`, `inbound-comments`, `inbound-research` | auto-DM systems |
| Reddit comment routine and r/VegasRealtor weekly posts | `Reddit`, `subreddit-post` | community-led growth |
| Short-form video | `claude-shorts` | shorts pipeline |

## Ops

| System | Skill | Note |
|---|---|---|
| Daily checklist and calendar | `daily-checklist` | personal ops, also drives transaction coordination below |
| Skill discovery menu | `menu` | internal |
| Skill authoring and auditing | `skill-builder` | this is how new modules get built |

## Added 2026-08-03 after disk verification

These were missing from the first pass. Status re-checked directly, because `_System/plugins/` holds dev/source copies while the running versions live in `~/.claude/`. Presence in `_System/plugins/` alone does NOT mean a thing runs.

| System | Skill | Status |
|---|---|---|
| Transaction coordination, per-address cadences and templates | `transaction-coordination` (`_System/plugins/tc-plugin/`) | **LIVE with real data.** The plugin is not installed, but the installed `daily-checklist` reads its `active-transactions.json` and surfaces TC actions daily. Currently 3 active deals: 3550 All Hallows (buyer-new-construction), 8320 Moapa Water (buyer-resale), 29 Amber Rock (seller). 5 transaction folders on disk. This means Module 2 is not theory, it runs. |
| Landing page / asset generation | `digital-cannonball` | **LIVE.** Installed plugin. |
| Diagrams | `excalidraw` | **LIVE.** Installed plugin. |
| MLS listing remarks to fixed structure and voice | `listing-description` (`_System/plugins/listing-description-plugin/`) | **BUILT, NOT INSTALLED.** Dev copy only, not referenced by any installed skill or plugin. Ryan cannot invoke it today. Does NOT qualify as "built" for matrix purposes until installed. Installing it is a small task and would immediately add a YES row. |

## AI consulting clients (proof that the model sells)

Live client work in `AI Clients/`: Brian Esposito (first responder + lender engagement plugins), Nick Nolf Prop. Mgmt, Crystal (website), Zbuyer.

This matters for the T4-THESIS videos. Saraev argues in "Why I Don't Sell AI to Local Businesses" that the local-business model is bad. Ryan has paying local-business clients. That is a direct, evidenced counterexample and it is the strongest content angle available to him.

## Honest gaps

Revised 2026-08-03 after the deep-reads and disk verification. The original gap 2 was wrong and has been replaced.

1. **Missed-lead speed-to-response.** Inbound call or form to text back in under 5 minutes. Nothing covers this. Highest content value and highest buildability.
2. **An eval / QA layer.** Nothing scores any skill's output before Ryan sees it. He has rules in CLAUDE.md but no scorer. Two deep-reads point straight at this, `8rVQuZlRaqo` (scored checklist) and `qKU-e0x2EmE` (automated prompt optimization). In a licensed business where fair housing and MLS rules apply to published copy, this is a bigger hole than cold email.
3. **Database reactivation** at scale against past clients and sphere.
4. **Cold email infrastructure.** Demoted to last. Saraev's own three-niche test put real estate dead last at 0% positive reply across 510 emails and he killed the campaign on camera in `wLNw-rpklfE`.

~~Transaction coordination~~ is NOT a gap. Verified live above with 3 active deals. What is genuinely still open in that area is contract generation and e-sign, which is brokerage platform territory and not worth building.

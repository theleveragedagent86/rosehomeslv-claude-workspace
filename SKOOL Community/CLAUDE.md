# CLAUDE.md — SKOOL Community ("The Leveraged Agent")

This folder is the **Skool community business — "The Leveraged Agent"** — Ryan's coaching/course brand that teaches real estate agents to run their business with AI. It is a **separate business** from Rose Homes LV (the actual real estate practice) and from the AI Clients agency. Different audience (agents, not home buyers/sellers), different brand.

**Heads-up: this is the largest folder on disk** (~80 GB) because of `Final Videos/`. Those rendered videos are git-ignored and should be archived to the external SSD (see the SSD checklist / root `.gitignore`). Keep only active project files local.

## Working here

- The voice targets **agents/entrepreneurs**, not Las Vegas home buyers. Do not apply the Rose Homes LV realtor content rules here unless a specific asset calls for them.
- Course modules, the VSL, and launch walkthroughs are the product — treat them as canonical curriculum, version carefully.

## Active project: the Claude Code Course for Realtors

Ryan is **replacing the module-based classroom with one flagship course**, built in [`Claude Code Course for Realtors/`](Claude%20Code%20Course%20for%20Realtors/). Structure and sequencing are modelled on Jack Roberts' Skool classroom; none of his copy is reused. The competitor archive that informed it is in [`Jack Roberts AI Course/`](Jack%20Roberts%20AI%20Course/).

**Decisions locked 2026-08-24, do not re-litigate:** one classroom tile, not ten. Level 0 through Level 10 plus three short bonus "OS" drops outside the numbering. The carried artifact is the **Business Brain** folder, which every level adds a layer to. **Claude Code throughout**, no browser-Claude fallback path; Cowork appears only in bonus drop B1 for scheduled routines and browser work. Jack's "website" level becomes **Landing Pages**. The `CLAUDE.md` framework taught in Level 1 is **BROKER** (Business, Range, Output, Keep out, Escalation, Results).

The new ladder **absorbs the existing modules**: Module 0 retires into Levels 1/2/4, Module 1 compresses into Level 5, Module 2 into Level 6, Open Houses into bonus B2, the planned social module into bonus B3. Those `Module-*.md` files are still here and stay until the ladder is recorded. Start at [`Claude Code Course for Realtors/COURSE-MAP.md`](Claude%20Code%20Course%20for%20Realtors/COURSE-MAP.md); read that folder's `CLAUDE.md` before working in it.

---

## Folder Map — keep this current

```
SKOOL Community/
├── Module-0-Start-Here.md · Module-1-Listing-Launch-Package.md · Module-2-AI-Transaction-Coordinator.md
├── Module-Open-Houses.md   Open Houses module overview (name, description, cover, lesson index; no number, styled like Listing Launch Package)
├── Open-Houses-Post-Open-House-Outbound.md   Skool lesson-post copy for the Open Houses module's first (follow-up) video
├── Open-Houses-Lesson-Promo-Pack.md · Open-Houses-Lesson-Door-Knock-Invite.md · Open-Houses-Lesson-Geo-Ads.md · Open-Houses-Lesson-Circle-Prospecting.md   4 promotion-stage lesson posts (each has a YouTube package + 5 Instagram Shorts in Scripts/); grounded in Mackin/Pantana/Ferry/Tse
├── Open-Houses-Announcement-Post.md   Skool community-feed announcement post for the Open Houses module launch
├── Sellers-Announcement-Post-Weekly-Seller-Update.md   Skool community-feed announcement post for the Sellers module launch (Weekly Seller Update lesson)
├── Open-House-Reconnection-Prompt/   downloadable interview-style reconnection prompt (.md) + branded "how to use" guide (.html source → PDF) for the Open Houses module
├── The-Leveraged-Agent-Setup-Plan.md · VSL-Script-Main-Page.md · YouTube-Launch-Walkthrough.md
├── Cowork-Audit-Prompt.md · RESUME-2026-04-29.md
├── Cowork-Prompt-Community-Fixes.md   PASTE-READY Cowork prompt that executes the audit's
│                              "Today/This week" fixes on the live Skool. 5 phases: create Intros +
│                              Q&A categories, Calendar decision, publish-or-hide Listing Launch
│                              Package, replace the pinned welcome post, post + seed the pinned task
│                              thread, DRAFT (never send) 7 member DMs. All public copy is written out
│                              verbatim in the prompt so Cowork never authors. 3 DECISIONS at the top
│                              Ryan must fill in first. Hard rules: no deletes, no billing, no sending.
├── Community-Audit-2026-09-01.md   live audit of skool.com/the-leveraged-agent-7674. 11 members,
│                              8 posts ALL by Ryan, 0 member posts ever, dark since Jul 17. The pinned
│                              welcome post routes to 3 things that don't exist (Welcome & Intros, Q&A,
│                              Calendar tab); About sells weekly live calls that aren't happening;
│                              Listing Launch Package is in DRAFT; feed sells the Cowork/Module ladder
│                              being replaced and names stale models. Ordered fix list. Bottleneck =
│                              recording Level 0 + 1, not writing. DO NOT turn the IG/YT funnel on first.
├── Session-Record-Community-Fixes.md   what actually got executed on the live Skool, Sept 1 and
│                              Sept 8 2026, from Cowork-Prompt-Community-Fixes.md. Records Ryan's
│                              three decisions (D1 = no calls, kill the Calendar promise; D2 = leave
│                              Listing Launch Package in Draft, which already hides it; D3 = his
│                              three seed comments), the two categories created, both pinned posts
│                              rewritten, the task thread posted + pinned + seeded, all 8 member DMs
│                              sent verbatim, 18 dash fixes, model version numbers dropped, and the
│                              sidebar rewrite. Read this before touching live Skool copy.
├── Skool-Pro-Plan-2026-09-11.md   the $99/mo Skool Pro feature inventory + sequenced plan, read
│                              live 2026-09-11. HEADLINE: Freemium is live and BUYABLE at /plans,
│                              Premium $86/m and VIP $1,500/m, and Premium's four bullets promise a
│                              prompt library, monthly new workflows, a members-only channel and
│                              early access that DO NOT EXIST. Full Pro inventory: 7 of 9 Pro
│                              plugins off (Auto DM, Links, Instant approval, Zapier, Webhook, Meta
│                              pixel, Google ads, Cancellation video), custom URL unclaimed,
│                              Affiliates off, Calendar + Map tabs off, "New customer email"
│                              notification off, onboarding video is probably Skool's stock clip,
│                              0 reviews, $0 MRR on 15 free/lifetime members. Also: 3 live
│                              em-dashes on the About page + Open Houses course description that
│                              the Sept 1 feed sweep missed, 15 unread membership-question answers
│                              that already name each member's #1 time waster, and overdue builds
│                              promised to Jessica Martin and Tausha Rodriguez. 4 phases; phase 3
│                              is still recording Level 0 + 1.
│                              PHASE 1 EXECUTED 2026-09-11, logged at the bottom of that same file.
│                              Ryan kept both paid tiers, so items 1-2 were skipped. Done: Auto DM
│                              on with the Group A message, Instant approval on, "New customer
│                              email" on, all 3 sidebar links live, 5 em-dashes fixed (2 more than
│                              the plan had found, incl. Ryan's own profile bio), onboarding video
│                              plugin turned OFF because the loaded clip was Skool's stock demo.
│                              **THE COMMUNITY URL IS NOW `skool.com/the-leveraged-agent`**, the
│                              `-7674` suffix is retired (old links redirect; further changes cost
│                              $100 each). **The Leveraged Agent IG is `@the.leveraged.agent`, WITH
│                              DOTS**; the dotless `@theleveragedagent` on Instagram belongs to
│                              somebody else, while on YouTube dotless IS Ryan's real channel
│                              (`youtube.com/@theleveragedagent`). Forward-facing workspace files
│                              were rewritten to match; the dated audit/record docs deliberately
│                              keep the old URL.
├── Skool-Onboarding-Video-Script.md   word-for-word 60 second script for the Skool Onboarding video
│                              plugin, written 2026-09-11. NOT the About-page VSL: that 6:23 clip sells
│                              the join and was rejected for this slot because it re-sells a decision
│                              already made. This one does a single job, send them to the pinned thread
│                              to comment the one task they'd hand off. 189 words, 65-68 sec, one take
│                              on a phone, no sting and no music. Carries a 172-word tighter cut and the
│                              upload steps. NOT RECORDED; the plugin stays OFF until it is.
├── Skool-Welcome-DM.md         the new-member onboarding DM system. Part 1 = the evidence, all 8
│                              welcome DMs Ryan got joining other Skools (Jack, Lanie, Florian, Tommi,
│                              Saraev, Chase, BAMx, Nate Herk); he replied to none. Part 2 = the system.
│                              Core move: the DM asks ONE question (what task is repetitive), then Ryan
│                              hands their own answer back and says paste it into the community, so the
│                              post is transcription not composition. Never ask for the post cold, never
│                              say "pain point". Also: the 6-line post template, the pinned "one task
│                              you'd hand off" comment thread (lower friction, higher volume), the
│                              second post ask AFTER the Level 0 win, and the post-it-I-build-it engine
│                              that feeds level order + content + case studies. NOT SENT YET
├── Post Open House Outbound-4K.mov   loose 4K master (git-ignored → archive to SSD)
├── Sellers-Module/             the Sellers module (cover = Brandkit/Classroom-Covers/08-sellers.png, no
│                              module number on it). Meant to hold every seller workflow, listing appt to
│                              closing. Lesson-Weekly-Seller-Update.md = first lesson page, Jack Roberts
│                              format, 24 timestamps off Ryan's 18:30 recording; images/ = the cropped
│                              29 Amber Rock report used as the top image. The prompt + PDF it attaches
│                              live in Claude Code Course for Realtors/05-Level-5-Listing-Launch/.
├── Brandkit/                   CANONICAL Leveraged Agent brand: light + dark logos, banner, brand guide
│                              (Design-System/ = THE BUILD SOURCE, extracted 2026-09-01 from Ryan's
│                               Claude Design project "Leveraged Agent, classroom tiles": v2.0 Vector
│                               tokens, la-components.css, the <la-logo> web component, self-hosted
│                               Barlow/Raleway/Inter woff2, and build-assets.mjs. EVERY brand image
│                               in Brandkit is rendered from it, so edit the source and rerun
│                               `node Design-System/build-assets.mjs`, never retouch a PNG.
│                               Logos/ = the v2.0 logo set, PNG + SVG masters with the fonts embedded.
│                               YouTube-Banner/ = the 2560x1440 channel banner source.
│                               v1-archive/ = the retired cream/teal/gold cover + icon, reference only.
│                               The 5 canonical root PNGs were REGENERATED IN PLACE on 2026-09-01;
│                               the ~29 bundled copies under hyperframes-student-kit/video-projects/
│                               */assets/ are deliberately still v1, because those compositions are
│                               still on v1 teal gradients)
│                              (incl. YouTube-Bumpers/ = the 3s intro sting (plus bumper-9x16.mp4, the vertical twin from compositions/bumper-vertical.html, used as the end tag on Reels/Shorts) + two transparent
│                               like/subscribe overlays (6s mid-roll, 20s ending) used on every
│                               YouTube upload, hyperframes HTML in / video out. Overlays are alpha
│                               ProRes and composite over recorded footage. The full-frame end card
│                               was DELETED 2026-08-24. The ending overlay is the approved wordmark
│                               panel plus the Like + Subscribe chips, all in the left column, and
│                               it holds still after the entrance. YouTube only, deliberately NOT
│                               used on Skool lessons)
│                              (Brand-Guide/ = CANONICAL v2.0 "Vector" palette in tokens.css/.json,
│                               ADOPTED 2026-08-19: white base, TRUE-black dark surface, one blue
│                               accent #1768E5, Barlow 800 / Raleway 600 / Inter. BRAND-GUIDE.md is
│                               the written spec. tokens-v1.css/.json = the RETIRED v1.0 cream / teal
│                               / gold, archived verbatim. brand-guide.html is STALE, it hardcodes v1
│                               hexes. Dead proposals kept as files: v2 Voltage + Ember, v3 Broker
│                               (V3-BROKER.md), v4 losers Ultramarine + Meridian + Signal + Ivory.
│                               Rejected and DELETED 2026-08-19: Rosewood, Crimson, Sovereign.
│                               V4-PALETTES.md = the full decision record; v4-final.html = the 3-way
│                               decision page; v4-fonts.html = the type decision page (P08 = Ryan's
│                               pick); v4-weights.html = the headline weight page (800 confirmed);
│                               v4-preview.html and v4-type.html are superseded and stale;
│                               PEDIGREE-BRAND-RESEARCH.md + pedigree-board.html = measured brand
│                               research on 10 top US brokerages. EVERY logo file is v1 artwork and is
│                               now OFF-PALETTE; regeneration not started),
│                              YouTube thumbnail template (UNTOUCHED, Ryan locked it for CTR
│                               2026-07-16, so it is still system-font 900 not Barlow 800),
│                               Skool classroom-cover template (REBUILT 2026-09-01 on v2.0: type
│                               only, black field, no icon and no gradient; 9 covers rendered,
│                               Modules 01-09 (08 = Sellers, 09 = Resources, both 2026-09-17, no module number). NOTE they do not match the live classroom or the
│                               "one tile, Level 0-10" course decision, reconcile before uploading)
│                                → Brandkit/CLAUDE.md
├── Scripts/                    content scripts (per-lesson YouTube packages + IG/YouTube shorts; open house promo set = YouTube-Package-Open-House-*.md + Open-House-*-Instagram-Shorts.md + Open-House-Promotion-YouTube-Shorts-Descriptions.md; Saraev rebuttal set = YouTube-Package-Saraev-Rebuttal.md (beat outline, titles, thumbnail, compliance) + Saraev-Rebuttal-Teleprompter.md (full word-for-word read), both sourced from Mentor-Mining/); YouTube-Package-Weekly-Seller-Update.md = Level 5 weekly seller update YouTube cut (titles, description, chapters, tags, pinned comment; prompt deliberately NOT linked, Skool only) + Weekly-Seller-Update-Instagram-Shorts.md (5 scripts + captions, each with a B-roll timestamp from the long video; the paste-ready IG Reel captions for the clipped Reels are in their own file, Weekly-Seller-Update-Instagram-Reel-Captions.md, long-form local-news caption format, 250-400 word bodies, no hashtags); Open-House-Lead-Automation-Instagram-Reel-Captions.md = same-format paste-ready captions for the 12 clipped Final Videos/Open-House-Reel-*.mp4 (visitor, coworker and landmark kept anonymous); Shorts-Build/ = clipped-Reel builds: weekly-seller-update/ (build.py + caps.mjs + words.json CUT 12 real clips from the raw Sept 17 footage, screen top / face bottom, Barlow captions, 9:16 bumper end, into Final Videos/Weekly-Seller-Update-Reel-NN-*.mp4, + covers/cover-01..12.png) and open-house-lead-automation/ (same pipeline, 12 face-only clips from the raw July 14 Final Cut media into Final Videos/Open-House-Reel-NN-*.mp4, prospect name/phone kept out, + covers/), and reel-covers/ = the shared cover template (cover.html SETS + shoot.mjs, alternating black/white for the grid); Thumbnails/<slug>/ = per-video Leveraged Agent YouTube thumbnails (open-house-lead-automation/, weekly-seller-update/ with brief.md, thumb-a/b .html+.png, squint proofs, shoot.mjs)
├── Instagram/                  Skool-brand IG content (separate from Rose Homes LV IG); prospect
│   │                          research TSVs + Outreach-Plan.md live at its root.
│   │                          Posting-Times-Research.md = when realtors are on IG (2026-09-21),
│   │                          from 21K realtor comments in Competitor-Research/: post 5-6pm PT,
│   │                          optional 5am PT, best days Sun/Mon/Sat, weakest Thu/Fri
│   ├── Competitor-Research/   teardowns of other agent-facing IG accounts, one folder per account.
│   │                          Peyson-Robertson/ = @peyson.robertson (29.8K, Coachella Valley team +
│   │                          "Obsidian" bootcamps), harvested 2026-09-01 via IG's own web API from
│   │                          a logged-in session. 556 posts with full captions + metrics, 45,969
│   │                          comment rows (37,967 third-party) and 49,709 liker rows =
│   │                          33,738 unique accounts, nearly all realtors. STRATEGY-TEARDOWN.md is
│   │                          the analysis: the whole account is ONE mechanism, a comment-keyword
│   │                          DM funnel worth 11-12x on comments, carousels convert 3x reels,
│   │                          AI/Claude is his best topic (214 median comments) and motivational
│   │                          posts are 30% of output for 7% of return. Ranked outreach lists
│   │                          A-E + TOP-300-DM-TARGETS.csv. Raw JSON in data/ so lists can be
│   │                          re-cut. Prospects, not leads: follow and engage before DMing.
│   │                          Whitney-Bartlette/ = @whitneybartlette.social (932.6K, general
│   │                          creator/biz coach, NOT realtors: only 3.8% of captured accounts carry
│   │                          a realtor name signal), harvested 2026-09-09. 228 of 994 posts
│   │                          (18 Feb 2025 - 9 Sep 2026, dense from Dec 2025), 18,149 comment rows
│   │                          and 22,568 liker rows = 28,461 unique accounts. Post enumeration is
│   │                          grid-scrape only, the feed endpoint is dead, so this is 23% of the
│   │                          account and never the whole thing. Headline: same keyword-to-DM
│   │                          mechanic as Peyson (4.8x on reels, 5.2x on carousels) but FULLY
│   │                          AUTOMATED, 17 of 18,149 comments are her own replies, and 58% of all
│   │                          human comments are people typing a trigger word. 932.6K followers
│   │                          against a $29/mo Skool with 133 members = 0.014% conversion. Her AI
│   │                          posts convert 4.4x her median topic and pulled 2,720 opt-ins off
│   │                          seven asks, while her paid-community keyword SHIFT pulled 220 off
│   │                          seventeen. She sells no AI product. That gap is the opening for The
│   │                          Leveraged Agent.
│   │                          Kristi-Jencks/ = @kristijencks (13.4K, verified, Tom Ferry senior
│   │                          coach + Phoenix agent, builds "Claude for Agents" with husband
│   │                          Merrill Jencks), harvested 2026-09-09. PARTIAL: post half only.
│   │                          238 posts (29 Jan - 9 Sep 2026) with full captions + metrics in
│   │                          data/kj_posts_meta.json; NO people lists, the bulk commenter/liker
│   │                          harvest was refused by the session permission classifier and IG's
│   │                          /feed/user/ endpoint is dead (grid scrape + shortcode decode
│   │                          instead). Closest direct competitor to The Leveraged Agent: same
│   │                          avatar, same software, teaching Claude to agents right now.
│   │                          Headline: same keyword-to-DM mechanic (14x lift on carousels,
│   │                          9.2x on reels) at ~1/14th Peyson's yield. Median post = 3 comments,
│   │                          32% get zero, top 5 posts hold 49% of all comments. Volume up 5x
│   │                          this year, median engagement flat. Ladder has a hole: free
│   │                          newsletter, then $500/$750 one-off AI sessions, no community rung.
│   │                          Kimberly-Prince/ = @kindlykimberly (11.5K, verified, Sacramento
│   │                          luxury/relocation REALTOR at eXp, founder of The REDD Group,
│   │                          hosts "In Your Neighborhood" on @gooddaysac), harvested
│   │                          2026-09-10. 216 of 1,337 posts (24 Jan 2025 - 9 Sep 2026, grid
│   │                          scrape so Feb-Apr and Sep 2025 are missing), 1,821 human comment
│   │                          rows = 1,136 unique commenters, 13,205 liker rows = 5,291 unique
│   │                          likers. Like counts are HIDDEN on this account, the likes columns
│   │                          are a harvested liker sample (median 61/post), not real likes.
│   │                          Headline: the keyword-to-DM mechanic again, but the keyword has to
│   │                          NAME THE THING. Unique property keywords (NEWCASTLE, PENRYN, BARN)
│   │                          are 17% of posts and 40% of all comments, median 12; generic
│   │                          keywords (LOCAL, BUY, REDD) median 3, which is WORSE than posting
│   │                          no CTA at all (4). 2.2x lift on reels, 0.6x on carousels. She is a
│   │                          listing agent who recruits, not a coach: 75% of posts are consumer
│   │                          facing and outperform her agent-facing 25% on reach and comments.
│   │                          Ladder is $17 checklist, $34 playbook, $97/mo Powerhouse Try On
│   │                          (Amy Gregory's product, not hers), then join eXp under REDD.
│   │                          Openings: she names AI as the lever in 7 posts and teaches none of
│   │                          it, her top rung needs a brokerage switch, and she is geo-anchored
│   │                          to Sacramento + Newport Beach. 367 agent-facing commenters (97 with
│   │                          a realtor name signal) in LIST-B, which is the hot list here
│   │                          because LIST-A only has 21 people.
│                          NEWSLETTER-TEARDOWN.md = the OTHER half of his funnel, added
│                          2026-09-01 from 8 forwarded issues of his weekly email "IN THE
│                          TRENCHES" (Jul-Aug 2026, raw text in data/). Instagram acquires,
│                          the EMAIL sells: a fixed 9-block template, three stacked offers
│                          every issue (7 Figure Agent Club mastermind, Obsidian Group team
│                          recruiting, the paid Obsidian Bootcamp with a public seat counter),
│                          a reply-for-the-Zoom-password trigger, and a Freddie Mac + "My take"
│                          market block. KEY FINDING: his paid mastermind spent the summer
│                          teaching Claude Code, Cowork, ManyChat and AI clones, so the
│                          "he only teaches Claude at a surface level" note in
│                          STRATEGY-TEARDOWN.md applies to his PUBLIC content only.
│   └── Carousels/             finished carousels from /skool-carousel. Per carousel: a .md (copy,
│                              design brief, DM reply), render.html + shoot.mjs (Playwright), and
│                              png/ with the 1080x1350 slides. dm-reply-*.txt = IG saved-reply text,
│                              claude-design-prompt.md = paste-ready Claude Design build prompt.
│                              Carousel 01 (Transaction Coordination) was REBUILT 2026-08-20 on
│                              v2.0 Vector with 9 inline-SVG line illustrations, Barlow 800 /
│                              Raleway 600 / Inter, and black covers at slides 1/7/9; it uses a
│                              typographic wordmark because every logo PNG is still v1 art.
│                              REDESIGNED 2026-09-15 as render-v3.html + shoot-v3.mjs -> png-v3/,
│                              which is now the SHIP VERSION; render.html is the 2026-08-20 cut,
│                              kept for reference. v3 keeps Vector but adds the frame the newer
│                              carousels use: 96/120/190 safe band so nothing is corner-pinned, a
│                              full-bleed progress rail, a 420px ghost numeral bleeding off the
│                              right edge, and an eyebrow row naming each slide's beat. Black bands
│                              moved to 1/4/7/9. The .md's DESIGN BRIEF was rewritten at the same
│                              time; it used to spec the RETIRED v1 cream/teal/gold + Poppins. A
│                              real client address on the slide-6 email mock was swapped for a
│                              placeholder.
│                              render-v1-archive.html = the retired v1 cream/teal/gold, CSS-box,
│                              03-listing-automation/ and 04-reel-hooks/ added 2026-09-11: the
│                              first carousels built on the Whitney Bartlette numbered-list
│                              finding (count in the cover, the list IS the deliverable, no
│                              keyword gate, save/share CTA). 7 and 6 slides, not the usual 9.
│                              Each now carries design/ = the .dc.html artboards, gen.mjs,
│                              canvas.json and rendered png/. Both are published as Claude
│                              Design canvases. Every slide sits in the 4:5 safe band
│                              (padding 152/64/166, nothing corner-pinned) so it survives the
│                              1:1 profile-grid crop; check with check-slides.mjs in the
│                              skool-carousel skill.
│                              zero-illustration version, reference only, do not ship from it.
│                              TC-folder-structure.md + transaction-template.json = the lead
│                              magnet the "DM me TC" saved reply (tc2) promises. Sanitized mirror
│                              of _System/plugins/tc-plugin; keep them in sync if that skill's
│                              schema or cadences change. No real client addresses in either file.
│                              02-business-brain/ = the Business Brain carousel, Ryan's answer to
│                              Peyson Robertson's top-performing carousel (see Competitor-Research/).
│                              9 slides, dark at 1/7/9, built as Claude Design artboards
│                              (Main.dc.html + S02..S09 + Caption.dc.html + canvas.json), seeded to
│                              business-brain-carousel.html and published as a canvas Artifact. No
│                              PNGs rendered yet. Caption sheet carries the caption, 4 alternate
│                              hooks, the BRAIN keyword reply, and a bracketed receipt line that
│                              stays out unless Ryan has the real numbers.
│                              MANYCHAT-BRAIN-FLOW.md = the full ManyChat automation for the
│                              BRAIN keyword: triggers, 6 rotating public comment replies, DM 1
│                              through DM 5 verbatim (all under IG's 1000-char cap), the Skool
│                              follow-up at +20h, the day-3 hand-sent Human Agent message, tags,
│                              custom fields, 24h-window rules and guardrails. Supersedes the
│                              manual saved-reply pattern in ../dm-reply-TC.txt.
│                              BUSINESS-BRAIN-STARTER.md = the deliverable the DM promises, the
│                              folder tree + paste-ready BROKER CLAUDE.md + starter skills +
│                              level ladder + a Leveraged Agent links block + compliance footer.
│                              Publish as a view-only Doc/PDF, NOT behind a Skool signup.
│                              3 links still NOT FOUND and must be filled before posting:
│                              YouTube URL, Leveraged Agent IG handle, the published asset URL.
├── Reddit Researcher/          Skool-brand Reddit research (has its own .claude)
├── Claude Code Course for Realtors/   RYAN'S FLAGSHIP COURSE BUILD. One Skool classroom tile,
│                              Level 0-10 + 3 bonus "OS" drops, ~5h40m across 14 videos. Carried
│                              artifact = the Business Brain folder. Claude Code only (Cowork lives
│                              in bonus B1). Absorbs Module 0/1/2 + Open Houses + planned social.
│                              Spine docs: COURSE-MAP.md (index), COURSE-ARCHITECTURE.md (the
│                              ladder + why), LESSON-TEMPLATE.md (9-block Skool description
│                              template), DELIVERY-PLAYBOOK.md (on-camera template). Each
│                              <NN>-Level-N-*/README.md holds a paste-ready Skool description on
│                              top and production notes below the rule. Levels 0 and 1 also have
│                              SCRIPT.md (word-for-word teleprompter read with deck + Claude Code
│                              cues) and a matching deck in deck/ (Vector v2.0 inverted, true-black scrolling
│                              deck served off serve.rb on :8091, arrow keys advance, ?s=N deep
│                              links to a slide). YouTube/ holds the cut-down funnel versions of
│                              the levels, which are NOT the same scripts. Instagram/ holds 12
│                              Reels per level (Levels 0 and 1 so far) that feed those videos,
│                              plus Carousels-Build-Drops.md, 10 keyword carousels built on the
│                              Kristi Jencks format finding. Level 5 also holds
│                              Weekly-Seller-Update-Prompt/ (Plan-Mode prompt + how-to-use PDF).
│                              WRITTEN, NOT RECORDED.
│                              Start at COURSE-MAP.md  → Claude Code Course for Realtors/CLAUDE.md
├── Jack Roberts AI Course/     COMPETITOR COURSE ARCHIVE, not Ryan's content. Complete local
│                              capture (2026-08-23) of Jack Roberts' "🤖 Claude Code Course" from
│                              skool.com/aiautomationsbyjack. 25 lessons / ~10h20m across 3
│                              sections: Start here (2), Claude (14), Hermes Agent (9). Archive
│                              and Certification sections deliberately NOT captured. Every lesson
│                              is its own folder with README.md (Jack's full description +
│                              timestamps + link table + attachment table), transcript.md,
│                              attachments/ and images/. 33 attachments, 25 images, 47 external
│                              links. KEPT AS REFERENCE so Ryan can copy the onboarding flow and
│                              Level 0-to-N ladder for The Leveraged Agent. Do not edit Jack's
│                              verbatim text, do not repurpose his copy as Leveraged Agent
│                              content, and build any derived Ryan content OUTSIDE this folder.
│                              Start at COURSE-MAP.md  → Jack Roberts AI Course/CLAUDE.md
├── Mentor-Mining/              mentor teardowns, one subfolder per mentor  → Mentor-Mining/CLAUDE.md
├── Nick-Nolf-TNG/              student / case-study material
├── hyperframes-student-kit/    student build kit (own git repo); also holds "Rose Homes Brandkit" (realtor brand)
└── Final Videos/               rendered videos (~32 GB, git-ignored → archive to SSD)
```

**Skill:** `/coach-teardown <handle>` researches a realtor coach or agent influencer end to end:
harvests every commenter and liker off their Instagram, reverse-engineers the funnel mechanic,
cuts ranked DM lists, and folds in their email newsletter if Ryan forwards one. Their coaching
clients are the same avatar as this Skool. Source in
[_System/skills/coach-teardown/](../_System/skills/coach-teardown/), symlinked live. Output goes
to `Instagram/Competitor-Research/<Coach-Name>/`. Reference implementation: `Peyson-Robertson/`.

**Skill:** `/skool-carousel` writes agent-audience Instagram carousels for this brand.
Source lives in [_System/skills/skool-carousel/](../_System/skills/skool-carousel/), symlinked live.
It reads `CLAUDE.md`, `Brandkit/CLAUDE.md`, `Mentor-Mining/ryan-built-inventory.md`,
`Mentor-Mining/content-queue.md`, and `VSL-Script-Main-Page.md` from this folder as grounding.
Do not use Rose Homes LV's `ig-carousel` here, different business.

**Brand assets:** the Leveraged Agent logos live in [Brandkit/](Brandkit/), copy from there into new projects. The canonical palette, contrast rules, clear-space and min-size rules are in [Brandkit/Brand-Guide/](Brandkit/Brand-Guide/); read `BRAND-GUIDE.md` before designing anything for this brand. **The brand is v2.0 "Vector", adopted 2026-08-19** when Ryan said "lets go vector": white `#FFFFFF` base, `#F7F8FA` sunken fill, TRUE-black `#000000` dark surface, navy ink `#050E3D`, one accent `#1768E5` that works both as a fill and as text on white, and **Barlow 800** headlines at `-0.028em` / **Raleway 600** subtext only / **Inter 400-500** body. One accent, one value, no second darker variant, no warm colors, black is a surface and never text. **The v1.0 cream / teal / gold system is retired** and archived verbatim as `tokens-v1.css` / `tokens-v1.json`. **The regeneration happened on 2026-09-01:** the five PNGs at `Brandkit/` root and the classroom covers were rebuilt from the imported Claude Design system in `Brandkit/Design-System/`, and the v1 cover icon was archived. **Still on v1 and not refreshed:** the ~29 bundled copies under `hyperframes-student-kit/video-projects/*/assets/` (left deliberately, their compositions are still v1 teal) and the Instagram carousel system. `brand-guide.html` is stale too, it hardcodes v1 hexes. `YouTube-Thumbnails/template.html` is unaffected. The losing proposals survive as files and are all dead: v2 `Voltage` and `Ember`, v3 `Broker`, and the v4 finalists `Ultramarine` and `Meridian` plus also-rans `Signal` and `Ivory`. Three v4 candidates were rejected and **deleted** on 2026-08-19: `Rosewood` (failed the accent-as-text test), `Crimson` (too loud), `Sovereign` (purple, Mike Sherrard already owns it in this niche). **Ryan also rejected Space Grotesk, Fraunces and Bodoni Moda**, which removed every serif from the system, so hierarchy is bought with weight and size alone. The 800-to-400 gap is the whole hierarchy. Do not re-propose anything on those rejection lists, and do not re-propose the 800-on-page / 900-in-thumbnail weight split, which was offered and declined. The full record with every hex is in `V4-PALETTES.md`. `PEDIGREE-BRAND-RESEARCH.md` + `pedigree-board.html` are the measured brand-convention research on 10 high-pedigree US brokerages (Serhant, Agency, Compass, Elliman, Eklund Gomes, Altman, Sotheby's, Corcoran, Real, Tom Ferry); read it before proposing any palette change. Note `hyperframes-student-kit/Rose Homes Brandkit/` is the *realtor* brand and belongs to a different business; never mix the two.

**Maintenance rule:** When you add, remove, move, or rename anything here, update this map. Keep this Skool brand separate from Rose Homes LV and AI Clients. Never leave the map stale.

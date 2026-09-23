# The Nick Saraev Formula

**What this is:** the repeatable structure extracted from 38 structured deep-reads of Nick Saraev's YouTube videos, cross-checked against view and velocity data for his full 303-video catalog.

**Sources:** `01-deep-reads/` (38 files, identical 9-section schema) and `00-corpus.csv` (303 videos, snapshot as of 2026-08-03).

**How to use it:** every heading is a question. Jump to the one you have. Every number here is computed from `00-corpus.csv` or quoted from a deep-read. Video ids are in brackets like `[TxMAUMUn-is]` so you can audit any claim back to its file.

**Rule applied throughout:** a pattern needs several instances. Anything with n=1 or n=2 is labeled an anecdote and should not be treated as a lever.

---

## READ THIS FIRST: the one number that distorts every other number

Views per day is not age-neutral. YouTube front-loads views, so a video measured 5 days after publish reports a far higher views/day than the same video measured 500 days later.

| Publish year | videos in corpus | median views/day |
|---|---|---|
| 2021 | 5 | 2.8 |
| 2022 | 1 | 1.5 |
| 2024 | 115 | 19.1 |
| 2025 | 134 | 69.7 |
| 2026 | 48 | **997.6** |

Spearman correlation of `age_days` against `views_per_day` across all 303 videos: **-0.737**. That is the strongest relationship in the entire dataset, stronger than any hook, title, or format effect.

**Consequence:** a raw ranking of "which hook wins" mostly ranks "which hook he used most recently." Every ranked table below therefore carries the group's median age and, where the sample allows, a 2026-only median so you can compare like with like. Do not quote a cross-group median without the age column next to it.

Within the 38 deep-read batch the same skew holds: 2024 videos median 68.9 views/day (n=2), 2025 median 183.7 (n=20), 2026 median 1,998.2 (n=16).

---

## 1. What is the structural spine? (the formula in one table)

| Slot | What happens | How many of the 38 | Who deviates |
|---|---|---|---|
| **0:00 to 0:20** | The hook is the literal first sentence. No channel intro, no "before we begin," no sponsor, no logo sting. | **37 / 38** | `[XE6VcwCBSqA]` opens on a cross-channel plug. The deep-read's own verdict: "Mechanism: None. This is housekeeping, a cross-channel promo, not a hook." |
| **0:00 to 0:20** | A specific number appears in the spoken hook (revenue, student count, price, percentage, timeframe, or item count). Counted only against the text quoted in each deep-read's Hook block. | **22 / 38** | The 16 without a number are almost all demo-first or contrarian opens where the picture or the negation carries the tension instead. |
| **0:00 to 0:20** | The finished artifact is already on screen while he talks. | **9 / 38** | This is the demo-first group. See §2. |
| **~0:34** | A second structural beat lands: a roadmap, a curriculum read-out, a proof drop, or an objection pre-empt. Median timestamp of the beat immediately after the hook across all 38: **34 seconds**. | **38 / 38** | 34 of 38 land inside a 16-second window (0:26 to 0:42). The four outliers are 0:14 `[7Su6W_FlUbk]`, 1:03 `[sduaTkhIm_w]`, 1:07 `[MxyRjL7NG18]`, 1:15 `[k1DTxuBur-Y]`. |
| **0:20 to 2:00** | He opens loops he will not close for 20+ minutes. Longest examples: 15 loops in one read-out `[QoQBzR1NIqI]` at 0:33, 15-item curriculum `[MxyRjL7NG18]` at 0:00, 8 techniques `[EsTrWCV0Ph4]` at 0:34, 5 pillars `[bMmlCPLDk1c]` at 0:30, 3 reasons previewed `[TxMAUMUn-is]` at 0:32. | present in every long-form video | Short commentary videos (7 to 10 min) skip it: `[ikxxjRWX0Yg]`, `[esXXuejofgk]`. |
| **Middle** | A live screen-share build or a node-by-node walk of an on-screen artifact. | **28 / 38** | 10 are commentary or interview only: `[36xOZ1e6tuM] [g_Q15Ibn3Iw] [YIl-awY250k] [esXXuejofgk] [ikxxjRWX0Yg] [k1DTxuBur-Y] [TxMAUMUn-is] [DbZotE0Ch0g] [bMmlCPLDk1c]`, plus `[4ryBQ9P_p64]` which walks a mind map with no build. |
| **Middle** | At least one failure, dead end, weak result, or honest limit is kept on camera and named as such in the beat table. | **at least 24 / 38** | Clean examples: "wrong endpoint dead end" `[9zBtU1mwOR4]` 12:53; "visible failure" `[gsPGdq2C97c]` 62:02 where the webhook never works and he narrates giving up; "kill a loser" `[eLqveVYFWc4]` 9:06 where his own real estate campaign returns 0 positives; "This is going to work like 20% of the time" `[7Su6W_FlUbk]` 8:39. |
| **End** | The paid ask sits in the final ~2% of runtime. No pre-roll pitch, no mid-roll interruption for the paid offer, in any of the 38. | **36 / 38 have an ask at all** | `[QoQBzR1NIqI]` puts its only pitch at 249:58 of 250.7 min and labels it: "That's my last and only pitch of this video." `[MxyRjL7NG18]` at 340:50 of 341.7 min. |
| **End** | CTA hardness distribution: soft mention only **23**, hard close **8**, mid-roll-strength stacked close **5**, no CTA at all **2**. | 38 / 38 | Zero CTA: `[esXXuejofgk]` (1,037.0 views/day) and `[ikxxjRWX0Yg]` (1,901.2 views/day). Both outperform most of the hard-close videos. |
| **End** | A money-back guarantee is attached to the paid offer ("first customer in 90 days or your money back"). | **13 / 38** | Every instance is the same offer, Maker School. |

**The one-line version:** first sentence is the hook, second beat at 0:34, loops opened before minute two, a live build with the failures left in, and a single soft ask in the last 30 seconds.

---

## 2. Which hook mechanism should I use? (ranked)

This is the section that matters most. Read the age column before you read the median.

### 2a. All 38, ranked by median views/day

| Rank | Mechanism | n | Median views/day | Median age (days) | Range | Verbatim example |
|---|---|---|---|---|---|---|
| 1 | **Threat** | 4 | **1,706.2** | 68.5 | 1,315 to 2,095 | "agentic workflows have the potential to bring about what I think is one of the largest wealth transfers in human history. But very few people are currently talking about how to practically use them" `[MxyRjL7NG18]` |
| 2 | **Contrarian** | 5 | **1,037.0** | 334 | 98 to 6,026 | "up until now, virtually every instance of knowledge bases or second brains or whatever have just been total hot air" `[eCx3SSCcISo]` |
| 3 | **Demo-first** | 9 | **873.5** | 28 | 118 to 9,789 | "So, KimmyK3 can design absolutely gorgeous, beautiful websites just like these for literally just a dollar or two" `[0zlwXSVmoeg]` |
| 4 | **Loss-frame** (anecdote, n=2) | 2 | 680.0 | 301 | 210 to 1,150 | "about 70% of the time I run a skill, I get an intended output, but 30% of the time it's a bag of rocks" `[qKU-e0x2EmE]` |
| 5 | **Proof-first** | 10 | **457.8** | 219 | 34 to 12,924 | "I use Cloud Code every day to manage a business that does over $4 million a year in profit. I also teach over 2,000 people" `[QoQBzR1NIqI]` |
| 6 | **Number-first** | 7 | **163.1** | 484 | 104 to 587 | "Here are five boring AI automations that you could sell today for 1,500 bucks a pop or more" `[jBF48jNWPJE]` |
| 7 | **No hook** (anecdote, n=1) | 1 | 69.8 | 389 | n/a | "Hey everybody, my daily updates channel is where I post more casual day-to-day content" `[XE6VcwCBSqA]` |

### 2b. The same table, 2026 videos only (age-controlled)

2026 cohort baseline across the full corpus: **997.6** views/day.

| Mechanism | n (2026) | Median views/day | vs 2026 baseline | Videos |
|---|---|---|---|---|
| **Demo-first** | 5 | **3,751.0** | 3.8x | `[0zlwXSVmoeg] [k1DTxuBur-Y] [KDkR0cJRiJk] [h6G9R4UxR6g] [7Su6W_FlUbk]` |
| **Contrarian** | 2 | 3,531.4 *(anecdote)* | 3.5x | `[eCx3SSCcISo] [esXXuejofgk]` |
| **Threat** | 3 | 1,901.2 *(thin)* | 1.9x | `[8rVQuZlRaqo] [ikxxjRWX0Yg] [Ob5Vu-gD3mo]` |
| **Proof-first** | 5 | 1,456.2 | 1.5x | `[QoQBzR1NIqI] [EsTrWCV0Ph4] [rbUFFMtKcaQ] [sduaTkhIm_w] [DbZotE0Ch0g]` |
| **Loss-frame** | 1 | 1,150.3 *(anecdote)* | 1.2x | `[qKU-e0x2EmE]` |
| **Number-first** | **0** | n/a | n/a | he published none in 2026 |

**The headline finding of this whole document:** the number-first hook, the format that built his channel in 2024 and 2025, appears **zero times** in his 2026 output. Once you age-control, demo-first is the mechanism he actually moved to, and it beats the 2026 baseline by 3.8x.

### 2c. When each mechanism applies

**Demo-first.** Open with the finished artifact on screen while you narrate. Use it when you have something visually falsifiable in under 10 seconds. It fails when the output is invisible (a spreadsheet, a policy, a mindset). Median age of this group is 28 days, so treat the raw median as inflated, but the 2026-controlled 3,751.0 is real.
- Sub-variant that works: **demo-first plus price anchor** `[0zlwXSVmoeg] [KDkR0cJRiJk]`. Show something expensive-looking and quote a tiny cost in the same breath.
- Sub-variant: **demo-first plus scarcity peg** `[h6G9R4UxR6g]` ("given that we all have an additional 5 days of Claude Fable 5").
- Sub-variant: **demo-first plus live open loop** `[wLNw-rpklfE]`, where he commits to an outcome he does not yet have.

**Contrarian.** State the consensus, negate it flatly, then immediately buy the right to the negation. `[esXXuejofgk]` spends several sentences proving he actually used the tool before delivering the verdict. `[eCx3SSCcISo]` signals reluctance ("that's hard for me to say"). `[YIl-awY250k]` pays the toll with a revenue figure before betraying the category. The pattern only works if you concede something first. The two lowest contrarian performers `[36xOZ1e6tuM]` (98.1) and `[TxMAUMUn-is]` (198.9) are both 2025, so the spread here is age, not mechanism quality.

**Threat.** Frame the viewer's current tool, skill, or workflow as already obsolete or actively harmful. Half the work is done in the title, not the audio: `[ikxxjRWX0Yg]` opens with a flat news read and lets the title ("Do not talk to Claude's new voice mode") carry all the tension. `[Ob5Vu-gD3mo]` recruits n8n users to defend their own tool. Best for news-pegged coverage of a product your audience already pays for. Median age 68.5 days, so this is also recency-flattered.

**Proof-first.** Lead with a receipt: revenue, student count, years, or a proxy's number. Widest range in the dataset (34.3 to 12,924). It does not lift a video on its own. Both his single best video `[QoQBzR1NIqI]` and his single worst `[4ryBQ9P_p64]` open proof-first. What separates them is topic recency, not hook craft.
- **Proof-first through a proxy** `[DbZotE0Ch0g]`: the student makes the claim, not you. The deep-read's read on why it works: "Nick does not make the claim, the student does, which makes it feel like evidence rather than marketing."

**Loss-frame.** Name a bill or a failure rate the viewer is already paying and has never quantified. Two instances only, so this is an anecdote, not a pattern. But `[qKU-e0x2EmE]`'s "30% of the time it's a bag of rocks" is the cleanest single line in the batch, because the viewer has felt the number and never counted it.

**Number-first.** Open with a count, price, or ratio as the promise. Median 163.1, the worst of any real mechanism, median age 484 days, and abandoned entirely in 2026. Do not build a channel on this.

**No hook.** One instance `[XE6VcwCBSqA]`, 69.8 views/day, third-lowest of the 38. Not enough data to prove causation, but it is the only video in the batch where the deep-read could not name a mechanism at all.

---

## 3. Which title formula should I use? (ranked by median views/day)

### 3a. Formula families across the full 303-video corpus

Ranked by median views/day. **The age column is load-bearing.** Families concentrated in 2026 sit at the top partly because 2026 videos are young.

| Rank | Formula, slots marked | n | Median views/day | Median age | 2026 subset | Live example |
|---|---|---|---|---|---|---|
| 1 | `<TOOL> FULL COURSE <N> HOURS: <Verb> & <Verb> (<YEAR>)` | 9 | **2,292.8** | 154d | 7 of 9 | "CLAUDE CODE FULL COURSE 4 HOURS: Build & Sell (2026)" `[QoQBzR1NIqI]` 12,923.6 |
| 2 | `<New product> ... Kills / Destroys / Killed <incumbent the audience pays for>` | 5 | **1,511.1** | 136d | 5 of 5 | "Cerebras Killed Notion, Obsidian, and Your \"Second Brain\"" `[eCx3SSCcISo]` 6,025.8 |
| 3 | `I Spent $<N> <verb>-ing <brand new thing>` / `I Gave <model> Unlimited <resource>` | 4 | **1,302.8** | 26d | 4 of 4 | "I Spent $400 Benching Opus-5. Here's What It Can Do" `[k1DTxuBur-Y]` 6,214.1 |
| 4 | Any named frontier model or product in the title | 40 | **1,093.2** | 130d | 36 of 40 | see 3b |
| 5 | `<New product> Just Dropped, And <verdict>` | 6 | **906.0** | 124d | 6 of 6 | "Claude Managed Agents Just Dropped, And It Kills n8n" `[Ob5Vu-gD3mo]` 1,511.1 |
| 6 | `<Hyped thing> Sucks, Actually` *(anecdote, n=2)* | 2 | 892.6 | 158d | 2 of 2 | "Clawdbot Sucks, Actually" `[esXXuejofgk]` 1,037.0 |
| 7 | Year stamp `(<YEAR>)` anywhere in the title | 34 | 120.1 | 472d | 9 of 34 | 2026 subset median 2,087.8 |
| 8 | `$<figure>` anywhere in the title | 80 | 58.3 | 474d | 8 of 80 | see 3c, this reverses by year |
| 9 | `$<N>/month` income figure in the title | 28 | **52.5** | 448d | 1 of 28 | "Steal This Cold Outreach Strategy & Make $9K/Month Selling AI" `[XE6VcwCBSqA]` 69.8 |
| 10 | `The <platform> <transgressive label> System (<result> in <timeframe>)` | 5 | 49.6 | 591d | 0 | "The N8N Instagram Parasite System (10K Followers In 15 Days)" `[9zBtU1mwOR4]` 159.3 |
| 11 | `How I / How to <do the thing>` | 66 | 42.7 | 710d | 5 of 66 | "How I'd Automate a Plumbing Company in 15 Steps" `[4ryBQ9P_p64]` 34.3 |
| 12 | `<N> <adjective> <things> To Sell For $<price> Each in <year>` (listicle count) | 20 | **30.6** | 545d | **0** | "5 \"BORING\" AI Automations To Sell For $1.5K+ Each in 2025" `[jBF48jNWPJE]` 587.4 |
| 13 | `(FREE TEMPLATE)` in the title | 5 | 69.6 | 478d | **0** | "I Built An AI Asset-Based Lead Gen System (Free Template)" `[yYVfcfa7n5A]` 69.6 |
| 14 | `Watch me <do the hard thing> in <N hours>` | 23 | **16.8** | 798d | **0** | "Watch me start & sell an AI service in 10 hours" `[wLNw-rpklfE]` 786.3 |

### 3b. The one title lever that survives age-control

Within the 2026 cohort only (n=48, baseline median 997.6):

| | n | Median views/day |
|---|---|---|
| Title names a specific model, product, or company (Claude, Opus, Fable, Gemini, GPT, Kimi, Sonnet, GLM, Cerebras, Antigravity, Nano Banana, Kling, Clawdbot, Paperclip) | 36 | **1,165.2** |
| Title names none | 12 | **476.4** |

**2.4x, inside a single publication year.** This is the most defensible title finding in the dataset. The proper noun is doing the work, not the promise. The 12 no-proper-noun 2026 videos include his four worst 2026 performers, all of which are abstract essays ("Advice for working in a post-AGI world" 106.6, "how to stay economically valuable from 2026-2029" 122.4, "It's Official: AI Makes You Worse At Stuff" 52.6).

### 3c. The dollar figure reversed polarity between 2024 and 2026

| Year | $ in title, n | median | No $ in title, n | median |
|---|---|---|---|---|
| 2024 | 29 | 18.8 | 86 | 19.2 |
| 2025 | 43 | 61.9 | 91 | **71.4** |
| 2026 | 8 | **2,675.7** | 40 | 929.5 |

In 2025 a dollar figure in the title made a video slightly *worse* than its cohort. In 2026 it made a video 2.9x better. The difference is the kind of figure. In 2024 and 2025 the dollar was an **income claim** ("$9K/Month", "$13k/m Agency", "$200,000/Yr"). In 2026 it is a **cost or price-gap claim** ("For Just $1", "I Spent $400", "$1 Website ... Looks Like $10K").

Income figures specifically, isolated by year: 2025 income-in-title n=18 median 56.6 against a 2025 no-income median of 75.5. He then stopped: **1 of 48 in 2026** `[DbZotE0Ch0g]`.

### 3d. Title formulas that put an unsupported number in the title

Four of the 38 carry a dollar figure in the title that the transcript never states, defends, or derives. A fifth carries an unsupported non-dollar claim.

| Video | Title figure | What the deep-read found |
|---|---|---|
| `[XE6VcwCBSqA]` | `$9K/Month` | "the title's $9K/month is never stated anywhere in the transcript, and no dollar figure is attached to the Loom strategy itself" |
| `[k1DTxuBur-Y]` | `$400` | "the title's $400 is never mentioned in the transcript ... the number has to be in the title, not in the script" |
| `[h6G9R4UxR6g]` | `$10K Websites` | "The \"$10K\" in the title is never said anywhere in the transcript ... it exists purely to price the free thing" |
| `[KDkR0cJRiJk]` | `Looks Like $10K` | "The \"$10K\" comparison in the title is never stated or defended anywhere in the transcript ... neither has to be justified in the video" |
| `[36xOZ1e6tuM]` | `Using Just ONE AI Automation` | "the video does not deliver on the \"ONE AI automation\" claim at all, the guest states plainly that she does not sell content automations" |

A sixth is a hedged percentage doing quiet legal work: `[OroDNJl-pyc]` titles itself "(99% FREE)". The deep-read: "The \"99%\" is doing quiet legal work, it admits an exception without naming one."

This is deliberate technique on his part, not sloppiness. It is also the single most dangerous thing in this document for a licensed agent to copy. See §7.

### 3e. Abstracted slot patterns from all 38 (for adaptation)

Sorted by the video's views/day, highest first. Slots in `<angle brackets>`.

| Views/day | Pattern | Source |
|---|---|---|
| 12,923.6 | `<TOOL> FULL COURSE <N> HOURS: Build & Sell (<YEAR>)` | `[QoQBzR1NIqI]` |
| 9,789.2 | `<New model> does <premium creative outcome> for just $<tiny number>` | `[0zlwXSVmoeg]` |
| 6,214.1 | `I Spent $<N> <verb>-ing <brand new thing>. Here's What It Can Do` | `[k1DTxuBur-Y]` |
| 6,025.8 | `<Credible company> Killed <tool 1>, <tool 2>, and Your "<identity noun>"` | `[eCx3SSCcISo]` |
| 3,802.9 | `<Topic> Full Course <Year>: Master <Topic> (<N> Hours)` | `[EsTrWCV0Ph4]` |
| 3,751.0 | `The Viral $<tiny number> <thing> That Looks Like $<huge number> (Tutorial)` | `[KDkR0cJRiJk]` |
| 3,025.0 | `<Hot model> Is Back. Use It To Print With These $<big number> <asset>` | `[h6G9R4UxR6g]` |
| 2,095.2 | `A Practical <thing> For <audience> In <future year> (Guide)` | `[8rVQuZlRaqo]` |
| 1,901.2 | `Do not <do the obvious thing with> <newly released product>` | `[ikxxjRWX0Yg]` |
| 1,511.1 | `<New product> Just Dropped, And It <Kills> <incumbent>` | `[Ob5Vu-gD3mo]` |
| 1,492.2 | `What I'd Learn Instead of <the thing my audience subscribed for> in <year>` | `[YIl-awY250k]` |
| 1,456.2 | `I Gave <model> Unlimited <resource> to <do thing> (+ Results)` | `[rbUFFMtKcaQ]` |
| 1,315.1 | `<ALL-CAPS CATEGORY>: Build & Sell <thing> (<YEAR>)` | `[MxyRjL7NG18]` |
| 1,150.3 | `Stop <the manual chore>. <New named technique> Does It For You` | `[qKU-e0x2EmE]` |
| 1,037.0 | `<Hyped Thing> Sucks, Actually` | `[esXXuejofgk]` |
| 941.2 | `<TOOL> FULL COURSE: <Outcome Verb> Your <Thing> (<year>)` | `[sduaTkhIm_w]` |
| 873.5 | `The BEST <thing> No One Is Using` | `[7Su6W_FlUbk]` |
| 786.3 | `Watch me <do the hard thing> in <N hours>` | `[wLNw-rpklfE]` |
| 718.7 | `$<exact odd figure>/m, <constraint>, while <second constraint>` | `[DbZotE0Ch0g]` |
| 587.4 | `<N> "<CONTRARIAN ADJECTIVE>" <category> To Sell For $<price>+ Each in <year>` | `[jBF48jNWPJE]` |
| 247.4 | `I <verb>ed <big round number>+ <artifact> Using THIS AI System (FREE TEMPLATE)` | `[oAWe5wFwHlo]` |
| 209.8 | `<Do the expensive thing> WITHOUT Paying for <the thing everyone pays for> (<n>% FREE)` | `[OroDNJl-pyc]` |
| 198.9 | `Why I Don't <do the recommended thing> (Despite What <named group> Claim)` | `[TxMAUMUn-is]` |
| 196.8 | `How to get SO many <resource> you don't know what to do with them` | `[2XHgJXX49Jk]` |
| 190.4 | `How I Would <start the thing> in <year> (If I could start over)` | `[bMmlCPLDk1c]` |
| 190.0 | `<N>% of <domain> in Just <N> Minutes` | `[4PZYb86j4wg]` |
| 177.3 | `Build This <adjective> <platform> System in 1 Hour (<Tool>)` | `[gsPGdq2C97c]` |
| 163.1 | `<N> industries desperately paying for <thing> (<year>)` | `[g_Q15Ibn3Iw]` |
| 159.3 | `The <tool> <transgressive label> System (<result> In <timeframe>)` | `[9zBtU1mwOR4]` |
| 131.5 | `It's <negative adjective>, But <outcome> SO Easy` | `[eLqveVYFWc4]` |
| 123.3 | `How to Acquire Your First <outcome> For $<absurdly precise low number>` | `[bao3ogOcpiw]` |
| 117.8 | `building a <business thing> the LAZY way (<Mechanism>)` | `[Uj-1we7Rew4]` |
| 117.8 | `The <N> Best <category> niches in <year>` | `[OLwEtOEF36A]` |
| 103.6 | `How I <get a scarce asset> in <short time>` | `[eElnA0mCzXw]` |
| 98.1 | `How She Built a $<N>k/m <business> Using Just ONE <thing>` | `[36xOZ1e6tuM]` |
| 69.8 | `Steal This <asset> & Make $<N>/Month Selling <category>` | `[XE6VcwCBSqA]` |
| 69.6 | `I Built An AI <category> System (Free Template)` | `[yYVfcfa7n5A]` |
| 34.3 | `How I'd Automate a <unglamorous local business> in <N> Steps` | `[4ryBQ9P_p64]` |

---

## 4. What does he argue over and over? (the recurring theses)

Nine arguments recur across five years and multiple tiers. Each is listed with the videos it appears in and a verbatim quote.

### 4.1 Lead data is never the bottleneck
Appears in `[2XHgJXX49Jk] [eElnA0mCzXw] [oAWe5wFwHlo] [OroDNJl-pyc] [bao3ogOcpiw]`.
> "To me, the leads are never the bottleneck here, just because we have platforms like Apollo and Appify and stuff that let us get an almost infinite number of them." `[oAWe5wFwHlo]`

The corollary he states repeatedly: "the marginal cost of sending a cold email nowadays tends to zero if you guys have all the infrastructure set up." `[2XHgJXX49Jk]`

### 4.2 Sell the outcome, never the mechanism
Appears in `[36xOZ1e6tuM] [XE6VcwCBSqA] [sduaTkhIm_w] [bMmlCPLDk1c] [jBF48jNWPJE]`.
> "fulfillment is not about delivering the system" `[bMmlCPLDk1c]` beat at 22:51

> "you sell white glove service, not templates" `[XE6VcwCBSqA]` beat at 12:59

The `[36xOZ1e6tuM]` version is the strongest statement of it: agencies "narrow into selling one revenue outcome to one ICP, and the automation becomes an internal cost lever rather than the thing being sold."

### 4.3 Sell before you build
Appears in `[eLqveVYFWc4] [wLNw-rpklfE]`, and is the spine of both.
> "you are selling the idea of a thing" `[eLqveVYFWc4]` beat at 2:31

> "you guys can do literally all of this in a week. And if you do that, it'll cost somewhere between $200 to $300 ... Now, compare that to spending 3 months building a piece of crap that nobody wants." `[eLqveVYFWc4]`

### 4.4 If you have an SOP, you already have a skill
Appears in `[sduaTkhIm_w] [Uj-1we7Rew4] [MxyRjL7NG18] [QoQBzR1NIqI]`.
> "if you guys have a standard operating procedure, if you have an SOP, you have a skill" `[sduaTkhIm_w]` at 19:22

> "skills are basically the evolution of standard operating procedures just for agents" `[sduaTkhIm_w]` at 15:19

The DO framework in `[Uj-1we7Rew4]` and `[MxyRjL7NG18]` is the same argument formalized: **D**irectives are plain-language markdown SOPs, **O**rchestration is the agent routing, **E**xecution is code the agent writes itself.

### 4.5 Push deterministic work out of the model and into code
Appears in `[MxyRjL7NG18] [EsTrWCV0Ph4] [qKU-e0x2EmE] [8rVQuZlRaqo] [QoQBzR1NIqI]`.
> Native LLM sort roughly 30 seconds versus a Python script at 53 milliseconds `[MxyRjL7NG18]` at 66:58

> "imagine if you were a business that made $100,000 a month and you sent a wrong invoice 5% of the time ... that would have like a 95% impact on your business." `[MxyRjL7NG18]` at 61:17

Compound error math is the numeric spine of the argument: 90% accuracy five steps deep is 59%.

### 4.6 Every service business is the same shape, only fulfillment differs
Appears in `[YIl-awY250k] [4PZYb86j4wg] [bMmlCPLDk1c] [TxMAUMUn-is]`.
> the shape: "marketing leads to sales leads to onboarding leads to delivery leads to reactivation and retention," claimed universal across every product and service type `[YIl-awY250k]`

> "only fulfillment is different, everything else is shared with every business" `[4PZYb86j4wg]` beat at 2:32

### 4.7 The technical skill is the commodity, the business skill is the moat
Appears in `[YIl-awY250k] [4PZYb86j4wg] [sduaTkhIm_w] [XE6VcwCBSqA] [DbZotE0Ch0g]`.
> "You need to stop learning how to drag and drop modules and start learning how to identify problems worth more than $50,000 or so to solve." `[YIl-awY250k]`

> "most demos build backend fulfillment pipelines, most people that do these sorts of things still don't make any money ... build front-end skills, sales and marketing, and actually use them" `[sduaTkhIm_w]` beats at 43:19 and 44:36

> "most people don't need agents, man" `[DbZotE0Ch0g]` at 3:57

### 4.8 Give the value before you make the ask
Appears in `[bao3ogOcpiw] [yYVfcfa7n5A] [OLwEtOEF36A] [XE6VcwCBSqA] [jBF48jNWPJE]`.
> "This is how high quality people are doing cold outreach today. Because the bar has gone up so much, you got to deliver value. You got to do it up front. And usually, you got to do it without some sort of super crazy hard ask." `[yYVfcfa7n5A]`

> the CTA design: replace "book a call" with "respond with a thumbs up" `[XE6VcwCBSqA]` at 4:06

### 4.9 Ideation is the machine's job, taste is yours
Appears in `[rbUFFMtKcaQ] [0zlwXSVmoeg] [7Su6W_FlUbk] [EsTrWCV0Ph4] [8rVQuZlRaqo]`.
> "AI ideates over a large space, humans apply taste to pick" `[0zlwXSVmoeg]` beat at 4:40

> "stop writing the prompt, make the model build its own infrastructure" `[rbUFFMtKcaQ]` beat at 3:05

The operational form is generate-many-then-select: five variants because the effect lands one time in five `[7Su6W_FlUbk]`, stochastic multi-agent consensus `[EsTrWCV0Ph4]`, three parallel generations to trade credits for wall-clock time `[0zlwXSVmoeg]`.

### 4.10 A human QA gate is non-negotiable
Appears in `[8rVQuZlRaqo] [Uj-1we7Rew4] [sduaTkhIm_w] [jBF48jNWPJE] [EsTrWCV0Ph4]`.
> "You can't just trust an AI agent to do everything entirely on its own" `[8rVQuZlRaqo]` at 5:21

> he refuses the bulk action and asks to review all 97 emails first `[sduaTkhIm_w]` at 27:35

> the "honest residue," the manual QA he still does, kept in as "credibility through incompleteness" `[Uj-1we7Rew4]` at 24:59

Note the through-line from 4.10 back to 4.5: the eval checklist in `[8rVQuZlRaqo]` and the autoresearch optimization loop in `[qKU-e0x2EmE]` are the same idea applied twice, and they are the two most directly transferable things in the whole batch.

---

## 5. What does NOT move views? (anti-cargo-cult)

Rigorous section. Each item appears in both his best and his worst performers, or fails a cohort-controlled test.

### 5.1 Runtime, below about two hours
Spearman correlation of `dur_min` against `views_per_day` across all 303 videos: **-0.065**. Effectively zero. Within the 38-video batch it is **-0.306**, mildly negative.

2026 cohort by runtime bucket:

| Bucket | n | Median views/day |
|---|---|---|
| under 10 min | 9 | 941.9 |
| 10 to 20 min | 20 | 906.0 |
| 20 to 40 min | 10 | 1,318.2 |
| 40 to 120 min | 3 | 783.1 |
| **120 min+** | 6 | **2,563.2** |

Everything under two hours is noise. The 120-minute bucket is real (2.6x cohort, and the 2025 cohort shows the same shape at 284.9 against a 69.7 baseline), but **5 of those 6 videos are titled "FULL COURSE."** The lever is the completeness-signal title formula, not the minutes. A 90-minute video with a normal title gets nothing for its length: `[gsPGdq2C97c]` runs 72.4 min at 177.3, `[9zBtU1mwOR4]` runs 79.8 min at 159.3.

**Do not** conclude "make longer videos." Conclude "if you are going to make a 2-hour video, title it as a course."

### 5.2 Engagement rate
Spearman correlation of `eng_rate` against `views_per_day`: **-0.064** overall, and **negative inside every single cohort**: 2024 **-0.375**, 2025 **-0.266**, 2026 **-0.426**.

Within the 38: top-10 by views/day have a median engagement rate of 3.33, bottom-10 have 3.27. His single best video `[QoQBzR1NIqI]` has an engagement rate of 2.89, below the batch median. His 8.5-minute rant `[esXXuejofgk]` has 4.42 and 15th place.

Engagement rate measures how hard a video works its existing audience. It does not measure reach. Optimizing for it is optimizing for the wrong thing.

### 5.3 Live builds with the failures left in
This is his most distinctive craft move and it does not sort videos at all.
- Present in his best: `[QoQBzR1NIqI]` 12,923.6, `[EsTrWCV0Ph4]` 3,802.9 (uses his own real TikTok failure as the demo problem at 55:46).
- Present in his worst: `[gsPGdq2C97c]` 177.3 (webhook fails on camera at 62:02, he narrates giving up), `[9zBtU1mwOR4]` 159.3 (wrong-endpoint dead end at 12:53), `[yYVfcfa7n5A]` 69.6 (debugs live twice).

It buys trust, which matters for conversion. It does not buy reach. Keep it, but do not expect it to grow the channel.

### 5.4 The revenue credential in the hook
The `$72,000 a month` credential appears in six of the 38: `[OLwEtOEF36A] [jBF48jNWPJE] [oAWe5wFwHlo] [TxMAUMUn-is] [4PZYb86j4wg] [bao3ogOcpiw]`. All six are 2025. Their median is 194.4 against a 2025 cohort median of 69.7, so at the time it did outperform. He then stopped saying it.

More importantly, an income figure **in the title** underperformed its own cohort in 2025 (n=18, median 56.6, against a 75.5 no-income median), and he cut it to 1 of 48 videos in 2026. The credential is not what carries a video, and putting the money figure in the title is actively worse than not.

### 5.5 CTA hardness, in either direction
- **Zero CTA:** `[esXXuejofgk]` 1,037.0 and `[ikxxjRWX0Yg]` 1,901.2.
- **Hard close:** `[QoQBzR1NIqI]` 12,923.6 but also `[g_Q15Ibn3Iw]` 163.1 and `[bMmlCPLDk1c]` 190.4.
- **Soft mention:** ranges from `[k1DTxuBur-Y]` 6,214.1 down to `[4ryBQ9P_p64]` 34.3.

The CTA is a conversion decision, not a reach decision. Nothing in the data says the pitch costs him views. It also does not earn any.

### 5.6 Free assets and lead magnets in the title
"(FREE TEMPLATE)" family: 5 corpus videos, median 69.6, none published since 2025-05. Compare `[h6G9R4UxR6g]`, which gives away everything free and never says so in the title, at 3,025.0. The giveaway works as a retention device inside the video. In the title it does nothing.

### 5.7 The "Watch me..." real-time-proof format
23 corpus videos, median **16.8** views/day, the worst family measured. Its best instance `[wLNw-rpklfE]` at 786.3 is a genuine outlier (it is 91.7 minutes and doubles as a paid-curriculum demo). He has published zero since 2025-07. The format reads as high-effort and performs as low-reach.

### 5.8 Depth of the economic argument
This one is nearly inverted. His four highest-velocity 2026 videos contain almost no dollar math at all:
- `[0zlwXSVmoeg]` 9,789.2: "No total build cost, no client price, no revenue figure is stated."
- `[ikxxjRWX0Yg]` 1,901.2: "None. No figures stated."
- `[Ob5Vu-gD3mo]` 1,511.1: "He makes no ROI pitch and prices nothing."
- `[eCx3SSCcISo]` 6,025.8: "No dollar figures stated."

Meanwhile the videos densest with per-deal ROI math are among his lowest: `[OLwEtOEF36A]` 117.8, `[bao3ogOcpiw]` 123.3, `[g_Q15Ibn3Iw]` 163.1, `[4ryBQ9P_p64]` 34.3.

Detailed unit economics is a conversion tool for people already listening. It is not a reach tool, and there is no evidence in this dataset that it ever was.

### 5.9 The listicle
20 corpus videos, median 30.6 views/day, **zero published in 2026**. Last one: "3 \"Boring\" Agentic Workflows That Will Make You $5,000+", 2025-11-27, 100.7 views/day. Within the 2025 cohort, listicles ran 43.9 against a 69.7 baseline. He killed the format that built his early channel.

---

## 6. Where does he lose people, and what does he do badly?

### 6.1 The one video with no hook
`[XE6VcwCBSqA]` "Steal This Cold Outreach Strategy & Make $9K/Month Selling AI." It opens on a plug for a different channel. The deep-read: "Mechanism: None. This is housekeeping, a cross-channel promo, not a hook. The only tension in the first 20 seconds is imported from the title, and the actual hook line does not arrive until [0:31]." Result: 69.8 views/day, third-lowest of the 38.

### 6.2 Title and content mismatches
- `[36xOZ1e6tuM]` "How She Built a $13k/m Agency Using Just ONE AI Automation." No automation is built, demoed, or described. The guest states she does not sell content automations. 98.1 views/day.
- `[XE6VcwCBSqA]` promises "$9K/Month" and never prices the strategy anywhere in 19.8 minutes.
- `[jBF48jNWPJE]` is the counter-example that proves he can do it right: the title promises five automations at $1,500+ and all five are shown end to end on screen. 587.4 views/day, the best T1 video in the batch.

### 6.3 Figures in the title that the video never defends
Four dollar figures and one "ONE" claim, listed in full at §3d: `[XE6VcwCBSqA]` `[k1DTxuBur-Y]` `[h6G9R4UxR6g]` `[KDkR0cJRiJk]` `[36xOZ1e6tuM]`. Plus the hedged `(99% FREE)` in `[OroDNJl-pyc]`.

The deep-read for `[k1DTxuBur-Y]` states the technique plainly: "the $400 is never justified in the video, which is the point: the number has to be in the title, not in the script."

### 6.4 Arithmetic errors delivered on camera as fact
- `[OLwEtOEF36A]` at 12:12, live lifetime-value math on Sendbird's pricing page: "18 * 500 is $99,000 um customer lifetime value." 18 x 500 is 9,000. He then builds a pricing recommendation on top of it.
- `[OLwEtOEF36A]` again: "75,000 time 20% is 15,000 so as a recruitment agency you will make $115,000 just making that placement." The correct figure is 15,000.
- `[bao3ogOcpiw]`: claims he delivers recruitment agencies "somewhere between $5 to $110,000 a month," almost certainly a garbled "$5 to $10,000."
- `[eLqveVYFWc4]`: "If you guys get a 75% booking rate, that's great," where the surrounding math implies 0.75%. The same video quotes lead cost as both "$120 per thousand leads" and "one cent a lead," which differ by 12x.
- `[EsTrWCV0Ph4]` at 122:14: the 60-30-10 cost-routing worked example has its addends transposed against its own multiplications.

### 6.5 He tells you the numbers are made up, in three separate videos
- `[g_Q15Ibn3Iw]` at 8:24: "3 to 50k at a certain point. I'm pulling numbers out of my ass."
- `[wLNw-rpklfE]` at 13:40: "I'm just pulling some stuff out of my ass."
- `[EsTrWCV0Ph4]` at 20:22: hedges model differences with "pulling out numbers out of my butt."

This is a credibility move (it inoculates against pushback) and it works on camera. It is not available to a licensed professional, because the audience will read the admission and the figure separately, and only the figure travels.

### 6.6 His own revenue claims do not reconcile across videos
Same speaker, overlapping periods, different numbers, revenue and profit used interchangeably:

| Claim | Where | Date |
|---|---|---|
| "$72,000 a month" (agency) | `[OLwEtOEF36A] [jBF48jNWPJE] [oAWe5wFwHlo] [TxMAUMUn-is] [4PZYb86j4wg] [bao3ogOcpiw]` | Jan to May 2025 |
| "over 160 grand a month in combined profit" | `[eLqveVYFWc4]` | Oct 2025 |
| "$160,000 a month in combined revenue" | `[MxyRjL7NG18]` | Dec 2025 |
| "I made 400 grand last month" | `[YIl-awY250k]` | Sep 2025 |
| "over $4 million a year in profit" | `[QoQBzR1NIqI] [EsTrWCV0Ph4] [sduaTkhIm_w]` | Feb to Mar 2026 |
| "still make over 300 something thousand per month right now in profit" | `[QoQBzR1NIqI]` | Feb 2026 |
| "My business is going to do over $400,000 this month" | `[8rVQuZlRaqo]` | Jul 2026 |

`[eLqveVYFWc4]` calls $160k/month "profit," `[MxyRjL7NG18]` calls the same figure "revenue." $4M/year in profit is $333k/month, which sits between the $300k and $400k monthly figures, so it may be internally consistent, but nothing in any video reconciles it and no source is ever cited. A viewer who checks cannot verify a single figure.

### 6.7 He is inconsistent about pre-empting the objection
Videos where the deep-read flags an objection pre-empt inside the first two minutes tend to be his tighter work. Videos where the pre-empt does not arrive until minute five or later leak viewers in exactly the window where they decide: `[gsPGdq2C97c]` (first pre-empt at 5:02, 177.3 views/day), `[h6G9R4UxR6g]` (5:05, though this one still performs), `[8rVQuZlRaqo]` (5:21). This is directional, not proven, given the small n.

### 6.8 Errors in the deep-reads themselves, do not propagate these
Four deep-reads contain velocity claims that are false against `00-corpus.csv`:

| Deep-read | Claim | Actual |
|---|---|---|
| `[XE6VcwCBSqA]` | "this is the lowest views/day video in the batch" | 69.8, **third**-lowest. `[4ryBQ9P_p64]` is 34.3 and `[yYVfcfa7n5A]` is 69.6 |
| `[esXXuejofgk]` | "the highest views/day video in this batch by a wide margin" | 1,037.0, **15th of 38**, and 11th of the 12 T2 videos |
| `[0zlwXSVmoeg]` | "Highest views-per-day in this batch by an order of magnitude" | 9,789.2, **2nd of 38**, and 1.3x behind `[QoQBzR1NIqI]` at 12,923.6, not an order of magnitude |
| `[ikxxjRWX0Yg]` | "it outperforms his multi-hour builds on a per-minute basis" | true against `[MxyRjL7NG18]` (1,315.1), false against `[QoQBzR1NIqI]` (12,923.6) and `[EsTrWCV0Ph4]` (3,802.9) |

---

## 7. What can a licensed real estate agent safely copy?

Ryan holds an active license, is subject to his broker's advertising review, NAR's Code of Ethics, Nevada real estate advertising rules, and (for the Skool/coaching side) FTC rules on endorsements and earnings claims. The list below sorts Saraev's techniques by that exposure.

This is a risk map, not legal advice. Anything in the UNSAFE column should go to the broker's compliance review or to counsel before it ships.

### 7a. SAFE to copy as-is

| Technique | Source | Why it is clean |
|---|---|---|
| **Hook is the first sentence, no intro** | 37 of 38 | Pure structure. No claim attached. |
| **Demo-first open**: the finished artifact on screen while you talk | `[0zlwXSVmoeg] [KDkR0cJRiJk] [7Su6W_FlUbk] [k1DTxuBur-Y]` | Showing real work you actually did is the safest possible proof. Best-performing mechanism in the 2026 cohort at 3.8x baseline. |
| **Second beat at 0:34**: roadmap, curriculum read-out, or objection pre-empt | 38 of 38, median 34 seconds | Structure only. |
| **Loops opened before minute two, closed late** | `[QoQBzR1NIqI] [EsTrWCV0Ph4] [bMmlCPLDk1c] [TxMAUMUn-is]` | Structure only. |
| **Live build with the failures kept in** | at least 24 of 38 | Actively good for a licensed professional. It is the opposite of overclaiming. Does not grow reach (see §5.3), does grow trust. |
| **"I have no background in this" credibility inversion** | `[KDkR0cJRiJk]` at 0:31: "I did not go to programming school ... I learned how to do it watching free YouTube tutorials like you are now" | This is the exact posture for realtors who think AI is for engineers. It makes no claim about anyone's outcome. |
| **Single soft ask in the final 30 seconds** | 36 of 38 | Nothing in the data says a harder or earlier pitch earns views (§5.5), so take the version with the least pressure. |
| **Time-compression title**: `<N>% of <domain> in Just <N> Minutes` | `[4PZYb86j4wg]` | The only numbers are a scope ratio and a runtime, both of which you control and can honor. |
| **Prohibition title**: `Do not <do the obvious thing with> <new product>` | `[ikxxjRWX0Yg]` 1,901.2, 7 minutes, one take, zero production | Cheapest video in the batch to produce. Safe as long as the target is a tool or a practice, never a named brokerage, agent, or competitor (see 7b). |
| **Named-proper-noun title**: put the actual tool or product name in the title | 2026 cohort: 1,165.2 with a name, 476.4 without (2.4x) | Naming a *tool* is factual. This is the strongest title lever in the dataset and it costs you nothing. |
| **The eval-checklist gate** | `[8rVQuZlRaqo]` 12:24 to 15:26, `[qKU-e0x2EmE]` entire video | Not just safe. **Mandatory.** For a licensed agent this is the control that keeps a model from shipping a fair-housing violation or a fabricated price. Build the rubric with binary criteria: no fabricated figures, no protected-class language, every price and square footage traceable to MLS, brokerage identification present. |
| **Human QA gate before anything publishes** | `[8rVQuZlRaqo] [Uj-1we7Rew4] [sduaTkhIm_w] [jBF48jNWPJE]` | Same. Non-negotiable, and he already argues for it. |
| **"If you have an SOP, you have a skill"** | `[sduaTkhIm_w]` 19:22 | Pure method. The single best teaching frame in the batch for realtors. |
| **Personalized screen-share video sent as a give, not a pitch** | `[bao3ogOcpiw]` 32:19, `[XE6VcwCBSqA]` 1:27 to 4:06 | The craft transfers intact (open on their page so the animated thumbnail proves it is real; close with "reply with a thumbs up" instead of "book a call"). The *recipient list* is the regulated part, see 7b. |
| **Free asset in the description, no email gate** | `[sduaTkhIm_w]` 21:18: "you don't need to sign up or give me your email" | Costs nothing, no claim attached. Note it does not lift views (§5.6), it lifts goodwill. |

### 7b. UNSAFE, or safe only after a rebuild

Ranked by how much trouble it can cause.

| # | Technique | Where he does it | The specific exposure |
|---|---|---|---|
| 1 | **Undefended dollar figures in the title** | `[XE6VcwCBSqA]` "$9K/Month", `[k1DTxuBur-Y]` "$400", `[h6G9R4UxR6g]` "$10K Websites", `[KDkR0cJRiJk]` "Looks Like $10K" | He states the technique openly: "the number has to be in the title, not in the script." For a licensed agent, a dollar figure in an ad you cannot substantiate on demand is a misrepresentation problem under NAR Article 12 (truth in advertising) and state advertising rules. For the coaching business it is an unsubstantiated earnings claim under FTC rules. **Never put a number in a title you cannot document.** |
| 2 | **Income claims about what students earn** | `[DbZotE0Ch0g]` "$20,354/m, solo, while working a 9-to-5"; `[36xOZ1e6tuM]` "$13k/m Agency"; `[TxMAUMUn-is]` "Many of them make 10, 15, or $20,000 in their first 60 days in the program" | Testimonial-based earnings claims require substantiation and a typicality disclosure. "Many of them make $10-20k in 60 days" is exactly the claim shape that draws attention. If Ryan runs student case studies, they need written substantiation on file, a clear statement of what is typical, and a disclaimer. **Do not put the student's revenue figure in the title.** |
| 3 | **"First customer in 90 days or your money back"** | 13 of 38 videos | A results guarantee on a coaching product is an earnings-claim adjacent promise and creates a refund obligation you must honor exactly as written. If Ryan runs one, the terms need to be in writing, dated, and identical everywhere they appear. A results guarantee attached to *real estate services* (list-or-it-sells, guaranteed price) is separately regulated in most states and should not be copied at all. |
| 4 | **Scraping consumer contact data and cold-emailing or texting it** | The spine of `[eElnA0mCzXw] [OroDNJl-pyc] [bao3ogOcpiw] [oAWe5wFwHlo] [yYVfcfa7n5A] [2XHgJXX49Jk] [gsPGdq2C97c] [wLNw-rpklfE] [eLqveVYFWc4] [MxyRjL7NG18]` | Nine of the deep-reads flag this themselves. Homeowner contact data plus unsolicited email or SMS runs into CAN-SPAM, TCPA, federal and state Do Not Call, Nevada solicitation rules, and MLS/IDX data-use terms all at once. **The B2B version is the only survivable one**: lenders, title reps, property managers, builder reps, contractors, relocation contacts, agent-to-agent. Even that needs CAN-SPAM compliance and brokerage sign-off. |
| 5 | **AI-generated or AI-altered imagery of property** | `[0zlwXSVmoeg]` (generated cinematic hero video), `[rbUFFMtKcaQ]` (fabricated products and imagery), `[7Su6W_FlUbk]` (video-to-video alteration of real footage) | The `[7Su6W_FlUbk]` deep-read already draws the line correctly: "the effect belongs on the person and never on the house." Altering, generating, or enhancing imagery of a listed property is a misrepresentation issue and in some cases a Fair Housing issue (who is depicted in a neighborhood). **Effects on the agent: fine. Anything touching the property or the neighborhood: no.** |
| 6 | **"It Kills <named competitor>" / "<Product> Sucks, Actually"** | `[Ob5Vu-gD3mo] [eCx3SSCcISo] [esXXuejofgk]`, plus 5 more in the corpus | High-performing (median 1,511.1) and the highest-risk title family for a licensed agent. NAR Article 15 prohibits false or misleading statements about competitors and their business practices. Aiming this at a *software tool* is defensible. Aiming it at a brokerage, a portal, an iBuyer, or a named agent is not. **Restrict the target to non-real-estate software.** |
| 7 | **Automated LinkedIn connection requests and DMs** | `[gsPGdq2C97c]` (Phantom Buster auto-connect), plus the "Parasite System" family | Violates LinkedIn's terms of service and risks account loss. The deep-read flags it. Not a legal exposure so much as a business-continuity one, but it also touches unsolicited-solicitation rules if the recipients are consumers. |
| 8 | **Scraping and AI-rewriting other creators' content** | `[9zBtU1mwOR4]` "The N8N Instagram Parasite System" | Copyright exposure on the source material, and a real reputational cost in a small local market that does not exist in the AI-news niche. The deep-read says so directly: "There is also a reputational cost to visibly parroting other local agents." The corpus also says the format does not work: 5 videos, median 49.6 views/day, none since 2025-06. |
| 9 | **Saying the numbers are made up, on camera** | `[g_Q15Ibn3Iw] [wLNw-rpklfE] [EsTrWCV0Ph4]` | "I'm pulling numbers out of my ass" is a credibility move for an unlicensed creator. For a licensed agent the disclaimer does not travel with the clip. Only the number does. |
| 10 | **On-camera arithmetic you have not checked** | `[OLwEtOEF36A]` (two errors), `[bao3ogOcpiw]`, `[eLqveVYFWc4]` (12x contradiction on lead cost) | If you are teaching agents to price services or model returns, an error like "18 x 500 is $99,000" is not a rounding issue, it is the whole recommendation. Pre-compute every figure and put it on a slide. |
| 11 | **Reusing a stale revenue credential** | "$72,000 a month" across six videos in five months, alongside three other incompatible figures (§6.6) | A credential you repeat for a year should be dated and sourced. "I closed N transactions in 2025" beats any monthly income figure, because it is verifiable from public record and does not imply anyone else's outcome. |
| 12 | **Guest testimonial that sells the community** | `[36xOZ1e6tuM]` at 38:10, "last point before I make you sell my community" | The format is strong and the deep-read rates it FORMAT-ONLY-transferable. The exposure is FTC endorsement rules: a material connection (free access, discount, affiliate) must be disclosed clearly and conspicuously, and the endorsement must reflect honest opinions. **Disclose the connection on screen, not in the description.** |

### 7c. The rebuild rule

Across the 38 deep-reads the verdict distribution is: **DIRECT 5**, **ADAPTABLE 21**, **FORMAT-ONLY 12**. Almost nothing ports unchanged.

The single recurring reason is always the same. Saraev sells B2B to businesses that can be scraped, emailed, and quantified. Real estate sells to consumers who are protected by DNC, TCPA, CAN-SPAM, Fair Housing, and MLS data licensing, and the practitioner is licensed and supervised.

**Practical filter for every Saraev idea:** does the mechanism touch a consumer's contact information, a property's representation, or a dollar figure about someone's income? If yes, rebuild it. If no, copy it.

---

## Appendix A: the 38, auditable

Sorted by views/day. `vpd` = views_per_day from `00-corpus.csv`, `age` = age_days at snapshot.

| vpd | age | min | tier | id | hook mechanism | title |
|---|---|---|---|---|---|---|
| 12,923.6 | 172 | 250.7 | T3 | `QoQBzR1NIqI` | proof-first | CLAUDE CODE FULL COURSE 4 HOURS: Build & Sell (2026) |
| 9,789.2 | 12 | 21.6 | T2 | `0zlwXSVmoeg` | demo-first | Kimi K3 Designs Websites That Feel Like MOVIES For Just $1 |
| 6,214.1 | 10 | 15.9 | T2 | `k1DTxuBur-Y` | demo-first | I Spent $400 Benching Opus-5. Here's What It Can Do |
| 6,025.8 | 15 | 23.8 | T2 | `eCx3SSCcISo` | contrarian | Cerebras Killed Notion, Obsidian, and Your "Second Brain" |
| 3,802.9 | 148 | 133.2 | T3 | `EsTrWCV0Ph4` | proof-first | AI Agents Full Course 2026: Master Agentic AI (2 Hours) |
| 3,751.0 | 5 | 22.9 | T2 | `KDkR0cJRiJk` | demo-first | The Viral $1 Website Effect That Looks Like $10K (Tutorial) |
| 3,025.0 | 27 | 10.6 | T2 | `h6G9R4UxR6g` | demo-first | Fable 5 Is Back. Use It To Print With These $10K Websites |
| 2,095.2 | 20 | 19.4 | T2 | `8rVQuZlRaqo` | threat | A Practical AI Agent Workflow For Companies In 2027 (Guide) |
| 1,901.2 | 11 | 7.0 | T2 | `ikxxjRWX0Yg` | threat | Do not talk to Claude's new voice mode |
| 1,511.1 | 117 | 16.5 | T2 | `Ob5Vu-gD3mo` | threat | Claude Managed Agents Just Dropped, And It Kills n8n |
| 1,492.2 | 334 | 14.7 | T2 | `YIl-awY250k` | contrarian | What I'd Learn Instead of Automation in 2026 |
| 1,456.2 | 22 | 20.2 | T2 | `rbUFFMtKcaQ` | proof-first | I Gave GPT-5.6-Sol Unlimited Money to Make Ads (+ Results) |
| 1,315.1 | 225 | 341.7 | T3 | `MxyRjL7NG18` | threat | AGENTIC WORKFLOWS: Build & Sell AI Automations (2026) |
| 1,150.3 | 143 | 16.5 | T3 | `qKU-e0x2EmE` | loss-frame | Stop Fixing Your Claude Skills. Autoresearch Does It For You |
| 1,037.0 | 188 | 8.5 | T2 | `esXXuejofgk` | contrarian | Clawdbot Sucks, Actually |
| 941.2 | 154 | 47.7 | T3 | `sduaTkhIm_w` | proof-first | CLAUDE SKILLS FULL COURSE: Automate Your Work (2026) |
| 873.5 | 28 | 15.2 | T2 | `7Su6W_FlUbk` | demo-first | The BEST AI Video Strategy No One Is Using |
| 786.3 | 467 | 91.7 | T4 | `wLNw-rpklfE` | demo-first | Watch me start & sell an AI service in 10 hours |
| 718.7 | 24 | 46.1 | T4 | `DbZotE0Ch0g` | proof-first (proxy) | $20,354/m, solo, while working a 9-to-5 |
| 587.4 | 470 | 23.3 | T1 | `jBF48jNWPJE` | number-first | 5 "BORING" AI Automations To Sell For $1.5K+ Each in 2025 |
| 247.4 | 455 | 30.4 | T1 | `oAWe5wFwHlo` | demo-first | I Deep-Personalized 1000+ Cold Emails Using THIS AI System |
| 209.8 | 459 | 21.4 | T1 | `OroDNJl-pyc` | loss-frame | Scrape Unlimited Leads WITHOUT Paying for APIs (99% FREE) |
| 198.9 | 475 | 17.5 | T4 | `TxMAUMUn-is` | contrarian | Why I Don't Sell AI to Local Businesses (Despite What Gurus Claim) |
| 196.8 | 266 | 32.6 | T1 | `2XHgJXX49Jk` | proof-first | How to get SO many leads you don't know what to do with them |
| 190.4 | 306 | 29.7 | T4 | `bMmlCPLDk1c` | number-first | How I Would Start AI Consulting in 2026 (If I could start over) |
| 190.0 | 484 | 29.7 | T3 | `4PZYb86j4wg` | number-first | 80% of AI Automation Basics in Just 29 Minutes |
| 177.3 | 488 | 72.4 | T1 | `gsPGdq2C97c` | demo-first | Build This Automated AI LinkedIn DM System in 1 Hour (N8N) |
| 163.1 | 479 | 25.4 | T1 | `g_Q15Ibn3Iw` | number-first | 5 Industries Desperately Paying for AI Automation (2025) |
| 159.3 | 538 | 79.8 | T1 | `9zBtU1mwOR4` | proof-first | The N8N Instagram Parasite System (10K Followers In 15 Days) |
| 131.5 | 299 | 20.3 | T1 | `eLqveVYFWc4` | proof-first | It's Dumb, But Makes Getting Clients SO Easy |
| 123.3 | 550 | 50.3 | T1 | `bao3ogOcpiw` | number-first | How to Acquire Your First AI Automation Client For $0.00-$0.60 |
| 117.8 | 244 | 40.4 | T1 | `Uj-1we7Rew4` | demo-first | building a service business the LAZY way (Agentic Workflows) |
| 117.8 | 554 | 46.5 | T1 | `OLwEtOEF36A` | number-first | The 3 Best AI Automation Agency Niches in 2025 |
| 103.6 | 707 | 40.5 | T1 | `eElnA0mCzXw` | number-first | How I Scrape Thousands of Local Business Emails In 15 Minutes |
| 98.1 | 453 | 47.2 | T1 | `36xOZ1e6tuM` | contrarian | How She Built a $13k/m Agency Using Just ONE AI Automation |
| 69.8 | 389 | 19.8 | T1 | `XE6VcwCBSqA` | **none** | Steal This Cold Outreach Strategy & Make $9K/Month Selling AI |
| 69.6 | 472 | 40.5 | T1 | `yYVfcfa7n5A` | proof-first | I Built An AI Asset-Based Lead Gen System (Free Template) |
| 34.3 | 749 | 29.8 | T1 | `4ryBQ9P_p64` | proof-first | How I'd Automate a Plumbing Company in 15 Steps (AI & More) |

**Mechanism assignment rule:** each video is assigned the one mechanism that supplies the tension in the first sentence, taken from the deep-read's own Hook block. Where a deep-read names two ("Number-first plus contrarian plus price anchor"), the dominant one is used and the modifier is noted in §2c. Every assignment is reproducible from the Hook section of the corresponding file in `01-deep-reads/`.

## Appendix B: method notes

- All velocity figures come from `00-corpus.csv` (303 rows, snapshot 2026-08-03). Nothing was estimated.
- Medians, not means, throughout. The distribution is heavily right-skewed (top video 12,923.6, median video 69.7 in its own cohort).
- Spearman rank correlation used for continuous relationships, because the view distribution is not normal.
- Title-formula families were matched by regex against the full 303-title corpus, not just the 38. Family membership is reproducible.
- Where n is 1 or 2 the finding is labeled an anecdote in place. Do not build on those rows.
- Structural counts (hook present, number in hook, live build present, failure kept in, CTA hardness) were counted against the fixed 9-section schema of the 38 deep-reads. The counting rule is stated inline with each count so any one of them can be re-derived.

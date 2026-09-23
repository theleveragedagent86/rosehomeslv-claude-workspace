# Watch me start & sell an AI service in 10 hours

- **id:** wLNw-rpklfE · **url:** https://youtube.com/watch?v=wLNw-rpklfE
- **tier:** T4-THESIS
- **published:** 2025-04-23 · **views:** 367,203 · **views/day:** 786 · **runtime:** 91.7 min

## Hook (0:00–0:20)
> "Today, I'm going to start an AI automation service completely from scratch and build out all of the infrastructure that you need in order to get your very first paying client using this business model. I'm going to whip up the offers. I'm going to do the copywriting. I'm going to talk templates and blueprints. And I'm going to do it all live in front of you all the way up to getting my very first interested party on a call."

**Mechanism:** demo-first with a live open loop. He commits to an unfaked outcome (a real interested lead) before he has it, so the viewer stays to see whether he lands it. He even admits at [1:27] he titled it "in just X hours" because "I don't know what the X is yet."

## Thesis
Do not build a product and hope buyers appear, sell three unbuilt offers by cold email at volume and let the positive-reply data pick which product you actually build.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | hook | open loop, promises live unedited outcome |
| 0:29 | roadmap | five-step contents list, pre-empts "this will be chaotic" |
| 1:58 | niche picking | shows his own paid template, soft product placement |
| 3:59 | picks niches | "Why don't we do real estate agents?" chosen semi-randomly |
| 5:04 | research demo | reads Skool and Reddit threads live to mine customer pain |
| 8:10 | pre-empts objection | says do NOT automate customer research, it is the core skill |
| 13:40 | offer design | invents services off the cuff, "I'm just pulling some stuff out of my ass" |
| 18:35 | infrastructure | source, scrape, enrich framing, then Apollo plus Apify plus make.com |
| 35:20 | AI icebreaker | builds the personalization layer, shows failed prompt attempts on camera |
| 56:00 | copy formula | drops the reusable 4-question email structure |
| 74:01 | mistake shown | wastes 3,000 ops, keeps it in as authenticity proof |
| 81:30 | payoff | reveals reply counts, closes the loop opened at 0:00 |
| 90:28 | CTA | Maker School hard pitch with money-back guarantee |

## System demoed
End-to-end cold outbound machine. Inputs: three Apollo.io saved searches (website agencies, video agencies, US real estate agents 1 to 20 employees). Apify "Apollo code_crafter" [sic?] actor scrapes ~2,000 records per audience into Google Sheets. He deletes ~500 dead columns, concatenates the work-email and personal-email columns to recover more addresses, dedupes on email. make.com scenario reads each row, sends the headline, employment history, industry, city and country to GPT 4.1 mini with a few-shot prompt plus a rule to shorten company names ("San Fran instead of San Francisco"), writes a one-line icebreaker back to column I. CSV goes to Instantly with pre-purchased pre-warmed inboxes, 15 mailboxes, 150 sends per day per campaign, text-only first email, no open tracking, one follow-up at 2 days, Monday to Saturday 7am to 6pm ET. Two copy variants per campaign, split tested. Output: replies in the Instantly Unibox.

## Who it's for
A total beginner with no clients, no product and no niche who is intimidated by "what do I even sell." He explicitly says at [2:29] "I wanted to put myself in as similar a position to as many of you as possible," and he is selling to people who have not yet made a single dollar with an automation service.

## Economic argument
Cost side, verbatim: "The one that I use is called Apollo code_crafter just because it's like a$120 per thousand leads" [sic?, spoken as one-twenty per thousand] and "it's just $120 per thousand. So, not totally breaking the bank here." On a wasted run: "Sometimes you make mistakes and when you do, they cost you $6. And I just made myself a $6 mistake." Proof side, inside his own email copy: "we made 125K in a little over a week," "I actually used to run a videography company in Vancouver, BC, and I scaled it to about 10,000 bucks a month," and "scaled revenue to 90k a month at around 50% margins." Historical campaign benchmarks from his templates: "this one had a 4.8% reply rate still made me tons of money. This one down here was a little bit better, 11.6 ... This one made me 6.1% reply rate." Result: "In the last, I think 13 or 14 hours, we received a total of 11 replies. Seven of them were positive." Forward math: "we could already be in the neighborhood of generating 10 positive replies a day" and "If you can get them on a call, realistic rate is something like 60 to 75% positive reply to a call."

## CTA
- **What:** Join Maker School, his 90-day zero-to-one program, first client in 90 days or money back. Secondary: Make Money With Make for people already earning.
- **Where:** [1:27] soft, [56:00] mid-roll product placement while pulling templates, [90:28] hard close
- **How hard:** hard close, and the entire video doubles as a demo of the paid curriculum

## Title + thumbnail pattern
"Watch me <do the hard thing> in <N hours>" → real-time-proof format. The clock is the promise and the unknown outcome is the open loop. Reusable as "Watch me get a listing appointment from scratch in one day."

## Transferable to realtors?
- **Verdict:** ADAPTABLE
- **Why:** The scrape, enrich, AI-icebreaker, sequence stack transfers cleanly to agent-to-agent, investor, expired and vendor outreach, and the 4-question email formula (is this spam, who are you, why does it matter, what next) is directly usable today. But it is a B2B cold-email machine, so a realtor cannot point it at consumers without a different data source and different compliance footing. Worth flagging honestly for Ryan: real estate was one of his three test niches and it was the loser, "The real estate campaign has had three replies ... we've had zero opportunities ... I have a feeling this real estate campaign probably just ain't it, dog" [83:29].

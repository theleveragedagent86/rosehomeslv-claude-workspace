# 5 "BORING" AI Automations To Sell For $1.5K+ Each in 2025

- **id:** jBF48jNWPJE · **url:** https://youtube.com/watch?v=jBF48jNWPJE
- **tier:** T1-SYSTEM
- **published:** 2025-04-20 · **views:** 276,094 · **views/day:** 587 · **runtime:** 23.3 min

## Hook (0:00–0:20)
> "Here are five boring AI automations that you could sell today for 1,500 bucks a pop or more. These are not flashy chat bots. They're not AI agents. What they are are unsexy but very simple straightline automations that can add value to virtually any business. I sold systems just like this when I scaled my automation agency to $72,000 per month."

**Mechanism:** Number-first plus contrarian plus price anchor, all inside twenty seconds. The scare-quoted "BORING" gives permission to the viewer who feels behind on agents, and the $1,500 figure lands before any content so the whole video is priced.

## Thesis
Simple linear automations that fix an obvious business bottleneck sell more reliably and for more money than impressive-looking AI agents, because the buyer can understand them.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | hook | number, contrarian frame, price, revenue proof |
| 0:36 | system 1 | search-intent scraping, opens with the buyer's context not the build |
| 2:55 | design pattern | the dedupe sheet, teaches a reusable principle inside a specific build |
| 4:32 | enrichment | Perplexity research to AI icebreaker, shows the output text as proof |
| 6:13 | system 2 | podcast repurposing, self-references his own prior video for authority |
| 10:10 | system 3 | invoice chaser, pauses to restate the contrarian thesis |
| 11:13 | value framing | "I can't overstate just how much money is usually tied up in unpaid invoices" |
| 13:35 | system 4 | cyclic content generator, name-drops that it is his oldest published system |
| 18:33 | pre-empt objection | argues for a human in the loop before anyone can call the output slop |
| 19:36 | system 5 | email categorization, framed as the easiest foot in the door |
| 21:41 | client-retention trick | let the client edit the filter so they feel ownership |
| 22:08 | price close | restates $1,500, escalates to 10K, cites his own sales |
| 22:40 | CTA | Maker School with day-by-day roadmap and price-increase scarcity |

## System demoed
Five, each shown end to end on screen.
1. **Search-intent scraper.** Apify scrapes a LinkedIn jobs URL, filters (website exists, not linkedin.com, under 150 employees), dedupes against a Google Sheet by company name, GPT-4 mini filters for relevance, Any Mail Finder gets the CEO, a webhook catches results, Perplexity researches the person, AI writes a custom icebreaker, then an HTTP call pushes them into an Instantly campaign.
2. **Podcast repurposing engine.** Podcast URL in, Apify YouTube Transcript Ninja pulls the transcript, OpenAI extracts the 10 most engaging points as JSON, a split-out node fans them to three parallel generators (Instagram, LinkedIn, Facebook), DALL-E makes an image, everything lands in per-platform sheet tabs, then a 7am schedule trigger publishes the first row without a "posted on" value via the Meta Graph API or an HTTP request.
3. **Invoice chaser (make.com).** Reads a Google Sheet or Stripe/QuickBooks/Xero, filters status = overdue, branches on days elapsed (7/14/21/28/35/42), sends the matching pre-written follow-up email.
4. **Cyclic content generator (make.com).** Form takes keyword plus email, OpenAI web search finds competing articles, builds and then progressively improves an outline, splits it into sections, writes each section separately, summarizes each in three sentences to prompt an image, merges image plus text, aggregates to HTML, emails a Google Doc.
5. **Email categorizer (make.com).** New email fires a webhook, AI assigns one of four labels (sponsorship requests, people selling me stuff, invoices and receipts, worthwhile), applies the Gmail label and marks read.

## Who it's for
The automation freelancer or new agency owner who has the skills but not enough sellable offers. He says the goal is "you'll have added five more great systems to your arsenal", and the Maker School pitch is explicitly "zero to one" with daily tasks for someone who has not landed a first customer.

## Economic argument
Verbatim close: "You guys could sell any of these systems for $1,500 a pop or more. I've seen people sell a couple of these systems for more than 10K, and I myself have sold my content generator system for at least that amount on a couple of occasions." Opening credential: "I sold systems just like this when I scaled my automation agency to $72,000 per month." Value logic on the invoice system: "I can't overstate just how much money is usually tied up in unpaid invoices for the average B2B agency or manufacturing company." Other figures: "somebody that's run a $92,000 a month content writing company", OpenAI "tier two. I think you need like $30 or $50 on the card", community "over 2,000 people... and I increase the price every 100 members."

## CTA
- **What:** Join Maker School for the templates and blueprints to all five systems
- **Where:** [22:40] main pitch, [23:11] like/comment/subscribe
- **How hard:** mid-roll strength but placed at the end, with price-increase scarcity ("let this be the sign and let this be the permission you need")

## Title + thumbnail pattern
"<N> "<CONTRARIAN ADJECTIVE IN SCARE QUOTES>" <category> To Sell For $<price>+ Each in <year>" → count plus a self-deprecating quality claim plus an exact price plus a recency stamp. The scare quotes do the work: they signal the adjective is a trap and the payoff is money.

## Transferable to realtors?
- **Verdict:** DIRECT
- **Why:** Three of the five run for a realtor with only names changed: email categorization on a lead-heavy inbox, the podcast/video repurposing engine (one listing or market-update video fanned to IG, LinkedIn, Facebook on a schedule), and the cyclic content generator (neighborhood and community blog posts with a human editing pass). The invoice chaser has almost no realtor use case, and the search-intent scraper is B2B and would need a real estate rebuild.

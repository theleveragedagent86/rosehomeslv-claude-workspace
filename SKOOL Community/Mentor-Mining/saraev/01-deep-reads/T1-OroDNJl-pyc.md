# Scrape Unlimited Leads WITHOUT Paying for APIs (99% FREE)

- **id:** OroDNJl-pyc · **url:** https://youtube.com/watch?v=OroDNJl-pyc
- **tier:** T1-SYSTEM
- **published:** 2025-05-01 · **views:** 96,285 · **views/day:** 210 · **runtime:** 21.4 min

## Hook (0:00–0:20)
> "Hey, today I'm building a simple system in NAD [sic?] that lets you scrape emails from Google Maps completely free without needing any thirdparty APIs. That's right, we're going to do it entirely in NAND [sic?]. And what I'll do first is demo the flow before then showing you guys how to build it on your own from scratch."

**Mechanism:** Loss-frame plus demo-first. "Without paying for APIs" names a bill the viewer is already resenting, then he promises proof before instruction so nobody bails during the build.

## Thesis
You do not need a paid scraping API to build a lead list, a raw HTTP request to the Google Maps search URL plus two regex code nodes gets you the same emails for free.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | hook | names the cost being avoided, promises demo before tutorial |
| 0:34 | live proof | runs the flow, 8 emails land in the Google Sheet |
| 1:47 | teaching frame | "not from the outside in, but from the inside out", pre-empts "you just showed me a finished thing" |
| 2:20 | build starts | manual trigger, then the HTTP request to the Maps search URL |
| 3:29 | de-scare the code | "I just asked Chat GBT [sic?] in 10 seconds, whip me up a little snippet" |
| 5:04 | de-scare again | explains regex as "not some super convoluted scary programming stuff" |
| 6:47 | show the mess | admits the raw output is full of Google, gstatic, schema junk |
| 7:16 | fix live | builds the filter node in real time, iterating out bad domains |
| 9:01 | dedupe | 60 items into 27 |
| 9:34 | credibility beat | warns your IP gets blocked, adds a loop and a 1-second wait node |
| 12:16 | demo hygiene | adds a limit node so the recording does not take 30 seconds |
| 13:23 | second regex | swaps URL pattern for email pattern |
| 14:31 | admit the limits | "We couldn't find any emails in the first three", raises limit to 10 |
| 15:32 | error handling | on-error continue, "NAN [sic?] can't scrape all web pages" |
| 16:41 | finish | split out, dedupe, append row to Google Sheet |
| 18:04 | upsell the build | how to extend to sub-pages with a third loop |
| 19:13 | pre-empt failure | Google rate limits, proxies, SERP proxies, plugs the Appify [sic?] proxy course |
| 20:53 | CTA | 6-hour n8n course, like/comment/subscribe, Maker School |

## System demoed
An n8n (transcribed as "NAD"/"NAND"/"NAN" [sic?]) workflow. Input: a Google Sheet with one column of search strings like "Calgary plus dentist". Steps: (1) HTTP request to `www.google.com/maps/search?<query>` with ignore-SSL and include-response-headers turned on, returning raw HTML; (2) a JavaScript Code node running a regex against `$input.first().json` to extract every URL; (3) a Filter node with "does not contain" rules stripping schema, google, gg, gstatic; (4) Remove Duplicates; (5) Loop Over Batches with a 1-second Wait node and an HTTP request per site, redirects disabled, on-error continue; (6) a second Code node with an email regex; (7) Filter for non-null, Split Out, Remove Duplicates; (8) Append Row in Google Sheets. Extension he describes but does not build: crawl sub-pages with a third loop, and route the first request through a SERP proxy to beat Google rate limits.

## Who it's for
A beginner-to-intermediate n8n builder doing cold outbound lead gen who is currently paying for, or scared off by, scraping APIs like Apollo or Apify. Explicitly someone with no JavaScript background.

## Economic argument
He makes no dollar argument at all, only a cost-avoidance one. Verbatim close: "Hopefully you guys saw just how easy and straightforward it was to put together a real actual NN [sic?] scraper that allows you to get and extract email addresses directly from Google Maps listings without requiring any APIs or third party services." **No figures stated** for cost, savings, or lead value. The only numbers in the video are throughput counts: 8 emails in the demo, 302 items filtered to 133, 60 deduped to 27, a test limit of 3 then 10, and "In the demo, I think we pumped in like 300 or something. We got like a 100."

## CTA
- **What:** Grab the free template in the description; then the free 6-hour n8n zero-to-hero course; then Maker School, his paid AI automation program. Also plugs the Appify [sic?] proxy course as a free affiliate resource.
- **Where:** 20:18 (Appify), 20:53 (course, subscribe, Maker School)
- **How hard:** soft mention throughout, one stacked soft close at the very end. No price named, no urgency.

## Title + thumbnail pattern
"<Do the expensive thing> WITHOUT Paying for <the thing everyone pays for> (<n>% FREE)" → bill-avoidance framing with a hedged percentage. The "99%" is doing quiet legal work, it admits an exception without naming one.

## Transferable to realtors?
- **Verdict:** ADAPTABLE
- **Why:** The mechanism transfers cleanly to B2B real estate targets, scraping property managers, contractors, lenders, title reps, or investor-facing directories to build a referral list, and he even name-checks "county real estate databases" at 20:53. But it does not transfer to consumer lead gen: scraping homeowner contact info for unsolicited email runs straight into CAN-SPAM, state DNC rules, and MLS/IDX terms, so this needs a different data source and an opt-in path before a realtor can use it.

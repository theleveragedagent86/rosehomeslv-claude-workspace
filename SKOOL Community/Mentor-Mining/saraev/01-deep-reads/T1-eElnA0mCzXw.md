# How I Scrape Thousands of Local Business Emails In 15 Minutes

- **id:** eElnA0mCzXw · **url:** https://youtube.com/watch?v=eElnA0mCzXw
- **tier:** T1-SYSTEM
- **published:** 2024-08-26 · **views:** 73,260 · **views/day:** 104 · **runtime:** 40.5 min

## Hook (0:00–0:20)
> "hey everybody Nick here have you ever wanted to scrape local service business email addresses I'm talking the plumber across the street maybe the flower shop down the block well in this video I'm going to show you a simple system that takes less than 20 minutes to set up that lets you scrape thousands of local service businesses in just minutes"

**Mechanism:** number-first with a concreteness anchor. "The plumber across the street" makes an abstract data problem physical, then "less than 20 minutes" and "thousands" set a small-effort, large-payoff ratio the viewer wants verified.

## Thesis
Lead data should never be your bottleneck, because Google Maps plus an off-the-shelf scraper plus an email enrichment API produces thousands of contactable local businesses for a few dollars.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | hook | number-first promise, "watch me build it" |
| 0:39 | map the flow | Whimsical diagram, reduces perceived complexity before any tool appears |
| 1:09 | show the raw source | searches plumbers in Calgary, estimates "500 to a th000 minimum" |
| 2:23 | anti-build argument | "no use rebuilding a wheel," pushes Apify store over custom code |
| 3:27 | cost objection killed | "it just gives you $5 in credit just up front" |
| 6:24 | port to make.com | explains why he shows the tool first, then the automation |
| 10:54 | de-intimidate | calls input JSON "the most intimidating field," then defuses it |
| 16:57 | price anchor | "I've sold systems like this for anywhere from $1,000 to $2,000" |
| 18:13 | filter step | website-exists filter, teaches the enrichment failure mode |
| 21:35 | positioning hack | formats the Google Sheet prettily to raise perceived deliverable quality |
| 32:51 | honest yield | 16 of 26 rows got emails, roughly 60% |
| 36:21 | production fix | splits into two scenarios so the 120-second sync timeout stops breaking it |
| 39:50 | CTA | soft, asks for build requests in comments |

## System demoed
Two make.com scenarios. Scenario 1 runs on a daily schedule and fires the Apify "Google Maps Extractor" actor (Compass) with an input JSON containing deeperCityScrape, a locationQuery such as "Calgary Alberta", maxCrawledPlacesPerSearch, and a searchStringsArray such as plumber, flower shop, HVAC. Scenario 2 watches for that actor run finishing via webhook, pulls "get dataset items" with the defaultDatasetId, filters to rows where the website field exists, sends the domain to Any Mail Finder ("search for a company's emails"), then appends business name, website, unformatted phone, review score and the email array to a Google Sheet. A sheet-side SPLIT formula on the email string fans multiple emails across columns instead of hardcoding email 1 through 5 in make.com. Final refinement: a second filter so only rows with at least one email get written.

## Who it's for
Someone starting or running a small cold-outreach or automation service who cannot afford paid lead databases and does not want to write a scraper. He repeatedly says he uses free plans on purpose "just to show you guys how much you can get done with $5 a month in usage."

## Economic argument
Verbatim: "I've sold systems like this for anywhere from $1,000 to $2,000 so I just wanted to recreate exactly what that looks like for you guys." On cost: "the cool part about apify is it just gives you $5 in credit just up front so you could scrape a lot of leads essentially with that $5 in credits" and "you could theoretically run a system like this for just a few dollars a day you just need to spend money on the make.com operations and then the apfi um I think it's like memory or runtime." On yield: "16 out of 26 is about 60% or so of the emails which is a reasonable good result uh not the best result but it's pretty solid so you know if if you were to feed in 10,000 or so you would get 6,000 email um 6,000 rows with the presence of at least one email."

## CTA
- **What:** Drop build requests in the comments, like and subscribe. Community mention is passing only.
- **Where:** [21:35] passing mention of "my community um which teaches people how to do this stuff", [39:50] close
- **How hard:** soft mention. This is the least salesy video in the batch.

## Title + thumbnail pattern
"How I <get a scarce asset> in <short time>" → speed-as-proof. The asset (emails) is the thing the viewer already wants, the time figure is the credibility hook. Reusable as "How I pull every expired listing in Clark County in 10 minutes."

## Transferable to realtors?
- **Verdict:** DIRECT
- **Why:** Change "plumber, Calgary" to "mortgage broker, Las Vegas" or "property manager, Henderson" and the exact pipeline runs unmodified, producing a referral-partner and vendor contact list in a sheet. Caveat worth stating plainly: the output is business emails, so it builds referral and commercial-prospecting lists, not buyer or seller leads, and any outreach still has to clear CAN-SPAM and brokerage advertising rules.

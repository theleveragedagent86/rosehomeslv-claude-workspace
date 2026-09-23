# Kimi K3 Designs Websites That Feel Like MOVIES For Just $1

- **id:** 0zlwXSVmoeg · **url:** https://youtube.com/watch?v=0zlwXSVmoeg
- **tier:** T2-PACKAGING
- **published:** 2026-07-22 · **views:** 117,471 · **views/day:** 9,789 · **runtime:** 21.6 min

## Hook (0:00–0:20)
> "So, KimmyK3 [sic?] can design absolutely gorgeous, beautiful websites just like these for literally just a dollar or two. And in this video, I'm going to show you everything that you need to do in order to create these sorts of cinematic journey experiences and then host them on a website."

**Mechanism:** demo-first plus price anchor. The finished sites are on screen while he speaks, so the visual does the persuading and the "dollar or two" creates a gap between perceived value and stated cost that the viewer stays to resolve.

## Thesis
The wow in a cinematic scroll site comes from the video asset, not the code, so a cheap frontier model plus a video generator and a frame interpolator produces agency-tier web experiences for a couple of dollars.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | hook | demo-first, price anchor, promises free prompts |
| 0:38 | reveal the trick | "the website itself is what's moving ... it's actually just a video in the background" |
| 1:48 | tool intro | Kimmy K3 [sic?] from Moonshot, benchmarks it against "Fable, GPT 5.6, Soul" [sic?] |
| 2:26 | scarcity note | subscriptions "heavily throttled," plans Moderato, Allegrato, Allegro, Vivace [sic?] |
| 2:57 | de-intimidate | walks the terminal install slowly for non-coders |
| 4:02 | prompt 1 | ideation prompt for 10 scroll-driven concepts, 8-second macro journey |
| 4:40 | philosophy aside | AI ideates over a large space, humans apply taste to pick |
| 7:39 | prompt 2 | concept to video prompt, using an example to set detail level |
| 8:16 | creative gen | Cinematic Studio 3.0 [sic?] on Higgsfield, 16:9, 1080p, 8s, ~80 credits |
| 8:53 | quality argument | interpolation from 30 to 60 fps, "unlike what a lot of other people do" |
| 12:25 | batching | runs three generations at once, trades credits for wall-clock time |
| 14:05 | automation upgrade | installs the Higgsfield MCP into Kimmy so it calls the models directly |
| 18:28 | deploy | Netlify OAuth token pasted into the agent, site goes live |
| 19:05 | payoff | "the motherload," one prompt that runs the whole pipeline end to end |
| 20:57 | CTA | Maker Zero free, then Maker School |

## System demoed
Six stages, all prompt-driven. 1) Kimmy K3 [sic?] generates 10 scroll-driven landing page concepts, each constrained to a single continuous 8-second extreme macro journey. 2) A second prompt converts a chosen concept into a detailed cinematic video prompt, using a worked example to set the detail bar. 3) Higgsfield Cinematic Studio 3.0 [sic?] generates the clip at 16:9, 1080p, 8 seconds, roughly 80 credits, three run in parallel. 4) ByteDance AIGC [sic?] interpolates 30 fps to 60 fps so scroll scrubbing is not choppy. 5) The Higgsfield MCP is installed into Kimmy Code (writes an mcp.json) so the agent calls generation and upscaling itself rather than him using the web UI. 6) A long "site prompt" takes the local video file path plus the original concept and produces the scroll-bound site with a tour autoplay mode, then a Netlify personal access token pasted into the agent deploys it. The finale is a single consolidated prompt that runs all six stages and only asks two questions.

## Who it's for
Someone who wants to produce visually premium web work without design or front-end skill, framed at the end as someone who wants to "sell these sorts of interactive visual experiences to other people and get paid for it." Not a developer video, he narrates the terminal for people who find it "kind of intimidating if you're new to this sort of stuff."

## Economic argument
Thin and mostly implied by the title. Verbatim: "can design absolutely gorgeous, beautiful websites just like these for literally just a dollar or two." On credits: "obviously every video generation uh you know, consumes some amount of credits. In this case, it looks like it's about 80." On the batching tradeoff: "Obviously, I'm trading off my money here in credits for, you know, time and and efficiency, but I typically do this because I'm never really 100% of the time with the outputs of AI. I'm satisfied maybe 30 to 50% of the time." No total build cost, no client price, no revenue figure is stated. Guarantee at close: "if you do not acquire client number one, I will literally just give you your money back."

## CTA
- **What:** Free prompts inside Maker Zero, then Maker School, the 90-day accountability program with a first-client-or-refund guarantee.
- **Where:** [3:26] and [16:30] free-prompt mentions used as retention devices, [20:57] hard close
- **How hard:** mid-roll pitch for the free community, hard close at the end, self-aware about it ("I'll stop shilling my own products")

## Title + thumbnail pattern
"<New model> does <premium creative outcome> for just $<tiny number>" → price-gap. Pair a high-status output with an absurdly low cost, and let a new model name supply the recency. Highest views-per-day in this batch by an order of magnitude, so the model-name-plus-price-gap combination is the strongest packaging lever Saraev is currently pulling.

## Transferable to realtors?
- **Verdict:** ADAPTABLE
- **Why:** A scroll-driven cinematic microsite is a real luxury-listing and community-page format, and the pipeline shape (concept, hero video, interpolate, scroll-bind, deploy) transfers. The rebuild is total on the creative source: a listing page has to use real photography and video of the actual property, so the AI macro-journey asset can only be used for brand, neighborhood or abstract hero sections, never to depict a home for sale. Treat the front half of this video as web-craft technique and discard the generative-imagery-of-a-property idea entirely.

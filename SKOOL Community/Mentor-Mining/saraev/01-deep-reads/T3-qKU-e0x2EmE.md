# Stop Fixing Your Claude Skills. Autoresearch Does It For You

- **id:** qKU-e0x2EmE · **url:** https://youtube.com/watch?v=qKU-e0x2EmE
- **tier:** T3-TEACHING
- **published:** 2026-03-13 · **views:** 164,492 · **views/day:** 1,150 · **runtime:** 16.5 min

## Hook (0:00–0:20)
> "I freaking love Claude code skills. I think you do too, but sometimes they're a little bit unreliable. I would say about 70% of the time I run a skill, I get an intended output, but 30% of the time it's a bag of rocks."

**Mechanism:** Number-first loss-frame. He names a failure rate the viewer has felt but never quantified, so the 30% becomes a wound the rest of the video promises to close.

## Thesis
A prompt is not a thing you hand-tune, it is a thing you optimize, so give an agent an objective metric, an automated measurement tool, and permission to mutate the prompt on a loop, and your skills will improve themselves overnight.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | hook | quantifies a shared frustration, opens the reliability loop |
| 0:37 | borrowed authority | attributes autoresearch to Andrej Karpathy, ex-OpenAI and ex-Tesla |
| 1:15 | de-scope the source | "you don't need to read the whole repo", only three files matter |
| 1:56 | analogy | maps train.py to your skill.md and program.md to your agent |
| 2:29 | proof drop | unrelated case: website load time 1,100 ms down to 67 over 67 tests |
| 3:05 | future-value reframe | the log of attempted changes is itself an asset to hand to GPT-6 or Opus 5.0 |
| 3:38 | the recipe | names the three required ingredients: objective metric, measurement tool, thing to change |
| 5:21 | teach evals | argues prompts are noisy distributions, so you must run many and take mode and median |
| 7:07 | make it concrete | picks his own diagram-generator skill as the meta example |
| 7:44 | show the rubric | reads his four binary criteria out loud |
| 8:58 | live build | pastes the repo link, the four criteria, and a Whisper Flow voice prompt into the agent |
| 11:07 | price anchor | 2 cents per generation, 20 cents per test, ~$10 to optimize the skill |
| 11:41 | live results | dashboard shows score moving from 32 out of 40 to 37 |
| 13:25 | scale claim | lists other skills he will run this on, promises a meta skill |
| 13:56 | payoff | hits 39 out of 40, "equivalent to me getting 97.5% on a test" |
| 14:35 | pre-empt failure | warns against Likert scales and over-narrow evals that the model will game |
| 15:45 | CTA | free access below, then pitch for the 4-hour Claude Code course |

## System demoed
Take Karpathy's autoresearch repo pattern and point it at a Claude Code skill. Ingredients: (1) an objective metric, here an eval pass rate; (2) an automated measurement tool, here an agent-written test suite scored by Claude Sonnet Vision; (3) something to mutate, here the skill's markdown prompt. He hands the agent the repo URL, four binary yes/no criteria (text legible and grammatically correct, fits a pastel color palette, layout is linear left-to-right or top-to-bottom, free of numbers and ordinals), plus the instruction to generate 10 diagrams every 2 minutes, score them out of 40, mutate the prompt, and keep the winner. Runs in Antigravity with the Claude Code extension, model is Opus 4.6, images from Nano Banana Pro 2, output pasted into Excalidraw. It builds itself a live scoring dashboard.

## Who it's for
Someone who already writes and runs Claude Code skills daily, is annoyed that they work most but not all of the time, and has never built an eval set.

## Economic argument
He prices the optimization loop directly. Verbatim: "My total cost is about 2 cents per generation using this super fast model. And that means, you know, if we're going to run 10 every single time, logically speaking, I'm going to spend about 20 cents per test. So, if within 50 tests I can get it to a good place, I will have optimized the skill for about $10. And just given how much money my YouTube videos make me, you know, a good banger video might make me several hundred dollars in ad revenue per day. Um obviously, this is like a pretty positive return on investment for me." Supporting figures: "this auto research methodology took my load speed from about 1,100 milliseconds literally down to 67", "an 81.3% improvement in time", over "67 different tests", and the skill score moving "from uh 32 up to 37" and eventually "39 out of 40".

## CTA
- **What:** Take the setup free ("No email, no gatekeeping whatsoever"), then optionally buy the 4-hour Claude Code course; also leave a comment with next-video requests.
- **Where:** 15:14, 15:45, 16:22
- **How hard:** soft mention for the freebie, single soft mid-roll-style pitch for the course at the very end. No hard close.

## Title + thumbnail pattern
"Stop <the manual chore you're doing>. <New named technique> Does It For You" → permission-to-quit framing. Names a labor the viewer resents, then hands them a proper-noun mechanism to blame it on.

## Transferable to realtors?
- **Verdict:** ADAPTABLE
- **Why:** The eval loop is exactly the missing piece for realtor AI assets, listing descriptions, CMA narratives, DM replies, that "work 70% of the time". The rebuild is defining the rubric: a real estate version needs binary criteria for fair-housing compliance, factual accuracy against MLS data, and brand voice, plus an evaluator that can check facts, not just look at an image.

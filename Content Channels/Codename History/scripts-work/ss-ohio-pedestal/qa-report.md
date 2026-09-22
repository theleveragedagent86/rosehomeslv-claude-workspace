# QA Report: Codename: Pedestal - The Broken Tanker That Saved Malta

Adversarial re-verification with fresh independent web checks. I did not trust the research report; I re-checked each high-risk claim against sources independently and redid the loss math.

## Claim-by-claim verification

| # | Claim (as spoken) | Where | Source(s) checked | Verdict |
|---|-------------------|-------|-------------------|---------|
| 1 | Malta sat on the Axis North Africa supply route and was one of the most heavily bombed places of the war; faced surrender by September 1942 without resupply | Act 1 | IWM "Operation Pedestal and the Siege of Malta"; Wikipedia "Operation Pedestal" | VERIFIED |
| 2 | Operation Pedestal = 14 merchant ships with a large Royal Navy escort | Act 2 | IWM; Wikipedia "Operation Pedestal"; Warfare History Network | VERIFIED |
| 3 | Convoy passed Gibraltar in the second week of August 1942 (sailed 2/3 Aug, passed Gibraltar 9/10 Aug) | Act 2 | Wikipedia "Operation Pedestal"; IWM | VERIFIED |
| 4 | SS Ohio built in America (Pennsylvania) for Texaco/The Texas Company; British Merchant Navy crew | Act 2 | Wikipedia "SS Ohio" | VERIFIED |
| 5 | Master was Captain Dudley Mason | Act 2, 7 | Wikipedia "Dudley Mason"; Wikipedia "SS Ohio" | VERIFIED |
| 6 | HMS Eagle torpedoed by German submarine U-73 (Helmut Rosenbaum), four torpedoes, sank in ~4 minutes on 11 Aug 1942 | Act 3 | Wikipedia "HMS Eagle (1918)"; Wikipedia "Operation Pedestal" | VERIFIED |
| 7 | 131 of Eagle's men killed, many trapped in machinery spaces | Act 3 | Wikipedia "HMS Eagle (1918)"; uboat.net; ww2db | VERIFIED (see conflict note) |
| 8 | Hundreds of Eagle survivors pulled from the sea | Act 3 | Wikipedia "HMS Eagle (1918)" (929 survivors rescued) | VERIFIED |
| 9 | HMS Indomitable badly damaged by dive bombers, could no longer operate aircraft | Act 3 | Wikipedia "Operation Pedestal"; Warfare History Network | VERIFIED |
| 10 | Italian submarine Axum torpedoed Ohio amidships; hole about the size of a small house (~24 x 27 ft) | Act 3-4 | Wikipedia "SS Ohio"; Warfare History Network | VERIFIED |
| 11 | A shot-down Ju 87 Stuka crashed onto Ohio; a second downed aircraft also came down on her | Act 4 | Wikipedia "SS Ohio"; Warfare History Network | VERIFIED |
| 12 | Near-misses lifted the loaded tanker out of the water; her back broke; engines died | Act 4 | Wikipedia "SS Ohio" | VERIFIED |
| 13 | Crew abandoned and reboarded Ohio more than once | Act 4 | Wikipedia "SS Ohio"; War History Online summary | VERIFIED |
| 14 | Night torpedo-boat attacks sank/crippled ships; HMS Cairo lost, HMS Foresight crippled, HMS Manchester scuttled by her own crew | Act 5 | Wikipedia "Operation Pedestal"; Wikipedia "HMS Manchester (15)"; Naval Historical Society of Australia | VERIFIED |
| 15 | HMS Penn tried to tow alone; lines snapped; HMS Bramham added; Ohio lashed between two destroyers; HMS Ledbury assisted | Act 5 | Wikipedia "SS Ohio"; Warfare History Network | VERIFIED |
| 16 | Ohio reached Grand Harbour, Valletta on 15 Aug 1942, the Feast of Santa Marija | Act 6 | Wikipedia "SS Ohio"; Warfare History Network; IWM | VERIFIED |
| 17 | Fuel pumped ashore as the ship sank; Ohio settled onto the harbour bottom after delivering | Act 6 | Wikipedia "SS Ohio" | VERIFIED |
| 18 | 14 merchant ships set out, only 5 reached Malta, 9 lost | Act 7 | Wikipedia "Operation Pedestal"; IWM; Warfare History Network | VERIFIED |
| 19 | RN lost carrier Eagle, cruisers Manchester and Cairo, destroyer Foresight; Indomitable badly damaged | Act 7 | Wikipedia "Operation Pedestal"; Warfare History Network | VERIFIED |
| 20 | More than 500 sailors and airmen killed | Act 7 | IWM; Wikipedia "Operation Pedestal" | VERIFIED |
| 21 | Captain Mason awarded the George Cross; citation wording ("skill and courage of the highest order... her valuable cargo... eventually reached Malta") | Act 7 | Wikipedia "Dudley Mason"; The Gazette (London Gazette 35659) | VERIFIED |
| 22 | Ohio never sailed again, eventually scrapped | Act 7 | Wikipedia "SS Ohio" | VERIFIED |
| 23 | Convoy delivered tens of thousands of tons of supplies, enough to sustain Malta for weeks | Act 7 | Wikipedia "Operation Pedestal" (~32,000 tons); Warfare History Network | VERIFIED |

## Math re-check

- 14 merchant ships set out, 5 reached Malta -> 14 - 5 = 9 lost. Matches "nine were sunk." CORRECT.
- Eagle: 131 killed + 929 rescued survivors are internally consistent across the dedicated sources. CORRECT.
- Script avoids any invented precise total-dead figure; uses sourced "more than 500." CORRECT.

## Issues found and fixed during QA

1. George Cross line was originally a loose paraphrase ("skill and determination... vital cargo"). Fixed to track the real London Gazette citation ("skill and courage of the highest order... her valuable cargo... eventually reached Malta"). Now accurate.
2. Added a sourced night-action beat (Cairo/Foresight/Manchester) so the "9 lost" total is explained rather than asserted, and confirmed Manchester was scuttled on her captain's order after Italian MTB attack. Accurate.

## Conflict resolution

- HMS Eagle death toll: Warfare History Network states ~260 killed; the dedicated HMS Eagle record, uboat.net, and ww2db all give 131. Resolved in favor of 131 (specific, multiply-corroborated, dedicated-ship sourcing). Script uses 131. Not averaged.
- "Supplies enough for ~10 weeks" (Wikipedia) vs "three months" (some outlets): script says "for weeks" and "long enough," staying safely inside both. No overclaim.

## Tone check

- Human-cost beats straight? YES. HMS Eagle sinking (131 dead, men trapped below) is marked TONE: STRAIGHT and carries no joke. The night action losses (Cairo, Foresight, Manchester, merchant crews) are marked TONE: STRAIGHT. The Act 7 cost section (9 of 14 ships, four warships, 500-plus dead) is entirely straight and explicitly states "both things are true at once. It saved Malta. And it cost a terrible amount." The civilian-siege beat in Act 1 is marked TONE: STRAIGHT. No jokes land on any death, casualty, or suffering beat. PASS.
- Jokes ride only on documented absurdity (a tanker surviving a torpedo, two crashed planes, and a broken back, then being dragged between destroyers). No invented flaws or fabricated bits.

## Cold read notes

- Reads cleanly in the OverSimplified voice. Every act ends on a hook or cliffhanger fragment ("It did not miss.", "It just needed to hold on a little longer.", "So the Royal Navy came up with a plan...").
- No brackets or stage directions inside any NARRATOR line.
- No em-dashes anywhere (grep confirmed 0).
- Narration word count 3,009, within 10% of the 3,300 target for the deep-dive tier.
- No real-estate, Las Vegas, Lofty, or contact-info contamination.
- All required sections present: title line, header, ACCURACY + VOICE notes, COLD OPEN + TITLE CARD, seven acts with timecodes, OUTRO + END, PRODUCTION NOTES (3 titles + recommended), YouTube description, FACT-CHECK LOG, SOURCES block.

## VERDICT: PASS

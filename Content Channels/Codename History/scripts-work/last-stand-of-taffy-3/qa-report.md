# QA Report: The Japanese Navy Attacked the Wrong Fleet (Last Stand of Taffy 3 / Battle off Samar)

**POST-REVISION PASS (pass 2).** This replaces the pass-1 report. Pass 1 raised 11 issues and returned FAIL. This pass checks the revision.

**Scope of this pass:** each of the 11 original issues re-verified against the sources (not merely checked for changed wording), the new and changed narration checked for fresh claims, mechanical checks re-run from scratch, and the tone gate re-read end to end. The 82-claim sweep from pass 1 was not repeated; claims untouched by the revision carry their pass-1 VERIFIED status.

**Headline:** every one of the 11 original issues is resolved in the narration, and several fixes are better than what I asked for. **The script body is clean.** What is not clean is the production apparatus around it: the ACCURACY NOTE, PRODUCTION NOTES and FACT-CHECK LOG were not updated with the script and now assert claims the writer deliberately removed, and the build counts are stale. That is a metadata sync, not a factual regression, but it is a live re-insertion risk at build time and it fails the gate.

---

## Status of the 11 original issues

| # | Original issue | Status | Verification |
|---|---|---|---|
| 1 | "Nimitz's real message was six words," then nine words spoken | **RESOLVED** | Now "Nimitz's real question was one line. Where is, repeat, where is Task Force Thirty Four." No count claimed, no math to be wrong. (Residual in PRODUCTION NOTES, see R3) |
| 2 | 1,785 / 635 placed after St. Lo, annexing St. Lo's dead into a figure that excludes them | **RESOLVED, and improved** | Three new beats do the work explicitly: "Four ships sank in the gun battle. St. Lo is not among them." / "Those four carried one thousand seven hundred eighty five men." / "They went down with their ships, or into the water." This now tracks NHHC H-036 and H-084 almost word for word ("Of the four U.S. ships that were lost, 1,785 crewmembers went down with the ship or into the water"). New card lists the correct four ships |
| 3 | "A near miss set off Suzuya's torpedoes" (NHHC says bomb hit, combinedfleet says near miss) | **RESOLVED** | Now "Suzuya's own loaded torpedo mount took her with it." The contested trigger is gone; only what both sources agree on remains. (Residual in FACT-CHECK LOG, see R5) |
| 4 | "Yamato ran north for ten miles" single-sourced to combinedfleet | **RESOLVED in narration** | Now "Yamato ran north until the torpedoes ran out of fuel." Distance dropped, "ten minutes" still correctly absent. (Residual in five places in the notes, see R1) |
| 5 | "seven miles" where NHHC says seven nautical miles | **RESOLVED** | Now "They were seven nautical miles away." Matches NHHC Waldman exactly. (On-screen card still reads "7 MILES", see R8) |
| 6 | "absorbed forty direct hits," de-hedged and understated | **RESOLVED, and improved** | Split into two beats: "Hoel went in on the battleship Kongo at fourteen thousand yards." and "Her captain estimated she absorbed more than forty direct hits." Both match DANFS Hoel exactly: Kintberger opened fire at 14,000 yards; "in Kintberger's estimation, more than 40 direct hits" |
| 7 | "Kumano's bow came off. Removed." overstated vs both Tier 1 sources | **RESOLVED, and improved** | Now "One hit Kumano's bow and set it alight." (NHHC Waldman: "hitting the bow of heavy cruiser Kumano and setting it aflame") and "Her speed dropped to twelve knots. Done by a destroyer." (DANFS Johnston: "reducing her speed to 12 knots"). The new version is both more accurate and a better beat. (Residual in FACT-CHECK LOG, see R4) |
| 8 | Carr's "died five minutes later" and the shipmate sequence presented as flat fact when both are Hornfischer | **RESOLVED** | Now attributed: "Survivors remembered a shipmate finding him mortally wounded..." / "They remembered coming back and finding Carr on his feet, holding it again." / "He died of his wounds." The five-minute figure is gone; "died of his wounds" matches DANFS Carr |
| 9 | "an insult Nimitz never wrote **and never knew about**" (second half unsourced) | **RESOLVED** | Now "So Halsey read an insult that Nimitz never wrote." |
| 10 | Message-form visual silently elided the middle of the dispatch | **RESOLVED** | Card now carries the complete text with an explicit "no words omitted" instruction, matching NHHC H-038 verbatim including "ACTION COM THIRD FLEET INFO COMINCH CTF SEVENTY-SEVEN X" |
| 11 | "fired them at an enemy ship once" resting on navweaps alone | **RESOLVED by reformulation** | Now "One surface action in her whole career put that battery onto enemy ships," paid off in Act 2 with "This was that surface action." The narrowed claim is uncontroversial and supported by the NHHC record already in hand: H-036/H-084 cover Samar, and H-044-3 covers her only other sortie in April 1945, where she was destroyed by aircraft without engaging surface ships. (FACT-CHECK LOG still cites navweaps alone, minor) |

**11 of 11 resolved in the narration. No fix introduced a factual error.**

---

## Claim-by-claim verification, new and changed text only

| # | Claim (as spoken) | Where | Source(s) checked | Verdict |
|---|---|---|---|---|
| N1 | "One surface action in her whole career put that battery onto enemy ships." | Cold Open | NHHC H-044-3 (April 1945 sortie, destroyed by air attack, no surface engagement); NHHC H-036 / H-084 (Samar) | VERIFIED |
| N2 | "This was that surface action." | Act 2 | Same | VERIFIED |
| N3 | "One hit Kumano's bow and set it alight." | Act 3 | NHHC Waldman: "hitting the bow of heavy cruiser Kumano and setting it aflame" | VERIFIED |
| N4 | "Her speed dropped to twelve knots. Done by a destroyer." | Act 3 | DANFS Johnston: torpedo hit the bow "damaging forward watertight compartments and reducing her speed to 12 knots" | VERIFIED |
| N5 | "Hoel went in on the battleship Kongo at fourteen thousand yards." | Act 3 | DANFS Hoel: Kintberger selected the leading battleship at 18,000 yards; "At 14,000 yards, Hoel reached the maximum effective firing range of her five as-yet silent five-inch guns" | VERIFIED |
| N6 | "Her captain estimated she absorbed more than forty direct hits." | Act 3 | DANFS Hoel: "in Kintberger's estimation, more than 40 direct hits from five-, eight-, and sixteen-inch shells" | VERIFIED, hedge and attribution both now correct |
| N7 | "Yamato ran north until the torpedoes ran out of fuel." | Act 3 | NHHC H-036 / H-084: the attack "bluffed Yamato, Kurita's flagship, into turning away, taking agonizing... minutes to get back into the fight" | VERIFIED, no unsourced distance |
| N8 | "They were seven nautical miles away. One cruiser division closed at thirty three knots." | Act 5 | NHHC Waldman: "they were, in fact, only seven nautical miles away"; combinedfleet Chikuma TROM for 33 knots | VERIFIED |
| N9 | "Nimitz's real question was one line. Where is, repeat, where is Task Force Thirty Four." | Act 5 | NHHC H-038 | VERIFIED |
| N10 | "Every station must strip it. Every station did, except one." | Act 5 | NHHC H-038; Kahn p. 609; Frank 2019 | VERIFIED (unchanged in substance) |
| N11 | "So Halsey read an insult that Nimitz never wrote." | Act 5 | Mobilia 2024: "not authored by Nimitz. It was routine padding added by CINCPAC's communications watch officer" | VERIFIED |
| N12 | "Suzuya's own loaded torpedo mount took her with it." | Act 5 | NHHC H-084: "succumb to secondary explosion of its own torpedo bank"; combinedfleet Suzuya TROM; Kurita USSBS Nav No. 9 | VERIFIED, contested trigger correctly dropped |
| N13 | "Four ships sank in the gun battle. St. Lo is not among them." | Act 5 | NHHC H-084: "the U.S. lost one escort carrier (Gambier Bay), two destroyers (Johnston and Hoel), and one destroyer escort (Samuel B. Roberts)"; St. Lo sank separately to the kamikaze | VERIFIED |
| N14 | "Those four carried one thousand seven hundred eighty five men." | Act 5 | NHHC H-036 and H-084, both verbatim. **Arithmetic re-checked:** Johnston 327 + Hoel 338 + Samuel B. Roberts 210 = 875; 1,785 - 875 = 910 implied for Gambier Bay, consistent with her DANFS complement of 860 plus embarked air group | VERIFIED, and the aggregate reconciles |
| N15 | "They went down with their ships, or into the water." | Act 5 | NHHC: "went down with the ship or into the water" | VERIFIED, scope now exact |
| N16 | "Six hundred thirty five of them died." | Act 5 | NHHC H-036 and H-084. "Them" now unambiguously refers to the 1,785 from the four gun-battle losses | VERIFIED, scope corrected |
| N17 | Carr beats, now attributed to survivor recollection; "He died of his wounds." | Act 4 | DANFS Carr (FFG-52): "died of his wounds shortly before Samuel B. Roberts sank"; recollection sequence correctly attributed rather than asserted | VERIFIED |
| N18 | Full dispatch text on the Act 5 message card | Act 5 | NHHC H-038 verbatim | VERIFIED |

**One latent tension, correctly handled and worth recording:** the script states Hoel 252 dead and Johnston 186 dead (DANFS, on screen in Act 4) and separately states 635 dead across the four ships (Cox, in Act 5). These do not sum, because Cox's aggregate and the DANFS ship-level figures are the known Tier 1 non-reconciliation flagged in the research. The script never invites the addition, never blends the two, and the FACT-CHECK LOG discloses it. This is exactly the required handling. No action needed.

---

## Issues to fix

All eight are in the production apparatus. **None is in the narration.** Nothing here changes a word the viewer hears; every one is a document that now contradicts the script it describes.

1. **R1. The ACCURACY NOTE and PRODUCTION NOTES still assert "Yamato ran ten MILES," in five places** (line 8 ACCURACY NOTE; line 610 Voice choices; line 620 Accuracy correction 4; line 621 Accuracy correction 5, whose entire heading is "Yamato ran ten MILES"; line 678 FACT-CHECK LOG). **Ruling, as requested: this is a blocker.** It is not spoken, but the ACCURACY NOTE is explicitly addressed to production, is headed "Do NOT re-simplify them back into the myth," and now instructs the builder that a claim the writer deliberately cut is the correct one. Correction 5 in particular reads as a standing instruction to keep "ten MILES" in. A note that contradicts the narration is precisely how a removed claim gets reinstated at build. - Fix: change all five to the sourced formulation, that the torpedoes chased Yamato out of her own battle and NHHC records the turn-away without a distance; keep the "not ten minutes" warning, which is still correct and still worth having.

2. **R2. Every count in PRODUCTION NOTES is stale.** Actual now: **1,497 narration words** (notes say 1,466), **129 VISUAL tags** (notes say 125), **115 unique stills** (notes say 111), runtime **9:59** at 150 wpm (notes say 9:46). The per-act split is wrong in all seven rows. This one has operational teeth: the BUILD NOTE's cost model tells the builder "125 tags minus 14 reuse = 111 unique stills to generate," so the build will be short four plates. - Fix: replace with 1,497 / 129 / 115, per-act split Cold Open 72/6, Act 1 173/15, Act 2 211/19, Act 3 337/30, Act 4 280/24, Act 5 367/31, Outro 57/4, and 11.6 words per still (4.6 seconds at 150 wpm).

3. **R3. Accuracy correction 1 still says "the six-word real message shown."** The script no longer claims a word count, and six was the wrong count anyway. - Fix: "the real one-line question shown."

4. **R4. FACT-CHECK LOG line 673 still reads "blows Kumano's bow off."** This re-asserts the exact overstatement the revision removed and misdescribes what the script now says. - Fix: "nearly 200 rounds, ten torpedoes, one hit on Kumano's bow, speed reduced to 12 knots."

5. **R5. FACT-CHECK LOG line 707 still reads "Suzuya destroyed by her own loaded torpedo mount after a near miss."** Re-asserts the contested trigger. - Fix: drop "after a near miss" and note the NHHC-versus-combinedfleet split on the trigger as the reason it is not stated on screen.

6. **R6. Voice choices line 612 lists "Removed. By a destroyer." as one of the script's punchy fragments.** That line no longer exists. - Fix: swap in a fragment that is actually in the script, e.g. "Done by a destroyer."

7. **R7. Accuracy correction 12 claims St. Lo's dead are "given as 'around one hundred and forty one'."** The script never states St. Lo's casualties at all. The note describes a beat that is not there. - Fix: rewrite to say St. Lo's dead are deliberately not stated, because the sources conflict at 141 / "more than 140" / 143, and because stating them next to the 1,785 figure would reintroduce the scope problem this revision just fixed.

8. **R8. The Act 5 range-ruler card still reads "7 MILES"** while the narration now correctly says seven nautical miles. Small, but it is the same unit ambiguity on screen that the narration just fixed in the VO. - Fix: card reads "7 NAUTICAL MILES."

Minor, not counted: the FACT-CHECK LOG row for Yamato's single surface action still cites navweaps alone; the claim as now worded is supported by the NHHC material already in the source list, so the citation can simply be upgraded.

---

## Tone check

**Human-cost beats straight: YES. Nothing to cut. The gate holds.**

- **Act 4** re-read in full: 24 tags, zero character voices, zero jokes, zero wordplay. Hoel and the 252, Gambier Bay capsizing, the burning and crushing, the scalded compartment, Carr, Evans on the fantail, Evans drifting away. All flat and factual.
- **The rewritten Carr passage specifically, re-read as instructed.** The attribution ("Survivors remembered...", "They remembered coming back...") is added without any change in register. It stays completely straight, and the hedge actually makes it land harder rather than softer, because it reads as testimony rather than narration. "He died of his wounds. He received the Silver Star, posthumously." is the right ending for the beat. No jokes anywhere near it. Approved.
- **Act 5 after the TONE: STRAIGHT marker** re-read in full: St. Lo, the four-ship card, the 1,785, the water, the overflying aircraft, the search error, the barracudas, the 635, the botched rescue. All straight. The new bookkeeping beat ("Four ships sank in the gun battle. St. Lo is not among them.") sits inside the straight section and is delivered flat, so it corrects the scope without breaking the tone. That was the right place to put it.
- Comedy before the markers still sits only on documented decisions and machinery, never on a death.

---

## Format check

- **All nine required sections present:** title line, header block, ACCURACY and VOICE notes, COLD OPEN with title card, five acts with timecodes, OUTRO with `[END]`, PRODUCTION NOTES, FACT-CHECK LOG, SOURCES.
- **Em-dashes: 0. En-dashes: 0.** Clean.
- **Camera moves inside VISUAL tags: 0.** No VISUAL tag implies motion; the only zoom/pan/dolly language is the BUILD NOTE prohibition.
- **VISUAL tag count: 129** (was 125). Reuse tags: 14. Unique stills: **115** (was 111).
- **Narration word count: 1,497** (was 1,466). Inside the 1,250 to 1,550 hard range.
- **Act timecodes still track after the edits.** Every act is within 5 seconds of its slot at 150 wpm: Cold Open -0.8, Act 1 +0.8, Act 2 +1.6, Act 3 -3.8, Act 4 +3.0, Act 5 -4.8, Outro +0.2. Total narration is now 9:59 against a final timecode of 9:55, so the cut runs about four seconds long. Within tolerance given the note's own "hold stills at 4 seconds rather than 5" fallback, but the stated runtime figure needs updating with the rest of R2.
- **No real-estate, Las Vegas, or realtor content.**

---

## Cold read notes

The revision did the work properly. It did not paper over the flags, it went back and re-cut the beats, and in four places (issues 2, 6, 7, 11) the fixed version is better television than what it replaced. Splitting Hoel's fourteen thousand yards from the more-than-forty hits gives two clean beats where there was one muddy one. "One hit Kumano's bow and set it alight. Her speed dropped to twelve knots. Done by a destroyer." is more specific, more accurate, and hits harder than "Removed. By a destroyer." ever did. And the casualty fix, "Four ships sank in the gun battle. St. Lo is not among them," turns a scope problem into one of the most characteristic moments in the episode: the script stopping to tell you exactly what a number does and does not cover. That is the show's whole thesis, performed rather than asserted.

The pass-1 pattern of the punchline running a half-step ahead of the source is gone. I looked for it specifically in the new text and did not find it. Every rewritten line now sits at or inside what the source will carry.

What is left is bookkeeping, and it is the predictable consequence of editing narration without walking the apparatus behind it. The FACT-CHECK LOG and PRODUCTION NOTES are now describing the previous draft. In an ordinary document that would be untidy. In this document it matters more than usual, for two concrete reasons. First, the ACCURACY NOTE is not commentary, it is an instruction to the build, and it currently instructs the build to hold a claim the writer removed on purpose. Second, the BUILD NOTE's still count is wrong by four, so following it produces an incomplete asset list.

There is no re-research required for any of it. Every fix is a find-and-replace against numbers I have recomputed above and wording already settled in the narration. This should be a short pass, and on its completion the episode is clear to ship.

---

## VERDICT: FAIL

---

## PASS 3 CLOSURE (Manager verification, not a QA agent pass)

The pass-2 report above was written against a mid-write copy of `script.md`. Re-checked against the final saved file, five of the eight listed residuals were already resolved by the writer's own metadata pass:

- **R1 "ten miles" residue** RESOLVED. The ACCURACY NOTE now reads "stated with no duration and no distance." Voice choices, Accuracy correction 4, Accuracy correction 5 and the FACT-CHECK LOG all carry the no-number formulation.
- **R2 stale counts** RESOLVED. PRODUCTION NOTES now read 1,497 narration words, 129 VISUAL tags, 14 reuse tags, 115 unique stills, runtime 9:59 at 150 wpm, with the per-act split recut. The BUILD NOTE cost model reads 129 minus 14 = 115.
- **R3 "six-word real message"** RESOLVED. Accuracy correction 1 now describes the complete dispatch shown with the real question isolated by greying the padding.
- **R4 "blows Kumano's bow off"** RESOLVED. FACT-CHECK LOG now logs the bow hit, the fire, and the drop to twelve knots, and records the correction.
- **R5 Suzuya "after a near miss"** RESOLVED. FACT-CHECK LOG now states the mount as the cause and explicitly notes no trigger is asserted.

The three genuinely outstanding items were applied by the Manager directly, all in the production apparatus, none touching narration:

- **R6** Punchy-fragment list in Voice choices cited "Removed. By a destroyer.", a line deleted in the revision. Replaced with the line that is actually in the script, "Done by a destroyer."
- **R7** Accuracy correction 12 claimed St. Lo's dead are given on screen as "around one hundred and forty one." The script never states a St. Lo casualty figure. Rewritten to record that the figure is deliberately omitted, because the sources conflict at 141, "more than 140," and 143, and because stating it beside the 1,785 would reintroduce the scope problem correction 14 exists to prevent. Carries an explicit instruction not to add one in the edit.
- **R8** The Act 5 range-ruler card read "7 MILES" against a VO that says seven nautical miles. Card now reads "7 NAUTICAL MILES."
- **Minor, also applied:** the FACT-CHECK LOG row for Yamato's single surface action cited navweaps alone. Upgraded to NHHC H-036 and H-084 for Samar plus NHHC H-044-3 for her April 1945 sortie, which is the Tier 1 anchor the pass-2 report identified as already in hand.

Re-verified on the final file: 0 em-dashes, 0 en-dashes, 129 VISUAL tags, 0 camera moves inside any tag, 7 TONE: STRAIGHT markers, all nine required sections present, no real-estate or Las Vegas content.

**All 11 pass-1 narration issues and all 8 pass-2 apparatus issues are resolved.** The pass-2 `VERDICT: FAIL` above refers to the pre-fix state and is retained for the record.

FINAL STATUS: CLEARED TO SHIP

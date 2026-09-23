# QA REPORT (FINAL): The Escape That Hid Inside a Gym Class
### Codename History, "The Wooden Horse" v2, Stalag Luft III East Compound, 8 July to 29 October 1943

**Status:** FINAL CONFIRMATION PASS. This file is the permanent QA record for the episode and is written to stand alone. It consolidates all three QA passes (two FAIL, one PASS) into a single self-contained document. Every count in it was recomputed from `script.md` on this pass, not carried forward.

**Scope of QA:** script body lines 1 to 613 for factual, tonal and format checks. Apparatus (production notes, BUILD BUDGET, FACT-CHECK LOG, sources) checked separately for internal consistency with the body.

---

## 1. Verdict summary

| Pass | Blocking issues found | Result |
|---|---|---|
| Pass 1 | 6 factual, 3 log/tier, 1 build-budget | FAIL |
| Pass 2 | 6 mechanical (stale log rows, stale note, 3 wrong table rows) | FAIL |
| Pass 3 (this pass) | 0 blocking | **PASS** |

All ten fixes from pass 1 and all seven fixes from pass 2 are confirmed present and correct. Nothing in the script body regressed. One cosmetic off-by-two remains in a non-load-bearing table row, documented in section 6 and explicitly not blocking.

---

## 2. Confirmation of the seven pass-2 fixes

| # | Required fix | Location | Verified |
|---|---|---|---|
| 1 | BUILD BUDGET `Total on-screen image slots` 142 to 140 | L650 | **YES.** Reads 140. Recomputed actual: 140 |
| 2 | BUILD BUDGET `[CARD: ...]` beats 19 to 18 | L651 | **YES.** Reads 18. Recomputed actual: 18 |
| 3 | BUILD BUDGET `[VISUAL: REUSE ...]` beats 38 to 37 | L653 | **YES.** Reads 37. Recomputed actual: 37, and the prose reuse list below the table independently sums to 37 |
| 4 | FACT-CHECK LOG "Codner sealed in at 1pm" to "that morning" | L692 | **YES.** Row now reads "Codner sealed in that morning". Agrees with body L406 |
| 5 | FACT-CHECK LOG "under five days after the breakout" to "six days" | L700 | **YES.** Row now reads "six days after the breakout". Agrees with body L518 and with the arithmetic in section 4 |
| 6 | Production note "Act 6 on Stockholm in five days" to "six days" | L621 | **YES.** Reads "Act 6 on Stockholm in six days" |
| 7 (optional) | Butterworth row flags the 1949 date as Tier 2 | L686 | **YES.** Row now ends "The 1949 date is Tier 2, TNA confirms the audition but does not date it." |

**Stale-string sweep, whole file.** Grepped for every superseded figure:

| Searched | Hits | Note |
|---|---|---|
| `five days` | **0** | Clean |
| `1pm`, `1 pm`, `one o'clock`, `13:00`, `one in the afternoon` | **0** | Clean |
| `142` | **0** | Clean |
| `38` | 3 | All three are IWM oral history catalogue number **9938** at L679, L699, L732. Not the REUSE figure. Clean |
| `19` as a standalone table value | **0** | Clean |

No superseded figure survives anywhere in the file.

---

## 3. Claim-by-claim factual verification (consolidated, all passes)

Tier 1 = primary record or museum catalogue. Tier 2 = participant memoir or contemporary press. Tier 3 = downstream retelling, not used as assertion.

### Camp and setting

| Claim as spoken | Tier | Verdict |
|---|---|---|
| Stalag Luft III, Sagan, **Lower** Silesia, about 100 miles from Berlin, Luftwaffe run, full of captured Allied airmen | 1 | **CONFIRMED.** IWM. Lower, not Upper. IWM's own American Archive page has this wrong and was not followed |
| Huts set far back from the wire | 1 | **CONFIRMED.** IWM, Stalag Luft III literature |
| Huts raised on stilts so guards can see underneath | 1 | **CONFIRMED.** Stated only as "raised". The 60 cm figure is Tier 2 and is correctly not spoken |
| Grey soil over bright yellow sand, so spoil betrays a dig | 1 | **CONFIRMED.** IWM, CWGC |
| Seismograph microphones buried in a perimeter ring | 1 | **CONFIRMED** as a camp defence only. See prohibited sweep, section 5 |
| Ferrets, a specialist anti-tunnel unit with metal probes | 1 | **CONFIRMED** |

### The three men

| Claim as spoken | Tier | Verdict |
|---|---|---|
| Michael Codner was a **Lieutenant**, Royal Artillery, not a Captain | 1 | **CONFIRMED, CORRECTS v1.** London Gazette 36486 p.1926; TNA WO 373/94/547; TNA WO 416/71/64; CWGC. He reached Captain later, after these events. The script's on-screen correction card is accurate |
| Codner was not an airman, he was a gunner | 1 | **CONFIRMED.** TNA WO 373/94/547 |
| Captured in Tunisia, December 1942, on the ground | 1 | **CONFIRMED.** TNA WO 373/94/547 |
| Mis-sorted by a German clerk into the Luftwaffe airmen's camp | 1 | **CONFIRMED.** IWM EPH 6366 label: an officer in the Royal Artillery who was mistaken for an Air Force prisoner |
| Codner and Flight Lieutenant Eric Williams devised the scheme, Trojan Horse inspiration | 1 | **CONFIRMED.** IWM EPH 6366; TNA WO 373/94/547; Telegraph obituary 6 May 1993. Script attributes to both men jointly, which is the safest reading |
| Every scheme had to be registered with the escape committee; they went to Oliver Philpot in June 1943; Philpot approved it then joined it | 2 | **CONFIRMED, memoir-sourced.** Philpot, *Stolen Journey*, p.240. The MC recommendation compresses this. Presented as plot, not as record, which is appropriate |
| All three awarded the Military Cross | 1 for Codner and Philpot, corroborated for Williams | **CONFIRMED.** London Gazette 36486 p.1926 and 36516 supplement p.2242. Williams' award line lacks a clean Tier 1 Award field but is corroborated by IWM's catalogue title "Flight Lieutenant E Williams MC" |

### The horse and the dig

| Claim as spoken | Tier | Verdict |
|---|---|---|
| Camp timber frame, Red Cross packing case plywood skin, padded top, white linen | 2 | **CONFIRMED.** Williams, *The Wooden Horse*, ch.3. Corrects v1's "made from Red Cross crates" |
| Four slots, four six foot poles, carried sedan chair style by four men | 2, corroborated | **CONFIRMED.** Williams ch.3; RAFA corroborates the four man carry |
| **No weight and no dimensions stated anywhere** | n/a | **CORRECT OMISSION.** Weight NOT FOUND, dimensions conflict across sources. Verified absent, section 5 |
| Weeks of genuine vaulting before any digging, to bore the guards | 2 | **CONFIRMED in substance.** Memoir-derived. Stated as observed behaviour, not as a quoted plan |
| German suspicion and a physical inspection of the horse | 1 in outline | **CONFIRMED.** IWM oral history 9938 Reel 5 topic list includes German suspicion of wooden horse. Inspection specifics are memoir-derived and correctly not detailed on screen |
| Digging began **8 July 1943**, escape **29 October 1943**, **114 days** | 1 | **CONFIRMED.** TNA WO 373/94/547 gives both dates; IWM EPH 6366 states 114 days of digging; Telegraph obituary agrees. Not "three months", not "four and a half months". Arithmetic verified in section 4 |
| Trapdoor under the horse, shaft lined with stolen Red Cross plywood | 2 | **CONFIRMED** |
| About thirty inches of sand between vaulters' boots and the digger | 2 | **CONFIRMED.** Philpot, *Stolen Journey*, p.262 |
| Dug with bowls, by candlelight; they did not dare cut air holes | 2 | **CONFIRMED, conservative reading chosen.** Sources conflict (dared not bore airholes vs metal rods to poke through). Script takes the more conservative statement |
| Sand in bags sewn from cut off trouser legs, carried back inside the horse | 2 | **CONFIRMED.** Williams |
| Shaft capped each evening, grey surface sand brushed over | 2 | **CONFIRMED** |
| Spoil dried in the canteen attic, then dispersed around the compound | 1 for the attic, named participant for dispersal | **CONFIRMED.** Williams via IWM record for the canteen attic; Mac Colquhoun RCAF, a named participant, for gardens and the theatre stage |
| Dig schedule redesigned because the vaulters were tiring | 2 | **CONFIRMED.** Philpot, *Stolen Journey*, p.255 |
| Deliberate knock-overs of the empty horse; leaving it unattended over the entrance | 2, contemporary | **CONFIRMED.** RAFA quoting a first-hand Air Mail 1949 article by men who were there. Documented goon-baiting used as an engineering control |
| Tunnel found about **30 degrees** off course by probing with a poker in October | 2 | **CONFIRMED.** Philpot, *Stolen Journey*, p.262 |
| "Goon" sold to the Germans as German Officer Or Non-Com, accepted by the guards | Widely attested, contemporary usage confirmed | **CONFIRMED.** b24.net; 1949 Air Mail first-hand account. A POW story about themselves, presented as such |
| Cave-in buried Codner, broke the surface in daylight, a vaulter fell across the hole faking a twisted ankle | 2/3 | **ATTRIBUTED, NOT ASSERTED.** Narration opens the beat with "the way Williams told it later". This is the correct handling and was a pass-1 requirement |

### Escape night and the runs

| Claim as spoken | Tier | Verdict |
|---|---|---|
| **Friday 29 October 1943** | 1 | **CONFIRMED.** TNA WO 373/94/547. Day of week independently verified, section 4 |
| October deadline set by stolen railway timetables running only to month end | 2 | **CONFIRMED in substance.** Consistent across accounts. Presented as a fact of the plan, not sourced to a document |
| **Codner sealed into the tunnel that morning**, stayed down all day, roll call faked | 1 for date, 2 for the hour | **CONFIRMED as now written.** The earlier "one o'clock" was unsourced and was removed in pass 1. "That morning" sits correctly against "He stayed down there all day" |
| Horse out that evening with Williams, Philpot, and a fourth man, McKay, who sealed them in | 2 | **CONFIRMED.** McKay's first name and unit NOT FOUND, so only the surname is used. Correct restraint |
| Diversion of trumpets, singing and banging in the huts nearest the wire | 2 | **CONFIRMED** |
| Broke through just after six | 2 | **CONFIRMED** |
| **Fifteen feet beyond the wire** | 1 | **CONFIRMED.** TNA WO 373/94/547. This is the load-bearing fact and correctly leads the beat |
| Twelve inches short, in the sentry's path, German night patrol running late | 2, single source | **ATTRIBUTED, NOT ASSERTED.** Telegraph obituary 6 May 1993 only, not corroborated elsewhere. All three items are spoken as "By Philpot's account" / "He said" / "He said". This was a pass-1 requirement and is the episode's most important hedge |
| Philpot looked up at a sentry facing away into the camp | 1 | **CONFIRMED.** Philpot's own recorded voice, TNA "Great Escapes" exhibition. Sequencing corrected in pass 1 to match the recording |
| Williams and Codner as French workmen via Frankfurt an der Oder, Kustrin, Stettin; hidden by a Danish sailor; reached Sweden | 1 | **CONFIRMED.** TNA WO 373/94/547. Script says "reached Sweden" without dating it, for pace. The record date (11 November) is in the log, not on screen. Acceptable |
| Philpot as Norwegian margarine salesman Jon Jorgensen; real prewar margarine executive at Unilever; spoke no Norwegian; chose Norwegian to reduce the odds of meeting one; built the identity before he had an escape | 1/2 | **CONFIRMED.** Telegraph obituary; *Stolen Journey*; Philpot's IS9 file |
| The pipe to excuse his accent, and the Hitler moustache | 2, single source | **ATTRIBUTED.** Telegraph obituary only. Narration hedges with "By his account". Correct |
| Fell asleep on his suitcase, fell off, swore in English, the carriage laughed, then passed a plainclothes check on a card carrying another officer's photograph | 2, multi-corroborated | **CONFIRMED.** Telegraph obituary; *Stolen Journey*; IWM oral history 9938 Reel 7 |
| Reached Stockholm **six days** after leaving camp | 1 | **CONFIRMED.** IWM, two separate pages: British Legation, Stockholm, 4 November 1943. Arithmetic verified in section 4. The earlier "five days" was wrong and is gone from body and log |

### The Butterworth thread

| Claim as spoken | Tier | Verdict |
|---|---|---|
| Peter Butterworth and Talbot Rothwell performed badly on stage so booing covered digging noise | 1 | **CONFIRMED.** TNA "Great Escapes" exhibition text; Kristen Alexander |
| Both became Carry On legends | 1 | **CONFIRMED** |
| Butterworth personally vaulted over the horse | 2 | **CONFIRMED at Tier 2.** Widely reported, consistent with TNA's account of his role, not in a Tier 1 record. Narration says only "also vaulted over the horse" |
| Butterworth auditioned for the 1950 film **in nineteen forty nine** and was rejected | Audition Tier 1, **year Tier 2** | **CONFIRMED with the year flagged.** TNA confirms the audition and rejection but does not date it. The 1949 year is Tier 2. Log row L686 now says so explicitly. Low risk: the film released in 1950, so a 1949 audition is chronologically sound |
| The producers said he did not look heroic or athletic enough | Reason not in the record | **ATTRIBUTED, NOT ASSERTED.** TNA records the rejection but no reason. Narration says "The producers said", not "he was". The Tier 3 "too heavy" version is correctly not used |

### The cost act

| Claim as spoken | Tier | Verdict |
|---|---|---|
| Germany held **170,000** British and Commonwealth prisoners | 1 | **CONFIRMED.** IWM. Wording verified to carry IWM's scope without importing a survival claim |
| **Fewer than 1,200** ever escaped and got home, under one percent | 1 | **CONFIRMED.** IWM. This is a successful-escape figure, not a survival figure. Pass-1 fix; the false survival reading is gone from both card and narration |
| Night of **24 to 25 March 1944**, North Compound | 1 | **CONFIRMED.** TNA; CWGC. Day of week verified, section 4 |
| **76** got clear | 1 | **CONFIRMED.** IWM's "80 climbed out, four caught at the mouth" is the same night counted differently. 76 is the number that got clear, which is what the script says |
| **73** recaptured | 1 | **CONFIRMED** |
| **50** murdered by the Gestapo, on Hitler's orders | 1 | **CONFIRMED.** TNA; CWGC. The word "murdered" is used, not a euphemism |
| Only three got home: **Per Bergsland, Jens Muller, Bram van der Stok** | 1 | **CONFIRMED.** TNA WO 208/3319/1866 and 1867; TNA WO 208/5273/5378 |
| **48 of the 50** lie in a cemetery in Poznan | 1 | **CONFIRMED.** CWGC, "all but two" |
| "That was the Great Escape. This story is not that story." | n/a | **CORRECT.** This is the central correction of the episode and it is stated explicitly |
| Film and book use fictional names, Peter Howard for Williams, John Clinton for Codner | 1 | **CONFIRMED.** Williams' own author's note, October 1963; Kristen Alexander |

**No claim in the script body is unsourced, and no Tier 2 or single-source claim is spoken as record.**

---

## 4. Math re-check

Computed independently on this pass from first principles, not taken from any source or from a prior report.

- **8 July 1943 to 29 October 1943.** July 8 to July 31 is 23 days, August 31, September 30, October 29. Elapsed 113 days, **114 inclusive**. The card "8 JULY 1943. DAY 1 OF 114" uses inclusive counting, which lands day 114 exactly on 29 October. **Correct.**
- **Day of week, 29 October 1943.** 1 January 1943 was a Friday. Day-of-year 302 in a non-leap year. (302 minus 1) mod 7 = 0, so **Friday**. Matches the card at L396. **Correct.**
- **29 October to 4 November 1943.** Two days remaining in October plus four in November = **6 days**. Cross-check by weekday: Friday plus six is Thursday, and 4 November 1943 was a Thursday. **Six is correct. The former "five days" was wrong and is now gone from the body (L518), the log (L700) and the production notes (L621).**
- **Day of week, 24 March 1944.** 1 January 1944 was a Saturday. Day-of-year 84 in a leap year. (84 minus 1) mod 7 = 6, so **Friday**. "The night of twenty four to twenty five March" spans Friday into Saturday. **Correct.**
- **76 minus 73 = 3.** Matches the three named home runs. **Correct.**
- **1,200 of 170,000 = 0.706 per cent.** "Under one percent" is correct, and it now describes successful escapes rather than survival. **Correct.**
- **48 of 50 at Poznan.** Consistent with CWGC's "all but two". **Correct.**
- **Reuse arithmetic.** The prose reuse list names 25 base images with 62 total uses, so 62 minus 25 = **37 re-cuts**. Matches the recomputed REUSE tag count of 37 and the corrected table row. **Internally consistent.**
- **Unique images.** 121 VISUAL tags minus 37 REUSE = **84** unique generated images. Matches the table. **Correct.**

**Every arithmetic claim in the file, body and apparatus alike, is now correct.** The one arithmetic error that survived pass 2 (the "under five days" log row) is resolved.

---

## 5. Prohibited-claims sweep

Script body, lines 1 to 613. The ACCURACY NOTE at L10 is excluded from hit counting because it is the prohibition itself.

| Prohibited item | Result |
|---|---|
| Codner called a Captain | **CLEAN.** "Lieutenant Michael Codner, Royal Artillery" at L122, and the deliberate on-screen correction "LIEUTENANT. NOT CAPTAIN." at L124 to L126. The only other occurrence of the word is inside that correction |
| Wooden Horse and Great Escape conflated | **CLEAN.** No Great Escape figure is applied to the Wooden Horse and no Wooden Horse figure to the Great Escape. The two events are separated structurally (own act, own tone, own card set) and then explicitly in words at L584 |
| Vaulting masked the seismograph microphones | **CLEAN.** Microphones appear at L96 and L98 only, as one of four camp defences. Zero masking language anywhere in the file. The script substitutes the sourced reason for the horse: the tunnel had to start out in the open near the wire. The theatre-booing beat at L336 to L342 is a separate, Tier 1 sourced claim and is not a substitute for the removed one |
| A weight or firm dimensions for the horse | **CLEAN.** Zero hits for pounds, kilograms, kilos, weighed, or a length. The only measurements on screen are the six foot poles and the thirty inches of sand, both sourced |
| The horse's fate, survived or destroyed | **CLEAN.** Zero hits for destroyed, survives, or museum. Never mentioned |
| Karl "Rubberneck" Griese | **CLEAN.** Zero occurrences in the entire file outside the NOT USED log row. He belongs to the 1944 period, not this dig |
| A German unwittingly helping the escapers | **CLEAN.** The sentry facing away and the late patrol are framed as luck, and both are attributed to Philpot rather than asserted |
| Anyone injured vaulting | **CLEAN.** The only injury in the episode is the deliberately faked ankle, and L378 says so out loud: "The only injury in this entire story was completely fictional." |
| A direct quotation attributed to Eric Williams or Michael Codner | **CLEAN.** No real quotation is used anywhere. L354 "the way Williams told it later" is attribution, not quotation. The seven character-voice lines are labelled invented comic dialogue and go only to an unnamed prisoner, an unnamed guard, and Philpot |
| Re-simplification of a corrected beat back into a myth | **CLEAN.** All ten pass-1 corrections hold, and the FACT-CHECK LOG now agrees with every one of them, which closes the mechanism by which a correction gets undone on a later pass |

---

## 6. Format check (exact counts, recomputed this pass)

Counted programmatically over the script body. The `**BUILD SPEC:**` header at L8 contains the literal strings `[VISUAL: REUSE ...]` and `[CARD: ...]` as documentation of the notation and was excluded from all tag counts, as were its camera-move words, which are the prohibition itself.

### Hard format rules

| Check | Required | Actual | Result |
|---|---|---|---|
| Em-dash, U+2014, whole file | 0 | **0** | **PASS** |
| En-dash U+2013 and horizontal bar U+2015, whole file | 0 | **0** each | **PASS** |
| Narration or dialogue beats over 12 words | 0 | **0** | **PASS.** Longest is exactly 12 words. Eight beats tie at 12 |
| Camera moves inside `[VISUAL:` or `[CARD:` tags | 0 | **0** | **PASS.** Swept for zoom, pan, push in, dolly, Ken Burns, drift, tilt, truck, crane, tracking shot, slow in, slow out. STILLS ONLY spec is honoured throughout |
| Brackets or stage directions inside spoken narration | 0 | **0** | **PASS.** The seven "(character voice)" markers sit in the speaker label, outside the spoken text. TTS-safe |
| Kling or any video clip called for | 0 | **0** | **PASS** |

### BUILD BUDGET table verified against the body

| Metric | Table says | Recomputed actual | Verdict |
|---|---|---|---|
| Total narration beats | 139 | **139** | **Correct** |
| Narration word count | 1,463 | **1,461** whitespace-split | Off by 2, cosmetic. See note below |
| `[VISUAL: ...]` beats, total | not stated | **121** | For reference |
| `[VISUAL: REUSE ...]` beats | 37 | **37** | **Correct.** Now matches the prose reuse list, which sums to 37 |
| `[CARD: ...]` beats | 18 | **18** | **Correct** |
| `[TITLE CARD: ...]` beats | 1 | **1** | **Correct** |
| Total on-screen image slots | 140 | **140** | **Correct.** 121 plus 18 plus 1 |
| **Unique generated images required** | **84** | **84** | **Correct.** 121 minus 37. This is the row that drives generation spend |
| Kling video clips required | 0 | **0** | **Correct** |
| VO takes required | 139 | **139** | **Correct** |
| Longest single narration beat | 12 words | **12** | **Correct** |
| Average narration beat | 10.5 words | **10.51** | **Correct** |

**Note on the word count, non-blocking.** The table's 1,463 is a punctuation-token count, which treats possessives such as "Philpot's" and "sentry's" as two tokens. The whitespace-split count, which is the one that matters for a 150 wpm runtime estimate, is **1,461**. The discrepancy is two words, or about **0.8 seconds** of runtime against a projected 10:05 to 10:25. It does not change the projected-runtime row, it does not reach the viewer, and it does not affect generation spend. Recorded here for completeness and explicitly **not treated as a defect**. If Ryan wants the file perfect, it is a one-character edit at L649.

The BUILD BUDGET table is otherwise fully reconciled with the script body for the first time across three passes.

---

## 7. Tone check

**The human-cost act is completely straight. PASS.**

The `TONE: STRAIGHT` marker at L552 carries the correct scope, "everything from the next beat to the end of this act", plus the full production-level strip: muted desaturated grade, slower cuts, no music stings, no comic timing, cuts still held to the five second ceiling.

Lines 554 to 584 were read again line by line on this pass. Eight narration beats, every one a flat declarative. No narrator personality, no second-person pull-in, no callback to any running gag, no irony, no undercutting. The word "murdered" is used rather than a euphemism. The fifty get their own card. The three survivors are named individually. The forty eight graves at Poznan get their own beat. The act ends on the myth correction rather than on a punchline.

**Seam check.** The last comic line before the marker is L550, "He was rejected for being unconvincing as himself", which closes the Butterworth bit completely and does not run over the seam. None of the seven pass-2 fixes touched the straight act at all. **Nothing comic touches the murders.**

**Comic register in the rest of the episode.** Deadpan and dry throughout, consistent with the VOICE NOTE. The three running gags (the suspicious box, the gym class nobody questioned, the number of days) all land and all pay off. The seven invented dialogue lines are clearly marked as character voice and none of them puts words in a real named participant's mouth except Philpot, whose two lines are transparently comic bits at the escape committee desk and could not be mistaken for record. Second-person pull-ins appear in the cold open and Act 4 as designed.

---

## 8. Cold read notes

- The episode's central editorial job, separating the Wooden Horse from the Great Escape in the audience's head, is done twice: structurally, by giving the Great Escape its own tonally isolated act, and then explicitly in words. That is the right amount of insistence for a topic this reliably confused.
- Fix 1 from pass 1 reads correctly on a cold listen: "Germany held a hundred and seventy thousand. Fewer than twelve hundred ever escaped and got home." A listener cannot mistake that for a survival figure. This was the single most dangerous error in v2 and it is fully closed.
- The twelve-inches cluster is the best-executed correction in the file. Leading on the Tier 1 "Fifteen feet beyond the wire" and then handing the twelve inches, the sentry's path and the late patrol to Philpot keeps the drama on the record and demotes the obituary detail without losing the beat. Three consecutive attributions ("By Philpot's account / He said / He said") are slightly repetitive on the ear, but that is the correct trade and should not be smoothed away in the VO.
- "That morning" against "He stayed down there all day" is a cleaner scene than the unsourced one o'clock ever was. The accuracy fix improved the writing.
- The FACT-CHECK LOG now agrees with the script it certifies on every corrected beat. This matters more than it looks: a log asserting "1pm" and "under five days" as Tier 1 confirmed, sitting one page below a script that says "that morning" and "six days", was exactly the mechanism by which a corrected beat gets re-simplified back into a myth on the next production pass. The script's own ACCURACY NOTE warns against that. It is closed.
- The BUILD BUDGET is now reconciled and the build agent can trust it. 84 unique images, 37 re-cuts, 19 locally rendered cards including the title card, zero video clips.
- Nothing in the script body changed between pass 2 and pass 3. All certified line references (L406, L438, L450, L494, L518, L542, L546, L550, L552, L584, L596) are intact at the same positions with the same text. No regression.

---

## 9. Residual caveats for production

These are not defects. They are things the build and VO should not accidentally undo.

1. **Do not strip the hedges.** Five beats are single-source and are deliberately spoken as attribution, not as fact: the twelve inches, the sentry's path, the late patrol (all Telegraph obituary 6 May 1993), the pipe and moustache (same obituary), and the cave-in with the faked ankle (Williams, memoir-derived). If a VO or edit pass tightens "By Philpot's account, twelve inches short" down to "twelve inches short", the episode loses its accuracy footing. Leave the hedges in.
2. **The 1949 audition year is Tier 2.** TNA confirms the audition and the rejection but does not date it. The year is chronologically sound against a 1950 release and is fine to keep, but do not promote it to a hard on-screen date card.
3. **The 114 days figure is Tier 1 and inclusive.** Day 1 is 8 July, day 114 is 29 October. Do not "correct" it to 113.
4. **Lower Silesia, not Upper.** IWM's own American Archive page has this wrong. If anyone checks the script against that page, the script is right.
5. **McKay stays surname-only.** First name and unit are NOT FOUND. Do not let an image prompt or a Short caption invent one.
6. **No weight, no dimensions, no fate for the horse.** All three are unsourced or conflicted. They are absent by design, and they are the most likely things to creep back in via a Shorts caption or a thumbnail.
7. **The straight act stays straight in the mix too.** No sting, no music swell, no comic timing on lines 554 to 584. The tonal isolation is a production instruction as much as a writing one.

---

## 10. Final verdict

All seven pass-2 fixes are present and correct. No superseded figure survives anywhere in the file. The BUILD BUDGET table reconciles with the body on every load-bearing row and with its own supporting reuse list. Every arithmetic claim in the file is correct. Every factual claim is sourced, and every Tier 2 or single-source claim is attributed rather than asserted. The prohibited-claims sweep is clean on all ten items. The human-cost act is completely straight. All hard format rules pass: zero em-dashes, zero beats over 12 words, zero camera moves, zero stage directions inside spoken lines, zero video clips.

The single residual, a two-word discrepancy in the narration word count row worth about 0.8 seconds of runtime, is cosmetic, does not reach the viewer, does not affect spend, and is recorded rather than blocking.

The episode is cleared for build.

VERDICT: PASS

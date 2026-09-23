# QA / FACT-CHECK REPORT — LOOP 2 (FINAL LOOP)
Episode: Vincigliata escape (Castello di Vincigliata, PG 12)
Script: script.md
Predecessor: qa-report.md (loop 1, VERDICT: FAIL, 9 blocking)
Loop 2 agent: Wave 3 QA. Appending as I go.

---

## SECTION 0. MECHANICAL CHECKS (run first)

### 0.1 Mandated script output (verbatim, run on the amended file)

```
SPOKEN: 1400 beats: 112 visuals: 112 REUSE: 9 em: 0 inlineTONE: 0
OVER14: []
REUSE problems: none
```

**All seven required values hit exactly.** SPOKEN 1400 (target band 1396-1404), beats 112, visuals 112, REUSE 9, em-dashes 0, inline TONE tags 0, OVER14 empty, REUSE problems none. The five word-neutral narration edits were genuinely word-neutral: the file is still at 1,400, unchanged from loop 1.

Runtime consequence: 1,400 words at 173 wpm (fast end) = 8:05.8, still above the 8:00 mid-roll floor. At 158 wpm = 8:51.6. At 151 wpm = 9:16.6, i.e. 4.97 s per image across 112 images, inside the 5-second ceiling. No runtime regression.

### 0.2 Structural checks

| Check | Result |
|---|---|
| All 9 required sections present and in order | **PASS.** Title/front matter, COLD OPEN, ACTS 1-11, OUTRO, PRODUCTION NOTES, FACT-CHECK LOG, SOURCES. Headings at lines 1, 14, 48, 92, 120, 156, 204, 236, 284, 312, 344, 388, 420, 494, 520, 561, 660. |
| Brackets or stage directions inside a NARRATOR line | **PASS, none.** `inlineTONE: 0` and a manual sweep of all 112 spoken lines finds no `[`, `]`, `(`, `)`, asterisk or markdown inside any spoken string. All numbers spelled out. No curly quotes. |
| Camera moves in any `[VISUAL:]` tag | **PASS, none.** Swept all 112 tags for pan, zoom, tilt, dolly, track, push, pull, crane, whip, Ken Burns, "camera", "slow", "drift", "reveal". Zero hits. Every tag is a static description. |
| Act timecodes continuous | **PASS.** 0:00-0:33, 0:33-1:22, 1:22-1:47, 1:47-2:28, 2:28-3:23, 3:23-3:56, 3:56-4:47, 4:47-5:17, 5:17-5:50, 5:50-6:39, 6:39-7:13, 7:13-8:27, 8:27-8:51. Every act begins on the previous act's end second, no gaps, no overlaps, terminating at 8:51 = the stated target runtime. |
| Title format | **PASS.** `The Generals Who Dug Out of a Castle With a Croquet Set \| Codename History`. Standard `[hook] \| Codename History` form. No `Codename:` convention forced onto an operation that has none. PRODUCTION NOTES states the reason explicitly. |

**Section 0 verdict: the mechanical gate is clean. Nothing in this section blocks.**

---

## SECTION 1. DID THE NINE BLOCKING FIXES LAND?

Checked each against the amended file, in context.

| # | Fix | Landed? | Regression? |
|---|---|---|---|
| B1 | `Two years a prisoner` -> `Sixteen months a prisoner` (Act 11) | **YES**, line 480 area: "Fifty-two. Member of parliament. Sixteen months a prisoner. He could have stopped." 12 words, unchanged | See 1.1, arithmetic redone |
| B2 | `changed trains at Como` -> `got off at Como` (Act 7) | **YES**: "Hargest and Miles got off at Como and took the road toward Chiasso." 13 words | See 1.2, true on both Tier 1 accounts |
| B3 | `Almost no guard against escape` -> `Nobody expected them to escape` (cold open) | **YES**, 12 words | **See 1.3. One real prose regression, non-blocking, fix supplied** |
| B4 | `A German sergeant` -> `A German soldier`, narration AND visual tag (Act 10) | **YES, both.** Narration 14 words; tag now reads "A German soldier pointing down a road..." | See 1.4, one stale log row |
| B5 | `Never less than eighteen inches wide` -> `By Boyd's measure, eighteen inches wide` (Act 4) | **YES**, 12 words | See 1.5, one prose echo, non-blocking |
| B6 | "fourteen other ranks" log row rewritten off the false TNA claim | **YES**, verbatim | **Row's Beat column is now stale against S3. See 3.2** |
| B7 | Beda Fomm row and wire row relabelled off `TIER 2 HEDGED` | **YES.** Beda Fomm now `TIER 1`; wire now `TIER 1 PRIMARY` | Clean |
| B8 | TNA SOURCES bullet states the redirect and the archival route | **YES**, verbatim, no bare link | Clean |
| B9 | Gallery-width row no longer demotes the Gazette | **YES.** Row now reads `PRIMARY, ATTRIBUTED ON CAMERA, CONFLICT NAMED` and calls the Gazette "Tier 1, not Tier 2" | Clean |

Plus the two accepted non-blocking suggestions:

| # | Fix | Landed? |
|---|---|---|
| S1 | `one hand` -> `one arm` (Act 6) | **YES**, 14 words. **But it orphaned a FACT-CHECK LOG row. See 3.1** |
| S3 | `Fourteen other ranks left with the officers.` -> `By Neame's count, fourteen other ranks left.` (Act 11) | **YES**, 7 words -> 7 words. **Link to the officers survives. See 1.6** |

Plus the seven understating-row rewrites and the three new SOURCES bullets: all present, all checked in Section 3.

**All nine blocking fixes landed. None of them was mis-transcribed. The spoken word count is unchanged.**

---

## SECTION 2. THE BIG NEWS THIS LOOP: I OPENED MASON

Loop 1 could not open W. Wynne Mason, *Prisoners of War* (Official History of New Zealand in the Second World War, 1954). Its note 4.8 says NZETC is behind an Incapsula wall and the Wayback set covers "chapters 2, 4, 6, 7 and 11 only, none of which carries the Vincigliata narrative", so it left the Mason-dependent claims as **TIER 1 CARRIED** from Wave 1.

**That assessment was wrong on both halves, and I have now read the entire book.**

Route, for the record and for the SOURCES block: `nzetc.victoria.ac.nz` 301s to a National Library of New Zealand web-archive viewer that returns no text to a fetcher. But the NZETC chapter pages expose the **complete TEI-XML source of the whole book** at `nzetc.victoria.ac.nz/tei-source/WH2Pris.xml`, and the Internet Archive holds it. I pulled it with the `id_` raw-content modifier:

```
http://web.archive.org/web/20161011095643id_/http://nzetc.victoria.ac.nz/tei-source/WH2Pris.xml
```

2,198,406 bytes, 263,667 words, the full text including every biographical footnote and the index. Chapter 6, "Turning Point of the War in Europe and in North Africa (June 1942 - July 1943)", **does** carry the Vincigliata narrative, at pp. 118-19 and 213.

**Every Mason-dependent claim in the episode is now Tier 1 OPENED rather than Tier 1 CARRIED.** The relevant passage, verbatim:

> "In March 1943 the 'Generals' camp' at Villa Vincigliata - Campo PG 12 - was the scene of one of the most notable escapes of the war. ... There had been several unsuccessful attempts to escape from the villa by one or two of the officers in the spring and summer of 1942. Finally in September entry was gained to a disused and sealed-up chapel, from which a tunnel leading into the outer garden was begun. All the officers and other ranks in the camp assisted in some way in the tunnelling and other preparations for this attempt. On a wet evening - 29 March 1943 - the six men went out through the completed tunnel, and by 9.30 p.m. four were on their way to the railway station to catch a **night train** to Milan, and the two generals had set off to walk to the Swiss border. The latter and two of the others had the misfortune to be recaptured; but the two New Zealand brigadiers travelled by train to Como, and at half past ten on the evening following the break-out they crawled through the frontier wire near Chiasso into Switzerland. Later in the year, separately and each with the assistance of the French Resistance Movement, they reached the borders of Spain. Brigadier Hargest was able to make his way to the British consulate in Barcelona and was **flown to England in December**. Brigadier Miles **lost his life in Spain in this last stage of a game attempt to reach Allied territory**."

Mason's footnote on the camp's strength, attached to "Generals' camp":

> "There were at this stage in the camp one lieutenant-general, three major-generals, one air vice-marshal, eight brigadiers, two junior officers, and **14 other ranks**."

Mason's footnote on the escape statistic:

> "Of the **1500 attempts** at escape from Italy before the armistice known to British Military Intelligence only three (including these two) are on their records as having got clear of Italy."

Mason's biographical footnotes, verbatim:

> "Brig J. Hargest, CBE, DSO and bar, MC, m.i.d.; Member of Parliament for Invercargill 1931-35, **Awarua 1935-44**; born Gore, **4 Sep 1891**; farmer; ... comd 5 NZ Inf Bde May 1940-Nov 1941; **p.w. 27 Nov 1941**; escaped Mar 1943; **killed in action, France, 12 Aug 1944**."

> "Brig R. Miles, CBE, DSO and bar, MC, ED, m.i.d.; born Springston, **10 Dec 1892**; Regular soldier; NZ Fd Arty 1914-19; **CRA 2 NZ Div 1940-41**; comd 2 NZEF (UK) 1940; wounded and p.w. 1 Dec 1941; **died, Spain, 20 Oct 1943**."

And Mason on the camp itself, pp. 118-19:

> "Campo PG 12, a castle-like villa at Vincigliata on a hill above Florence, housed all the captured British generals and brigadiers ... in quarters suitable to their rank. **A close watch was kept on their activities in order to prevent the escape of such valuable prisoners.** But they were allowed to keep **hens, rabbits, and a vegetable garden**, to indulge in hobbies, to have **books** and gramophone records, and to take daily walks **under strong guard** in the surrounding countryside."

### 2.1 What Mason CONFIRMS (nine upgrades, all in the safe direction)

| Script line | Mason, verbatim | Effect |
|---|---|---|
| "Sixteen months a prisoner." | "p.w. **27 Nov 1941**" + "escaped Mar 1943" | **Loop 1's blocking-1 fix confirmed at the source.** Arithmetic redone below. |
| "New Zealand's official history says only that he lost his life." | "lost his life in Spain in this last stage of a game attempt to reach Allied territory", and the footnote gives only "died, Spain, 20 Oct 1943", **no cause** | **The word "only" is now verified.** Mason genuinely gives no cause of death. Loop 1's biggest carried item closes. **TIER 1 CARRIED -> TIER 1 OPENED.** |
| "Through occupied France, then Spain, that December." | "each with the assistance of the **French Resistance Movement**, they reached the borders of Spain. Brigadier Hargest ... was **flown to England in December**." | **Confirms all three clauses and resolves loop 1's note 4.10.** The unopened CWGC "November" is now outweighed 3 to 1 (Mason explicit, DNZB "late in 1943", script "that December"). |
| "Fifty-two." (Hargest) | b. 4 Sep 1891, d. 12 Aug 1944 = 52 | Confirmed, third independent line |
| "The twelfth of August, nineteen forty-four." | "killed in action, France, **12 Aug 1944**" | Confirmed, third independent line |
| "Member of parliament" (spoken twice) | "Member of Parliament for Invercargill 1931-35, **Awarua 1935-44**" | Confirmed. Awarua to 1944 = to his death. Third independent line. |
| "Brigadier Reginald Miles, who commanded the New Zealand Division's guns." | "**CRA 2 NZ Div** 1940-41" | Confirmed, third independent line |
| "A chicken run. A vegetable garden. A library." | "allowed to keep **hens**, rabbits, and a **vegetable garden** ... to have **books**" | **Upgraded.** Was Parri alone; now two Tier 1 lines. Mason also gives rabbits, which the script correctly does not add. |
| "Todhunter and Stirling dug and stayed behind." | "**All the officers and other ranks in the camp assisted in some way** in the tunnelling" | Confirmed. Third line beside the Gazette and TNA. |
| "The next night, they were out." | "at **half past ten on the evening following the break-out** they crawled through the frontier wire near Chiasso" | **"The next night" is now verbatim-supported.** Best possible handling of the 29/30 March conflict, vindicated. |
| "Six men went out in three pairs." | "the six men went out ... four were on their way to the railway station ... and the two generals had set off to walk" | Confirmed |
| "Military Intelligence knew of three men who got clear of Italy before the armistice." | "only **three** (including these two) are on their records as having got clear of Italy" | **Upgraded from "Mason p. 213 as cited" to Mason opened, verbatim.** |
| "Fourteen other ranks" | "and **14 other ranks**" in the camp at that stage | **Upgraded. See 3.2. The log currently calls this Tier 2 and single-sourced. It is neither.** |

### 2.2 What Mason COSTS the episode (one blocking item, one documentation item)

| Script line | Mason, verbatim | Effect |
|---|---|---|
| "on the **early train**" (Act 5) | "by 9.30 p.m. four were on their way to the railway station to catch a **night train** to Milan" | **BLOCKING. See 4.1.** |
| "**Twenty-five** prisoners." (cold open) | "one lieutenant-general, three major-generals, one air vice-marshal, eight brigadiers, two junior officers, and 14 other ranks" = **15 officers and 14 other ranks, 29 people**, at March 1943 | Documentation. **See 5.5.** Not blocking, because the cold open is set in 1942 and Parri's Tier 1 range is 21 to 30, which holds both figures. But the log must stop presenting 25 as clean. |

### 2.3 A forbidden item is no longer unverified

The commission forbade the "roughly 1,500 escape attempts" denominator as unverified, and the script correctly does not speak it. **It is Mason's own footnote, Tier 1 official history**, verbatim above. The script should still not speak it, because the commission said so and because a denominator invites a percentage the episode does not need. But the FACT-CHECK LOG row that calls it "unverified" is now making a false statement about a source, which is the defect class this batch keeps failing. Replacement row at 5.7.

---

## SECTION 3. THE SPECIFIC RE-CHECKS THE MANAGER ASKED FOR

### 3.1 `Sixteen months a prisoner` - arithmetic redone from scratch

Capture **27 November 1941** (Mason's footnote "p.w. 27 Nov 1941", opened by me this pass; DNZB agrees). Break-out **29 March 1943**.

- 27 Nov 1941 to 27 Nov 1942 = **12 months**
- 27 Nov 1942 to 27 Mar 1943 = **4 months**
- 27 Mar 1943 to 29 Mar 1943 = **2 days**

**Total: 16 months and 2 days. "Sixteen months" is correct and is the nearest whole month, rounding down.** Loop 1's fix stands. The old "two years" overstated by eight months.

Cross-check for internal contradiction: the cold open says the castle was a prison "in nineteen forty-two", and Mason says Hargest and Miles "were kept in a villa near Sulmona until transferred to Campo PG 12 in the spring of 1942". So Hargest was a prisoner for sixteen months but at Vincigliata for about twelve. **The script says "Sixteen months a prisoner", not sixteen months in the castle. No contradiction.** Good line as written.

### 3.2 `got off at Como` - true on both Tier 1 accounts?

**YES, verified against both, and I re-read both this pass.**

- **NZ Gazette DSO citation, 21 Sep 1944 (Tier 1, primary):** "caught a train to Milan where they went to the North station. They caught a train to **Como and walked towards Chiasso**." They got off at Como. TRUE.
- **TNA blog (Tier 1), which I re-fetched verbatim this pass:** "Meanwhile Hargest and Miles successfully **changed trains at Como** and then took the road towards the border near Chiasso." Changing trains at Como necessarily means getting off at Como. TRUE.
- **Mason (Tier 1, newly opened):** "the two New Zealand brigadiers travelled by train to **Como**". Consistent with both. TRUE.

**"Got off at Como" is true on all three Tier 1 accounts and asserts nothing any of them denies.** Loop 1's blocking-2 fix is the correct one and it is now three-for-three rather than two-for-two. No regression.

### 3.3 `By Boyd's measure, eighteen inches wide` - voice and sufficiency

**Reads naturally: YES.** Act 4 opens on "Boyd wrote the tool list himself", so Boyd is already established as the act's documentary voice four beats earlier. "By Boyd's measure" lands as continuous with that, not as a new hedge appearing from nowhere. The act's register is already "here is the paperwork and it is absurd", so naming the paperwork is in-voice.

**Discharges the conflict: YES.** The Gazette says "a 3 foot by 3 foot tunnel". Boyd's notes say "never less than 3 1/2 feet by 1 1/2 feet". With the attribution in place the script no longer asserts a width as fact; it reports whose measurement it is, and the viewer is told. That is the same device the script already uses for Neame's garrison figure. **Sufficient. Ships.**

One prose observation, non-blocking, at 6.3: the preceding beat contains "Neame **measured** the distance outside", so "**measure**" now appears in two consecutive beats. Optional alternative supplied there.

### 3.4 S3 - did `By Neame's count, fourteen other ranks left` lose the link to the officers?

The original read "Fourteen other ranks left **with the officers**." The new line drops "with the officers". The manager is right that the following beats turn on the officers getting away and the other ranks being taken, so this needed checking.

**The link survives, and it survives inside the same act.** The run reads:

1. "By Neame's count, fourteen other ranks left. Sergeant Bain wired the tunnel."
2. "The Germans found them in the hills. **The officers were higher up.**"
3. "They got away. The NCOs and the other ranks were taken."

**Beat 2 does the work the dropped words used to do, and does it better.** "The officers were higher up" can only mean the officers were in the same hills at the same time, which establishes that both groups left together, and it establishes the physical separation that makes beat 3's outcome land. Beat 3's "They got away" then has an unambiguous antecedent in "The officers".

Upstream, Act 10 beat 1 already says "the prisoners changed into civilian clothes and simply left", so "left" in the Act 11 beat has a clear referent one act earlier.

**Not a regression. No replacement wording required.** If anything the new line is stronger, because it converts the episode's one remaining bare Tier 2 number into an attributed one without spending a word (7 words to 7 words).

**Orphaned-pronoun check on this run: clean.** "them" in beat 2 = the fourteen other ranks. "The officers" is named explicitly rather than pronominalised. "They" in beat 3 = the officers, named in the immediately preceding clause. No dangling referent.

### 3.5 S1 - did `one arm` create any new conflict?

**No. It removed one.** Checked every other mention of Carton de Wiart's injuries in the file:

| Location | Text | Consistent with "one arm"? |
|---|---|---|
| ACT 5 visual tag | "one with an eye patch and **an empty sleeve**" | YES. An empty sleeve is an arm, not a hand. This tag was already inconsistent with the old "one hand" line. |
| ACT 6 visual tag (scene 53) | "black eye patch, **empty pinned sleeve**, heavily scarred face" | YES. Same. Was inconsistent before S1. |
| ACT 9 narration | "He had lost an eye and **an arm**." | YES, now matches |
| ACT 9 visual tag (REUSE of scene 53) | byte-identical to the above | YES |
| ACT 9 narration | "the **eye patch** read as a prisoner exchange" | Neutral |
| FACT-CHECK LOG row | "Carton de Wiart 62, one eye, **one hand**, no Italian" | **NO. Stale. See 5.1.** |
| SOURCES / PRODUCTION NOTES | no mention of hand or arm | Neutral |

**S1 fixed a pre-existing narration-versus-visual mismatch that loop 1 recorded as note 4.4 but did not connect to the tags.** Before S1, two visual tags depicted an empty sleeve while the narration said "one hand". Now all five references agree, and the spoken word matches Garland and Smyth's Tier 1 "he had lost an eye and an arm". **Net accuracy improvement.**

The one casualty is the FACT-CHECK LOG row, which still says "one hand" and still cites the TNA phrasing. That is the single piece of collateral damage S1 caused and it is documentation only. Replacement row at 5.1.

**Ensemble check on S1: no drift.** The line is "Carton de Wiart was sixty-two, one eye, one arm, and no Italian. Blending in." The joke's target is the plan, not the man, and the beat exists to explain his **recapture**, which is the opposite of the indestructibility framing. Two beats later the script says out loud "Not indestructible. Just extremely recognisable." over greyed-out competitor thumbnails. **"One arm" is if anything a heavier injury than "one hand" and therefore pushes further from the unkillable lane, not toward it.** The commission is still obeyed.

---

## SECTION 4. BLOCKING FINDINGS (2). BOTH ARE PASTE-IN FIXES.

### 4.1 BLOCKING. `on the early train` is contradicted by the official history, from the same research sentence that produced loop 1's blocking 2

**Where:** ACT 5, the sixth beat.

**What is wrong.** Three Tier 1 sources touch the train and they do not agree:

| Source | Verbatim | Tier |
|---|---|---|
| TNA blog | "New Zealand Brigadiers Hargest and Miles, dressed as workmen, travelled by **the early train** from Florence station to Milan." | Tier 1, secondary summary |
| **Mason, official history (opened this pass)** | "by 9.30 p.m. four were on their way to the railway station to catch a **night train** to Milan" | Tier 1, official history, and it is the only source that gives a clock time |
| NZ Gazette DSO citation | "dressed as workmen and having **walked to Florence station**, caught a train to Milan" | Tier 1, primary. Silent on the time. |

The break-out was at 2100 (Gazette). Mason has them walking to the station by 2130. Vincigliata to Florence station is about five miles on foot, so they reached the platform late that night. **Mason's "night train" is mechanically consistent with the break-out time; TNA's "early train" is not**, unless "early" means the small hours, which is not how a viewer will hear it.

**This is the same defect class as loop 1's blocking 2, and it comes from the same sentence.** The research report's own summary line 586 reads: "Hargest and Miles went **dressed as workmen on the early train** from Florence to Milan, **changed trains at Como** ...". Loop 1 already proved the second half of that sentence wrong against the Gazette. The first half is the untested half, and it fails against Mason. The research report also carries Mason's "night train" verbatim at its own line 31, so **the report contradicts itself and the writer took the wrong branch, twice, from one sentence.**

**TNA's reliability in this exact passage is now measurable and poor.** Six items in the Vincigliata narrative where TNA stands alone against better sources: the break-out date ("30 March", 3 to 1 against), the Swiss surrender ("1 April", against Mason and the Gazette), Boyd's rank ("Air Marshall", he was an Air Vice Marshal), the Milan prison ("San Vittorio", it is San Vittore), the change of trains ("at Como", the Gazette says Milan), and now the train ("early", Mason says night). The script already silently declines to reproduce the first four. It should decline the sixth on the same reasoning.

**The fix removes the conflict rather than picking a side, exactly as loop 1's blocking 2 did.**

- **OLD (14 spoken words):** `Hargest and Miles went as workmen on the early train. Boyd and Combe too.`
- **NEW (14 spoken words):** `Hargest and Miles walked to Florence station dressed as workmen. Boyd and Combe too.`

Net change **0**. Word-for-word check: Hargest(1) and(2) Miles(3) walked(4) to(5) Florence(6) station(7) dressed(8) as(9) workmen(10) Boyd(11) and(12) Combe(13) too(14). At the 14-word ceiling, not over it.

**Why this wording.** Every clause is verbatim-supported by more than one Tier 1 source and contradicted by none:
- "walked to Florence station" - Gazette verbatim ("having walked to Florence station"), Mason ("on their way to the railway station").
- "dressed as workmen" - Gazette verbatim, TNA verbatim.
- "Boyd and Combe too" - TNA ("Also travelling by train were Boyd and Combe"), Mason ("four were on their way to the railway station").

It also **gains** something: the five-mile night walk to the station in the rain is a better image than a train time, and it sets up the "dark railway platform" already in the visual tag.

**The `[VISUAL:]` tag needs no change.** It reads "Hargest and Miles in rough workmen's jackets and flat caps standing on a dark railway platform." A dark platform fits Mason's night train and fits the new line. It was already the wrong picture for an early-morning train, so this fix removes a picture-versus-word mismatch as well.

**Alternative if the manager wants to keep the train in the sentence** (also 14 words, also conflict-free): `Hargest and Miles went as workmen on a train north. Boyd and Combe too.` I prefer the Florence-station version because both its factual clauses are verbatim quotations.

---

### 4.2 BLOCKING. Loop 1's blocking-3 fix removed the "no guard" claim from the narration and left it in the picture

**Where:** COLD OPEN, the third `[VISUAL:]` tag (scene 3).

**Current tag:** `**[VISUAL: Two bored Italian sentries leaning on their rifles at an iron gate, facing outward, away from the castle.]**`

**What is wrong.** Loop 1 blocked "Almost no guard against escape" because the NZ Gazette says "This camp was **extremely well guarded**" and because the commission forbade any pre-escape guard characterisation. **The tag asserts the identical claim in pictures**: bored, slouching, facing the wrong way. It is on screen for roughly four and a half seconds at the top of the episode, and it now has a second Tier 1 source against it, which loop 1 could not read:

- **NZ Gazette (Tier 1 primary):** "This camp was extremely well guarded".
- **Mason (Tier 1 official history, opened this pass):** "**A close watch was kept on their activities in order to prevent the escape of such valuable prisoners**" and the prisoners took daily walks "**under strong guard**".

Two Tier 1 sources say the guard was close and strong. The picture says the guards were bored and looking the other way. **This is the exact claim the gate blocked in loop 1, relocated from the audio to the video.** Fixing the narration and leaving the picture is not a fix.

**It also costs nothing.** Scene 3 is not in the REUSE set (the reused scenes are 4, 5, 6, 7, 9, 12, 13, 39 and 53), so this is a prompt edit on a generation that is already budgeted. No word count effect, no image budget effect, still 112 tags and 103 unique generations.

**Replacement tag, paste over the existing one:**

```
**[VISUAL: Two alert Italian sentries with rifles at an iron gate, one watching the courtyard, the other watching the wall.]**
```

This still reads as "guards at a gate" for the beat, still contrasts with the escape, and now agrees with both Tier 1 sources. **It also improves the hook**: "well guarded, and they still went out through the floor" is a stronger cold open than "nobody was watching".

**Related, and free:** the tag one beat earlier reads `**[VISUAL: Twenty-five British and Commonwealth officers standing in a stone courtyard in worn uniforms and shorts.]**`. Mason enumerates the camp as **15 officers and 14 other ranks**. There were never twenty-five officers at Vincigliata. Scene 2 is also not reused, so this is free to correct:

```
**[VISUAL: About twenty-five British and Commonwealth prisoners standing in a stone courtyard in worn uniforms and shorts.]**
```

I am folding this into 4.2 rather than raising it separately because it is the same free prompt-level pass. **Blocking status: the sentry tag blocks; the "twenty-five officers" tag is a strong recommendation** (nobody counts figures in a crowd shot, but the prompt should not instruct the model to draw a fact that is wrong).

---

## SECTION 5. FACT-CHECK LOG AND SOURCES AUDIT

I re-audited **every** row against what the cited source actually contains, including the rows the manager pasted this cycle, and including the rows loop 1 did not touch.

**The manager's nine pastes are all correct.** Blocking 6, 7, 8 and 9 landed verbatim, the seven understating rows now state the right tier, and the three new SOURCES bullets are honest about what they support. I found **no new overstatement introduced by the manager's edits**.

What I did find is **eleven rows that are now stale, wrong, or newly upgradeable** because of (a) the narration edits applied this cycle, and (b) Mason being opened. Every one below is documentation only. **None of them blocks shipping on its own**, but rows 5.1, 5.2, 5.3 and 5.4 describe lines that no longer exist in the script, which is the condition that let the previous three episodes ship defective logs, so I am treating the whole set as **required paste-ins**.

Line numbers are for the file as it stands now.

### 5.1 REQUIRED. Line 601. Stale after S1, and cites the wrong source

The row still describes "one hand" and the script now says "one arm".

**Paste over line 601:**

```
| Carton de Wiart 62, one eye, one arm, no Italian | **TIER 1 FOR THE MAIMING**, arithmetic checks | Born 5 May 1880, escape March 1943, so 62. **"An arm" follows Garland and Smyth, *Sicily and the Surrender of Italy*, ch. 23, verbatim: "he had lost an eye and an arm in the service of his country."** The TNA blog uses the looser "an eye patch and a missing hand"; the script follows the US Army official history because it is the more specific of the two Tier 1 phrasings and because it matches Act 9 and the empty-sleeve visual tags. Changed from "one hand" in the loop 1 pass to remove an internal inconsistency. "No Italian" is characterisation, not a sourced claim, and carries no number. |
```

### 5.2 REQUIRED. Line 623. Beat column stale after S3, and the figure is no longer Tier 2

Two problems. The Beat column quotes narration that no longer exists ("left with the officers"), and **Mason independently gives 14 other ranks in the camp**, so the row's "Tier 2 and single-sourced" is now understating in the same way the seven rows the manager just rewrote were.

**Paste over line 623:**

```
| **By Neame's count, fourteen other ranks left; Sergeant Bain wired the tunnel** | **BAIN PRIMARY; FOURTEEN TIER 1 FOR THE NUMBER, TIER 2 FOR THE DEPARTURE, ATTRIBUTED ON CAMERA**, STRAIGHT | Bain and the wiring from Boyd's notes, primary. **Mason, *Prisoners of War*, ch. 6, footnote to the "Generals' camp" passage, enumerates the camp at March 1943 as "one lieutenant-general, three major-generals, one air vice-marshal, eight brigadiers, two junior officers, and 14 other ranks", so the figure of fourteen other ranks is Tier 1 official history, not the single Tier 2 line previously recorded.** That all fourteen left with the officers in September 1943 is Neame, *Playing With Strife*, p. 314, via Wikipedia "Vincigliata", Tier 2, which is why the narration now attributes it out loud as "By Neame's count". **TNA does not carry the other ranks anywhere and must not be cited for them.** CQMS Morgan led them out. Neame separately says "thirteen NCOs and men" did the watching during the escape itself, which is a different count of a different thing and not a conflict. |
```

### 5.3 REQUIRED. Line 596. Must change with the blocking fix at 4.1

**Paste over line 596:**

```
| Hargest and Miles walked to Florence station dressed as workmen; Boyd and Combe also went by train | **TIER 1, THREE INDEPENDENT LINES; TRAIN TIME DELIBERATELY NOT SPOKEN, CONFLICT NAMED** | NZ Gazette DSO citation, verbatim: "dressed as workmen and having walked to Florence station, caught a train to Milan". TNA blog: "dressed as workmen, travelled by the early train from Florence station to Milan ... Also travelling by train were Boyd and Combe." Mason, ch. 6: "by 9.30 p.m. four were on their way to the railway station to catch a night train to Milan". **TNA says "early train" and Mason says "night train", an unresolved Tier 1 conflict, and Mason is the only source that gives a clock time and is the one consistent with the 2100 break-out. The script therefore speaks no train time at all. Do not restore "the early train".** |
```

### 5.4 REQUIRED. Line 605. Cites only TNA for a beat that exists because TNA is wrong

The row is the reason blocking 2 happened and it still records none of it.

**Paste over line 605:**

```
| Como, the road toward Chiasso, cutting across country | **TIER 1, CONFLICT NAMED, RESOLVED IN THE WORDING** | NZ Gazette DSO citation, verbatim: "They caught a train to Como and walked towards Chiasso. 2 kilometres from Chiasso they left the main road and proceeded across country". Mason, ch. 6: "the two New Zealand brigadiers travelled by train to Como". **The TNA blog says they "changed trains at Como"; the Gazette says the change of trains was at Milan, Centrale to Nord, and that at Como they left the train and walked. The script says "got off at Como", which is true on all three accounts and asserts nothing any of them denies. Do not restore "changed trains at Como".** |
```

### 5.5 REQUIRED. Line 568. S5 item one, plus Mason's enumeration

This is the manager's requested S5 row for the Italian-usage caveat (loop 1 note 4.1). **I have added Mason's enumeration to it**, which loop 1 did not have. Mason counts 29 people in the camp at March 1943, not 25, and the script speaks 25.

The spoken line is **not blocking**, for three reasons. The cold open is set in "nineteen forty-two", not at the break-out. Parri, Tier 1, gives the camp's actual population as 21 to 30, which holds both 25 and 29. And 25 is itself a sourced number: Neame's post-escape 11 officers plus 14 other ranks. But the log must stop presenting it as clean, and a future build agent must not "correct" either number into the other.

**Paste over line 568:**

```
| About 25 men, roughly a dozen generals | **TIER 1, RANGE SOURCE, SECOND TIER 1 SOURCE COUNTS DIFFERENTLY** | Parri sheet: ceiling 36, actual 21 to 30, about 12 generals. Script says "twenty-five" and "a dozen", both inside that Tier 1 range. **Mason, ch. 6, enumerates the camp at March 1943 as "one lieutenant-general, three major-generals, one air vice-marshal, eight brigadiers, two junior officers, and 14 other ranks", which is 15 officers and 14 other ranks, 29 people. That is also inside Parri's range. The script's twenty-five matches Neame's post-escape figure of 11 officers plus 14 other ranks, spoken again and attributed in Act 8; the cold open is set in 1942 rather than at the break-out, so the two are not in contradiction.** **Italian-usage caveat: the Parri sheet is Italian and Italian convention counts a brigadier as a general officer (*generale di brigata*); British usage does not. Mason's enumeration gives 5 general officers plus 8 brigadiers, which is 13 on Italian usage and 5 on British. "A dozen" is correct on the Italian count and on Parri's own figure. The script never calls any named brigadier a general, so no individual claim is wrong. Do not "correct" twenty-five to twenty-nine, or a dozen to five.** |
```

### 5.6 REQUIRED. Line 591. S5 item two. "Agreed" is not true

The manager's requested S5 row for loop 1 note 4.2.

**Paste over line 591:**

```
| Six months, four hours a day, everyone involved | **TIER 1, MAJORITY FIGURE, VARIANTS NAMED** | Mason, ch. 6, verbatim: "All the officers and other ranks in the camp assisted in some way in the tunnelling and other preparations for this attempt." Corroborated by the NZ Gazette: "All officers and other ranks worked, with the exception of one officer who was awaiting repatriation." **On the duration, six months is the majority but it is NOT agreed. TNA blog: "Work started in September 1942 and after six months of painstaking effort". Boyd, the NZ Army Museum and Wikipedia: six. The NZ Gazette gives 18 September 1942 to "the end of February 1943", about five and a half months of digging inside a six-month captivity-to-escape window. The DNZB entry on Miles says "five months' tunnelling". Six is the majority reading and matches September to March, which is what the script speaks. Do not restore the claim that six "is agreed".** No completion date is stated, because 20 March and late February conflict. |
```

### 5.7 REQUIRED. Line 608. The 1,500 denominator is no longer unverified

**Paste over line 608:**

```
| Three men known to British Military Intelligence to have got clear of Italy before the armistice, two of them these two | **TIER 1, OPENED AT SOURCE** | Mason, *Prisoners of War*, ch. 6, footnote, verbatim: "Of the 1500 attempts at escape from Italy before the armistice known to British Military Intelligence only three (including these two) are on their records as having got clear of Italy." Independently corroborated by Monte San Martino Trust (Jeremy Archer). **Correction to the previous row: the "1,500 attempts" denominator is NOT unverified. It is Mason's own footnote, Tier 1 official history. It remains deliberately unspoken, per the commission, because a denominator invites a percentage the episode does not need and cannot check, not because it lacks a source.** The third man is not named by any source reached, and the script does not speculate. |
```

### 5.8 REQUIRED. Line 617. S5 item three. The Tier 2 specific IS spoken

The manager's requested S5 row for loop 1 note 4.6.

**Paste over line 617:**

```
| Armistice, civilian clothes, an Italian general laid on a train, into the Apennines | **TIER 1 FOR THE SHAPE; THE GENERAL IS TIER 2 AND IS SPOKEN, UNNAMED** | TNA blog (WO 208/3444), verbatim: "the prisoners donned civilian clothing and the Italians moved them by train to Arezzo. Helped by Italian officers and police, they hid in local vineyards and were then bussed up into the Apennine Hills". **That the train was arranged by an Italian general is Neame, *Playing With Strife*, p. 314, via Wikipedia, Tier 2, and the script does speak it, as "An Italian general put a train on". Only his name is withheld. The previous wording of this row, that the Tier 2 specifics "are NOT spoken", was wrong: what is not spoken is General Chiappe's name, the 10 September date and the 60 miles to Arezzo.** The three competing dates for the move (Parri 8 September for Neame, Parri camp sheet 9 September for the transfer to Camaldoli, Wikipedia 10 September) are why no date is spoken. |
```

### 5.9 REQUIRED. Lines 627 and 630. Both are now OPENED, not CARRIED

These are the two rows loop 1 had to leave on trust. I opened both. **Line 630's conflict is also now resolved.**

**Paste over line 627:**

```
| **New Zealand's official history says only that he lost his life** | **TIER 1, OPENED AND VERIFIED, STRAIGHT** | Mason, *Prisoners of War*, ch. 6, verbatim: "Brigadier Miles lost his life in Spain in this last stage of a game attempt to reach Allied territory." **The word "only" in the narration is verified: Mason gives no cause of death anywhere, and his biographical footnote says only "died, Spain, 20 Oct 1943". The contrast the next beat draws with the DNZB is therefore real and correctly stated.** Read from the complete TEI-XML source of the book, nzetc.victoria.ac.nz/tei-source/WH2Pris.xml, via the Internet Archive raw-content capture of 11 October 2016. This supersedes the earlier TIER 1 CARRIED label. |
```

**Paste over line 630:**

```
| **Hargest reached England in December 1943** | **TIER 1, OPENED AND VERIFIED, CONFLICT RESOLVED**, STRAIGHT | Mason, ch. 6, verbatim: "Later in the year, separately and each with the assistance of the French Resistance Movement, they reached the borders of Spain. Brigadier Hargest was able to make his way to the British consulate in Barcelona and was flown to England in December." Corroborated by the DNZB: "Late in 1943 he travelled across occupied France and into Spain ... He then flew to England." **This resolves the earlier conflict note: the reported CWGC "November 1943" is outweighed by Mason's explicit December and the DNZB's "late in 1943", and the script's "that December" is correct.** Mason also verifies the occupied-France leg, which the script speaks: "with the assistance of the French Resistance Movement". |
```

### 5.10 REQUIRED. New row. A spoken number in a straight beat has no log row at all

The script speaks "Sixteen months a prisoner" in Act 11, the most sensitive act in the episode, and **no row in the FACT-CHECK LOG covers it.** Loop 1 fixed the narration and no row was created. That is a documentation gap on exactly the kind of claim the log exists for.

**Insert as a new row immediately after line 630:**

```
| **Hargest was a prisoner for sixteen months** | **TIER 1, TWO INDEPENDENT LINES, ARITHMETIC REDONE**, STRAIGHT | Mason, ch. 6, biographical footnote, verbatim: "Brig J. Hargest ... comd 5 NZ Inf Bde May 1940-Nov 1941; p.w. 27 Nov 1941; escaped Mar 1943". Corroborated by the DNZB (Crawford): "Hargest was captured on 27 November 1941, when his headquarters was overrun." Capture 27 Nov 1941 to break-out 29 Mar 1943 is 16 months and 2 days, so "sixteen months" is correct and rounds down. **Corrected in the loop 1 pass from "two years", which overstated by eight months. Do not restore it.** Note that he was a prisoner for sixteen months but at Vincigliata for about twelve; Mason says he and Miles "were kept in a villa near Sulmona until transferred to Campo PG 12 in the spring of 1942". The script says "a prisoner", not "in the castle", so the two are consistent. |
```

### 5.11 RECOMMENDED. Line 569. The row's own title asserts what blocking 3 removed

Not stale against the narration, but the Beat column reads "**Italians did not guard against escape** because senior officers would not stoop to breaking out", and that first clause is the claim two Tier 1 sources now deny. A build agent reading the log rather than the script could put it back.

**Paste over line 569:**

```
| Italians assumed senior officers "would not stoop to breaking out" | **TIER 1, ATTRIBUTED ON CAMERA; DO NOT WIDEN INTO A GUARD CLAIM** | TNA blog, verbatim: "An abortive attempt to scale the walls out of sight of the guards put the sentries on their guard. Up till then, the Italians had assumed that senior officers would not stoop to breaking out. How wrong they were!" The cold open attributes this to The National Archives out loud and Act 2 turns on it. **The assumption is the only part TNA supports. It is NOT evidence that the camp was lightly guarded, and two Tier 1 sources say the opposite: the NZ Gazette DSO citation opens "This camp was extremely well guarded", and Mason, ch. 6, says "A close watch was kept on their activities in order to prevent the escape of such valuable prisoners" and that walks were taken "under strong guard". Any pre-escape guard characterisation, in narration or in a visual prompt, is forbidden.** |
```

### 5.12 RECOMMENDED. Line 619. Beat title versus what is spoken

**Paste over line 619:**

```
| A German soldier gave them directions while they cycled | TIER 1 | TNA blog, verbatim: "They cycled to Pesaro (once even directed by a German non-commissioned officer who didn't know who they were)." **The narration and the visual tag both say "a German soldier", not "sergeant", because TNA gives no rank beyond non-commissioned officer. Corrected in the loop 1 pass. Do not restore a rank.** |
```

### 5.13 SOURCES block

**Everything the manager pasted checks out.** I verified each new bullet against what the source actually contains:

- **TNA bullet.** The redirect statement is true. I confirmed it myself: the blog URL is unreachable directly and the article text is only retrievable from the Internet Archive capture, which is exactly what the bullet says. **Honest. No change.**
- **NZ Gazette bullet.** I checked its list of supported items against the citation's verbatim text, clause by clause: tunnel dimensions, 18 September 1942 start, "All officers and other ranks worked", 2100 hours on 29 March 1943, train to Milan and Como, twelve-foot cyclone netting with brambles, wire cut with pliers at ground level, crossing into Switzerland. **All eight are genuinely in the document. No overstatement.**
- **NZHistory D-Day bullet.** URL resolves, quotation is verbatim, and it supports exactly what the bullet claims. **Honest.**
- **Crawford DNZB Hargest bullet.** Supports both claims made for it. **Honest**, though it is the only DNZB bullet without an address, see below.
- **Te Ara Miles bullet.** Now gives the entry's own address, as instructed. **Honest**; it makes no availability claim, so it is not the blocking-8 defect class.

**One required SOURCES change, and it is the same defect class as blocking 8.** The Mason bullet ends "Online via the New Zealand Electronic Text Collection, https://nzetc.victoria.ac.nz". That address now **301s to a National Library of New Zealand web-archive viewer that returns no readable text**, which I hit myself this pass. A viewer following it will not reach the book. This is the identical problem blocking 8 fixed for TNA and it must be fixed the same way.

**Paste over the Mason bullet:**

```
- W. Wynne Mason, *Prisoners of War*, Official History of New Zealand in the Second World War 1939-45 (War History Branch, Wellington, 1954), edited by Major-General Sir Howard Kippenberger. Chapter 6 carries the Vincigliata narrative, at pp. 118-19 and 213. Source for the camp's strength and conditions, the September 1942 start in the sealed chapel, "All the officers and other ranks in the camp assisted in some way", the 29 March 1943 break-out on a wet evening, the crossing of the frontier wire near Chiasso on the following evening, Hargest's return through occupied France to Barcelona and England in December 1943, Miles's death in Spain, and the capture dates of both men. Published by the New Zealand Electronic Text Collection at nzetc.victoria.ac.nz ; that address now redirects into the National Library of New Zealand web archive, so the most reliable route to the full text is the Internet Archive capture of the collection's own TEI source file, nzetc.victoria.ac.nz/tei-source/WH2Pris.xml
```

**Two recommended SOURCES improvements, neither blocking:**

1. The **NZ Gazette bullet gives no route at all.** It is the best primary document in the episode and a viewer has no way to reach it. Append to that bullet: ` The citation is reproduced in full as a blockquote in the Wikipedia article "Reginald Miles", which is the most accessible route to the text; the underlying document is the official contemporaneous *Gazette* entry.` That is honest about the route without dressing Wikipedia up as the source.
2. The **Crawford DNZB Hargest bullet has no address** while the Clayton DNZB Miles bullet does. Append: ` https://teara.govt.nz/en/biographies/4h9/hargest-james` for consistency. Verify the slug before pasting; if production cannot confirm it, use `[NOT FOUND: exact entry URL]` rather than guessing, per the block's existing convention.

**One observation, no action.** The CWGC bullet cites "casualty records for Brigadier James Hargest and Brigadier Reginald Miles". Neither research wave nor either QA loop has opened CWGC, which blocks automated access. Nothing in the script rests on it uniquely, and the bullet makes no availability claim, so it is not the blocking-8 class. Leave it.

---

## SECTION 6. COLLATERAL DAMAGE HUNT

The manager flagged that in two of the previous three episodes, loop 1's own fixes introduced new defects. Here is the full sweep.

### 6.1 Orphaned pronouns and broken referents

I traced the referent of every pronoun in the beat before and the beat after each of the seven edits (five blocking, two suggestions).

| Edit | Beat before | Beat after | Referents |
|---|---|---|---|
| Cold open b2 | "A castle in the hills above Florence. In nineteen forty-two, a prison." | "Not laziness. The Italians had made an assumption about senior officers." | "them" x2 in the new line = the twenty-five prisoners, named in the same line. Clean. **But see 6.2.** |
| Act 4 "By Boyd's measure" | "Neame measured the distance outside in daylight ... Twenty-seven feet." | "The spoil filled the chapel ..." | No pronouns. Clean. |
| Act 5 "the early train" | "Six men went out in three pairs ..." | "Which leaves the two most senior men." | "the two most senior men" depends on the previous beat naming four of the six, which it does ("Hargest and Miles ... Boyd and Combe too"). **My blocking fix at 4.1 keeps all four names, so this dependency is preserved.** Clean. |
| Act 6 "one arm" | "Boyd got clear of Milan alone, and was caught at the border." | "The National Archives finds it amazing they lasted as long as they did." | "they" = the walkers, Carton de Wiart and O'Connor. Established by Act 5's closing beat and by the Act 6 map beat. Clean. |
| Act 7 "got off at Como" | Act 6's last beat: "He bought two days for men he could not know were free." | "The frontier wire was twelve feet ..." | New line names both men explicitly. Clean, and it correctly re-anchors after an act break. |
| Act 10 "a German soldier" | "When they ran, monks at Eremo bricked their luggage into a wall, never found." | "In one day: twenty miles over mountains ..." | "them" and "they" = the escaping generals. Clean. |
| Act 11 "By Neame's count" | "Six times they tried to meet a boat. Those helpers risked death." | "The Germans found them in the hills. The officers were higher up." | Fully traced at 3.4. Clean. |

**No orphaned pronouns. No broken referents. This is the failure mode that bit a previous episode and it did not happen here.**

### 6.2 The one real prose regression: the cold open's beats 2, 3 and 4

**Not blocking. Accuracy is fine. The craft is not.**

Loop 1 predicted its own fix would improve the cold open: "it sets up 'Not laziness. The Italians had made an assumption about senior officers' instead of duplicating it." **It did the opposite.** The run now reads:

1. "A castle in the hills above Florence. In nineteen forty-two, a prison."
2. "Twenty-five prisoners. A dozen of them generals. **Nobody expected them to escape.**"
3. "**Not laziness.** The Italians had made an assumption about senior officers."
4. "The National Archives puts it plainly. **Senior officers would not stoop to breaking out.**"
5. "How wrong they were. Six months later they went out through the floor."

Two problems, both introduced by the replacement:

- **"Not laziness" lost its antecedent.** The old beat 2 was a security claim ("almost no guard"), so "Not laziness" answered "why was there no guard?". The new beat 2 is an expectation claim, and an expectation is not the sort of thing that can be laziness. The seam is soft rather than broken, and the bored-sentry picture supplies the missing cue, but the picture is the thing I am also blocking at 4.2, so the cue is going away.
- **Beat 2 now pre-empts beat 4.** "Nobody expected them to escape" and "Senior officers would not stoop to breaking out" say the same thing eight seconds apart, with beat 3 hedging in between. The National Archives payoff lands as a restatement rather than a reveal. Loop 1's own cold-read note said beats 2, 3 and 4 should be "setup, misdirection and payoff"; as applied they are assertion, hedge, restatement.

Accuracy footnote: **the new line is Tier 1 supported.** TNA verbatim, "the Italians had assumed that senior officers would not stoop to breaking out", is exactly this claim. So there is nothing to block. But it sits in tension with Mason's "A close watch was kept on their activities in order to prevent the escape of such valuable prisoners", and with the Gazette's "extremely well guarded", and the tension is avoidable at zero word cost.

**RECOMMENDED replacement, word-neutral across the pair. 23 spoken words in, 23 out.**

- **OLD beat 2 (12 words):** `Twenty-five prisoners. A dozen of them generals. Nobody expected them to escape.`
- **NEW beat 2 (12 words):** `Twenty-five prisoners. A dozen of them generals. The Italians watched them closely.`
- **OLD beat 3 (11 words):** `Not laziness. The Italians had made an assumption about senior officers.`
- **NEW beat 3 (11 words):** `And they had still made one large assumption about senior officers.`

Word-for-word: beat 2, Twenty-five(1) prisoners(2) A(3) dozen(4) of(5) them(6) generals(7) The(8) Italians(9) watched(10) them(11) closely(12). Beat 3, And(1) they(2) had(3) still(4) made(5) one(6) large(7) assumption(8) about(9) senior(10) officers(11). **12 + 11 = 23, identical to the current 12 + 11 = 23. Net change 0, script stays at 1,400.**

Why this is better on all three axes:

- **Accuracy.** "The Italians watched them closely" is near-verbatim Mason ("A close watch was kept on their activities") and agrees with the Gazette ("extremely well guarded"). Two Tier 1 lines, where the current line has one and is in tension with two.
- **Structure.** Beat 2 states a fact, beat 3 turns it ("and they had still made one assumption"), beat 4 pays it off with the Archives naming the assumption, beat 5 detonates it ("How wrong they were"). Setup, turn, payoff, detonation. No duplication, no orphan.
- **Hook strength.** "Well guarded, and they still went out through the floor" is a stronger cold open than "nobody was watching", which quietly tells the viewer the escape was easy.

Referent check: "them" in the new beat 2 = the twenty-five prisoners, named in the same line. "they" opening the new beat 3 = the Italians, named in the immediately preceding clause. "they" in beat 5's "How wrong they were" = the Italians, unchanged. **Clean.**

Consistency check against Act 2: Act 2 says "Until then the sentries had not been watching **for this**. Now they were." That is TNA's wall-climb beat and it is about watching for **escape attempts specifically**, where the cold open's new line is about general supervision of valuable prisoners. Mason draws the same distinction. **No contradiction, and the arc actually improves**: closely watched, but with one blind spot; the wall attempt closed the blind spot; so they went down instead of over.

**This pairs with the blocking visual fix at 4.2.** If the manager applies 4.2 and not 6.2, the picture will say "alert sentries" while the narration says "nobody expected them to escape", which is a milder mismatch than the current one but still a mismatch. **Applying both is the clean outcome. Applying 4.2 alone is acceptable. Applying neither is not.**

### 6.3 Hedge collision: are two attributed beats now adjacent?

I counted every spoken line in the episode that names a source or an authority. **There are eleven.**

| # | Beat | Attribution |
|---|---|---|
| 1 | Cold open b4 | "The National Archives puts it plainly." |
| 2 | Act 3 | "Boyd on the fit." |
| 3 | Act 4 b1 | "Boyd wrote the tool list himself." |
| 4 | Act 4 b6 | "**By Boyd's measure**" (added this cycle) |
| 5 | Act 6 | "The National Archives finds it amazing" |
| 6 | Act 8 b2 | "Neame put the new garrison at" |
| 7 | Act 8 b5 | "The Archives holds it, and calls it" |
| 8 | Act 9 b5 | "The United States Army official history." |
| 9 | Act 11 b3 | "**By Neame's count**" (added this cycle) |
| 10 | Act 11 | "New Zealand's official history says only" |
| 11 | Act 11 | "His entry in the Dictionary of New Zealand Biography says something else." |

**Eleven attributions across 112 beats, one every ten beats. That is rigour density, not hedge density.**

**Adjacency: exactly one pair, #10 and #11, and it is deliberate and pre-existing.** It is the contrast device the whole Miles sequence is built on: source A says this, source B says something else. Two attributions in a row is the only way to stage a disagreement between two sources, and it reads as care, not waffle. It was in the script before loop 1 and loop 1 passed it. **Leave it.**

**The two attributions added this cycle are both well isolated.** #4 is preceded by "Neame measured the distance outside in daylight, faking a deck tennis court. Twenty-seven feet." and followed by "The spoil filled the chapel..." Neither is an attribution. #9 is preceded by "Six times they tried to meet a boat. Those helpers risked death." and followed by "The Germans found them in the hills." Neither is an attribution. **No new collision. The failure mode that bit a previous episode did not happen.**

**One small echo, non-blocking, introduced by blocking 5.** Act 4 now has "Neame **measured** the distance" and, in the very next beat, "By Boyd's **measure**". Same root word, consecutive beats, different men. It is a faint repetition rather than a hedge collision and most viewers will not register it. If the manager wants it gone, here is a word-neutral alternative that keeps the attribution:

- **OLD (12 words):** `Ten feet down, then a gallery. By Boyd's measure, eighteen inches wide.`
- **ALT (12 words):** `Ten feet down, then a gallery. Boyd's notes say eighteen inches wide.`

Ten(1) feet(2) down(3) then(4) a(5) gallery(6) Boyd's(7) notes(8) say(9) eighteen(10) inches(11) wide(12). Net 0. "Boyd's notes" is also marginally more precise, since the source is a written document. **Optional. I am not pressing it. The current line ships.**

### 6.4 Visual tags depicting wording the narration no longer uses

I swept all 112 tags against the seven edits.

| Tag | Status |
|---|---|
| Act 10, "A German **soldier** pointing down a road" | **Correctly updated.** Matches the narration. |
| Act 5 and Act 6 Carton de Wiart tags, "empty sleeve" / "empty pinned sleeve" | **Now correct.** These depicted an arm all along; S1 brought the narration into line with them. |
| Act 7, "the line Florence to Milan to Como picked out" | **Correct and improved.** Showing the Milan leg matches the Gazette, which is the source the "got off at Como" fix rests on. |
| Act 5, "standing on a dark railway platform" | **Correct**, and it fits Mason's night train better than TNA's early train. Compatible with the 4.1 fix. |
| Act 11, bell-board REUSE on the "By Neame's count" beat | Correct. It illustrates the Bain clause, which is the second half of the beat. |
| Cold open scene 3, "Two **bored** Italian sentries ... facing outward, away from the castle" | **WRONG. Blocking. See 4.2.** |
| Cold open scene 2, "**Twenty-five** British and Commonwealth **officers**" | **Wrong on the roster.** Recommended fix at 4.2. |

**One blocking tag, one recommended tag, everything else clean.**

### 6.5 Other staleness introduced or left behind

- **FACT-CHECK LOG:** eleven rows, all listed in Section 5.
- **PRODUCTION NOTES, non-blocking prose only.** Three small inaccuracies, none of which reaches the viewer: the comedy-density bullet lists "the two-and-a-half-year revenge of the Italian army", which is not a line in the script; the Build notes say the comedy resumes "at the subscribe call to action, three beats after the last straight beat", where the subscribe line is not comedy and the first comic line is the **fifth** beat of the outro; and the voice-choices bullet repeats "three beats after the last straight beat" for the teaser. Loop 1 flagged the second of these. All three err in the safe direction. **Tidy them if the file is open anyway; they do not block.**
- **Image budget note** ("reused scenes renumber to 4, 5, 6, 7, 9, 12, 13, 39 and 53"): I verified this against the REUSE tags in the file. **Correct, all nine, no forward references, all byte-identical to their targets.** Unaffected by every edit this cycle.

---

## SECTION 7. TONE, RE-CHECKED AFTER THE EDITS

**Result: PASS. No cuts. No joke sits on, immediately before, or immediately after any of the twenty-one declared straight beats.**

Three of the seven edits sit inside or near the tone-sensitive zones, so I re-ran the adjacency test in both directions rather than trusting loop 1's clearance.

### 7.1 The whole of ACT 11 (seventeen straight beats)

| Direction | Beat | Verdict |
|---|---|---|
| **Before** | ACT 10 closer: "They landed at Termoli. But not everyone got a road home." | Pivot, not a punchline. **CLEAR.** |
| Distance to the nearest joke before | The German-soldier beat, **three beats earlier**, with the mountains-and-bicycles beat and the taxi-and-fishing-boat beat between. Blocking 4 changed one word in that joke and did not move it. | **CLEAR.** |
| **After** | OUTRO beat 1, which is itself straight. | **CLEAR.** |
| **Internal** | All seventeen re-read line by line. The two edited beats inside the act are "By Neame's count, fourteen other ranks left. Sergeant Bain wired the tunnel." and "Fifty-two. Member of parliament. Sixteen months a prisoner. He could have stopped." | **Neither introduces a joke, a bit, a wink or an ironic lift.** "Sixteen months" is if anything harder and flatter than "two years". "By Neame's count" is a neutral attribution. **CLEAR.** |

One judgement call worth stating: **an attribution inside a straight run is not a tonal defect.** "By Neame's count" is beat 3 of 17, early, before the act's weight lands, and it reads as the narrator being careful rather than the narrator hedging away from grief. The three hardest lines, at beats 6, 12 and 17, carry no attribution in their own sentences. **The register holds.**

### 7.2 The three straight beats in ACT 6 (San Vittore)

| Direction | Beat | Verdict |
|---|---|---|
| **Before** | "But in Milan, Combe had done something the popular telling leaves out." | Neutral setup. **CLEAR.** |
| Distance to the nearest joke before | "So that is the honest version. Not indestructible. Just extremely recognisable." is **three beats** earlier, with the Archives beat and the thirty-days-solitary beat between. | **CLEAR.** |
| **After** | ACT 7 opener, now "Hargest and Miles got off at Como and took the road toward Chiasso." Flat and factual. **The blocking-2 edit did not add a joke to this position**, which matters because it is the beat immediately after a straight run. | **CLEAR.** |
| **After, if 4.1 is applied** | 4.1 changes an ACT 5 beat, not this one. The Act 7 opener is unaffected. | **CLEAR.** |

**Checked specifically:** the S1 edit ("one arm") sits **four** beats before the Combe straight run, with the Archives beat, the honest-version beat and the solitary beat between it and the run. It is a wry beat and it is nowhere near a straight beat. **CLEAR.**

### 7.3 The first beat of the OUTRO

| Direction | Beat | Verdict |
|---|---|---|
| **Before** | ACT 11's last beat, "The twelfth of August, nineteen forty-four. He was killed by shell fire." Itself straight. | **CLEAR.** |
| **After** | "Neame designed it. Boyd made the knives. Todhunter and Stirling dug and stayed behind." A roll-call delivered flat. No punchline, no callback gag. | **CLEAR.** |

### 7.4 The Zeppelin L 59 teaser

**It does not land as a punchline after Hargest's death. Confirmed, and the separation is wider than loop 1 stated.**

Outro beat order: (1) "Six went out. Two got clear. Within eighteen months, both were dead." **straight**; (2) the roll-call, flat; (3) "For the true stories from these wars that almost nobody tells, subscribe." not comedy; (4) "Next time, Zeppelin L fifty-nine. Four thousand two hundred miles, about ninety-five hours." factual figures, no joke; (5) "An airship built so the crew could take it apart and eat it." **the first comic line.**

The comic line is the **fourth beat after the last straight beat**, roughly nineteen seconds later, with a roll-call, a subscribe call and a figures beat between. **Ample separation. CLEAR.** (The PRODUCTION NOTES prose says "three beats"; the count is four. Safe-direction error, noted at 6.5.)

### 7.5 Ensemble framing after S1

**Still sells the ensemble. No drift toward the "unkillable soldier" lane. S1 did not tilt it.**

- Carton de Wiart appears in three places and only three: one of six escapers (Act 5), the recaptured walker (Act 6), the Lisbon paperwork (Act 9). He is never called unkillable, indestructible, or the leader.
- Act 6 contains an explicit on-screen refusal of the lane, over a visual of greyed-out competitor thumbnails: "So that is the honest version. Not indestructible. Just extremely recognisable."
- **The injuries are used only as the two Tier 1 sources use them**, and both uses cut against the hero framing: in Act 6 the eye and the arm are why he was **caught**, and in Act 9 they are why the Italians chose him as **credentials**. Neither is a feat.
- **S1 makes the injury heavier, not lighter.** "One arm" is a larger maiming than "one hand", and it appears in a beat whose payoff is his recapture. It pushes away from indestructibility, not toward it.
- The design credit goes to Neame, the tools to Boyd, the two days at San Vittore to Combe, and Switzerland, the title beat and the entire ending to the two New Zealanders. The title sells the ensemble. The thumbnail note steers to the hole and the croquet hoops rather than a famous face.
- The other-ranks gap beat is intact and honest: "What happened to them, I cannot tell you. It is not recorded." Followed by the episode's moral, "The generals wrote books. The men who dug beside them did not." **Mason independently confirms the premise of that pairing: "All the officers and other ranks in the camp assisted in some way."**

**Commission obeyed. Tone gate passed with no cuts.**

---

## SECTION 8. S2, THE MILES WORDING. MY FINAL RECOMMENDATION.

**Recommendation: apply S2. Change "exhausted and in despair" to "in depression and exhaustion". One paragraph, as asked.**

The manager's framing is the decisive point and it changes my predecessor's answer. The two beats are grammatically joined: beat one says the DNZB entry "says something else", and beat two opens with "**That,**", which makes the whole of beat two the content clause of "says". A viewer does not hear an attributed summary, they hear the entry being read out, and the script's PRODUCTION NOTES even single this line out as one of the three hardest in the episode, to be held long against a still image, which is precisely the treatment that invites the viewer to take it as quotation. The DNZB's actual words are "in a state of **depression** and exhaustion". "Despair" is not a synonym for depression: despair is a feeling, depression is a condition, and the swap silently converts a clinical description into an emotional one, which on a death by suicide is the single most consequential kind of paraphrase drift the channel can commit and the one a viewer with the entry open will catch in five seconds. Loop 1 was right that "despair" is warmer and reads better on a still, and right that no reasonable person would call it an error, but "reads better" is exactly the wrong tiebreaker on the one beat in the episode that carries a mandatory mental-health support line, and the exact-match version costs nothing: `That, in depression and exhaustion, he took his own life.` is 10 words against the current 10, net zero, still under 14, and it keeps the script's own "took his own life" in place of the entry's dated "committed suicide", which is the one place the script should and does depart from its source. **Apply it. It is not a blocking defect and I am not failing the episode over it, but if you are pasting anyway, paste this one too.**

- **OLD (10 spoken words):** `That, exhausted and in despair, he took his own life.`
- **NEW (10 spoken words):** `That, in depression and exhaustion, he took his own life.`

Net change **0**. If S2 is applied, the PRODUCTION NOTES Build-notes sentence that quotes this line as one of the three hardest must be updated to the new wording in the same paste, or the notes go stale. **The FACT-CHECK LOG row at line 627-ish already quotes the DNZB verbatim as "in a state of depression and exhaustion", so the log needs no change either way.**

---

## SECTION 9. THE GATE

### 9.1 What blocks shipping (2 items, both exact pastes, total cost: zero words, zero images)

| # | Where | What | Fix at |
|---|---|---|---|
| **B1** | ACT 5, narration | `on the early train` is an unresolved Tier 1 conflict on a spoken specific. TNA says early train, Mason's official history says night train and is the only source with a clock time. Same defect class as loop 1's blocking 2, from the same research sentence. | **4.1**, word-neutral, 14 to 14 |
| **B2** | COLD OPEN, `[VISUAL:]` scene 3 | The bored, slouching, looking-away sentries are the "almost no guard" claim loop 1 blocked, relocated from the audio into the picture. Two Tier 1 sources deny it: the Gazette's "extremely well guarded" and Mason's "a close watch was kept ... to prevent the escape of such valuable prisoners". | **4.2**, prompt edit only, scene 3 is not in the REUSE set |

### 9.2 What does not block but must be pasted before the log is trustworthy (documentation only)

Ten FACT-CHECK LOG rows and one SOURCES bullet, all written out verbatim in Section 5: **5.1** through **5.10** are required, **5.11** and **5.12** are recommended, and the **Mason SOURCES bullet** at 5.13 is required because it repeats the blocking-8 defect for a second source.

Of those, **5.5, 5.6 and 5.8 are the three S5 rows the manager asked for.** They are the "dozen generals" row (line 568), the "six months" row (line 591) and the "an Italian general put a train on" row (line 617).

### 9.3 What is optional

| # | Item | At |
|---|---|---|
| R1 | Cold open beats 2 and 3 rewrite. Fixes the orphaned "Not laziness", removes the beat 2 / beat 4 duplication, and swaps a one-source claim for a two-source one. Word-neutral, 23 to 23. **Strongly recommended, and it pairs with B2.** | 6.2 |
| R2 | Cold open scene 2 tag: "Twenty-five ... officers" should be "prisoners". There were 15 officers, not 25. Free. | 4.2 |
| R3 | S2, the Miles wording. **My recommendation is to apply it.** Word-neutral, 10 to 10. | 8 |
| R4 | Act 4 "measured" / "measure" echo in consecutive beats. Word-neutral, 12 to 12. Not pressing it. | 6.3 |
| R5 | Three stale sentences in PRODUCTION NOTES prose. All err in the safe direction. | 6.5 |
| R6 | NZ Gazette SOURCES bullet has no access route; Crawford DNZB bullet has no address. | 5.13 |

### 9.4 Re-verification after pasting

Every narration change proposed in this report is word-neutral, so the file must still read exactly 1,400. Re-run the mandated script and confirm:

```
SPOKEN: 1400 beats: 112 visuals: 112 REUSE: 9 em: 0 inlineTONE: 0
OVER14: []
REUSE problems: none
```

B2 and R2 touch `[VISUAL:]` tags on scenes 2 and 3, neither of which is a REUSE target, so `visuals` stays at 112, `REUSE` stays at 9 and `REUSE problems` stays `none`. If R1 and R3 are also applied, SPOKEN is still 1400 because both are net zero. **If the script prints anything other than the block above, stop and re-check the paste rather than shipping.**

### 9.5 Where this episode actually stands

I want to be plain about this, because "FAIL" on a final loop reads worse than the state of the file warrants.

**This is a paste-and-ship FAIL, not a rework FAIL.** Two items block, one is a fourteen-word line swap and the other is a sentence inside an image prompt. Neither costs a spoken word, an image, or a second of runtime. There is nothing structural, nothing tonal, and nothing that requires the writer to go back.

The episode is in genuinely good shape. **All nine of loop 1's blocking fixes landed correctly and word-neutrally**, the tone gate passes in both directions on all twenty-one straight beats, the ensemble commission is obeyed and if anything strengthened by S1, the mechanical state is perfect on every one of the seven required values, and the sourcing got materially better this pass: **thirteen claims moved up a tier or gained an independent Tier 1 line because I was able to open Mason.** Two of loop 1's three carried items are now verified at the source and the CWGC conflict on Hargest's return is resolved in the script's favour.

I am failing it for the same reason loop 1 failed it. A channel whose brand is accuracy cannot speak an unattributed specific that the official history contradicts, and cannot put a claim in the picture that it just took out of the narration. Both are free to fix and the fixes are written out above.

**The dominant sourcing error in this script is still understatement, not inflation.** Of the eleven log rows I am asking to be replaced, eight understate the support that exists and only three are stale in the risky direction. Tell the writer that. It is the opposite of the last three episodes and it is worth saying twice.

### 9.6 One note for whoever runs the next episode

The route that unlocked Mason is worth keeping. When a text collection is bot-walled and its HTML pages are unreachable, check whether it publishes a **TEI or XML source file** and whether the Internet Archive holds it, using the `id_` raw-content modifier on the Wayback URL. That turned a 67KB report's largest carried item into a fully opened Tier 1 source in about four minutes, and it produced the one blocking defect two research waves and a full QA loop had all walked past. **The same trick will work on NZETC for every other volume of the New Zealand official histories**, which this channel is going to keep needing.

---

VERDICT: FAIL

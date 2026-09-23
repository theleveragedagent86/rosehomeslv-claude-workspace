# QA Report v5, confirmation pass: Ten Prisoners Stole a Nazi Bomber at Lunchtime

**Reviewed:** `script-v2-final.md` after the four hand-applied fixes for V-1 to V-4.
**Scope:** confirmation only. Names, dates, casualty arithmetic, unit trail, museum figures, act structure, timecodes and tone outside the changed passages were verified in passes 1 to 3 and were not re-audited. Structural numbers below were measured twice, once with a parser written for this pass and once with the folder's `verify_script.py`; both agree exactly.

---

## Blocking-fix closure

| Item | Closed? | Notes |
|---|---|---|
| **V-1** scene 69 | **CLOSED** | `grep` for "taught" over the whole file returns **zero hits**. Body, title, description, thumbnail guidance and production notes are all clean of it. Scene 69 now reads "He ran the start up sequence from memory. Nothing happened." (10 words). **On the "from memory" judgement: fairly carried, not an over-claim.** Scenes 46, 47, 54 and 55 establish the scrap heap explicitly, in narration, before this beat: "He memorised instrument layouts off the wrecks" (47) and "He rebuilt an entire bomber cockpit in his head from other people's wrecks" (54). "From memory" points backward at that established, footnoted material and asserts no instructor, no demonstration and no documented sequence. It is the only reading the script's own ten preceding scenes permit. If it had read "the sequence he had memorised" it would over-claim, because panel layouts are not a start-up sequence; "from memory" says only that nobody was telling him what to do, which is exactly the surviving evidence base. No new unsupported claim. |
| **V-2** scene 104 | **CLOSED** | The exoneration-by-statements claim is gone from the body; no variant of it survives anywhere ( `grep "clear him"` hits only the log entry recording the cut). Scene 104 now reads "He was not cleared then. That would take another twelve years." (11 words), option (a) from pass 3. Supported by the undisputed 15 August 1957 Hero of the Soviet Union award, which the script itself carries at scene 108, and by HTM Peenemünde's "Erst 1957 … freigesprochen". **Arithmetic checks:** scene 99 puts him in custody "until September" 1945, scene 105 has Korolev walking him round the site in September, scene 108 dates the award 15 August 1957. September 1945 to August 1957 is eleven years eleven months, so "another twelve years" and scene 108's "Twelve years later" are consistent with each other and round correctly. **Log entry corrected:** line 660 no longer calls the cut claim verified. It now states outright that "A previous version of this log called it 'Verified and unanimous', which was **false**", quotes the new narration verbatim, and adds "Do not reinstate the exoneration-by-statements beat." "Verified and unanimous" appears nowhere else in the file. |
| **V-3** Förderverein newsletter | **CLOSED** | **Both** places rewritten. Header SOURCES line: "(the inline citation German Wikipedia carries for the intelligence-value argument. NOTE: the newsletter link is dead and no archive snapshot was found, so it could NOT be read directly. The correction ships on the independently verified West versus East split, not on this newsletter.)" SOURCES block entry: "**It could not be retrieved: the link is dead and no archive snapshot was found.** The narration's correction therefore rests on the independently verified Peenemünde West versus East split, not on this newsletter." The phrase "it is what was read" is gone from the file. The one remaining mention, in the FACT-CHECK LOG intelligence-value entry, cites it as "[Förderverein Peenemünde Infoblatt 1/2015, via de.wikipedia]" and explicitly rests the surviving correction on the independently verified split. No line anywhere now claims the newsletter was consulted. |
| **V-4** Devyatayev memoir | **CLOSED** | **Both** places rewritten. Header SOURCES line: "NOT consulted directly: the 11:45 versus 12:36 discrepancy is reported in a ru.wikipedia footnote, and ru.wikipedia cites the 1972 edition. The '21 minutes' is footnoted there to rg.ru 2007, not to the book." SOURCES block entry: "**Not consulted directly, and listed here only because the narration attributes to him.**" plus the same three attributions, and the 1988/Kazan year is dropped from the block entry entirely. Each detail is now attributed to where it actually came from. The old "origin of the '21 minutes'" assertion is gone. |

**No fix introduced a new unsupported claim.** Both replacement lines are shorter and weaker than what they replaced, and both rest on material the script already carries and already sources.

**One stale artefact the fixes created, non-blocking, mechanical.** The two edits took the script from 1,404 to **1,400** spoken words. Four places still state the old number and the old distribution. The measured count is inside the 1,390 to 1,410 budget, so nothing structural fails, but the file now misstates itself in four spots and should be corrected before build:

- Line 3, header: `(1,404 spoken words)` → `(1,400 spoken words)`
- Line 16, VO RATE note: `It has been restored to 1,404 words` → `It has been restored to 1,400 words`
- Line 552, production notes: `**Narration length:** 1,404 spoken words.` → `**Narration length:** 1,400 spoken words.`
- Line 556, beat distribution: `3 beats at 10 words, 2 at 11, 46 at 12, 54 at 13, 7 at 14` → `4 beats at 10 words, 3 at 11, 45 at 12, 53 at 13, 7 at 14`
- Line 669, FACT-CHECK LOG: `**1,404 spoken words across 112 beats**` → `**1,400 spoken words across 112 beats**`, and `Beat distribution 3@10, 2@11, 46@12, 54@13, 7@14.` → `Beat distribution 4@10, 3@11, 45@12, 53@13, 7@14.`

Runtime figures at lines 3, 553 and 554 do not need changing: 1,400 words at 158 wpm is 8:52, which the file's stated 8:53 and 4.76 s average hold round to within a second.

---

## Minor-item adjudication

| # | Item | Shippable or blocking | Exact fix if any |
|---|---|---|---|
| 1 | Scene 38 "technical staff" vs rocket scientists | **Shippable**, but take the fix | Replace scene 38 narration with: **"Two German rocket scientists died. Which brings us to the security arrangements."** 12 words, identical count, no budget effect. The current wording is not false, but "technical staff" reads as the whole technical establishment and silently undercounts the roughly 170 German personnel killed. "Rocket scientists" is what en.wikipedia's Operation Hydra actually says and it makes the beat's point harder. |
| 2 | The word "just" at scene 90 | **Shippable**, take the fix | Replace scene 90 narration with: **"He belly landed the bomber behind the Soviet front line, near Woldenberg."** 12 words, down one. "Behind the Soviet front line" is the Tier 1 museum wording; "just" quietly reasserts a proximity ru.wikipedia's own note disputes at about 30 km. One-word deletion, no other consequence. |
| 3 | Special Camp No. 7 chronology | **Shippable as written.** Optional fix | Not false: the camp did occupy the Sachsenhausen site, from 16 August 1945, and Devyatayev was in custody into September, so the overlap is real if short. Scene 101's "If so" already hedges the identification, and ru.wikipedia's footnote for it is `samlib.ru`, Tier 3, so that hedge must stay exactly as strong as it is. If Ryan wants the chronology tightened, replace scene 100 with: **"Special Camp Number Seven. By August it occupied the site of Sachsenhausen camp."** 13 words, permitted length. I would not hold the ship for it. |
| 4 | "Nine kills" placement, scene 14 | **Shippable**, take the fix | Replace scene 14 narration with: **"May forty four. He talked his way back into fighters. Nine kills overall."** 13 words, up one, permitted. The sources genuinely disagree (de.wikipedia: nine across the whole war and 150 sorties; en.wikipedia: nine with the 104th GIAP after May 1944), so this is a conflict, not an error. "Overall" is safe under both readings. Do **not** use "in all" or "in total": both push the beat to 14 words and scene 14 is not on the approved-exception list. |
| 5 | Bunkerbau cited as Kanetzki but unfootnoted | **Shippable**, take the fix, log-only | In the FACT-CHECK LOG Bunkerbau entry (line 630), replace the trailing citation **`[de.wikipedia citing Kanetzki]`** with **`[de.wikipedia, paragraph unfootnoted, adjacent to Kanetzki]`**. Note this is the *only* occurrence to change: line 631's identical-looking `[de.wikipedia citing Kanetzki; Arolsen …]` on the Greifswald entry is correctly attached and must be left alone. No narration effect. |
| 6 | Scenes 62 to 65 invert the source order | **Shippable**, take the note | Chronology reordered for comedy, no claim falsified, but undocumented. Add one bullet to PRODUCTION NOTES: **"- **Deliberate reordering, scenes 62 to 65.** ru.wikipedia's order is: the group approached a parked aircraft, the guard queried them, Sokolov gave the revetment story, and only then, as the mechanics broke for lunch, the fire was lit at about noon. The script lights the fire first so the lunchtime callback from scene 2 pays. No claim is changed. Do not read this as an error in a future pass."** |
| 7 | Log's weapon rationale is false | **Shippable**, take the fix, log-only | ru.wikipedia does specify the weapon (Krivonogov, "ударив его заранее заготовленной железной заточкой в голову"), so the log's stated reason is wrong even though the narration's silence is right. In the FACT-CHECK LOG guard entry (line 646), replace **"The method is not specified in the v2 sources, so the script does not name a weapon."** with **"ru.wikipedia does specify the method. The script does not name a weapon, and that is a tone decision, not a sourcing one: this beat is TONE: STRAIGHT and no weapon may be named or shown."** Narration does not change. |
| 8 | "Four hundred metres" unsourced, scene 76 | **Shippable**, fix preferred | No source gives a distance for the aborted first run. It is the one invented specific in a script that is otherwise scrupulous, and it also collides audibly with scene 34's "Four hundred men". Replace scene 76 narration with: **"A fascinating vote of no confidence seconds into the plan."** 10 words, down two. |

**Nothing in Part 2 is blocking.** None was upgraded. Items 1, 2, 4 and 8 are the ones worth applying; 5, 6 and 7 are documentation hygiene with no narration effect; 3 is fine as it stands.

**Budget effect if 1, 2, 4 and 8 are all applied:** 1,400 + 0 − 1 + 1 − 2 = **1,398** spoken words, still inside 1,390 to 1,410. No beat crosses 14 words, no new 14-word beat is created, and the 10-word bucket goes from four beats to five. If they are applied, use 1,398 in the five places listed above instead of 1,400, and the distribution becomes 5@10, 3@11, 44@12, 53@13, 7@14.

---

## Structural check

Real output, `verify_script.py`, run against the fixed file:

```
FILE: .../devyatayev-flight/script-v2-final.md
total spoken words          : 1400
visual tag count            : 112
contiguity 1..112           : OK
REUSE tags                  : 10
beat word distribution      : 4@10, 3@11, 45@12, 53@13, 7@14
max beat length             : 14
14-word beat scene numbers  : [31, 33, 34, 97, 98, 101, 112]
beats over 14 words         : []
em-dash count               : 0
en-dash count               : 0
beats with zero spoken words: []
brackets in spoken lines    : []
```

Independent parser written for this pass, same file:

```
total 1400 visuals 112 reuse 10
dist [(10, 4), (11, 3), (12, 45), (13, 53), (14, 7)]
14s [31, 33, 34, 97, 98, 101, 112] over14 []
scene69 10 ['He ran the start up sequence from memory. Nothing happened.']
scene104 11 ['He was not cleared then. That would take another twelve years.']
min 10 [6, 41, 44, 69]
```

| Constraint | Required | Measured | Result |
|---|---|---|---|
| Total spoken words | 1,390 to 1,410 | **1,400** | PASS |
| Visual tags | 112, contiguous 1 to 112 | 112, contiguous | PASS |
| REUSE tags | 10 | 10 (scenes 42, 60, 61, 69, 83, 100, 101, 106, 111, 112) | PASS |
| Max beat length | 14 | 14 | PASS |
| 14-word beats | exactly 31, 33, 34, 97, 98, 101, 112 | exactly 31, 33, 34, 97, 98, 101, 112 | PASS |
| Beats over 14 words | none | none | PASS |
| Em-dashes | 0 | **0** | PASS |
| En-dashes | not required, tracked | 0 | PASS |
| Brackets or stage directions inside spoken lines | none | none, all 112 beats | PASS |
| Beat distribution vs stated | match | **MISMATCH**, file states 3@10/2@11/46@12/54@13/7@14, measured 4@10/3@11/45@12/53@13/7@14 | Stale, mechanical fix listed above |
| Stated word count vs measured | match | **MISMATCH**, file states 1,404 in five places, measured 1,400 | Stale, mechanical fix listed above |

Both fixes are net-shortening, which is why the count moved: scene 69 lost two words, scene 104 lost one, and one further word came out of the same two rewrites. The measured value stays comfortably inside the budget, so the mid-roll floor is unaffected: 1,400 words at 173 wpm is 8:05, still clear of 8:00.

**FACT-CHECK LOG quotes vs body.** Checked by extracting every quoted string of twelve characters or more from the FACT-CHECK LOG and testing each against the concatenated narration lines. Every quote that the log presents as *current* narration is verbatim present in the body. Every quote that is not present is explicitly framed as deleted, superseded, German or Russian source text, or a source title, and each such quote is preceded by "previously said", "old line", "is deleted", "CUT", or a source name. Specifically re-checked after the fixes:
- The log's scene 104 quote, "He was not cleared then. That would take another twelve years.", is verbatim in the body at visual 104.
- No log entry anywhere quotes "he had been taught" or "Statements from former fellow prisoners". Both strings return zero hits in the file except inside line 660's record of the cut.
- The log's scene 55, 51 and 53 entries quote deleted lines, correctly labelled as deleted.
**PASS.**

**Description vs body.** All eight description claims re-tested against narration after the fixes: one guard at lunchtime (scenes 2 and 3), 8 February 1945 (visual 67 and the log), Peenemünde-West (scenes 27, 28, 106), He 111 stolen and flown out (scenes 4, 68, 90), pilot had never flown a bomber (scene 5), learned the cockpit from wrecked instrument panels on the scrap heap (scenes 46 to 48, 54, 55), the identity swap contradicted by the prisoner register (scenes 24 to 26), the pursuing fighter unresolved (scenes 84, 85), and did not steal the V-2 programme (scenes 106, 107). **The description asserts nothing about being cleared, exonerated, taught, or instructed**, so neither fix stranded it. Chapter marks still match the eight act headings exactly. **PASS.**

---

## Tone spot-check

Limited to the changed passages, as instructed.

- **Visual 104 carries the `TONE: STRAIGHT` marker**, confirmed in the tag: "[VISUAL 104: Soviet officers across a desk, a thick file open between them, the prisoner standing. TONE: STRAIGHT.]"
- **The new line is grave and factual.** "He was not cleared then. That would take another twelve years." No joke, no wink, no ironic lift, no comic reversal. It is flatter and colder than the line it replaced, and it is better placed dramatically: it sets up scene 108's award instead of resolving the suspicion early. It sits inside the 93 to 103 straight block's shadow and does not break it.
- **Scene 69 is outside every straight range** and its beat is unchanged in register. "Nothing happened." still lands as the setup for the flat-battery gag at 70 and 71, which is untouched.
- No tone failure in either changed passage.

---

## VERDICT: PASS

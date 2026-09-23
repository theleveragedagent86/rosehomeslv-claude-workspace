# QA Report, LOOP 2 (final gate): The Zeppelin They Sent To Africa (Episode 8, L 59)

Wave 3 gate, second and final pass. I read the current `script.md` fresh, not from memory of loop 1.
For this loop I re-downloaded Douglas Robinson's *The Zeppelin in Combat* full text from the Internet
Archive item `zeppelin-in-combat-a-history-of-the-german-naval-airship-division` and re-read pages
239-240, 274, 280, 310, 314 and 315 in the original; I pulled the raw wikitext of de.wikipedia
"LZ 104", en.wikipedia "Zeppelin LZ 102" and en.wikipedia "Battle of Ngomano"; I pulled Downes,
*With the Nigerians in German East Africa* (1919), pp. 279-281 from the Internet Archive; and I
pulled Schiffer Publishing's own product record for the Etzold book. Where I quote below I have the
words in front of me.

**Headline: every one of the loop 1 fixes landed correctly and none of them introduced a new error in
the narration.** All eleven narration and visual fixes are in place and verified against source. All
five overstated log rows and all four understated log rows are corrected. The mechanicals are exact.
The two binding constraints both pass.

**Five blocking issues remain. All five are in NON-SPOKEN material: one visual prompt, one production
note, and three FACT-CHECK LOG / SOURCES cells. None of them touches a `NARRATOR:` line, so the
script stays at exactly 1,400 spoken words after all five are applied, with no rebalancing needed.**
Two of the five are errors I introduced myself in loop 1 and the Manager applied in good faith.

---

## Part 1. Mechanical checks, measured independently

I parsed the file rather than counting by eye. Every Manager figure is confirmed.

| Check | Manager's figure | My measurement | Result |
|---|---|---|---|
| Spoken words | 1,400 | **1,400** | PASS |
| Spoken beats | 112 | **112** | PASS |
| `[VISUAL:]` prompts | 112 | **112** | PASS |
| Beats over 14 spoken words | none | **none**, longest is 14 | PASS |
| Reuse tags | 10 | **10** | PASS |
| Unique generations | 102 | **102** distinct visual bodies | PASS |
| Em-dashes / en-dashes | 0 | **0**. In fact zero non-ASCII characters anywhere in the file | PASS |
| Brackets, parentheses or stage directions inside a spoken line | none | **none**. Also zero numerals inside any spoken line, so nothing will trip the TTS | PASS |

Beats per act: cold open 6, Act 1 8, Act 2 9, Act 3 9, Act 4 10, Act 5 14, Act 6 24, Act 7 7,
**Act 8 21**, outro 4. Sum 112. Note the Act 8 count against the production note, see blocking issue 5.

## Part 2. Reuse tags, all ten re-checked

Scene numbering in this script is "scene N = the Nth `[VISUAL:]` prompt in file order", which I
confirmed against the unambiguous anchors (scene 2 is the second visual, scene 5 the fifth). Every
reuse points backwards and every one is byte-identical to its target.

| Reuse at visual # | Points to | Backwards? | Byte-identical? |
|---|---|---|---|
| 31 | scene 25 | yes | yes |
| 45 | scene 11 | yes | yes |
| 63 | scene 55 | yes | yes |
| 72 | scene 51 | yes | yes |
| 78 | scene 29 | yes | yes |
| 80 | scene 11 | yes | yes |
| 81 | scene 43 | yes | yes |
| 82 | scene 5 | yes | yes |
| 84 | scene 8 | yes | yes |
| 109 | scene 2 | yes | yes |

There are exactly nine distinct visual bodies that appear more than once, and every one of the extra
appearances carries a REUSE tag. There is no untagged duplicate, and no orphan tag. **Scene 24, the
manic-grin Bockholt caricature, is now referenced by nothing, which is the correct outcome of the
loop 1 tone fix.** 112 visuals minus 10 reuses equals 102 unique generations, confirmed.

## Part 3. The eleven loop 1 fixes, re-verified against source

| # | Fix | Current state | Source check done this loop | Result |
|---|---|---|---|---|
| 1 | L 57 "converted", "never left Germany" | landed, line 112 | en.wikipedia LZ 102, raw: the Naval Office "had LZ 102 cut in half and added two more segments - 30 m in length"; first flight 26 Sept 1917 at Friedrichshafen, two further test flights, then to **Jueterbog**, where she was lost. She never left Germany | VERIFIED |
| 2 | "A gale wrecked her there, fully loaded" | landed, line 116 | en.wikipedia LZ 102, raw: "Loading was completed at noon on 6 October", storm damage just before midnight, fire about two o'clock, burned until morning. de.wikipedia: "durch Sturmboeen beim Luftschiffhafen in Jueterbog schwer beschaedigt, ehe es seine Fahrt antreten konnte" | VERIFIED |
| 3 | "Doctor Max Zupitza. A military physician." | landed, line 84 | Robinson p. 310, read again: "Dr. Zupitza, on board as liaison officer". de.wikipedia: "Der Militaerarzt Maximilian Zupitza machte daher dem Reichskolonialamt die Anregung". Neither gives a professorship | VERIFIED |
| 4 | "nearly forty eight thousand pounds of petrol" | landed, line 212 | Robinson p. 310, read again, verbatim: "20,200 pounds, together with 47,800 pounds of petrol, the cargo amounting to 35,800 pounds, and Dr. Zupitza, on board as liaison officer, and the crew of 21" | VERIFIED |
| 5 | "He overran a Portuguese garrison at Ngomano" | landed, line 384 | en.wikipedia Battle of Ngomano uses that exact noun twice: "made plans to attack the Portuguese garrison across the river at Ngomano"; "the Portuguese garrison at Ngomano received word". 900 troops, six machine guns | VERIFIED |
| 6 | Ngomano visual, "a garrison marked Ngomano" | landed, line 382 | as above | VERIFIED |
| 7 | "The Italians never claimed to have shot her down" | landed, line 430 | Robinson p. 315, read again, verbatim: "When the Italians made no claim to have destroyed her, the Germans concluded that L 59 had fallen victim to an accident." No mention of the British anywhere on the page | VERIFIED |
| 8 | "two points of fire, far off" | landed, line 414 | Sprenger's log, Robinson p. 315, read again, verbatim: "Bearing about 200 degrees, distance from U.B. 53 estimated at 25-30 miles, two points of fire seen in the air, apparently shrapnel bursts" | VERIFIED in the narration. **The visual under it was not updated. See blocking issue 1** |
| 9 | "Most died of disease, not in combat" | landed, line 478 | Hay and Burke, disease-led throughout. The words exhaustion, hunger, starvation and malnutrition still do not occur in the paper | VERIFIED |
| 10 | Bockholt death portrait, no caricature | landed, line 424, unique plate, referenced by nothing | Robinson p. 315: "Bockholt and his crew have been dead for many years" | VERIFIED |
| 11 | Archive visual, folders on a desk not an empty drawer | landed, line 346 | matches the narration's claim exactly and no longer asserts an empty archive | VERIFIED |

## Part 4. Full sweep of all 112 visual prompts against the corrected narration

I read every visual prompt against its own narration beat and against the surrounding beats, not just
the two that changed. Findings:

**One visual now contradicts a corrected narration line. Blocking, see issue 1.** Visual 91 still
places the explosion overhead, which is exactly the error removed from the line beneath it.

**One visual contradicts Robinson and the visual immediately after it.** Visual 96 washes the fuel
tank up on a beach; Robinson p. 315 has it "found off Durazzo", and visual 97 correctly draws the same
tank on the water. Recommended, not blocking, see R2.

**One visual is set dressing that the fuller record contradicts.** Visual 23 puts the L 57 wreck
inside a torn hangar. En.wikipedia's detailed account has Bockholt ordering her walked OUT of the
hangar, a gust taking her across the field in front of the hangar door, and the ship burning until
morning. Recommended, not blocking, see R1. I passed this visual in loop 1 and I was working from a
thinner account of the loss then; I am recording the correction rather than quietly leaving it.

**One referent ambiguity, production only.** Visual 87 opens "The same officer", but the last officer
plate is three visuals back at 84. Recommended, see R6.

**Everything else is clean.** Specifically checked and passed: visual 22's red cross reads as a
struck-out line item and is explained in the prompt; visuals 64 and 65 depict the myth while the
narration is describing the myth, and 65's "theatrical wink" flags it as a story rather than asserting
it; visual 77 no longer overclaims; visuals 74 and 75 hold the two questions apart exactly as the
narration does; visual 105's "fifteen point two" is the correct rounding of Hay and Burke's 15.18
percent; visual 101's "August twenty twenty five" matches BJMH 11.2; every visual in the carrier block
is explicitly plain and uncaricatured, as the build note requires.

## Part 5. Binding constraints, re-checked in their corrected state

**Constraint 1, the recall-signal myth. PASS, and no overcorrection.** Act 6 is unchanged in substance
and still does the thing it was asked to do. It separates the two questions in consecutive beats and
names them as two questions. It affirmatively states that German accounts admit later rumours of
spying and planted false reports, which I re-confirmed verbatim in de.wikipedia this loop: "Zudem gab
es Anzeichen, dass die Briten ueber die Zeppelin-Mission informiert waren, was spaetere Geruechte
ueber Spionageakte und angebliche Falschmeldungen hervorrief." It states the absence of a
contemporary German forgery accusation as an absence, then immediately says "Which is not proof it
never happened", then says Robinson declines to settle it. The load-bearing leg is the German
chronology, which I read again in Robinson p. 310 this loop, verbatim: "three and a half hours after
Bockholt's take-off, the Colonial Office advised the Naval Staff that it could no longer be
responsible for the operation. Von Holtzendorff notified the Kaiser at once... and Jamboli was
directed to recall the airship." No line asserts the British did forge it and no line asserts they
definitively did not. The one visual overclaim from loop 1 is gone. Nothing new was introduced.

**Constraint 2, human cost in Act 8, and the adjacency. PASS.** I re-read the whole act and the beat
either side after the two changes.

- The beat immediately BEFORE Act 8 is Act 7's last, "Afterwards he doubted she would ever have found
  him. A month too late." Sober irony, no punchline, correct ramp down. I re-confirmed the underlying
  claim verbatim in de.wikipedia: "Lettow-Vorbeck bezweifelte im Nachhinein, dass LZ 104 ihn und seine
  Truppe ueberhaupt gefunden haette. Seiner Ansicht nach war die Fahrt um einen Monat zu spaet
  erfolgt."
- The beat immediately AFTER Act 8 is the first outro beat, a flat summary. No joke.
- Inside Act 8, all 21 beats are straight. There is no joke, no wink and no undercut in any line.
- **The visual layer of Act 8 is now clean.** This was the loop 1 failure and it is fixed. The death
  beat carries a unique plain portrait, the caricature is referenced nowhere in the act, and the
  carrier block's plates are all explicitly plain and uncaricatured.
- The carrier-corps material specifically: no joke on it, none in the beat before it ("That was all
  anyone found. The cause has never been settled."), none in the beat after it (the outro summary).
  The changed line "disease, not in combat" is straight and is not adjacent to anything comic.
- The comic Ngomano beats sit two and three beats before Act 8 with the sober Lettow-Vorbeck ramp-down
  beat between them and the act boundary. That separation is intact and is the same as loop 1.

**Constraint 6, format. PASS.** See Part 1.

**Constraint 7. Honoured.** ASCII transliterations are deliberate and not flagged.

---

## Part 6. Blocking issues

Five. All are in non-spoken material. **Applying all five changes the spoken word count by zero, so
the script remains at exactly 1,400 words with every beat at or under fourteen. No rebalancing is
required and no narration line is touched.**

### BLOCKING 1. A visual still puts the explosion overhead, contradicting the line you just corrected. (Act 8, line 412)

The narration was corrected from "two points of fire above him" to "two points of fire, far off",
because Sprenger's log, which Robinson quotes verbatim on p. 315 and which I read again this loop,
puts them "distance from U.B. 53 estimated at 25-30 miles". The visual beneath that corrected line was
not updated and still reads "high above the horizon". At 25 to 30 miles an airship at any plausible
altitude subtends about one degree, that is, effectively on the horizon. The frame as written puts the
explosion over the submarine, which is the exact error the narration fix removed, and it does so in
the straight act on the only eyewitness record the episode has. Visual 91 is not a reuse source and is
not reused, so this edit has no knock-on effects.

OLD: `**[VISUAL: The same submarine crew watching a dark sky, two small points of fire high above the horizon.]**`
NEW: `**[VISUAL: The same submarine crew watching a dark sky, two small points of fire low and far off on the horizon.]**`

### BLOCKING 2. The Etzold publication year is wrong, and it is wrong because of me. (FACT-CHECK LOG line 562, and SOURCES line 630)

In loop 1 I told the Manager the year was 2023 and the Manager applied it in both places. That is
wrong. Schiffer Publishing's own product record for ISBN 9780764370823 carries the tags `PD:2026-04-28`
and `PY:2026`. The author bio on that same publisher page says "His first book, *Reaping the
Whirlwind*, was published by Schiffer in 2023", so *The Africa Ship* cannot also be a 2023 title.
English Wikipedia's citation of the book independently gives 2026. Two independent confirmations of
2026 and a positive disconfirmation of 2023.

While I was there I re-read the publisher description and confirm the quotation used in the log is
verbatim and current: "There was no consideration of a return journey; L 59 would be disassembled for
supplies and her crew would join the fight on the ground."

This one matters more than a typo. The SOURCES block is public, it ends with an invitation to correct
the channel, and it is the block a viewer would check first.

OLD (log, line 562): `Dominic Etzold, *The Africa Ship* (Schiffer, 2023), publisher description:`
NEW (log, line 562): `Dominic Etzold, *The Africa Ship* (Schiffer, 2026), publisher description:`

OLD (SOURCES, line 630): `Dominic Etzold, *The Africa Ship: Ludwig Bockholt, Zeppelin L 59, and the Most Daring Rescue Mission of WWI* (Schiffer Publishing, 2023).`
NEW (SOURCES, line 630): `Dominic Etzold, *The Africa Ship: Ludwig Bockholt, Zeppelin L 59, and the Most Daring Rescue Mission of WWI* (Schiffer Publishing, 2026).`

### BLOCKING 3. The landing-date row claims Tier 1 for something that is illegible in the scan. (FACT-CHECK LOG line 590)

Same class as loop 1's O3, and I missed it then. I checked the scan directly this loop. Robinson's
p. 314 is legible from the words "days - and had covered 4,200 miles" onward, so the fuel figure and
"Nobody had expected L 59 to return" are genuinely Tier 1 and I read them again. But the sentence
giving the landing itself sits in the destroyed p. 313 to 314 transition, which in the scan reads
"Bor th ro / Sig dore..." and is unrecoverable. Nobody on this episode has read the date in Robinson.

The date is still solid, so the spoken line does not change. de.wikipedia states it directly, which I
confirmed verbatim this loop: "In den Morgenstunden des 25. Novembers 1917 wurde schliesslich der
Ausgangsplatz Jambol wieder erreicht." It is also arithmetically forced: Robinson's Tier 1 take-off of
08:30 on 21 November plus the directly sourced 95 h 05 min lands on the morning of 25 November. Only
the tier claim is wrong.

OLD: `| Landed back at Jamboli 25 Nov 1917 with 22,750 lb of fuel, enough for 64 more hours; nobody had expected her back | Robinson p. 314, verbatim | Tier 1 | Popular "19,900 lb" figure rejected |`
NEW: `| Landed back at Jamboli 25 Nov 1917 with 22,750 lb of fuel, enough for 64 more hours; nobody had expected her back | Fuel and "Nobody had expected L 59 to return" are Robinson p. 314, verbatim, read in the original by QA; the landing sentence itself falls in the illegible p. 313 to 314 transition, so the date rests on de.wikipedia, "In den Morgenstunden des 25. Novembers 1917 wurde schliesslich der Ausgangsplatz Jambol wieder erreicht", plus arithmetic: Robinson's 08:30 take-off on 21 Nov plus 95 h 05 min lands on the morning of 25 Nov | Tier 1 for the fuel, Tier 2 plus arithmetic for the date | Popular "19,900 lb" figure rejected |`

### BLOCKING 4. The "China Show" log row now contradicts the corrected production note. (FACT-CHECK LOG line 565)

The Manager correctly amended the PRODUCTION NOTES to say the real code name was the German
*China-Sache*, rendered in English both as "China Show" and as Robinson's "China Matter". The log row
was not brought into line with it. As it stands the row asserts `Code name "China Show"` flatly, cites
only "standard in the literature", and has a completely empty note cell, so the file now says two
different things about the same fact in two different places. I confirmed both renderings myself this
loop: de.wikipedia, "erhielt sie den Decknamen *China-Sache*", cited to Meighoerner-Schardt 1992; and
Robinson's index entry, which is legible and which I read, "China Matter" (flight to German East
Africa), 306. The "China Area" half is genuinely Tier 1: Robinson p. 310, verbatim, quotes the German
staff on "information coming in from the 'China Area'".

OLD: `| Code name "China Show", Berlin's "China Area" | Operation name standard in the literature; Robinson Tier 1 documents Berlin planning around the "China Area" | Tier 1 / Tier 2 | |`
NEW: `| Code name "China Show", Berlin's "China Area" | Robinson p. 310, verbatim, for Berlin planning around the "China Area": "information coming in from the 'China Area,' where a certain deterioration of the situation seems to have taken place"; de.wikipedia for the original code name, "erhielt sie den Decknamen China-Sache", citing Meighoerner-Schardt 1992; MilitaryHistoryNow renders it "China Show" | Tier 1 for "China Area", Tier 2 for the English rendering | The original code name is German, *China-Sache*. "China Show" is one of two common English renderings, the other being Robinson's own index entry "China Matter". Both are translations, not the original. The spoken line stands; see the note under Title options |`

### BLOCKING 5. The Act 8 build note miscounts the act it is enforcing. (PRODUCTION NOTES, line 513)

Act 8 has **21** beats, not twenty. I counted them programmatically and by hand. This is the single
instruction that enforces binding constraint 2, so a wrong count in it is the one place a miscount can
actually cost a beat its TONE: STRAIGHT tag. The note does also anchor the range by naming its first
and last beat, which is what saves it, but the number should be right.

OLD: `That is all twenty beats, from "They rebuilt her as a bomber.`
NEW: `That is all twenty one beats, from "They rebuilt her as a bomber.`

---

## Part 7. Ruling on the Manager-originated Ngomano log row

**The row is accurate in substance and correctly tiered at Tier 2. It is not blocking. I am
recommending a precision tightening in both directions, below.**

What I verified this loop, from en.wikipedia "Battle of Ngomano" raw wikitext and from Downes,
*With the Nigerians in German East Africa* (1919), pp. 279-281, which I pulled in full:

- **"Portuguese garrison" is the sources' own word, not a QA coinage.** The article uses it twice:
  "made plans to attack the Portuguese garrison across the river at Ngomano", and "the Portuguese
  garrison at Ngomano received word from a British intelligence officer". Good.
- **The casualty figures in the support cell are exactly the article's headline set.** Infobox: "200
  killed and wounded", "700 captured", commander Joao Teixeira Pinto killed in action. Downes
  independently: "Major Pinto was killed early in the fight, together with eight other Europeans...
  forced to surrender with 700 Askaris, 6 machine-guns, a quantity of ammunition." The hedges "c." and
  "about" are doing the right work.
- **One understatement.** The article says plainly that "Estimates of Portuguese casualties vary" and
  gives a materially lower alternative set, around 25 Portuguese killed with 162 Askari and almost 500
  captured. The row gives only the higher set with no signal that a lower one exists. Nothing is
  spoken, so this is a log-accuracy point only, but the row should say so.
- **One mild overstatement.** "It was a defended garrison" can be read as "it was a prepared defensive
  position", and both sources explicitly deny that. Wikipedia: "Rather than prepare defensive
  positions, the Portuguese had begun building a large encampment." Downes: "Instead of preparing a
  position for defensive purposes, this column busied themselves in laying out an elaborate camp."
  They fought, from rifle pits dug during the action, and fired 30,000 to 40,000 rounds, so "defended"
  is not false, but "a garrison force that fought and surrendered" is what the sources actually
  support.
- **A second understatement, and this one closes a real gap.** The next spoken beat is "Rifles,
  ammunition, food", and until now nothing in the log supported the word **food**. Downes supplies it
  directly: the Portuguese surrendered with "700 Askaris, 6 machine-guns, a quantity of ammunition,
  and six days' rations for 150 Europeans and 1000 natives", and the Germans then used the prisoners
  as carriers for "all the arms, ammunition, and supplies". The spoken beat is fine; the log simply
  was not carrying its support.

Recommended replacement row, which fixes both directions at once:

OLD: `| On 25 Nov 1917 Lettow-Vorbeck crossed the Rovuma into Portuguese territory and overran the Portuguese garrison at Ngomano | Standard in the East Africa literature; English Wikipedia, "Battle of Ngomano" (c. 200 Portuguese killed or wounded, about 700 captured, Maj. Teixeira Pinto killed) | Tier 2 | It was a defended garrison, not a supply depot. Narration and visual corrected. Date coincidence with the landing is the payoff and is well established |`
NEW: `| On 25 Nov 1917 Lettow-Vorbeck crossed the Rovuma into Portuguese territory and overran the Portuguese garrison at Ngomano, taking rifles, ammunition and food | English Wikipedia, "Battle of Ngomano", which uses the word garrison itself: a Portuguese force of about 900 under Maj. Joao Teixeira Pinto, encamped rather than entrenched (c. 200 killed or wounded, about 700 captured, Pinto killed); Downes, *With the Nigerians in German East Africa* (1919), pp. 279-280, read by QA: surrendered "with 700 Askaris, 6 machine-guns, a quantity of ammunition, and six days' rations for 150 Europeans and 1000 natives" | Tier 2, two independent | It was a garrison force of about 900 that fought and surrendered, not a supply depot. Narration and visual corrected. Casualty estimates vary and a materially lower set exists, so no figure is spoken. Downes's captured rations are the support for the spoken word "food". Date coincidence with the landing is the payoff and is well established |`

## Part 8. Ruling on the three unapplied optional items

**All three: content to ship as they stand. I am escalating none of them.** Two of the three are
better supported now than they were in loop 1.

1. **"Guess whose name was available" (Act 3).** *Ship it, and my loop 1 caveat is withdrawn.* I
   called this a framing rather than a finding. That was too cautious. En.wikipedia's LZ 102 article,
   citing Robinson pp. 306-307 and Belafi, states it outright: "The Imperial German Naval command
   selected the relatively inexperienced *Kapitaenleutnant* Ludwig Bockholt as they did not want to
   lose an experienced commander." That is the beat's exact claim, sourced, and it sits alongside
   Robinson's Tier 1 record of Strasser's dislike of him. The beat is a finding. No change. If the
   Manager wants the log to carry it, see R7.
2. **The schooner-already-abandoned beat (Act 3).** *Ship it.* I re-read Robinson pp. 239-240 in the
   original this loop. The war diary is verbatim "crew leave her in the boats on approach of airship.
   Ascertained ship is unarmed and abandoned... As prize crew, Warrant Quartermaster and two petty
   officers put on board". Nothing spoken is false: three men were in fact put aboard as a prize crew,
   so "He put a boarding party aboard, took the ship, and sent her home" is accurate, and "met by
   German destroyers and escorted into the Elbe" supports "sent her home". This was only ever a note
   that a better joke was sitting unused. It is not a defect and it is not worth spending words on at
   this stage.
3. **"China Show" spoken (Act 2).** *Ship the spoken line.* Confirmed again this loop that it is a
   real and common English rendering, used by MilitaryHistoryNow among others, and the amended
   production note now states the situation correctly. **But the log row was left behind, and that is
   blocking issue 4 above.** The fix is to the log cell only. The narration does not change.

## Part 9. Recommended, not blocking

Each is paste-ready. None touches a spoken line. Apply or decline at the Manager's discretion; none of
them gates the build.

**R1. The L 57 wreck was not inside a hangar. (visual 23, line 114.)** En.wikipedia's detailed account:
Bockholt "ordered the airship to be removed from the hangar"; the gust hit her in the open; "just in
front of the hangar door, the airship suddenly rose 20 m into the air and a strong gust of wind began
to pull it across the field"; she "caught fire about two o'clock" and "the fire burned until the
morning". A wreck on the open field, burning, is both truer and a better frame. I passed this in loop
1 on a thinner account and I am correcting myself.
OLD: `**[VISUAL: A wrecked airship collapsed inside a torn hangar in a storm, canvas flapping, small figures running.]**`
NEW: `**[VISUAL: A huge airship down and burning on open ground in front of a hangar in a storm, small figures running.]**`

**R2. The fuel tank was found at sea, not on a beach. (visual 96, line 432.)** Robinson p. 315,
verbatim: "An oil slick, with some pieces of wood floating in it, and ultimately one of the airship's
droppable fuel tanks, were found off Durazzo." The very next visual, 97, correctly draws that tank on
flat grey water, so as written the same object appears in two incompatible places one beat apart.
OLD: `**[VISUAL: A single dented metal fuel tank washed up on a shingle beach, nothing else around it.]**`
NEW: `**[VISUAL: A single dented metal fuel tank floating alone on open grey water, nothing else around it.]**`

**R3. The Ngomano log row.** Full replacement given in Part 7.

**R4. Zupitza is not sourced as a colonial physician. (FACT-CHECK LOG line 564.)** My loop 1
replacement text said "a military and colonial physician". The row's own support cell only carries
"Militaerarzt" and Robinson's "Dr. Zupitza"; nothing I have reached supports "colonial". The narration
is safe because it says only "A military physician", but the log's claim cell should not claim more
than the narration or the cited sources.
OLD: `The idea came from Dr. Max Zupitza, a military and colonial physician, who flew as liaison officer`
NEW: `The idea came from Dr. Max Zupitza, a military physician, who flew as liaison officer`

**R5. Referent ambiguity for the generator. (visual 87, line 390.)** "The same officer" is three
visuals back, with a map and a stores plate in between.
OLD: `**[VISUAL: The same officer sitting on a crate writing in a field notebook, the captured stores stacked behind him.]**`
NEW: `**[VISUAL: The same German officer in the slouch hat sitting on a crate writing in a field notebook, captured stores stacked behind him.]**`

**R6. "Roughly what the Zeppelin was carrying" (Act 7).** Not an error and not worth a word change.
Recording the seam for the record: the Ngomano haul included six days' rations, and the Zeppelin's
13,930 kg supplies subtotal contained no food for Lettow-Vorbeck at all, its 700 kg of tinned food
being crew provisions outside that subtotal. "Roughly" carries it, and Downes's own summary of what
Lettow-Vorbeck took away, "all the arms, ammunition, and supplies", is the same shape as the airship's
load. Leave it.

**R7. Optional new log row, now that the beat is sourced.** If the Manager wants the log to cover the
Act 3 selection beat:
`Bockholt got the Africa mission partly because the command was unwilling to risk an experienced commander | en.wikipedia Zeppelin LZ 102, citing Robinson pp. 306-307 and Belafi: "The Imperial German Naval command selected the relatively inexperienced Kapitaenleutnant Ludwig Bockholt as they did not want to lose an experienced commander"; Robinson pp. 239-240 Tier 1 for Strasser's dislike of him | Tier 2, resting on a Tier 1 source whose page is illegible in the open scan | Spoken as a sardonic question, "Guess whose name was available", not as a flat claim |`

---

## Part 10. What I re-verified in the original this loop, for the record

So the Manager knows exactly how much of this pass is first-hand rather than carried over.

- **Robinson pp. 239-240**, the schooner capture, read again in full. War diary verbatim, the 688-ton
  schooner, the pit-props, "the only instance of its kind during the war", "Bockholt's flamboyant
  gesture appealed particularly to the men", "To Strasser, however, it almost certainly appeared as a
  foolhardy stunt", "He made sure that the performance was not repeated."
- **Robinson pp. 274 and 280 plus footnote 4**, the hundred-hour flight, read again. "100 hours or
  more", the 10:40 p.m. take-off from Seerappen on 26 July, the western, eastern and northern Baltic,
  and the footnote "Ernst Lehmann, 'Report of 100 hour flight of LZ 120 from July 26-31, 1917'". The
  new U1 row is correct as written.
- **Robinson p. 310**, read again in full. Ballast, petrol, cargo, Zupitza, crew of 21, "cloudy, the
  temperature was exactly freezing", "At 8:30 a.m. came the cry, 'Up ship!'", the whole three and a
  half hours recall paragraph including von Holtzendorff and "L 59 can no longer be reached from here,
  request she be recalled through Nauen", the Nauen calls "but in vain", St Elmo's Fire, the antenna
  wound in, and the "China Area" quotation.
- **Robinson pp. 310-311**, the desert crossing, read again. Ras Bulair near Mersa Matruh at 5:15
  a.m., gas blowing off through the automatic valves, "nose down with an excess load of 1,650 pounds
  aft", Farafrah shortly after noon, Dakhla soon after 3 p.m., and the pinpoint-accuracy comment.
- **Robinson pp. 314 and 315**, read again. 4,200 miles, 22,750 lb and 64 hours, "Nobody had expected
  L 59 to return", the Naples raid on the night of 10 March, the 7 April departure for Malta, UB 53
  under Sprenger, "less than 700 feet high", Sprenger's log in full, the oil slick and droppable fuel
  tank off Durazzo, the Italians making no claim, the fuel-line leaks, and "Bockholt and his crew have
  been dead for many years".
- **Robinson's index**, read again. "China Matter" (flight to German East Africa), 306; "China Area"
  (German East Africa), 308-310; Zupitza, Dr, 305, 310; Juterbog (Germany), ... 306 ...
- **The illegible ranges, checked directly rather than taken on trust.** Pages 308-309 and 311-313 are
  confirmed unrecoverable OCR in this scan. The SOURCES disclosure is accurate. Two consequences worth
  knowing: fragments of the L 57 loss and of the gas-cell shooting are visibly present but unreadable
  on 308-309, and a fragment of the cracked reduction-gear housing is visibly present but unreadable
  on 311-313, which independently confirms the decision to keep both at Tier 2 or cut them.
- **de.wikipedia "LZ 104" raw wikitext.** Confirmed verbatim: the *China-Sache* code name and its
  Meighoerner-Schardt citation; the Zupitza proposal sentence; the Juterbog loss of LZ 102; 95 h 05
  min and 6,757 km; the 25 November morning return; the full German recall signal text and its
  Klein-Arendt p. 324 citation; the manifest and its Klein-Arendt p. 321 citation, with the Klein-
  Arendt imprint matching the SOURCES block exactly, Koeln, Wilhelm Herbst Verlag, 1995, pp. 319-325;
  the "Anzeichen, dass die Briten... informiert waren" sentence; the Gruender conclusion; the 10 March
  Naples raid; "aus ungeklaerter Ursache" for the loss; and Lettow-Vorbeck's own later doubt.
- **en.wikipedia "Zeppelin LZ 102" raw wikitext**, new this loop. The lengthening, the 26 September
  first flight, the two test flights, the delivery to Juterbog, loading complete at noon on 6 October,
  the storm, the fire, and the selection of Bockholt.
- **en.wikipedia "Battle of Ngomano" raw wikitext**, and **Downes 1919 pp. 279-281**, new this loop.
  See Part 7.
- **Schiffer Publishing's product record for ISBN 9780764370823**, new this loop. See blocking 2.

## Part 11. SOURCES block, re-audited after the loop 1 edits

| Element | State now | Result |
|---|---|---|
| Robinson line, illegibility disclosed | "pages 308 to 309 and 311 to 313 are illegible" | **Correct**, and I verified both ranges directly in the scan this loop |
| Hay and Burke | unchanged, live, read | PASS |
| Klein-Arendt, no URL | imprint, year, chapter and page range all match de.wikipedia's citation exactly | PASS |
| Garfield and Lockman, no URL | not opened, and the block does not claim otherwise | PASS |
| **Knox 1993, split onto its own line, "No open URL"** | applied | **PASS**, this was the loop 1 defect and it is fixed |
| **Auk review, keeps the URL, 403 disclosed** | applied | PASS |
| Graichen and Gruender | matches de.wikipedia's bibliography | PASS |
| **Etzold, year added** | year added but the year is wrong | **FAIL, blocking 2** |
| de.wikipedia, en.wikipedia LZ 104, en.wikipedia Battle of Ngomano | live, and all three re-pulled as raw wikitext this loop | PASS |
| **Closing paragraph naming warhistory.org and MilitaryHistoryNow** | applied, and it correctly names all three in-flight details that rest on them | **PASS**, this was the loop 1 gap and it is closed |

No URL in the block is invented. Nothing is cited to the Internet Archive as an authority.

---

## Summary

Narration: clean. Every spoken word in this script is now either Tier 1 in a source I have read in the
original, or Tier 2 hedged on camera in the line itself. The mechanicals are exact. Both binding
constraints pass, including the Act 8 adjacency in the visual layer, which was the loop 1 failure.

The five blocking items are a visual prompt, a build note, two log cells and one citation year. None
of them is spoken, none of them changes the word count, and two of the five are mistakes I made in
loop 1 rather than anything the Manager did. Apply the five pastes above and nothing needs
re-verifying: no narration line, no beat length, no word total, no reuse tag and no other log row is
affected by any of them.

VERDICT: FAIL

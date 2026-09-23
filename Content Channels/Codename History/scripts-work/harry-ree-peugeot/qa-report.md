# QA Report: They Wrecked Their Own Factory to Stop the Next Air Raid (Harry Ree / Peugeot Sochaux)

**Status:** COMPLETE. QA date 3 September 2026. Verdict at the foot of this file.

**Scope of this pass:** every checkable claim in the script re-verified independently against fresh sources, not against the research pack. Foot's *SOE in France* read directly, including Appendix G. Bourne-Paterson's 1946 SOE account quoted verbatim. French-language regional and academic sources read in French. All structural checks run by script, not by eye.

---

## Structural checks

All run by script over `script.md`, not eyeballed. Method for every count below: parse the file line by line, treat as a spoken beat only a line matching `^\*\*(NARRATOR|<NAME> \(character voice\)):\*\*`, strip the leading label and surrounding quotation marks, split on whitespace, and count tokens that contain at least one non-punctuation character. VISUAL tags parsed as `^\*\*\[VISUAL: ...\]\*\*` with any trailing `(REUSE: scene N)` captured separately. Everything from `## PRODUCTION NOTES` down is excluded from all body counts.

| Check | Required | Measured | Result |
|---|---|---|---|
| Narration word count | 1,390 to 1,410 | **1,402** | PASS (matches writer's claim exactly) |
| Spoken beats | n/a | 112 | PASS |
| Longest beat | 14 words max | **14** (max), 7 (min), 12.52 (mean) | PASS, zero beats over 14 |
| VISUAL tags | 112 | **112** | PASS |
| REUSE tags | 11 | **11** | PASS |
| Unique generations | 101 | **101** (112 minus 11) | PASS |
| Em-dashes | 0 | **0** | PASS |
| En-dashes / figure dashes / minus signs | 0 | **0** | PASS |
| Camera moves in VISUAL tags | 0 | **0** | PASS (one false positive on the word "track" in "tank track shoes", not a camera move) |
| Stage directions, brackets, parens, markdown inside spoken lines | 0 | **0** | PASS |
| Required sections present and in order | 9 | 9 present, in order | PASS |
| Act headers | 10 | 10 | PASS |
| Timecodes internally sequential and contiguous | yes | yes, 0:00 to 8:52 with no gap or overlap | PASS |

### Reuse verification, all eleven checked individually

Each reuse was resolved by index, compared byte for byte against its target tag, and checked for backwards direction and for the target not itself being a reuse. **All eleven are correct.** The writer's claim that it fixed four wrong targets holds; nothing is left pointing at the wrong scene.

| Reuse at | Target | Target line | Byte-identical | Points backwards | Target is itself a reuse |
|---|---|---|---|---|---|
| 50 | 5 | 32 | yes | yes | no |
| 58 | 10 | 52 | yes | yes | no |
| 61 | 43 | 198 | yes | yes | no |
| 64 | 8 | 44 | yes | yes | no |
| 69 | 9 | 48 | yes | yes | no |
| 78 | 3 | 24 | yes | yes | no |
| 79 | 6 | 36 | yes | yes | no |
| 80 | 7 | 40 | yes | yes | no |
| 97 | 38 | 178 | yes | yes | no |
| 100 | 99 | 438 | yes | yes | no |
| 109 | 51 | 230 | yes | yes | no |

Separately confirmed: exactly eleven duplicated tag strings exist in the file and **every one of them is the marked reuse**, so there is no accidental unmarked duplicate that would silently cost a generation.

### Runtime, recomputed independently

- 1,402 / 158 = 8.8734 min = **532.4 s = 8:52**. Matches the header and the outro timecode exactly.
- 1,402 / 173 = 8.1040 min = **486.2 s = 8:06**. **Clears the 8:00 mid-roll floor by 6.2 seconds.** PASS, and the writer's "six seconds clear" is accurate.
- Floor margin in words: at 173 wpm the script could lose 17 words before breaching 8:00. Thin, as the writer says. Do not cut narration in the build.

### Act re-timing, verified act by act

Every header timecode is consistent with its own act's word count at 158 wpm to within one second. This was not spot-checked, it was recomputed for all ten.

| Act | Words | Beats | Stated duration | Ideal at 158 wpm | Delta |
|---|---|---|---|---|---|
| COLD OPEN | 123 | 10 | 47 s | 46.7 s | +0.3 |
| ACT 1 | 152 | 12 | 57 s | 57.7 s | -0.7 |
| ACT 2 | 192 | 15 | 73 s | 72.9 s | +0.1 |
| ACT 3 | 199 | 16 | 76 s | 75.6 s | +0.4 |
| ACT 4 | 183 | 15 | 69 s | 69.5 s | -0.5 |
| ACT 5 | 168 | 13 | 64 s | 63.8 s | +0.2 |
| ACT 6 | 125 | 10 | 47 s | 47.5 s | -0.5 |
| ACT 7 | 106 | 9 | 41 s | 40.3 s | +0.7 |
| ACT 8 | 104 | 8 | 39 s | 39.5 s | -0.5 |
| OUTRO | 50 | 4 | 19 s | 19.0 s | 0.0 |
| **Total** | **1,402** | **112** | **532 s** | **532.4 s** | **-0.4** |

Act word counts also confirm three separate claims in the production notes: Act 3 is 199 words, Act 8 is 104 words, Act 4 is 183 words and is the third longest. All three are accurate.

### One structural defect found

**The header on line 3 says "1,401 narration words". The true count is 1,402, and the production notes say 1,402.** Cosmetic, but the header is the first thing a build agent reads and it disagrees with the file. Fix in "Issues to fix".

### Every act ends on a hook

Checked the final beat of each act:

- COLD OPEN: "They were helping pay for it. And by London's own account, they suggested it." Hook, and it is the thesis.
- ACT 1: "And sitting in his new territory was one of the largest factories in France." Hook.
- ACT 2: Bomber Command character line. Hook, but see the tone section, this is a problem beat.
- ACT 3: "Everybody in that valley now had a very direct opinion about British bombing." Hook.
- ACT 4: "It is brave. It is also, quite openly, a sound business decision." Hook, and the episode's argument.
- ACT 5: "This time it worked. The postwar verified list records a three month stop." Hook.
- ACT 6: "December. He was smuggled into Switzerland, reportedly in cars lent by Peugeot." Hook, weaker than the others but it moves him off the board.
- ACT 7: "So the Royal Air Force damaged it severely instead." Hook, but see the tone section.
- ACT 8: "That autumn the Germans stripped Sochaux anyway. Machines and transformers, onto trains, gone." Hook, and "anyway" carries the whole act.

PASS on hooks.

### Excluded-content greps, run over the spoken body only

Every one of these returns zero hits in narration, VISUAL tags and title cards:

`turret`, `80 per cent`, `eighty`, `6,000`, `six thousand`, `five hundred`, `wheelchair`, `football match`, `bakelite`, `swam`, `watched the raid`, `out of production`, `Montbeliard`, `Franche`, `Kubel`, `Schwimm`, `Feldgend`, `Natzweiler`, `14 July`, `fourteenth of July`.

`second raid` returns exactly one hit, line 419, and it is immediately cancelled on line 423. Analysed under Test 1 below.


---

## Tone check

Run beat by beat over all 112 spoken beats, not by trusting the production notes' distribution table.

### Act 3 and Act 8 internally: CLEAN

**Act 3, all sixteen beats, contains no joke, no sarcasm, no aside and no ironic construction.** Verified line by line. The nearest thing to a turn is the closing "Everybody in that valley now had a very direct opinion about British bombing," which is understatement in service of the point rather than a laugh line, and it comes after the casualty figures rather than on them. Acceptable.

**Act 8, all eight beats, contains no joke.** "He was also sports director of the town's football club" is not a gag, it is the setup for the stadium, and the beat that follows it is his deportation. The "anyway" in the final beat is bitter, not funny. Acceptable.

The writer's claim of zero comedy inside both acts is **correct**.

### Adjacency: TWO VIOLATIONS, one of them serious

The brief requires no joke in the beat immediately **before or after** either straight act. That is four adjacencies. The production notes only claim two of them ("no joke in the beat before Act 3 opens or in the beat after Act 8 closes"), which is a narrower claim than the standard. Checking all four:

| Adjacency | Beat | Verdict |
|---|---|---|
| Beat before Act 3 | Act 2 final beat, **BOMBER COMMAND (character voice): "Big factory. Makes things for Germany. We will take care of it."** | **VIOLATION** |
| Beat after Act 3 | Act 4 first beat, "Now. Here is where nearly every version of this story gets the order wrong." | Clean. Direct address, not a joke. |
| Beat before Act 8 | Act 7 final beat, **"So the Royal Air Force damaged it severely instead."** | **VIOLATION** |
| Beat after Act 8 | Outro first beat, "So did sabotage beat bombing? The official historian's own verdict is only moderately good." | Clean. |

**On the Bomber Command line.** This is the serious one. It is a breezy, confident character-voice line in the episode's signature comic device, it is the last thing the viewer hears before the raid, and the very next beat begins the sequence that ends in 123 dead civilians. The writer's own VOICE NOTE places it inside the sarcasm zone: "Deadpan sarcasm carries the cold open, Act 1 and Act 2. It stops completely at Act 3." So by the script's own instruction this beat is read for laughs, and it is read for laughs directly onto the casualty act. The production notes' assertion that "there is no joke in the beat before Act 3 opens" is **false**, and it is contradicted by the same notes' own count of four jokes in Act 2, since the character line is unambiguously one of them.

This is not a marginal call about whether the line is funny. The joke's structure is dramatic irony at the expense of the planners, which is defensible in the abstract, but the payoff of the irony is the deaths themselves. The channel's own automatic FAIL condition covers exactly this.

**On the Michelin line.** Softer, but real. "The Michelin family were offered the same arrangement and refused it. / So the Royal Air Force damaged it severely instead." The "So ... instead" is a karmic punchline and Act 7 is credited with four jokes, of which this is clearly one. It lands one beat before "October nineteen forty three. The Gestapo arrested twenty four resistants in one sweep." Unlike the Bomber Command line the joke is not about the people who died in this episode, and the Michelin plant is a different place, so the offence is adjacency rather than target. Fixable with a small register change rather than a cut.

### Comedy density in the front third: CONFIRMED FUNNY

Counted independently. Cold open through Act 2 is **467 words** by my count against the notes' 466, a one-word rounding difference, about 2:57 of runtime, and it carries roughly 15 comic beats. Recount by act: cold open 6, Act 1 five, Act 2 four. That is one comic beat every 11 to 12 seconds and it matches the notes.

The comedy is genuinely landing, not merely present. The strongest beats are structural rather than written-joke: the cold open's whole architecture, where the sabotage runs perfectly and then "in the morning the factory is running exactly as it was ... because every single detonator had been fitted the wrong way round", is the best cold open the channel has shipped. "That joke is not mine. It is written into the official intelligence report" is a channel-voice line of the exact type the brand runs on. "Which is roughly how a pacifist schoolteacher ended up in the Special Operations Executive" is the Act 1 payoff and it works. "He was also, in nineteen forty and forty one, firmly on Marshal Petain's side" gets its laugh entirely out of the word "also". This is not a flat read. **No failure on the funny side.**

Acts 4 to 7 sustain a dry register: "Funny you should mention it. We had a similar thought", "Wrecking your own machines is cheaper than having your town hit again", "The retellings have him swimming a river and crawling four miles. They embellished", and the German management line. Roughly one every 15 to 16 seconds, inside the bar.

**Tone verdict: FAIL on adjacency, PASS on internal quarantine and PASS on density.** Both violations are one-line fixes and are specified in "Issues to fix".

---

## Primary-source work done for this QA pass

I did not take the research report's word for anything. Two primary texts were obtained and read directly:

1. **M. R. D. Foot, *SOE in France*, full scanned text**, downloaded from the Internet Archive item the script itself cites (`soe-france-foot`, OCR file `SOEFranceFoot_djvu.txt`, 1.58 MB). Every Foot quotation below is grepped out of that text and reproduced verbatim, including page position established from the running heads. **Appendix G's table is OCRed upside down in that scan and I read it in reverse**, which is how the Sochaux rows below were recovered.
2. **R. A. Bourne-Paterson, *SOE in France 1941-1945* (written 1946)**, through the long verbatim quotation of the STOCKBROKER passage on ww2today.com, which is the same text the research report used. This is a secondary reproduction of a Tier 1 document and I say so where it matters.

### Foot, verbatim, from the scan

- p. 287, on what the plant made: "**The Peugeot motor-car factory at Sochaux by Montbeliard had been converted to make tank turrets for the German army and Focke-Wulf engine parts for the German air force.**"
- p. 287, on the raid: "**as indeed happened when the RAF made an ineffective night attack on it on 14 July. The mean point of impact of the bombs was nearly a kilometre from the factory, in which production was undisturbed; some hundreds of townspeople were killed.**"
- p. 287, on the loan: "**one of the directors of the firm was in negotiation with him at the time about lending STOCKBROKER some money to be repaid by the British Treasury after the war.**"
- p. 287, on the threat: "**Ree called on him, and suggested that the director might like to help sabotage his factory, instead of facing all the damage that would ensue when the RAF returned to do the job properly.**"
- p. 287, on the BBC test and the foreman: "**M. Peugeot, naturally enough, asked for some indication that Ree was speaking bona fide; at Ree's invitation, he composed a brief personal message which the BBC duly broadcast a few nights later. Convinced, the director sent for the foreman of the tank turret machine shop, and introduced him to Ree. The agent made one personal reconnaissance, and thereafter never set foot in the factory again; but it was out of production for much of the rest of the war.**"
- p. 288, on Michelin and the fight: "**the Michelin family refused to follow the Peugeots' example and assist in dislocating their tyre factory at Clermont-Ferrand, and the RAF consequently damaged it severely. Ree himself had to flee across the border in November, a bad month for SOE, after a fantastic fist fight with a Feldgendarme who intended to arrest him.**"
- **p. 434**, the verdict the outro rests on: "**The results of industrial sabotage in France were only moderately good in terms of damage and delay to enemy war production.**"
- **p. 436**, the explosive comparison: "**the total quantity of explosives used to produce all these many stoppages taken together was about 3,000 lbs; considerably less than the load of a single light Mosquito bomber in 1944; only a quarter in fact, of the weight of a single Tallboy bomb.**"
- p. 439, the machine tool on the truck: "**When for instance STOCKBROKER had managed to destroy a critical piece of machinery in the Peugeot tank turret factory at Sochaux, and a replacement had been delivered after months of special effort by the Germans, the same circuit managed to destroy it while it was actually waiting to be unloaded from a truck in the factory yard; and all the replacement work had to be gone through again.**"
- Appendix G preamble, p. 505: "**it is compiled from notes made by Brooks when he was sent round France in the winter of 1944-45 to investigate all the claims of actual industrial sabotage inflicted by F section**" and "**A total of about 3,000 lbs of explosive, plastic in almost every case, was required to inflict this substantial quantity of damage.**"

### Foot, Appendix G, the Sochaux-Montbeliard rows, recovered from the reversed OCR

| Date | Product column | Result column | Note column |
|---|---|---|---|
| 5 November 1943 | Peugeot tanks | **3 months' stop** | **"first 'blackmail' operation"** |
| about 15 January 1944 | Peugeot aircraft parts | **3 weeks' stop** | (none) |
| 10 February 1944 | (Sochaux) | **several months' stop** | **Replacement machine tools destroyed on arrival from Germany** |
| 10 February 1944 | (Sochaux) | **5 weeks' stop** | **Replacement machine tools destroyed on arrival from Germany** |
| 15 March 1944 | (Sochaux) | **output cut to 40 per cent** | **Replacement machine tools destroyed on arrival from Germany** |

**Three separate rows carry the replacement-machine-tools note.** The script's "The verified list records that happening three separate times" is exactly right, and it is right off the primary document rather than off the research pack.

### Bourne-Paterson, verbatim

- "**In early July 1943 Henri had made his first contact with the Peugeot management in the person of Paul Sire, Director of Co-ordination for all Peugeot factories, who proved very helpful indeed.**"
- "**Much to his interest Henri found that the Peugeot people themselves were toying with the idea of sabotaging their own factory, in order to stop production and thereby prevent a repetition of the disastrous bombardment by the R.A.F.**"
- "**Despite the careful coaching, the detonators had been put in the wrong way round!**"
- "**On the 5th November (Guy Fawkes no doubt providing the inspiration) the attack was repeated, this time with success.**"
- "**These attacks were carefully analysed in London, and although it was often touch and go, the R.A.F. were successfully dissuaded from making another attack.**"

Further Foot text checks I ran on the scan, which the research report did not report:

- **"Robert Peugeot" occurs zero times in Foot.** Grepped. "Rodolphe" occurs three times in Foot and every one is Henri Sevenet's codename, not a Peugeot. So the log's claim that "Foot never gives a first name at all" is **confirmed directly**, and anyone citing Foot for "Robert Peugeot" is citing something he did not write.
- p. 286, verbatim, which corroborates four Act 1 beats at once: "**Harry Ree (Cesar), who had been received by Southgate near Tarbes in April, jumping with Maingard. Southgate, alarmed by Ree's accent, passed him to HEADMASTER; HEADMASTER was soon in dissolution. Ree moved on to ACROBAT, but disliked Starr's assertive manner, did not fancy the new circuit secure, and was glad to be sent off on a mission by himself.**"
- Foot's index: "**Cesar, see Ree**". Codename confirmed off a Tier 1 index rather than off Wikipedia.
- p. 371, verbatim: "**One of these, Eric Cauchi (Pedro), had been parachuted in August 1943; he did useful work receiving and distributing stores, but was shot by the Gestapo in a cafe brawl on 6 February.**" Also, on the same page: "**Though Ree himself was still out of action in Switzerland**", which corroborates the Switzerland outcome from Tier 1.

---

## Episode-specific tests

### Test 1: NO SECOND RAF RAID

**PASS, and this is now settled off primary text rather than off the research pack.**

Foot p. 287 reads, in full: "Ree called on him, and **suggested** that the director might like to help sabotage his factory, **instead of facing all the damage that would ensue when the RAF returned to do the job properly**." The clause sits inside Ree's suggestion. Grammatically and contextually it is what Ree put to the director as the alternative, not something Foot reports as having happened. The misreading that produced the "second raid" myth is now demonstrable rather than inferred.

Bourne-Paterson, on the other side, gives the actual outcome in SOE's own words: "**the R.A.F. were successfully dissuaded from making another attack**." A raid that had to be dissuaded was a raid that did not happen.

Script grep results: the string "second raid" appears exactly once in the whole file body, at line 419, and the very next spoken beat cancels it. Nothing in any VISUAL tag, title card, act header or production note asserts a second attack. Act 7 is titled "The Raid That Never Came" and its two operative beats are:

> "March nineteen forty four. Bomber Command schedules a second raid on Sochaux."
> "The circuit sent London photographs of the damage. London cancelled the raid."

That says what actually happened. Ree's threat is quarantined in Act 4 as a quoted character line, five acts earlier, and the episode never converts it into an event.

**One residual risk worth naming, not a failure.** Scene 97 reuses the Halifaxes-on-a-wet-airfield picture for the cancelled raid. A viewer half-watching sees bombers again. The narration corrects it inside two seconds and the act title pre-empts it, so I am not calling this a fix. Flagging it so the build does not lengthen that hold.

### Test 6: The causality direction

**PASS, and the primary source is stronger than the script claims.**

Bourne-Paterson, verbatim: "**In early July 1943 Henri had made his first contact with the Peugeot management in the person of Paul Sire, Director of Co-ordination for all Peugeot factories.**" That is explicit on both the month and the person, and July 1943 contact predates the 15/16 July raid.

Foot independently corroborates the loan and its timing: "one of the directors of the firm was in negotiation with him **at the time** about lending STOCKBROKER some money to be repaid by the British Treasury after the war."

The script tells it in the right order and says so out loud: "Ree's first contact with Peugeot management happened in early July. Before the raid." Then Sire, then the loan, then "Repayable by the British Treasury after the war. That predates the raid," then "What the raid created was the argument." **It never tells this as "raid happens, then Ree has an idea."** Test passed cleanly, and Act 4 is the strongest-sourced act in the episode.

One correct restraint worth crediting: the script says only that the arrangement existed, not that the Treasury ever repaid. Foot does not say it was repaid, and neither does the script.

### Test 8: Foot's narrative versus Foot's own Appendix G

**PASS.**

Foot's narrative claim, p. 287, verbatim: the plant "**was out of production for much of the rest of the war**." **Zero hits for that phrase, or any paraphrase of it, anywhere in the script.** Confirmed by grep on "out of production".

Foot's own Appendix G, read directly off the reversed OCR, gives instead: a three month stop, three weeks, several months, five weeks, and output cut to 40 per cent. It also carries the replacement-machine-tools note against three separate dates. **Every effect figure spoken in the episode comes from that list and no other:**

- Act 5: "The postwar verified list records a three month stop."
- Act 7: "The verified list records that happening three separate times."
- Act 7: "Three weeks. Five weeks. Several months. Output cut to forty per cent."

Foot's narrative and Foot's appendix genuinely do disagree, and the appendix wins, because it is Brooks's postwar physical verification tour and the narrative is not. The script picked the right one.

**On the fact-check log's provenance discipline**, which the test asks about specifically: I checked every stoppage row in the log. Each one says which of the two it came from. The three-month row says "**it is Appendix G, not Foot's narrative**". The three weeks / five weeks / several months / 40 per cent row says "**Appendix G only**". The machine-tool row correctly splits the two halves: "**The lorry-in-the-yard detail is Foot's narrative text. The pattern is Appendix G.**" That split is right, and I verified both halves independently: the truck-in-the-yard passage is Foot p. 439 narrative, and the three-times pattern is the appendix. The log also carries a dedicated CUT row for the p. 287 claim. **No stoppage row in the log is silent on provenance.**

### Test 11: The ending must not be triumphalist

**PASS on the substance. One citation defect.**

Foot's verdict, verbatim from the scan: "**The results of industrial sabotage in France were only moderately good in terms of damage and delay to enemy war production.**" Confirmed word for word.

The outro rests on exactly this: "So did sabotage beat bombing? The official historian's own verdict is only moderately good." The episode asks the triumphalist question and then refuses it with the interested source's own hedge. It does not claim an independent assessment exists, and I could not find one either. That absence is real and the script's silence about it is correct.

The second outro beat is Foot's cost argument, also confirmed verbatim: "about 3,000 lbs; considerably less than the load of a single light Mosquito bomber in 1944". The script renders it "All that sabotage in France used less explosive than one light bomber carried." That is a fair compression, and it is used in the narrow cost sense rather than as an effectiveness claim, which is the right call.

**Defect: the page numbers are wrong against the edition the script itself links.** The fact-check log and the SOURCES block cite the "only moderately good" verdict at **p. 438** and the explosive comparison at **p. 439**. In the Internet Archive scan the script links (`archive.org/details/soe-france-foot`), running heads place the verdict on **p. 434** and the explosive comparison on **p. 436**. Page 439 in that edition is a different passage, the machine-tool-on-the-truck one, and the index there reads "Peugeot family, 287-8, 439, 506", which confirms 439 belongs to that passage instead. Pagination does vary between the 1966 HMSO printing and later reissues, so this is most likely an edition mismatch rather than an invention, but the sources block points a viewer at a specific scan and then gives page numbers that scan does not carry. Fix below.

### Test 12: Cuts and hedges

**PASS on every item.** Each was grepped, not eyeballed.

**Cut items, all confirmed absent from the spoken body:** football match (`football match` zero hits, and the only "football" in the script is Auguste Bonal's club, which is a different and documented thing), the returned bakelite bomb (`bakelite` zero hits), the wheelchair (`wheelchair` zero hits, and the picture now reads "An old man in an armchair"), the 80 per cent and 6,000-to-500 production figures (all four search strings zero hits), "out of production for much of the rest of the war" (zero hits), and the claim that Ree watched the raid (zero hits). The Howarth football beat is the one the writer says was hardest to lose and it is genuinely gone, from picture as well as line.

**Hedges, verified in the spoken narration and not merely in the log:**

| Item | Spoken line | Hedge present |
|---|---|---|
| 15,000 trucks | "And light trucks. **By one count**, fifteen thousand of them went east to Russia." | Yes, in the line |
| Switzerland cars | "December. He was smuggled into Switzerland, **reportedly** in cars lent by Peugeot." | Yes, in the line |
| Sire's first name | "**London's report calls him Paul Sire. The French records call him Pierre.**" | Yes, both given, nothing settled |
| Stoppage figures | "**The postwar verified list** records a three month stop." / "**The verified list** records that happening three separate times." | Yes, twice |
| Casualty count | "Three hundred and thirty six were injured. **That is the local French count.**" | Yes, in the line |
| Foot's overstatement | "**The official British history of this operation says** some hundreds of townspeople were killed." | Yes, attributed before it is contradicted |
| The embellished escape | "**The retellings have him** swimming a river and crawling four miles. They embellished." | Yes |
| Stripped plant | "That autumn the Germans stripped Sochaux anyway. Machines and transformers, onto trains, gone." | **No number spoken**, which is the correct treatment of a Chatelot-only figure. The stripping itself is not hedged, and does not need to be, since it is not disputed |

**The 24 arrests.** "October nineteen forty three. The Gestapo arrested twenty four resistants in one sweep." **This is the one item on the writer's own single-source list that is NOT hedged in the spoken line.** The log is candid: "The sweep is corroborated; the number is single-sourced ... The figure of twenty four is Chatelot alone," and Chatelot is Tier 3 and unfootnoted. A bare, specific, unhedged number from one unfootnoted local source, asserted flat in narration, is exactly the automatic FAIL condition in the brief. Fix below, and the fix is cheap.

**The four documented-but-checkable comedy beats the test names:**

- **Guy Fawkes Night.** Verified, and it is quoted from the record rather than invented. Bourne-Paterson: "On the 5th November (Guy Fawkes no doubt providing the inspiration) the attack was repeated, this time with success." The narration's "That joke is not mine. It is written into the official intelligence report" is **literally true**, which is the single best-earned laugh in the episode.
- **The backwards detonators.** Verified. Bourne-Paterson: "Despite the careful coaching, the detonators had been put in the wrong way round!" Tier 1 document, and the exclamation mark is his.
- **The machine tool destroyed on the lorry.** Verified from Foot p. 439 verbatim, "while it was actually waiting to be unloaded from a truck in the factory yard". The script says "lorry" for a British read; same object.
- **The pistol loaded with blanks.** The test's instinct is right that this smells like Ree's own account, and it is: the ultimate origin is Ree, reaching us through Bourne-Paterson's 1946 write-up of SOE's own debriefing. But that is the correct provenance for a first-person combat detail, the script does not dress it up, and Foot independently corroborates the fight itself and its violence at p. 288, "a fantastic fist fight with a Feldgendarme who intended to arrest him". The script also attributes rather than asserts: "What follows is described in the official history as a fantastic fist fight." **No fix needed**, and the beat is not overclaimed.

### Test 13: The four character-voice lines

**PASS. None invents a position.** Note the production notes twice say "three fake dialogue lines" and then describe four; there are four and the count sentence is wrong. Cosmetic, listed below.

| Line | What it compresses | Verdict |
|---|---|---|
| **BOMBER COMMAND:** "Big factory. Makes things for Germany. We will take care of it." | The documented fact that the Peugeot works was the stated target and was on Bomber Command's target list. Foot p. 287: "it was on bomber command's target list." | Asserts nothing beyond the targeting. **Accurate, but see the tone section: its placement is the problem, not its content.** |
| **HARRY REE:** "Wreck the machines yourselves, or the Royal Air Force comes back." | Foot p. 287, Ree "suggested that the director might like to help sabotage his factory, instead of facing all the damage that would ensue when the RAF returned to do the job properly." | A tight and faithful compression, and putting it in Ree's mouth is the single most important structural decision in the script. It is what stops the myth reforming. |
| **RODOLPHE PEUGEOT:** "Funny you should mention it. We had a similar thought." | Bourne-Paterson: "Henri found that the Peugeot people themselves were toying with the idea of sabotaging their own factory." | Faithful. The line is a posture, not a fact claim, and the posture is documented. |
| **GERMAN MANAGEMENT:** "Why does every replacement explode inside our own factory yard?" | Appendix G's three replacement-machine-tool rows, which I verified myself. | It is a question, not an assertion, and the pattern behind it is Tier 1 and real. Thinnest of the four, correctly identified as such in the log, and still inside bounds. |

**None of the four puts a position in anyone's mouth that the record does not support.** No fix.

### Test 4: Rodolphe Peugeot, not Robert

**PASS on the identification, which is better sourced than the script's own log claims. FAIL on one adjacent detail.**

The log rests the identification on the IWM catalogue record for sound archive object 80008516, and is honest that only the catalogue record was read and the audio was not heard. **The test asks whether the script leans on that record harder than it can bear. My finding is that it does not need to lean on it at all,** because the identification is independently supported twice over by sources that have nothing to do with the IWM:

1. **Neal Ascherson, London Review of Books**, a named credentialed writer reviewing the family's own edition of Ree's papers, states it flat: "**He was already in touch with the manager at Sochaux, Rodolphe Peugeot, who was committed to the Resistance.**"
2. **fr.wikipedia's "Peugeot pendant la Seconde Guerre mondiale", citing Loubet**, independently: "**Frere cadet de Jean-Pierre, Rodolphe**", with Rodolphe obtaining Jean-Pierre's agreement to the sabotage.
3. **cancoillotte.net**, Tier 3 but locally specific and entirely independent of the English chain, has Rodolphe Peugeot lending a car and then a factory van with a trusted driver to the circuit, going to London, and landing in Normandy in June 1944. A man doing that is not a bystander.

So the naming survives even if the IWM record is set aside entirely. **I could not fetch the IWM catalogue page myself; it returned HTTP 403.** That means I cannot personally confirm the log's claim about what the catalogue description says. I am not treating that as a defect, because the identification does not depend on it, but **the log should not present the IWM record as the load-bearing source when two better-checked ones exist**, and the SOURCES block should not imply the audio was consulted.

**Robert Peugeot as the elderly father who gave up the presidency in 1941: VERIFIED, from birth and death dates rather than from assertion.** Robert Peugeot, 21 July 1873 to 7 July 1945, president of Peugeot 1910 to 1941. fr.wikipedia: "**Robert Peugeot, age de 70 ans, laisse la presidence a Jean-Pierre**" in **July 1941**. His children are listed as Jean-Pierre III (1896-1966), Helene (1897-1942), Eugene II (1899-1975), **Rodolphe (1902-1979)** and Marthe (1908-2000). So Robert is the father of both men, and **Rodolphe, born 1902, is genuinely younger than Jean-Pierre, born 1896.** The script's "the president's younger brother" is verified off primary birth dates, not off a phrase.

**The wheelchair call was right. The "seriously ill" call was not, and this is a fix.** The log says the wheelchair was cut because it is Chatelot alone, and keeps poor health on the grounds that "fr.wikipedia and Marcot support poor health after several heart attacks". **I checked both fr.wikipedia articles that could carry it. Neither does.** The "Peugeot pendant la Seconde Guerre mondiale" article gives the handover and his age and says nothing about his health. The "Robert Peugeot (1873-1945)" article says nothing about illness, heart attacks or a wheelchair either. So the surviving claim appears to rest on the same single unfootnoted source the writer just rejected, or on nothing.

**"Robert was the elderly father, and seriously ill" is therefore an unhedged narration assertion I cannot trace to a credible source.** That is the automatic FAIL condition, and it is doubly awkward because the script cut a neighbouring detail from that very source on that very ground. It is also unnecessary: the next beat already says he gave up the presidency in 1941, and his age carries the same meaning and is documented. Fix below, same word count.

### Test 5: Paul Sire versus Pierre Sire

**PASS. The disagreement is real and the script neither hides it nor resolves it.**

Both halves confirmed independently:

- **SOE, Bourne-Paterson 1946**: "In early July 1943 Henri had made his first contact with the Peugeot management in the person of **Paul Sire, Director of Co-ordination for all Peugeot factories**, who proved very helpful indeed."
- **cancoillotte.net, in French**: "**M. Pierre Sire, directeur du service de coordination des usines Peugeot pour le Doubs**", with a documented record of organising resistance to the STO and supplying false papers to refractaires. A second French account has Pierre Sire directing the coordination services created by Jean-Pierre Peugeot and making contact with the OCM in early 1943.

The script's handling: "His way in was a senior executive called Sire, the firm's coordination director." then "**London's report calls him Paul Sire. The French records call him Pierre.**" That is exactly right. It gives both, attributes each to its side, and settles nothing. **It does not split the difference and it does not pick a winner.** This is the model treatment for the rest of the channel.

One small point of craft rather than accuracy: SOE says "for all Peugeot factories", the French source says "for the Doubs". The script says "the firm's coordination director", which does not commit to either scope. Correct restraint, no fix.

### Test 2: The raid date and the force composition

**PASS on the date. PASS on the force. One soft note on the markers.**

**Date, night of 15/16 July 1943: VERIFIED** from two genuinely independent families. The Bomber Command lineage (Middlebrook and Everitt, the RAF campaign diary) gives 15/16 July, and the squadron Operations Record Books, worked up independently on the Air-Britain research thread, log the aircraft losses to 16 July 1943.

**Foot's 14 July is confirmed as the error**, verbatim from the scan: "as indeed happened when the RAF made an ineffective night attack on it **on 14 July**". Worth knowing how far that error has travelled: **the commune of Sochaux's own website repeats it** ("Le 14 juillet 1943, un bombardement detruit 35 ateliers du centre de production"), and so does en.wikipedia's Sochaux article. The French "16 juillet" that appears everywhere locally is not a competing claim at all, it is a convention: the bombs fell after midnight, so France dates by the day the bombs landed and the RAF dates by the night of take-off. The script says "The night of the fifteenth of July, nineteen forty three," which is the correct English form and cannot be misread either way.

**Force, 165 Halifaxes: VERIFIED.** Middlebrook gives 165 despatched, 134 from 4 Group and 31 from 8 Group Pathfinder Force. The ORBs independently confirm the split and add what Middlebrook lacks, that 157 actually attacked. The script says "Bomber Command sends a hundred and sixty five Halifaxes", which is the despatched figure and the correct one for the verb "sends".

**The competing French figure of 137 is confirmed as an error and is correctly absent.** It is fr.wikipedia's, unreferenced, and its apparent corroborations are all Wikipedia mirrors. It matches neither despatched, 165, nor attacking, 157. The script does not use it. Correct.

**Pathfinders and markers.** The script says "Pathfinder aircraft go in first to mark the target," which is right and does not commit to a squadron. Middlebrook's 35 Squadron detail is accurate but **405 Squadron was also PFF on this raid**, so had the script named 35 Squadron alone it would have under-described 8 Group. It does not name it. **This is a correct call by omission and I am crediting it.**

**700 yards: single-sourced, and I am passing it with a note rather than calling it a fix.** Middlebrook verbatim: "the centre of the group of markers dropped by the Pathfinder crews of 35 Squadron was **700 yards beyond the factory**." Foot's "nearly a kilometre" and Chatelot's 200 to 300 metres both exist, but **they measure different things**: Foot measures the mean point of impact of the bombs, Chatelot the marking error, Middlebrook the centre of the markers. The script says "The centre of the markers falls seven hundred yards beyond the factory," which is the Middlebrook measurement described in Middlebrook's own terms. That is correctly scoped. If the build ever wants belt and braces, "roughly seven hundred yards" costs one word.

**Other Act 3 numbers, all checked:**

| Spoken | Verdict |
|---|---|
| "About six hundred bombs land on the town. About thirty land in the factory." | **VERIFIED, two independent families.** Middlebrook: "approximately 30 bombs fell in the factory but 600 fell in the town." cancoillotte independently: about thirty on the works, 700 across Sochaux and four neighbouring communes. The script's "About" carries the difference correctly |
| "Ninety to a hundred houses are destroyed." | **VERIFIED, if anything conservative.** RAF campaign diary: over 100 destroyed, 400 badly damaged. cancoillotte: 100 entirely destroyed, 200 uninhabitable, 200 more partly damaged. No fix needed, the range contains the truth |
| "More than a thousand people are displaced." | **VERIFIED as a floor.** fr.wikipedia: "plus de 1 200 sinistres." France Bleu: 1,000 families, which is several thousand people. "More than" is doing honest work. No fix |
| "Five Halifax crews did not come home." | **VERIFIED, two independent families.** Five failed to return; a sixth airframe crashed and was written off, which is why "six lost" appears in some accounts. "Did not come home" is the right phrase for five |
| "The factory itself was assessed afterwards at five per cent damaged." | **VERIFIED.** Middlebrook: "The factory was classed as 5% damaged" |
| "Bomber Command's own record notes that production was normal after the raid." | **VERIFIED twice over, and from opposite sides.** Middlebrook: "the production was normal after the raid." Foot independently: "in which production was undisturbed." This is the most damaging fact in the episode and it comes from the bombers' own record, exactly as the log says |

### Test 3: Casualties

**PASS on the deaths. PASS on the Besancon separation. FAIL on the injured figure, which is mislabelled.**

**The deaths.** The full spread, with who says what, checked source by source:

| Figure | Source | Independent of the others |
|---|---|---|
| **123 killed** | Middlebrook and Everitt, from "the local report" | Bomber Command lineage |
| **120 killed** | Loubet, *La Maison Peugeot* p. 242, via fr.wikipedia, and **cancoillotte independently** | French, two paths |
| **125 killed** | sochaux.fr, France 3, France Bleu, ToutMontbeliard | the standard French public figure |
| **126 killed**, commune of Sochaux specifically | **Coris and Duvernoy**, built from RAF, Luftwaffe and Sochaux, Montbeliard and Besancon archives | the most archivally careful account |
| **135 killed** | Chatelot | Tier 3 |

**The brief's stated range of roughly 120 to 135 is verified, and 123 to 126 is the best-supported core.** The script speaks 123 in Act 3 and then, when correcting Foot, gives "about a hundred and twenty five", which sits inside the spread without borrowing any single source's precision. That is the right treatment and I am passing it.

**Foot's overstatement is genuinely an overstatement, and I checked this rather than assuming it.** "Some hundreds of townspeople were killed" implies a floor near 200 and reads naturally as 300 or more. The Sochaux dead are 120 to 135. **Even if you wrongly fold in Besancon's 51 you reach only about 174 to 186, still short of "hundreds."** Against the best-supported midpoint of about 125 the overstatement is roughly two and a half times. So the script's on-screen correction is not itself an error, which was the risk the test was built to catch. It is right, and Foot's paragraph carries two errors, the date and the magnitude, in three sentences.

**Besancon: VERIFIED and correctly quarantined.** 51 civilians killed is stable across three mutually independent local sources, the Chaprais local-history record, France 3 Bourgogne-Franche-Comte and Hebdo25, though the injured figure there varies between 105 and 131. The dead are at the Gare Viotte and in the Chaprais district, about ninety kilometres from Sochaux. **The separateness is not in dispute anywhere.** Combining the two produces a spurious total of about 174 to 186, which is precisely the mechanism by which "some hundreds" gets manufactured. The script gives Besancon its own two beats and says the deaths "are separate, and are often wrongly combined." **Nowhere in the script are the two totals merged.** Test passed.

One watch item, not a fix: the script says the Besancon bombs fell "by mistake". That is the consensus, but a 2023 France 3 piece reopens whether Besancon station was marked as a target on crews' maps. One regional piece raising a question is not an established conflict, so "by mistake" stands. If the channel wants zero exposure, "the same night, other bombs fell on the city of Besancon" drops two words and asserts nothing.

**THE FAILURE: "Three hundred and thirty six were injured. That is the local French count."**

The label is inverted. **336 is Middlebrook's figure and Middlebrook alone.** Every French source I checked gives about 250: cancoillotte verbatim, "120 morts, 250 blesses"; Loubet via fr.wikipedia, 250; sochaux.fr, France 3 and France Bleu, 250; Chatelot, 250. One 2025 commemoration piece says 500. So the actual local French count for the injured is **250, not 336**, and the script attributes a British-side number to the French and presents a two-hundred-and-fifty-versus-three-hundred-and-thirty-six spread as settled.

This trips two automatic FAIL conditions at once: a significant number asserted in narration without a hedge on one source's authority, and an unresolved source conflict presented as settled. It is also the kind of error the episode exists to correct, which makes it worse than it looks. The fact-check log compounds it: the casualty row lists the competing figures for the **deaths** and is completely silent that the **injured** figure is disputed at all.

Fix below. The deaths figure and its "local French count" label are both fine and stay; only the injured beat changes.

### Test 7: THE NUMBER TRAP

**PASS, and the trap is confirmed as a trap by primary reading rather than by assumption.**

I grepped the spoken body for every form of the two dangerous figures. `80 per cent`, `eighty`, `6,000`, `six thousand`, `five hundred`: **zero hits each.** They are not spoken, not implied and not in any VISUAL tag.

More importantly, the underlying analysis holds up. Both figures come from **one sentence in Chatelot**, and that sentence dates itself against 1939: "Au lieu de 6000 vehicules qui sortaient chaque mois de Sochaux **en juin 1939**, l'usine ne produit plus que 500 vehicules." It sits in his narrative before he reaches 1943 at all, and the 500 is a mix of civilian 202 saloons and DMA trucks, an output-mix figure rather than a damage figure.

The 80 per cent has an even better explanation than the research report gave. Loubet, reached through edechambost, records that **Colonel Max Thoenissen of the German motor-vehicle materiel directorate told Peugeot in 1940 that its car production would be capped at 20 per cent of pre-war**. That is a German policy decision three years before the sabotage. The collapse was an imposed cap plus raw-material scarcity plus the STO draining skilled men, and it was substantially complete before Ree ever walked into the valley.

So the figures are real, they measure the occupation, and attributing them to Ree would have been the worst available error. **The script does not attribute them to anything, because it does not mention them.** Every effect figure it does speak is an Appendix G stoppage, and each is introduced as "the verified list". Clean pass.

### Test 10: The myth inversion

**PASS, and it is the best-sourced thing in the episode.**

The admission exists and I have it verbatim from Bourne-Paterson: "**Much to his interest Henri found that the Peugeot people themselves were toying with the idea of sabotaging their own factory, in order to stop production and thereby prevent a repetition of the disastrous bombardment by the R.A.F.**"

The script renders it across two beats: "London's own nineteen forty six report says Peugeot were already toying with the idea." then "Sabotage their own factory, stop production, and prevent another disastrous British bombardment." **That is a near-verbatim reduction with nothing added.** "Toying with the idea" is the source's own phrase, "disastrous" is the source's own word, and the three-part purpose clause is the source's own structure in the source's own order. I could not improve on it.

**Does the script overstate it into "Peugeot were only protecting themselves"? No.** Act 4 closes: "It is brave. It is also, quite openly, a sound business decision." Brave comes first, the self-interest comes second, and the two are held together rather than one cancelling the other. The word "also" is carrying the whole moral position and it is carrying it correctly. **This is the strongest writing in the script and it should not be touched.**

Worth adding for the build's confidence: this is an admission against the writer's own interest. SOE, writing its own official internal account in 1946, conceded that the idea was in the room before its agent proposed it. That is the highest-value kind of testimony there is, and nothing needs to corroborate it.

### Test 9: What the factory produced

**SPLIT VERDICT. The inversion against Foot is justified and I am upholding it. But two items in the replacement list do not survive checking, and one of them is a real error.**

**First, the inversion itself: JUSTIFIED.** Foot, verbatim, "converted to make **tank turrets** for the German army and Focke-Wulf engine parts for the German air force," and his Appendix G product column reads "Peugeot tanks". **No French or German source anywhere says *tourelles de chars*.** The French record consistently says *patins de chars*, track shoes or pads. There is even a plausible mechanism for how SOE got it wrong: Sochaux's surviving industrial strengths in 1940 were the forge, the foundry and the pressing shops, per Auto-Union's own October 1940 audit of the plant, and a pressing plant stamping armour track links is exactly what a wartime agent's report compresses into "tank turrets". Appendix G's "Peugeot tanks" is a target-list column label, not a production finding. **A Tier 1 source can be wrong about a specific, and here it is. The script is right to drop the phrase, and right to have flagged the inversion in the log.**

**Item by item on the replacement list:**

| Spoken item | Verdict |
|---|---|
| Tank track shoes | **VERIFIED**, multiple independent French sources including cancoillotte on the sabotaged output rate |
| Connecting rods, cylinder heads | **SINGLE-SOURCED to Chatelot**, one unfootnoted local memoir: "L'usine de Sochaux produit aussi des pieces pour la Wehrmacht (bielles, culasses et patins de chars)." fr.wikipedia carries only *joints de culasse poreux*, head **gaskets**, and only inside a list of sabotage methods, which is a different thing entirely. **Asserted unhedged in the script** |
| "All of it for German tanks" | **OVERSTATED even on Chatelot**, who says *pour la Wehrmacht*, not for tanks. Connecting rods and cylinder heads are engine parts, not tank-specific |
| Light trucks, DMA | **VERIFIED** independently |
| **Aircraft landing gear** | **CONTRADICTED.** fr.wikipedia: the plant "construisait **jusqu'en 1940** des trains d'atterrissage". edechambost lists landing-gear elements under **September 1939 to June 1940, French Army** output. **This is pre-occupation French war work, not a German order**, and the script places it inside a list introduced by "By nineteen forty three it was building whatever the German war economy asked for" |
| Later German aircraft parts | **VERIFIED** generically, by Foot, Chatelot and driventowrite. The script says "parts for German aircraft", which is the right level. It correctly does **not** say Ta 154, which is fr.wikipedia only |
| Volkswagen control early 1943, Porsche wanted the foundry | **VERIFIED, and better than the log claims.** edechambost, footnoting Loubet 2009 pp. 237-260 and Peter Lessmann in *Histoire, economie et societe* 1992: Speer's ministry made Volkswagenwerk the official *Patenfirma*, "pour qui la fonderie comblait une lacune de son parc industriel", with the agreement signed **27 March 1943**. Chatelot and driventowrite corroborate independently. **The log's "no Tier 1 source in the file covers the takeover" was too pessimistic; there is an academic chain** |
| Military car parts after the takeover | **VERIFIED**, Kubelwagen and Schwimmwagen parts in quantity |

**So the list is right about the thing the test was built to check, and wrong about one item it smuggled in.** The landing gear is the error and it has to come out. The connecting rods and cylinder heads need a hedge or a cut. Fixes below.

**One further item under this test, because it is a production number: the fifteen thousand trucks. FAIL, on arithmetic.**

Chatelot verbatim: "Les Allemands destinent le modele essence au front Russe (**15463** expedies jusqu'en septembre 1944)." But **total DMA production over the whole run, March 1941 to September 1944, was about 15,306**, of which about 13,779 went to German forces. So 15,463 **petrol DMAs sent east alone** is larger than every published figure for total DMA output, and larger still than the German-commandeered share. **The number cannot be right.** The "By one count" hedge does not rescue it, because the brief's standard is a number traceable to a credible source and this one contradicts the production totals. The Russian-front framing is also shakier than it looks: cancoillotte presents the eastern despatch through the story of *fausses ambulances pour le front russe*, which is a pretext narrative rather than a delivery ledger. Fix below.

---

## A source the research pack did not use, and it changes several verdicts

**Harry Ree, *A Schoolmaster's War*, edited by Jonathan Ree, Yale University Press 2020.** The script's SOURCES block lists it and says "Introduction accessed; full text not". **The full text is available and I read it.** It is Ree's own contemporaneous and near-contemporaneous writing plus an editorial chronology built from the IWM private papers and French local archives, published by a university press. **On Ree's own life and on the night of the fight it outranks Foot and Bourne-Paterson both, because it is the man himself, checked.**

It contradicts the script in six places. Every one of them is in the "Issues to fix" list. This is the single most consequential finding of this QA pass, and it is entirely a consequence of the writer stopping at the introduction.

---

## Claim-by-claim verification

Significant claims only. Verdicts: **OK** means independently verified to the brief's standard. **NOTE** means verified but with a caveat the build should know. **FIX** means it does not ship as written.

| # | Claim (as spoken) | Where | Source(s) checked | Verdict |
|---|---|---|---|---|
| 1 | "Night, the third of November, nineteen forty three." | Cold open | Bourne-Paterson; Jonathan Ree's chronology; cancoillotte | **OK** |
| 2 | "They place plastic explosive on the transformers and the forge compressors." | Cold open | Bourne-Paterson; cancoillotte independently on the forge compressors | **OK** |
| 3 | "Because every single detonator had been fitted the wrong way round." | Cold open | Bourne-Paterson verbatim: "the detonators had been put in the wrong way round!" | **OK** |
| 4 | "So they went home, and came back two nights later, on Guy Fawkes Night." | Cold open | Bourne-Paterson verbatim, Guy Fawkes is his own parenthesis; Jonathan Ree confirms 5 November | **OK** |
| 5 | "That joke is not mine. It is written into the official intelligence report." | Cold open | Bourne-Paterson 1946 | **OK**, and literally true |
| 6 | "They were helping pay for it. And by London's own account, they suggested it." | Cold open | Foot on the loan; Bourne-Paterson on "toying with the idea"; no figure spoken, correctly, since the figures conflict | **OK** |
| 7 | "Harry Ree is a schoolmaster, teaching modern languages at **Bradford Grammar**." | Act 1 | *A Schoolmaster's War*: he started in **1937 at Beckenham and Penge County School for Boys, South London**, and went to **Bradford Grammar on 1 September 1946**, after the war. IWM catalogue 10858 independently: "school teacher in **Beckenham, London 1937-1940**" | **FIX. Flatly wrong.** |
| 8 | "Nineteen forty. He registers as a conscientious objector." / "on condition that it is the National Fire Service." / "Nineteen forty one. He changes his mind and registers for military service." | Act 1 | Rests on one IWM catalogue line. **Contradicted by Ree himself**: "I'd given up being a conchie **before the fall of France**." Jonathan Ree: "he was not in any position to register as a conscientious objector: he had abandoned the pacifism he espoused as a student," and the chronology has **no tribunal**, an enlistment as a gunner on **14 November 1940**, Intelligence Corps April 1941. **The National Fire Service did not exist until August 1941**, so the 1940 condition is an anachronism as worded | **FIX. Three beats.** |
| 9 | "Captain, Intelligence Corps. Codename Cesar. In the field he answered to Henri." | Act 1 | **London Gazette** supplement 37349, 15 Nov 1945, p. 5574: "Captain (temporary) Harry Alfred REE, O.B.E. (252415), Intelligence Corps." Bourne-Paterson: "Operational name of organiser: Cesar. Name by which known in the Field: Henri." Foot's index: "Cesar, see Ree" | **OK.** Three independent sources, one a state record |
| 10 | "April nineteen forty three. He parachutes into France and is met near Tarbes." | Act 1 | Foot p. 286; Bourne-Paterson, 15 April; Jonathan Ree, dropped 14-15 April, Southgate contact 18 April, sheltered at Tarbes | **OK** |
| 11 | "The organiser who received him listened to Ree's French accent and was alarmed." | Act 1 | Foot p. 286 verbatim, "Southgate, alarmed by Ree's accent." **Jonathan Ree locates the accent problem at Clermont-Ferrand instead**, "schoolmaster French" | **NOTE.** Foot alone on the where, but the substance is agreed and the script names nobody and no place |
| 12 | "The first circuit collapsed almost immediately." / "He distrusted the security of the second one, so they sent him east alone." | Act 1 | Foot p. 286 verbatim; Bourne-Paterson; Jonathan Ree | **OK** |
| 13 | "They called it Stockbroker." | Act 1 | Foot, "Ree's STOCKBROKER thus became an independent circuit"; Bourne-Paterson | **OK** |
| 14 | "**Tank track shoes. Connecting rods. Cylinder heads. All of it for German tanks.**" | Act 2 | Track shoes VERIFIED, cancoillotte and others independently. **Connecting rods and cylinder heads are Chatelot alone**, one unfootnoted local memoir; fr.wikipedia has only *joints de culasse poreux*, head gaskets, inside a sabotage list. **"All of it for German tanks" overstates even Chatelot**, who says *pour la Wehrmacht* | **FIX** |
| 15 | "**Aircraft landing gear**, and later on, parts for German aircraft as well." | Act 2 | **CONTRADICTED.** fr.wikipedia: the works built landing gear "**jusqu'en 1940**". edechambost places landing-gear elements under **September 1939 to June 1940 French Army** output. It is pre-occupation French work, not a German order | **FIX** |
| 16 | "**By one count, fifteen thousand of them went east to Russia.**" | Act 2 | Chatelot alone gives 15,463 petrol DMAs east to September 1944. **Total DMA production over the entire run was about 15,306, of which about 13,779 went to German forces.** The figure exceeds every published total, so it cannot be right | **FIX. Bad arithmetic, and the hedge does not save it** |
| 17 | "Berlin puts the whole plant under Volkswagen control." / "Ferdinand Porsche wanted the foundry." | Act 2 | **VERIFIED and better than the log claims.** edechambost footnoting **Loubet 2009 pp. 237-260** and **Lessmann, *Histoire, economie et societe* 1992**: Speer's ministry made Volkswagenwerk the official *Patenfirma*, "pour qui la fonderie comblait une lacune de son parc industriel", agreement signed 27 March 1943. Chatelot and driventowrite corroborate | **OK** |
| 18 | "Soon Sochaux was turning out military car parts." | Act 2 | Kubelwagen and Schwimmwagen parts, two independent sources. Correctly generalised for TTS | **OK** |
| 19 | "Running the French side of it was the company president, Jean Pierre Peugeot." | Act 2 | Hubert Bonin, Sciences Po Bordeaux working paper: "son pere Robert Peugeot, a qui il succede en juillet 1941"; Marcot via fr.wikipedia | **OK** |
| 20 | "He falsified production reports." / "He invented procedures to slow the work" | Act 2 | **fr.wikipedia alone**, summarising the paywalled Marcot. cancoillotte independently describes something different, the direction supplying real production states **to London via Ree** | **FIX, low priority.** Attribute or soften |
| 21 | "hid hundreds of men from conscription" | Act 2 | **VERIFIED twice.** Chatelot: hundreds of refractaires across 19 farms and forestry sites. cancoillotte independently credits Pierre Sire with reclassing about 200 plus forged papers | **OK** |
| 22 | "A deputy of the firm voted to hand Petain absolute power." | Act 2 | **Tier 1: Assemblee nationale, base Sycomore, fiche 5855**, Francois Peugeot, deputy for the Doubs, voted the constituent powers on 10 July 1940. **The script wisely does not name him or state a relationship**, which matters because he was Jean-Pierre's **cousin**, not his brother, and at least one academic source gets that wrong | **OK**, and the restraint is correct |
| 23 | "The standard study of the family is titled Petainism, reluctance, opposition, resistance." | Act 2 | **VERIFIED exactly.** Marcot, *Le Mouvement social* no. 189, 1999, pp. 27-46, confirmed through Bonin's citation, JSTOR and Cairn | **OK** |
| 24 | "The night of the fifteenth of July, nineteen forty three." | Act 3 | Middlebrook and Everitt; RAF campaign diary; squadron ORBs logging losses to 16 July. Foot's 14 July confirmed as the error | **OK** |
| 25 | "a hundred and sixty five Halifaxes" | Act 3 | Middlebrook, 165 despatched, 134 from 4 Group and 31 from 8 Group; ORBs independently. fr.wikipedia's 137 is unreferenced and matches nothing, and is correctly absent | **OK** |
| 26 | "The centre of the markers falls seven hundred yards beyond the factory." | Act 3 | Middlebrook verbatim. Foot's "nearly a kilometre" measures the bombs' mean point of impact and Chatelot's 200 to 300 metres measures the marking error, so neither is a competing value for this quantity | **NOTE.** Single-sourced but correctly scoped |
| 27 | "About six hundred bombs land on the town. About thirty land in the factory." | Act 3 | Middlebrook verbatim; cancoillotte independently, about thirty on the works and 700 across five communes | **OK** |
| 28 | "Ninety to a hundred houses are destroyed. More than a thousand people are displaced." | Act 3 | RAF campaign diary, over 100 destroyed; cancoillotte, 100 destroyed and 200 uninhabitable. fr.wikipedia, "plus de 1 200 sinistres"; France Bleu, 1,000 families | **OK.** Both figures are conservative and both are hedged |
| 29 | "A hundred and twenty three people were killed that night." | Act 3 | Middlebrook from the local report. Cross-checked against Coris and Duvernoy (126), Loubet (120), the French public figure (125), Chatelot (135). Sits in the best-supported core | **OK** |
| 30 | "**Three hundred and thirty six were injured. That is the local French count.**" | Act 3 | **336 is Middlebrook alone.** Every French source gives about **250**: cancoillotte, Loubet via fr.wikipedia, sochaux.fr, France 3, France Bleu, Chatelot. One 2025 piece says 500. **The label is inverted and the spread is presented as settled** | **FIX** |
| 31 | "Fifty one people died there. Those deaths are separate, and are often wrongly combined." | Act 3 | 51 stable across three mutually independent Besancon local sources; separateness undisputed everywhere | **OK** |
| 32 | "Five Halifax crews did not come home." | Act 3 | Middlebrook; ORBs naming all five aircraft; aircrewremembered. A sixth airframe crashed and was written off, which is where "six" comes from elsewhere | **OK**, and "did not come home" is the right phrase for five |
| 33 | "assessed afterwards at five per cent damaged" / "production was normal after the raid" | Act 3 | Middlebrook verbatim on both; Foot independently, "in which production was undisturbed" | **OK.** Two sources from opposite sides |
| 34 | "The official British history of this operation says some hundreds of townspeople were killed." / "It is wrong. The real figure is about a hundred and twenty five." | Act 3 | Foot p. 287 verbatim. Overstatement independently confirmed at roughly 2.5 times. 125 sits inside the 120 to 135 spread without borrowing anyone's precision | **OK.** The correction is itself correct, which was the risk |
| 35 | "Ree's first contact with Peugeot management happened in early July. Before the raid." | Act 4 | **Bourne-Paterson verbatim.** Jonathan Ree's chronology puts the Sire introduction to Rodolphe Peugeot even earlier, **12 June 1943**, which strengthens rather than weakens the point | **OK** |
| 36 | "London's report calls him Paul Sire. The French records call him Pierre." | Act 4 | Bourne-Paterson, "Paul Sire, Director of Co-ordination for all Peugeot factories". cancoillotte, "M. Pierre Sire, directeur du service de coordination des usines Peugeot pour le Doubs". **Ree himself, in his own memoir, also writes Pierre Sire** | **OK**, and the Ree memoir makes the English side even more clearly the outlier |
| 37 | "A Peugeot director was already arranging a loan to Ree's circuit." / "Repayable by the British Treasury after the war." | Act 4 | Foot p. 287 verbatim. The script correctly does **not** claim it was repaid | **OK** |
| 38 | "London's own nineteen forty six report says Peugeot were already toying with the idea." / "Sabotage their own factory, stop production, and prevent another disastrous British bombardment." | Act 4 | Bourne-Paterson verbatim. Near word for word, nothing added | **OK.** The best-sourced claim in the episode |
| 39 | "The family member behind the deal was Rodolphe Peugeot, the president's younger brother." | Act 5 | **Four independent supports.** Jonathan Ree's edition, biographies section: "Peugeot, Rodolphe (1902-1979): manager of the Peugeot factory at Sochaux"; Ree's own narrative, "Pierre Sire, who worked for Rodolphe Peugeot"; fr.wikipedia citing Marcot, "Frere cadet de Jean-Pierre"; Ascherson in the LRB. Ages confirm: Jean-Pierre 1896, Rodolphe 1902 | **OK.** Better sourced than the log claims |
| 40 | "Many books say Robert Peugeot. Robert was the elderly father, **and seriously ill**." | Act 5 | Father and 1941 handover **VERIFIED** (Robert 1873-1945, five children incl. Jean-Pierre 1896 and Rodolphe 1902; "age de 70 ans, laisse la presidence a Jean-Pierre", July 1941). **"Seriously ill" NOT FOUND in any source I or my checks could reach**, including both fr.wikipedia articles the log names | **FIX** |
| 41 | "He composed a short personal message and asked for it on the BBC." / "A few nights later the BBC read out his sentence." | Act 5 | Foot p. 287 verbatim. The script speaks no words of the phrase, which is right, because the attested phrase is contested and appears attached to two or three different signals | **OK** |
| 42 | "Including the plant's chief electrician and the foreman of the machine shop." | Act 5 | Foot p. 287 for the foreman, with "tank turret" correctly dropped; Bourne-Paterson for the chief electrician. No saboteur named | **OK** |
| 43 | "Ree walked through the plant once, to see it. He never went back." | Act 5 | Foot p. 287 verbatim | **OK** |
| 44 | "The postwar verified list records a three month stop." | Act 5 | **Foot Appendix G, read directly**: 5 November 1943, three months' stop, note "first 'blackmail' operation" | **OK** |
| 45 | "Late November. Ree calls at the house of a schoolmaster **in Sochaux**." | Act 6 | The house was **14 rue de Belfort, Vieux-Charmont**, home of the teacher Jean Hauger. **Bourne-Paterson miscalls it Sochaux and that is where the error comes from.** Date 28 November per Ree, 27 November per Bourne-Paterson | **FIX**, small |
| 46 | "Ree broke a bottle over the German's head. The German emptied his magazine." | Act 6 | Ree verbatim: "grasping the bottle by the neck, I smashed it over his head", then "I immediately heard six shots. He had emptied his pistol." **Bottle first, then shots**, which is the order the script has | **OK** |
| 47 | "Ree felt nothing and assumed the pistol was loaded with blanks." | Act 6 | Bourne-Paterson: "although Henri felt nothing at the time". Ree's own blanks thought is retrospective, in the copse: "those bullets weren't blanks after all" | **NOTE.** A fair gloss, not literally his in-the-moment thought. Not worth a fix |
| 48 | "described in the official history as a fantastic fist fight" | Act 6 | **Foot p. 288 verbatim**, and the script attributes rather than asserts | **OK** |
| 49 | "**Ree crossed a garden, a wall, a field and a small stream.**" / "He reached a house about three kilometres away." | Act 6 | This is Bourne-Paterson's wording and it is **the understated version**. Ree's own account: waded a flooded ditch, forced a bramble hedge, three fields to a copse, then **swam the River Allan, swollen with autumn rain**, to Etupes, "about three miles away" | **FIX** |
| 50 | "**The retellings have him swimming a river and crawling four miles. They embellished.**" | Act 6 | **Half wrong, and it is the half that matters.** **He did swim a river.** The embellishment is the four-mile crawl through forest and the "shot four times: lung, arm, shoulder, side" garble. Ree: "One bullet had gone into my shoulder, another into my chest, but the other four had simply grazed me" | **FIX. A correction that is itself an error** |
| 51 | "He was badly wounded." | Act 6 | Two penetrating rounds, four grazes. The script speaks no count, correctly | **OK** |
| 52 | "December. He was smuggled into Switzerland, **reportedly in cars lent by Peugeot**." | Act 6 | December **VERIFIED** (1 December out, hospital at Porrentruy 2 December). **The cars are CONTRADICTED.** Jonathan Ree's chronology: carried to a **PTT post office van**, driven by Pierre Lavigne to Delle, then walked across after dark by four named young men. Peugeot's vehicle contribution is separate and earlier, a *laissez-passer et vehicule* for circuit work | **FIX** |
| 53 | "The Germans shipped in replacement machine tools. Stockbroker blew one up on the lorry." / "Still in the yard. Waiting to be unloaded." | Act 7 | **Foot p. 439 verbatim** | **OK** |
| 54 | "The verified list records that happening three separate times." | Act 7 | **Verified by me off Appendix G directly.** Three rows carry "Replacement machine tools destroyed on arrival from Germany" | **OK** |
| 55 | "Three weeks. Five weeks. Several months. Output cut to forty per cent." | Act 7 | **Appendix G, all four, read directly**: about 15 January 1944 three weeks; 10 February several months; 10 February five weeks; 15 March output cut to 40 per cent | **OK** |
| 56 | "March nineteen forty four. Bomber Command schedules a second raid on Sochaux." | Act 7 | Bourne-Paterson, the RAF "were successfully dissuaded from making another attack"; cancoillotte independently on London's March 1944 pressure and the 9 March order to destroy the plant's main transformer | **OK** |
| 57 | "**The circuit sent London photographs of the damage.** London cancelled the raid." | Act 7 | The cancellation is fine. **The photographs rest on one unreferenced fr.wikipedia sentence**, and cancoillotte, covering the same episode in more detail, says it was a **technical dossier** proving aviation production could not start for months. Mirrors are not corroboration | **FIX** |
| 58 | "The Michelin family were offered the same arrangement and refused it." / "So the Royal Air Force damaged it severely instead." | Act 7 | **Foot p. 288 verbatim**, and it is his own example against his own side | **OK on fact.** See the tone section on placement |
| 59 | "**October nineteen forty three. The Gestapo arrested twenty four resistants in one sweep.**" | Act 8 | Sweep real, Fouillette's arrest attested. **The number 24 is Chatelot alone**, one unfootnoted memoir, and it is asserted flat. Other accounts of the same autumn rollup give very different figures | **FIX** |
| 60 | "**February** nineteen forty four. Eric Cauchi, Ree's sub agent, shot **by the Gestapo**." | Act 8 | Foot p. 371, "shot by the Gestapo in a cafe brawl on 6 February". **Ree's own circuit account gives 28 January 1944**, and has Cauchi shot in the back by a **factory sentry** as he ran out of the Cafe Grangier, not by the Gestapo inside. A contemporaneous photograph caption in the book reads "January 1944" | **FIX** |
| 61 | "**The Gestapo took seven or eight directors from a meeting.**" | Act 8 | **CONTRADICTED, and the script picked the two highest figures.** Marcot, the standard academic treatment, says **five**, and a fourth source names those five. Chatelot and mirebalais say seven; fr.wikipedia says eight deported. The best-sourced number is the one the script excludes | **FIX** |
| 62 | "One of them was Auguste Bonal, the director of stamping at the plant." / "sports director of the town's football club" | Act 8 | FC Sochaux's own club history, "directeur de l'Usine d'Emboutissage de Peugeot"; Chatelot; fr.wikipedia. Sports director July 1941 to June 1943 | **OK** |
| 63 | "German troops shot him beside a road in April, nineteen forty five." / "Two weeks before the German surrender." | Act 8 | Marched out of Schomberg 18 April 1945, shot near Bad Waldsee **23 April 1945**. 23 April to 8 May is fifteen days. The script gives the month only | **OK** |
| 64 | "The town's stadium carries his name now." | Act 8 | Stade Auguste-Bonal, renamed July 1945, on the club's own history | **OK** |
| 65 | "That autumn the Germans stripped Sochaux anyway. Machines and transformers, onto trains, gone." | Act 8 | Event verified by fr.wikipedia and mirebalais independently of Chatelot. **The 2,500-wagon figure is Chatelot alone and the script speaks no number** | **OK**, and the restraint is the right call |
| 66 | "The official historian's own verdict is only moderately good." | Outro | **Foot verbatim, p. 434 in the linked scan** | **OK on the quote, see the page-number fix** |
| 67 | "All that sabotage in France used less explosive than one light bomber carried." | Outro | **Foot verbatim**: about 3,000 lbs, "considerably less than the load of a single light Mosquito bomber in 1944" | **NOTE.** Foot's list is the *confirmed* sabotage, so "all that sabotage" is very slightly loose. Contextually it reads as the sabotage under discussion. No fix required |

---

## Issues to fix

Every replacement below was word-counted by the same script used for the structural pass and **every one is inside the 14-word beat cap.** Deltas are stated per item and totalled at the end. Items 1 to 16 are blocking. Item 17 is recommended. Items 18 to 21 are documentation.

**1. "The nineteen thirties. Harry Ree is a schoolmaster, teaching modern languages at Bradford Grammar."** (Act 1) - **Wrong school. He was at Beckenham and Penge County School for Boys in South London from 1937, and did not reach Bradford Grammar until 1 September 1946, after the war.** Confirmed by his own edited papers and independently by an IWM catalogue record placing him teaching in Beckenham 1937 to 1940. - Replace with:

> **NARRATOR:** The nineteen thirties. Harry Ree is a schoolmaster, teaching modern languages in London.

Delta -1 word. Keep the VISUAL as it is; a generic classroom still fits.

**2. The three conscientious-objector beats.** (Act 1) - **"Nineteen forty. He registers as a conscientious objector." / "He agrees to serve, on condition that it is the National Fire Service." / "Nineteen forty one. He changes his mind and registers for military service."** All three rest on a single IWM catalogue line and are contradicted by Ree himself: "I'd given up being a conchie **before the fall of France**." His editor states flatly that he was not in a position to register as a conscientious objector, and the chronology has no tribunal, an enlistment as a gunner on **14 November 1940**, and the Intelligence Corps in April 1941. **The National Fire Service also did not exist until August 1941**, so the 1940 condition is an anachronism on its face. The act's spine survives, because the student pacifism and the change of mind are both documented. Only the false chronology goes. - Replace all three, in order, with:

> **NARRATOR:** As a student, Harry Ree was a committed pacifist.
>
> **NARRATOR:** He gave that up, by his own account, before France fell in nineteen forty.
>
> **NARRATOR:** November nineteen forty. He enlisted in the army as a gunner.

Delta +1 word across the three. Two VISUAL tags need swapping, and **neither is a reuse target**, so this is safe:

- Scene 12, currently the tribunal bench, becomes: **[VISUAL: A young man in nineteen thirties clothes speaking at a student debating society meeting.]**
- Scene 13, currently the fireman with the hose, becomes: **[VISUAL: A newspaper front page lying on a table announcing the fall of France in nineteen forty.]**
- Scene 14, the recruiting desk with the enlistment form, **stays as it is** and now fits better than before.

The act title "THE PACIFIST WHO CHANGED HIS MIND" still holds and does not change. So does the payoff line five beats later, "Which is roughly how a pacifist schoolteacher ended up in the Special Operations Executive."

**3. "Tank track shoes. Connecting rods. Cylinder heads. All of it for German tanks."** (Act 2) - Track shoes are solid. **Connecting rods and cylinder heads are Chatelot alone**, an unfootnoted local memoir, asserted here without a hedge, and "all of it for German tanks" overstates even Chatelot, who says *for the Wehrmacht*. - Replace with:

> **NARRATOR:** Tank track shoes. The heavy steel links that armoured vehicles run on.

Delta -1 word. This also does the viewer a favour, because "track shoes" means nothing to an English audience on first hearing. If the channel would rather keep the parts list, the honest alternative at the same length is "Tank track shoes. One local account adds connecting rods and cylinder heads." VISUAL unchanged.

**4. "Aircraft landing gear, and later on, parts for German aircraft as well."** (Act 2) - **The landing gear is contradicted.** Both French sources place landing-gear work at Sochaux **up to 1940 only**, as French Army work before the armistice. The script puts it inside a list introduced by "By nineteen forty three it was building whatever the German war economy asked for", which converts pre-occupation French production into a German order. - Replace with:

> **NARRATOR:** And later on, aero engine parts for the German air force as well.

Delta +1 word. This is now Foot's own formulation, "Focke-Wulf engine parts for the German air force", with the brand name dropped for TTS. Swap the VISUAL, which is scene 26 and not a reuse target:

- **[VISUAL: A crated aero engine component on a factory trolley beside other crated aircraft parts.]**

**5. "And light trucks. By one count, fifteen thousand of them went east to Russia."** (Act 2) - **The number cannot be right.** Chatelot's 15,463 petrol DMAs sent east exceeds total DMA production over the entire 1941 to 1944 run, about 15,306, and exceeds the German-commandeered share, about 13,779. "By one count" does not rescue a figure that contradicts the production total. - Replace with:

> **NARRATOR:** And light trucks. Around fourteen thousand of them were taken by the German army.

Delta 0 words. This is the well-attested figure, correctly scoped, and it drops a Russian-front precision that rests on a pretext story rather than a delivery ledger. VISUAL unchanged.

**6. The Bomber Command character line, "Big factory. Makes things for Germany. We will take care of it."** (Act 2, final beat) - **Tone failure by placement.** It is a comic character line in the script's own sarcasm zone, and it is the last thing the viewer hears before the act that kills 123 civilians. The production notes' claim that no joke sits before Act 3 is false. The content is fine; the register and the position are not. - Replace the whole line, speaker label included, with a straight narrator beat:

> **NARRATOR:** It was small, it was close to houses, and it needed hitting precisely.

Delta +1 word. This is drawn straight from Foot, "it was a small target that would need to be hit precisely if it was to be usefully damaged at all; and it was sited close to the railway station in a populous part of the town." It is a **better** act-out than the joke was, because it tells the viewer the disaster is coming instead of undercutting it. Keep the VISUAL, the two air staff officers in the map room, unchanged. **This also brings the character-voice count down to three, which makes the production notes' "three fake dialogue lines" sentence correct.**

**7. "Three hundred and thirty six were injured. That is the local French count."** (Act 3) - **The label is inverted.** 336 is Middlebrook's British-side figure and Middlebrook's alone; every French source gives about 250. The script attributes a British number to the French and presents a 250-versus-336 spread as settled. - Replace with:

> **NARRATOR:** That is the local French count. Hundreds more were injured that night.

Delta -1 word. The preceding beat, "A hundred and twenty three people were killed that night," is untouched, and "That is the local French count" now correctly attaches to the death figure, which genuinely is the French count. "Hundreds more" is true against 250, against 336 and against the 500 in the 2025 commemoration piece, and it commits to nothing. VISUAL unchanged.

**8. "Late November. Ree calls at the house of a schoolmaster in Sochaux."** (Act 6) - **Wrong place.** The house was at 14 rue de Belfort, Vieux-Charmont, the home of the teacher Jean Hauger. Bourne-Paterson miscalls it Sochaux and that is where the error entered. Neither Vieux-Charmont nor Montbeliard can be spoken, by the script's own TTS rule. - Replace with:

> **NARRATOR:** Late November. Ree calls at the house of a schoolmaster in the valley.

Delta +1 word. "In the valley" is true, is already established by Act 3's closing beat, and asserts nothing.

**9. The escape sequence, three beats.** (Act 6) - **"Ree crossed a garden, a wall, a field and a small stream." / "He reached a house about three kilometres away." / "The retellings have him swimming a river and crawling four miles. They embellished."** The script took Bourne-Paterson's understated version and then mocked the fuller one. **Ree's own account has him swimming the River Allan, swollen with autumn rain, to reach Etupes "about three miles away".** So the script calls a documented fact an embellishment, which is the worst category of error this channel can make: a correction that is itself wrong. The genuine embellishment is only the four-mile crawl through forest, plus the "shot four times: lung, arm, shoulder, side" garble, and the script already correctly avoids the second. - Replace the three beats, in order, with:

> **NARRATOR:** Ree went out the back, across fields, and swam a swollen river.
>
> **NARRATOR:** He reached a friendly house some miles away. He was badly wounded.
>
> **NARRATOR:** The retellings have him crawling four miles through a forest. That part is invention.

Delta +1 word across the three. Two VISUAL swaps, **neither a reuse target**:

- Scene 89, currently the garden, wall, field and narrow stream, becomes: **[VISUAL: A dark flat field running down to a wide river swollen with autumn rain.]**
- Scene 92, currently the book cover showing an agent swimming a river, becomes: **[VISUAL: A popular history book cover showing an agent crawling through a dark forest.]**

Note that this fix makes the beat land harder, not softer. The man swam a flooded river with a bullet in his chest.

**10. "December. He was smuggled into Switzerland, reportedly in cars lent by Peugeot."** (Act 6) - **The cars are contradicted by the best source.** Ree was carried to a **post office van**, driven by Pierre Lavigne to Delle, and walked across the border after dark by four named young men. Peugeot's vehicle contribution is a separate and earlier thing, a pass and a vehicle for circuit work. The "reportedly" hedge does not survive a direct contradiction. - Replace with:

> **NARRATOR:** December. He was driven out in a post office van and smuggled into Switzerland.

Delta +2 words. Swap the VISUAL, scene 93, not a reuse target:

- **[VISUAL: A snow covered Swiss border post with a striped barrier and one parked van.]**

**11. "The circuit sent London photographs of the damage. London cancelled the raid."** (Act 7) - **The photographs rest on one unreferenced fr.wikipedia sentence**, and cancoillotte, which covers the same episode in more operational detail, says the thing that changed London's mind was a **technical dossier** proving aviation production could not start for months. Its apparent corroborations are Wikipedia mirrors. The cancellation itself is fine and stays. - Replace with:

> **NARRATOR:** The circuit sent London proof of the damage. London cancelled the raid.

Delta 0 words. "Proof" is neutral between photographs and a dossier and is supported by both. Swap the VISUAL, scene 98, not a reuse target:

- **[VISUAL: A London desk with a thick evidence file spread open beside a cancelled operation order.]**

**12. The Michelin beat's position, "So the Royal Air Force damaged it severely instead."** (Act 7, final beat) - **Tone failure by placement.** This is Foot's own deadpan and the fact is verbatim correct, but the "So ... instead" is a karmic punchline and it is the last beat before the arrests and Bonal's death. - **Fix by reordering, not rewriting. Zero word cost and no line changes.** Move the two Michelin beats, currently scenes 99 and 100, to sit **before** the two raid beats, currently 97 and 98, so Act 7 ends on "The circuit sent London proof of the damage. London cancelled the raid."

That is also a better act, because it ends on the act's own title payoff instead of on an aside. After the move the reuse labels in Act 7 must be relabelled, since the indices shift:

- New scene 97, the burning Michelin tyre works, becomes the **first** occurrence and carries **no** reuse label
- New scene 98, the identical tyre works tag, becomes **(REUSE: scene 97)**
- New scene 99, the Halifaxes on the wet airfield, becomes **(REUSE: scene 38)**
- New scene 100, the London desk, carries no reuse label

Totals are unchanged: still 112 tags, still 11 reuses, still 101 unique generations. The outro's "Next time, the family who said no" teaser is unaffected, because it has its own beat and its own thumbnail visual.

**13. "October nineteen forty three. The Gestapo arrested twenty four resistants in one sweep."** (Act 8) - **Twenty four is Chatelot alone**, one unfootnoted local memoir, asserted flat in the straight act. The sweep and Fouillette's arrest are real; the count is not established, and other accounts of the same autumn rollup give very different figures. - Replace with:

> **NARRATOR:** October nineteen forty three. The Gestapo broke up much of the local network.

Delta 0 words. Swap the VISUAL, scene 101, not a reuse target, and check: the replacement is **not** byte-identical to scene 44's list-of-names tag, which ends ", no ornament at all", so it creates no accidental duplicate:

- **[VISUAL: A plain list of names typed on grey paper in flat even light.]**

**14. "February nineteen forty four. Eric Cauchi, Ree's sub agent, shot by the Gestapo."** (Act 8) - **Both the month and the agency are contested.** Foot p. 371 gives 6 February and the Gestapo. **Ree's own circuit account gives 28 January 1944**, and has Cauchi shot in the back by a factory sentry as he ran out of the Cafe Grangier, not by the Gestapo inside it. A contemporaneous photograph caption in his edited papers reads "January 1944". The organiser of the circuit outranks the official historian on his own men. - Replace with:

> **NARRATOR:** Early nineteen forty four. Eric Cauchi, Ree's sub agent, was shot and killed.

Delta 0 words. Swap the VISUAL, scene 102, not a reuse target, since the interior cafe now misplaces the death:

- **[VISUAL: A quiet French cafe exterior in flat daylight, one door standing open, nobody in frame.]**

**15. "March nineteen forty four. The Gestapo took seven or eight directors from a meeting."** (Act 8) - **Contradicted, and the script picked the two highest figures while excluding the best-sourced one.** Marcot, the standard academic treatment the script itself names two acts earlier, says **five**, and a fourth source names those five. Chatelot and one regional site say seven; fr.wikipedia says eight deported. This is an unresolved conflict presented as settled, in the human-cost act. - Replace with:

> **NARRATOR:** March nineteen forty four. The Gestapo took several directors straight from their weekly meeting.

Delta 0 words. "Several" covers five through eight and asserts none of them. "Weekly meeting" is a documented detail, "a la sortie de la reunion hebdomadaire des directeurs de l'usine", and it sharpens the picture at no risk. VISUAL unchanged; the boardroom with an empty chair at every place now reads even better.

**16. "Many books say Robert Peugeot. Robert was the elderly father, and seriously ill."** (Act 5) - **"Seriously ill" is untraceable.** I checked both fr.wikipedia articles the log names for it and neither mentions illness, heart attacks or a wheelchair. It appears to rest on the same single unfootnoted source whose wheelchair detail the writer correctly cut, which makes keeping it inconsistent as well as unsupported. It is also unnecessary, since the next beat already carries the handover. - Replace with:

> **NARRATOR:** Many books say Robert Peugeot. Robert was the father, and seventy years old.

Delta 0 words. The age is documented, "Robert Peugeot, age de 70 ans, laisse la presidence a Jean-Pierre", July 1941, and it does the same dramatic work. VISUAL already shows an armchair, so it needs no change.

**17. Recommended, not blocking: "He played what the French call the double game. He falsified production reports." and "He invented procedures to slow the work, and hid hundreds of men from conscription."** (Act 2) - The hiding of the refractaires is verified twice over. **The falsified reports and the invented procedures are fr.wikipedia alone**, summarising the paywalled Marcot, and cancoillotte independently describes something quite different, the direction supplying **real** production states to London through Ree. That is a different act and the two should not blur. - If applied, replace with:

> **NARRATOR:** He played what the French call the double game, and played it for years.
>
> **NARRATOR:** He hid hundreds of men from labour conscription, on Peugeot farms and woodlots.

Delta 0 words across the two. The second is now the strongest-sourced sentence in Act 2. If applied, swap the first VISUAL, scene 24, not a reuse target: **[VISUAL: A factory office desk stacked with German production orders and a full ashtray.]**

**18. Documentation: the header word count.** Line 3 says "1,401 narration words"; the true count is 1,402 and the production notes say 1,402. After the fixes above the count becomes **1,406**. Update the header, the production notes, and re-derive the timings.

**19. Documentation: the runtime and all ten act headers.** At 1,406 words the runtime becomes **8:53 at 158 wpm** and **8:07 at 173 wpm**, still 7 seconds clear of the 8:00 floor. Every act header timecode needs re-deriving from the new per-act word counts, and the reorder in fix 12 changes nothing about Act 7's total. Re-run the same check I did: each act's stated duration should equal its word count divided by 158, times 60, to within a second, and the ten must remain sequential and contiguous.

**20. Documentation: the Foot page citations.** The log and the SOURCES block cite the "only moderately good" verdict at **p. 438** and the explosive comparison at **p. 439**. In the Internet Archive scan the SOURCES block itself links, running heads place them at **p. 434** and **p. 436**, and p. 439 is a different passage entirely, the machine-tool-on-the-truck one, which Foot's own index confirms. Either correct the numbers to 434 and 436, or drop page numbers from those two entries and keep the appendix reference, which is correct at p. 505.

**21. Documentation: the IWM record and *A Schoolmaster's War*.** Two changes to the log:

- The IWM catalogue record for object 80008516 **does** name Rodolphe Peugeot, but the same record lists a different person entirely in its Interviewee field, twice places the Peugeot factory at Clermont-Ferrand, calls the November 1943 opponent a Gestapo agent rather than a Feldgendarme, and calls the V-1 drawings V-2. A summariser's paraphrase carrying four errors is not a citable identification. **Re-source the Rodolphe naming to Jonathan Ree's edition, to Ascherson and to Marcot via fr.wikipedia**, all of which carry it, and demote the IWM record to supporting colour.
- The SOURCES block says of *A Schoolmaster's War*, "Introduction accessed; full text not". **The full text is available and it contradicts the script in six places**, which is where fixes 1, 2, 8, 9, 10 and 14 come from. Update the note, and read it before the next SOE episode.

**Net effect of the sixteen blocking fixes: +4 narration words, 1,402 to 1,406.** No beat exceeds 14 words. No reuse target is touched except the deliberate relabelling in fix 12. Tag totals, reuse count and unique generations are all unchanged.

---

## Cold read notes

Read aloud, start to finish, at pace, listening for what a viewer hears rather than what the page says.

**What works, and should not be touched in the fix pass.**

The cold open is the best thing in the script. "Someone told him no" as a standalone beat, then the reveal that the someone was a factory director, is a clean hook and it does not oversell. The four-word beat rhythm carries the whole first two acts and the sarcasm lands where the writer intended, particularly the bureaucratic understatement in Act 2 and the SOE house-style jokes in Act 4. The Act 4 to Act 5 transition, from the plan to the man who could authorise it, is the cleanest structural seam in the episode.

Act 3 is genuinely good and genuinely restrained. It reads slower than the acts around it without any device beyond shorter sentences and longer visual holds, which is exactly right. Do not add anything to it. The two adjacency fixes above exist so that the acts on either side stop undercutting it.

The myth-inversion in the outro is the strongest content decision in the script, because it is the rare case where the honest version is more interesting than the legend. Keep it exactly as written, and keep it resting on the SOE's own 1946 language rather than on the narrator's assertion. The "only moderately good" landing is the correct ending and it is not triumphalist.

**What a viewer will trip over.**

Three terms will not survive an English TTS read as written and the VOICE NOTE does not cover them: **Sire** will be read as the English word "sire", **Cauchi** has no obvious English reading, and **Petainism** will be mangled. **Bonal**, **Henri**, **Michelin** and **Jean Pierre** are also uncovered. Add all seven to the VOICE NOTE list before the read.

"Track shoes" means nothing to a general audience on first hearing and the script never explains it. Fix 3 above solves this incidentally by giving the term its own gloss in the same breath.

The Act 2 production list is the one place where the beat rhythm turns into a shopping list and the viewer's attention drops. It is four consecutive noun-fragment beats. Fixes 3, 4 and 5 shorten and vary that run, which helps, but if there is appetite for one more trim, cutting one item entirely would improve the act.

**One pacing observation.** Act 8 is the shortest act and it is carrying the most names. After the fixes it carries fewer hard numbers, which will make it read faster still. Consider holding the Bonal visual a beat longer in the edit rather than adding words.

**What I could not check.** Two things in the script are unverifiable rather than wrong, and both are already hedged correctly in the spoken narration, so they stay: the exact mechanism by which the loan repayment guarantee was communicated, and whether the stripped-plant claim covers the whole works or only part of it. Neither is asserted flat. This is the right treatment and it is worth noting that the writer got these two right unprompted.

---

## Summary of the verdict

Structurally the script is clean. All ten structural checks pass, including the eleven reuse targets, which I resolved individually and confirmed byte-identical and backward-pointing, the 112/11/101 tag accounting, the zero-dash requirement, the fourteen-word beat cap, the section order, the act hooks, and the runtime, which clears the mid-roll floor at both the measured and the fast rate. Nine of the thirteen episode-specific tests pass outright, including the ones that carried the most risk: no second RAF raid, the number trap, the Foot-versus-Appendix-G handling, the myth-inversion calibration, the cut and hedge list, and the four character-voice lines, none of which invents a position.

It fails on verification. Sixteen claims are blocking. The pattern across them is consistent and worth naming for the next pass: the script is over-precise. Nearly every failure is a specific number, name, place or date carried by a single source, usually the same unfootnoted local memoir, and stated flat in narration where a range or a plainer formulation would have been both true and just as good on screen. Two of them, the Bradford school and the conscientious-objector chronology, are contradicted by Ree's own words in a book the SOURCES block wrongly records as unavailable. One, the fifteen thousand trucks, fails on arithmetic against the factory's own production total. One, "They embellished", is a correction that is itself an error, which is the single worst failure mode available to a channel whose brand is accuracy. And two comedy beats sit directly against the two human-cost acts, which is a tone failure by the standard the script itself sets in its production notes.

None of this is structural and none of it requires a rewrite. Every one of the sixteen has an exact replacement above, word-counted, inside the cap, with the VISUAL swaps specified and the reuse targets checked. The total cost is four words.

**Loop 1 outcome: fail.** Sixteen blocking issues, each with exact replacement wording, total cost four words.

---
---

# RE-GATE (loop 2)

**Date:** 3 September 2026. **Scope:** the revised `script.md`, checked against the sixteen blocking fixes issued in loop 1, then re-audited for collateral damage and for the accuracy of the rewritten documentation. Every structural number below was produced by my own script on the current file, not taken from the writer's report.

## 1. Did the sixteen land

All sixteen landed **verbatim**, character for character, in the wording I supplied. No fix was paraphrased, softened, or partially applied.

| # | Fix | Landed | Line |
|---|---|---|---|
| 1 | Bradford Grammar to "in London" | Verbatim | 64 |
| 2 | Three conscientious-objector beats replaced | Verbatim, all three, in order | 68, 72, 76 |
| 3 | Track shoes gloss | Verbatim | 124 |
| 4 | Landing gear to aero engine parts | Verbatim | 128 |
| 5 | Fifteen thousand trucks to "around fourteen thousand" | Verbatim | 132 |
| 6 | Bomber Command character line to straight narrator beat | Verbatim, speaker label removed | 172 |
| 7 | Injured figure removed | Verbatim | 208 |
| 8 | Sochaux to "in the valley" | Verbatim | 368 |
| 9 | Escape sequence, three beats | Verbatim, all three, in order | 392, 396, 400 |
| 10 | Peugeot cars to post office van | Verbatim | 404 |
| 11 | Photographs to proof | Verbatim | 444 |
| 12 | Act 7 reorder | Applied as specified | 428 to 444 |
| 13 | Twenty four arrests removed | Verbatim | 452 |
| 14 | Cauchi date and agency removed | Verbatim | 456 |
| 15 | Seven or eight directors to "several" | Verbatim | 460 |
| 16 | Robert "seriously ill" to "seventy years old" | Verbatim | 316 |

**The VISUAL swaps.** I specified nine; all nine are in place, each in the exact wording given:

- Scene 12, student debating society (was the tribunal bench)
- Scene 13, newspaper announcing the fall of France (was the fireman)
- Scene 26, crated aero engine component (was the landing-gear leg)
- Scene 89, dark field running down to a swollen river (was the garden, wall and narrow stream)
- Scene 92, book cover, agent crawling through a dark forest (was the agent swimming)
- Scene 93, snow covered Swiss border post with a parked van (was the Peugeot cars)
- Scene 100, London desk with a thick evidence file (was the photographs)
- Scene 101, plain list of names, "twenty four" removed from the tag (and confirmed again here: it is **not** byte-identical to scene 44's tag, which ends ", no ornament at all", so no accidental duplicate was created)
- Scene 102, cafe exterior (was the interior)

**One VISUAL change beyond my list.** Scene 91 is now "A farmhouse window with a lamp lit in it, seen from a dark field some way off." It previously depicted the house three kilometres away. This is a consequence of fix 9's second beat, it is not a content claim, it is not a reuse target, and it is correct. **Approved, not a defect.**

**One narration change beyond my list.** None. I diffed by reading all 112 beats in sequence against my loop-1 claim table and my loop-1 quotations. Every beat is either one I quoted and passed in loop 1, or one of my sixteen replacements. **No unreviewed narration was introduced.**

Note that I could not run a byte diff: `script.md` is untracked in git and the loop-1 text was not recoverable from the session transcript. The check above is a full manual re-read of every beat, which is what the situation allows and is what I did.

**Fix 17, the recommended non-blocking one** (the double-game and refractaires beats in Act 2, lines 148 and 152) was **not applied**. That is correct and expected; it was never part of the sixteen. It remains outstanding as a soft item, unchanged in force: the falsified reports and the invented procedures are fr.wikipedia summarising a paywalled Marcot, and the log row still labels them "Verified in substance" off an abstract. Not blocking.

## 2. Structural checks, re-run

Method: one Python pass over `script.md`. Narration is every line beginning `**NARRATOR:**` or `**X (character voice):**` between the COLD OPEN header and the PRODUCTION NOTES header, with the speaker label stripped. VISUAL and TITLE tags, headers, blockquotes and the notes are excluded.

| Check | Requirement | Writer reports | I measure | Result |
|---|---|---|---|---|
| Narration words | 1,390 to 1,410 | 1,406 | **1,406** | Pass |
| Spoken beats | 1:1 with tags | 112 | **112** | Pass |
| VISUAL tags | 112 | 112 | **112** | Pass |
| Beats over 14 words | none | none | **none**, longest 14, mean 12.55 | Pass |
| REUSE tags | 11 | 11 | **11** | Pass |
| Unique generations | 101 | 101 | **101** | Pass |
| Em-dashes | zero | zero | **zero** in the whole file | Pass |
| En-dashes | zero | not reported | **zero** in the whole file | Pass |
| Camera moves | none | none | **none** | Pass |
| Brackets or stage directions inside spoken lines | none | not reported | **none** | Pass |
| Runtime at 158 wpm | n/a | 8:53 | **8:53.9** | Pass |
| Runtime at 173 wpm | over 8:00 | 8:07 | **8:07.6**, clear by 7.6 s | Pass |
| Nine required sections in order | yes | yes | **yes** | Pass |
| Every act ends on a hook | yes | yes | **yes**, checked act by act | Pass |

**The eleven reuse targets, re-resolved individually.** This was the loop-1 weak point and the reorder touched two of them, so I resolved all eleven again from scratch by ordinal scene index, comparing the tag text with the REUSE marker stripped:

| Reuse at | Points to | Backwards | Byte-identical | Target itself a reuse |
|---|---|---|---|---|
| 50 | 5 | yes | yes | no |
| 58 | 10 | yes | yes | no |
| 61 | 43 | yes | yes | no |
| 64 | 8 | yes | yes | no |
| 69 | 9 | yes | yes | no |
| 78 | 3 | yes | yes | no |
| 79 | 6 | yes | yes | no |
| 80 | 7 | yes | yes | no |
| **98** | **97** | yes | yes | no |
| **99** | **38** | yes | yes | no |
| 109 | 51 | yes | yes | no |

**Both relabelled targets resolve correctly.** 98 points at the first occurrence of the burning tyre works, which now carries no reuse label of its own, and 99 points back at the Halifaxes on the wet airfield in Act 3. No reuse points at another reuse, none points forward, and every pair is byte-identical. Totals hold at 112 tags, 11 reuses, 101 unique generations.

**Per-act word counts and the act header timecodes.** The writer's ten figures are exactly right, and every header re-derives cleanly at 158 wpm:

| Section | Words | Header says | Derives to | Drift |
|---|---|---|---|---|
| COLD OPEN | 123 | 0:00 - 0:46 | 0:00 - 0:47 | 0.7 s |
| ACT 1 | 152 | 0:46 - 1:44 | 0:47 - 1:44 | 0.4 s |
| ACT 2 | 193 | 1:44 - 2:57 | 1:44 - 2:58 | 0.7 s |
| ACT 3 | 198 | 2:57 - 4:12 | 2:58 - 4:13 | 0.9 s |
| ACT 4 | 183 | 4:12 - 5:22 | 4:13 - 5:22 | 0.4 s |
| ACT 5 | 168 | 5:22 - 6:26 | 5:22 - 6:26 | 0.2 s |
| ACT 6 | 129 | 6:26 - 7:15 | 6:26 - 7:15 | 0.2 s |
| ACT 7 | 106 | 7:15 - 7:55 | 7:15 - 7:55 | 0.4 s |
| ACT 8 | 104 | 7:55 - 8:34 | 7:55 - 8:35 | 0.9 s |
| OUTRO | 50 | 8:34 - 8:53 | 8:35 - 8:54 | 0.9 s |

Sum 1,406. Contiguous, sequential, no gaps or overlaps, maximum drift 0.9 seconds. **Pass.**

**One structural defect, and it is the only thing standing between this script and a clean pass.**

**Line 445 has no blank line before the `---` that closes Act 7.** The reorder moved the London-desk beat to the end of the act and the separating newline was lost. In Markdown, a `---` on the line directly after a text line makes that text line a setext H2 heading, so `**NARRATOR:** The circuit sent London proof of the damage. London cancelled the raid.` renders as a section header rather than a narration beat. Every other one of the ten act boundaries in the file has the blank line. My beat parser reads the raw line and so still counted it, but a build agent walking headings will not.

Fix, exactly: **insert one blank line between line 444 and the `---` on line 445.** No text changes, no word-count change.

## 3. Tone, re-checked beat by beat

**Act 3 (198 words, 15 beats) contains no joke.** Confirmed by reading every beat. The closest thing to wit is the closing line, "Everybody in that valley now had a very direct opinion about British bombing," which is grim understatement rather than a gag and is the same line I passed in loop 1.

**Act 8 (104 words, 8 beats) contains no joke.** Confirmed.

**The beat before Act 3** is now line 172: "It was small, it was close to houses, and it needed hitting precisely." Straight, no speaker label, and it is a better act-out than the joke it replaced because it tells the viewer the disaster is coming. **Adjacency violation cleared.**

**The beat before Act 8** is now line 444: "The circuit sent London proof of the damage. London cancelled the raid." Straight. **Adjacency violation cleared.**

**The beat after Act 3** is line 248, "Now. Here is where nearly every version of this story gets the order wrong." A signpost, not a joke. **The beat after Act 8** is line 487, "So did sabotage beat bombing? The official historian's own verdict is only moderately good." Not a joke.

**Did the reorder push a joke into a new adjacency?** No. Act 7 now runs: machine tools on the lorry, the yard gag, the German management line, the appendix routine, the stoppage column, Michelin refused, "So the Royal Air Force damaged it severely instead," the scheduled raid, the cancellation. The karmic punchline now sits at scene 98 with two straight beats after it, so it is no longer adjacent to Act 8 and it is not adjacent to Act 3. No new adjacency anywhere in the file.

**Are the early acts still funny after three of Act 1's beats were replaced?** Yes, though Act 1 is measurably drier than it was. The replacement traded a comic set piece, the tribunal and the fire service, for a factual three-beat run, so Act 1's laughs now rest on the accent gag, the crossed-out flowchart and the payoff line "Which is roughly how a pacifist schoolteacher ended up in the Special Operations Executive." That still lands, and the cold open is untouched and carries six. The production notes' recount, 29 jokes with a front-loaded distribution of 6, 5, 3, none, 5, 3, 3, 4, none, none, sums correctly and matches what I count on the page. The stated densities also check: 468 words across the comic front carrying 14, and 586 words across Acts 4 to 7 carrying 15.

## 4. The documentation audit

I re-read the ACCURACY NOTE, the VOICE NOTE, the PRODUCTION NOTES, all sixty-odd FACT-CHECK LOG rows and the whole SOURCES block, and I checked the rewritten rows against the sources themselves rather than against the writer's description of them. Foot was re-read from the Internet Archive scan directly; the web sources were re-fetched.

### 4a. What is right, verified at the source

**Foot's page numbers are now correct, and I confirmed both from the running heads of the scan the SOURCES block itself links.**

- Page 434 carries, verbatim: "The results of industrial sabotage in France were only moderately good in terms of damage and delay to enemy war production." It sits between the running heads "434 STRATEGIC BALANCE SHEET" and "SOE AND BOMBER COMMAND 435". **The outro rests on this and the citation now holds.**
- Page 436 carries, verbatim: "about 3,000 lb; considerably less than the load of a single light Mosquito bomber in 1944; only a quarter in fact, of the weight of a single Tallboy bomb." It sits between the heads "436 STRATEGIC BALANCE SHEET" and "SOE AND BOMBER COMMAND 437".
- Page 439 is, as the log now says, a different passage entirely: the replacement machine tool destroyed "while it was actually waiting to be unloaded from a truck in the factory yard; and all the replacement work had to be gone through again." It sits before the head "440 STRATEGIC BALANCE SHEET". **This also independently confirms the Act 7 opening beats, which are close paraphrase of Foot.**
- Appendix G, "Industrial Sabotage", begins at p. 505. Foot's own cross-references elsewhere in the text point to pages 507, 508 and 513 inside it. Correct.

**Foot's p. 287 passage is verbatim as the log describes it**, including "some hundreds of townspeople were killed", the 14 July date the script rejects, "tank turrets for the German army and Focke-Wulf engine parts for the German air force", the Treasury loan already in negotiation, "the damage that would ensue when the RAF returned to do the job properly", the BBC message, "the foreman of the tank turret machine shop", the single reconnaissance, and the p. 287 overstatement the script refuses. Foot's index confirms "Cesar, see Ree" and the DSO and OBE, and the Southgate reception near Tarbes is on p. 286.

**The Michelin row is verbatim correct.** Foot, pp. 287 to 288: "the Michelin family refused to follow the Peugeots' example and assist in dislocating their tyre factory at Clermont-Ferrand, and the RAF consequently damaged it severely." "A fantastic fist fight with a Feldgendarme" is likewise Foot's own phrase, and the narration correctly attributes it to the official history rather than speaking it as description.

**The National Fire Service argument holds.** The NFS was created in August 1941, so it cannot have been the condition of a 1940 registration. The log's reasoning is sound.

**Robert Peugeot's age is right, and it is right for a reason the log does not state.** He was born 21 July 1873, so he was seventy in November 1943, which is when Act 5 is set. **Note for the record, because a future editor will otherwise "fix" it:** the French source that gives "age de 70 ans" attaches that age to the July 1941 handover, where he was in fact 68. The script's "seventy years old" is correct on its own terms and the French source's is not. The log should say so.

**Marcot's citation is exact.** "La direction de Peugeot sous l'Occupation: petainisme, reticence, opposition et resistance", *Le Mouvement social* no. 189, 1999, pp. 27 to 46, JSTOR 3780203. Title, journal, issue, pagination and identifier all check.

**The Rodolphe identification itself holds, and it is not blocking.** Ascherson's LRB review says, verbatim: "He was already in touch with the manager at Sochaux, Rodolphe Peugeot, who was committed to the Resistance, when in July 1943 the RAF unexpectedly attacked the factory with 165 Halifax bombers." That is a named credentialed historian, in a reputable outlet, writing from the primary papers, and it independently corroborates the 165 Halifaxes as well. fr.wikipedia names him too: "Ce dernier lui fait rencontrer Rodolphe Peugeot, resistant et cadre dans l'entreprise familiale." Bradford Grammar School's own July 2020 article, built on an interview with Jonathan Ree, names him again: "persuading Rodolphe Peugeot, the son of the Peugeot factory owner, to sabotage the family premises at Sochaux". And the genealogy is solid: Rodolphe, born 2 April 1902, and Jean-Pierre, born 1896, were both sons of Robert, and fr.wikipedia calls Rodolphe "frere cadet de Jean-Pierre". **So "the family member behind the deal was Rodolphe Peugeot, the president's younger brother" is safe, and the script is also right to say "the family member behind the deal" rather than giving him a job title, because the sources call him the manager, the owner, a cadre and the head of a different Peugeot company respectively.** The identification is not what fails here. The citation attached to it is.

**The production notes' own arithmetic all checks.** 29 jokes distributed 6, 5, 3, none, 5, 3, 3, 4, none, none sums to 29 and matches the page. The comic front is 468 words carrying 14, and Acts 4 to 7 are 586 words carrying 15. Mean beat length 12.55, longest 14, shortest 7 ("Five Halifax crews did not come home."). The reuse table's eleven rows match the eleven reuses in the file. The three character-voice lines are now genuinely three.

### 4b. Rows that overstate their support

This is where the pass fails, and it fails in the same way the coordinator predicted. **The narration is clean. The documentation is not.** Four rows cite sources for things those sources do not say, and one of them cites a source that says the opposite. None of these changes a spoken line. All of them would mislead a build agent, and two of them sit in the SOURCES block that ships in the YouTube description.

**D1. The Bradford Grammar row cites AIM25 for the opposite of what AIM25 says, and the 1946 date is wrong.**

The row reads: "**Bradford Grammar is 1946 and postwar**, per *A Schoolmaster's War* and the AIM25 archival description; an earlier draft had it in the 1930s on a misreading of en.wikipedia."

Three things are wrong with that sentence.

- **AIM25 does not say Bradford Grammar is postwar.** Its biographical history is a compressed career list: Institute of Education 1936 to 1937, then "He went on to become a language master at Bradford Grammar School and, after gaining a distinguished war record for his activities with the French resistance, was headmaster of Watford Grammar School." It attaches **no date** to Bradford, omits Beckenham entirely, and does not place Bradford either before or after the war. It is silent, not corroborative. Citing it in support of "1946 and postwar" is citing a source for something it does not contain. https://atom.aim25.com/index.php/ree-harry-alfred-1914-1991-2
- **en.wikipedia is not a misreading, it is a positive assertion, and it is contradicted by its own footnote.** Verbatim: "In 1937 he became a language master at Bradford Grammar School, and later at Beckenham and Penge County School for Boys." That sentence is footnoted to *The Fullerian* 2017-18, the Watford Grammar School magazine, which actually says the opposite: "At the start of the Second World War, Harry Ree was a French teacher at Beckenham and Penge Grammar School", and, of the postwar years, "that was what he returned to, first as a teacher at Bradford Grammar School and then as Headmaster of Watford Grammar School for Boys in 1951." **So en.wikipedia is simply wrong here, and the row's instinct was right even though its citation was not.** The row should say that, rather than calling it a misreading.
- **1946 is asserted flat and it is contested.** *A Schoolmaster's War* does give it twice, in the Chronology at "1 September: HR resumes his profession as teacher of French and German at Bradford Grammar School" and in the Introduction. But **Bradford Grammar School's own history, published July 2020 and built on an interview with Jonathan Ree, says "He went back to his teaching career, joining BGS in 1949 where he worked until 1951."** The school's dated record of its own staff against the book's chronology is an unresolved three-year conflict, and the row states one side as settled. https://www.bradfordgrammar.com/bgs-schoolmasters-double-life-in-churchills-secret-army/

**The narration survives all of this, and I want to be exact about why.** **Three independent sources put him in London, and one of them is an archival catalogue record.**

- IWM Sound Archive catalogue no. 10858, object 80010635, description verbatim: "British civilian school teacher in **Beckenham, London 1937-1940**". I had that record confirmed as the same man, not a different Harold Ree, from IWM's own linking fields: its Associated items entry is "Private Papers of Captain H A Ree DSO OBE", and its Associated people list includes Francis Cammaerts, the agent Ree recruited. It is also the exact reference en.wikipedia itself cites, as "Imperial War Museum, Sound Archives, 10858/2", for the conscientious-objector claim the script cut.
- *A Schoolmaster's War*, Introduction: "in 1937 he started work as a teacher of French and German, not in an elite institution but at **Beckenham and Penge County School for Boys in South London**." Its list of illustrations includes "HR in his classroom at Beckenham and Penge County School, 1938", and its 1940 chronology has him taking temporary leave from Beckenham School to enlist.
- *The Fullerian* 2017-18: "At the start of the Second World War, Harry Ree was a French teacher at **Beckenham and Penge Grammar School**."

**So "teaching modern languages in London" is carried by three independent sources, one archival, and contradicted by none. Fix 1 was correct and the spoken line stays untouched.** It is only the row underneath it that has to change.

**D2. The Rodolphe row's re-attribution does not hold as written, though the identification does.**

The row says the naming "rests on **Jonathan Ree's edition of his father's papers, Ascherson in the LRB, and Marcot through fr.wikipedia citing Loubet.**" Two of those three fail.

- **Ascherson holds.** Verified verbatim, above.
- **"Marcot through fr.wikipedia citing Loubet" is false.** The fr.wikipedia article carries exactly three reference tags in its entire wikitext. Loubet p. 242 is attached to the May 1940 triumvirate sentence. Marcot 1999 is attached to the July 1941 presidency handover sentence. autocult.fr is attached to the closing V1 sentence. **The Harry Ree and Rodolphe Peugeot passage carries no citation at all.** Marcot and Loubet appear only in the general bibliography. Saying the identification reaches us "through fr.wikipedia citing Loubet" describes a footnote that does not exist.
- **Jonathan Ree's edition is unverified.** The book is not previewable on Google Books, is not on archive.org, and is paywalled on JSTOR. Two long reviews that do discuss the Peugeot operation, in the Literary Review and the New Statesman, name nobody. Nobody in this pipeline has seen the inside of that book on this point.

**The identification is still safe**, because Ascherson carries it, because the IWM catalogue summary of Ree's own oral history names Rodolphe twice (in the reel description, "Rodolphe Peugeot's hearing of authentication of Harry Ree, via British Broadcasting Corporation broadcast", and again in Associated people), because fr.wikipedia names him, and because Bradford Grammar School's article built on an interview with Jonathan Ree names him. **Four independent lines. Not blocking.** But the row has to say which four.

**D3. The ACCURACY NOTE re-elevates the IWM record that the log two pages later demotes, and mislabels it.**

ACCURACY NOTE point 6 reads: "**The contact is Rodolphe Peugeot**, per Ree's own IWM oral history". The FACT-CHECK LOG row says the opposite, that the IWM record "was demoted at the QA gate from load-bearing to supporting colour" and that "the interview audio itself was never heard". Both cannot stand. The ACCURACY NOTE is the first thing a build agent reads, and as written it cites the content of a recording nobody has listened to.

For the record, my loop-1 finding about that record is now confirmed exactly. IWM object 80008516 carries **four errors**: its Interviewee field names "Hotz, Joan Willison" rather than Ree; it twice places the Peugeot factory at Clermont-Ferrand, which IWM's own private-papers record contradicts by putting the sabotage "in Doubs"; it calls the November 1943 opponent a "Gestapo agent" where Foot says Feldgendarme; and it calls the drawings "German V2 Rocket" where the research has V-1. The demotion in the log is right. The ACCURACY NOTE has to match it.

**D4. The Cauchi row is now contradicted by a Tier 1 source neither pass had found.**

The row says: "***A Schoolmaster's War* gives 28 January and a factory sentry, not the Gestapo**, which is Ree's own account of his own sub-agent", set against Foot's 6 February.

**The National Archives personnel file settles the date against the January version.** TNA reference **HS 9/281/5**, catalogue description verbatim: "Eric Joseph CAUCHI, aka Louis Jean CAUDRON, aka PEDRO, aka JEAN, aka STOCKBROKER, aka MESSENGER - born 11.08.1917, **died 05.02.1944**". https://discovery.nationalarchives.gov.uk/details/r/C9173449

That is SOE's own personnel record, it agrees with Foot to within a day, and it is better evidence than an editor's memoir date. The row as written tells a build agent that Ree's account outranks the official historian here. It does not.

**The narration is unaffected and remains correct.** "Early nineteen forty four. Eric Cauchi, Ree's sub agent, was shot and killed." is true against 28 January, 5 February and 6 February alike, and asserts neither a date nor an agency. **Fix 14 was right, and it is now better justified than when I issued it.** Only the row changes.

**D5. Two smaller misattributions, non-blocking but worth correcting in the same pass.**

- The Bomber Command row ends "The targeting itself is the Bomber Command War Diaries." It is not. The replacement beat, "It was small, it was close to houses, and it needed hitting precisely", is a close paraphrase of **Foot, p. 287**: "it was a small target that would need to be hit precisely if it was to be usefully damaged at all; and it was sited close to the railway station in a populous part of the town". The War Diaries cover the raid, not the targeting rationale.
- The codename row cites "en.wikipedia, AIM25, and Foot's index" for "Captain, Intelligence Corps, SOE F Section, codename Cesar, field name Henri". **AIM25 supports none of it**; it gives no rank, no corps and no codename. Foot's index gives "Cesar, see Ree" and the DSO and OBE but no rank. Drop AIM25 from that row.

### 4c. *A Schoolmaster's War*: are the six corrections actually in it

Yes. I had the book's text checked claim by claim and **all six are in it**, five of them cleanly and one with a caveat. This is the row I was most worried about, because in loop 1 the SOURCES block recorded the book as unread and I issued six fixes off it. The book carries them.

| Correction | In the book | Evidence |
|---|---|---|
| London teaching post, not Bradford Grammar | Yes | Introduction: "in 1937 he started work as a teacher of French and German, not in an elite institution but at Beckenham and Penge County School for Boys in South London." Illustrations: "HR in his classroom at Beckenham and Penge County School, 1938" |
| Pacifism abandoned before the fall of France | Yes, verbatim | p. 153, from a 1973 Salford symposium talk: "'conchie war hero' would be a lovely thing for the press, but I'd given up being a conchie before the fall of France" |
| Enlisted as a gunner, 14 November 1940 | Yes, verbatim | Chronology 1940, p. 174: "14 November: Having taken temporary leave from Beckenham School, HR enlists ('for duration of emergency') as gunner in Field Training Regiment, Topsham, Exeter" |
| The swim across the flooded River Allan is real | Yes, verbatim, and it is the strongest of the six | pp. 62 to 63: "There was a wide river (the Allan) at the edge of the wood... I found a spot where the river got a bit narrower, and slithered into the water and started to swim. The river was swollen with autumn rain and it swept me far beyond where I was aiming for" |
| Post office van into Switzerland, not Peugeot cars | Yes | Chronology, 1 December 1943: "HR is carried to a PTT (post office) van and driven by Pierre Lavigne to Delle where he rests till dark and is smuggled into Switzerland by four young men". **The book contains no mention of cars lent by Peugeot anywhere in connection with the escape** |
| Cauchi, 28 January, shot by a factory sentry | Yes in the book, **but now outweighed on the date, see D4** | Chronology 1944: "28 January: Eric Cauchi is fatally wounded outside Cafe Grangier." Biographies: "he walked into a trap at Cafe Grangier on 28 January 1944, and was shot as he ran away, dying a few hours later." pp. 71 to 72 identify the shooter: "He was part of the security detail at the factory, and he happened to be in a sentry box up on the wall" |

**Three things the book turns up that the log should absorb.**

- **The escape has two watercourses, not one.** The Chronology reads: "scrambling through the River Savoureuse and over fields and scrub, swimming across the River Allan, finding a bridge over the Canal du Rhone au Rhin, and reaching the house of Suzanne Bourquin at Etupes." Ascherson's LRB review independently says "across fields and through two rivers". The narration's "swam a swollen river" is true and safe; it just understates.
- **"About three miles" is the distance to the village, not the swim.** The book, p. 62: "out across some fields to the village of Etupes, about three miles away." The narration says "a friendly house some miles away", which is correct. Nothing in the script implies he swam three miles, and nothing should be allowed to drift that way in the build.
- **He did not walk into Switzerland under his own steam**, and the script correctly does not say he did. He was carried to the van and smuggled across by four named passeurs while badly wounded. My own loop-1 note said "walked across the border", which the book does not support; the script's wording, "driven out in a post office van and smuggled into Switzerland", is the accurate one and is what shipped.

**One correction to the SOURCES block that matters, because it goes public.** The block says of the book: "**The full text is available and was read at the QA gate.**" The book is not available in full through any licensed route. Open Library reports no ebook, archive.org has no copy, JSTOR is paywalled, Google Books shows no preview, and the Yale UP extract is dead. The complete text is readable only through unauthorised uploads. **A YouTube description should not say "the full text is available".** Say what is true: the book was consulted, and its Introduction, Chronology, Biographies and the escape chapter carry the six corrections.

### 4d. The forest crawl, re-opened

This is my own loop-1 wording and it deserves the same scrutiny as the writer's.

**The crawl is not in Ree's papers.** The word "forest" appears zero times in the book. "Crawl" appears twice, neither in the escape: crawling forward inside the aircraft before the jump, and insects on a blade of grass. The escape itself, pp. 61 to 63, is dragging, wading a ditch, forcing through brambles, three fields, a copse, the swim, a ploughed field, a canal bridge, and walking into Etupes.

**Where the crawl actually comes from.** Spartacus Educational carries it: "Despite being shot four times in the lung, arm, shoulder and side Ree managed to escape by swimming across a river and crawling four miles through a forest." en.wikipedia carries it as "according to his own account, had to swim across a river and crawl through a forest" and **that sentence has no citation attached to it in the article's wikitext.** The same sentence's "shot four times" is contradicted by the book, which has six bullets, two lodged and four grazes.

**So the substance of the correction is sound.** But "That part is invention" is a universal negative resting on absence, and I can only prove absence from the published papers, not from every telling Ree ever gave. Given that this channel's whole brand is not overclaiming, and given that the previous draft's failure here was a correction that was itself wrong, the line should be pulled back one notch to something provable. **Recommended, not required**, and word-neutral:

> **NARRATOR:** The retellings have him crawling four miles through a forest. Not in his papers.

14 words, exactly as now, delta 0. The VISUAL is unaffected.

## 5. Conditions

Seven edits. **None of them touches a spoken line, a VISUAL tag, a word count, a timecode or a reuse target.** Six are documentation and one is a missing newline. Each is given as exact wording to drop in.

### C1. Line 445, the missing blank line (structural)

Insert **one blank line** between line 444 and the `---` on line 445, so that Act 7's closing beat is separated from the rule the way every other act boundary in the file is. No text changes.

### C2. Line 590, the schoolmaster row, third column, replace entirely

> Ree taught at **Beckenham and Penge County School for Boys, in South London, from 1937 to 1940**, which is the posting the narration refers to. **Three independent sources carry it.** *A Schoolmaster's War*: "in 1937 he started work as a teacher of French and German, not in an elite institution but at Beckenham and Penge County School for Boys in South London", plus an illustration captioned "HR in his classroom at Beckenham and Penge County School, 1938". **IWM Sound Archive, catalogue 10858, object 80010635**: "British civilian school teacher in Beckenham, London 1937-1940". *The Fullerian* 2017-18: "At the start of the Second World War, Harry Ree was a French teacher at Beckenham and Penge Grammar School." **Bradford Grammar is postwar and that is not in doubt, but its year is:** the book's chronology says 1 September 1946, while **Bradford Grammar School's own history says he joined in 1949 and left in 1951**. Both fit the Watford headmastership from 1951, and **no year is spoken in the episode, nor should one be.** **en.wikipedia's "In 1937 he became a language master at Bradford Grammar School" is wrong and is contradicted by its own footnote**, *The Fullerian*, which places him at Beckenham at the outbreak of war. **AIM25 is silent on this and is no longer cited for it:** it lists Bradford in one compressed career sentence with no date attached and never mentions Beckenham. The narration says only "the nineteen thirties" and "in London" |

### C3. Line 615, the Rodolphe row, replace the sentence beginning "The naming rests on"

> The naming rests on **four independent lines, and none of them is Marcot.** **Neal Ascherson, LRB 42/15**, verbatim: "He was already in touch with the manager at Sochaux, Rodolphe Peugeot, who was committed to the Resistance, when in July 1943 the RAF unexpectedly attacked the factory with 165 Halifax bombers." **The IWM catalogue summary of Ree's own oral history**, object 80008516, which lists "Rodolphe Peugeot's hearing of authentication of Harry Ree, via British Broadcasting Corporation broadcast" and carries him again under Associated people. **fr.wikipedia**: "Ce dernier lui fait rencontrer Rodolphe Peugeot, resistant et cadre dans l'entreprise familiale". **And that sentence is uncited.** The article carries exactly three footnotes, on the May 1940 triumvirate, the July 1941 handover and the closing V1 sentence, **so this must not be described as Marcot or Loubet citing anything.** And **Bradford Grammar School's July 2020 article, built on an interview with Jonathan Ree**: "persuading Rodolphe Peugeot, the son of the Peugeot factory owner, to sabotage the family premises at Sochaux." **Jonathan Ree's edition has not been checked on this point and is not cited for it.** The sources disagree on his job title, calling him the manager at Sochaux, the owner, a cadre in the family firm, and the head of Aciers et Outillages Peugeot, **which is exactly why the narration says only "the family member behind the deal"**

### C4. Line 652, the SOURCES entry for IWM 80008516, replace the clause after "four errors of its own"

> so the Rodolphe identification rests instead on **Ascherson in the LRB, on fr.wikipedia, and on Bradford Grammar School's account of an interview with Jonathan Ree**

### C5. Line 8, ACCURACY NOTE point (6), replace "per Ree's own IWM oral history"

> per **Ascherson in the LRB and the IWM catalogue summary of Ree's own oral history**

This is the one that matters most, because as written the ACCURACY NOTE contradicts the log two pages below it and cites the content of a recording nobody in this pipeline has listened to. The log's demotion is right; the note has to match it.

### C6. Line 631, the Cauchi row, third column, replace entirely

> **Three dates are in play and the script speaks none of them.** **The National Archives, HS 9/281/5**, SOE's own personnel file record: "Eric Joseph CAUCHI, aka Louis Jean CAUDRON, aka PEDRO, aka JEAN, aka STOCKBROKER, aka MESSENGER - born 11.08.1917, **died 05.02.1944**". **Foot, p. 371**, gives 6 February 1944 and a cafe brawl. ***A Schoolmaster's War* gives 28 January**: "he walked into a trap at Cafe Grangier on 28 January 1944, and was shot as he ran away, dying a few hours later", and it names the man who fired as a German soldier on the factory security detail, "in a sentry box up on the wall", **not the Gestapo**. **One nuance to keep: the trap in the cafe was German-run, so "not the Gestapo" is true of the fatal shot and not of the operation.** The earlier draft asserted February and the Gestapo, choosing a side silently. **Tier 1 sits on the February side and Ree's own papers on the January side, so the conflict is unresolved**, and the narration now says only "early nineteen forty four" and "was shot and killed", which is true on every reading. The brawl is omitted because it sits in the straight act |

### C7. Two smaller misattributions and one public-facing sentence

**Line 602**, the Bomber Command row, replace the closing sentence "The targeting itself is the Bomber Command War Diaries":

> The targeting itself is **Foot, p. 287**: "it was a small target that would need to be hit precisely if it was to be usefully damaged at all; and it was sited close to the railway station in a populous part of the town"

**Line 592**, the codename row, replace "en.wikipedia, AIM25, and Foot's index":

> en.wikipedia and Foot's index, which gives "Cesar, see Ree" and the DSO and OBE but no rank. **AIM25 carries no rank, no corps and no codename and is not cited for this**

**Line 657**, the SOURCES entry for *A Schoolmaster's War*, replace "**The full text is available and was read at the QA gate, where it corrected the script in six places**":

> **Consulted at the QA gate, where it corrected the script in six places.** The book is not available in full through any licensed route: no ebook on Open Library, no copy on archive.org, no Google Books preview, paywalled on JSTOR

That last one is not pedantry. The SOURCES block ships in the YouTube description, and "the full text is available" is a claim about the book's availability that is not true of any legitimate source.

**Also in that entry**, the six-item list ends "and the 28 January date and factory sentry in Eric Cauchi's death". Given C6, change that to:

> and the contested January date and the factory sentry in Eric Cauchi's death, which is why the narration gives neither

## 6. Recommended, not conditions

- **The forest crawl**, section 4d above. Replace line 400 with "The retellings have him crawling four miles through a forest. Not in his papers." 14 words, delta 0.
- **Act 1's repeated name.** Line 68 currently reads "As a student, Harry Ree was a committed pacifist," one beat after line 64 has already introduced him by full name, and it also jumps from "is a schoolmaster" to "was a pacifist" without a signal. Word-neutral fix, 9 words for 9: **"As a student, he had been a committed pacifist."** This is my own loop-1 wording being tidied, not a defect in the revision.
- **Fix 17 from loop 1**, the double-game and refractaires beats at lines 148 and 152. Still outstanding, still non-blocking, unchanged in force.
- **Line 549** in the production notes reads "The fourth line, German management's..." and then corrects itself with "It is the third of the three, not a fourth." The count is right; the sentence is a leftover from the old numbering and will confuse a build agent. Change "The fourth line" to "The third".
- **The SOURCES entry for the TNA personnel file** could carry its piece reference, **HS 9/1240/3**, which I confirmed resolves to "Harry Alfred REE - born 15.10.1914".
- **Robert Peugeot's age.** The log says "The age is straightforward from his dates", which is true: born 21 July 1873, so seventy in the November 1943 of Act 5. Worth adding a line, because a future editor will otherwise "correct" it: the French source that gives "age de 70 ans" attaches that age to the **July 1941** handover, where he was in fact 68. The script's seventy is right and the French source's is not.

## 7. Nothing was touched beyond scope

Confirmed by a full sequential re-read of all 112 beats, all 112 VISUAL tags, both blockquote notes, the production notes, every log row and the whole SOURCES block.

- **Narration:** every beat is either one I quoted and passed in loop 1, or one of my sixteen replacements. No unreviewed line.
- **VISUAL tags:** the nine swaps I specified, plus scene 91's farmhouse window, which is a necessary consequence of fix 9 and carries no factual claim. Nothing else.
- **Structure:** tag totals, reuse count, unique generations, beat cap, section order and act hooks are all unchanged from the loop-1 file except where a fix required it.
- **Documentation:** rewritten extensively, which is what the coordinator asked for, and audited row by row above.
- **The one thing that changed without being asked for** is the lost newline at line 445, which is a side effect of the reorder rather than an edit anyone made on purpose. C1 restores it.

## 8. Cold read, second pass

Read aloud end to end again. The episode is better than the loop-1 draft, and in one place noticeably so.

**Act 2 now ends on "It was small, it was close to houses, and it needed hitting precisely."** That is the single biggest improvement in the revision. The old joke let the viewer relax one beat before a hundred and twenty three people are killed. The new line does the opposite: it tells you what is about to go wrong, in Foot's own terms, and then Act 3 opens flat and stays flat. The act-out is now doing work instead of getting a laugh.

**Act 7 is also better for the reorder**, and not only on tone. Ending on "London cancelled the raid" pays off the act's own title, "THE RAID THAT NEVER CAME", which the old order buried two beats early behind a Michelin aside. The aside still lands where it sits now, and it sets up the outro's teaser cleanly.

**Act 1 is drier than it was.** The three replaced beats traded a comic set piece for a factual run, and the act's laughs now rest on the accent gag, the crossed-out flowchart and the SOE payoff line. It still works and the cold open in front of it is untouched, but this is the one place where accuracy cost the episode something. Worth knowing rather than worth fixing.

**Act 2's production list reads better** than it did. Glossing track shoes in the same breath solved a comprehension problem I flagged in loop 1, and the run is now three items rather than four.

**The VOICE NOTE now covers everything I flagged.** Sire as SEER rather than the English word, Cauchi, Petainism, Bonal, Henri, Michelin and Jean Pierre are all in. Nothing else in the narration would break an English TTS read.

**The two hardest lines are still the two hardest lines** and both are untouched. Tag both acts TONE: STRAIGHT as the build notes say, and give "A hundred and twenty three people were killed that night" the longest hold in the episode.

## 9. Re-gate verdict

**The narration is clean.** All sixteen loop-1 fixes landed verbatim. Every structural check passes on my own measurement: 1,406 words, 112 tags, 112 beats, none over 14, 11 reuses all resolving backwards and byte-identical including the two the reorder relabelled, 101 unique generations, zero dashes, zero camera moves, per-act counts exact and every act header timecode re-derived to within 0.9 seconds, 8:53 at the measured rate and 8:07.6 at the fast end, which clears the mid-roll floor by seven and a half seconds. Both tone-adjacency violations are cleared and the reorder created no new one. Act 1 coheres and still ends on a hook. Act 7 ends on its own title payoff. **I found no unreviewed narration and no collateral damage in the spoken script.**

**The defects are all in the documentation, and there are six of them plus one lost newline.** Three rows cite sources for things those sources do not contain: AIM25 for a Bradford Grammar date it does not give, fr.wikipedia's Marcot and Loubet footnotes for a Rodolphe sentence that carries no footnote at all, and AIM25 again for a rank, corps and codename it does not carry. One row, on Eric Cauchi, is now outweighed by a Tier 1 source neither pass had found, The National Archives file HS 9/281/5, which gives 5 February 1944 against the memoir's 28 January. The ACCURACY NOTE re-elevates the IWM record that the log correctly demotes, and cites the content of a recording nobody has heard. And the SOURCES block, which ships in the YouTube description, says the full text of *A Schoolmaster's War* is available when no licensed route to it exists.

**None of that changes a spoken word.** The identification of Rodolphe holds on four independent lines including Ascherson verbatim in the LRB. "In London" holds on three, one of them an IWM archival record. All six of the *A Schoolmaster's War* corrections are genuinely in the book, verified quotation by quotation. Foot's two corrected page numbers, 434 and 436, are both confirmed from the running heads of the scan the script itself links, and the outro rests safely on p. 434.

**So this is a conditional pass, and the condition is C1 through C7 in section 5.** They are exact drop-in wordings, they take one editing pass, and they touch nothing a viewer will ever see or hear. Applying all seven is what makes this a PASS. **Shipping without them is not sanctioned by this gate**, because a materially false log row is worse than no row at all by the file's own stated standard, and two of the seven are public-facing.

The recommendations in section 6, including the softening of my own "That part is invention" line, are not conditions and the episode ships without them.

VERDICT: PASS

---

## Manager close-out

Conditions C1 through C7 were applied verbatim on 2026-09-03, each anchored by content rather than by line number (the C1 newline insertion had shifted the report's line numbering) and each verified to occur exactly once before replacement.

Three of the section 6 recommendations were also applied, all of them gate-authored verbatim wording:
- The forest crawl line, "That part is invention" to "Not in his papers", because the gate correctly identified its own loop-1 wording as a universal negative that outran the evidence. Word-neutral.
- The Act 1 repeated-name tidy, "As a student, Harry Ree was a committed pacifist" to "As a student, he had been a committed pacifist". Word-neutral, 9 words for 9.
- The stale "A fourth" numbering in the production notes, corrected to "The third".

Fix 17 remains outstanding and non-blocking, as it has been since loop 1. The remaining section 6 recommendations (the TNA piece reference and the Robert Peugeot age note) were not applied.

Per the QA agent's own statement, "Applying all seven is what makes this a PASS." That condition is satisfied. This is the QA agent's conditional PASS taking effect, not a new Manager judgement.

VERDICT: PASS

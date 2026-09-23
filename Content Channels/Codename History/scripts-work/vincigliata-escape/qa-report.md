# QA Report: The Generals Who Dug Out of a Castle With a Croquet Set

*Wave 3 QA / fact-check gate. Written incrementally, cheapest checks first.*

## 1. MECHANICAL CHECKS

### Mandated script output (verbatim)

```
SPOKEN: 1400 beats: 112 visuals: 112 REUSE: 9 em: 0 inlineTONE: 0
OVER14: []
```

| Metric | Required | Actual | Result |
|---|---|---|---|
| SPOKEN | 1396-1404 | 1400 | PASS |
| beats | 112 | 112 | PASS |
| visuals | 112 | 112 | PASS |
| REUSE | 9 | 9 | PASS |
| em-dashes | 0 | 0 | PASS |
| inline TONE | 0 | 0 | PASS |
| OVER14 | empty | empty | PASS |

**All mechanical counts PASS.**

### Structural checks (by eye + script)

| Check | Result |
|---|---|
| All 9 sections present, in order (title line, header block, ACCURACY + VOICE blockquotes, COLD OPEN + title card, ACT 1-11 with timecodes, OUTRO + subscribe CTA + teaser + `[END]`, PRODUCTION NOTES, FACT-CHECK LOG, SOURCES) | PASS |
| Brackets / stage directions inside spoken lines | PASS. The only parentheses are in the three speaker LABELS (`**ITALY (character voice):**`), never inside the spoken text. Every NARRATOR line is clean prose. |
| Camera moves in `[VISUAL:]` tags (zoom, pan, push-in, dolly, tracking, slow reveal, Ken-Burns, tilt, crane, rack focus) | PASS. Zero hits across all 112 tags. |
| Act timecodes continuous, no gaps or overlaps | PASS. 0:00 -> 8:51 unbroken. |
| Timecode arithmetic vs per-act word count at 158 wpm / 531 s | PASS. Recomputed independently; every act boundary lands within 1 second of the stated code. Per-act: Cold Open 86w, A1 129, A2 66, A3 108, A4 145, A5 89, A6 135, A7 77, A8 87, A9 129, A10 91, A11 194, Outro 64. Sum 1400. |
| REUSE pointer integrity | PASS. All 9 REUSE tags are byte-identical to the earlier tag they name (scenes 22->9, 32->6, 41->5, 54->4, 66->12, 70->7, 79->53, 93->39, 98->13). 103 unique tag texts, matching the stated generation budget. |
| Title format | PASS. `The Generals Who Dug Out of a Castle With a Croquet Set \| Codename History` is Standard format. No `Codename:` prefix forced onto an operation with no codename. |
| Em-dashes anywhere in file | PASS. Zero. |

### Forbidden-item sweep of spoken narration only

| Forbidden item | Result |
|---|---|
| "roughly 1,500 escape attempts" denominator | ABSENT |
| Pre-escape guard ratio / "many times their number" | ABSENT |
| Boyd recaptured "near Como" | ABSENT (script says only "caught at the border") |
| Starvation / brutality framing of the camp | ABSENT. The only "starv" hit is the refusal line "And forget the starving prisoner picture." |
| "Nobody has written about this" | ABSENT. Felton's *Castle of the Eagles* is credited in SOURCES. |
| "the twenty-ninth or thirtieth" spoken hedge | ABSENT |
| Hard date for the Swiss crossing | ABSENT. Act 7 says "The next night, they were out." Manager instruction obeyed. |
| "unkillable" / "indestructible" as framing | ABSENT as framing. "indestructible" appears once, in the explicit refusal: "Not indestructible. Just extremely recognisable." Correct use. |
| Boyd's rank | PASS. "Air Vice Marshal Owen Boyd" (Act 1). TNA's "Air Marshall" error is not reproduced. |
| San Vittore spelling | PASS. Script visual tag and log both use **San Vittore**. TNA's "San Vittorio" appears once, only inside the fact-check log where it is explicitly flagged as TNA's error. |
| Gambier-Parry | Not named anywhere in spoken narration. No spelling exposure. |

---

## 2. THE TWO WRITER-FLAGGED CLAIMS: BOTH RESOLVED, BOTH NOW TIER 1

### 2a. Hargest "member of parliament" - CONFIRMED, Tier 1, two independent lines

I opened the **Dictionary of New Zealand Biography** entry for Hargest (J. A. B. Crawford, DNZB, Te Ara, Manatu Taonga / Crown copyright), via the Internet Archive capture of the official Te Ara print URL `teara.govt.nz/en/biographies/4h16/hargest-james/print` (capture 20151009072937). Verbatim:

> "In 1931 he narrowly succeeded in taking the Invercargill parliamentary seat for the coalition government. Four years later he switched to the rural Southland seat of Awarua, **which he held until his death**."

Second independent line: a **1944 Awarua by-election** was held, which only happens because the seat fell vacant on his death in office.

**Verdict: the script's "a sitting member of parliament" (Act 1) and "Member of parliament" (Act 11) are both CORRECT and now Tier 1 anchored.** The `VERIFY BEFORE LOCK` flag on this row can be cleared. No change to the narration.

### 2b. "ashore in Normandy on D-Day as New Zealand's observer" - CONFIRMED, Tier 1, NOT a fabricated specific

I opened **NZHistory** (Manatu Taonga, the New Zealand Ministry for Culture and Heritage), `nzhistory.govt.nz/war/d-day`, via the Internet Archive capture 20260309030305. Verbatim:

> "While no New Zealand military units landed on the beaches of Normandy, individual New Zealanders did. **Brigadier James Hargest, New Zealand's official observer with the Allied forces, went ashore with the British 50th Division on D-Day**, and radar specialist Ned Hitchcock landed amidst the carnage on Omaha Beach the following day."

Corroborated independently by the DNZB entry: "At his own suggestion, Hargest was appointed New Zealand's observer with the Allied armies preparing to invade France. He was attached to the British 50th Division, which landed in Normandy on D-Day."

**Verdict: the line stands as written. It is not a fabricated specific.** Two independent New Zealand government sources, one of which states his personal landing on 6 June explicitly. No change to the narration.

DNZB also supplies **Tier 1** for the manner of death, which the FACT-CHECK LOG currently rates Tier 2: "Wounded in June, **Hargest was killed by shell fire on 12 August 1944**."

### 2c. Miles's death and the DNZB entry - **I OPENED IT.** Here is what it actually says.

Te Ara is behind Cloudflare and refused both automated fetch and a real browser session (I did not attempt to defeat the bot check). I reached the entry instead through the **Internet Archive capture of the official Te Ara print URL** `teara.govt.nz/en/biographies/5m46/miles-reginald/print`, capture timestamp **20231004201516** (4 October 2023). The words are the DNZB's; the route was archival. Author and date confirmed on the page: **Garry James Clayton, 'Miles, Reginald', Dictionary of New Zealand Biography, first published in 2000.**

The operative sentence, **verbatim**:

> "Miles was made a CBE and received a bar to his DSO for his 'splendid achievement in escaping'. **However, on 20 October 1943, in a state of depression and exhaustion, he committed suicide in Figueras, north of Barcelona.** He was survived by his wife and daughters."

**This closes the single most sensitive open item in the episode.** The claim is real, it is Tier 1 (.govt.nz, Crown copyright, named academic author, bibliography citing Hargest's *Farewell Campo 12*, Murphy's *2nd New Zealand Divisional Artillery*, and the *Evening Post* obituary of 26 October 1943), and the script's attributed treatment is the right call: it names the source rather than asserting in the channel's own voice, names no method, and does not use it as a reveal. **I endorse the attributed treatment. It ships.**

The same entry also independently upgrades four other claims to Tier 1:

| Script line | DNZB verbatim | Verdict |
|---|---|---|
| "Brigadier Reginald Miles, who commanded the New Zealand Division's guns" | "seconded to the Second New Zealand Expeditionary Force as **commander of the Divisional Artillery**, with the rank of brigadier" | CONFIRMED, upgraded to Tier 1 |
| "He reached the Spanish frontier that October, nineteen forty-three, and died there." | "on 20 October 1943 ... in **Figueras, north of Barcelona**" | CONFIRMED |
| "Fifty." | Born **10 December 1892**, died **20 October 1943**. My arithmetic: 50 years, 10 months. | CONFIRMED, math redone |
| "His **only son** had died three years earlier on HMS Glorious." | "they were to have **four daughters and a son**" ... "he lost his son Reginald, a Fleet Air Arm officer, when the aircraft carrier Glorious was sunk" ... "He was survived by his wife and **daughters**." | CONFIRMED, upgraded from Tier 2 to Tier 1. June 1940 to October 1943 is three years four months, so "three years earlier" is correct. |

Two small divergences from the DNZB, neither blocking, both logged in section 4 below: the DNZB says "in a state of **depression** and exhaustion" where the script says "exhausted and **in despair**"; and the DNZB says "**five** months' tunnelling" where the script says six.

---

## 3. THE FIND THAT DRIVES MOST OF THIS REPORT: THE NEW ZEALAND GAZETTE DSO CITATION

Chasing the "12 foot wire" claim, which the FACT-CHECK LOG rates as single-sourced Tier 2 Wikipedia, I found that the Wikipedia passage is a **blockquote of the citation for Miles's bar to the DSO, published in *The New Zealand Gazette*, 21 September 1944**. That is a contemporaneous official government document written from the escapers' own reports. It is **Tier 1 and primary**, and neither wave of research identified it as such. It reads, verbatim and in full on the escape:

> "Escape from Camp 12, P.M. 3200, Italy (General's Camp). This camp was extremely well guarded and in consequence it was decided that the only possible method of escape would be by way of a tunnel. On the 18th September, 1942, tunnelling began. All officers and other ranks worked, with the exception of one officer who was awaiting repatriation. The entrance to the tunnel was through a sealed up chapel which all soil was placed. The work, which consisted of a 3 foot by 3 foot tunnel, 40 feet long with a 10 foot shaft at the entrance and a 7 foot shaft at the exit, was completed by the end of February 1943. At 2100 hours on the 29th March, 1943, Brigadiers Miles and Hargest, in company with four other officers, escaped through the tunnel. The four other officers were subsequently recaptured. Brigadiers Miles and Hargest dressed as workmen and having walked to Florence station, caught a train to Milan where they went to the North station. They caught a train to Como and walked towards Chiasso. 2 kilometres from Chiasso they left the main road and proceeded across country until they reached a knoll south of Chiasso where the frontier lay along the opposite slope of a valley below them. The frontier consisted of heavy cyclone netting 12 foot high interlaced with brambles and with small bells near the top. They cut the wire with pliers at ground level without making much noise and came on to Swiss territory at 220 hours on the 30th March, 1943. They gave themselves up to the police at Mendrisio and were released in Berne on the 2nd April, 1943."

**What this document does for the episode, good and bad:**

| Effect | Detail |
|---|---|
| UPGRADES the wire | "heavy cyclone netting 12 foot high interlaced with brambles" and "cut the wire with pliers at ground level" are **Tier 1 primary**, not the single Tier 2 line the log claims. The script's Act 7 wire beats are better sourced than the script believes. |
| SETTLES the 29 vs 30 March conflict, 2 to 1 for Mason | A **third independent Tier 1 line** now gives the break at 2100 on 29 March and the Swiss crossing on 30 March. TNA's 30 March / 1 April is the outlier. The Manager's no-spoken-crossing-date instruction was still the right call, but "The next night" is now the best-supported reading and the log should say so. |
| CONFIRMS the ten-foot entrance shaft | "a 10 foot shaft at the entrance". Second independent line beside Boyd. |
| CONFIRMS workmen's clothes, Florence to Milan, Como, the walk toward Chiasso | All Tier 1. |
| RESOLVES the Todhunter question | "**All officers and other ranks worked**, with the exception of one officer who was awaiting repatriation." Combined with Mason, "Todhunter and Stirling dug" is now Tier 1, not the Tier 2 the log concedes. |
| **CONTRADICTS the cold open** | "**This camp was extremely well guarded**". See blocking issue 3. |
| **CONTRADICTS the gallery width** | "a **3 foot by 3 foot** tunnel, 40 feet long". The log dismisses 3x3 as "the conflicting Tier 2 '3 foot by 3 foot'". It is not Tier 2. See blocking issue 5. |
| **CONTRADICTS "changed trains at Como"** | The change of trains was at **Milan** (Centrale to Nord). At Como they left the train and walked. See blocking issue 2. |

**This citation should be added to SOURCES.** It is the single best primary document on the escape's mechanics that either research wave reached.

---

## 4. CLAIM-BY-CLAIM VERIFICATION

Tier 1 sources I opened myself this pass: **DNZB Miles** (Clayton, 2000), **DNZB Hargest** (Crawford), **NZHistory D-Day** (Manatu Taonga), **Garland and Smyth ch. 23** (US Army official history, HyperWar), **Gavin Long, *To Benghazi*, ch. 11** (Australian official history, HyperWar), and the **NZ Gazette DSO citation** of 21 September 1944.

| # | Claim (as spoken) | Where | Source(s) checked | Verdict |
|---|---|---|---|---|
| 1 | "A castle in the hills above Florence. In nineteen forty-two, a prison." | Cold open | Parri PG 12 sheet; TNA blog; NZ Gazette ("Camp 12 ... General's Camp") | PASS |
| 2 | "Twenty-five prisoners. A dozen of them generals." | Cold open | Parri sheet (21-30 held, about 12 generals). Note: the Italian sheet counts brigadiers as generals, Italian convention. TNA's "nearly half of the officers" for six implies about 13 officers, which makes 12 consistent. | PASS with note (4.1) |
| 3 | "Almost no guard against escape." | Cold open | TNA supports the *assumption*; **NZ Gazette says "extremely well guarded"** | **FAIL, blocking 3** |
| 4 | "Senior officers would not stoop to breaking out." | Cold open | TNA blog, verbatim, re-read in the report's LATE TIER 1 section | PASS |
| 5 | "Six months later they went out through the floor." | Cold open | Gazette: began 18 Sept 1942, out 29 March 1943 = 6.3 months. Boyd, Mason, NZ Army Museum agree six. DNZB Miles says five. Majority and arithmetic both support six. | PASS with note (4.2) |
| 6 | "Two stolen carving knives and a croquet set." | Cold open | Boyd's tool list, primary; **DNZB Miles independently: "with a kitchen knife and iron bars"** | PASS, upgraded to two lines |
| 7 | "The man who designed it complained about the security." | Cold open, Act 8 | TNA blog, document reproduced, WO 32/10706, "yet another complaint" | PASS |
| 8 | "Lieutenant General Sir Philip Neame. Victoria Cross. Royal Engineer." | Act 1 | Boyd's notes (Chief Engineer); VC and RE uncontested | PASS |
| 9 | "Air Vice Marshal Owen Boyd, captured in Sicily before he ever reached his command." | Act 1 | MSMT POW index: 20 Nov 1940, Sicily, en route to Deputy AOC-in-C Middle East. **Rank correct; TNA's "Air Marshall" error not reproduced.** | PASS |
| 10 | "Brigadier John Combe, who trapped an entire Italian army at Beda Fomm." | Act 1 | **Gavin Long, *To Benghazi*, ch. 11 (Australian official history):** Combe of the 11th Hussars commanded the flying column that took position astride the Benghazi-Agedabia road at Sidi Saleh, 5 Feb 1941; "the Italian surrender at Beda Fomm" followed on the 7th; "the last remnant of the Italian Tenth Army". | PASS, **upgraded from the log's Tier 2 to Tier 1**. Note 4.3 on his rank at the time. |
| 11 | "Brigadier James Hargest, a sitting member of parliament." | Act 1 | **DNZB Hargest: Awarua, "which he held until his death"**; 1944 Awarua by-election | PASS, Tier 1, flag cleared |
| 12 | "Brigadier Reginald Miles, who commanded the New Zealand Division's guns." | Act 1 | **DNZB Miles: "commander of the Divisional Artillery"**; NZ National Army Museum CRA 2 NZ Div | PASS, Tier 1 |
| 13 | "O'Connor destroyed the Italian Tenth Army. Over a hundred thousand prisoners." | Act 1 | **Long, ch. 11: O'Connor's corps "had advanced 500 miles and taken 130,000 prisoners, 400 tanks and 1,290 guns", destroying ten Italian divisions.** | PASS, **upgraded from the log's Tier 2 to Tier 1**. "Over a hundred thousand" sits safely under 130,000. |
| 14 | "A German patrol found his car and handed him to the army he beat." | Act 1 | Tier 2 across Neame's, Combe's and O'Connor's entries. Needs no number. | PASS, low risk |
| 15 | "A chicken run. A vegetable garden. A library." | Act 1 | Parri sheet, Tier 1, verbatim. The "nearly a thousand books" figure correctly NOT spoken. | PASS |
| 16 | "They could leave with an escort and lunch at a trattoria." | Act 1 | Parri sheet, verbatim: "They could leave the castle with an escort and often went to eat in a trattoria not far from the camp." | PASS |
| 17 | "The first attempt was not a tunnel. Somebody climbed the wall." / "Now they were." | Act 2 | TNA verbatim: "An abortive attempt to scale the walls out of sight of the guards put the sentries on their guard." Script correctly does not name the climber. | PASS |
| 18 | Chapel bricked up, full of furniture; service lift halted between floors; 2.5 feet of stone | Act 3 | Boyd's notes, primary, verbatim on the wall thickness. Gazette independently: "The entrance to the tunnel was through a sealed up chapel". | PASS |
| 19 | "The hole was fifteen inches by twelve." | Act 3 | Boyd's notes, primary: "about fifteen inches by 12 inches, a tight fit" | PASS |
| 20 | "Boyd on the fit. Where my shoulders would go, Jim's backside would go." | Act 3 | Boyd's notes, primary, quoted and attributed on camera. Faithful truncation of "Calculated that where my shoulders would go, Jim's backside would go, and vice versa." | PASS |
| 21 | Three-ply sandpaper cover, water-bottle counterweight | Act 3 | Boyd's notes, primary | PASS |
| 22 | Two carving knives with handles Boyd fitted; croquet-hoop spikes; iron bars from a well | Act 4 | Boyd's notes verbatim ("Iron bars found in previously opened well chamber"); **DNZB Miles corroborates knife plus iron bars** | PASS, upgraded to two lines |
| 23 | "Their spirit level was an aspirin tube of water." | Act 4 | Boyd's notes, primary | PASS |
| 24 | "Faking a deck tennis court. Twenty-seven feet." | Act 4 | Boyd's notes on Neame's method, primary. No competing figure found. | PASS |
| 25 | "Ten feet down, then a gallery." | Act 4 | Boyd (3ft x 4ft, 10ft deep) **and** NZ Gazette ("a 10 foot shaft at the entrance"). Two independent Tier 1 lines. | PASS, upgraded |
| 26 | "Never less than eighteen inches wide." | Act 4 | Boyd's notes: "never less than 3 1/2 feet by 1 1/2 feet". **NZ Gazette (Tier 1, not Tier 2 as the log claims): "a 3 foot by 3 foot tunnel".** Unresolved Tier 1 conflict, spoken unattributed. | **FAIL, blocking 5** |
| 27 | Ping-pong table and coconut matting retaining the spoil | Act 4 | Boyd's notes, primary | PASS |
| 28 | "Two RAF sergeants wired a bell into the tunnel" / "ringing for room service" | Act 4 | Boyd's notes name Sgt Ronald Bain RAF and Sgt Pitt, and the bell off the bedroom push | PASS |
| 29 | White silk pyjamas, weekly inspection, "Ghost goes West" | Act 4 | Boyd's notes, primary, attributed to the men | PASS |
| 30 | "The twenty-ninth of March, nineteen forty-three. A wet evening." | Act 5 | Mason; MSMT Boyd index; **NZ Gazette "At 2100 hours on the 29th March, 1943"**. Three independent Tier 1 lines. TNA's 30 March is the outlier and the log names it. | PASS, strengthened |
| 31 | "Dummies in the beds. Specifically to beat the night search." | Act 5 | TNA verbatim | PASS |
| 32 | Zigzag outside lid pressed into pine needles | Act 5 | Boyd's notes, primary. The 5-inch unbroken depth correctly not spoken. | PASS |
| 33 | "Six men went out in three pairs. Nearly half the officers in the castle." | Act 5 | Mason for six in three pairs; **TNA verbatim "this was nearly half of the officers in the castle"**; Gazette: "in company with four other officers" | PASS |
| 34 | "Hargest and Miles went as workmen on the early train. Boyd and Combe too." | Act 5 | TNA; **Gazette: "dressed as workmen and having walked to Florence station, caught a train to Milan"** | PASS |
| 35 | "They decided to walk to Switzerland." (O'Connor, Carton de Wiart) | Act 5 | Mason, Tier 1 carried | PASS |
| 36 | "Within about a week, four of the six were back inside the castle." | Act 6 | Mason for four of six; "about a week" deliberately used because 5 April (Parri) and eight days (Wikipedia) do not reconcile. Correct handling. | PASS |
| 37 | "Combe never got out of Milan. Police took him at the station." | Act 6 | TNA blog, from Combe's own report | PASS |
| 38 | "Boyd got clear of Milan alone, and was caught at the border." | Act 6 | TNA: "trying to cross the border". **"Near Como" correctly absent.** | PASS |
| 39 | "Carton de Wiart was sixty-two, one eye, one hand, and no Italian." | Act 6 | Born 5 May 1880, escape March 1943 = 62. Math redone, correct. "one hand" follows TNA; Act 9 follows Garland and Smyth's "an eye and an arm". Internal inconsistency, note 4.4. | PASS with note |
| 40 | "The National Archives finds it amazing they lasted as long as they did." | Act 6 | TNA verbatim, attributed on camera | PASS |
| 41 | "Not indestructible. Just extremely recognisable." | Act 6 | Editorial, and it is the commission's own instruction. Correct refusal of the saturated lane. | PASS |
| 42 | "A week at large, then back through the gate. Thirty days solitary." | Act 6 | MSMT POW index (built on Boyd's papers): "returned to Vincigliata for 30 days solitary confinement" | PASS |
| 43 | "Two days. He refused to admit he was a prisoner of war." / civilian prison / "He bought two days" | Act 6, straight | TNA verbatim from Combe's own report. **San Vittore spelling correct**, TNA's "San Vittorio" not reproduced. | PASS |
| 44 | "Hargest and Miles changed trains at Como." | Act 7 | TNA says Como. **NZ Gazette says the change was at Milan; at Como they left the train and walked.** Tier 1 vs Tier 1. | **FAIL, blocking 2** |
| 45 | "Twelve feet of heavy netting, laced through with brambles." | Act 7 | **NZ Gazette, verbatim: "heavy cyclone netting 12 foot high interlaced with brambles"** | PASS, **upgraded from the log's Tier 2 to Tier 1 primary** |
| 46 | "They cut it at ground level. The next night, they were out." | Act 7 | **Gazette: "They cut the wire with pliers at ground level"**; TNA also says cut. "The next night" commits to no date and matches Mason and the Gazette. | PASS |
| 47 | "Two New Zealand brigadiers, both in their fifties." | Act 7 | Hargest b. 4 Sept 1891 = 51; Miles b. 10 Dec 1892 = 50. Math redone, both correct. | PASS |
| 48 | "Military Intelligence knew of three men who got clear of Italy before the armistice." Two were these two. | Act 7 | Mason p. 213 as cited in the Gazette-adjacent literature, **and** Monte San Martino Trust (Jeremy Archer) independently. Two independent lines. **The "1,500" denominator correctly absent.** | PASS |
| 49 | "Neame put the new garrison at a hundred men, for twenty-five prisoners." | Act 8 | Neame p. 308 via Wikipedia, Tier 2, **attributed on camera to Neame**, which is the correct handling. 11 officers + 14 other ranks = 25, arithmetic checks. **No pre-escape ratio spoken.** | PASS |
| 50 | Neame's complaint; "yet another complaint"; the Red Cross list after their "departure" | Act 8 | TNA blog, document reproduced, WO 32/10706, TNA's own quotation marks | PASS |
| 51 | "On the nineteenth they gave him a civilian suit and took him out." | Act 9 | TNA verbatim, 19 August 1943 | PASS |
| 52 | "Rome was sending a general called Zanussi to Lisbon, and Zanussi needed British credentials." | Act 9 | **Garland and Smyth verbatim: "As credentials, Carboni suggested that Zanussi take with him a British prisoner of war. Lt. Gen. Sir Adrian Carton de Wiart was selected."** | PASS, opened by me |
| 53 | "The United States Army official history. He was well known and easily recognised." | Act 9 | **Verbatim: "He was a good choice, for he was well known and easily recognized"** | PASS, opened by me |
| 54 | "He had lost an eye and an arm. The empty sleeve was the disguise." | Act 9 | **Verbatim: "he had lost an eye and an arm in the service of his country."** "Disguise" is the script's gloss, named honestly in the log and explained by the very next beat. | PASS, note 4.5 |
| 55 | "If the Germans stopped the car, the eye patch read as a prisoner exchange." | Act 9 | **Verbatim: "If the Germans discovered him in Zanussi's company, it would be obvious that the mission concerned merely the exchange of prisoners."** | PASS, opened by me |
| 56 | "Rome had already sent another general. The Lisbon ambassador declined to meet Zanussi." | Act 9 | **Verbatim: "Sir Ronald replied through an intermediary, since he saw no reason why he should meet another Italian general. The Allied terms were already in Castellano's hands."** | PASS, opened by me |
| 57 | "He negotiated nothing. He was never the negotiator. He was the paperwork." | Act 9 | **Verbatim: "While Carton de Wiart was kept out of sight and later returned to London, Zanussi was invited to visit the Allied camp."** Plus: de Wiart "offered to return to Rome with Zanussi since it began to appear that Zanussi had come on a futile mission." | PASS, opened by me |
| 58 | "The prisoners changed into civilian clothes and simply left." / "An Italian general put a train on." | Act 10 | TNA for the shape. That the train was laid on by a general is Neame p. 314 via Wikipedia, Tier 2. Chiappe's name, the 10 September date and the 60 miles correctly not spoken. Note 4.6. | PASS with note |
| 59 | "Monks at Eremo bricked their luggage into a wall, never found." | Act 10 | TNA verbatim | PASS |
| 60 | "A German sergeant, not knowing who they were, pointed them the way." | Act 10 | TNA says "a German **non-commissioned officer** who didn't know who they were". "Sergeant" is a rank the source does not give. | **FAIL, blocking 4** |
| 61 | "Twenty miles over mountains, then seventy-five on bicycles. In their fifties." | Act 10 | TNA verbatim. Ages 1943: Neame 55, Boyd 54, O'Connor 54. Math redone. | PASS |
| 62 | "Just before Christmas, a taxi to the coast, then a paid fishing boat's hold." / "They landed at Termoli." | Act 10 | TNA: night of 17/18 Dec 1943, taxi, paid captain, hold, Termoli. MSMT: 19 Dec. Date correctly softened. | PASS |
| 63 | "Every one of those escapes ran on Italian civilians who hid them." / "Six times they tried to meet a boat. Those helpers risked death." | Act 11, straight | TNA verbatim: "six unsuccessful attempts to rendezvous with a boat ... especially for their Italian helpers who risked death" | PASS |
| 64 | "Fourteen other ranks left with the officers. Sergeant Bain wired the tunnel." | Act 11, straight | Bain: Boyd's notes, primary, PASS. **Fourteen: Neame p. 314 via Wikipedia, Tier 2 only. The log claims TNA support that does not exist.** | Spoken line PASS with note 4.7; **log row FAIL, blocking 6** |
| 65 | "The Germans found them in the hills. The officers were higher up." / "The NCOs and the other ranks were taken." | Act 11, straight | Neame p. 325 via Wikipedia, Tier 2, deliberately undated. **The 120 Germans and 29 October correctly not spoken.** Correct handling of a Tier 2 claim the script cannot avoid. | PASS |
| 66 | "What happened to them, I cannot tell you. It is not recorded." | Act 11, straight | Honest. Both research waves searched and found nothing beyond Morgan, Bain and Pitt. Stating the gap on camera is the right call and is itself accurate. | PASS |
| 67 | "The generals wrote books. The men who dug beside them did not." | Act 11, straight | Neame *Playing With Strife*, Hargest *Farewell Campo 12*, Carton de Wiart *Happy Odyssey*, Ranfurly *To War with Whitaker* all exist. DNZB Hargest: "he wrote his classic account of the escape, Farewell Campo 12". No other-ranks memoir found. | PASS |
| 68 | "He reached the Spanish frontier that October, nineteen forty-three, and died there." | Act 11, straight | **DNZB: "on 20 October 1943 ... in Figueras, north of Barcelona"**; NZ National Army Museum. Day correctly not spoken. | PASS |
| 69 | "New Zealand's official history says only that he lost his life." | Act 11, straight | Mason: "lost his life in Spain in this last stage of a game attempt to reach Allied territory". Tier 1 carried, not re-opened by me (NZETC is bot-walled and the relevant chapter is not in the Wayback set). Flagged in note 4.8. | PASS, carried |
| 70 | "His entry in the Dictionary of New Zealand Biography says something else. That, exhausted and in despair, he took his own life." | Act 11, straight | **OPENED. DNZB verbatim: "on 20 October 1943, in a state of depression and exhaustion, he committed suicide in Figueras, north of Barcelona."** | PASS. Wording note 4.9. |
| 71 | "Fifty. His only son had died three years earlier on HMS Glorious." | Act 11, straight | **DNZB: b. 10 Dec 1892, d. 20 Oct 1943 = 50, math redone. "four daughters and a son" ... "he lost his son Reginald, a Fleet Air Arm officer" ... "survived by his wife and daughters".** Glorious June 1940 to Oct 1943 = three years four months. | PASS, **upgraded from Tier 2 to Tier 1** |
| 72 | "James Hargest did get home. Through occupied France, then Spain, that December." | Act 11, straight | Mason: December 1943. **DNZB: "Late in 1943 he travelled across occupied France and into Spain ... He then flew to England."** Compatible. The reported CWGC "November" could not be opened by either wave or by me (CWGC blocks automated access). Note 4.10. | PASS with note |
| 73 | "Fifty-two. Member of parliament. Two years a prisoner." | Act 11, straight | Fifty-two: b. 4 Sept 1891, d. 12 Aug 1944 = 52, correct. MP: confirmed Tier 1. **"Two years a prisoner": captured 27 Nov 1941 (Mason and DNZB), out 29 March 1943 = SIXTEEN MONTHS.** | **FAIL, blocking 1** |
| 74 | "He went back, ashore in Normandy on D-Day as New Zealand's observer." | Act 11, straight | **NZHistory (Manatu Taonga) verbatim: "Brigadier James Hargest, New Zealand's official observer with the Allied forces, went ashore with the British 50th Division on D-Day."** Plus DNZB. Two independent NZ government lines. | PASS, Tier 1, flag cleared |
| 75 | "The twelfth of August, nineteen forty-four. He was killed by shell fire." | Act 11, straight | **DNZB verbatim: "Hargest was killed by shell fire on 12 August 1944."** Mason's footnote agrees on the date. | PASS, **shell fire upgraded from Tier 2 to Tier 1** |
| 76 | "Six went out. Two got clear. Within eighteen months, both were dead." | Outro, straight | 29 March 1943 to 20 Oct 1943 = 7 months (Miles); to 12 Aug 1944 = 16.5 months (Hargest). Both inside eighteen. Math redone, correct. | PASS |
| 77 | "Neame designed it. Boyd made the knives. Todhunter and Stirling dug and stayed behind." | Outro | Neame and Boyd primary. **"Dug" now Tier 1 for both via the NZ Gazette: "All officers and other ranks worked, with the exception of one officer who was awaiting repatriation."** Stayed behind: TNA WO 208/3484 and the Pegasus transcription of WO 208/3320/94. | PASS, **upgraded from the log's split Tier 1 / Tier 2** |
| 78 | "Zeppelin L fifty-nine. Four thousand two hundred miles, about ninety-five hours." | Outro teaser | Carried from the commission, to be verified in that episode's own research. Correctly flagged as out of scope in the log. | OUT OF SCOPE, correctly flagged |

### Notes referenced in the table (all non-blocking)

**4.1 "A dozen of them generals."** Sourced to the Istituto Parri sheet, which is Tier 1, but Italian usage counts a brigadier as a general officer (*generale di brigata*) and British usage does not. At Vincigliata the genuine general officers were roughly O'Connor, Neame, Carton de Wiart, Gambier-Parry and Boyd; the rest of the twelve were brigadiers. The script never calls any named brigadier a general, so no individual claim is wrong, and the figure is the Tier 1 source's own. Leave the line. **Add the usage caveat to the log row** so a future build agent does not "correct" it.

**4.2 "Six months of digging."** The NZ Gazette gives 18 September 1942 to "the end of February 1943", about five and a half months of digging inside a six-month captivity-to-escape window; DNZB Miles says "five months' tunnelling"; Boyd, Mason, the NZ Army Museum and Wikipedia say six. Six is the majority and matches September to March. Keep it. **Add the DNZB and Gazette variants to the log row**, which currently says six "is agreed" across the sources. It is not universally agreed.

**4.3 Combe's rank at Beda Fomm.** Long's official history calls him "Colonel Combe of the 11th Hussars" in February 1941; he held the temporary rank of brigadier by his capture in April 1941. The script introduces him by his Vincigliata rank and then gives an earlier credential, which is normal biographical practice and not an error. The visual tag's 11th Hussars cap and armoured car are correct.

**4.4 "one hand" (Act 6) versus "an arm" (Act 9).** Each follows the source cited in that act: TNA says "a missing hand", Garland and Smyth say "he had lost an eye and an arm". Both are Tier 1 and the script is being faithful to each, but a viewer hears an inconsistency inside three minutes. Optional word-neutral fix in section 6.

**4.5 "The empty sleeve was the disguise."** The log's flag is honest and, in my judgement, sufficient. The word "disguise" is not in Garland and Smyth. It is a paradox line, and the risk of a viewer reading it as "he wore a fake sleeve" is closed by the very next beat, which states the actual mechanism. The gloss is also not attributed on camera to any source, which is the correct handling. No change required.

**4.6 "An Italian general put a train on."** That the train was arranged by a general is Neame p. 314 via Wikipedia, Tier 2. The log says the Tier 2 specifics "are NOT spoken", but the general is spoken, minus his name. Minor log imprecision. **Correct the log row wording**; the spoken line is fine.

**4.7 "Fourteen other ranks."** The number itself is Neame's own memoir via Wikipedia, and Neame was the senior officer who led them out, so it is a participant's roster figure rather than a contested statistic. I am not blocking the spoken line. I am blocking the log row that claims TNA carries it. See blocking issue 6, and the optional attributed rewrite in section 6.

**4.8 Mason's "lost his life" wording.** I could not open Mason directly. NZETC is behind an Incapsula wall and the Wayback set for *Prisoners of War* covers chapters 2, 4, 6, 7 and 11 only, none of which carries the Vincigliata narrative. The quotation is carried from Wave 1 and is corroborated in shape by the DNZB entry saying something different, which is the whole point of the beat. **The log's "TIER 1 CARRIED" label on this row is honest and I am leaving it.** If production wants belt and braces, a human can open nzetc.victoria.ac.nz in a normal browser in two minutes.

**4.9 "exhausted and in despair" versus the DNZB's "in a state of depression and exhaustion".** The beat is framed as reporting what the DNZB says. "Despair" for "depression" is a fair and arguably kinder rendering and no reasonable viewer would call it an error, so I am not blocking it. An exact-match option is offered in section 6 if the channel wants the line to survive a frame-by-frame comparison against the source. Note also that the DNZB says "committed suicide" and the script says "took his own life", which is the better modern phrasing and I endorse it.

**4.10 "that December" for Hargest reaching England.** Mason says December, DNZB says "late in 1943", and only an unopened CWGC story page is reported to say November. Two Tier 1 sources are compatible with December and nothing I could open contradicts it. Not blocking. If production can open the CWGC page before the record, do so.

**4.11 The Carton de Wiart portrait tag says "aged sixty-two" and is REUSED in Act 9**, where the scene is August 1943 and he was 63. It is an image-prompt description, not spoken, and the REUSE requires a byte-identical tag. Trivial. No action.

**4.12 The NEAME character-voice line.** ITALY and ROME are national caricatures, which is the house convention and reads as such. NEAME is a named, real, identifiable man, and his invented line is delivered over a shot of the real document TNA reproduces. The substance is accurate to what TNA says the document does, and the PRODUCTION NOTES declare it as character voice. I am not blocking it, but it is the one place in the script where a viewer could reasonably mistake invented words for a quoted document. Optional fix in section 6.

---

## 5. AUDIT OF THE FACT-CHECK LOG AND THE SOURCES BLOCK

I audited every row against what the cited source actually contains. **The direction of error in this script is mostly the opposite of the last three episodes: seven rows UNDERSTATE their support.** That is the safe direction and it is worth saying plainly, because it means this writer was not inflating. But there are four rows that overstate, and one public-facing SOURCES defect, and those are blocking.

### Rows that OVERSTATE (blocking)

| Row | What it claims | What is true |
|---|---|---|
| "Fourteen other ranks left with the officers; Sergeant Bain wired the tunnel" | "TIER 1 / PRIMARY" and "the fourteen other ranks from Neame **via TNA** and Wikipedia" | **TNA does not carry the other ranks at all.** The research report says so twice, in the LATE TIER 1 ADDITION ("TNA does not mention them at all in the evasion") and in STILL NOT FOUND. The number is Neame *Playing With Strife* p. 314 via Wikipedia, Tier 2, single line. Bain and the wiring are correctly PRIMARY. |
| "Combe trapped an Italian army at Beda Fomm" | Status **TIER 2 HEDGED** | The log's own status key defines TIER 2 HEDGED as "audible hedge in narration". **There is no hedge.** The row even admits it: "Script states it flatly as a one-line credential." A status label that contradicts its own note is the exact defect class that failed the last three episodes. (The underlying fact is fine and I have now raised it to Tier 1.) |
| "Wire 12 feet high, netting laced with brambles, cut at ground level" | Status **TIER 2 HEDGED**, "Single-sourced Tier 2 (Wikipedia 'Reginald Miles')" | **No hedge is spoken**, and the sourcing is wrong in the *safe* direction: the Wikipedia passage is a blockquote of the **NZ Gazette DSO citation of 21 September 1944**, a Tier 1 primary document. Both halves of the row are wrong. |
| "Gallery never less than 18 inches wide" | "The script uses Boyd, not the conflicting **Tier 2** '3 foot by 3 foot'" | The 3x3 figure is **not Tier 2**. It is the NZ Gazette DSO citation, Tier 1. The row demotes a competing Tier 1 source to justify the choice. That is a tier-manipulation defect even though Boyd is probably the better source. |

### SOURCES block: one untrue availability claim (blocking)

The block gives the TNA blog as a live link:

> `https://blog.nationalarchives.gov.uk/a-great-escape-from-castello-di-vincigliata`

The research report states plainly that this URL "now 301s into the UK Government Web Archive, which sits behind a CAPTCHA", and that the article text was read from an Internet Archive capture of 10 July 2025. **A viewer clicking the link in the description will not reach the article.** This is the same defect class as the previous episode's "the full text is available" claim. It must be annotated. This is the most-cited source in the whole script, so it matters.

Everything else in SOURCES checks out. The three `[NOT FOUND: exact item URL]` markers are honest. HyperWar resolves and I read Garland and Smyth there this pass. The NZETC claim for Mason is true for a human browser. All seven book citations (Felton, Tudor, Hargest, Neame, Carton de Wiart, Ranfurly, Absalom) have correct authors, titles, publishers and years, and none carries an access claim. The "Further reading" framing of Felton correctly kills any "nobody has told this story" implication.

### Rows that UNDERSTATE (not blocking, but fix them so downstream agents do not weaken good material)

1. **Beda Fomm** is Tier 1: Gavin Long, *To Benghazi*, Australian official history, ch. 11.
2. **O'Connor's 130,000 prisoners** is Tier 1: same chapter, verbatim.
3. **The 12-foot wire and the pliers at ground level** are Tier 1 primary: NZ Gazette, 21 Sept 1944.
4. **Hargest ashore on D-Day** is Tier 1: NZHistory (Manatu Taonga), verbatim.
5. **Hargest killed by shell fire** is Tier 1: DNZB, verbatim. The log rates it Tier 2.
6. **Miles's only son and HMS Glorious** is Tier 1: DNZB, verbatim. The log rates the son Tier 2. (The log also asserts "HMS Glorious sunk 8 June 1940 is uncontested"; the DNZB says 9 June. No date is spoken, so this is harmless, but "uncontested" is not true.)
7. **"Todhunter and Stirling dug"** is Tier 1 for both, not Tier 2 for Todhunter: NZ Gazette, "All officers and other ranks worked".
8. **The 29 March break-out** now has a third independent Tier 1 line and the conflict with TNA is 3 to 1, not 1 to 1. The row should say so.
9. **The "verify before lock" flags on Hargest's MP status and the DNZB Miles entry are both now CLEARED**, and the D-Day line is anchored. Replacement row text is in section 6.

---

## 6. ISSUES TO FIX, WITH VERBATIM REPLACEMENT WORDING

**Net spoken word change across all five narration fixes: ZERO. The script stays at 1,400 spoken words, 112 beats, 112 visuals, no beat over 14 words, no em-dashes.**

### BLOCKING 1. "Two years a prisoner" is wrong by eight months, in a straight human-cost beat

- **Where:** ACT 11, the Hargest beat.
- **What is wrong:** Hargest was captured at Sidi Azeiz on **27 November 1941** (Mason's footnote "p.w. 27 Nov 1941", and DNZB: "Hargest was captured on 27 November 1941, when his headquarters was overrun") and went out through the tunnel on **29 March 1943**. That is **sixteen months**, not two years. The research report itself says "sixteen months in a castle" in its Miles section and then says "He had been a prisoner for two years" in its Hargest section; the writer carried the wrong one. It is an inflated number in the most sensitive act in the episode.
- **OLD (12 spoken words):** `Fifty-two. Member of parliament. Two years a prisoner. He could have stopped.`
- **NEW (12 spoken words):** `Fifty-two. Member of parliament. Sixteen months a prisoner. He could have stopped.`
- Net change 0. The beat loses nothing; "sixteen months" is if anything a harder, more specific number.

### BLOCKING 2. "changed trains at Como" contradicts the primary escape document

- **Where:** ACT 7, first beat.
- **What is wrong:** TNA's blog says they "changed trains at Como", but the **NZ Gazette DSO citation**, written from the escapers' own reports, says they "caught a train to Milan where they went to the **North station**. They caught a train to Como and **walked** towards Chiasso." The change of trains was at Milan. Two Tier 1 sources in unresolved conflict on a spoken specific. The fix removes the conflict rather than picking a side.
- **OLD (13 spoken words):** `Hargest and Miles changed trains at Como and took the road toward Chiasso.`
- **NEW (13 spoken words):** `Hargest and Miles got off at Como and took the road toward Chiasso.`
- Net change 0. Both Tier 1 sources agree they left the train at Como and walked toward Chiasso, so the new line is true on either account.

### BLOCKING 3. "Almost no guard against escape" is contradicted by a Tier 1 primary document, and is the pre-escape guard framing the commission forbade

- **Where:** COLD OPEN, beat 2.
- **What is wrong:** The **NZ Gazette DSO citation** opens "This camp was **extremely well guarded** and in consequence it was decided that the only possible method of escape would be by way of a tunnel." The commission also forbade any pre-escape guard characterisation, and only the post-escape garrison figure is sourced. What TNA actually supports is the *assumption*, not the absence of guards, and the very next beat already says so. The current line asserts a physical-security fact the script does not have and a primary document denies.
- **OLD (12 spoken words):** `Twenty-five prisoners. A dozen of them generals. Almost no guard against escape.`
- **NEW (12 spoken words):** `Twenty-five prisoners. A dozen of them generals. Nobody expected them to escape.`
- Net change 0. This is also a better cold open: it sets up "Not laziness. The Italians had made an assumption about senior officers" instead of duplicating it.

### BLOCKING 4. "A German sergeant" invents a rank the source does not give

- **Where:** ACT 10.
- **What is wrong:** TNA's wording is "once even directed by a German **non-commissioned officer** who didn't know who they were". "Sergeant" is a specific rank the source does not state. A fabricated specific, small but real, and free to fix.
- **OLD (14 spoken words):** `Then, bicycles. A German sergeant, not knowing who they were, pointed them the way.`
- **NEW (14 spoken words):** `Then, bicycles. A German soldier, not knowing who they were, pointed them the way.`
- Net change 0. The joke is unchanged. **The `[VISUAL:]` tag on this beat should also change "A German sergeant" to "A German soldier"** so the picture does not paint chevrons the source does not support. That tag is not spoken and does not affect word count.

### BLOCKING 5. "Never less than eighteen inches wide" is a spoken number in an unresolved Tier 1 conflict

- **Where:** ACT 4.
- **What is wrong:** Boyd's own notes give "never less than 3 1/2 feet by 1 1/2 feet". The **NZ Gazette DSO citation** gives "a **3 foot by 3 foot** tunnel, 40 feet long". These conflict on the width, 1.5 feet against 3 feet, and both are Tier 1. The log dismisses the 3x3 figure as Tier 2, which is false. Boyd is probably the better source, because he dug it and wrote the figure down at the time, but an unattributed flat number cannot carry an unresolved conflict. The script already uses on-camera attribution twice for exactly this reason ("Boyd wrote the tool list himself", "Neame put the new garrison at"). Do the same here and the number ships.
- **OLD (12 spoken words):** `Ten feet down, then a gallery. Never less than eighteen inches wide.`
- **NEW (12 spoken words):** `Ten feet down, then a gallery. By Boyd's measure, eighteen inches wide.`
- Net change 0. "By Boyd's measure" is four syllables of insurance and it matches the act's established voice.

### BLOCKING 6. FACT-CHECK LOG row claims TNA support that does not exist

- **Where:** FACT-CHECK LOG, the "Fourteen other ranks left with the officers; Sergeant Bain wired the tunnel" row.
- **What is wrong:** the row reads "TIER 1 / PRIMARY, STRAIGHT | Bain and the wiring from Boyd's notes; the fourteen other ranks from Neame **via TNA** and Wikipedia." TNA does not carry the other ranks anywhere. The research report says so explicitly, twice.
- **Replacement row, paste over the existing one:**

```
| **Fourteen other ranks left with the officers; Sergeant Bain wired the tunnel** | **BAIN PRIMARY; FOURTEEN TIER 2, SINGLE LINE**, STRAIGHT | Bain and the wiring from Boyd's notes, primary. **The figure of fourteen is Neame, *Playing With Strife*, p. 314, via Wikipedia "Vincigliata", Tier 2 and single-sourced. TNA does not carry the other ranks anywhere and must not be cited for them.** CQMS Morgan led them out. Neame separately says "thirteen NCOs and men" did the watching during the escape itself, which is a different count of a different thing and not a conflict. |
```

### BLOCKING 7. Two FACT-CHECK LOG rows use a status label that contradicts the log's own key

- **Where:** the "Combe trapped an Italian army at Beda Fomm" row and the "Wire 12 feet high" row, both statused **TIER 2 HEDGED**, which the key defines as "audible hedge in narration". Neither line is hedged. Both are now Tier 1 anyway.
- **Replacement rows, paste over the existing ones:**

```
| Combe trapped an Italian army at Beda Fomm | TIER 1 | Gavin Long, *To Benghazi*, Official History of Australia in the Second World War, ch. 11 (via HyperWar): Combe of the 11th Hussars commanded the flying column that took position astride the Benghazi to Agedabia road at Sidi Saleh on 5 Feb 1941, and the remnant of the Italian Tenth Army surrendered on the 7th. Long calls him "Colonel Combe" at the time; brigadier was his later temporary rank, and the script introduces him by his Vincigliata rank, which is normal practice. Stated flatly and that is now correct. |
```

```
| Wire 12 feet high, cyclone netting laced with brambles, cut with pliers at ground level | TIER 1 PRIMARY | **Citation for Miles's bar to the DSO, *The New Zealand Gazette*, 21 September 1944**, verbatim: "The frontier consisted of heavy cyclone netting 12 foot high interlaced with brambles and with small bells near the top. They cut the wire with pliers at ground level without making much noise." Wikipedia "Reginald Miles" reproduces this as a blockquote; the underlying document is official and contemporaneous. **Supersedes the earlier "single-sourced Tier 2" assessment.** Mason's "crawled through" is a looser summary of the same event; the script says cut, which both TNA and the citation support. The small bells near the top are not spoken and are available if a beat is ever needed. |
```

### BLOCKING 8. SOURCES makes an access claim that is not true

- **Where:** SOURCES, "Primary and official", first bullet.
- **What is wrong:** the TNA blog URL is given bare. It now 301s into the UK Government Web Archive behind a CAPTCHA, so a viewer clicking it from the YouTube description does not reach the article. This is the same defect that failed a previous episode.
- **Replacement bullet, paste over the existing one:**

```
- Katrina Lidbetter and Keith Mitchell, "A Great Escape from Castello di Vincigliata", The National Archives (UK) blog, 30 September 2024. Originally published at https://blog.nationalarchives.gov.uk/a-great-escape-from-castello-di-vincigliata ; that address now redirects into the UK Government Web Archive, so the most reliable route to the article text is the Internet Archive capture of the original URL.
```

### BLOCKING 9. The gallery-width row demotes a Tier 1 source

- **Where:** the "Gallery never less than 18 inches wide" row, which calls the competing 3x3 figure "the conflicting Tier 2 '3 foot by 3 foot'".
- **Replacement row, to be used together with the narration fix in blocking 5:**

```
| Gallery, by Boyd's measure eighteen inches wide | PRIMARY, **ATTRIBUTED ON CAMERA, CONFLICT NAMED** | Boyd's notes: begun at 4 feet by 2 feet and "never less than 3 1/2 feet by 1 1/2 feet". **The citation for Miles's bar to the DSO, *The New Zealand Gazette*, 21 September 1944, gives "a 3 foot by 3 foot tunnel, 40 feet long". That is Tier 1, not Tier 2, and it conflicts with Boyd on the width.** The script therefore attributes the figure to Boyd out loud rather than asserting it, on the ground that Boyd dug the gallery and recorded the dimension at the time. Overall length is still NOT stated: 36 feet (Boyd family talk), 40 feet (NZ Gazette, NZ National Army Museum and Wikipedia). |
```

### Log rows that should be REWRITTEN because they now understate (do these in the same pass)

```
| Hargest a sitting member of parliament | **TIER 1, VERIFIED, FLAG CLEARED** | Dictionary of New Zealand Biography, J. A. B. Crawford, "Hargest, James", Te Ara: elected Invercargill 1931, "Four years later he switched to the rural Southland seat of Awarua, **which he held until his death**." Independently corroborated by the existence of the 1944 Awarua by-election. Spoken twice, in Act 1 and Act 11, and correct in both. |
```

```
| **Hargest ashore in Normandy on D-Day as New Zealand's observer, killed by shell fire 12 August 1944** | **TIER 1 THROUGHOUT, VERIFIED, FLAG CLEARED**, STRAIGHT | NZHistory (Manatu Taonga, NZ Ministry for Culture and Heritage), "D-Day and the battle for Europe", verbatim: "**Brigadier James Hargest, New Zealand's official observer with the Allied forces, went ashore with the British 50th Division on D-Day.**" Corroborated by the DNZB: "He was attached to the British 50th Division, which landed in Normandy on D-Day", and for the death, verbatim: "**Wounded in June, Hargest was killed by shell fire on 12 August 1944.**" Mason's footnote agrees on the date. The script does not name the division. |
```

```
| **The Dictionary of New Zealand Biography says that, exhausted and in despair, he took his own life** | **ATTRIBUTED ON CAMERA, TIER 1, VERIFIED, FLAG CLEARED** | Garry James Clayton, "Miles, Reginald", *Dictionary of New Zealand Biography*, first published 2000, Te Ara, verbatim: "**However, on 20 October 1943, in a state of depression and exhaustion, he committed suicide in Figueras, north of Barcelona.**" Te Ara itself is behind Cloudflare; the entry was read from the Internet Archive capture of the official Te Ara print URL, teara.govt.nz/en/biographies/5m46/miles-reginald/print, capture 4 October 2023. The entry's bibliography is Hargest *Farewell Campo 12*, Murphy *2nd New Zealand Divisional Artillery*, and the *Evening Post* obituary of 26 Oct 1943. The script attributes rather than asserts, names no method, and does not use it as a reveal. **The description's mental-health support line remains mandatory.** |
```

```
| O'Connor destroyed the Italian Tenth Army, over a hundred thousand prisoners | **TIER 1** | Gavin Long, *To Benghazi*, ch. 11, verbatim: O'Connor's corps "had advanced 500 miles and taken **130,000 prisoners**, 400 tanks and 1,290 guns", having destroyed ten Italian infantry divisions. "Over a hundred thousand" sits safely beneath that. Do not add tank or gun counts on screen. |
```

```
| **Miles was fifty; his only son was killed on HMS Glorious three years earlier** | **TIER 1**, STRAIGHT | DNZB, verbatim: Miles and his first wife "were to have four daughters and a son"; "he lost his son Reginald, a Fleet Air Arm officer, when the aircraft carrier Glorious was sunk"; "He was survived by his wife and daughters." Born 10 Dec 1892, died 20 Oct 1943, so fifty. Glorious June 1940 to October 1943 is three years and four months. Note the DNZB dates the sinking 9 June and other sources 8 June; **no date is spoken, so this does not matter, and the log must stop calling it "uncontested"**. |
```

```
| **Todhunter and Stirling dug and stayed behind** (outro) | **TIER 1 FOR BOTH HALVES** | "Dug": citation for Miles's bar to the DSO, *The New Zealand Gazette*, 21 September 1944, verbatim: "**All officers and other ranks worked, with the exception of one officer who was awaiting repatriation.**" Corroborated by Mason: "All the officers and other ranks in the camp assisted in some way." This supersedes the earlier "Todhunter as a digger is Wikipedia, Tier 2" assessment. "Stayed behind": TNA blog (WO 208/3484) and the Pegasus transcription of WO 208/3320/94. The script still speaks no pairing, shift or date. |
```

```
| Break-out on the evening of 29 March 1943, in rain | **TIER 1, THREE INDEPENDENT LINES**, **CONFLICT NAMED** | Mason gives 29 March in rain; MSMT's Boyd index independently gives 29 March; **the NZ Gazette DSO citation independently gives "At 2100 hours on the 29th March, 1943"**. **The National Archives blog gives the night of 30 March and is now the lone outlier, three to one.** The script speaks 29 March once and speaks no crossing date. The Gazette also gives the crossing as 30 March and release in Berne on 2 April, which sits with Mason against TNA's 1 April. Still do not average and still do not say "the twenty-ninth or thirtieth" on camera. |
```

Add to SOURCES, under "Primary and official":

```
- Citation for the bar to the Distinguished Service Order awarded to Brigadier R. Miles, published in *The New Zealand Gazette*, 21 September 1944. The contemporaneous official account of the escape, written from the escapers' own reports: the tunnel's dimensions, the 18 September 1942 start, "All officers and other ranks worked", the 2100 hours break-out on 29 March 1943, the journey by train to Milan and Como, the twelve-foot cyclone netting laced with brambles, the wire cut with pliers at ground level, and the crossing into Switzerland.
- New Zealand Ministry for Culture and Heritage (Manatu Taonga), "D-Day and the battle for Europe", NZHistory. https://nzhistory.govt.nz/war/d-day  The source for Hargest going ashore with the British 50th Division on D-Day.
- J. A. B. Crawford, "Hargest, James", *Dictionary of New Zealand Biography*, Te Ara. The source for Hargest holding the Awarua seat until his death, and for his death by shell fire on 12 August 1944.
```

Also change the existing Te Ara bullet to give the entry's own address, `https://teara.govt.nz/en/biographies/5m46/miles-reginald`, rather than the bare domain.

---

## 7. NON-BLOCKING SUGGESTIONS (all word-neutral, take them or leave them)

**S1. Internal consistency on the maiming (see note 4.4).** Act 6 says "one hand", Act 9 says "an arm", and Act 9's imagery is an empty sleeve.
- OLD (14 words): `Carton de Wiart was sixty-two, one eye, one hand, and no Italian. Blending in.`
- NEW (14 words): `Carton de Wiart was sixty-two, one eye, one arm, and no Italian. Blending in.`
- Net 0. Aligns with Garland and Smyth, with Act 9, and with the empty-sleeve visual. TNA's "missing hand" is the looser of the two Tier 1 phrasings.

**S2. Exact match to the DNZB's wording on Miles (see note 4.9).** Only if the channel wants the line to survive a frame-by-frame comparison.
- OLD (10 words): `That, exhausted and in despair, he took his own life.`
- NEW (10 words): `That, in depression and exhaustion, he took his own life.`
- Net 0. I do not recommend this one strongly. "Despair" is warmer and reads better on a still, and the beat is attributed rather than quoted. Ryan's call.

**S3. Attribute the fourteen (see note 4.7).** Converts the one remaining single-sourced Tier 2 number in Act 11 into an attributed one.
- OLD (12 words): `Fourteen other ranks left with the officers. Sergeant Bain wired the tunnel.`
- NEW (12 words): `By Neame's count, fourteen other ranks left. Sergeant Bain wired the tunnel.`
- Net 0. Matches the attribution pattern already used for Boyd's tool list and Neame's garrison figure.

**S4. The NEAME character-voice line (see note 4.12).** If Ryan wants zero risk of invented words being heard as a quoted document, the cheapest fix is not to the line but to the picture: change that beat's `[VISUAL:]` from the reused complaint-letter tag to a shot of Neame writing. That breaks the REUSE and costs one generation, so it is a budget decision, not an accuracy one. **My assessment is that the current handling is defensible as written** and I am not pressing this.

**S5. Log housekeeping.** Add the Italian-usage caveat to the "dozen generals" row (note 4.1), the DNZB and Gazette variants to the "six months" row (note 4.2), and fix the "an Italian general put a train on" row's claim that the Tier 2 specifics are not spoken (note 4.6).

---

## 8. TONE CHECK

**Human-cost beats played straight: YES. No joke sits on, immediately before, or immediately after any of the twenty-one declared straight beats. No cuts required for tone.**

I checked adjacency in **both** directions on all twenty-one, which is the specific test the previous episode failed.

| Straight run | Beat immediately BEFORE | Beat immediately AFTER | Verdict |
|---|---|---|---|
| ACT 6, three beats (San Vittore), from "Two days. He refused to admit he was a prisoner of war." to "He bought two days for men he could not know were free." | ACT 6: "But in Milan, Combe had done something the popular telling leaves out." Neutral setup, no punchline. The nearest wry line, "Not indestructible. Just extremely recognisable.", is **three** beats earlier. | ACT 7 opener: "Hargest and Miles changed trains at Como and took the road toward Chiasso." Flat, factual, no joke. | CLEAR |
| ACT 11, all seventeen beats | ACT 10 closer: "They landed at Termoli. But not everyone got a road home." A pivot line, not a punchline. The last joke in Act 10 is the German soldier beat, **three** beats earlier. | The first beat of the OUTRO, which is itself straight. | CLEAR |
| OUTRO beat 1: "Six went out. Two got clear. Within eighteen months, both were dead." | ACT 11's last beat, itself straight. | OUTRO beat 2: "Neame designed it. Boyd made the knives. Todhunter and Stirling dug and stayed behind." A roll-call, delivered flat. No punchline. | CLEAR |

**Internally**, all seventeen Act 11 beats and all three Act 6 beats are free of jokes, bits and winks. The three hardest lines are correctly identified in Build notes and correctly marked for the longest holds.

**The Zeppelin L 59 teaser does not read as a punchline after Hargest's death.** The comic line, "An airship built so the crew could take it apart and eat it", is the **fifth** beat of the outro and the **fourth** beat after the last straight beat, roughly nineteen seconds later, with the subscribe call to action and a factual figures beat between. That is ample separation.

One small correction to the PRODUCTION NOTES prose, non-blocking: the notes say "the comedy does not resume until the subscribe call to action, three beats after the last straight beat." The subscribe call to action is not comedy, and the first comic line is four beats after. The note errs in the safe direction; tighten it if the file is being edited anyway.

**Ensemble framing: PASS, and it is the best thing about this script.** Carton de Wiart appears in exactly three places, is never called unkillable, indestructible or the leader, and Act 6 puts an explicit on-screen refusal of the listicle lane over a visual of greyed-out competitor thumbnails. Neame gets the design, Boyd the tools, Combe the two days at San Vittore, and the two New Zealanders get Switzerland, the title beat and the ending. The title sells the ensemble. The thumbnail note correctly steers to the hole and the croquet hoops rather than a famous face. **The injuries are used only as both Tier 1 sources use them, as the reason he was conspicuous on the run and the reason the Italians chose him as credentials, and both uses cut against the hero framing.** No drift into indestructibility anywhere.

**The NCO gap beat is present and honest.** "What happened to them, I cannot tell you. It is not recorded." That is exactly what both research waves found, and stating it on camera rather than skipping it is the right call. It is also, correctly, followed by "The generals wrote books. The men who dug beside them did not.", which is the moral of the episode and is verifiable: four of the officers published memoirs and no other-ranks account was found.

---

## 9. COLD READ NOTES

- **TTS hygiene is clean.** No digits, no brackets, no markdown, no stage directions and no curly quotes anywhere inside a spoken line. Every number, date and designation is spelled out ("Campo P.G. twelve", "Zeppelin L fifty-nine", "nineteen forty-three"). Nothing will trip the voice model.
- **"Boyd on the fit."** (Act 3) is the one line that may read oddly aloud. It is a headline construction, not a sentence. It works if the read puts a full stop after "fit" and treats the next clause as the quotation. Flag it for the VO pass rather than rewriting it, because the attribution is doing real accuracy work.
- **"General Sir Richard O'Connor"** (Act 1). He was a lieutenant general in 1941 and a full general later. The post-war styling is standard and no source is contradicted, so leave it.
- **The cold open is one beat away from being excellent.** Beat 2's current claim is the weak link (blocking 3) precisely because it duplicates beat 3 and 4. With the replacement wording, beats 2, 3 and 4 become setup, misdirection and payoff instead of assertion, assertion, assertion.
- **"Then it rained."** closing Act 4 into Act 5's rain is a good hinge.
- **"He negotiated nothing. He was never the negotiator. He was the paperwork."** is the strongest line in the script and it is the most heavily sourced one. It is verbatim-supportable from the US Army official history on all three clauses.
- **The Act 6 refusal beat** ("So that is the honest version. Not indestructible. Just extremely recognisable.") does the commission's job without a gotcha, and the Act 9 correction is correctly phrased as "what he was actually there for" rather than a debunk. **I checked specifically for a triumphant gotcha built on TNA's loose "to negotiate peace terms" clause and there is none.** The proportion is right.
- **"You have never heard of either."** is aimed at the two New Zealanders, not at the coverage. No "nobody has told this story" framing anywhere, and Felton's *Castle of the Eagles* is credited in SOURCES as a full-length history of exactly this escape. Correct.
- **Nothing in the script speaks a forbidden item.** No 1,500 denominator, no pre-escape ratio, no "near Como", no starvation framing, no spoken "twenty-ninth or thirtieth", no hard crossing date, no tunnel length, no completion date, no 120 Germans, no 29 October, no Gambier-Parry, no Olympic medal, no "hardly a centimetre out".
- **`San Vittore` is spelled correctly** in the visual tag and the log. TNA's "San Vittorio" appears exactly once in the file, inside the log row that flags it as TNA's error. Correct handling.
- **`Air Vice Marshal` is used**, not TNA's "Air Marshall". Correct.
- The `[VISUAL:]` tag on the German NCO beat should change with blocking 4. It is the only visual tag that asserts an unsourced specific.

---

## 10. SUMMARY OF THE GATE

**9 blocking issues. 5 non-blocking suggestions.**

Blocking, by kind:
- **5 in the spoken narration** (1 numeric error, 1 Tier 1 versus Tier 1 conflict, 1 claim a primary document contradicts, 1 fabricated rank, 1 unattributed number carrying an unresolved conflict). **All five have word-neutral replacements. Net spoken change is zero, so the episode stays at 1,400 words and above the eight-minute mid-roll floor.**
- **3 in the FACT-CHECK LOG** (one row citing TNA for content TNA does not contain; two rows carrying a status label that contradicts the log's own key; one row demoting a Tier 1 source to Tier 2 to justify a choice).
- **1 in the public-facing SOURCES block** (an access claim that is not true).

Nothing here is a structural or a tone failure. The mechanical state is perfect, the timecodes are exact, the ensemble commission is obeyed, the tone-adjacency rule that failed the previous episode is obeyed in both directions on all twenty-one straight beats, and the two claims the writer honestly flagged as unverified both turned out to be **true and Tier 1 anchorable**. The dominant sourcing error in this script is understatement, not inflation, which is the opposite of the last three episodes and worth telling the writer.

But five spoken defects, four of them factual, in an episode whose brand is accuracy, plus a log that cites a source for content it does not contain and a description link that does not resolve, is a fail. Every one of them is a paste-in fix and none of them costs a word.

**Re-run the mechanical script after the fixes and confirm SPOKEN 1400, beats 112, visuals 112, REUSE 9, em 0, inlineTONE 0, OVER14 empty. If those hold, this passes on the re-look.**

VERDICT: FAIL

# QA Report v4: Ten Prisoners Stole a Nazi Bomber at Lunchtime (script-v2-final.md)

**Reviewed:** `script-v2-final.md`, 112 scenes, 1,404 spoken words, after the third and final allowed revision.
**Method:** structural budget measured with a parser I wrote from scratch, then cross-checked against the folder's `verify_script.py` (both agree exactly). Every checkable claim re-verified from primary museum and memorial pages and from the **raw wikitext** of the cited encyclopedia articles, pulled through the MediaWiki API so footnote attachment could be inspected sentence by sentence. `research-report-v2.md` was not used as evidence at any point. Every URL in the SOURCES block resolved. Nothing was taken on the revision's word.

**Result: FAIL**, narrowly, on four items. Three of the four are one-line fixes.

The revision did what it said it did on the five prior blocking items, and I confirmed each against source rather than against the file's own account of itself. B-1's cut is real and thorough. The structural budget, tone discipline, act hooks, arithmetic, names, dates and casualty counts are all clean, and several of them are better sourced than any previous pass recorded. What blocks the ship is the same disease for the fourth time, in two smaller places: a four-word residue of the cut learning chain survives at scene 69, and scene 104 keeps the surviving half of the exact unfootnoted German Wikipedia sentence whose other half this revision cut, while the log calls it "Verified and unanimous". Two SOURCES-block entries also assert that a source was read when it demonstrably was not.

---

## Prior-defect closure

| Item | Closed? | Notes |
|---|---|---|
| **B-1** (F-1 / N-1) German-pilot lesson, translator, start-up-checks observation | **YES in the learning sequence, NO globally** | I pulled the raw wikitext of `Michail Petrowitsch Dewjatajew` again. The paragraph reads "…beschädigte Startbahnen ausbessern`<ref name="Schilling155" />` und dort abgestellte Erprobungsflugzeuge tarnen … So beobachteten sie die Startvorbereitungen der deutschen Piloten, ein Mitglied der Gruppe übersetzte die deutschen Beschriftungen … Der Pilot zeigte dabei Dewjatajew bereitwillig alle dafür notwendigen Abläufe und Handgriffe." Confirmed: the one footnote attaches to runway repair, everything after is unreferenced. **All three claims are gone from the body.** Grep over the whole file returns the translator, the start-up-checks beat and the pilot demonstration only inside the notes and the log, which record the cuts. Scene 55's "not in dispute" sentence is deleted and not replaced. No line anywhere in the file calls this material undisputed, documented, on the record or confirmed. The old title is withdrawn and the description no longer touches it. **But one four-word residue survives at scene 69. See V-1.** |
| **B-2** (F-2) Bunkerbau 295 | **YES** | "295" appears nowhere except the log entry explaining the cut. I re-pulled `Peenemünde-West` wikitext: "Das Kommando „Bunkerbau" bestand aus 400 Häftlingen. Der Einsatz dieses Kommandos wird von Zeitzeugen als der brutalste beschrieben. Insgesamt 295 Tote sind dokumentiert, einschließlich deutscher Bauarbeiter und Häftlinge." Scene 34 asserts no number and tracks the "brutalste" testimony. No collision with the 248 at scene 31. |
| **B-3** (F-3) "nine surfaces" | **YES** | Gone from narration (scene 20: "A track of different surfaces") and from visual 20. I re-read the Sachsenhausen Memorial history page in full: "a shoe testing path with various different surfaces which was laid out around the parade ground, and internees had to march on it for days on end with full packs to test the suitability of various shoe sole materials." No count anywhere. Scene 21's "for industry" and scene 22's "commercial test data" are both carried by "under the command of civilian officials from the 'Reich' Ministry of Economics". |
| **B-4** (F-4) Special Camp No. 7 | **YES in narration** | Scene 99 "Russian records put him inside", scene 101 opens "If so". Act retitled "There was no parade". de.wikipedia raw confirms the competing account ("in eine Strafeinheit der Armee versetzt") and the shared half ("bis September 1945 in Haft und wurde immer wieder verhört"). The unanimous half is what carries the act. Chronology wrinkle unchanged, see MINOR-3. |
| **B-5** (F-5) "never on the Army site" | **YES, and now better sourced than recorded** | Scene 107 reads "He was never inside the rocket programme. He worked the Luftwaffe airfield." No collision with the Korolev walk-around at 105. I also found **independent corroboration nobody has logged**: ru.wikipedia's biography says "Поскольку Девятаев служил в аэродромной команде, а ракетный полигон находился в отдалении, ничего сверхсекретного он поведать не мог", and de.wikipedia's `Peenemünde-West` says the Luftwaffe station "war im Unterschied zur Heeresversuchsanstalt … in der Regel nicht direkt an der Entwicklung … beteiligt". The claim no longer rests on the Förderverein newsletter alone. |
| **N-1** rebuilt learning chain | **YES** | Scenes 46 to 55 now carry the sequence on the scrap heap alone. ru.wikipedia raw: "изучал приборные панели и оборудование кабины самолёта Heinkel-111 по фрагментам кабин разбитых машин, находившихся на свалке рядом с аэродромом", with `sfn Девятаев 1972 с=182` and `sfn Кривоногов 1963 страницы=153` closing the passage. de.wikipedia independently mentions instruments from aircraft wrecks. Footnoted and multi-sourced. Correct call. |
| **N-2** description puts words in the museum's mouth | **YES** | "The museum on the site says so itself" is gone. Grep confirms the string appears nowhere in the file. I re-read the museum's Dewjatajew page in full and re-confirm it says nothing about intelligence value or the V-2 programme, so the deletion was the right remedy. |
| **N-3** cold open states "21 minutes" as fact and says "home" | **YES** | Scene 4 now reads "Within the hour ten men will steal a bomber and fly it out." No number, no "home". The attributed version at scenes 82 to 83 is untouched and still correctly hedged with "By his own account". ru.wikipedia's 300 to 400 km landing distance is no longer contradicted. |
| **N-4** landing distance stated flat | **YES, with a residual word** | "eight kilometres" is gone. Scene 90 reads "just behind the Soviet front line, near Woldenberg", which is exactly the second option the pass-3 report offered. "Behind the Soviet front line" is Tier 1: HTM Peenemünde says "landete auf einer Wiese hinter der sowjetischen Frontlinie". See MINOR-2 on the word "just". |
| **M-1** log misquotes narration | **YES** | I extracted every log string framed as `Narration … says/reads "…"` and matched it against the spoken text mechanically. All 16 match verbatim (two apparent misses were sentence-initial capitalisation only). Both pass-3 misquotes are corrected. |
| **M-2** Stahms citation | **YES, verified independently** | `Peenemünde-West` raw wikitext: the Stahms and Milch sentence carries `<ref>Volkhard Bode, Gerhard Kaiser: ''Raketenspuren: Waffenschmiede und Militärstandort Peenemünde.'' Ch. Links Verlag, 2011, S. 54.</ref>`. Kanetzki footnotes the following sentences. The log and SOURCES block now say exactly this, and the blanket denial is gone. |
| **M-3** visual 38 | **YES** | Now "Burned rows of barracks at Trassenheide, smoke still rising, nobody in frame." The false "undamaged scientists' housing" is gone. |
| **M-7** header word-count label | **YES** | Header now says "1,404 spoken words". |
| **M-4, M-5, M-6, M-8** | **NO** | All four carried forward unfixed. All four were non-blocking in pass 3 and remain non-blocking. See MINOR section. |

---

## Newly written text, fresh verification

Everything the revision touched was treated as unverified and checked from scratch.

**Scene 4 (rewritten).** "Within the hour ten men will steal a bomber and fly it out." Asserts no time figure and no destination. The theft to airborne window is inside an hour on every account, and "fly it out" means out of the airfield, which is not the disputed part. Clean.

**Scenes 46 to 55 (rebuilt).** Verified beat by beat.
- 46, 47, 48, 49, 50, 54, 55 all ride the scrap heap, which is footnoted in ru.wikipedia to Devyatayev 1972 p. 182 and Krivonogov 1963 p. 153 and corroborated in de.wikipedia. Solid.
- **Scene 51, "Their detail patched bombed runways and hid test aircraft under camouflage nets."** I confirmed the `Schilling155` footnote sits mid-sentence after "ausbessern", with the camouflage clause inside the same sentence. **It is also independently footnoted a second time**, which nobody has logged: `Peenemünde-West` lists the work commandos as "Beseitigung von Bombenschäden … Abdecken von Flugzeugen … Entschärfung von Bomben", carrying `<ref name="Kanetzki" details="66–73">`, a Historisch-Technisches Museum Peenemünde publication. Scene 51 is double-footnoted across two articles and two sources. It is the strongest line in the sequence. It also independently re-footnotes scene 33.
- **Scene 52, "And while they worked, they watched the movements out on the airfield."** ru.wikipedia raw: "Выполняя хозяйственные работы, они со стороны наблюдали за перемещениями на аэродроме." The narration says exactly this and no more. The escalated German version ("Startvorbereitungen der deutschen Piloten") is not used. Correct, and correctly restrained.
- **Scene 53, the new Luftwaffe gag.** "The wrecks are only rubbish. Nobody is going to study the rubbish." Rides the scrap heap, targets German security, sits outside every TONE: STRAIGHT range. It is labelled a gag and not a quotation in the notes. No tone problem.

**Scene 90 (rewritten).** Covered under N-4 above and MINOR-2 below.

**Scene 104 (rewritten).** **This is where the pass fails. See V-2.**

**Visual 38 (rewritten).** Correct, and now matches the record.

**FACT-CHECK LOG.** Quote-accuracy is fixed and verified mechanically. Two entries make sourcing claims the evidence does not support: the scene 104 entry (V-2) and, more mildly, the Bunkerbau entry (MINOR-5).

**SOURCES block.** The seven withdrawn sources are gone: grep returns no HistoryNet, no Defense Media Network, no ODKB or CSTO, no en.wikipedia Walther Dahl, no Mathews or Foreman, no NKVD order numbers, and no "citing Kanetzki" attribution for Stahms. Two entries remain that assert a source was read when it was not. See V-3 and V-4.

**YouTube description.** Every one of its eight factual claims appears in the script, and I checked each against the narration individually. The chapter marks match all eight act boundaries exactly. Clean apart from the two SOURCES lines.

---

## Claim-by-claim verification

| # | Claim (as spoken) | Where | Source(s) checked | Verdict |
|---|---|---|---|---|
| 1 | Title: ten prisoners, a Nazi bomber, at lunchtime | title, TITLE CARD, sc. 60-61 | HTM Peenemünde: "erschlugen er und neun weitere sowjetische Häftlinge einen zu ihrer Bewachung eingesetzten Soldaten … stahlen ein deutsches Bombenflugzeug des Typs He-111"; de.wiki raw: ten prisoners, one guard, "Um die Mittagszeit"; ru.wiki raw: fire lit "примерно в 12 часов", mechanics leaving for the lunch break, the dead guard's watch reading 12:15 | **PASS on all three elements independently.** Museum plus two language editions. Nothing in the title touches a contested claim. |
| 2 | River navigator, then flying school | sc. 7 | de.wiki raw, "Ausbildung zum Schiffsnavigator", 1938, `Schilling153` | PASS |
| 3 | Ju 87 on 24 June 1941, two days into the war | sc. 8-9 | de.wiki raw: "Bereits zwei Tage nach dem deutschen Angriff … am 24. Juni 1941 seinen ersten Abschuss – eine Ju 87", `Schilling153` | PASS |
| 4 | MiG-3, shot down over Tula 1942, thigh wound, then U-2 supply and casualty flights | sc. 10-13 | de.wiki raw: MiG-3 over Moscow, "Bei Luftkämpfen über Tula … schwer am Oberschenkel verwundet … als Pilot einer U-2 auf Bomben- und Versorgungsflügen und zum Transport von Verwundeten", `Schilling154` | PASS |
| 5 | Pokryshkin May 1944, back to fighters, nine kills | sc. 14 | de.wiki: nine kills over 150 sorties **for the whole war**; en.wiki places nine with the 104th GIAP after May 1944 | PASS on the number, sources disagree on placement. See MINOR-4. |
| 6 | 13 July 1944, 185th sortie, shot down, no aircraft named | sc. 15 | de.wiki raw: "auf seinem 185. Einsatz … Nach dem Absprung aus seiner La-5"; en.wiki: "while flying a Bell P-39" | PASS. Narration and visual both correctly decline to name a type. |
| 7 | Captured wounded, failed tunnel in August, Sachsenhausen late September | sc. 16-17 | de.wiki raw: tunnel at Klein-Königsberg, failed 13 August, "Ende September … Sachsenhausen" | PASS |
| 8 | Over 200,000 interned; at least 10,000 Soviet POWs murdered autumn 1941 | sc. 18-19 | Sachsenhausen Memorial, re-pulled and read in full, both figures verbatim | PASS (Tier 1) |
| 9 | Shoe track, different surfaces, days under full packs, sole materials for industry | sc. 20-22 | Sachsenhausen Memorial, verbatim | PASS (Tier 1) |
| 10 | Register lists him as 11024 under his own name; the legend ran fifty years | sc. 23-25 | de.wiki raw: "unter der Nummer 11024 mit dem Namen „Dewjatajew, Michail" geführt", footnoted `Häftlingsliste … HTM Peenemünde, Archiv, EC/45/17`; the Nikitenko story carries "Angeblich" and `Schilling154` | PASS. The calibration is right: the paperwork disagrees, the legend is not called a lie, and no act is attributed to Devyatayev. |
| 11 | Shipped to Usedom "that autumn" | sc. 25-26 | de.wiki says November, ru says October | PASS, the hedge avoids a live conflict. |
| 12 | East was the Army and rockets, West was the Luftwaffe, flying bombs and glide bombs | sc. 27-28 | de.wiki `Peenemünde-West` raw: "im Unterschied zur Heeresversuchsanstalt / Peenemünde-Ost in der Regel nicht direkt an der Entwicklung … beteiligt"; "Erprobung bis zur Truppeneinführung von ferngelenkten und selbstgesteuerten Gleit- und Fallbomben"; Fi 103 launch positions on the airfield | PASS, and load-bearing for the correction at 106-107. |
| 13 | April 1943, ~3,000 foreign workers a secrecy risk, replaced with camp prisoners | sc. 29-30 | de.wiki `Peenemünde-West` raw: Stahms, "da die 3000 in ganz Peenemünde eingesetzten Fremdarbeiter die Geheimhaltung gefährdeten", Milch agreed, footnoted **Bode and Kaiser, Raketenspuren, 2011, S. 54** | PASS, and the citation is now correct. M-2 closed. |
| 14 | About 1,500 prisoners, 248 deaths documented by name | sc. 31 | HTM Peenemünde Memorial Landscape, re-pulled: "1,500 male prisoners of different nationalities"; "The death of 248 prisoners from May 1943 to March 1945 is documented" | PASS (Tier 1, verbatim). de.wiki's "durchschnittlich etwa 800" is average occupancy, not a conflict. |
| 15 | 150 kg warheads carried through marsh; dud bombs dug out of craters for defusal | sc. 32-33 | HTM Peenemünde, verbatim both; de.wiki `Peenemünde-West` Kanetzki-footnoted commando list repeats both | PASS (Tier 1, and double-sourced) |
| 16 | 400 men, one concrete shelter, witnesses called it the worst detail, no number | sc. 34 | de.wiki `Peenemünde-West`, "400 Häftlingen", "von Zeitzeugen als der brutalste beschrieben" | PASS as spoken. Paragraph is unfootnoted; see MINOR-5. |
| 17 | No crematorium; some to Greifswald, others buried on site | sc. 35 | de.wiki raw: "Mindestens 171 Häftlinge … im Krematorium Greifswald verbrannt, andere Leichen wurden vor Ort verscharrt", `<ref name="Kanetzki" details="79f." />`; HTM Memorial Landscape confirms the mass grave of 56 found in the mid-60s | PASS, footnoted, and the on-site burials are no longer erased. |
| 18 | RAF August 1943; hit the forced labour camp instead; several hundred labourers killed | sc. 36-37 | en.wiki Operation Hydra raw: "at least 500 and possibly 600 slave workers"; HTM Memorial Landscape: Trassenheide "bombarded by mistake … around 300 people were killed" | PASS. "Several hundred" is the correct hedge across a 300 to 600 spread. |
| 19 | "Two German technical staff died" | sc. 38 | en.wiki Hydra raw: "about 170 German civilian personnel were killed, **including two V-2 rocket scientists**"; Thiel and Walther killed in a slit trench | **Imprecise.** The two is right for the rocket scientists, not for German technical staff generally. See MINOR-1. |
| 20 | Autumn 1943, SS handed guard duty to a home guard platoon; LANDESSCHÜTZENZUG 308/XI on the signboard | sc. 39-40 | de.wiki `Peenemünde-West` raw: "Die Bewachung erfolgte durch SS und ab Herbst 1943 durch den Landesschützenzug 308/XI der Luftwaffe" | PASS |
| 21 | A German fellow prisoner got him onto the airfield detail | sc. 43 | de.wiki raw | CONDITIONAL, unchanged. Sentence itself unfootnoted, next clause carries `Schilling155`. Low stakes, no specific asserted. |
| 22 | He learned instrument layouts off wrecked cockpits on the airfield scrap heap | sc. 45-50, 54-55 | ru.wiki raw, footnoted Devyatayev 1972 p. 182 and Krivonogov 1963 p. 153; de.wiki agrees on wreck instruments | **PASS. The solid leg, and it now carries the sequence alone.** |
| 23 | The detail patched bombed runways and camouflaged test aircraft | sc. 51 | de.wiki raw `Schilling155`; **and** de.wiki `Peenemünde-West` Kanetzki-footnoted commando list | **PASS, double-footnoted across two articles.** |
| 24 | They watched the movements out on the airfield | sc. 52 | ru.wiki raw: "со стороны наблюдали за перемещениями на аэродроме" | PASS, stated at exactly the source's level and no further. |
| 25 | Aircraft picked about a month in advance; sympathetic gunner declined for his family; Tsygan framed, Nemchenko took the place | sc. 56-59 | ru.wiki raw, all three, footnoted Devyatayev 1972 and Krivonogov 1963 | PASS |
| 26 | Campfire to warm up and heat the lunch; revetment cover story by Sokolov; guard accepted | sc. 62-65 | ru.wiki raw | PASS on facts. Order inverted against the source, unchanged from pass 3. See MINOR-6. |
| 27 | Krivonogov killed the guard and took his rifle, no weapon named, no name given | sc. 61, 66-67 | ru.wiki: "Кривоногов по сигналу Девятаева убил конвоира"; de.wiki; HTM Peenemünde | PASS. "Johnen" absent from the whole file except the log. **The log's stated reason for naming no weapon is still false**, see MINOR-7. |
| 28 | Kutergin greatcoat, contested | sc. 67 | ru.wiki carries both versions in one parenthesis, exactly as the script frames it | PASS, contested in the narration itself |
| 29 | Start-up sequence "he had been taught" | sc. 69 | No source. The only account of instruction was cut this pass. ru.wiki: he simply tried to start the engine and found no battery | **FAIL. Surviving residue of B-1. See V-1.** |
| 30 | No battery; battery cart fetched; failed first takeoff; rifle pointed at him; taxied at the ground crew; trim wheel found after the second takeoff | sc. 68, 70-81 | ru.wiki raw, sequence matches beat for beat including the elevator trim wheel stabilising the aircraft **after** takeoff, `sfn Девятаев 1972 с=252` | PASS |
| 31 | "By his own account it was twelve thirty six … twenty one minutes" | sc. 82-83 | ru.wiki raw: "по словам Девятаева, часы показывали 12:36, а вся операция заняла 21 минуту", with the attached note "В книге Девятаева указывается 11:45" | PASS, attributed in narration, no time burned on screen, and the cold open no longer repeats it. |
| 32 | Pursuit contested, no ammunition claim made | sc. 84-85 | ru.wiki; de.wiki; HTM Peenemünde (which records only the 1999 Hobohm meeting) | PASS. The contradiction is spoken out loud. |
| 33 | Soviet flak hit it and set it on fire; sideslip put the fire out | sc. 86-89 | ru.wiki: "Девятаеву удалось сбить пламя, бросив самолёт вниз со скольжением" | PASS |
| 34 | Belly landed just behind the Soviet front line, near Woldenberg | sc. 90 | HTM Peenemünde (Tier 1): "landete auf einer Wiese hinter der sowjetischen Frontlinie"; de.wiki: crossed the line over Pomerania, belly-landed in a meadow; ru.wiki: Woldenberg, with its own note disputing proximity | PASS as rewritten. The 8 km is gone. See MINOR-2 on "just". |
| 35 | Found by Soviet soldiers, taken for Germans | sc. 91-92 | ru.wiki; de.wiki (SMERSH) | PASS |
| 36 | 22 Feb 1945, seven to the 215th Reserve Rifle Regiment, then line infantry | sc. 93-94 | ru.wiki raw personnel trail: 23rd assembly point, 22 Feb to the 215th, arrived 16 March, 19 March six to the 397th Rifle Division / 447th RR, 29 March Oleynik to the 448th, **plus the article's explicit note that the unit was not a penal one** | **PASS, re-confirmed independently. Not penal battalions.** en.wiki's penal-battalion paragraph is `{{Fact}}`-tagged and correctly discounted. |
| 37 | Four killed 16 April forcing the Oder; Oleynik 21 April; Nemchenko 24 April; six of ten within eleven weeks; four lived | sc. 95-98 | ru.wiki raw, named and dated per man; de.wiki independently: "sechs von ihnen fielen", "Nur drei von ihnen haben die Kämpfe um Berlin überlebt" | **PASS. Arithmetic redone from scratch.** 4 + 1 + 1 = 6 named dead. 3 surviving comrades + Devyatayev = 4. 6 + 4 = 10. 8 Feb to 24 Apr 1945 = 75 days = 10.71 weeks, so "within eleven weeks" is correct. |
| 38 | Nemchenko lost an eye in captivity and argued his way to the front as a medical orderly | sc. 97-98 | ru.wiki: "даже Немченко, потерявший один глаз, уговорил отправить его на фронт в качестве санитара стрелковой роты" | PASS |
| 39 | Held and interrogated until September; Russian records put him in Special Camp No. 7 on the Sachsenhausen site | sc. 99-102 | ru.wiki (Спецлагерь № 7, footnoted to samlib.ru, Tier 3); de.wiki raw ("in eine Strafeinheit der Armee versetzt"; "bis September 1945 in Haft und wurde immer wieder verhört") | PASS as hedged. Chronology wrinkle at MINOR-3. |
| 40 | Over four million returnees went through filtration | sc. 103 | Zemskov archival figures via the filtration literature: 4,199,488 Soviet citizens repatriated as of 1 March 1946, all subject to the filtration regime; Palgrave *Remaking Soviet Society* | PASS, 2+ independent |
| 41 | "Statements from former fellow prisoners eventually helped clear him of being a spy" | sc. 104 | de.wiki raw, **the sentence carries no footnote**; **absent** ru.wiki escape article; **absent** ru.wiki biography; **absent** en.wiki (which credits Korolev in 1957); **absent** HTM Peenemünde, which says "Erst 1957 wurde Dewjatajew vom Vorwurf der Kollaboration … freigesprochen" | **FAIL, single-sourced on an unfootnoted sentence and falsely logged as unanimous. See V-2.** |
| 42 | Colonel Sergeyev walked him round the ruined site for days; Sergeyev was Korolev | sc. 105-106 | ru.wiki: "С. П. Королёв, работавший под псевдонимом «Сергеев», вызвал его на остров Узедом", showed launch installations and underground shops | PASS |
| 43 | Never inside the rocket programme, worked the Luftwaffe airfield | sc. 107 | de.wiki raw, footnoted to Förderverein Infoblatt 1/2015; **plus ru.wiki biography**: "Поскольку Девятаев служил в аэродромной команде, а ракетный полигон находился в отдалении, ничего сверхсекретного он поведать не мог"; **plus** de.wiki `Peenemünde-West` on the East/West division of work | **PASS, and now genuinely multi-sourced.** The Infoblatt is no longer load-bearing. |
| 44 | Twelve years later, on Korolev's initiative, Hero of the Soviet Union | sc. 108 | ru.wiki: "Через 12 лет после событий, 15 августа 1957 года, по инициативе С. П. Королёва"; de.wiki: "Zwölf Jahre später wurde er durch Bemühungen von Sergej Koroljow …"; HTM Peenemünde: "Erst 1957 …" | PASS, three sources |
| 45 | Soviet press turned him into a poster | sc. 109 | HTM Peenemünde: "Von der sowjetischen Presse wurde Dewjatajew als Familienvater und Kriegsheld inszeniert … unterstützte die Propaganda mit der Geschichte von seiner spektakulären Flucht" | PASS (Tier 1) |
| 46 | Hydrofoil captain on the Volga; never flew again; died 2002 | sc. 110-111 | de.wiki raw: first captain of a Meteor (1961), "Er flog jedoch nie wieder ein Flugzeug", died 24 November 2002 in Kazan; en.wiki and ru.wiki agree | PASS, multi-sourced |
| 47 | H22 variant, Göring order, Hitler personal enemy, Mandralsky, chimney, crowbar, guard's name | throughout | grep of the full file | PASS, absent from narration and visuals. Present only in the notes recording the cuts. |

---

## Citation integrity audit

I went through the FACT-CHECK LOG and the SOURCES block line by line and tested each citation against what the named source actually says.

**Resolved correctly, verified rather than assumed:**
- Bode and Kaiser, *Raketenspuren*, 2011, p. 54 for scenes 29 to 30. Confirmed as the literal inline `<ref>` on the Stahms and Milch sentence in `Peenemünde-West` wikitext.
- The SOURCES block's statement about the 2008 6th edition is **exactly right**, which I did not expect and checked character by character. `Michail Petrowitsch Dewjatajew`'s Literatur section carries "Volkhard Bode, Christian Thiel: *Raketenspuren. Waffenschmiede und Militärstandort Peenemünde*, 6. Auflage, Ch. Links, Berlin 2008, S. 128 f." It is a further-reading entry and not an inline citation, precisely as the block says. The instruction not to merge the two author strings is correct and should be kept.
- Arolsen 1-1-35-1_2267002 is genuinely the Greifswald crematorium death list for Peenemünde subcamp prisoners, and it genuinely supports scene 35.
- Kanetzki, Schilling, the Sachsenhausen Memorial, the HTM Memorial Landscape, the HTM Heldenmythos page, en.wikipedia Operation Hydra, IWM, and the two filtration sources are all cited for claims they actually carry.
- All seven sources the revision claims to have removed are gone. Verified by grep.

**URLs.** 18 of 18 resolve. IWM and Tandfonline return 403 to automated requests, which is bot-blocking and not a dead link; both are live in a browser. The two Arolsen record pages refuse plain curl but the host serves; their identity was confirmed in pass 3 and I found no reason to doubt it.

**Defects found:**

- **V-2 below.** The scene 104 entry says "Verified and unanimous". It is neither. This is the fourth recurrence of the same disease and the most serious finding in this pass.
- **V-3 below.** The Förderverein Infoblatt entry ends "and it is what was read". The URL German Wikipedia carries for it, `foerderverein-peenemuende.de/infoblatt0115/inbl0115.htm`, returns **404**, and the Wayback Machine has **no snapshot of it at all**. Nobody read this newsletter.
- **V-4 below.** The Devyatayev *Побег из ада*, Kazan 1988 entry asserts the book's contents. Those facts come from ru.wikipedia's editorial note, and ru.wikipedia's own `sfn` citations are to **Девятаев 1972**, a different work, while the article notes he wrote two autobiographies.
- **MINOR-5.** The Bunkerbau entry is cited "[de.wikipedia citing Kanetzki]". That paragraph carries no footnote; the Kanetzki ref closes the paragraph before it. Plausible but not what the wikitext says.

**Listed but not tied to any logged claim:** the HTM 8 February 2025 commemoration page, the Arolsen Karlshagen transport list 22.05.1943, the RAF Benevolent Fund page, and the Gedenkstätten Mecklenburg-Vorpommern Karlshagen I page. All four are genuine, relevant, working pages and reasonable further reading for viewers, so I am **not** treating these as the "listed but never read" defect. Noting them only so the owner knows nothing in the log depends on them.

---

## Tone check

**PASS.** Re-checked from scratch, not carried over.

The 26 TONE: STRAIGHT scenes are 18-22, 31-38, 66-67 and 93-103, which matches the production notes exactly. I read the narration of all 26 individually.

- **Sachsenhausen block (18 to 22):** straight. Losing the number cost nothing and added no comedy.
- **Karlshagen and island block (31 to 38):** straight. Scene 34's "Witnesses called it the island's worst detail" is testimony delivered flat. Scene 35 states the burials plainly with no body count and no chimney anywhere in the file.
- **The killing (66 to 67):** correct. Frame darkens before contact, no weapon named, no name on the card, and the joke at 65 lands before the kill rather than on it. Note that ru.wikipedia **does** specify the weapon; the script's silence is the right editorial call regardless.
- **Casualty and filtration block (93 to 103):** straight throughout and still the strongest passage in the script. The B-4 hedge did not soften it.
- **The new scene 53 gag:** sits at scene 53, outside every straight range, rides the scrap heap, and targets German security. **It does not touch human-cost material.** No tone failure.
- **Scene 38 remains the one borderline:** "Two German technical staff died. Which brings us to the security arrangements." The irony targets German priorities, not the dead. Flag for VO: play flat, no lift on "which brings us to". Passes, as it did twice before.

No joke lands on the camps, the casualties, the killed guard or the filtration. **No tone failures.**

---

## Structural check

Measured with a parser I wrote independently, then cross-checked against `verify_script.py`. Both return identical numbers.

| Constraint | Required | Measured | Result |
|---|---|---|---|
| Visual tags | 112, contiguous 1 to 112 | 112, contiguous | PASS |
| REUSE tags | 10 | 10, at scenes 42, 60, 61, 69, 83, 100, 101, 106, 111, 112 | PASS |
| Total spoken words | 1,390 to 1,410 | **1,404** | PASS |
| Max beat length | 14 | 14 | PASS |
| 14-word beats | only 31, 33, 34, 97, 98, 101, 112 | exactly 31, 33, 34, 97, 98, 101, 112 | PASS, approved exception, not a defect |
| Beats over 14 words | none | none | PASS |
| Em-dashes | 0 | **0** | PASS |
| En-dashes | 0 | 0 | PASS |
| Brackets, parentheses or stage directions in spoken lines | none | none, all 112 beats checked | PASS |
| Beat distribution vs notes | notes claim 3@10, 2@11, 46@12, 54@13, 7@14 | identical | PASS |
| Header and IMAGE BUDGET word count vs measured | match | both say 1,404, measured 1,404 | PASS, M-7 closed |
| Act timecodes | continuous | 0:00-0:27, 0:27-1:17, 1:17-3:00, 3:00-4:38, 4:38-6:22, 6:22-7:15, 7:15-8:33, 8:33-8:53. No gaps, no overlaps | PASS |
| OUTRO end vs stated runtime | match | 8:53 and 8:53 at 158 wpm | PASS |
| Description chapters vs acts | match | all eight marks identical | PASS |
| Act-out hooks | every act | Cold open, 1, 2, 3, 5, 6 and OUTRO all land. Act 4 still ends on the trim wheel, a resolution rather than a cliffhanger. Unchanged from passes 2 and 3, still the one boundary a viewer could leave on. Not a blocker | PASS with the standing note |
| SOURCES URLs resolve | required | 18 of 18 | PASS |
| FACT-CHECK LOG quotes narration accurately | required | 16 of 16 verbatim | PASS, M-1 closed |
| Description claims nothing absent from the script | required | all 8 claims present in narration | PASS, N-2 closed |

**Structural budget fully intact.**

---

## BLOCKING

### V-1. A four-word residue of the cut learning chain survives at scene 69.

**Scene 69: "He ran the start up sequence he had been taught. Nothing happened."**

The revision cut the German-pilot demonstration, the translator and the start-up-checks observation as a unit, correctly. **"he had been taught" is what is left of them.** Nothing in the surviving evidence base says anyone taught Devyatayev a start-up sequence. The scrap heap gives him instrument layouts memorised off wrecks, which is a different thing, and the ru.wikipedia account of the moment is simply "Попытавшись завести двигатель, Девятаев обнаружил, что в самолёте нет аккумулятора" — he tried to start the engine and found there was no battery. No instruction, no teacher.

This is B-1 surviving in softened form, in narration, in the exact clause a hostile viewer would trace back to the withdrawn title. The file's own instruction at the top forbids exactly this.

**Fix:** delete four words. "He ran the start up sequence. Nothing happened." That is 11 words, inside budget, and it does not disturb the "flight school" and "free tuition" gags at 48 and 50, which are jokes about the scrap heap and do not assert a teacher.

### V-2. Scene 104 keeps the surviving half of the unfootnoted sentence this revision cut, and the log calls it unanimous.

**Scene 104: "Statements from former fellow prisoners eventually helped clear him of being a spy."**

The German Wikipedia sentence, in full, is:

> "Dewjatajew wurde schließlich nur aus der Haft entlassen, nachdem **Aussagen von früheren Mitgefangenen** und ein Verhörprotokoll des deutschen Luftflottenkommandos 6 zu seiner Entlastung beigetragen hatten."

The revision cut the interrogation-protocol half of that sentence for being unfootnoted and uncorroborated, and kept the other half of **the same sentence**. I pulled the wikitext: the sentence carries no footnote. The `<ref>` that follows belongs to the next sentence, the intelligence-value argument.

Corroboration search, done from scratch: **absent** from ru.wikipedia's escape article, **absent** from ru.wikipedia's biography, **absent** from en.wikipedia, which instead says "Soviet authorities cleared Devyataev only in 1957, after the head of the Soviet space program Sergey Korolyov personally presented his case", and **absent** from the Historisch-Technisches Museum Peenemünde page, which says "Erst 1957 wurde Dewjatajew vom Vorwurf der Kollaboration mit den Deutschen freigesprochen." The Tier 1 source on the site does not merely fail to corroborate the mechanism, it puts the clearing twelve years later than the script's placement between the 1945 filtration beat and the September 1945 Korolev beat implies.

The FACT-CHECK LOG entry reads "**Verified and unanimous**, and this is the half that ships." It is single-sourced, unfootnoted, and contradicted in emphasis by three of the four next-best sources including the museum. This is the fourth recurrence of the defect that failed passes 2 and 3.

**Fix, choose one:**
- **(a)** Cut the claim and replace with what the museum and en.wikipedia both carry, which is stronger anyway and sets up scene 108: "He was released in September. The suspicion did not lift for twelve years." Then correct the log entry.
- **(b)** Attribute it audibly, the way the pursuit is attributed: "One German account says statements from former prisoners helped clear him." Then correct the log entry to "single-sourced, unfootnoted, attributed in narration".
- **(c)** Ship as written. Not available. The claim is asserted flat and the log asserts a sourcing status it does not have.

### V-3. The SOURCES block says a source "is what was read". It cannot have been.

**SOURCES entry:** "*Vor 70 Jahren: Flucht aus Peenemünde*, Infoblatt des Fördervereins Peenemünde, Nr. 1/2015. … It is a local support-association newsletter, **and it is what was read.**"

The URL German Wikipedia carries in that footnote, `http://www.foerderverein-peenemuende.de/infoblatt0115/inbl0115.htm`, returns **404**. The Wayback Machine holds **no snapshot of it at any date**. There is no accessible copy of this newsletter online. What was actually read is the footnote text inside de.wikipedia's wikitext.

The good news is that the claim underneath no longer needs it. Scene 107 is now independently carried by ru.wikipedia's biography and by de.wikipedia's `Peenemünde-West`, both of which I quote above. So this costs the episode nothing to fix.

**Fix:** replace "and it is what was read" with "the newsletter itself is no longer online; what was read is the inline footnote in German Wikipedia". Better still, add the ru.wikipedia biography line as the readable corroboration, since it says the same thing and a viewer can actually check it.

### V-4. The SOURCES block asserts the contents of a book nobody opened.

**SOURCES entry:** "Mikhail Devyatayev, *Побег из ада*, Tatar Book Publishing House, Kazan 1988. His own account, and the origin of the '21 minutes'. **Note that the book itself gives the takeoff time as 11:45**; the 12:36 reading appears only in later memoirs."

Both assertions come from ru.wikipedia, not from the book:
- The 21 minutes is footnoted in ru.wikipedia to `rg.ru` 2007, a *Rossiyskaya Gazeta* article by Vasily Peskov, **not** to the book. So calling the book "the origin of the 21 minutes" is wrong on the wikitext's own terms, and it contradicts the same entry's next clause.
- The 11:45 comes from ru.wikipedia's editorial note "В книге Девятаева указывается 11:45", which names no edition. ru.wikipedia's actual `sfn` citations are to **Девятаев 1972** and Девятаев 2015, and the article records that he wrote **two** autobiographies, *Побег из ада* and *Полёт к солнцу*. The block pins a specific 1988 Kazan printing and reports its contents.

This is the "book pulled from a further-reading list and cited as if read" pattern, in the public description, on a channel whose pitch is that it cites what it read.

**Fix:** either drop the edition specificity and attribute honestly, for example "Devyatayev's own memoirs, via ru.wikipedia, which notes that his book gives 11:45 while 12:36 appears only in later recollections; the 21 minutes is carried by *Rossiyskaya Gazeta*, 4 May 2007", or cite the rg.ru article directly, since that is the readable source that actually carries the figure.

---

## MINOR, not shipping-blocking

Listed separately so the owner can ship over them if he chooses. None of these would have failed a first pass.

**MINOR-1. Scene 38, "Two German technical staff died."** en.wikipedia's Operation Hydra says "about 170 German civilian personnel were killed, including two V-2 rocket scientists". The two is right for the scientists, Thiel and Walther, but "German technical staff" reads much broader and undercounts by about 170. **One-word fix that keeps the beat and the word count identical: "Two German rocket scientists died."** I would take the fix, but the substance of the beat, that the raid missed the people it was aimed at, is correct as it stands.

**MINOR-2. Scene 90, the word "just".** "Just behind the Soviet front line, near Woldenberg" is exactly the option pass 3 offered, and "behind the Soviet front line" is Tier 1 from the museum. But "just" softly reasserts the proximity that ru.wikipedia's own note disputes, since the note says Dobiegniew was about 30 km from the line and outside 61st Army's sector. Dropping one word closes it completely.

**MINOR-3. Special Camp No. 7 chronology (M-4, carried forward).** I confirmed independently: the camp was at Weesow until August 1945 and moved onto the Sachsenhausen grounds on 16 August 1945, when over 5,000 inmates walked more than 40 km to the site. Devyatayev was in custody February to September 1945, so at most the final three weeks could have been on that ground. Scene 101's "If so" hedges the identification but not the chronology, and 101 is the beat the notes call the one the episode turns on. **Not false**, because the camp did occupy the site and he was in custody into September, but thinner than the file believes. One clause fixes it, for example "by then on the site of Sachsenhausen". Note also that ru.wikipedia's footnote for the identification is `samlib.ru`, a self-publishing site, Tier 3, which is a further reason the existing hedge should stay exactly as strong as it is.

**MINOR-4. Scene 14, "Nine kills" placement (M-8, carried forward).** de.wikipedia gives nine kills across 150 sorties for the whole war; en.wikipedia places nine with the 104th GIAP after May 1944. The sources genuinely disagree, so this is a conflict rather than an error, but the juxtaposition will be heard as nine after May 1944. "Nine kills in all" resolves it in one word and is safe under both readings.

**MINOR-5. Bunkerbau citation.** The log cites scene 34 as "[de.wikipedia citing Kanetzki]". The Bunkerbau paragraph in `Peenemünde-West` carries no footnote; the Kanetzki ref closes the preceding paragraph. Plausible attribution, but not what the wikitext says. Restate as "[de.wikipedia, paragraph unfootnoted, adjacent to Kanetzki]" for accuracy.

**MINOR-6. Scenes 62 to 65 invert the source order (M-5, carried forward).** ru.wikipedia's order is: the group approached a parked aircraft, the guard noticed, Sokolov gave the revetment story, and only then, as the mechanics packed up for the lunch break, the fire was lit at about noon. The script lights the fire first. No claim is falsified and the comedy is better this way, but it is a chronology change and it is still not noted anywhere in the file. Add one line to the production notes so a future pass does not read it as an error.

**MINOR-7. The log's reason for naming no weapon is still false (M-6, carried forward).** The log says "The method is not specified in the v2 sources." ru.wikipedia specifies it: Krivonogov "убил конвоира, ударив его заранее заготовленной железной заточкой в голову". The narration's silence is correct on tone and editorially, and should not change. Restate the log's reason as a tone decision rather than a sourcing one.

**MINOR-8. Scene 76, "four hundred metres into the plan."** No source gives a distance for the aborted first takeoff run. It reads as a rhetorical figure and passed twice before, so I am not raising it as a defect, only noting that it is an invented specific in a script that is otherwise scrupulous about not inventing them. "Seconds into the plan" costs nothing.

---

## Cold read notes

- It reads better than v3 did. Cutting the whole learning chain rather than hedging it was the right call, and the sequence is tighter for it. Scenes 46 to 55 now say less and mean more.
- Scene 53's replacement gag is genuinely good and lands harder than the pilot dialogue it replaced, because the joke is now about German complacency rather than German helpfulness.
- The myth-correction beats at 23 to 25 and 84 to 85 remain the best-written thing in the script. 106 to 107 pays off the East versus West diagram cleanly.
- Scene 69's "he had been taught" is the one line a careful viewer will catch, because the script has just spent ten scenes establishing that nobody taught him anything.
- The lunchtime callback from scene 2 to scene 62 is well planted and pays.
- Zero em-dashes, zero en-dashes, no brackets or stage directions in any spoken line, TTS-safe throughout. Sentence-splitting across scene boundaries is consistent and reads at pace.
- Act 4 still ends on a resolution rather than a hook. Standing note, third pass, still not a blocker.

---

## Summary

Five of five prior blocking items are genuinely closed, and I confirmed each against source rather than against the file. B-1's cut is complete in the learning sequence and the title, description and thumbnail guidance are all clean of it. N-1 through N-4 are closed. Eleven of the twelve pass-3 minor items are closed or correctly carried. The structural budget, the arithmetic, the names, the dates, the casualty count and the tone discipline are all clean, and three claims are now better sourced than any previous pass recorded, including scene 51, which turns out to be double-footnoted across two articles, and scene 107, which no longer depends on the unreachable Förderverein newsletter.

What blocks the ship is small and it is the same disease, twice in the body and twice in the SOURCES block. Four words at scene 69 keep alive the instruction the script spent this whole revision cutting. Scene 104 keeps the surviving half of the very sentence whose other half was cut, asserts it flat, and the log calls it "verified and unanimous" when three of the four next-best sources are silent and the museum on the site puts the clearing twelve years later. And two SOURCES entries tell the audience that a source was read when one is a 404 with no archive anywhere and the other is a book whose reported contents came from a Wikipedia footnote.

None of this is hard. V-1 is a deletion of four words. V-2 is one sentence rewritten or attributed plus one log entry corrected. V-3 and V-4 are one clause each. The eight minor items are notes-and-wording hygiene and the owner can ship over all of them. Do the four blocking fixes and this is a strong episode.

VERDICT: FAIL

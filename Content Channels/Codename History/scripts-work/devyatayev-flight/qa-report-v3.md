# QA Report v3: Ten Prisoners Stole a Nazi Bomber at Lunchtime (script-v2-final.md)

**Reviewed:** script-v2-final.md, 112 scenes, 1,403 spoken words, revised after the pass-2 FAIL.
**Method:** structural budget re-measured with an independently written script, not the one in the folder (both agree). Every checkable claim re-verified from primary museum and memorial pages and from the **raw wikitext** of the cited encyclopedia articles, pulled via `Spezial:Exportieren` / `Special:Export`, so footnote attribution could be inspected sentence by sentence rather than assumed. The research report was not treated as evidence. Every URL in the SOURCES block was resolved.

**Result: FAIL.** F-1 to F-5 are closed at the level the pass-2 report demanded, and the structural budget, tone discipline and cold read are clean. But the pass-2 fix for F-1 rebuilt the sequence on a "verified chain" that is **not verified**: two of its three legs come out of the same unfootnoted German Wikipedia paragraph that killed the old title, and the narration now asserts out loud that they are "not in dispute". Separately, the citation disease behind I-1 has recurred in three new places, one of them in the published YouTube description, where it falsely puts a claim in the mouth of the Historisch-Technisches Museum Peenemünde.

---

## First-pass issue closure

| Item | Fix verified? | Notes |
|---|---|---|
| **F-1** German-pilot start-up lesson | **PARTIAL** | The demotion itself is done properly. Scene 52 says "One German account, and only one"; scene 54 says "The museum on the site does not carry that story. Treat it carefully." I read the museum's full Dewjatajew page and confirm the negative is accurate. "That's in the record" and "Because he was being polite" are gone (grep-confirmed). Title, TITLE CARD and description no longer rest on the claim. **But the replacement chain fails on its own terms. See N-1 below.** |
| **F-2** Bunkerbau 295 | **YES** | Grep: no "295" anywhere in the file except the log entry explaining the cut. Scene 34 now reads "Four hundred men built one concrete shelter. Witnesses called it the island's worst detail", which tracks de.wikipedia's "von Zeitzeugen als der brutalste beschrieben". No number reinstated, no contradiction with the 248 at scene 31. |
| **F-3** "nine surfaces" | **YES** | Gone from narration (scene 20: "A track of different surfaces") and from visual 20 ("a patchwork of different paving surfaces"). Matches the Sachsenhausen Memorial's "a shoe testing path with various different surfaces", which I re-pulled and which still gives no count. |
| **F-4** Special Camp No. 7 | **YES, in narration** | Scene 99: "Russian records put him inside". Scene 101 opens "If so". The hedge is spoken, not just a production note. Act 6 retitled "There was no parade". The unanimous half (custody and repeated interrogation until September 1945) is what carries the act. See minor issue M-4 for a chronology wrinkle neither side of the dispute resolves. |
| **F-5** "never on the Army site" | **YES** | Scene 107 now reads "He was never inside the rocket programme. He worked the Luftwaffe airfield." That is a claim about the programme, not about where a man stood, and it no longer collides with the Korolev walk-around at 105. |
| **I-1** citation integrity | **NO** | The two specific repairs asked for are done: the Förderverein Infoblatt 1/2015 is now cited as the inline footnote for the intelligence-value argument (I confirmed it is exactly that in the raw wikitext), and the author string is Bode and Thiel. **But three new or surviving false citations are in the file. See N-2, N-3, M-2.** |
| **I-2** 12:36 clock | **YES** | Visual 82 now reads "a cockpit clock in frame with no readable time on the dial". Narration keeps "By his own account". The 11:45 variant is now in the log. |
| **I-3** "He told that story for fifty years" | **YES** | Scene 25 now "The legend ran anyway for fifty years." No act attributed to Devyatayev. |
| **I-4** Greifswald erasing on-site burials | **YES** | Scene 35: "There was no crematorium. Some were driven to Greifswald. Others buried on site." Matches "andere Leichen wurden vor Ort verscharrt" in the Kanetzki-footnoted sentence. |
| **I-5** visual 15 aircraft type | **YES** | Visual 15 is now a text-only map card, "No aircraft type shown". |
| **I-6** guard's name | **YES** | "Johnen" is absent from the whole file except the log entry recording the removal. Scene 61 says "one home guard private"; visual 67 reads "The guard. Killed 8 February 1945." |
| **I-7** production-notes arithmetic | **YES** | Notes claim 1,403 words and 3@10, 3@11, 45@12, 54@13, 7@14. My independent measurement returns exactly that. |
| **I-8** log quoting text not in the script | **NO** | Fixed for the Hero of the Soviet Union entry. **Two new misquotes introduced. See M-1.** |
| **I-9** dead URL | **YES** | memorialmuseums.org is gone from the block. All 18 remaining URLs resolve (IWM and Tandfonline return 403 to automated requests, which is bot-blocking; both Arolsen records load and their titles match what the block claims they are, which I checked). |
| **I-10** description inherits F-1 | **PARTIAL** | "because he asked politely" is gone and the description now hedges the pilot claim correctly. **But the description introduces a worse false attribution. See N-2.** |

---

## Claim-by-claim verification

| # | Claim (as spoken) | Where | Source(s) checked | Verdict |
|---|---|---|---|---|
| 1 | Title: ten prisoners, a Nazi bomber, at lunchtime | title, TITLE CARD, sc. 60-61 | HTM Peenemünde Dewjatajew page: "erschlugen er und neun weitere sowjetische Häftlinge einen zu ihrer Bewachung eingesetzten Soldaten ... stahlen ein deutsches Bombenflugzeug des Typs He-111"; de.wikipedia raw: work detail of ten, one guard, "Um die Mittagszeit"; ru.wikipedia: fire lit "примерно в 12 часов по местному времени", mechanics leaving for the lunch break | **PASS on all three elements, independently.** Ten, stolen, He 111, midday. Museum plus two language editions. Nothing in the title touches a contested claim. |
| 2 | River navigator; Ju 87 on 24 June 1941; MiG-3 and Tula 1942, thigh wound; U-2 years; Pokryshkin May 1944; nine kills; 185th sortie 13 July 1944 | sc. 7-15 | de.wikipedia raw, footnoted Schilling 153 to 155 throughout | PASS. Narration still does not name the aircraft type at 15, correctly, since de.wikipedia says La-5 and en.wikipedia says P-39. |
| 3 | 200,000 interned; at least 10,000 Soviet POWs murdered autumn 1941 | sc. 18-19 | Sachsenhausen Memorial, re-pulled, verbatim both figures | PASS (Tier 1) |
| 4 | Shoe track, days under full packs, sole materials for industry, commercial test data | sc. 20-22 | Sachsenhausen Memorial: detail set up 1940 "under the command of civilian officials from the 'Reich' Ministry of Economics", march "for days on end with full packs" | PASS (Tier 1) |
| 5 | Register lists him as 11024 under his own name; legend ran fifty years | sc. 23-25 | de.wikipedia raw: "unter der Nummer 11024 mit dem Namen „Dewjatajew, Michail" geführt", footnoted `Häftlingsliste ... HTM Peenemünde, Archiv, EC/45/17`; "Angeblich" hedge on the Nikitenko story, footnoted Schilling154 | PASS. Calibration is right: paperwork disagrees, legend not called a lie. |
| 6 | East Army rockets, West Luftwaffe | sc. 27-28 | de.wikipedia/Peenemünde-West raw | PASS |
| 7 | April 1943, 3,000 foreign workers, replaced with camp prisoners | sc. 29-30 | de.wikipedia/Peenemünde-West raw: Stahms, "da die 3000 in ganz Peenemünde eingesetzten Fremdarbeiter die Geheimhaltung gefährdeten", Milch agreed | PASS on the claim. **The log's citation for it is wrong. See M-2.** |
| 8 | 1,500 prisoners, 248 deaths documented by name | sc. 31 | HTM Peenemünde Memorial Landscape, re-pulled: "1,500 male prisoners of different nationalities"; "The death of 248 prisoners from May 1943 to March 1945 is documented" | PASS (Tier 1, verbatim) |
| 9 | 150 kg warheads through marsh; dud bombs out of craters | sc. 32-33 | HTM Peenemünde, verbatim both | PASS (Tier 1) |
| 10 | 400 men, one shelter, worst detail, no number | sc. 34 | de.wikipedia/Peenemünde-West raw (Kanetzki) | PASS. F-2 closed. |
| 11 | No crematorium; some to Greifswald, others buried on site | sc. 35 | de.wikipedia raw (Kanetzki, "79f."); Arolsen Archives 1-1-35-1_2267002, whose actual title is "Totenliste (Krematorium Greifswald) zu Häftlingen, die im Außenlager Peenemünde verstorben sind", Nov 1943 to Sept 1944 | PASS, and the Arolsen citation is genuine, which I verified rather than assumed. |
| 12 | RAF August 1943; forced labour camp hit instead; several hundred labourers killed; two German technical staff died | sc. 36-38 | en.wikipedia Operation Hydra: 17/18 Aug 1943, "at least 500 and possibly 600 slave workers", Dr Walter Thiel and Dr Erich Walther | PASS in narration. **Visual 38 is wrong. See M-3.** |
| 13 | SS handed guard duty to a home guard platoon, autumn 1943; LANDESSCHÜTZENZUG 308/XI on the signboard | sc. 39-40 | de.wikipedia/Peenemünde-West raw: "ab Herbst 1943 durch den Landesschützenzug 308/XI der Luftwaffe" | PASS |
| 14 | A German fellow prisoner got him onto the airfield detail | sc. 43 | de.wikipedia raw | CONDITIONAL. Sentence itself unfootnoted, though the next clause carries Schilling155. Low stakes, no specific asserted. |
| 15 | Learned instrument layouts off wrecked cockpits on the airfield scrap heap | sc. 46-47 | ru.wikipedia raw: "изучал приборные панели и оборудование кабины самолёта Heinkel-111 по фрагментам кабин разбитых машин, находившихся на свалке рядом с аэродромом", footnoted Devyatayev 1972 p.182 and Krivonogov 1963 p.153; de.wikipedia agrees | **PASS. This is the one solid leg of the learning chain.** |
| 16 | "Another prisoner translated the German labels. Free tuition." | sc. 48 | de.wikipedia raw, **unfootnoted**; absent ru.wikipedia; absent en.wikipedia; absent HTM Peenemünde | **FAIL, single-sourced and unfootnoted. See N-1.** |
| 17 | "German crews ran their start up checks out in the open. The prisoners watched." / "Every switch, every drill, performed in daylight, in front of the work detail." | sc. 49-51 | de.wikipedia raw, **unfootnoted**; ru.wikipedia says only "со стороны наблюдали за перемещениями на аэродроме" | **FAIL, single-sourced, unfootnoted, and escalated beyond even that source. See N-1.** |
| 18 | "The rubbish heap and the free tuition, though, are not in dispute." | sc. 55 | as rows 15 to 17 | **FAIL. The script makes an affirmative sourcing claim that is false for half of what it names.** |
| 19 | Aircraft picked about a month in advance; sympathetic gunner declined for his family; Tsygan framed, Nemchenko took the place | sc. 56-59 | ru.wikipedia raw, all three, footnoted to Devyatayev 1972 and Krivonogov 1963 | PASS |
| 20 | Campfire, revetment cover story, guard accepted | sc. 62-65 | ru.wikipedia raw | PASS on facts. Order inverted against the source. See M-5. |
| 21 | Krivonogov killed the guard and took his rifle, no weapon named | sc. 66 | ru.wikipedia ("Кривоногов по сигналу Девятаева убил конвоира"); de.wikipedia; HTM Peenemünde | PASS. Narration correctly names no weapon. **The log's reason for that is false. See M-6.** |
| 22 | Kutergin greatcoat, contested | sc. 67 | ru.wikipedia carries both versions in one parenthesis | PASS, contested in the narration itself |
| 23 | No battery, battery cart, failed first takeoff, rifle pointed at him, taxied at ground crew, trim wheel | sc. 68-81 | ru.wikipedia raw, sequence matches beat for beat | PASS |
| 24 | "By his own account it was twelve thirty six ... twenty one minutes" | sc. 82-83 | ru.wikipedia: "по словам Девятаева, часы показывали 12:36, а вся операция заняла 21 минуту", with the note "В книге Девятаева указывается 11:45" | PASS as spoken, because it is attributed. **The cold open repeats it unattributed. See N-3.** |
| 25 | Pursuit contested, no ammunition claim made | sc. 84-85 | ru.wikipedia (Dahl, Fw 190, Hobohm "недостоверно"); HTM Peenemünde and de.wikipedia (Hobohm, Ju 88) | PASS. The contradiction is spoken out loud and the ammunition line does not appear. |
| 26 | Soviet flak hit it, sideslip put the fire out | sc. 86-89 | ru.wikipedia: "Девятаеву удалось сбить пламя, бросив самолёт вниз со скольжением" | PASS |
| 27 | "eight kilometres behind the Soviet front line, near Woldenberg" | sc. 90 | ru.wikipedia main text says 8 km, **and its own attached note says Dobiegniew was about 30 km from the line, outside 61st Army's sector, and that Sochneva 2009 puts the landing elsewhere** | **FAIL, unresolved conflict stated flat. See N-4.** |
| 28 | Found by Soviet soldiers, taken for Germans | sc. 91-92 | ru.wikipedia; de.wikipedia (SMERSH) | PASS |
| 29 | 22 Feb 1945, seven to the 215th Reserve Rifle Regiment, then line infantry | sc. 93-94 | ru.wikipedia raw personnel trail: 23rd assembly point, 22 Feb to the 215th, arrived 16 Mar, 19 Mar six to the 397th Rifle Division / 447th RR, 29 Mar Oleynik to the 448th, **plus an explicit editorial note that the unit was not a penal one** | **PASS, re-confirmed independently. Not penal battalions.** en.wikipedia's penal-battalion paragraph is tagged {{Fact}} and internally incoherent; correctly discounted. |
| 30 | Four killed 16 April forcing the Oder; Kutergin, Serdyukov, Sokolov, Urbanovich; Oleynik 21 April; Nemchenko 24 April; six of ten within eleven weeks; four lived | sc. 95-98 | ru.wikipedia raw, named and dated per man | **PASS, arithmetic redone from scratch.** 4 + 1 + 1 = 6 named dead. 6 + 4 = 10. Survivors confirmed as Devyatayev, Krivonogov, Yemets, Adamov ("остались только четверо"). 8 Feb to 24 Apr 1945 = 75 days = 10.7 weeks, so "within eleven weeks" is correct. de.wikipedia independently agrees: six fell, three of the nine survived, plus Devyatayev = four. |
| 31 | Nemchenko lost an eye in captivity, argued his way to the front as a medical orderly | sc. 97-98 | ru.wikipedia: "немцы выбили ему один глаз"; "уговорил отправить его на фронт в качестве санитара стрелковой роты" | PASS. Note the same article elsewhere lists him as a machine-gun squad commander in the 447th; the script follows the orderly line, which is what the article's own escape section says. |
| 32 | Held and interrogated until September, Russian records put him in Special Camp No. 7 | sc. 99-102 | ru.wikipedia (Спецлагерь № 7, cited to samlib.ru); de.wikipedia raw ("in eine Strafeinheit der Armee versetzt"; "bis September 1945 in Haft und wurde immer wieder verhört") | PASS as hedged. See M-4. |
| 33 | Over four million returnees went through filtration | sc. 103 | Zemskov figures via Palgrave *Remaking Soviet Society* and the NKVD filtration-camp literature: 4.2 million repatriated as of 1 Mar 1946, roughly 100 camps processing more than 4,000,000 | PASS, 2+ independent |
| 34 | "A Luftwaffe interrogation protocol eventually helped clear him of being a German spy" | sc. 104 | de.wikipedia raw, **the sentence carries no footnote**; absent ru.wikipedia "Побег группы Девятаева"; absent ru.wikipedia "Девятаев, Михаил Петрович"; absent en.wikipedia; absent HTM Peenemünde | **FAIL, single-sourced, unfootnoted, and falsely cited in the log. See N-2.** |
| 35 | Colonel Sergeyev walked him round the ruined site for days; Sergeyev was Korolev | sc. 105-106 | ru.wikipedia: "С. П. Королёв, работавший под псевдонимом «Сергеев», вызвал его на остров Узедом"; he showed where the launch installations and underground shops were | PASS |
| 36 | Never inside the rocket programme, worked the Luftwaffe airfield | sc. 107 | de.wikipedia raw, footnoted to Förderverein Peenemünde Infoblatt 1/2015 (I confirmed the footnote text and its URL in the wikitext) | PASS in narration. **The description mis-attributes it. See N-2.** |
| 37 | Twelve years later, on Korolev's initiative, Hero of the Soviet Union | sc. 108 | ru.wikipedia: "Через 12 лет после событий, 15 августа 1957 года, по инициативе С. П. Королёва"; de.wikipedia; HTM Peenemünde ("Erst 1957 ... freigesprochen") | PASS |
| 38 | Soviet press turned him into a poster | sc. 109 | HTM Peenemünde: "Von der sowjetischen Presse wurde Dewjatajew als Familienvater und Kriegsheld inszeniert ... unterstützte die Propaganda mit der Geschichte von seiner spektakulären Flucht" | PASS (Tier 1) |
| 39 | Hydrofoil captain on the Volga; never flew again; died 2002 | sc. 110-111 | de.wikipedia raw: first captain of a Meteor (1961), "Er flog jedoch nie wieder ein Flugzeug", died 24 Nov 2002 in Kazan; ru.wikipedia agrees | PASS, and "never flew again" is now two-sourced, better than pass 2 recorded |
| 40 | H22 variant, Göring order, Hitler personal enemy, Mandralsky, chimney, crowbar | throughout | grep of the full file | PASS, absent from narration and visuals. Present only in the notes that record the cuts. |

---

## Newly introduced text, fresh verification

Everything below was checked as unverified text, not assumed safe.

**Cold open, scenes 1 to 6, and TITLE CARD.** Scene 1's "most secret airfield in Nazi Germany" is a rhetorical superlative and reads as one; not blocking. Scene 2's one private at lunchtime is carried by de.wikipedia's one-guard work detail and the museum. Scene 3's "ten concentration camp prisoners" is right, Karlshagen I was a KZ-Arbeitslager and a Ravensbrück subcamp. Scene 5's "He learned from a scrap heap" is the solid leg, correct. Scene 6 and the TITLE CARD are clean. **Scene 4 is not. See N-3.**

**Scenes 20, 25, 34, 35, 61, 67, 99, 101, 107.** All nine changed lines were re-checked against source and all nine are accurate as written, subject to M-4 on the Special Camp chronology.

**Scenes 49 to 55.** This is the F-1 rebuild and it is where the pass fails. See N-1.

**Act 6 title.** "There was no parade" asserts nothing. Correct.

**YouTube description.** Chapter marks match the act boundaries exactly. The pilot-claim hedge is now honest and matches the script. The final sentence does not. See N-2.

### N-1. The chain that replaced F-1 is not the verified chain the script says it is. BLOCKING.

The pass-2 report offered fix (b): demote the pilot demonstration and let the observation, the scrap heap and the translator carry the sequence. The script took that option and wrote, at scene 55:

> **"The rubbish heap and the free tuition, though, are not in dispute."**

I pulled the raw wikitext again. The whole passage is one paragraph, and it contains exactly one footnote:

> "Ein deutscher Mithäftling sorgte dafür, dass Dewjatajew in ein Kommando eingeteilt wurde, das direkt auf dem Flugplatz tätig war. Dort musste er mit anderen Kriegsgefangenen beschädigte Startbahnen ausbessern`<ref name="Schilling155" />` und dort abgestellte Erprobungsflugzeuge tarnen. Dewjatajew begann daraufhin ... Fluchtpläne auszuarbeiten. **So beobachteten sie die Startvorbereitungen der deutschen Piloten, ein Mitglied der Gruppe übersetzte die deutschen Beschriftungen von Instrumenten aus Flugzeugwracks.** Wichtig während dieser Vorbereitungen war ... Der Pilot zeigte dabei Dewjatajew bereitwillig alle dafür notwendigen Abläufe und Handgriffe."

The single `Schilling155` footnote attaches to repairing runways. **Everything after it is unreferenced, including the start-up observation and the translator.** They sit in the same unfootnoted run of prose as the pilot demonstration that was withdrawn. So:

- **Scrap-heap instrument panels (sc. 46-47): SOLID.** ru.wikipedia carries it with footnotes to Devyatayev 1972 p.182 and Krivonogov 1963 p.153, de.wikipedia agrees. Multi-sourced, footnoted, keep.
- **Translator (sc. 48), the "free tuition" the callback is built on: de.wikipedia only, unfootnoted.** Absent from ru.wikipedia's escape article, absent from ru.wikipedia's biography, absent from en.wikipedia, absent from the museum's page, all of which I read.
- **Crews running start-up checks in the open (sc. 49-51): de.wikipedia only, unfootnoted.** ru.wikipedia says only that while doing chores they "со стороны наблюдали за перемещениями на аэродроме", observed movements at the airfield. That is not the same claim. Scene 51 then escalates past even the German sentence to "Every switch, every drill, performed in daylight, in front of the work detail", which no source says at all.

The fact-check log calls this leg "Verified in two languages" and says "ru.wikipedia agrees on the observation". It does not agree on the start-up preparations, only on general observation of the airfield. That log entry is an overstatement of the evidence, which is the precise thing this pass exists to catch.

The narration then tells the viewer these beats are "not in dispute" while the script simultaneously withdraws a title because a sentence eight words away in the same paragraph is unfootnoted. A viewer who checks will find the same footnote status for both. **This is F-1 relocated, not F-1 solved.**

**Fix, choose one:**
- **(a)** Carry the sequence on the scrap heap alone, which is genuinely footnoted and genuinely multi-sourced. Cut or attribute scenes 48 and 49 to 51 the way 52 to 54 are attributed. Rewrite scene 55 to "The rubbish heap, though, is not in dispute." Rebuild the "free tuition" callback on the wrecks.
- **(b)** Keep all three beats but move the attribution wall earlier, so scene 52's "One German account, and only one" covers 48 to 54 rather than 52 to 54, and delete scene 55's "not in dispute" sentence entirely.
- **(c)** Ship as written. Not available. The script asserts a sourcing status it does not have, in narration.

Also delete "Every switch, every drill, performed in daylight, in front of the work detail" (sc. 51) or reduce it to what the source supports. It is an invented specific on top of an unfootnoted claim, and the description repeats it as fact.

### N-2. The YouTube description puts a claim in the museum's mouth that the museum does not make. BLOCKING.

**Description, final line of paragraph three:** "And no, he did not steal the V-2 rocket programme. **The museum on the site says so itself.**"

I fetched and read the complete text of the HTM Peenemünde page the script cites, `museum-peenemuende.de/zeitreise/michael-dewjatajew/`. It covers the imprisonment, the killing of the guard, the He 111, the SMERSH suspicion, the 1957 rehabilitation, the propaganda staging, the Gedenkstein and the 1999 Hobohm meeting. **It says nothing whatever about the escapers' intelligence value or the V-2 programme.**

The actual source for that correction is the one the script's own SOURCES block correctly identifies: "Vor 70 Jahren: Flucht aus Peenemünde", *Infoblatt des Fördervereins Peenemünde*, Nr. 1/2015, a support-association newsletter cited inline in de.wikipedia. The Förderverein is not the museum. The description upgrades a newsletter into an institutional Tier 1 statement, in the most public-facing text the episode ships, in an episode whose entire pitch is that it cites what it actually read. It also breaks the rule that the description claim nothing absent from the script, since the narration never attributes this correction to anyone.

**Fix:** delete "The museum on the site says so itself." The museum sentence is legitimate one paragraph earlier, where it refers to the pilot claim, and that use is accurate.

### N-3. The cold open states the "21 minutes" as fact and extends it past what it covers. BLOCKING.

**Scene 4:** "In twenty minutes ten men will steal a bomber **and fly home**."

Two problems.

1. The script's own production note, item (3), lists "the '21 minutes' and the 12:36 clock reading" as things that are "Attributed, not asserted. **Do not upgrade these into hard facts in the edit, the thumbnail, or the description.**" Scene 82 to 83 obeys that ("By his own account"). The cold open does not. It is the first number the viewer hears and it is delivered flat.
2. As written it is wrong. ru.wikipedia's sentence is "вся операция заняла 21 минуту", the whole **operation**, meaning the seizure through getting airborne and stable. The flight home was not in it. The same article puts the landing "примерно в 300—400 километрах от места старта", 300 to 400 km from the start, which is over an hour in an He 111. "Steal a bomber and fly home" in twenty minutes is not what any source says.

**Fix:** "In twenty minutes ten men will steal a bomber." or, keeping the scale of the promise, "Within the hour ten men will steal a bomber and fly home."

### N-4. The landing location is an unresolved conflict stated flat. BLOCKING.

**Scene 90:** "He belly landed **eight kilometres** behind the Soviet front line, near Woldenberg."

ru.wikipedia's main text does say about 8 km, sourced to Krivonogov 1963. Immediately attached to that clause is the article's own note:

> "Добегнев ... находился примерно в 30 км от линии фронта, вне зоны дислокации 61 армии ... По другим источникам (Сочнева, 2009), место посадки находилась южнее населённого пункта Голлин."

So the cited source flags that Dobiegniew was about 30 km from the line, outside 61st Army's sector, that Krivonogov was writing in 1962 and may be in error, and that another source puts the landing somewhere else entirely. The script asserts one side of that flat, with a specific integer, exactly the pattern that produced F-2 and F-3.

**Fix:** "He belly landed behind the Soviet front line, in Pomerania." Or keep Woldenberg and drop the 8 km. The beat loses nothing.

---

## Minor issues, fix before build

**M-1. The fact-check log still misquotes narration, in two new places (I-8 recurrence).**
- Log, Landesschützenzug entry: "Narration at scenes 39 and 40 says **'the home guard. Second line. Older men.'**" The script says "The SS handed it to **a** home guard **platoon**. Second line. Older men."
- Log, pursuit entry: "Narration at scenes 84 and 85 states out loud that the accounts cannot agree **'which pilot, which aircraft, or what happened'**." The script says "which pilot, which aircraft, or **what went wrong**."

Both are inside quotation marks and presented as the script's text. Correct them or drop the quotation marks.

**M-2. The log misattributes the Stahms beat, and the SOURCES block makes a false blanket statement about Raketenspuren.** The log gives scenes 29 to 30 as "[de.wikipedia citing Kanetzki]". In the raw wikitext of `Peenemünde-West`, the Stahms and Milch sentence is footnoted to **"Volkhard Bode, Gerhard Kaiser: *Raketenspuren: Waffenschmiede und Militärstandort Peenemünde.* Ch. Links Verlag, 2011, S. 54."** Kanetzki footnotes the sentences that follow, on camp composition and work commandos. That also makes the SOURCES block's line "It is **not** the inline citation for any claim in this script" untrue: Raketenspuren is the inline citation for the claim narrated at scenes 29 and 30. The block's narrower point, that Raketenspuren is not the source for the intelligence-value argument in the Dewjatajew article, is correct and should be kept, but the blanket denial has to go. The Bode and Kaiser 2011 attribution the block mentions is confirmed by this same footnote.

**M-3. Visual 38 asserts something false on a TONE: STRAIGHT beat.** The visual reads "Burned rows of barracks at Trassenheide, and beyond them **the undamaged scientists' housing**." The scientists' housing estate was bombed. en.wikipedia's Operation Hydra article puts roughly 170 deaths in the settlement, and Thiel and Walther, the two technical staff the narration counts, were killed there in a slit trench. The narration at scene 38 is fine; the image contradicts the record and does so on a human-cost beat. Redraw as the burned Trassenheide barracks alone, or as damaged housing.

**M-4. Special Camp No. 7 was not on the Sachsenhausen site for most of his detention.** Scene 100 states flat: "Special Camp Number Seven. It occupied the site of Sachsenhausen concentration camp." Special Camp No. 7 was set up at Weesow in Brandenburg in May 1945 and only moved onto the Sachsenhausen grounds in August 1945, an advance party on 10 August and the main body arriving on the evening of 16 August. Devyatayev was in custody from February to September 1945. Even taking the Russian account at face value, at most the last three weeks of his detention could have been on that ground. The "If so" at scene 101 hedges the identification but not the chronology, and scene 101 is the line the notes call the one the episode turns on. Note also that ru.wikipedia's footnote for the Camp No. 7 identification is `samlib.ru`, a self-publishing site, which is Tier 3. Not blocking, because the narration attributes rather than asserts, but the beat is thinner than the file believes and one clause would fix it, for example "by then on the site of Sachsenhausen".

**M-5. Scenes 62 to 65 invert the source order.** In ru.wikipedia the group approached a parked aircraft, the guard noticed, and Sokolov gave the revetment cover story; the campfire was lit afterwards, at about noon, when the mechanics were packing up for the lunch break. The script lights the fire first and puts the cover story after. No claim is falsified and the comedy works better this way, but it is a chronology change and it is not noted anywhere in the file.

**M-6. The log's stated reason for not naming a weapon is false.** The log says "The method is not specified in the v2 sources, so the script does not name a weapon." ru.wikipedia specifies it: Krivonogov "убил конвоира, ударив его заранее заготовленной железной заточкой в голову", struck him in the head with a prepared iron spike. **The narration is right to stay silent**, both editorially and on tone. The log's reason is simply wrong and should be restated as a tone decision, not a sourcing one.

**M-7. Header word-count label.** Line 3 says "1,403 narration words". 1,403 is total spoken words. Narrator-only is 1,372; the other 31 are the three character-voice lines. The IMAGE BUDGET gets this right ("1,403 spoken words"). Cosmetic.

**M-8. "Nine kills" placement.** Scene 14 reads "May forty four. He talked his way back into fighters. Nine kills." de.wikipedia gives nine kills across 150 sorties for the whole war, not nine after May 1944. A viewer will hear the latter. One word fixes it, for example "Nine kills in all."

---

## Tone check

**PASS.** Re-checked from scratch, including every beat the revision touched.

- **Sachsenhausen block (18 to 22):** straight. The revised scene 20 lost a number and gained nothing comic.
- **Karlshagen and island block (31 to 38):** straight. The two revised beats are the ones that most needed care and both landed. Scene 34's "Witnesses called it the island's worst detail" is testimony, delivered flat. Scene 35's "Some were driven to Greifswald. Others buried on site." is the plainest possible statement of it, with no body count and no image of a chimney anywhere in the file.
- **Killing of the guard (66 to 67):** correct. The frame darkens before contact, no weapon is named, the memorial card is plain text and now carries no name. The preceding joke at 65 lands before the kill, not on it. Scene 61's "one home guard private, watching all ten" reads as a roast of the Reich's arrangements, not of the man.
- **Filtration and casualty block (93 to 103):** straight throughout, the strongest passage in the script, and the F-4 hedge did not soften it. "There was no parade" as an act title is bleak, not glib.
- **Cold open:** the sardonic register is aimed at German security, never at the prisoners. "That is the ratio" is dry, not a gag at their expense. Passes.
- **Scene 38 borderline, passed again:** "Two German technical staff died. Which brings us to the security arrangements." The irony targets German priorities. Flag for VO: play flat, no lift on "which brings us to".
- **Scene 53 dramatisation:** the fake German-pilot dialogue sits between two hedging lines and the notes forbid lifting it out for a Short or thumbnail. That is the right guardrail and it is written down.

No joke lands on camp conditions, casualties, the killing, or the filtration. **No tone failures.**

---

## Structural check

Measured with an independently written parser, then cross-checked against the folder's `verify_script.py`. Both agree exactly.

| Constraint | Required | Measured | Result |
|---|---|---|---|
| Visual tags | 112, contiguous 1 to 112 | 112, contiguous | PASS |
| REUSE tags | 10 | 10, at scenes 42, 60, 61, 69, 83, 100, 101, 106, 111, 112 | PASS |
| Total spoken words | 1,390 to 1,410 | **1,403** | PASS |
| Max beat length | 14 | 14 | PASS |
| 14-word beats | only 31, 33, 34, 97, 98, 101, 112 | exactly 31, 33, 34, 97, 98, 101, 112 | PASS, approved exception, not reported as defects |
| Beats over 14 words | none | none | PASS |
| Em-dashes | 0 | **0** | PASS |
| En-dashes | 0 | 0 | PASS |
| Brackets or stage directions in spoken lines | none | none, all 112 beats checked | PASS |
| Beat distribution vs notes | notes claim 3@10, 3@11, 45@12, 54@13, 7@14 | identical | PASS, I-7 closed |
| Act timecodes | continuous | 0:00-0:27, 0:27-1:17, 1:17-3:00, 3:00-4:38, 4:38-6:22, 6:22-7:15, 7:15-8:33, 8:33-8:53. No gaps, no overlaps | PASS |
| OUTRO end vs stated runtime | match | 8:53 and 8:53 at 158 wpm | PASS |
| Description chapters vs acts | match | all eight marks identical, and the 7:15 chapter carries the new Act 6 title | PASS |
| SOURCES URLs | resolve | 18 of 18 resolve. IWM and Tandfonline 403 to bots. Both Arolsen records load and their real titles match the block's descriptions | PASS, I-9 closed |
| Act-out hooks | every act | Cold open, 1, 2, 3, 5 strong. Act 4 still ends on "Then he found the elevator trim wheel", a resolution rather than a cliffhanger, unchanged from pass 2 and still the one boundary a viewer could leave on. Act 6 lands on the medal. Not a blocker | PASS with the standing note |
| FACT-CHECK LOG quotes narration accurately | required | **two misquotes**, see M-1 | **FAIL** |
| Description claims nothing absent from the script | required | **one, see N-2** | **FAIL** |

---

## Cold read notes

- It reads well and it reads honest. The myth-correction beats at 23 to 25 and 84 to 85 are still the best-written thing in the script, and 106 to 107 now lands cleanly with F-5 fixed.
- The F-1 demotion reads better than the old version did. Scene 52's "One German account, and only one" is a genuinely good line, and scene 54's "Treat it carefully" is the sort of thing this channel should say more often. It is a shame the beat that follows it undoes the work.
- Scene 55 is the one sentence a hostile viewer will screenshot. "Not in dispute" is a strong claim and the script cannot back half of it.
- Scene 4 is the other. First number of the episode, stated flat, and the script's own notes forbid stating it flat.
- The lunchtime callback from scene 2 to scene 62 is well planted and pays.
- Zero em-dashes, zero en-dashes, no stage directions in spoken lines, no brackets, TTS-safe throughout.
- Sentence-splitting across scene boundaries is applied consistently and reads at pace.

---

## Summary

The five blocking items from pass 2 are individually addressed and I confirmed each one against source rather than against the file's own claims about itself. F-2, F-3, F-4 and F-5 are genuinely closed. F-1's cuts are genuinely made, the title is off the failed claim, and the museum negative that the script now states out loud is accurate, which I verified by reading the museum page in full.

What blocks the ship is that the repair introduced its own version of the same disease. The chain that was supposed to be the safe ground under F-1 is two thirds unfootnoted German Wikipedia, from the very paragraph that was condemned, and the narration tells the viewer it is "not in dispute". The description hands a support-association newsletter's argument to a Tier 1 museum. The cold open states as fact a figure the script's own production notes forbid stating as fact, and states it wrongly. And one landing distance is asserted flat while the source that carries it carries a note disputing it.

None of these is hard to fix. N-1 needs one sentence rewritten and one attribution boundary moved. N-2 needs one sentence deleted. N-3 and N-4 need three words each. M-1 through M-8 are notes-and-visuals hygiene. Do those and I expect this passes.

VERDICT: FAIL

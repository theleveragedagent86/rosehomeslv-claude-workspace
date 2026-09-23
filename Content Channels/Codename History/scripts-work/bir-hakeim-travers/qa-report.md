# QA Report: She Drove the Breakout, Then Joined the Foreign Legion

Script under test: `script.md` (Bir Hakeim / Susan Travers, standard tier, 9 min)
QA run: 2026-09-01. Blocking gate.

---

## Structural checks

Method: all run with a Python script over `script.md`, not eyeballed. Spoken text is
defined as everything after `**NARRATOR:**` or `**X (character voice):**` on a line,
inside the script body only (everything above `## PRODUCTION NOTES`). Tokenisation
splits on whitespace and then discards any token containing no letter or digit, so a
stray quotation mark or a bare full stop is not counted as a word. This matters here
because naive whitespace tokenisation inflates counts on hyphenated forms and on the
opening and closing quote marks of the two Rommel lines. There are in fact zero
hyphens and zero digits anywhere in the spoken lines, so the two methods agree on
this script; I state the method anyway because the writer's 1,406 had to be
reproduced, not accepted.

| Check | Requirement | Measured | Result |
|---|---|---|---|
| Narration word count | 1,390 to 1,410 | **1,406** | PASS |
| Spoken beats | n/a | 112 | |
| Longest beat | max 14 words | **14** (33 beats sit exactly at the cap) | PASS |
| Shortest beat | no bare punch fragments | 8 words, Rommel's cleared quotation | PASS |
| Average beat | n/a | 12.55 | |
| `[VISUAL:]` tags | near 112 | **112** | PASS |
| `(REUSE: scene N)` | all point backwards at a matching picture | **11 of 11**, every one backwards, every one an exact word-for-word repeat of its target tag | PASS |
| Unique generations | writer reports 101 | **101** | PASS |
| Camera moves | none | none. Eight substring false positives only: "Spanish", "company", "pennant", "panzer" contain "pan"; "track" appears only as tank tracks and a tracked carrier | PASS |
| Em-dashes and en-dashes | zero | **zero**. U+2014, U+2013, U+2012, U+2015 all absent. The only `--` hits are markdown horizontal rules and table separators | PASS |
| Required sections | nine, in order | COLD OPEN, ACT 1 to ACT 7, OUTRO. Nine, in order. Title card after the cold open, END after the outro | PASS |
| Act-ending hooks | every act ends on a hook | all nine verified individually, listed below | PASS |
| Stage directions inside spoken lines | none | zero brackets, parentheses, braces, "VISUAL" or "REUSE" tokens inside any `NARRATOR:` or `(character voice)` line | PASS |
| Non-ASCII inside spoken lines | none | **zero**. No accented characters anywhere a TTS has to read | PASS |
| Digits inside spoken lines | none (numbers must be spelled) | zero | PASS |

**The 33 beats sitting exactly at 14 words** were each re-counted individually. None
is 15. The Manager-edited water beat, "The RAF air dropped a hundred and seventy
litres. Nearly all for the wounded," is one of them, at exactly 14. See test 12.

**Act-ending hooks, verified beat by beat:**

- Cold open: "She was not in it that night. That part comes later." Hook and disclaimer in one.
- Act 1: "And the first people to reach Bir Hakeim were not the Germans."
- Act 2: "By the second of June the ring closed. And somebody had come back in."
- Act 3: "She talked her way back into a siege. Which is bolder than refusing."
- Act 4: "The Germans decided to finish the job the next morning. They did not know."
- Act 5: Rommel, "Unfortunately for us, the French did not wait."
- Act 6: "So what did sixteen days at Bir Hakeim actually buy? Depends who you ask."
- Act 7: "And Churchill renamed the Free French the Fighting French. That part is real."
- Outro: the Amilakvari teaser.

**Reuse map, independently re-derived by numbering the 112 VISUAL tags 1 to 112 in
document order:** 29 to 26, 53 to 16, 72 to 5, 78 to 3, 79 to 6, 86 to 22, 87 to 21,
93 to 23, 100 to 46, 106 to 8, 107 to 9. Every target index is lower than its reuse
index, and every reuse tag is byte-identical to the tag it points at, so the build
will re-serve the existing file rather than generate a near-duplicate. The writer's
table is accurate.

---

## Tone check

**The writer's placement claim, verified independently rather than accepted.** I read
Acts 5 and 6 beat by beat and classified each of the 28 comic beats myself.

**Acts 5 and 6 contain exactly one comic beat, and it is the last line of Act 6.**
Confirmed. Act 5 has zero. Everything in Act 5 that could be mistaken for a joke is
grim understatement carrying information, not a punchline: "They only had to reach
them" is tension, not a laugh, and it sits before any casualty beat; "The driver
destroyed the gun anyway" is defiance, not a gag.

**The Act 6 joke, examined hardest, because this was the stated risk.** The line is
"So what did sixteen days at Bir Hakeim actually buy? Depends who you ask." Its
position relative to the human-cost beats:

| Beat | Content | Distance from the joke |
|---|---|---|
| "Of the men left behind, twenty two died in captivity without water." | death | 6 beats before |
| "One went blind. A hundred and eighteen died when their prison ship was torpedoed." | death, the last French casualty beat | 5 beats before |
| "Axis losses at Bir Hakeim are estimated at about three thousand three hundred." | death, the last casualty figure of any kind | 4 beats before |
| "Berlin radio then announced the prisoners would be executed as irregular troops." | a threat, not a death | 3 before |
| "De Gaulle promised the same for German prisoners. Berlin retracted the same day." | the threat withdrawn | 2 before |
| "Hitler had separately ordered captured German political refugees killed. Rommel ignored it." | an order not carried out | 1 before |
| "So what did sixteen days at Bir Hakeim actually buy? Depends who you ask." | the joke | |

**Verdict: NOT a tone FAIL.** Four beats separate the joke from the nearest casualty
figure and five from the nearest French death. The three beats in between are about a
threatened execution that was retracted and an order that was ignored, so nobody dies
in them. The joke's target is national historiography, not the men, and it lands on a
new picture (a stack of history books) which cues the register shift before the line
arrives. The writer's claim that it sits "after the last casualty beat, not adjacent
to one" is accurate as stated.

**One residual risk, advisory only.** The line follows immediately after an order to
kill prisoners. On a cold read with no pause, a listener could hear the shrug as
attaching to that. The mitigation is entirely in the VO direction, and the build notes
already ask for Act 7 "slowly and slightly tired" rather than bright. If the read of
"Depends who you ask" comes out arch rather than tired, it will scan wrong. Flagging
for the VO pass, not blocking the script.

**Comedy density in the front half, recomputed.** Cold open through Act 3 is 634
narration words. At the measured 158 wpm that is 240.8 seconds. I counted 22 comic
beats in that stretch, matching the writer: cold open 1, Act 1 seven, Act 2 eleven,
Act 3 three. That is one every 10.9 seconds, inside the every-15-to-20-second bar with
real margin. Act 4 has two and both are in its first half, before the water and the
wounded. The register-darkening claim holds.

**Are the early acts actually funny?** Yes, and this is not a formality. Act 2 has real
comic architecture rather than a string of asides: Rommel's dismissive order sets it
up, the Bersaglieri climbing back onto their trucks turns it, "This went exactly as
well as you are imagining" pays the audience's own arithmetic back to them, and the
punchline is a number, "Two men wounded, one truck, one gun," followed by a button
where the RAF keeps bombing tanks that are already dead. That is a built joke, not a
tone of voice. Act 1's "Every retelling calls them the French" is the strongest single
line in the episode because it is simultaneously the funniest and the most useful. No
flat-read risk in the front half.

**Nothing is joked about that should not be.** The Italians are never the butt; the
plan is. The garrison roster is played warm, not comic. The wounded, the aid post, the
prisoners, the torpedoed ship and the one-handed gunner are all read straight.

---

## Claim-by-claim verification

Sources are named by body, not by tier label alone. **MC22** is the Ministere des
Armees / DMPA booklet *Memoire et Citoyennete* no. 22, which I extracted and read in
French rather than fetching a summary of. **Saint-Hillier** is General Bernard
Saint-Hillier's eyewitness narrative at the Fondation de la France Libre. **artillerie**
is the Association de l'Artillerie's two-part study, which is independent of Wikipedia.
**Chauliac** is Guy Chauliac, *Le service de sante de la France Libre 1940 a 1943*,
hosted by the 1re DFL association. **Montanari** is the Italian Ufficio Storico SME
official history. **Playfair** is the British official history. **Rondeau** is Benoit
Rondeau's own site. **Esprit defense** is Ministere des Armees no. 3, spring 2022.

| # | Claim (as spoken) | Where | Source(s) checked | Verdict |
|---|---|---|---|---|
| 1 | "Bir Hakeim is a dry well and an old Italian camel corps post" | Act 1 | MC22: "un ancien poste mehariste italien etabli pres d'un puits a sec" | PASS, Tier 1 verbatim |
| 2 | "Seventy kilometres inland... southwest of Tobruk" | Act 1 | MC22: "a quelque 70 kilometres de la cote mediterraneenne, au sud-ouest de Tobrouk" | PASS, Tier 1 verbatim |
| 3 | "no hill... nothing to hide behind" / "a triangle sixteen kilometres around" | Act 1 | MC22: "un triangle, d'un perimetre d'environ seize kilometres, qu'aucun obstacle naturel ne defend" | PASS, Tier 1 verbatim |
| 4 | "Trenches cut a metre into solid rock. By hand. With picks. For three months." | Act 1 | MC22 confirms the earthworks with no dimension. fr.wikipedia's "un metre" attaches to **abris** (shelters), not trenches. Arrival 14 Feb, battle 26 May, so "three months" understates 3.5 and errs safe | SOFTEN (S8) |
| 5 | "General de brigade Marie Pierre Koenig. Former Foreign Legion officer." | Act 1 | MC22. Correctly not called Marshal or general d'armee, both later ranks | PASS |
| 6 | "about three thousand seven hundred men" | Act 1 | MC22: "plus de trois mille sept cents hommes"; annex gives 3,723 credited to the musee de l'Armee | PASS, Tier 1 |
| 7 | "Two thirds came from the colonies and overseas." | Act 1 | defense.gouv.fr/terre: "deux tiers sont issus des colonies et des outremers" | PASS, Tier 1 |
| 8 | "Two Foreign Legion battalions, including nearly three hundred Spanish Republicans." | Act 1 | Two Legion battalions: MC22, Tier 1. The ~300 is cited to Milza, Peschanski and Cuesta Bustillo, *Exils et migration*, L'Harmattan 1994, academic press, and attaches to the 3rd battalion, which is one of the two. The script's fact-check log **understates** this as "no ministry source"; academic press is stronger than the log claims | PASS |
| 9 | "A Pacific battalion. Volunteers from French Polynesia, New Caledonia and the New Hebrides." | Act 1 | Unit at Tier 1 (MC22 "du bataillon du Pacifique"); the three territories from fr.wikipedia, corroborated in substance by defense.gouv.fr/terre | PASS |
| 10 | "A battalion from Oubangui Chari, which is now the Central African Republic." | Act 1 | MC22: "du 2e bataillon de marche de l'Oubangui". Territory correct | PASS, Tier 1 |
| 11 | "A North African company. Algerians, Tunisians and Moroccans. About a hundred and eighty men." | Act 1 | Unit at Tier 1 (MC22 "d'une compagnie nord-africaine"). The ~180 and the nationalities are fr.wikipedia only, uncited | SOFTEN (S7) |
| 12 | "German and central European antifascists and refugees, wearing French uniforms." | Act 1 | Not found in any Tier 1 source, nor in the fr. or en. articles on the 13e DBLE. Historically orthodox and supported circumstantially by Porch's Hitler order, which presupposes the category | SOFTEN (S9) |
| 13 | "And a British anti aircraft battery, sitting right there in the position." | Act 1 | MC22: "La DCA est renforcee par une batterie anglaise". Tier 1. The script wisely names no unit; the circulating "HAA" designation is wrong, it was Light AA with Bofors 40 mm, which MC22 independently lists | PASS |
| 14 | "a Georgian prince called Dimitri Amilakvari" commanding the Legion battalions | Act 1 | Ordre de la Liberation: born Gori 12 Nov 1906, "le Prince Dimitri Amilakvari", given command of the 13e DBLE 16 Sept 1941, Koenig's deputy at Bir Hakeim | PASS, Tier 1 |
| 15 | "Twenty sixth of May. Rommel opens the Gazala offensive and swings five divisions south." | Act 1 | MC22 chronology and narrative | PASS, Tier 1 |
| 16 | "Twenty seventh of May. Rommel hands the job to the Italian Ariete division." | Act 2 | fr.wikipedia names the 09:00 order to De Stefanis; MC22 independently confirms the Italians attacked and were repulsed. Refinement: the assault was actually pressed by Lt-Col Prestisimone's IX Tank Battalion on its own initiative | PASS |
| 17 | Rommel: "Take the little fort in the corner. Should not take long." | Act 2 | Compresses the documented 27 May order plus MC22's "La prise du reduit ne doit etre qu'une formalite rapidement accomplie" ("the taking of the redoubt was to be no more than a formality quickly accomplished"). That is the ministry's own characterisation of the German expectation, so the line invents no view | PASS |
| 18 | "The Bersaglieri climbed off their trucks, got shelled, and climbed back on." | Act 2 | artillerie: "Devant les pertes, les troupes adverses sont contraintes a rembarquer et a se replier. Les chars italiens sont desormais seuls." Saint-Hillier: "Le 8e regiment de Bersaglieri... abandonne a son sort le 132e regiment de chars." Two independent sources, and the re-embarking is explicit | PASS, and better sourced than the log claims |
| 19 | "seventy odd tanks charging a minefield entirely on their own" | Act 2 | Saint-Hillier: "70 chars de la division Ariete"; artillerie: "deux vagues de 50 et de 20 chars". Montanari gives 60 to 62. 70 is the French estimate | PASS as a French figure |
| 20 | "A crew under Sergeant Walter Grand destroyed all six at point blank range." | Act 2 | Six inside and point-blank destruction verified independently (artillerie: "32 chars ennemis sont detruits dont 6 a l'interieur de la position"). **The name is not.** See F9 | **FAIL (F9)** |
| 21 | "Under an hour." | Act 2 | Saint-Hillier: "elle dure moins d'une heure"; artillerie: 09:30 to 10:15. **True, but not on MC22's authority**, which says "En une heure" | PASS on a different source than the writer thought |
| 22 | "The division went from over seventy tanks to thirty three." | Act 2 | Garbled. See F6 | **FAIL (F6)** |
| 23 | "It left thirty two tanks behind, and ninety one prisoners, including a colonel." | Act 2 | MC22: "quatre-vingt-onze prisonniers", "une trentaine de chars". 32 is the consensus across fr., it. and artillerie. Prestisimone verified. Script wisely says only "a colonel" | PASS, Tier 1 |
| 24 | "French losses that morning. Two men wounded, one truck, one gun." | Act 2 | fr.wikipedia only, uncited. Absent from MC22, Saint-Hillier and artillerie. Italian sources say "nessuna perdita da parte francese" | SOFTEN (S1) |
| 25 | "One captain burned his pennant, certain the position was lost." | Act 2 | Corroborated from **Koenig's own memoirs** p.223 via it.wikipedia, with the tank 15 metres away. Script correctly does not name him | PASS, better sourced than the log claims |
| 26 | "Then the RAF started bombing the wrecked Italian tanks." | Act 2 | Mechanism is wrong. See F12 | **FAIL (F12)** |
| 27 | "By the second of June the ring closed." | Act 2 | MC22 says the investment **began** 2 June; fr.wikipedia puts full encirclement at 6 June | **FAIL (F8)** |
| 28 | "Born in Kensington, London, nineteen oh nine." | Act 3 | GRO civil registration index via en.wikipedia; Esprit defense gives "naissance a Londres". France-Soir 1996 says Folkestone but that piece also misdates the battle's end to 19 June and puts 5,000 men at Bir Hakeim | PASS, conflict correctly resolved |
| 29 | "Semi professional tennis player." | Act 3 | Unsourced everywhere. See F5 | **FAIL (F5)** |
| 30 | "the Free French in London, August nineteen forty" | Act 3 | Esprit defense quoting SHD gives 1 Aug; France-Soir gives 28 Aug. "August nineteen forty" is true under both | PASS, conflict handled correctly |
| 31 | "By the summer of nineteen forty one, Koenig had made her his driver." | Act 3 | Esprit defense: "Au Levant, en plein ete 1941, le general Koenig la choisit comme chauffeur." Script gives him no rank, avoiding the source's own retroactive-rank slip | PASS, Tier 1 |
| 32 | "The legionnaires called her la Miss. She was the only woman in the brigade." | Act 3 | Esprit defense: "surnommee la miss"; "Seule femme de toute la brigade" | PASS, Tier 1 |
| 33 | "A researcher at the French defence archives says she also became his mistress." | Act 3 | Esprit defense states it in the article's own voice: "Elle deviendra aussi sa maitresse." Letang is quoted immediately after treating it as real ("cette histoire d'amour") but does not utter the attributed sentence | SOFTEN (S10) |
| 34 | "She did not refuse. She left." plus the convoy and the granted permission | Act 3 | fr.wikipedia citing Le Figaro 3-4 Mar 2018 and Le Monde 4 Mar 2018; en.wikipedia carries the same sequence and flags the Holden version with a citation-needed tag. **No credible source supports the refusal.** The refusal traces solely to Holden's 2009 BBC piece and content farms downstream of it | **PASS, strongly. See test 2** |
| 35 | "Second of June. Two Italian officers arrive under a white flag..." and three refusals | Act 4 | MC22: "Trois ultimatum successifs sont adresses aux Francais, en vain, les 2, 3 et 5 juin." The 10:30 detail corroborated by Playfair via en.wikipedia | PASS, Tier 1 |
| 36 | "Forty thousand heavy shells came in. The French fired forty two thousand back." | Act 4 | fr.wikipedia only, uncited. Covers 2 to 10 June only, and "heavy" means 105 to 220 mm | SOFTEN (S5) |
| 37 | "By Rommel's own count the Luftwaffe flew thirteen hundred attacks on the position." | Act 4 | Rommel, *La guerre sans haine*, via Fondation de la France Libre: "entre le 2 et le 11 juin... la Luftwaffe executa 1.300 attaques." Correctly attributed to Rommel | PASS, Tier 1 verbatim |
| 38 | Rommel: "You cannot drive tanks through a minefield full of anti tank guns." | Act 4 | Rommel's own words: "Kesselring exigea le declenchement immediat d'une offensive de grand style... Or, c'etait la une impossibilite ; les chars ne pouvaient etre utilises dans les champs de mines truffes de points d'appui." The line glosses "points d'appui" as anti-tank guns, which MC22 independently supports ("canons de 25, 47 et 75 mm") | PASS, fair compression |
| 39 | "Six hundred and twenty abandoned Indian prisoners walked in." | Act 4 | fr.wikipedia (uncited) and en.wikipedia (3rd Indian Motor Brigade, 30 May, plus 243 prisoners already there), but en. cites Liardet, who is also fr.'s external link, so probably one origin | SOFTEN (S6) |
| 40 | "a hundred and seventy litres. Nearly all for the wounded." | Act 4 | Source says "surtout", not "presque entierement". See F7 | **FAIL (F7)** |
| 41 | "Forty two Stukas. One bomb hit the brigade aid post." / "Seventeen men... killed there." | Act 4 | See F3 | **FAIL (F3)** |
| 42 | "An eighty eight destroyed a French gun crew... He loaded with the stump... That comes from a French general who was there." | Act 4 | fr.wikipedia quoting General Saint-Hillier, a 1re DFL veteran. The narration attributes it exactly as it stands and claims no more | PASS, correctly attributed |
| 43 | "About two hundred shells left. Seven hundred mortar bombs." | Act 4 | Untraceable, and the real figure is per gun. See F2 | **FAIL (F2)** |
| 44 | "The brigade will break out of the position by force." | Act 5 | FSALE quotes the order verbatim: "La brigade sortira de vive force cette nuit de la position. Elle s'ouvrira un passage vers le sud-ouest, les armes a la main." I fetched and read this myself | PASS, verbatim |
| 45 | "Two hundred trucks waited fifteen kilometres away." | Act 5 | Those are the numbers in Koenig's **order**. Saint-Hillier says 100 trucks of the 101e compagnie du train; Pitt says 7 km; MC22 says only "quelques kilometres plus loin" | SOFTEN (S2) |
| 46 | "The sappers were meant to clear a lane two hundred metres wide." / "much narrower than that" | Act 5 | fr.wikipedia, en.wikipedia (Pitt), FSALE and Saint-Hillier all agree. **No source anywhere gives a measured width for what was cleared, and the script speaks none** | PASS |
| 47 | "The lead company got out at quarter past midnight. Over an hour late." | Act 5 | FSALE: "Le II/13e doit quitter le dispositif en tete a 23 heures" and "a 0 heures 15, le 2e bataillon... s'engage dans la chicane." Saint-Hillier gives ~00:30 | PASS |
| 48 | "Two enemy automatic weapons opened on the leading company inside the minefield." | Act 5 | FSALE verbatim: "Deux armes automatiques ouvrent le feu sur la compagnie de tete... Ces premieres rafales ennemies causent des ravages dans ces unites qui marchent en formation serree." Both this beat and the next are the source's own words | PASS, verbatim |
| 49 | "Bren Carriers charged the gun positions and physically drove over them." | Act 5 | FSALE: "allant jusqu'a les ecraser sous leur poids"; Saint-Hillier independently describes the same act | PASS, two sources |
| 50 | "Lieutenant Dewey charged Breda guns three times..." / "A fifty millimetre gun killed him and his entire crew except the driver." | Act 5 | FSALE verbatim, and the **50 mm is confirmed by two independent sources** (FSALE and Saint-Hillier). fr.wikipedia is the outlier here with a 20 mm and a misspelled name; the script is right and fr.wikipedia is wrong | PASS |
| 51 | "Two more officers died on foot, throwing grenades." | Act 5 | The deaths of de Lamaze and Bricogne are confirmed by three sources. The on-foot-with-grenades manner is fr.wikipedia only, and FSALE gives a different account of de Lamaze's death | SOFTEN (S11) |
| 52 | "Susan Travers drove Koenig's car out through the gap, near the column's front." | Act 5 | FSALE places her driving Koenig's command van through the fire. Saint-Hillier independently puts Koenig "en tete du convoi motorise" but behind Bellec's Bren carriers, with the dismounted battalions ahead of that. **"Near the column's front" is exactly right** and is better supported than the writer believed | PASS, and the hedge is correctly calibrated |
| 53 | "By her own account she told the general to get down in the back." | Act 5 | Attributed on screen and correctly | PASS |
| 54 | "By eight in the morning the bulk of the brigade had reached the British." | Act 5 | Three-way conflict: 07:00 (Playfair), 07:30 (Saint-Hillier), 08:00 (fr.wikipedia) | SOFTEN (S3) |
| 55 | "Rommel attacked an empty fortress that morning. He counted twelve hundred fighting positions." | Act 5 | Not empty, and Rommel is not the source of the 1,200. See F13 | **FAIL (F13)** |
| 56 | Rommel: "Unfortunately for us, the French did not wait." | Act 5 | Verified verbatim with full provenance. See test 7 | PASS, Tier 1 |
| 57 | "About two thousand six hundred of three thousand seven hundred men reached British lines." | Act 6 | Spread is 2,500 (MC22) / 2,619 (Broche via fr.wikipedia) / 2,700 (defense.gouv.fr/terre and Playfair). "About 2,600" is the honest rounding of Broche's precise 2,619, not an average | PASS with a note, see test 3 |
| 58 | "More than a thousand were killed, wounded, captured or missing." | Act 6 | MC22 verbatim: "Plus de mille hommes sont tues, blesses, prisonniers ou disparus." Independently supported by the detailed breakdown totalling 1,033 and by en.wikipedia's 1,184 | PASS, Tier 1 verbatim |
| 59 | "Some accounts say around nine hundred, because they count the missing differently." | Act 6 | The ~900 exists; **the stated reason does not.** See F4 | **FAIL (F4)** |
| 60 | "The North African company lost seventy four men out of roughly one hundred eighty." | Act 6 | fr.wikipedia, uncited: 10 killed, 47 missing, 17 wounded, internally consistent at 74 | SOFTEN (S7) |
| 61 | "The Oubangui Chari battalion brought out sixty percent of its strength." | Act 6 | **Citation a l'ordre de l'Armee signed by de Gaulle**: "a reussi finalement a percer les lignes ennemies et a ramener 60 % de ses effectifs". A primary document | PASS, and the best-sourced casualty claim in the episode |
| 62 | "twenty two died in captivity without water" / "One went blind." | Act 6 | fr.wikipedia, footnoted. Source says four days specifically; the script does not inflate it | PASS with the log's own single-source flag standing |
| 63 | "A hundred and eighteen died when their prison ship was torpedoed." | Act 6 | Contradicted: Fondation de la France Libre material gives 143 French missing from the Nino Bixio. See F10 | **FAIL (F10)** |
| 64 | "Axis losses at Bir Hakeim are estimated at about three thousand three hundred." | Act 6 | Broche, *Bir Hakeim*, Perrin/Tempus 2012, pp. 158-160, via fr.wikipedia, under a heading reading "Du cote de l'Axe". en.wikipedia concurs: "3,300 dead or wounded". **The word Axis is in the same sentence and it is correct** | PASS. See test 3 |
| 65 | Radio Berlin, de Gaulle's reciprocity, the same-day retraction | Act 6 | de Gaulle, *Memoires de guerre* p.319, via fr.wikipedia. Partisan primary, de Gaulle recounting his own bluff, and no independent record found | PASS with the log's flag standing |
| 66 | "Hitler had separately ordered captured German political refugees killed. Rommel ignored it." | Act 6 | Porch p.272; en.wikipedia states it in near-identical terms. **No sweeping order about Free French exists.** See test 6 | PASS, Tier 1 |
| 67 | "France says the battle saved the Eighth Army and made El Alamein possible." | Act 7 | Verified as a real and widely-stated French claim, correctly reported as a claim rather than made | PASS |
| 68 | "A historian of the Afrika Korps calls that ridiculous and without foundation." | Act 7 | Rondeau's "ridicule et sans fondements" attaches specifically to the El Alamein half. See F14 | **FAIL (F14), narrow** |
| 69 | "Bir Hakeim fell on the eleventh. Tobruk did not fall until the twenty first." | Act 7 | MC22 for both. Rondeau makes the identical point: "il faut encore attendre plus de dix jours pour que Tobrouk tombe (le 21 juin)" | PASS, Tier 1 |
| 70 | "The fighting that actually broke the Eighth Army happened elsewhere on the same line." | Act 7 | Rondeau, plus fr.wikipedia's own "Contestation de la these officielle" section | PASS |
| 71 | "And Rommel's panzers were mostly not there. A few dozen German tanks." | Act 7 | First half verbatim from Rondeau. **The second half misappropriates a different sentence of his.** See F11 | **FAIL (F11)** |
| 72 | "The French defence ministry itself claims only three things." / "It slowed the advance, delayed Tobruk, and let the British pull back." | Act 7 | MC22 verbatim, read by me in the original: "ils ont freine l'avancee allemande, retarde la prise de Tobrouk et surtout permis aux troupes britanniques de se replier." All three, in order, and **MC22 makes no El Alamein claim anywhere** | PASS, Tier 1 verbatim. The strongest beat in the act |
| 73 | "The French telling also forgets the British battery, the air cover and the supply." | Act 7 | Rondeau verbatim: "quelques Britanniques etaient avec eux, et surtout la Desert Air Force, ils ont ete ravitailles par la 8th Army". All three elements, in order | PASS |
| 74 | "Almost everything English about Susan Travers traces back to one book she co wrote." | Act 7 | en.wikipedia is footnoted almost entirely to Holden, including a 2009 BBC piece Holden wrote herself. Structurally verified | PASS |
| 75 | "And Churchill renamed the Free French the Fighting French. That part is real." | Act 7 | Wrong actor. See F1 | **FAIL (F1)** |
| 76 | "June nineteen forty five... enrolled her as an adjudant chef and gave her a service number." | Outro | Esprit defense: "en juin 1945, Susan Travers reussit a integrer officiellement la Legion etrangere au grade d'adjudant-chef." Timeline sidebar independently prints "Juin 1945". Service number 22166 is **not** Tier 1 and is correctly not spoken | PASS, Tier 1 |
| 77 | "the form had no box for man or woman" attributed to a defence archives researcher | Outro | Esprit defense quoting Geraud Letang of the SHD: "il n'existait pas de case 'homme' ou 'femme' sur le formulaire d'engagement". Attribution exact | PASS, Tier 1 verbatim |
| 78 | "She is still the only woman ever formally enrolled in the Foreign Legion." | Outro | Every Tier 1 source says "**premiere**" (first), not "seule". "Only" is a well-supported inference from first-plus-none-since, and the word "still" carries it | SOFTEN (S12) |
| 79 | "She took the Legion of Honour in nineteen ninety six, aged eighty six." | Outro | Fondation de la France Libre: "Le 22 mai 1996, a Savigny-sur-Orge... miss Susan, 86 ans, a ete decoree de la Legion d'honneur." Age arithmetic checks: born 23 Sept 1909, so 86 in May 1996 | PASS |
| 80 | "the Georgian prince who commanded the Legion battalions and died that October" | Outro | Ordre de la Liberation: killed 24 October 1942 at El Himeimat. Same year, October | PASS, Tier 1 |
| 81 | "a thirty two year old Englishwoman" | Cold open | Born 23 Sept 1909, breakout 11 June 1942, so 32. Arithmetic correct | PASS |
| 82 | "Three years later" (1942 to 1945) and "Three years after the breakout" | Cold open, outro | June 1942 to June 1945 is exactly three years | PASS |
| 83 | "Her car came out riddled with bullets. She said she counted eleven." | Cold open | "Criblee de balles" is FSALE's own phrase. The eleven is one origin. See test 5 | SOFTEN (S4) |

---

## Episode-specific tests

### Test 1. THE CENTRAL CORRECTION: Travers was not in the Foreign Legion at Bir Hakeim. **PASS, strongly.**

**The enrolment verified independently.** *Esprit defense* no. 3, spring 2022, a
Ministere des Armees publication: "en juin 1945, Susan Travers reussit a integrer
officiellement la Legion etrangere au grade d'adjudant-chef" ("in June 1945, Susan
Travers succeeded in officially joining the Foreign Legion at the rank of
adjudant-chef"). The same document's timeline sidebar independently prints "Juin
1945". Month, year and rank all confirmed at Tier 1. Her status in 1942 was a Free
French volunteer driver attached to the 13e DBLE, which is what the script says.

**She is never given a rank in the desert.** Verified mechanically across all 112
spoken beats: the tokens "adjudant", "sergent", "sergeant" (of her), "legionnaire" and
"corporal" never attach to Travers before the outro. Worth noting because the FSALE
page, which the script otherwise leans on heavily, calls her "Le sergent-chef Susan
Travers" in its breakout narrative. That is a retroactive anachronism, it is sitting
right there in a source the writer used, and the writer did not copy it. Good
discipline.

**The cold read, done properly.** I read the title, the cold open and Act 3 in
sequence at speed, as a viewer hears them, without pausing to reason. The brief warned
that the script might be leaning on the single word "then". It is not. There are five
independent layers, and any one of them alone would probably do the job:

1. **The title's "then" is a sequence word in the headline itself**, and the two facts
   are in the only order that is true.
2. **The cold open's Legion beat leads with the interval, not the claim.** The sentence
   is "Three years later she became the only woman ever enrolled in the Foreign
   Legion." The listener hears "Three years later" before the word Legion arrives, so
   the gap is established before the claim it qualifies.
3. **The picture agrees with the words.** The VISUAL on that beat is an enlistment form
   on a desk, not a desert image, so the frame moves to 1945 at the same moment the
   narration does.
4. **The very next beat states the correction in plain words**: "She was not in it that
   night. That part comes later." No hedging language, no subordinate clause.
5. **The outro restates the date twice**, "June nineteen forty five" and "Three years
   after the breakout", in consecutive clauses.

**The one place I expected to find a leak, and did not.** Act 3 contains "The
legionnaires called her la Miss." That is the only time the word legionnaire comes near
her in the desert, and it casts them as a separate body who named her. She is the
object of the sentence, not a member of the group. The line immediately after is "She
was the only woman in the brigade", which uses **brigade**, not Legion. Correct on both.

**Residual risk, unavoidable and accepted.** A viewer who sees only the thumbnail in a
feed and never presses play could conflate the two halves of the title. No title that
keeps the Legion hook can do better than putting "then" between them, and the Legion
hook is the click. The recommended title is the right call.

### Test 2. She did not refuse the evacuation order. **PASS, strongly.**

**The sequence verified independently:** ordered out at the end of May, left, attached
herself to a resupply convoy, asked permission to return, permission granted. French
Wikipedia carries it citing *Le Figaro* 3 to 4 March 2018 and *Le Monde* 4 March 2018.
English Wikipedia carries the same sequence and, notably, flags the Holden refusal
version with a citation-needed tag.

**I searched specifically for support for the refusal version and found none in any
credible source.** It traces to Wendy Holden's 2009 BBC News piece and to English
content farms downstream of it. No French source states it. No ministry source states
it. This is the correction the episode was built to make and it holds.

**The script never writes the refusal version.** Verified by text search across the
full body: "refuse" appears exactly twice, once as "She did not refuse. She left" and
once as "Which is bolder than refusing." Both are the correction, not the myth.

**The "here is where the English version goes wrong" framing is itself accurate**, which
was the subtler half of this test. The refusal story is genuinely an English-language
artefact with an English-language origin, and the correct version is genuinely the one
carried in the French press and in the ministry-adjacent record. The script is not
inventing a national contrast for rhetorical convenience. It is describing a real one.

### Test 3. The casualty figures. **PASS on the labelling and the structure. One FAIL inside it (F4).**

**Each figure checked against what it measures:**

- **"More than a thousand killed, wounded, captured or missing."** MC22 verbatim: "Plus
  de mille hommes sont tues, blesses, prisonniers ou disparus." I read this in the
  original PDF myself. The script's four categories match the source's four categories
  in order. Independently corroborated by the detailed breakdown (99 killed and 109
  wounded during the siege, 41 killed, 21 wounded and 763 missing in the breakout,
  totalling **1,033**, arithmetic redone by me) and by English Wikipedia's 141 killed,
  229 wounded, 814 prisoners, totalling **1,184**. Both independent totals clear a
  thousand. **PASS.**
- **The ~3,300 is correctly labelled Axis.** Broche, *Bir Hakeim*, Perrin/Tempus 2012,
  pp. 158 to 160, under a heading reading "Du cote de l'Axe" ("On the Axis side").
  English Wikipedia concurs at "3,300 dead or wounded". The script says "**Axis** losses
  at Bir Hakeim are estimated at about three thousand three hundred," with the word
  Axis inside the same sentence. The pitch's original category error, treating it as a
  rival French count, is **not reproduced anywhere**. **PASS.** One correction to the
  script's own fact-check log: it credits this figure to defense.gouv.fr, which actually
  describes the losses as *allemandes* (German). Broche is the correct citation and says
  Axis. The narration is right and the log's sourcing note is wrong.
- **Nothing is averaged.** Confirmed. No spoken figure in the episode is the mean of two
  sources.
- **The residual disagreement is named, but the stated reason is invented.** This is
  **F4**. The script says the ~900 band arises "because they count the missing
  differently." No source says that, and the arithmetic refuses it: from the 1,033
  total, removing the 600 prisoners gives 433, and removing all 763 missing gives 270.
  Neither operation produces 900. FSALE's 946 sits on a different garrison baseline
  entirely (3,826). The variation is real; the mechanism is a fabricated explanation.
  **FAIL, fix supplied.**

**Garrison strength and got-out figures against Tier 1:**

- **Garrison.** MC22: "plus de trois mille sept cents hommes", with its annex giving
  3,723 credited to the musee de l'Armee. The script says "about three thousand seven
  hundred". **PASS, Tier 1.**
- **Got out.** The spread is **2,500** (MC22, "Quelque deux mille cinq cents hommes
  reussissent leur sortie"), **2,619** (Broche via French Wikipedia), **2,700**
  (defense.gouv.fr/terre and Playfair via English Wikipedia). The script says "about
  two thousand six hundred". **I considered failing this as splitting the difference and
  decided not to**, for a specific reason: 2,600 is not the mean of 2,500 and 2,700, it
  is the honest rounding of Broche's precise 2,619, which is a real sourced count. The
  word "about" is present. All three figures sit within four percent of it. **PASS with
  the spread recorded here**, and if the Manager wants the maximally conservative
  version, the Tier 1 number is 2,500, not 2,600.

### Test 4. The strategic claim, the episode's spine. **PASS on the load-bearing quote. Two FAILs inside it (F11, F14).**

I read Rondeau's article in French myself rather than accepting a summary, because the
brief correctly said a subtle error here is worse than an obvious one elsewhere.

**The ministry's own three-part modest claim is stated exactly right.** MC22, read by me
in the original: "En retenant Rommel et ses troupes, ils ont **freine l'avancee
allemande**, **retarde la prise de Tobrouk** et surtout **permis aux troupes
britanniques de se replier**." The script: "It slowed the advance, delayed Tobruk, and
let the British pull back." Three claims, in the source's own order, with no
embellishment and no fourth claim smuggled in. **I also searched the whole booklet and
confirm the ministry makes no El Alamein claim anywhere.** This is the single most
important sentence in the episode and it is correct. **PASS.**

**The specialist's rebuttal is represented too broadly.** This is **F14**. Rondeau's
"Une assertion ridicule et sans fondements" attaches to one specific proposition, which
he then states outright: "Cette resistance prolongee n'a nullement permis le
retablissement britannique sur El Alamein" ("this prolonged resistance in no way
permitted the British recovery at El Alamein"). The script's preceding beat bundles two
claims, saving the Eighth Army **and** making El Alamein possible, and then applies
"ridiculous and without foundation" to the pair. He said it about the El Alamein half.
This matters more than it looks, because four beats later the script endorses the
ministry's "let the British pull back", which is a weaker relative of the saved-the-
Eighth-Army claim. As written, the act appears to call something ridiculous and then
half-endorse it. **FAIL, fix supplied, and the fix makes the act sharper rather than
weaker** because it shows the episode splitting the claim instead of swinging at both.

**Is Rondeau himself overstated?** No, and I checked for it. His three checkable
assertions are independently verifiable and I verified them: Tobruk fell ten days later
(MC22 confirms 21 June), the German armour was largely elsewhere (Rommel's own diary has
90th Light and Trieste carrying the siege, an Afrikakorps shock group under Baade only
on 10 June and 15th Panzer ordered up after that), and the Free French were not alone
(MC22 independently lists the British AA battery and states the brigade "beneficient du
soutien logistique et de la couverture aerienne des Britanniques"). The script leans on
the checkable points as well as the opinion, which is the right structure. **One venue
caveat stands:** the article is on his own site, not in a peer-reviewed journal. His
credentials are real (Tallandier 2013, Perrin 2019).

**"The French telling also forgets the British battery, the air cover and the supply."**
Rondeau verbatim: "nos FFL n'etaient pas seuls: quelques Britanniques etaient avec eux,
et surtout la Desert Air Force, ils ont ete ravitailles par la 8th Army." Three
elements, same order, accurately rendered. **PASS.**

**"A few dozen German tanks" misappropriates a different sentence.** This is **F11**.
Rondeau's first clause is quoted correctly: "les Panzer de l'Afrika-Korps et le gros des
troupes allemandes de l'armee de Rommel ne se battent pas a Bir Hacheim." But "a few
dozen German tanks" is lifted from "quelques dizaines de chars allemands **en plus a El
Alamein**", which is a **counterfactual about El Alamein**, not a count of German armour
at Bir Hakeim. He is arguing that a few dozen extra tanks would not have changed El
Alamein. The script turns it into a headcount of the siege. **FAIL, fix supplied.**

**The English overclaim half of the act is sound.** "Almost everything English about
Susan Travers traces back to one book she co wrote" is verified structurally: English
Wikipedia's article is footnoted almost entirely to Holden, including a 2009 BBC piece
Holden wrote herself, which is one origin appearing twice. **PASS.**

### Test 5. The eleven bullet holes. **PASS on the hedge. SOFTEN recommended (S4).**

**Traced.** The count reaches English through Wendy Holden and only Holden: *Tomorrow to
Be Brave* (Free Press, 2000) and a 2009 BBC News article Holden wrote herself. Those are
one origin cited twice, exactly as the research suspected. **No independent source gives
a count.** The official French phrase is FSALE's "la camionnette, **criblee de balles**,
a pris une bonne direction", which asserts the condition and supplies no number. There is
also a competing figure in circulation, roughly twenty, appearing as a gloss on a 1re DFL
association page, which is itself weak but establishes that the eleven is contested.

**Is the hedge strong enough?** Formally, yes. "Her car came out riddled with bullets.
She said she counted eleven" splits the beat correctly: "riddled" is the French record's
own word and is asserted; the count is attributed to her and is not asserted. That is not
an auto-FAIL, because the auto-FAIL condition requires a significant claim asserted
**without** a hedge, and this one is hedged accurately. Holden does report Travers saying
it, so "She said" is true.

**But there is a structural problem the brief did not ask about and I am flagging
anyway.** Act 7's thesis is that almost everything English about Travers traces to one
book. The cold open's hook is a number from exactly that book, presented without saying
so. The episode's own argument undercuts its own opening. Softening the cold open to
signal the thinness costs nothing and makes Act 7 land harder when it arrives. **S4,
word-count neutral.**

### Test 6. The Hitler order. **PASS.**

**The negative check is clean.** I searched in French and English for any general Hitler
order that captured Free French be shot. **NOT FOUND**, confirming the research. It does
not appear anywhere in the script: I verified by text search that no beat asserts a
sweeping order, and the only Hitler beat is the narrow one.

**The narrow documented version is what appears**, and it is correct: "Hitler had
separately ordered captured German political refugees killed. Rommel ignored it." Porch,
*Hitler's Mediterranean Gamble* (2005), p. 272; English Wikipedia states it in
near-identical terms: "Hitler had ordered that captured German political refugees were to
be killed, an order that Rommel ignored." Two statements of the same narrow claim.
**PASS.**

**The Radio Berlin sequence verified in order.** Berlin radio announced the prisoners
would be executed as irregular troops, de Gaulle promised reciprocity for German
prisoners on the BBC, Berlin retracted the same day. Source is de Gaulle, *Memoires de
guerre, L'Appel 1940-1942*, Plon 1954, p. 319. **This is de Gaulle recounting his own
successful bluff and I found no independent record of the exchange.** It is specific,
dated and citable, and it is partisan primary. The script states it plainly and
attributes it to no ministry or archive, which is the correct handling for a
self-reported episode. The script's own log flags it accurately. **PASS.**

**A structural point in the script's favour:** placing the Hitler order beat on a reused
picture of the German antifascists from Act 1 is the correct visual argument, because
those are the men the order was actually about. That reuse is doing real work.

### Test 7. The Rommel quote. **PASS, with full provenance.**

**Wording and provenance verified at source.** Fondation de la France Libre, reproducing
the Bir Hakeim extract of *La guerre sans haine* (German original *Krieg ohne Hass*),
notes presented by Liddell Hart, from *Revue de la France Libre* no. 56, March 1953.
Entry dated **1 June 1942**, as the brief specified. The passage reads: "Le lendemain la
garnison francaise devait recevoir le coup de grace. **Malheureusement pour nous, les
Francais n'attendirent pas.** En depit des mesures de securite que nous avions prises,
ils reussirent a quitter la forteresse." The script uses only the cleared form,
"Unfortunately for us, the French did not wait," which is an exact translation of the
marked sentence. The "seldom in Africa" line was cut rather than loosely paraphrased.
**PASS.**

**Rommel's two character-voice lines, checked separately for invented views:**

- **Act 4: "You cannot drive tanks through a minefield full of anti tank guns."** Rommel's
  own words in the same document: "Kesselring exigea le declenchement immediat d'une
  offensive de grand style, appuyee par la totalite des forces blindees. Or, c'etait la
  une impossibilite ; **les chars ne pouvaient etre utilises dans les champs de mines
  truffes de points d'appui.**" The line compresses his stated reason accurately. The one
  liberty is glossing "points d'appui" (strongpoints) as "anti tank guns", and MC22
  independently establishes that those strongpoints were built around anti-tank guns of
  25, 47 and 75 mm. **Fair compression, invents nothing.**
- **Act 2: "Take the little fort in the corner. Should not take long."** Compresses the
  documented 27 May order handing Bir Hakeim to Ariete. Its tone is independently
  underwritten by MC22's own characterisation of the German expectation: "**La prise du
  reduit ne doit etre qu'une formalite rapidement accomplie**" ("the taking of the redoubt
  was to be no more than a formality quickly accomplished"). The dismissiveness is the
  ministry's reading of the German plan, not the writer's invention. **Fair compression.**

**Neither line invents a flaw, and the build note is right that he should be read
reasonable rather than villainous.** He is correct in both lines.

### Test 8. The Ariete attack. **The timing call was RIGHT. Four FAILs elsewhere in the act (F6, F8, F9, F12).**

- **The Italians opened the battle.** Verified: 27 May 1942, 132a Divisione corazzata
  Ariete. MC22 confirms the Italians made the attack and were repulsed. **PASS.**
- **The tanks lost.** Verified from three independent directions. **PASS.**
- **The prisoners.** MC22 verbatim: "quatre-vingt-onze prisonniers". Tier 1. Italian
  official history gives 76, which the script does not have to adopt. **PASS.**
- **The colonel.** Lt-Col Pasquale Prestisimone verified. The script says only "a colonel"
  and attempts no name, which also sidesteps a TTS hazard. **PASS.**
- **The tanks left behind.** 32 is the consensus across French, Italian and the
  Association de l'Artillerie; MC22's "une trentaine de chars" agrees. **PASS.**
- **THE 45-MINUTE CALL: the writer was right, but for the wrong reason.** The writer
  downgraded to "Under an hour" believing it rested on MC22's "En une heure". **It does
  not, and could not:** "en une heure" means completed in the space of an hour, and
  reading it as strictly less than an hour is a stretch. **"Under an hour" is rescued by a
  better source the writer did not use:** General Saint-Hillier, an eyewitness French
  general, writes "**elle dure moins d'une heure**" ("it lasts less than an hour"), and the
  Association de l'Artillerie times the action 09:30 to 10:15. So the statement is true,
  it is true under French Wikipedia's 45 minutes as well, and the downgrade was the right
  editorial call. **PASS, on different authority than the writer thought.**
- **The French casualties that morning.** Single-sourced and contradicted from the Italian
  side. **SOFTEN, S1.**
- **THE ARITHMETIC IS BROKEN.** This is **F6** and it is the most embarrassing kind of
  error for this channel, because a viewer does the subtraction in their head. The script
  says the division "went from over seventy tanks to thirty three" and then, in the very
  next beat, that "It left thirty two tanks behind". Seventy minus thirty two is about
  thirty eight, not thirty three. Worse, the 33 is a **garble at source**: Saint-Hillier
  writes "33 chars restent sur le terrain, les autres refluent en tirant" ("33 tanks remain
  on the ground, the others fall back firing"), so 33 is a count of **wrecks left behind**,
  not of survivors. French Wikipedia's "reduite a trente-trois chars" contradicts its own
  next sentence. **FAIL, fix supplied.**
- **Two further errors found in this act that were not on the test list:** the RAF beat
  states the wrong mechanism (**F12**) and the encirclement date is wrong (**F8**). Both
  detailed below.

### Test 9. The garrison composition, nine consecutive beats. **PASS. This is the strongest stretch in the episode.**

Every nationality, unit and number checked individually. The brief was right that this is
the best-sourced material and the easiest place to get a number subtly wrong, so I checked
the numbers hardest.

| Beat | Verdict |
|---|---|
| About 3,700 men | **PASS, Tier 1.** MC22 "plus de trois mille sept cents hommes"; annex 3,723 from the musee de l'Armee |
| Two thirds from the colonies and overseas | **PASS, Tier 1.** defense.gouv.fr/terre: "deux tiers sont issus des colonies et des outremers" |
| Two Legion battalions, nearly 300 Spanish Republicans | **PASS.** Battalions at Tier 1 (MC22). The ~300 is cited to Milza, Peschanski and Cuesta Bustillo, L'Harmattan 1994, **academic press**, and attaches to the 3rd battalion, which is one of the two named. The script's own log understates this as unsourced by any ministry; it is better sourced than the log claims, and the "nearly" matches the source's own hedge |
| Pacific battalion: French Polynesia, New Caledonia, New Hebrides | **PASS.** Unit at Tier 1 (MC22 "du bataillon du Pacifique"); the three territories corroborated |
| Oubangui Chari battalion, now the Central African Republic | **PASS, Tier 1.** MC22 "du 2e bataillon de marche de l'Oubangui". Territory correct |
| North African company, about 180 men | Unit at Tier 1 (MC22 "d'une compagnie nord-africaine"). The 180 and the nationalities are uncited French Wikipedia. **SOFTEN, S7** |
| The North African company's losses, 74 of ~180 | Uncited French Wikipedia: 10 killed, 47 missing, 17 wounded. **Internally consistent, arithmetic redone and correct at 74.** One wording issue: 74 is casualties, not deaths. **SOFTEN, S7** |
| German and central European antifascists | Not found in any Tier 1 source. Historically orthodox and circumstantially supported by Porch's order, which presupposes the category. **SOFTEN, S9** |
| A British anti aircraft battery | **PASS, Tier 1.** MC22: "La DCA est renforcee par une batterie anglaise." The script names no unit, which is fortunate, because the circulating "HAA" designation is wrong: it was Light AA with Bofors 40 mm, and MC22 independently lists "canons Bofors AA de 40 mm" among the position's weapons |
| Amilakvari, Georgian prince, commanding the Legion battalions | **PASS, Tier 1.** Ordre de la Liberation: "le Prince Dimitri Amilakvari", born Gori 12 Nov 1906, given the 13e DBLE 16 Sept 1941 |
| Oubangui Chari brought out 60 percent (Act 6 payoff) | **PASS, and the best-sourced casualty claim in the episode.** It comes from the battalion's citation a l'ordre de l'Armee signed by de Gaulle: "a ramener 60 % de ses effectifs". A primary document |

**The three reuses that return in Act 6 when the losses are read are doing real work**
and are the reason the roster earns nine beats. Verified: scenes 86, 87 and 93 return to
21, 22 and 23.

### Test 10. The Churchill "Fighting French" renaming. **FAIL. Wrong actor.**

The writer flagged this as the one beat resting on the research report's assertion rather
than a named source, and asked for an independent citation or a cut. I verified it
independently and it is worse than unsourced: **it is wrong.**

- The renaming of "la France libre" to "**la France combattante**" was decided by the
  **Comite national francais**, de Gaulle's own body, on **13 July 1942**, to mark the
  union of the external Free French with the internal Resistance.
- French Wikipedia's "France libre" article carries the decision, the date and the
  defining formula, and **no mention of Churchill or of the British government appears
  anywhere in connection with it.**
- Every general reference source I checked attributes the change to de Gaulle.
- Nothing connects it causally to Bir Hakeim at Tier 1. The claimed link appears only on
  low-tier French battle-summary pages.

The script asserts it flatly and then adds "**That part is real**", which is the strongest
possible verification claim an episode can make. On a channel whose entire brand is
accuracy, asserting a false attribution and then vouching for it is the worst single line
in the script. **The writer's instinct was correct and the cut is available. See F1 for
both options.**

### Test 11. Every Tier 2 single-sourced claim, and whether the log is honest about itself. **MIXED. The log is mostly honest, with three material misstatements.**

I audited the log's self-assessment row by row for the rows it self-declares.

| Row | Log says | What I found | Honest? |
|---|---|---|---|
| **620 Indian soldiers** | "Tier 2, single-sourced. French Wikipedia's Bilan section, **footnoted** but not corroborated" | The French Wikipedia sentence is **uncited**, not footnoted. English Wikipedia carries a fuller version (3rd Indian Motor Brigade, 30 May, plus 243 prisoners already present) citing Liardet, who is also French Wikipedia's external link, so it is probably one origin either way | **Overstated.** "Single-sourced" is right, "footnoted" is not. Also, they arrived 30 May and left with the convoy on 31 May, so the script's Act 4 placement implies a later date than the record supports. **SOFTEN, S6** |
| **42-Stuka raid, 17 wounded killed** | "Tier 2, single-sourced. This is the episode's hardest casualty beat and it rests on one source. It is played completely straight and no figure around it is embellished" | Honest about the tiering, and **wrong about the numbers surviving scrutiny.** See below | **Honest in framing, but the beat fails on the facts. FAIL, F3** |
| **170 litres of water** | "The narration now says 'Nearly all for the wounded,' which matches the source's 'almost entirely' **exactly**" | The source says "**surtout**", not "presque entierement". The claimed source wording does not exist | **Materially wrong. FAIL, F7. See test 12** |
| **The 88 gun beat** | "Attributed on screen, correctly. French Wikipedia quoting General Saint-Hillier, a 1re DFL veteran. The narration says 'That comes from a French general who was there,' which is exactly what it is and no more" | Confirmed. Saint-Hillier is a real, named, credentialed eyewitness and the narration claims precisely his authority and nothing beyond it | **Honest, and the model for how the rest should be handled** |
| **Ammunition, 200 shells and 700 mortar bombs** | "Verified. Tier 1.5 and Tier 2 agreeing. FSALE and French Wikipedia" | **Both claims are false.** I fetched the FSALE page myself: it contains no ammunition figures at all. French Wikipedia does not carry the 200/700 pairing. The nearest real figure inverts the meaning | **Dishonest, though probably by accident. FAIL, F2** |

**The 42-Stuka beat, scrutinised hardest as instructed.** Three separate problems:

1. **"Forty two Stukas" is uncited on French Wikipedia and contradicted** by the British
   official history (Playfair), which gives 45 Stukas plus three Ju 88s and ten Bf 110s
   under a 54-fighter escort on 8 June, and a further 60 Stukas that afternoon. There is
   also a tell that the number has migrated between sentences: French Wikipedia elsewhere
   uses "42" for aircraft **shot down across the whole battle**.
2. **"One bomb" is a fabricated specific.** No source says one bomb. The only detailed
   account, Guy Chauliac's *Le service de sante de la France Libre 1940 a 1943*, says
   **two**: "**Une bombe ecrase les camions operatoires, une autre tombe sur l'abri des
   grands blesses qui sont tous tues**" ("One bomb crushes the operating trucks, another
   falls on the shelter of the seriously wounded, who are all killed").
3. **"Seventeen" is a single-sourced casualty figure asserted flatly**, which the brief
   names as an automatic FAIL. Chauliac, the one genuinely independent source, gives a
   different figure on a different date: "par recoupement, il apparait que **15 blesses au
   moins et 3 infirmiers** ont disparu" ("cross-checking, it appears at least 15 wounded and
   3 orderlies were lost"), on 9 June.

**The good news, and the writer should hear it:** the **substance** of the beat is
corroborated by two independent sources. The aid post was hit and the seriously wounded
inside it were killed. Only the numbers are bad. **The replacement I supply uses Chauliac's
own account, which is better sourced and lands harder than the version it replaces.**

### Test 12. The Manager's water fix. **FAIL. The fix was applied to a source wording that does not exist.**

- **Word count and cap: correct.** The beat is exactly **14 words**, at the cap, verified
  by counter. "It went to the wounded" and "Nearly all for the wounded" are both five
  words, so the edit was genuinely word-count neutral, as claimed.
- **Accuracy to the source: incorrect.** French Wikipedia reads "La RAF arrivera a fournir
  un ravitaillement aerien de 170 litres en eau **qui servira surtout pour les blesses**".
  "Surtout" means **above all, mainly, especially**. It does not mean almost entirely. I
  checked specifically for "presque entierement" and "en quasi-totalite" and **neither
  phrase appears in the article.** The "almost entirely" wording the fix was written to
  match is not in the source.
- **So both the old and the new wording overstate, in the same direction.** "It went to
  the wounded" implies all of it; "Nearly all" implies almost all of it; the source says
  mainly. The fix moved the line sideways, not toward the source.
- **Fix supplied at F7, word-count neutral at 14, and accurate to "surtout".**
- Separately: the **170 litres figure itself is uncited** on French Wikipedia and I found
  it nowhere else. It is not a casualty figure, so it is not blocking, but it belongs on
  the soften list alongside the other uncited volume figures.

---

## Issues to fix

Format: **[exact claim as spoken]** then what is wrong, then the exact replacement.
Word deltas are given against the current beat. Every replacement below was counted with
the same script used for the structural checks, and **none exceeds the 14-word cap.**

### FAIL items, all blocking

**F1. "And Churchill renamed the Free French the Fighting French. That part is real."** (Act 7, final beat, 13 words)
Wrong actor, asserted flatly and then explicitly vouched for. The renaming to "la France
combattante" was decided by the **Comite national francais on 13 July 1942**, not by
Churchill, and no source connects Churchill or the British government to it.
- **Option A, recommended. CUT THE BEAT** and its VISUAL tag. Act 7 then ends on "Almost
  everything English about Susan Travers traces back to one book she co wrote," which is
  the English-overclaim punchline and a cleaner act ending than the Churchill line was.
  **Delta: minus 13 words. Also removes one VISUAL tag, taking the count to 111 and unique
  generations to 100.**
- **Option B, if a closing beat is wanted:** `And that July the Free French renamed themselves the Fighting French.`
  **Delta: minus 2 words (11).** Accurate on actor and date. **Caveat: do not follow it with
  any line implying Bir Hakeim caused it**, because that causal link is not Tier 1.
- **Option A is the better episode.** The Churchill name added nothing the act needed, and
  Option B ends the act on an administrative detail rather than on the argument.

**F2. "Tenth of June. About two hundred shells left. Seven hundred mortar bombs."** (Act 4, 12 words)
Untraceable. I fetched the FSALE page myself and it contains no ammunition figures; French
Wikipedia does not carry the pairing. The nearest real figure **inverts the meaning**: the
Association de l'Artillerie gives, for 9 June, "il ne reste plus que 150 a 200 coups **par
piece de 75**", which is 150 to 200 rounds **per gun** across dozens of guns, that is
thousands of rounds, not two hundred. "Seven hundred mortar bombs" appears nowhere.
- **Replacement:** `Tenth of June. Seven working guns left, and almost no ammunition anywhere.`
- **Delta: 0 (12 words).** Rests on the Association de l'Artillerie's 10 June state of the
  guns and on the English official-history detail that the last rounds were issued and
  bodies searched for more.

**F3. The Stuka aid-post beats.** (Act 4, two consecutive beats)
Detailed in test 11. Uncited and contradicted aircraft count, one fabricated specific, and
a single-sourced casualty figure asserted flatly.
- **Beat A, currently "Eighth of June. Forty two Stukas. One bomb hit the brigade aid post."** (13 words)
  **Replacement:** `Eighth of June. The heaviest raids yet. Bombs hit the brigade aid post.`
  **Delta: 0 (13 words).**
- **Beat B, currently "Seventeen men who were already wounded were killed there."** (9 words)
  **Replacement:** `One fell on the shelter of the worst wounded. All were killed.`
  **Delta: plus 3 words (12).** This is Chauliac translated closely and it is a **harder**
  beat than the one it replaces, not a softer one. It also justifies the plural "Bombs" in
  beat A.

**F4. "Some accounts say around nine hundred, because they count the missing differently."** (Act 6, 12 words)
The variation is real; the stated mechanism is invented and the arithmetic refuses it. See
test 3.
- **Replacement:** `Other official French figures say around nine hundred. Nobody has reconciled them.`
- **Delta: 0 (12 words).** States the disagreement without inventing a cause, which is also
  more on-brand for this channel than a false tidy explanation.

**F5. "Susan Travers. Born in Kensington, London, nineteen oh nine. Semi professional tennis player."** (Act 3, 13 words)
"Semi professional" is unsourced. French Wikipedia carries it with no citation; it is absent
from *Esprit defense*, from the France-Soir 1996 profile and from the reference works. Holden's
own BBC piece says only "tennis-playing socialite".
- **Replacement:** `Susan Travers. Born in Kensington, London, nineteen oh nine. A tennis playing socialite.`
- **Delta: 0 (13 words).** Uses the source's own phrase, and it is a better joke.

**F6. "Under an hour. The division went from over seventy tanks to thirty three."** (Act 2, 13 words)
Bad on-screen arithmetic (seventy minus the thirty two of the next beat is thirty eight, not
thirty three) and the 33 is a garble at source: Saint-Hillier's "33 chars restent sur le
terrain" counts **wrecks left behind**, not survivors. Note "Under an hour" itself is fine and
stays. See test 8.
- **Replacement:** `Under an hour. The Italians lost about half their tanks that morning.`
- **Delta: minus 1 word (12).** "About half" is true under every source: 32 lost from a force
  the French put at ~70 and the Italian official history at 60 to 62. Keeps the comic
  arithmetic and removes the collision.
- The preceding beat, "Which left seventy odd tanks charging a minefield entirely on their
  own," **can stay as written** once the 33 is gone, because seventy is the French estimate
  and it no longer contradicts anything downstream.

**F7. "The RAF air dropped a hundred and seventy litres. Nearly all for the wounded."** (Act 4, 14 words)
The source says "surtout" (mainly), not "almost entirely". See test 12.
- **Replacement:** `The RAF air dropped a hundred and seventy litres. Mostly for the wounded men.`
- **Delta: 0 (14 words, still exactly at the cap).**

**F8. "By the second of June the ring closed. And somebody had come back in."** (Act 2, final beat, 14 words)
MC22 says the investment **began** on 2 June ("L'investissement de la place commence le 2
juin"); full encirclement was not complete until 6 June.
- **Replacement:** `By the second of June the siege began. And somebody had come back in.`
- **Delta: 0 (14 words).** Preserves the hook exactly.
- **Also fix the VISUAL on this beat, no word cost.** It currently reads "closing a ring from
  the east". The German troops came from the **south** and the Italians from the **north**;
  nothing supports "from the east". Replace the tag with:
  `**[VISUAL: A map with a German division closing from the south and an Italian division from the north.]**`

**F9. "A crew under Sergeant Walter Grand destroyed all six at point blank range."** (Act 2, 13 words)
An unconfirmed name asserted in narration. "Walter Grand" appears only in French Wikipedia;
his own French Wikipedia biography is unsourced, undated, and describes him knocking out
**German** Panzers, not Italian tanks. Saint-Hillier, the Tier 1 eyewitness, does not name him
and credits different units. The six tanks and the point-blank destruction are independently
verified and stay.
- **Replacement:** `A French gun crew destroyed all six of them at point blank range.`
- **Delta: 0 (13 words).**

**F10. "One went blind. A hundred and eighteen died when their prison ship was torpedoed."** (Act 6, 14 words)
A single-sourced casualty figure asserted flatly, and **contradicted**: Fondation de la France
Libre material gives 143 French missing in the Nino Bixio sinking, against French Wikipedia's
118. An unresolved conflict presented as settled, on a death toll.
- **Replacement:** `One went blind. More than a hundred died when their prison ship was torpedoed.`
- **Delta: 0 (14 words).** True under both figures, still devastating, and it stops the episode
  asserting a contested number on a mass death.

**F11. "And Rommel's panzers were mostly not there. A few dozen German tanks."** (Act 7, 12 words)
The first sentence quotes Rondeau correctly. The second lifts "quelques dizaines de chars
allemands **en plus a El Alamein**" out of a **counterfactual about El Alamein** and turns it
into a headcount of the German armour at Bir Hakeim. He did not say that. See test 4.
- **Replacement:** `And Rommel's panzers were mostly not there. They arrived at the end.`
- **Delta: 0 (12 words).** Accurate to Rommel's own diary, which has 90th Light and Trieste
  carrying the siege, an Afrikakorps shock group under Baade only on 10 June and 15th Panzer
  ordered up after that. It also strengthens the act, because "they arrived at the end" is a
  sharper point than a vague quantity.

**F12. "Then the RAF started bombing the wrecked Italian tanks. Over and over."** (Act 2, 12 words)
Wrong mechanism, and the true version is both more accurate and funnier. The RAF was not
bombing dead tanks as a nuisance; it was **bombing Bir Hakeim itself**, misled by the Italian
wrecks around the position into taking it for a target. That is why Koenig burned them.
- **Replacement:** `Then the RAF started bombing Bir Hakeim, misled by the Italian wrecks.`
- **Delta: 0 (12 words).**
- **The following beat, "So Koenig sent men out to burn the wrecks so their allies would stop,"
  needs no change** and finally makes sense once beat A is corrected.

**F13. "Rommel attacked an empty fortress that morning. He counted twelve hundred fighting positions."** (Act 5, 13 words)
Two problems. The position was not empty: wounded and stragglers were still firing. And
**Rommel is not the source of the 1,200**: French Wikipedia states it as a fact about the
fortification works ("Les travaux de fortification autour de Bir Hakeim comprenaient, entre
autres, 1 200 emplacements de combat"), not as something Rommel counted. The Rommel extract I
read at the Fondation de la France Libre does not contain the figure at all. "He counted" is a
fabricated attribution.
- **Replacement:** `Rommel walked into a position that was already gone. Twelve hundred fighting positions.`
- **Delta: 0 (13 words).** Fixes both problems and keeps the number, which is real.

**F14. "A historian of the Afrika Korps calls that ridiculous and without foundation."** (Act 7, 12 words)
Rondeau's "ridicule et sans fondements" attaches to the El Alamein claim specifically, not to
the bundled pair in the preceding beat. See test 4.
- **Replacement, recommended:** `A historian of the Afrika Korps calls the El Alamein part ridiculous.`
  **Delta: 0 (12 words).**
- **Alternative if both adjectives are wanted:** `A historian of the Afrika Korps calls the El Alamein claim ridiculous and baseless.`
  **Delta: plus 2 words (14, at the cap).**

**Net effect of all fourteen FAIL fixes, taking F1 Option A and F14 recommended: minus 11
words. Narration goes 1,406 to 1,395, inside the 1,390 to 1,410 window.** VISUAL tags go 112
to 111, reuse stays at 11, unique generations 101 to 100.

**If the Manager wants the word count nearer the middle of the window**, the writer's own
noted candidate for restoration is available and now verified: the **3 June ultimatum was
Rommel's own handwritten note, and the French reply was a salvo from the 1st Artillery
Regiment**. That is real, well cited and would slot into Act 4 as a two-beat exchange.

### SOFTEN items, non-blocking, recommended

These are thin rather than wrong. None is a blocker on its own. All replacements are inside
the cap.

**S1. "French losses that morning. Two men wounded, one truck, one gun."** (Act 2, 11 words)
Uncited French Wikipedia only, absent from MC22, Saint-Hillier and the artillery study, and
Italian sources say the opposite ("nessuna perdita da parte francese"). It is the punchline of
Act 2, so hedging it rather than cutting it is right.
- **Replacement:** `By the French count that morning. Two men wounded, one truck, one gun.` **Delta: plus 2 (13).**

**S2. "Two hundred trucks waited fifteen kilometres away. They only had to reach them."** (Act 5, 13 words)
Those are the numbers in **Koenig's order**, not in the event. Saint-Hillier says 100 trucks of
the 101e compagnie du train; Pitt says 7 km; MC22 says only "quelques kilometres plus loin".
- **Replacement:** `The order promised trucks fifteen kilometres away. They only had to reach them.` **Delta: 0 (13).**

**S3. "By eight in the morning the bulk of the brigade had reached the British."** (Act 5, 14 words)
Three-way conflict: 07:00 (Playfair), 07:30 (Saint-Hillier), 08:00 (French Wikipedia).
- **Replacement:** `By that morning the bulk of the brigade had reached the British lines.` **Delta: minus 1 (13).** True under all three.

**S4. "Her car came out riddled with bullets. She said she counted eleven."** (Cold open, 12 words)
One origin (Holden, twice), contested by a competing count of roughly twenty, and it is the
one number in the episode that Act 7's own thesis is about. See test 5.
- **Replacement:** `Her car came out riddled with bullets. One account says eleven holes.` **Delta: 0 (12).**

**S5. "Forty thousand heavy shells came in. The French fired forty two thousand back."** (Act 4, 13 words)
Both figures are uncited on French Wikipedia and found nowhere else, and the 40,000 covers 2 to
10 June only.
- **Replacement:** `By one count, forty thousand heavy shells came in. Forty two thousand back.` **Delta: 0 (13).**

**S6. "Six hundred and twenty abandoned Indian prisoners walked in. The garrison took them in."** (Act 4, 14 words)
They were soldiers of the 3rd Indian Motor Brigade who had been captured and abandoned, and
"prisoners" reads as if they were the garrison's prisoners.
- **Replacement:** `Six hundred and twenty abandoned Indian soldiers walked in. The garrison took them in.` **Delta: 0 (14).**
- **Chronology note, no fix required:** they arrived 30 May and left with the convoy on 31 May.
  The script speaks no date, so nothing is false, but the Act 4 placement implies later.

**S7. "The North African company lost seventy four men out of roughly one hundred eighty."** (Act 6, 14 words)
The 74 is 10 killed, 47 missing and 17 wounded. "Lost" is standard casualty usage but in an act
about the dead it will be heard as 74 killed.
- **Replacement:** `The North African company had seventy four casualties out of roughly one hundred eighty.` **Delta: 0 (14).**

**S8. "So they made their own cover. Trenches cut a metre into solid rock."** (Act 1, 13 words)
The source's one metre attaches to **abris** (shelters), not to trenches; MC22 confirms the
earthworks but gives no dimension.
- **Replacement:** `So they made their own cover. Cut a metre down into solid rock.` **Delta: 0 (13).**

**S9. "German and central European antifascists and refugees, wearing French uniforms."** (Act 1, 10 words)
Not documented at Tier 1. The one thing that **is** documented is the refugee status, because
Porch's Hitler order presupposes exactly that category.
- **Replacement:** `German and central European refugees from Hitler, wearing French uniforms.` **Delta: 0 (10).**
  This also sets up the Act 6 Hitler beat more tightly.

**S10. "A researcher at the French defence archives says she also became his mistress."** (Act 3, 13 words)
*Esprit defense* states it in the **article's own voice** ("Elle deviendra aussi sa maitresse").
Letang is quoted immediately after treating the relationship as real, but he does not utter the
attributed sentence.
- **Replacement:** `The French defence ministry's own magazine says she also became his mistress.` **Delta: minus 1 (12).** Stronger attribution, and accurate.

**S11. "The driver destroyed the gun anyway. Two more officers died on foot, throwing grenades."** (Act 5, 14 words)
The two deaths are confirmed by three sources. The on-foot-with-grenades manner is French
Wikipedia only, and FSALE gives a different account of de Lamaze's death.
- **Replacement:** `The driver destroyed the gun anyway. Two more officers died in the lane.` **Delta: minus 1 (13).**

**S12. "Three years later she became the only woman ever enrolled in the Foreign Legion."** (Cold open, 14 words)
Every Tier 1 source says "**premiere**" (first), not "seule" (only). "Only" is a well-supported
inference, but the cold open asserts the inference while the outro states the sourced form.
- **Replacement for the cold open only:** `Three years later she became the first woman ever enrolled in the Foreign Legion.` **Delta: 0 (14).**
- **Leave the outro exactly as written.** "She is still the only woman ever formally enrolled in
  the Foreign Legion" is the research report's safe formulation and the "still" carries the
  inference honestly. The pair then reads first in the hook, still the only in the payoff, which
  is a better arc than two identical claims.

**Net effect of all twelve SOFTEN fixes: minus 1 word. Applied on top of the FAIL fixes, the
narration lands at 1,394**, inside the window.

---

## Cold read notes

Read start to finish at pace, as a listener hears it, checking for anything a TTS will
mangle and anything the ear will mis-parse.

**TTS safety: clean.** Zero non-ASCII characters anywhere in a spoken line, verified
mechanically. No accented character, no French construction left in the read, no digits, no
hyphens, no brackets or stage directions inside any `**NARRATOR:**` or `(character voice)`
line. Every number is spelled out. The pronunciation guide in the voice note covers the five
risk words (Koenig, Amilakvari, Oubangui Chari, Bir Hakeim, adjudant chef) and each is
spelled in a form an English TTS will attempt sensibly even without the guide.

**Names that will still need a listen on the VO pass:**
- **"Bersaglieri"** appears once and is the hardest word in the script. Not in the voice note.
  Add it: ber-sal-YAIR-ee.
- **"Ariete"** appears once. Add it: ar-YEH-teh.
- **"la Miss"** may be read as "la miss" with a French article and an English noun in one
  breath, which is correct but will sound like a stumble unless the VO is told it is
  deliberate.
- **"Kesselring"** and **"Gazala"** are fine.
- **"Prestisimone" is correctly absent.** The script says "a colonel", which is both safer
  historically and safer phonetically.

**Ear-parse hazards found: two, both minor and both now fixed by other items.**
- The old Act 2 arithmetic ("over seventy ... to thirty three ... left thirty two behind")
  made the ear stumble because the listener starts subtracting. F6 removes it.
- "Forty two Stukas" followed two beats later by "An eighty eight" put two bare numbers in
  close succession in different roles, one a count of aircraft and one a gun calibre. F3
  removes the first, which incidentally fixes this.

**Sequence check on the central correction:** done in full at test 1. Nothing in the running
order lets a listener carry the Legion status backwards into the desert.

**Register on a continuous read:** the drop at Act 5 is audible and holds. The one place the
read could go wrong is the last line of Act 6, "Depends who you ask," which follows an order
to kill prisoners with no buffer beat. It is not adjacent to a casualty figure, so it passes,
but it must be read tired rather than arch. Flagged for the VO pass in the tone check above.

**Length:** at the measured 158 wpm, 1,395 words after the FAIL fixes is **8:50**, comfortably
clear of the 8:00 mid-roll floor. At the fast end of the observed range, 173 wpm, it is
**8:04**, still clear. The fixes do not endanger the mid-roll.

---

## Summary

**Structural: clean.** Word count, beat cap, VISUAL count, reuse targets, camera moves,
dashes, sections, hooks and TTS safety all pass, verified by script rather than by eye.

**Tone: clean.** The comedy is where the writer says it is, the front half is genuinely funny,
Acts 5 and 6 are straight, and the single Act 6 joke is four beats clear of the nearest
casualty figure. No joke sits on or beside a human-cost beat.

**The four corrections the episode was built to make all hold**, and two of them (the Legion
status and the evacuation order) hold very strongly. The ministry's three-part modest claim,
which is the spine of Act 7, is quoted exactly right. The Rommel quote has real provenance.
The Hitler order appears only in its documented narrow form.

**But fourteen claims fail.** One is a false attribution asserted as verified (F1). One rests
on numbers that exist in no source and whose nearest real figure means the opposite (F2). One
puts a fabricated specific and a contradicted single-sourced casualty figure on the episode's
hardest beat (F3). One invents a causal explanation that the arithmetic refuses (F4). One
misappropriates a historian's counterfactual as a headcount, in the act that is the episode's
spine (F11). Two more misrepresent the scope of a historian's rebuttal and the mechanism of an
RAF incident (F14, F12). The rest are an unsourced biographical detail, an unconfirmed name,
broken on-screen arithmetic, a wrong date, a fabricated attribution to Rommel, a contested
death toll asserted as settled, and a Manager fix written to match a source wording that does
not exist (F5, F9, F6, F8, F13, F10, F7).

**Every one has an exact replacement above.** Applied together they cost 11 narration words and
one VISUAL tag, landing at 1,395 words and 111 tags, both inside spec. Three of the fixes (F3,
F11, F12) make the episode better, not merely safer: Chauliac's account of the aid post is
harder than the version it replaces, "they arrived at the end" is a sharper point than "a few
dozen German tanks", and the RAF bombing Bir Hakeim by mistake is a funnier and truer joke than
the RAF bombing dead tanks.

**This is a strong script with a weak fact-check log.** The narration's hedging discipline is
genuinely good, and where the writer said a thing was attributed on screen, it almost always
was. The failures cluster in the log's own verification claims, not in the writer's judgement
about how to speak a hedge. Two log rows assert corroboration that does not exist (F2's "FSALE
and French Wikipedia agreeing", F7's "matches the source's 'almost entirely' exactly"). That is
the pattern to watch on the next episode.

**Re-QA required after the fixes are applied (loop 2 below).** I want to re-run the structural script and
re-read Act 2, Act 4 and Act 7 in sequence once the replacements are in, because F1 removes a
beat, F3 changes a beat length, and F6, F8 and F12 all land in the same act.

---
---

# RE-GATE, loop 2 of 2, 2026-09-02

Scope: verify the 26 fixes landed, hunt collateral damage in the three acts that took
multiple edits, re-audit the fact-check log against real sources, re-run the structural
script, and verify the re-timing. Nothing already passed in loop 1 was re-verified.

## Structural re-run, independently measured

| Check | Requirement | Writer reports | I measure | Result |
|---|---|---|---|---|
| Narration words | 1,390 to 1,410 | 1,394 | **1,394** | PASS |
| Spoken beats | n/a | n/a | 111 | |
| Longest beat | max 14 | 0 over | **max 14, zero over** | PASS |
| Shortest beat | no punch fragments | n/a | 8, Rommel's cleared quote | PASS |
| `[VISUAL:]` tags | n/a | 111 | **111** | PASS |
| Reuses | backwards, matching | 11, byte-identical | **11, all backwards, all byte-identical** | PASS |
| Unique generations | n/a | 100 | **100** | PASS |
| Camera moves | none | none | **none** | PASS |
| Em-dashes and en-dashes | zero | zero | **zero** (U+2012 through U+2015 and U+2212 all absent) | PASS |
| Sections | nine, in order | n/a | **nine, in order** | PASS |
| Brackets in spoken lines | none | n/a | **none** | PASS |
| Non-ASCII in spoken lines | none | n/a | **none** | PASS |
| Digits in spoken lines | none | n/a | **none** | PASS |

**Reuse renumbering handled correctly.** Dropping the Churchill tag shifted the last two
reuses from 106 and 107 to **105 and 106**. Both still resolve backwards to 8 and 9 and
both are byte-identical to their targets. The production notes table was updated to match,
which I checked line by line. This is the single most likely place a beat-removal breaks a
build and it did not break.

**All 26 replacements landed verbatim.** I string-matched every one of the 14 F items and
12 S items against the body. All 26 present, exact. I also swept for all 25 superseded
wordings ("Forty two Stukas", "Walter Grand", "the ring closed", "Nearly all for the
wounded", "A few dozen German tanks", and the rest): **zero stale wordings remain.**

**F1, the cut, is clean.** "Churchill" and "Fighting French" appear nowhere in any spoken
beat or any VISUAL tag. The four surviving mentions are all in documentation, the accuracy
note, the production notes, the deliberately-not-in-the-episode list and the fact-check log
row, where they belong as a record of why the beat is gone.

## Re-timing, verified independently

| Rate | Runtime | Margin over the 8:00 mid-roll floor |
|---|---|---|
| 158 wpm (measured) | 1394/158 = 8.8228 min = **8:49** | 49 s |
| 173 wpm (observed fast end) | 1394/173 = 8.0578 min = **8:03** | **3.5 s** |

**The writer's arithmetic is correct at both ends.** But state the exposure plainly: the
break-even rate is **1394/8 = 174.25 wpm**, so the episode drops under the mid-roll floor
if the VO comes in above 174.25. Against an observed fast end of 173 that is a margin of
**1.25 wpm, about 0.7 percent**. It holds, and it held before the fixes too, but it is thin
enough that the VO pass should be told not to rush.

**My two conditions below are deliberately word-count neutral so they do not erode this.**
If the Manager wants real headroom, the previously verified and currently unused **Rommel
handwritten ultimatum of 3 June** (his own handwritten note, answered by a salvo from the
1st Artillery Regiment) would add roughly 13 words, taking the fast end to about **8:08**
and the total to 1,407, still inside the window.

## Collateral damage sweep

I read Acts 2, 4, 5 and 7 straight through at pace. Two real breaks, both introduced by my
own loop-1 replacements, both one line and both neutral.

### Act 2, five edits landed (F6, F8, F9, F12, S1)

**The arithmetic is fixed and now reconciles on screen.** "seventy odd tanks" then "lost
about half their tanks" then "left thirty two tanks behind": 32 of about 70 is 46 percent,
which is about half. A viewer who subtracts now gets the right answer. The loop-1 collision
is gone.

**F12 works and is the best change in the batch.** "Then the RAF started bombing Bir Hakeim,
misled by the Italian wrecks" followed by "So Koenig sent men out to burn the wrecks so
their allies would stop" is now a joke with a mechanism. In the first draft the second beat
did not follow from the first.

**COLLATERAL 1, condition C1. F6 broke a pronoun and duplicated a phrase.** The replacement
beat ends "The Italians lost about half their tanks that morning," and the very next
unchanged beat begins "**It** left thirty two tanks behind." In the first draft that "It"
pointed at "The division". My replacement swapped in the plural "The Italians", so "It" is
now dangling with no singular antecedent nearer than "morning". Separately, "that morning"
now appears in that beat **and** two beats later in S1's "By the French count that morning."
My fix caused both. One replacement clears both.

### Act 4, five edits landed (F2, F3, F7, S5, S6)

**F3 works exactly as designed.** The plural "Bombs hit the brigade aid post" correctly sets
up "**One** fell on the shelter of the worst wounded. All were killed." The antecedent chain
is clean, and the beat is harder than the numbered version it replaced.

**F2 improved its own hook.** "Seven working guns left, and almost no ammunition anywhere"
followed by "The Germans decided to finish the job the next morning. They did not know" is
a better payoff than the old shell count, because seven guns is a more vivid thing for the
Germans not to know.

**COLLATERAL 2, condition C2. S5 collided with the beat after it.** S5 opens "**By one
count,** forty thousand heavy shells came in," and the immediately following unchanged beat
opens "**By Rommel's own count** the Luftwaffe flew thirteen hundred attacks." Two
consecutive beats opening with the same hedging construction. This is precisely the
"softens compound into mush" failure the brief asked me to watch for, and it is the only
instance of it in the episode. Moving my hedge to the end of its beat clears it and reads
better, because the beat then opens on the number.

### Act 5, four edits landed (S2, S3, S11, F13)

Clean. **S2's "The order promised trucks fifteen kilometres away" reads as deliberate
anaphora**, not an echo, because the beat before it is "Koenig's order that evening", so
"The order" correctly points back. **S11's "died in the lane" is better than the wording it
replaced**, because it ties the deaths to the act's own title image. The consecutive "By her
own account" and "By that morning" is a pre-existing pattern, not collateral: the first
draft had "By her own account" and "By eight in the morning" in the same two slots.

### Act 7, two edits landed plus the F1 cut

**F14's scope is now exactly right.** Rondeau's "une assertion ridicule et sans fondements"
attaches to one proposition, which he states outright: "Cette resistance prolongee n'a
nullement permis le retablissement britannique sur El Alamein." The beat now says "calls
**the El Alamein part** ridiculous". That is his claim and only his claim.

**And it made the act structurally better, which I did not anticipate.** The act now runs:
France bundles two claims, the specialist demolishes the El Alamein half, the timeline and
the panzers then deal with the Eighth Army half on the evidence, and the ministry's own
modest three-part claim calibrates what is left. In the first draft the specialist appeared
to demolish both halves and then the act half-endorsed one of them four beats later via
"let the British pull back". That soft contradiction is gone.

**F11 is true and carries more than the line it replaced.** "They arrived at the end" is
verified from Rommel's own diary: 90th Light and Trieste carried the siege, an Afrikakorps
shock group under Colonel Baade was committed on **10 June**, and 15th Panzer was ordered up
after that. The breakout was the night of 10 to 11 June, so the German armour arrived on the
final day. The old line was a misappropriated counterfactual with no headcount behind it;
the new line is sourced to Rommel and makes a sharper point.

**The new Act 7 ending works, as an ending and as the argument.** Act 7 now closes on
"Almost everything English about Susan Travers traces back to one book she co wrote." The
act is titled "WHAT IT DID NOT DO" and its argument is that both national tellings are
inflated, each by its own mechanism: the French by forgetting the allies, the English by
having one source. Ending on the English mechanism completes the symmetry. The Churchill
beat was an appendix that added a fact after the argument had finished.

**The handoff into the outro is better than it was.** Act 7 ends by saying everything you
have heard about her comes from one book; the outro opens "June nineteen forty five" and
delivers the one part of her story that sits in a state archive. That adjacency is a genuine
payoff and the Churchill beat was sitting in the middle of it. It is less of a curiosity
hook than the other act endings, but Act 7 is the last act before the payoff and a
deflating turn is the right shape there.

## Do the twelve softens compound into mush?

**No, with the single exception at C2.** I counted every hedged construction in the finished
script: eleven attributed or hedged beats across 111, about one in ten, and six of those
eleven were already in the first draft ("By Rommel's own count", "That comes from a French
general who was there", "By her own account", "France says", "The French defence ministry
itself claims", "A defence archives researcher says"). The twelve softens added five net
hedges spread across seven acts. That is not a mush density.

**Every hedge is doing work.** I checked each against the question "if this were deleted,
would the line assert something the sources do not support?" All eleven pass. The two I
looked at hardest:

- **S2, "The order promised trucks"** carries a faint suggestion the trucks might not have
  been there, which is not warranted since the brigade reached them. But it is doing real
  work: it drops the disputed "two hundred" and correctly attributes the fifteen kilometres
  to Koenig's written order rather than to the event. **Keep.**
- **S1, "By the French count that morning"** adds a small throat-clear before Act 2's
  punchline. The joke is the absurd asymmetry and it survives intact. Given the figure is
  uncited at source and contradicted from the Italian side, the hedge is earning its cost.
  **Keep.**

**Comedy did not degrade.** Act 2 still carries eleven comic beats. F6 slightly softened the
arithmetic gag by trading a hard number for "about half", but beats 9 and 10 carry the
sequence and F12 added a better joke than the one it replaced. The front half is unchanged
in length, so density is unchanged.

**Tone re-checked after F10 touched Act 6.** The single Act 6 joke still sits four beats
after the last casualty figure and five after the last French death, with the retracted
Berlin threat and the ignored Hitler order in between. Unchanged from loop 1. **Passes.**

## The cold open and outro pairing, S4 with S12

**Consistent, and improved.** The cold open now says she became "the **first** woman ever
enrolled in the Foreign Legion" and the outro says "She is **still the only** woman ever
formally enrolled." First in the hook, still the only in the payoff. There is no
contradiction, "first" is the exact Tier 1 wording, and the pair now escalates across the
episode instead of repeating a claim.

**S4 produced an unplanned payoff.** The cold open now says "**One account** says eleven
holes," and Act 7 later says "almost everything English about Susan Travers traces back to
**one book** she co wrote." The hook now quietly plants the thinness that Act 7 pays off.
In the first draft the cold open borrowed a number from exactly the book Act 7 goes on to
discredit, without saying so.

## The three undirected VISUAL edits

**All three are correct and the reasoning behind them is right.** A VISUAL tag is a build
instruction. Leaving a ruled-unsupported specific inside one would send a QA-failed claim
straight into an image generator and out onto the screen, where it would be exactly as
public as the narration. Fixing the tag alongside the line is the correct instinct and I
should have specified it myself in loop 1.

| Edit | Verdict |
|---|---|
| F3: "Forty two dive bombers" to "Dive bombers" | **Correct.** The 42 is uncited and contradicted by Playfair. Verified the tag now reads "Dive bombers turning above a marked medical position with a red cross," and that no other tag carries the number |
| S6: "Six hundred prisoners" to "Six hundred soldiers" | **Correct**, and it fixes a real ambiguity: they were the Axis's prisoners, not the garrison's, so "prisoners ... walking into a defended perimeter" read the wrong way round |
| S9: "German antifascist volunteers" to "German and central European refugees", in both copies | **Correct, and the byte-identity was preserved.** I verified scene 23 and scene 93 are still character-for-character identical, so the 93 to 23 reuse still re-serves the existing file and the unique-generation count stays at 100. This was the risky one and it was done properly |

**Nothing else moved.** I diffed the full inventory of spoken beats and VISUAL tags against
loop 1: 26 directed narration changes, 3 declared VISUAL changes, 1 beat and 1 tag removed
for F1. No undeclared edits.

## Fact-check log re-audit

**The rewrite is real and the log is now honest.** I checked every row for a claim touched at
QA against the sources themselves, not against the writer's description. All four rows the
writer flagged as materially false are corrected and each now names the contradicting
evidence rather than quietly dropping the claim:

- **Ammunition:** now states outright that the first draft's "FSALE and French Wikipedia
  agreeing" was false in both halves, and names the Association de l'Artillerie's "150 a 200
  coups **par piece de 75**" as the figure that inverts the meaning. Matches what I found.
- **Water:** now quotes "qui servira **surtout** pour les blesses", states that "surtout"
  means mainly and not almost entirely, and admits the earlier row "was vouching for a
  phrase the source does not contain." Matches.
- **Axis 3,300:** now credits Broche, *Bir Hakeim*, Perrin/Tempus 2012, pp. 158 to 160, under
  the heading "Du cote de l'Axe", and explicitly corrects the defense.gouv.fr credit on the
  ground that page calls the losses *allemandes*. Exactly what I found.
- **Churchill:** retained as a **CUT AT QA** row with the correct actor, body and date. Keeping
  the false attribution on the record rather than deleting the row is the right call.

The other rewritten rows are equally straight. The Stuka row names Playfair's 45 plus 3 Ju 88s
and 10 Bf 110s, quotes Chauliac's two-bomb sentence in French, and offers the aircraft-shot-down
migration as the likely origin of the 42. The 620 Indians row corrects its own earlier
"footnoted" to "uncited" and adds the 30 to 31 May chronology caveat unprompted. The ~900 row
reproduces the arithmetic that refuses the invented mechanism. The Nino Bixio row names the
competing 143. The Walter Grand row notes his own biography is unsourced and describes German
Panzers. **These rows now say the thin thing where the support is thin.**

**But the rewrite only audited rows QA had flagged, and one unflagged row carries a false
corroboration claim.** This is condition **C3**:

> "About two thirds of the brigade came from France's colonies and overseas territories |
> Verified | **Tier 1.** MC22 and the Fondation Charles de Gaulle both state it"

**Neither source states it.** I searched the MC22 text directly for "tiers", "colonies" and
"outre": the only hits are "en outre equipes" (meaning "moreover equipped") and "Oubangui".
MC22 lists the colonial and overseas units individually but never gives a fraction. And my own
fetch of the Fondation Charles de Gaulle Bir Hakeim page in loop 1 returned no two-thirds
statement either. **The claim itself is true and Tier 1 supported**, but by a third page the row
does not name: defense.gouv.fr/terre, "deux tiers sont issus des colonies et des outremers."

The narration is safe. The log row is not, and it violates the writer's own new header rule
that "a row that overstates support is worse than no row at all." Fixing it costs nothing on
screen.

**Two further rows understate their support.** Both err in the safe direction so neither is a
condition, but both should be corrected when convenient: the Spanish Republicans row says "No
ministry source I have reaches the Spanish Republican figure" without mentioning that the
French Wikipedia footnote cites **Milza, Peschanski and Cuesta Bustillo, L'Harmattan 1994**,
which is academic press; and the British battery row leads with the French Wikipedia order of
battle without noting that **MC22 states it at Tier 1**, "La DCA est renforcee par une batterie
anglaise".

## Conditions

Three, all surgical. **C1 and C2 are word-count neutral and inside the 14-word cap, so the
narration stays at 1,394 and the runtimes stay at 8:49 and 8:03. C3 touches no narration.**

**C1. Act 2.** Replace:
`Under an hour. The Italians lost about half their tanks that morning.`
with:
`Under an hour. The division had lost about half of its tanks.`
Restores the singular antecedent for the next beat's "It left thirty two tanks behind" and
removes the duplicate "that morning" two beats later. **12 words, delta 0.**

**C2. Act 4.** Replace:
`By one count, forty thousand heavy shells came in. Forty two thousand back.`
with:
`Forty thousand heavy shells came in, by one estimate. Forty two thousand back.`
Clears the collision with the following beat's "By Rommel's own count", and the beat now opens
on the number. **13 words, delta 0.**

**C3. Fact-check log, the "two thirds" row.** Replace the support cell:
`**Tier 1.** MC22 and the Fondation Charles de Gaulle both state it`
with:
`**Tier 1.** defense.gouv.fr/terre: "deux tiers sont issus des colonies et des outremers." **Correction to the first draft's row, which credited MC22 and the Fondation Charles de Gaulle: QA searched both and neither states the fraction.** MC22 lists the colonial and overseas units individually but gives no proportion`

**Applying C1, C2 and C3 converts this verdict to PASS.** No re-gate is required after them:
they introduce no new claim, change no number, move no word count and touch no VISUAL tag,
and I have already verified the replacement wordings against the beats on either side.

## Polish, non-blocking, apply or ignore

- **P1.** F13's replacement reads "Rommel walked into a **position** that was already gone.
  Twelve hundred fighting **positions**." My wording, my echo. If you want it gone:
  `Rommel walked into a place that was already gone. Twelve hundred fighting positions.` **13 words, delta 0.**
- **P2.** Act 2 has "Then the attack collapsed" immediately followed by "Then the RAF started
  bombing". Pre-existing in the first draft, not collateral. Leave it or vary the second.
- **P3.** The two log rows that understate support, described above.
- **P4.** The production notes still say "**28 across the episode**" for the comedy count. The
  cut Churchill beat carried "That part is real", which was counted as one of Act 7's four.
  The figure is now 27. Documentation only.

## Re-gate summary

The revision did what it was asked to do. All 26 fixes landed verbatim, no stale wording
survived, the three undeclared VISUAL edits were correct and were declared, the beat removal
did not break the reuse chain, and the structural and timing numbers reproduce exactly. The
fact-check log has gone from the weakest part of the package to a genuinely useful one: it now
names contradicting sources, admits its own prior false claims in writing, and keeps the cut
Churchill row on the record.

Three of the fixes improved the episode rather than merely making it safe. Chauliac's aid-post
account is harder than the numbered version it replaced. The RAF bombing Bir Hakeim by mistake
is both true and funnier than the RAF bombing dead tanks. And narrowing the Rondeau rebuttal to
the El Alamein claim removed a soft self-contradiction in Act 7 that neither the writer nor I
had noticed in loop 1.

The two collateral breaks are mine, not the writer's: my Act 2 replacement orphaned a pronoun
and my Act 4 hedge collided with the hedge next to it. Both are one line and neither costs a
word. The one substantive finding against the revision is a fact-check log row that was never
flagged, and so was never re-audited, which claims corroboration from two sources that do not
carry the claim.

Nothing false remains in the narration. Every casualty figure is either corroborated or
hedged. Every named person is confirmed. Every number traces to a source I read. The arithmetic
reconciles on screen. Runtime clears the mid-roll floor at both ends of the observed VO range,
though only by three and a half seconds at the fast end, which the VO pass should be told.

**Conditional on C1, C2 and C3, which are supplied verbatim above and change no word count:**

VERDICT: PASS

---

## Manager close-out

The three conditions C1, C2 and C3 were applied verbatim on 2026-09-02, each verified to occur exactly once before replacement. Non-blocking polish item on the comedy count was also applied (28 to 27, with the reason recorded inline).

No new claim was introduced, no number changed, no VISUAL tag touched, and narration remains 1,394 words across 111 beats. Per the QA agent's own statement, "Applying C1, C2 and C3 converts this verdict to PASS. No re-gate is required after them."

That condition is satisfied. This is the QA agent's conditional PASS taking effect, not a new Manager judgement.

Noted for the build: fast-end runtime is 8:03 against the 8:00 mid-roll floor, a margin of 3.5 seconds. The VO pass must not be rushed. If more headroom is wanted later, QA verified that the Rommel handwritten-ultimatum beat would add about 13 words and take the fast end to roughly 8:08.

VERDICT: PASS

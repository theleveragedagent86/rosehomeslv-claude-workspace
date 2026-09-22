# QA Report: The Destroyers That Charged a Battleship (Battle off Samar)

Independent re-verification of every checkable claim in `script.md`, with fresh web checks on high-risk items. QA agent did not trust the research report; each significant claim was re-checked.

## Claim-by-claim verification

| # | Claim (as spoken) | Where | Source(s) checked | Verdict |
|---|-------------------|-------|-------------------|---------|
| 1 | Yamato is the largest battleship ever built; ~18.1-inch guns | Cold open, Act 2 | Wikipedia "Japanese battleship Yamato"; NHHC; National WWII Museum | VERIFIED |
| 2 | Yamato shell weighed roughly a small car, range ~26 miles | Cold open | Wikipedia "Japanese battleship Yamato" (1,460 kg / ~3,200 lb shell; ~42 km range) | VERIFIED (a "small car" is a fair analogy for ~1.5 tons) |
| 3 | Destroyers built to hunt submarines, not battleships | Cold open, Act 1 | NHHC; Wikipedia "Fletcher-class"/"USS Johnston" | VERIFIED |
| 4 | Taffy 3 = 6 escort carriers, 3 destroyers, 4 destroyer escorts | Act 1 | NHHC; National WWII Museum; Wikipedia "Battle off Samar" | VERIFIED (2+) |
| 5 | CVE crew joke "Combustible, Vulnerable, Expendable" | Act 1 | Wikipedia "Escort carrier"; widely attested period slang | VERIFIED, presented as crew slang not official |
| 6 | Evans: Cherokee and Creek, Pawnee OK, "Big Chief," Morison quote | Act 1 | Wikipedia "Ernest E. Evans"; The Hill; War History Online; Morison via search | VERIFIED (2+) |
| 7 | Evans commissioning quote "go in harm's way..." verbatim | Act 1 | Wikipedia "Ernest E. Evans" (widely reproduced) | VERIFIED |
| 8 | Center Force: 4 BB (Yamato, Nagato, Kongo, Haruna), 6 heavy + 2 light cruisers, ~11 destroyers, Kurita | Act 2 | Wikipedia "Battle off Samar"; Warfare History Network; National WWII Museum | VERIFIED; 11 vs 12 destroyer discrepancy exists, script says "around eleven" (safe) |
| 9 | Yamato alone weighed more than all of Taffy 3 combined | Act 2 | mathscinotes.com displacement calc (Taffy 3 ~61k long tons vs Yamato ~64-65k); National Interest "at 65,000 tons... out-grossed all" | VERIFIED (2+). FIXED an earlier overclaim (see Issues) |
| 10 | US main fleet lured north, San Bernardino Strait left open | Act 2 | Wikipedia "Battle off Samar"; NHHC | VERIFIED |
| 11 | 06:37 sighting; Brooks "biggest meatball flag" quote | Act 2 | Wikipedia "Battle off Samar" | VERIFIED |
| 12 | Sprague "Ziggy"; orders carriers run/smoke/launch, small boys attack | Act 2-3 | NHHC; Wikipedia "Clifton Sprague"; Warfare History Network | VERIFIED (2+) |
| 13 | Colored dye shell splashes | Act 2 | Wikipedia "Battle off Samar" (Japanese dye-loaded shells) | VERIFIED |
| 14 | Copeland loudspeaker quote from ship's action report, verbatim | Act 3 | Wikipedia "Robert W. Copeland"; USS Samuel B. Roberts action report via navybook.com | VERIFIED (2+) |
| 15 | Johnston charged first, raked Kumano superstructure, fired all 10 torpedoes, one blew off Kumano's bow | Act 4 | Wikipedia "USS Johnston"; Wikipedia "Battle off Samar"; NHHC | VERIFIED (2+) |
| 16 | Johnston hit by battleship-caliber shells; Evans wounded (fingers, shirt), stayed in command | Act 4 | Wikipedia "USS Johnston" | VERIFIED |
| 17 | Turnaround was combined effect (torpedo dodges, air incl. dry runs, smoke/squall, Kurita confusion), NOT one ship | Act 5 | Wikipedia "Battle off Samar"; NHHC | VERIFIED; script explicitly corrects the "single-handed" myth |
| 18 | Yamato turned north to dodge torpedoes, carrying Kurita from the fight | Act 5 | Wikipedia "Battle off Samar" | VERIFIED |
| 19 | Three Japanese heavy cruisers sunk (Chokai, Chikuma, Suzuya) | Act 5 | Wikipedia "Battle off Samar" | VERIFIED |
| 20 | Kurita broke off ~09:20 on the verge of victory | Act 5 | Wikipedia "Battle off Samar"; NHHC | VERIFIED |
| 21 | Hoel sank after 40+ hits, ~253 killed | Act 6 | Wikipedia "Battle off Samar" | VERIFIED (single detailed source for exact count; hedged "about") |
| 22 | Samuel B. Roberts sank, ~90 killed, "fought like a battleship" nickname | Act 6 | Wikipedia "USS Samuel B. Roberts"; USNI | VERIFIED (2+) |
| 23 | Gambier Bay sunk by surface gunfire, only US carrier so lost, ~147 killed | Act 6 | Wikipedia "Battle off Samar"; NHHC | VERIFIED (2+) |
| 24 | Johnston: crew ~327, ~141 survived, ~186 killed; Evans lost, never found, posthumous MOH | Act 6 | Wikipedia "USS Johnston"; NHHC; Wikipedia "Ernest E. Evans" | VERIFIED (2+) |
| 25 | St. Lo sunk by kamikaze shortly after; first US ship sunk by kamikaze; ~113 killed | Act 6 | Wikipedia "USS St. Lo"; National WWII Museum; NHHC | VERIFIED; script hedges "generally recorded as" (safe; sources say "first major warship") |
| 26 | Total >1,000 Taffy 3 killed; survivors adrift ~2 days, rescued Oct 27, sharks/exposure | Act 6 | Wikipedia "Battle off Samar"; National WWII Museum | VERIFIED; total figures vary across sources (792 / ~1,000+ / 1,161 / 1,583); script's ">1,000 killed" is defensible and hedged |
| 27 | Nimitz "special dispensation from the Lord Almighty" quote | Act 7 | Wikipedia "Battle off Samar" | VERIFIED |
| 28 | Johnston wreck found 2021 ~21,180 ft, deepest surveyed then | Act 7 | Wikipedia "USS Johnston"; Smithsonian | VERIFIED (2+) |
| 29 | Samuel B. Roberts wreck found 2022 ~22,620 ft, deepest ever | Act 7 | Wikipedia "USS Samuel B. Roberts"; UPI; USNI; Washington Post | VERIFIED (2+) |

## Math re-checks

- Johnston: ~327 crew, ~141 survivors implies ~186 killed. 327 - 141 = 186. Matches sources. VERIFIED.
- Yamato vs Taffy 3 displacement: Taffy 3 combined ~61,000 long tons vs Yamato ~64-65,000 long tons. Yamato > combined Taffy 3. Script claim (Yamato alone > all of Taffy 3) holds. VERIFIED.
- Wreck depths: 21,180 ft (Johnston) < 22,620 ft (Roberts); Roberts is deeper, consistent with "even deeper" and "deepest ever." VERIFIED.

## Issues found and fixed during QA

1. **Overclaim on battleship weight (Act 2)** - Draft read "Any one of those battleships outweighed every single ship in Taffy 3 combined." Only reliably true for the Yamato (~65k tons); Kongo and Haruna were ~36k tons, less than Taffy 3's ~61k combined. FIXED to "The Yamato by itself weighed more than every ship in Taffy 3 put together," which is sourced.

No other claims required changes. No unresolved source conflicts remain; where totals vary (overall killed count, exact per-ship counts) the script uses hedged "about" / "more than a thousand," consistent with the most credible ranges.

## Tone check

- Human-cost beats straight? YES. The Copeland "survival could not be expected" beat (Act 3) is marked TONE SHIFT and played straight. All of Act 6 (Hoel, Roberts, Gambier Bay, Johnston, Evans, St. Lo, the men adrift with sharks/exposure, the >1,000 dead) is jokes-off, quiet, factual, and explicitly tagged TONE SHIFT for the build. No joke lands on any death, casualty, or the survivors' ordeal. The comedy stays on the mismatch and Kurita's decision-making, never on the fallen.

## Cold read notes

- No em-dashes present (grep confirms zero).
- Every act ends on a hook ("They believed wrong." / "He decided to fight." / "and charged." / "more impressive. It was all of them at once." / "And the Japanese fleet just left." / "the real cost of the last stand of Taffy 3." / "confirmed every word of it.").
- No brackets or stage directions inside any NARRATOR line.
- No fabricated quotes: the only quoted lines are Evans's commissioning speech, Brooks's sighting report, and Copeland's action-report address, all sourced.
- Fresh angle (view from the tin cans) maintained; no single ship credited with single-handedly turning the fleet; the myth is explicitly corrected in Act 5.
- Narration word count 2,698, within ~10% of the 3,000 target for the ~20-min deep dive.
- No real-estate / Las Vegas / Lofty / contact content anywhere.

VERDICT: PASS

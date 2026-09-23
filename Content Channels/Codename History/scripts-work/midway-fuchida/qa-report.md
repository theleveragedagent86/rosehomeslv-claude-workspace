# QA Report: The Man Who Invented The Battle Of Midway

**Final pass. Loop 2 of 2.**

## VERDICT SUMMARY

**`script.md` PASSES.** Every check is clean. Both Richard Best frames are gone, the seam is invisible, the correction still stands on its three verified legs, all 16 loop-0 issues remain resolved, and every count and timecode I recomputed independently matches.

**One mandatory correction outside the script, and it is blocking for one asset.**

> ### HOLD: `shorts-package.md` line 37
> The published YouTube description for the `what-was-on-the-decks` Short **still contains the sentence that was cut from the script at loop 1**, verbatim:
>
> *"Lieutenant Richard Best, who put the bomb through Akagi's flight deck, said the only aircraft up there were Zeros."*
>
> This is public-facing copy. It carries both loop-1 failure modes: an unauthenticable quotation attributed to a named real person, and a bomb attribution that NHHC's own 2019 update contests. A description is worse than narration for this, because it is permanent indexed text that can be quoted back exactly.
>
> **Delete that one sentence. The `what-was-on-the-decks` Short must not publish until it is gone.** The long-form episode is not blocked by this and may build.

Three trivial numeric corrections are listed under Loop 2 item 7. None of them block anything.

I am not failing the episode over this. The substance was fixed correctly in the script, the residue is a single sentence in a metadata file that the coordinator hand-edited and missed, and the remedy is a deletion of the same class as the one already performed. Failing an otherwise-clean flagship episode unbuilt over that would be the wrong call. But the sentence is not optional and I am naming it at the top so it cannot be missed.

---

## Loop 2 verification

**1. Both Best frames gone, no orphan reference in the script.** CONFIRMED. Lines 339 to 345 of the loop-1 file are absent. `grep -i` across the whole script returns Best in exactly two places, both deliberate and both correct:
- **Production notes item 10** (line 618) now reads that the correction rests on three independent legs and that the Best leg "was drafted and then cut at QA loop 1. Do not reinstate it."
- **Fact-check log** (line 682) is flagged **CUT AT QA LOOP 1. DO NOT REINSTATE**, and records both failure reasons accurately, including Best's actual sentence ("six or seven Zeros, which were in the process of launching") and the NHHC H-006-4 2019 update naming Lt. (j.g.) Sonderling.

These are internal build records, not spoken content, and keeping them is right: they are what stops a future pass from re-adding the frames. The other "eyewitness" hits are the pre-existing `fuchida-didnt-fly` hook, and the "About thirty Zeros were waiting" line is the unrelated VT-8 beat.

**2. The seam is clean.** CONFIRMED. Read `what-was-on-the-decks` (lines 282 to 344) start to end as a standalone. Line 337 ("Akagi was landing fighters fifteen minutes before she was hit. You cannot land on a full deck.") now runs straight into the MYTH / RECORD card at 339 and the guardrail line at 342 ("Not empty. Nobody serious says empty. But more empty than occupied, and mostly fighters."). That is a better sequence than the loop-1 version: the strongest single piece of reasoning in the episode now lands immediately before the card that summarizes it, with nothing between them. No dangling connective, no orphaned setup, no tonal hitch.

Standalone comprehension is intact. The Short still opens by naming Fuchida and Pearl Harbor, states his claim in his own quoted words, then produces the counter-evidence, then hedges itself. A viewer with zero context gets a complete argument in 71 seconds.

**3. The three legs still carry it, and nothing promises a fourth.** CONFIRMED, all three present and correctly stated inside the Short:
- **kodochosho** (line 305): "The carriers' own air unit records say otherwise."
- **Senshi Sosho** (lines 308, 310, 314): the 1971 card, "Japan's official war history says otherwise, flatly," and the quotation card "there were no attack aircraft on the Japanese flight decks. Only fighters."
- **B-17 photographs** (lines 317, 319, 323): the 0800-0820 card, "American B seventeens photographed the formation that same morning," and "Soryu, Hiryu, Akagi. No strike planes on deck. A handful of fighters."

Plus the two supporting arguments that were never Best-dependent: the 45-minute spotting requirement (328, 332) and the 1010 CAP recovery (335, 337).

**No surviving counting or promising language.** I grepped specifically for "one more witness," "witness," "another," "one more," "fourth." The narration contains none of it. The removed line's "One more witness" opener went with it, so there is no sentence anywhere that sets up evidence the script no longer delivers.

**4. Recount.** All independently recomputed from the file. Every figure matches the coordinator's.

| Check | Coordinator | Measured | Result |
|---|---|---|---|
| Narration words | 1,625 | **1,625** (1,593 NARRATOR + 32 character-voice) | MATCH |
| VISUAL tags | 124 | **124** | MATCH |
| Duplicate VISUAL tags | 0 | **0** (124 unique of 124) | MATCH |
| NARRATOR lines | - | **120** (was 122, minus 2) | Consistent |
| Text-bearing frames | - | **32** (28 ON-SCREEN TEXT + 4 SPEECH BUBBLE), plus 1 TITLE CARD | Unchanged by the cut |
| TONE: STRAIGHT frames | 13 | **13** | MATCH |
| Straight frames carrying text | 0 | **0** | PASS |
| Em-dashes (U+2014) | 0 | **0** | PASS |
| En-dashes (U+2013) | 0 | **0** | PASS |
| Brackets or parens in NARRATOR lines | 0 | **0** of 120 | PASS |
| Short marker pairs | 6 | **6 opened, 6 closed, zero overlaps** | PASS |

Arithmetic note: the deletion was **24 narration words**, not the 23 I estimated in loop 1 (15 + 9). 1,649 minus 24 = 1,625, which is what the file measures. My loop-1 estimate was one word light; the executed result is correct.

**5. Timecode arithmetic.** CONFIRMED, and it holds tighter than required. 24 words at 150 wpm = 9.6 seconds, so a 9-second shift is right. Cold open, Act 1 and Act 2 correctly unshifted (the cut is inside Act 3). I then recomputed each act's own narration volume against its tagged span:

| Section | Words | Duration @150wpm | Tagged | Delta |
|---|---|---|---|---|
| COLD OPEN | 101 | 0:40 | 0:00-0:40 | 0s |
| ACT 1 | 208 | 1:23 | 0:40-2:04 | +1s |
| ACT 2 | 354 | 2:21 | 2:04-4:25 | -1s |
| ACT 3 | 251 | 1:40 | 4:25-6:06 | +1s |
| ACT 4 | 313 | 2:05 | 6:06-8:11 | 0s |
| ACT 5 | 344 | 2:17 | 8:11-10:29 | 0s |
| OUTRO | 54 | 0:21 | 10:29-10:51 | 0s |
| **TOTAL** | **1,625** | **10:50** | ends 10:51 | +1s |

Every act is within one second of its tagged span, boundaries are contiguous with no gaps or overlaps, and the total matches the header's ~10:50. The one-second residue at the end is rounding.

**6. Nothing else regressed.** CONFIRMED. All 16 loop-0 issues re-checked against the current file and all 16 remain resolved (table below). Both guardrails intact: the "not empty" line survives verbatim inside the Short at 342, and the American-victory protection survives at lines 547 and 551 ("This does not make the American victory smaller. Those men were skilled and brave and they beat a strong force. Correcting the story takes nothing from them."). The live Bennett dispute is still named out loud with its PARSHALL vs BENNETT card. Tone is unchanged: 13 straight frames, none carrying text, no joke on or adjacent to a human-cost beat, and the burning-carriers buffer frame is still in place.

**7. Companion-doc sync.** PARTIAL. `package.md` chapter marks are correctly resynced (0:00 / 0:40 / 2:04 / 4:25 / **6:06** / **8:11** / **10:29**) and the Act 2 chapter title correctly reads "Sixty Five Minutes Of Changing Their Minds." Four items were missed:

- **`shorts-package.md` line 37 — BLOCKING for that Short.** The Best sentence, described at the top of this report. Delete it. The rest of that description is accurate and stands on its own without the sentence.
- **`shorts-package.md` line 34** says "(~71 s, 178 narration words)". Measured: **177 words, 71 seconds.** Off by one. Note that deleting the Best sentence from the *description* does not change this figure, which counts the Short's narration, not its copy.
- **`shorts-package.md` line 5 and `package.md` line 4** both still say the parent video is ~11:00. It is **~10:50**.
- **`script.md` line 645**, the build note, still says "**126** VISUAL tags." It is **124**. The header was updated to 124 scenes but this line was not, and this is the line a build agent reads. Fix it to avoid a frame-count mismatch during production.
- **`package.md` line 85** carries `richard best` in the tag list. He is no longer in the episode. Remove the tag; tagging a figure we deliberately cut for sourcing reasons invites exactly the scrutiny we removed him to avoid.

---

## Loop 1 resolution (retained, all re-confirmed against the final file)

| # | Original issue | Status | Final-file confirmation |
|---|---|---|---|
| 1 | "Ninety five minutes" (narration + `ordnance-shuffle` hook) | **RESOLVED** | "Sixty five minutes" in narration, "65 minutes" in the hook, and `package.md`'s chapter title. 0715 to 0820 = 65, recomputed |
| 2 | "Nine minutes after Akagi was hit" | **RESOLVED** | "Three minutes." *Akagi* TROM: hit 1026, hangar explosions 1029 |
| 3 | "That was Carter Ham" | **RESOLVED** | "he was not the codebreaker. He ran the codebreakers." No name |
| 4 | Outro contradicting Act 1 on Rochefort | **RESOLVED** | "the man who ran the basement that won Midway" |
| 5 | `torpedo-squadrons` Short hook | **RESOLVED** | Hook binds 42, 99 and 3 to one population, matching NHHC H-006-1 verbatim. Date inside the clip |
| 6 | "every one of them down at wave top height" | **RESOLVED** | "strung out low and chasing the last torpedo attack" |
| 7 | 99/42 scope ambiguity | **RESOLVED** | "Counting the crews who flew from the island" |
| 8 | "Destroyed the same way" for VT-6 | **RESOLVED** | "Cut apart the same way" |
| 9 | Invented hangar-fueling causal link | **RESOLVED** | "And the Japanese fueled their aircraft down there in the hangars" |
| 10 | Phantom "second order" | **RESOLVED** | "An order, and then the counter order" |
| 11 | Parshall's Japan-credibility line unattributed | **RESOLVED** | "Parshall's line is that..." |
| 12 | "every single one of them rearmed" | **RESOLVED** | "He orders them rearmed with land attack bombs instead" |
| 13 | "Three American airmen" as a total count | **RESOLVED** | "Three of the Americans pulled from the water..." |
| 14 | Shorts 4 and 5 not self-contained | **RESOLVED** | Both open with their own orienting line; re-read standalone after the cut and both still work |
| 15 | "Lieutenant Jasper Holmes" | **RESOLVED** | "Jasper Holmes, one of Rochefort's staff" |
| 16 | Appendectomy/ankles asserted flat | **RESOLVED** | "By his own account, and nobody argues with this one..." |

Plus the two loop-1 blockers:

| Loop-1 blocker | Status |
|---|---|
| "Richard Best put the bomb that killed Akagi through her flight deck" (contested by NHHC's own 2019 update) | **RESOLVED, cut** |
| "He said the only aircraft up there were Zeros" (unauthenticable) | **RESOLVED in the script, OUTSTANDING in `shorts-package.md` line 37** |

---

## Shorts standalone-accuracy check (final)

Measured from the file, narration words per marked stretch:

| Slug | Lines | Words | Runtime | Verdict |
|---|---|---|---|---|
| `fuchida-didnt-fly` | 14-53 | 101 | 40s | PASS |
| `ordnance-shuffle` | 157-203 | 111 | 44s | PASS |
| `torpedo-squadrons` | 213-239 | 92 | 37s | PASS |
| `what-was-on-the-decks` | 282-344 | 177 | 71s | **Script PASS. Publication HELD** on the line-37 description fix |
| `hangar-deck` | 354-397 | 126 | 50s | PASS |
| `usni-1955` | 456-479 | 58 | 23s | PASS |

Zero overlaps, all six pairs opened and closed, none crossing an act boundary. Every hook is true standalone with no surrounding context.

---

## Advisories to ride along into the build (notes, not blockers)

1. **`script.md` line 645 says 126 VISUAL tags; the real count is 124.** Correct this before handing to the build agent, or it will expect two frames that do not exist.
2. **Yorktown is introduced cold** at Act 4 line 401 ("Now compare. Yorktown, same day, same battle"), because the 72-hour repair segment was cut from Act 1. A three-word patch fixes it: "the American carrier Yorktown."
3. **Hiryu is never established.** Act 3 says three carriers were fatally hit; Act 4 then says all four were burning and all four were scuttled. Both statements are verified true (*Hiryu* hit 1703, all four simultaneously burning ~1703 to ~1912), and eliding her counterstrike is a defensible runtime call, but a sharp viewer will notice the three-to-four jump.
4. **Osmus and "three survived."** NHHC's figure counts survivors of the battle, so Osmus, who survived his shootdown and was then murdered, is correctly excluded from the three. The script is faithful to the source. Noted so nobody "corrects" it later.
5. **The `what-was-on-the-decks` Short is the heaviest vertical-crop job** in the batch per `shorts-package.md`, and the cut removed a portrait and a cockpit POV, both of which cropped cleanly. The frames that survive skew wider than before. Budget accordingly.
6. **Do not reinstate Richard Best** in any form, in the script, the descriptions, the tags, or the thumbnail copy. The fact-check log records why. If a future pass wants an American eyewitness, the only defensible version is his real sentence, hedged and attributed, and it is weaker than the three legs already in place.

---

## Cold read notes

The cut improved the act. Act 3 previously spent its last three beats stacking evidence and then paused for a personality frame before the summary card; now the 1010 CAP recovery lands and the MYTH / RECORD card answers it immediately. That is tighter, and it puts the episode's single best argument, you cannot land aircraft on a deck that has a strike spotted on it, directly against the card that states the conclusion. The Short is 71 seconds instead of 80 and reads faster for it.

The rest of the script is where it was at loop 1, which is to say ready. The spine is verified from four directions in the source record and stated in three inside the video. Every accusation runs through a named historian in a named journal. The live dispute is on screen. Both guardrails are stated out loud rather than merely observed, and both survive inside the Shorts where they will travel. The arithmetic that failed loop 0 is now correct in every place it appears, including the on-screen cards that a viewer can check against the narration in real time.

The one thing left is a sentence in a metadata file. It matters because it is the exact claim this pass existed to remove, and because a Short description is more quotable than narration, not less. But it is a deletion, not a rewrite, and it does not touch the episode.

Fix `shorts-package.md` line 37, correct the four numbers, and this ships.

---

**Ship condition:** `script.md` is cleared for build to `transcripts/midway-fuchida.md`. The `what-was-on-the-decks` Short is cleared to build but **not to publish** until the Best sentence is deleted from its description. No re-QA is required for any of the seven corrections; they are deletions and numeric edits with no downstream dependencies.

VERDICT: PASS

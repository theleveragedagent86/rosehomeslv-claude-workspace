# BUILD SPEC: midway-fuchida (stills-only format)

This overrides the default `codename-history` build behavior for this episode. Read it before Wave C.

Verified against the live Higgsfield MCP on 2026-08-05 (account: Ultra plan, 2,681.35 credits).

---

## 1. Format change vs. previous episodes

| | final-minutes-ww1 (reference) | THIS EPISODE |
|---|---|---|
| Scenes | 150 | ~126 (one per VISUAL tag) |
| Unique stills | 36, reused across scenes | **~126, one per scene, ZERO reuse** |
| Motion clips | 9 Kling clips (90 credits) | **1, the cold open only** |
| Everything else | KENBURNS over reused stills | KENBURNS / static over unique stills |
| Pacing | variable | **one image every 3 to 7 seconds** |

**Hard rule: no still is used for more than one scene.** The previous pipeline's HOLD/reuse behavior (`stills/S72.png (HOLD)`) is disabled for this build. If a scene has no still, generate one, do not borrow the neighbor's.

Scene duration is driven by the VO take length, clamped to 3 to 7 seconds. If a take runs longer than 7 seconds, split the narration line and generate a second still rather than holding one image past 7 seconds.

---

## 2. Stills: `generate_image`, model `nano_banana_pro`

```
model: "nano_banana_pro"
aspect_ratio: "16:9"
resolution: "2k"
prompt: <scene STILL text> + <STYLE token string>
medias: [{ value: "<character sheet media id>", role: "image" }]   // from cast-map.md, holds characters on-model
```

**Why this model specifically:** `nano_banana_pro` is tagged `text-rendering` and `diagrams` in the live catalog. This episode puts words inside ~33 frames (speech bubbles, dates, document pages, myth-vs-record labels), and it is the model in the catalog built for legible in-image text. Do not substitute a different image model for the text-bearing frames.

### CREDIT WARNING, needs Ryan's confirmation before Wave C

`nano_banana_pro` carries `supports_unlim: true`, so it IS an unlimited-eligible model. **However, the live API currently reports `unlim: { available: false, remaining: null, expires_at: null }` for this account.** That means the free unlimited allowance is not spendable right now, and ~126 stills would draw against the 2,681 credit balance instead.

Before generating stills, re-check with:
```
models_explore(action="list", type="image", unlim=true)
```
and confirm the top-level `unlim.available` is `true`. If it is still `false`, STOP and tell Ryan, because the whole premise of this format is free stills. Do not silently spend credits on 126 images.

---

## 3. Motion: exactly ONE clip, scene S01 only

Every scene except S01 is a still. S01 is the cold open's single animated action.

**Recommended:** `kling3_0` (not `kling3_0_turbo`)
```
model: "kling3_0"
mode: "pro"
sound: "off"          // we lay Cillian VO + our own bed under it
duration: 5
aspect_ratio: "16:9"
medias: [{ value: "<S01 still>", role: "start_image" }]
```
`kling3_0` is a step up from the `kling3_0_turbo` used previously, supports `mode: "pro"`, and also carries `supports_unlim: true`. `sound: "off"` lowers the credit cost and we do not want its generated audio.

**Upgrade option if the Kling result is weak:** `veo3_1` with `variant: "veo-3-1-preview"`, `quality: "high"`, `duration: 4`. Top-tier cinematic quality, but it is NOT unlim-eligible and it leans photoreal, which fights the channel's flat cartoon look. Only reach for it if Kling fails twice.

Since this build spends 10 credits on motion instead of 90, there is ample room to re-roll S01 several times to get it right. Do that. It is the only motion in the video and it carries the cold open.

**Carry forward from lessons-learned:** the preset-recommendation gate still applies. If the first call returns a `preset_recommendation`, retry the identical request with `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"`. If it returns `status: "nsfw"` on a benign shot, do not fight it, animate the still locally with ffmpeg `zoompan`.

---

## 4. On-screen text tags (new this episode)

The script carries two new tag types. Both must survive into the shotlist.

- `SPEECH BUBBLE: "..."` appears INSIDE a `[VISUAL: ...]` tag, always on the frame immediately before a `(character voice)` line. Render as a cartoon speech bubble containing that exact text. 8 words or fewer.
- `**[ON-SCREEN TEXT: "..."]**` is its own tag following a visual. Render as a caption or label in the channel's heavy condensed sans. 6 words or fewer.

Pass the quoted string through to the image prompt verbatim, in quotes, and instruct the model to render it as legible text. Spell-check the rendered output: a misspelled word in a frame is a re-generate, not a ship.

**No text on any `TONE: STRAIGHT` frame.** There are 12 of them. The casualty and execution beats carry no words.

---

## 5. Voiceover: unchanged

ElevenLabs "Cillian", `variant: "elevenlabs"`, `voice_type: "preset"`, `voice_id: d8ba9f14-8a24-44db-932b-99e16c45bd32`. One take per scene, 6.5 s of text maximum. `voice_type` must be `preset`, never `element`.

---

## 6. Shorts: 6 vertical cuts, zero extra credits

The script carries 6 non-overlapping `<!-- SHORT-START: ... -->` / `<!-- SHORT-END: ... -->` marker pairs. Cut all 6 locally from the finished episode segments, exactly as `final-minutes-ww1` did. **No new generation.**

Output 1080x1920, 30 fps, AAC, to `episodes/midway-fuchida/shorts/`.

**The one new problem:** the source stills are 16:9 and the Shorts are 9:16, and unlike last time there is no motion to hide a crop behind. Handle it in this order:
1. **Center-crop to 9:16 first.** Free and instant. Check each frame: if the subject survives the crop, ship it.
2. **Where the crop kills the composition** (wide maps, side-by-side myth-vs-record frames, anything with on-screen text near the horizontal edges), regenerate that single frame natively at `aspect_ratio: "9:16"` with the same prompt. Same model, same cost basis as any other still.
3. Never letterbox a 16:9 frame into a 9:16 Short with black bars. It reads as lazy in the feed.

Text-bearing frames need the most attention here, since centered 16:9 text often clips at 9:16.

---

## 7. Wave-C checklist before generating anything

- [ ] `balance` returns successfully (Higgsfield connected).
- [ ] `unlim.available` is `true` for image models, or Ryan has explicitly approved spending credits on stills.
- [ ] Character sheets exist in `character-library/sheets/` and `cast-map.md` maps every recurring figure (Fuchida, Nagumo, Rochefort, Parshall, the American pilots).
- [ ] Scene table has one unique still slot per scene, no HOLD entries.
- [ ] Every scene duration falls between 3.0 and 7.0 seconds.
- [ ] Only S01 is marked KLING. Everything else is KENBURNS or STATIC.
- [ ] The 12 `TONE: STRAIGHT` scenes carry no on-screen text and get slow, somber Ken Burns.

# ManyChat Flow Spec — The Leveraged Agent

The canonical automation architecture every keyword-CTA carousel ships. The carousel skill
writes the copy into this shape. Building it in ManyChat is a separate, opt-in step.

**Brand boundary.** Leveraged Agent IG only (`@the.leveraged.agent`). Rose Homes LV inbound
is handled by the `inbound-dm-*` plugins, different account, different business. Never wire
a Leveraged Agent flow to the realtor account.

---

## The shape

One Growth Tool, one Flow, three outcomes.

```
TRIGGER  Instagram Comments on the carousel post
         keyword matches, case-insensitive
                │
                ├──► PUBLIC COMMENT REPLY   (rotated, 1 of 5)
                │    "Sent it over, check your DMs"
                │
                └──► DM SEQUENCE
                     Msg 1   tc1     the opener
                     delay 4s
                     Msg 2   tc2a    deliverable part 1
                     delay 4s
                     Msg 3   tc2b    deliverable part 2
                     delay 2s
                     Msg 4   the branch question + 3 buttons
                              ├─ [I run my own deals] ──► tc3   + tag
                              ├─ [I have a TC]        ──► tc3B  + tag
                              └─ [I'm brand new]      ──► tc3C  + tag
                                        │
                                        └──► tag TC-lead, 24h follow-up if no tap
```

A second trigger on the same Flow catches people who DM the keyword directly instead of
commenting. Same Flow, the comment-reply step is skipped, there is no comment to reply to.

---

## Why the buttons exist

The manual DM sequence deliberately stops after `tc2b` and waits for a human reply before
sending any link. Instagram throttles accounts that fire links at people who have not
replied, and a cold link reads as a bot.

The buttons satisfy that. A tap **is** a reply, it opens the conversation, and it routes
the branch without Ryan reading each DM. Do not replace the buttons with an auto-sent
`tc3`. The wait is the point.

---

## Copy rules inside the flow

- **1000 characters is the hard cap per Instagram DM.** Count every message. Instagram
  truncates silently, it does not warn. If a message is over, split it and add a step.
- Plain text only. DMs render markdown literally. No `**bold**`, no `#` headings, no
  bullets with `-`. Use CAPS section labels and blank lines.
- Links only in the branch messages, never before the button tap.
- Delays between messages, 3 to 5 seconds. Zero delay looks like a bot dump, 10 seconds
  looks broken.
- Same compliance as the carousel: no income claims, no guarantees, no pricing in the DM,
  no legal or lending advice.

---

## The public comment reply

Write **five** variants and rotate them. Identical replies stacked under one post is the
clearest bot signal on the platform, and it is what gets a post's reach cut.

Rules:
- Under 12 words.
- Confirm the send, nothing else. No pitch, no link, no hashtags.
- Never say "check your DMs" five times. Vary the verb and the structure.
- One variant should answer as a human would if the comment was a real question.
- No emoji in more than two of the five.

Ship them as a numbered list so they paste straight into ManyChat's rotation field.

---

## Keyword rules

- One word, 2 to 12 characters, uppercase in the carousel art, matched case-insensitive.
- Must not be a word that appears in normal praise, so never GREAT, LOVE, THIS, YES, INFO.
  A false match sends the wrong lead magnet to someone who was just being nice.
- Must not collide with a keyword already live on another post. Keep the running list in
  the carousel folder's automation file.
- Set matching to **contains**, not exact. People type "TC please" and "tc?" far more than
  they type the bare word.

---

## Build order, when driving the browser

Ryan does the three things involving credentials, they are not automatable and never
attempted: **sign up, pay, connect the Instagram account via OAuth.**

Then, in ManyChat:

1. Automation > New Automation > start from scratch. Name it `Carousel NN - KEYWORD`.
2. Add trigger: Instagram > Comments. Select the specific post. Set the keyword, contains,
   case-insensitive.
3. Enable the public reply on the trigger. Paste all five rotation variants.
4. Build the DM steps in order, one Instagram Message node each, with delay nodes between.
5. On the last message node add the three buttons. Each button targets its own message node.
6. Add a tag action on each branch. Tags: `TC-lead-self`, `TC-lead-hasTC`, `TC-lead-new`.
7. Add the smart delay 24h + condition "has not tapped" > follow-up message.
8. Preview the flow in ManyChat's own preview, then publish.
9. Test live from a second Instagram account before telling Ryan it is done. A flow that
   was never triggered has not been verified.

Screenshot after each numbered step. The builder is a drag-and-drop canvas, so nodes land
in the wrong place silently and connector lines fail to attach without any error.

---

## Verify in the builder, do not assume

These change with ManyChat and Meta releases. Check them live, mark NOT FOUND rather than
guessing:

- Max buttons per Instagram message node.
- Whether the public comment reply supports rotation natively, or needs a randomizer step.
- Whether a DM to a non-follower lands in the inbox or in Requests.
- The current messaging window rules and which message tag, if any, the 24h follow-up needs.

---

## What this flow does not do

It does not close anyone. It delivers the thing that was promised, sorts the lead into one
of three buckets, and hands Ryan a tagged list. The conversation is still his.

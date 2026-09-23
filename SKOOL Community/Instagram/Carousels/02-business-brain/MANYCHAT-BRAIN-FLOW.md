# ManyChat gameplan, keyword: BRAIN

Automation for the Business Brain carousel. Replaces the manual saved-reply system used for
the TC keyword (`../dm-reply-TC.txt`), which required Ryan to be at his phone.

Rule this whole flow is built around, taken from the Peyson teardown and from Instagram's own
throttling behavior: **the public comment reply is not the delivery, the DM is, and the link
does not go out until the person has interacted at least once inside the DM.** A link that
lands before any back and forth reads as a bot and gets the account rate limited.

---

## 0. The asset, and the three links you still need

The carousel promises "the folder structure and the CLAUDE.md I actually run my business on."

**That asset is written: `BUSINESS-BRAIN-STARTER.md` in this folder.** It carries the folder
tree, the full paste-ready CLAUDE.md on BROKER, the starter skills list, the level ladder, and
a Leveraged Agent block at the end with the community link, YouTube and Instagram, plus the
compliance footer. It is branded, it is not a naked text dump, and it does the second half of
the selling on its own after the DM is over.

**Publish it as a Google Doc set to "anyone with the link can view", or export to PDF and host
it.** Do not put it behind a Skool signup. The DM promised the file, not a signup, and breaking
that in the first message is how the whole funnel loses trust. The community ask happens inside
the doc and in DM 4, after the promise has already been kept.

One link is still missing. The other two were confirmed on 2026-09-11 off Ryan's own Skool
profile and the live channel:

- `[YT_URL]` = `https://www.youtube.com/@theleveragedagent` (The Leveraged Agent w/ Ryan Rose,
  29 videos). It appears in DM 3 and inside the asset.
- `[IG_HANDLE]` = `@the.leveraged.agent`. It appears inside the asset. Note the dots. The
  dotless `@theleveragedagent` on Instagram is somebody else's account, so never use it.
- `[BRAIN_ASSET_URL]` = wherever you publish `BUSINESS-BRAIN-STARTER.md`. It appears in DM 2C.
  **This is the only one still open.**

Skool link is known and already written in: `https://www.skool.com/the-leveraged-agent`

**Do not post the carousel until `[BRAIN_ASSET_URL]` is filled.**

---

## 1. Prerequisites, do these once

1. Instagram account is a **Professional** account (Business or Creator).
2. That account is **linked to a Facebook Page**. ManyChat connects through the Page, an IG
   account with no linked Page cannot be connected.
3. In the Instagram app: Settings > Messages and story replies > **Allow access to messages**
   is ON. If this is off ManyChat receives nothing and the flow silently never fires.
4. ManyChat account connected to the IG account, connection shows green in Settings.
5. **Verify the current ManyChat plan requirements yourself before building.** Instagram
   comment triggers have historically been a paid-tier feature and ManyChat's plan structure
   and contact pricing change. Do not assume, check the plan page.
6. Turn on ManyChat's **Live Chat notifications** to Ryan's phone. Step 7 of the flow depends
   on a human seeing the replies.

---

## 2. Flow map

```
IG comment contains "brain"  ─┐
IG DM contains "brain"       ─┼──> [Trigger]
Story reply contains "brain" ─┘
        │
        ├─ Action: public reply to the comment (rotates, no link)
        │
        └─ DM 1  opener + button "Send it"
                 │
                 ├─ button tapped ──> DM 2A  the folder structure
                 │                    DM 2B  the CLAUDE.md + BROKER
                 │                    DM 2C  the link  [BRAIN_ASSET_URL]
                 │                    Q      "what did you retype the most this week?"
                 │                              │
                 │                              └─ answer saved to field brain_task
                 │                                 ├─ tag: brain-answered
                 │                                 ├─ notify Ryan in Live Chat
                 │                                 ├─ DM 3  hand the answer back + route
                 │                                 │        to YouTube and Skool
                 │                                 │
                 │                                 └─ +20h  DM 4  the community follow up
                 │                                          │     (last automated send)
                 │                                          └─ day 3, Ryan sends DM 5 by hand
                 │                                                from Live Chat, Human Agent
                 │
                 ├─ no tap after 1 hour  ──> Nudge 1
                 ├─ no tap after 20 hours ──> Nudge 2   (last one inside the 24h window)
                 └─ still nothing         ──> stop. Tag brain-cold. No further sends.
```

---

## 3. Build order in ManyChat

**Step 1. New Automation, name it `IG · BRAIN · Business Brain carousel`.**

**Step 2. Trigger 1, Instagram Comments.**
- Post: select the Business Brain carousel specifically, not "any post".
- Keyword: `brain`, match type **contains** (catches "BRAIN", "Brain!", "brain please").
- Also add negative words if ManyChat offers them, skip if not.
- "Reply to the comment publicly": ON, load the six variants in section 4.
- "Trigger only once per user per post": ON. Peyson's replies double-count him in the comment
  total, that is fine for optics but a second automated DM to the same person is spam.

**Step 3. Trigger 2, Instagram Default Reply / Keyword on DM.**
- Same keyword `brain`, contains. This catches people who saw the carousel, did not comment,
  and DM'd the word instead. Costs nothing, catches real intent.

**Step 4. Trigger 3, Story Reply, keyword `brain`.**
- Only if the carousel gets a story repost with the keyword call-out. Optional.

**Step 5. Custom fields to create first** (Settings > Fields):
- `brain_task` (text), their answer to the one question.
- `brain_source` (text), set to `carousel-02-business-brain`, so later keywords stay separate.

**Step 6. Tags to create first:**
`brain-requested`, `brain-delivered`, `brain-answered`, `brain-invited`, `brain-cold`, `brain-hot`

**Step 7. Build the message sequence** using section 5 verbatim.

**Step 8. Test on a second IG account before the post goes live.** Comment the keyword from
that account, walk the whole flow, confirm the link renders and the question saves to the
field. A broken flow on a post that is already getting comments cannot be un-sent.

---

## 4. Public comment replies, rotate all six

Load every one of these into the comment-reply action. Instagram down-ranks accounts that
post the identical string dozens of times under one post.

```
Sent it over 🧠
Just sent it
In your DMs now
Sent. If you don't follow me it lands in your message requests
Sent 🧠 check your requests folder if you don't see it
Just sent, check DMs
```

No link in a public comment, ever. Two of the six mention the requests folder on purpose:
non-followers do not get the DM in their main inbox and will never see it otherwise.

---

## 5. The messages, verbatim

Instagram caps a DM at 1,000 characters. Every message below is under it. **Re-count if you
edit anything,** Instagram truncates silently rather than warning.

### DM 1, the opener

```
Hey, appreciate you commenting.

Short version: my Business Brain is one folder. Claude reads it before it writes anything, so
I never re-explain my market, my brokerage, my fee or my voice again.

You get the folder structure and the actual CLAUDE.md I run.

Tap below and it's yours.
```

Buttons (quick replies):
- `Send it` → goes to DM 2A
- `What's a CLAUDE.md?` → goes to the explainer below, which ends at DM 2A

### Explainer branch, "What's a CLAUDE.md?"

```
It's one plain text file at the top of the folder. Claude reads it first, every single time,
before it writes a word.

Mine says who I am, what market I work, what good output looks like, what it must never do,
when to stop and ask me, and how I judge the result.

Written once. Read forever. That's the whole trick.

Sending you mine now.
```

Then continues to DM 2A automatically.

### DM 2A, the structure

```
THE SETUP

One folder. Everything Claude needs to be useful lives in it.

business-brain/
  CLAUDE.md          the rules, read on every run
  clients/           one folder per client
  listings/          one folder per address
  skills/            the tasks you do more than twice
  market/            your comps, your neighborhoods, your numbers

WHAT GOES WHERE

Clients and listings hold the facts: the executed contract, the dates, the comps, the notes.
Claude reads the folder instead of asking you to remember.

Skills hold the repeats. Listing description, CMA, escrow emails, weekly seller update. Each
one is a prompt you wrote once and now run with a single word.
```

### DM 2B, the CLAUDE.md

```
THE ONE FILE THAT DOES MOST OF THE WORK

CLAUDE.md at the root, six sections. I use BROKER:

Business, who you are, your market, your brokerage
Range, what you want Claude touching and what you don't
Output, what good looks like, your voice, your format
Keep out, the hard nos, the things it must never write
Escalation, when it stops and asks you instead of guessing
Results, how you judge whether the output was any good

Six sections. Written once. Read on every single run.

Mine has one line that saves me more time than the rest combined: never use em dashes. I said
it once eight months ago and I have not fixed one since.
```

### DM 2C, the link

```
Here it is, the folder structure and my CLAUDE.md, no strings.

[BRAIN_ASSET_URL]

Don't build it for a future deal. Build it for the thing you're most behind on right now. The
next deal inherits the whole thing for free.
```

### The question, a ManyChat "User Input" step, text, saves to `brain_task`

```
One question so I point you at the right thing.

What's the task you retyped the most this week?
```

Skip button: `Just browsing` → tag `brain-delivered`, end flow, no follow-ups.

### DM 3, sent automatically once they answer

```
That's the one to turn into a skill first. Write it down once the way you'd explain it to a
new assistant, save it in skills/, and you never type it again.

Two places I go deeper, both free to look at.

I build these on camera, on real files, on YouTube. [YT_URL]

And the community is where the templates live and where we build these on members' actual
deals. https://www.skool.com/the-leveraged-agent

Start with the video. If it clicks, come say hi in the community.
```

### DM 4, the community follow up, 20 hours after their answer

This is the ask. DM 3 gave them the next step and dropped both links in passing. DM 4 does one
job and only one job: it tells them what The Leveraged Agent actually is and invites them in.
Sent 20 hours after their reply, which is inside the window their reply reopened.

```
One more thing and then I'm out of your inbox.

The folder I sent you is Level 0 of what I teach. The Leveraged Agent is the community where
the rest of it lives: the skills I actually run, the CLAUDE.md I actually use, and the level by
level build from an empty folder to a business that runs itself.

It's free to join and look around.

https://www.skool.com/the-leveraged-agent

If you join, post the task you just told me about. That's how you get the fastest answer in
there, including from me.
```

Variant, if they tapped `Just browsing` and never answered the question:

```
One more thing and then I'm out of your inbox.

That folder is Level 0 of what I teach. The Leveraged Agent is the community where the rest
lives, the skills, the CLAUDE.md, and the level by level build from an empty folder to a
business that runs itself.

Free to join, free to look around.

https://www.skool.com/the-leveraged-agent
```

Then tag `brain-invited` and **stop the automation.** Whatever happens next is Ryan, by hand.

### DM 5, day 3, sent BY HAND from Live Chat

Not automated. This one goes out under ManyChat's Human Agent tag, which is what the tag is
for: a real person writing a real reply. Ryan sends it from Live Chat to anyone tagged
`brain-hot`, referencing their actual answer. Template only, rewrite it every time.

```
Hey, following up on [their task]. Did you get a chance to put it in the folder?

If you did and it worked, come post it in the community, that exact win is what the rest of
them are stuck on. If you didn't, tell me where it snagged and I'll walk you through it.

https://www.skool.com/the-leveraged-agent
```

Nobody who is not tagged `brain-hot` gets a day 3 message. Do not batch this, do not template
it word for word across ten people, and do not send it to anyone who never replied.

### Nudge 1, 1 hour after DM 1, only if the button was never tapped

```
Still want it? Tap Send it above and I'll fire it over.
```

### Nudge 2, 20 hours after DM 1, only if still no tap

```
Last nudge on this, then I'll leave you alone. The folder structure and the CLAUDE.md are
sitting here whenever you want them.
```

Then tag `brain-cold` and stop. Do not build a third.

---

## 6. Timing and the 24 hour window

Instagram gives you a **24 hour standard messaging window** from the person's last interaction.
Everything above fits inside it on purpose: Nudge 2 at 20 hours is the last automated send.

- When someone replies at any point, the window resets from their reply.
- ManyChat's **Human Agent** tag extends the window to 7 days for a genuine human response.
  Use it only for real one to one replies from Ryan, not to sneak another broadcast in. Abusing
  it is how accounts lose messaging access.
- Anyone who never taps and never replies is done at 24 hours. Do not re-engage them through
  automation. They can be worked manually later off the `brain-cold` tag.
- **DM 4 is the last automated message in this flow**, and it is timed off their reply, not off
  DM 1, so it lands inside the window their reply reopened. If they answered and then went
  quiet, DM 4 still delivers. If they never replied at all, they never reach DM 4.
- **DM 5 on day 3 is outside the standard window on purpose.** That is the one legitimate use of
  Human Agent here: Ryan personally writing to someone who talked to him. Sending an automated
  sequence under that tag is how accounts lose messaging access.

---

## 7. Where Ryan actually shows up

The automation gets them the file. **The conversion is the human reply to `brain_task`.**

Set a ManyChat notification on the `brain-answered` tag. Once a day, Ryan opens Live Chat and
answers every new one personally, in his own words, referencing their specific answer. That
reply is the entire point of the funnel. This is the same doctrine as `../../../Skool-Welcome-DM.md`:
ask one question, hand their own answer back, then make the ask.

Tag `brain-hot` by hand on anyone whose answer names a real, specific, repeated task. Those
are the Skool invites worth sending individually.

---

## 8. Guardrails

- **No link in DM 1.** Not negotiable. The link goes out after the button tap, which is the
  interaction that tells Instagram this is a real conversation.
- **No link in any public comment.**
- **One automated DM sequence per person per post.**
- **No income claims, no guarantees, no pricing, no legal or lending advice.** Same standard as
  the TC replies. Everything above is compliant as written.
- **Leveraged Agent branding only.** No Rose Homes LV, no Real Broker, this is the coaching
  brand talking to agents.
- **No em dashes** in any message, including ones Ryan writes by hand in Live Chat.
- If Instagram starts bouncing sends or ManyChat reports delivery failures, stop the automation
  and let the backlog drain before restarting. Do not increase send volume to compensate.

---

## 9. What to watch, first 7 days

| Number | Where | What it tells you |
|---|---|---|
| Comments containing the keyword | IG post | whether the CTA slide works at all |
| DM 1 delivered / comments | ManyChat | how many are non-followers stuck in requests |
| Button tap rate on DM 1 | ManyChat | whether the opener earns the second message |
| `brain_task` answers / deliveries | ManyChat | the only number that predicts Skool joins |
| Skool joins tagged to the week | Skool | the actual return |

The Peyson benchmark is 12x comments on a carousel with a keyword CTA versus one without. That
is his account at his size, it is not a forecast for this one. Measure this post against Ryan's
own last five carousels, not against his.

---

## 10. Keyword hygiene going forward

Rotate the keyword per post, one word, in quotes, on its own line, last line of the caption.
The keyword is what labels the DM thread, so `BRAIN` should only ever mean the Business Brain
asset. When the next carousel ships, give it its own word and its own flow. Never reuse a
keyword for a different offer, the tags stop meaning anything the moment you do.

Live keywords so far:
- `TC` → transaction coordination folder (currently manual saved replies, migrate to ManyChat)
- `BRAIN` → Business Brain folder structure + CLAUDE.md (this flow)

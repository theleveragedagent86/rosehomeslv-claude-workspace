# The Business Brain

The folder my whole real estate business runs out of, and the CLAUDE.md that makes it work.

From Ryan Rose | The Leveraged Agent

---

## Why this exists

Every prompt you write starts from zero. It does not know your market, your brokerage, your
fee, your voice, or the deal you were working on yesterday. So you re-explain all of it, every
time, and you call that using AI.

A Business Brain fixes that. It is one folder. Claude reads it before it writes anything.

Prompts are rented. A Business Brain compounds.

---

## The rule

**One folder. Everything Claude needs to be useful lives in it. Facts live in files, not in
your head, and never in two places at once.**

If a name, a date or a number exists in two files, one of them is already wrong.

---

## The structure

```
business-brain/
├── CLAUDE.md                  the rules, read on every single run
├── market/
│   ├── neighborhoods.md       the areas you actually work
│   ├── numbers.md             your averages, your DOM, your price bands
│   └── vendors.md             lender, title, inspector, photographer, stager
├── clients/
│   ├── buyer-lastname/
│   │   ├── profile.md         what they want, what they said, what they can spend
│   │   └── notes.md           every conversation, dated
│   └── seller-lastname/
│       ├── profile.md
│       └── notes.md
├── listings/
│   └── 123-example-st/
│       ├── property.md        the facts: beds, baths, sqft, HOA, lot, year
│       ├── documents/         executed contract, disclosures, reports
│       └── timeline.md        dates pulled off the contract, not off memory
└── skills/
    ├── listing-description.md
    ├── cma.md
    ├── escrow-emails.md
    └── weekly-seller-update.md
```

Six folders. That is the entire system.

**market/** is the part almost nobody builds and it is the part that makes the output sound
like you instead of like a robot in a city it has never visited.

**clients/ and listings/** hold facts only. Claude reads the folder instead of asking you to
remember.

**skills/** holds the repeats. One file per task you have done more than twice.

---

## CLAUDE.md, the one file that does most of the work

This file sits at the root. Claude reads it first, every time, before it writes a word. Six
sections. I use BROKER so it is impossible to forget one.

**B, Business.** Who you are, what market, what brokerage, what license state.
**R, Range.** What you want it touching and what you do not.
**O, Output.** What good looks like. Your voice, your format, your length.
**K, Keep out.** The hard nos. The things it must never write, ever.
**E, Escalation.** When it stops and asks you instead of guessing.
**R, Results.** How you judge whether the output was any good.

Paste this in, fill the brackets, delete what does not apply.

```markdown
# CLAUDE.md

## Business
I am [name], a licensed real estate agent with [brokerage] in [city, state].
I work [neighborhoods]. My typical client is [describe them in one sentence].
My license number is [number] and it goes on anything public.

## Range
You help with: listing copy, market analysis, client emails, transaction
deadlines, social content, follow up sequences.
You do not touch: pricing advice given as fact, contract interpretation,
anything that needs my broker to sign off.

## Output
Write the way I talk. Short sentences. Sixth grade reading level.
No jargon, no "premier", no "luxury opportunity", no exclamation points.
Never use em dashes. Use commas or periods.
Default length is short. If I want long I will ask.

## Keep out
Never invent a price, a square footage, a school rating, an HOA amount or a
builder incentive. If you do not have it, write NOT FOUND and stop.
Never make an income claim or a guarantee.
Never give legal or lending advice.
Never put a client's phone number or email in anything that leaves my computer.

## Escalation
Stop and ask me when: a number is missing, a date does not match the contract,
the request needs my broker, or you are about to guess at anything factual.
Asking me is always better than guessing.

## Results
Good output is something I can send without editing. If I have to rewrite the
first sentence, it was not good. Match the examples in skills/, not your
instincts.
```

The single highest value line in mine is the em dash rule. I wrote it once and I have not
fixed one since.

---

## Skills, the part that saves the hours

A skill is a prompt you write once and then run with a single word. Anything you have done
more than twice belongs in `skills/`.

A skill file needs three things and nothing else:

1. **When to use it.** One sentence.
2. **What it needs from me.** The inputs, listed.
3. **What good looks like.** One real example of your own past work.

That third one is the whole trick. Do not describe your voice, show it. Paste in the best
listing description you ever wrote and say "match this".

**Start here, in this order:**

- `listing-description.md` because you write one every time and hate every one of them
- `weekly-seller-update.md` because it is the thing you skip when you get busy
- `escrow-emails.md` because the deadlines are the same on every deal
- `cma.md` last, because it needs your market folder built first

---

## Where to start today

Do not build this for a future deal.

Pick the one task you retyped the most this week. Make a folder called `business-brain`, put a
`CLAUDE.md` in it with the six sections above, and write that one task into `skills/`.

That is it. That is Level 0. Every deal after this one inherits the whole thing for free, and
the folder gets smarter every week because every deal adds to it.

---

## Where this goes next

The folder you just built is the first layer. The ladder from here looks like this:

**Level 1.** The CLAUDE.md written properly, on BROKER, so the output stops needing edits.
**Level 2.** Client and listing folders, so Claude stops asking you for facts you already have.
**Level 3.** Your first three skills, running on real files.
**Level 4.** A memory system, so last month's deal informs this month's.
**Level 5 and up.** Listing launch, transaction coordination, open houses, landing pages,
content, and the routines that run while you are asleep.

Same folder the whole way. Every level adds a layer to it.

---

## The Leveraged Agent

I teach this whole ladder in a free community called **The Leveraged Agent**. It is agents
building the same folder on their own deals, plus the actual skill files, the CLAUDE.md I run,
and the level by level build.

**Community, free to join:**
https://www.skool.com/the-leveraged-agent

**YouTube, where I build these on camera on real files:**
https://www.youtube.com/@theleveragedagent

**Instagram:**
https://www.instagram.com/the.leveraged.agent/

If you join, post the task you were retyping this week. That is the fastest way to get a
straight answer in there, including from me.

---

Ryan Rose | The Leveraged Agent

Nothing in this document is legal, tax, lending or investment advice, and nothing here is an
income claim or a guarantee of any result. Check your own brokerage's policies and your state's
advertising rules before publishing anything AI helped you write. You are still the licensee.

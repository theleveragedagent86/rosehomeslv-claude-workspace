# Transcript: Level 7: Security & Compliance

_Section: 🥇 Hermes Agent · Source file: `Level 7.txt`_

---

[00:00:00] Hey there, beautiful AI automator and
[00:00:02] welcome to level seven where we're going
[00:00:04] to be talking about security and
[00:00:05] compliance. So this is about when you're
[00:00:07] using Hermes agent, how do you keep
[00:00:09] everything super duper secure and locked
[00:00:12] up so you can have peace of mind? And
[00:00:13] then also if you're selling, if you're
[00:00:16] doing commerce, if you're working with
[00:00:17] businesses, what are the sorts of things
[00:00:19] that we need to think about from a
[00:00:20] compliance point of view? We're going to
[00:00:21] go into all of it. I have my spicy
[00:00:23] water. I have my beverages. We're going
[00:00:25] to have a great time. Hopefully, you've
[00:00:26] got the coffee and you're ready for a an
[00:00:28] awesome conversation around this sort of
[00:00:30] stuff. So, let's go ahead and take a
[00:00:32] look at what we're doing and how
[00:00:33] everything is flying with this. So, the
[00:00:35] first thing to understand actually is
[00:00:37] going to be around the front. And the
[00:00:38] idea with this is that think of it, you
[00:00:40] know, the analogy I've got here is like
[00:00:41] a hospital, right? You wouldn't have
[00:00:43] visitors in the lobby wandering into the
[00:00:45] surgical theater. It probably wouldn't
[00:00:47] be appropriate. They probably would get
[00:00:48] somebody injured or worse if that
[00:00:50] happened. So the idea is that you think
[00:00:52] about things when you're using Hermes
[00:00:54] agent that we actually lock and restrict
[00:00:57] things by design. We've spoken before
[00:00:59] about the principle of least access. In
[00:01:02] other words, that any AI system that we
[00:01:04] build, we actually only give it the
[00:01:08] minimum number of tools, capabilities,
[00:01:10] and accessibilities that it actually
[00:01:12] needs. I can tell you in building glider
[00:01:14] my speech to text startup even our team
[00:01:16] uh it's like does everybody need access
[00:01:19] to this super important database and if
[00:01:21] the answer is no it's easier just not to
[00:01:23] have it so principle to think about here
[00:01:25] is what we call locked by design it's a
[00:01:27] very very important concept and if you
[00:01:29] take replet for example replet's agent
[00:01:31] deleted a production database during a
[00:01:34] code freeze can you believe it so
[00:01:36] basically lin told the agent 11 times in
[00:01:38] all calves do not touch production it
[00:01:41] deleted live records for 1,26
[00:01:46] executives anyway generated 4,000 fake
[00:01:48] users to cover the gap and claimed roll
[00:01:50] back was impossible which it wasn't the
[00:01:52] manual roll roll back actually worked
[00:01:54] and the agents own postmortem it
[00:01:56] panicked instead of thinking now here's
[00:02:00] the thing as these models get better
[00:02:02] this happened in July 2025 so you're
[00:02:04] talking like maybe haiku 3 or something
[00:02:06] but these things aren't impossible so we
[00:02:09] don't want to give models the keys to
[00:02:10] the kingdom yet until we're
[00:02:11] overwhelmingly certain in a couple years
[00:02:13] time there will just be a level but even
[00:02:15] still we don't by system design it
[00:02:18] shouldn't be possible and this idea of
[00:02:20] like it should not be possible if this
[00:02:23] model is malevolent or if this model has
[00:02:25] been poisoned and corrupted and taken
[00:02:28] information to release some information
[00:02:29] it still should not do it so I want you
[00:02:31] to think about everything that you you
[00:02:33] build with Hermes agent and your systems
[00:02:35] in four levels so we have tier one which
[00:02:37] is looking at stuff searching for stuff
[00:02:40] summarizing stuff, reading files,
[00:02:42] checking calendars, browsing documents.
[00:02:44] Um, we allow that automatically. We
[00:02:46] don't care about that. It doesn't
[00:02:47] matter. Worst case scenario, we waste
[00:02:49] tokens. Now, if you're doing oorthth, if
[00:02:52] we're using the chat GPT subscription,
[00:02:54] if we're using our gro subscription,
[00:02:56] doesn't really make a difference because
[00:02:57] it's on our subscription. And if we're
[00:02:59] using open router, we have model limits.
[00:03:01] So, we're okay though. So, this is just
[00:03:04] read stuff. We don't care. Tier 2 is
[00:03:07] reversible stuff. So it's drafts, it's
[00:03:09] editing GitHub repos, which are version
[00:03:12] controlled, which means that if it just
[00:03:14] sends it to Spanish, well, we can just
[00:03:15] zip it straight back. Every update and
[00:03:18] publish to GitHub is like a saved file
[00:03:21] and we have an infinite number of saved
[00:03:22] files we can go through. We don't care
[00:03:23] about it. Everything's an undo. Back up
[00:03:26] fully heals. We allow that and we log
[00:03:28] what it's done. Then we have tier three,
[00:03:30] which is external stuff. So sending
[00:03:32] stuff, posting stuff, spending things,
[00:03:35] emails, payments, deploys, anything any
[00:03:37] other human sees, undo does not exist in
[00:03:40] the real world. So it has to ask us
[00:03:42] first. And finally, the irreversible
[00:03:44] stuff, deleting, dropping, forcing,
[00:03:46] pushing, you know, production
[00:03:48] credentials, the replicier stuff, we
[00:03:50] deny or have human access to do that. So
[00:03:53] think about what you do from a safety
[00:03:54] and compliance point of view across
[00:03:56] these four levels. Really, really
[00:03:57] important to sort of understand that. So
[00:03:59] I wanted to include one rule for this
[00:04:01] entire chapter. So if you think about
[00:04:03] prompts as they're not as permissions.
[00:04:05] So if you think about the example of
[00:04:06] replet right, I think you even got it
[00:04:07] down here. This idea that it was told 11
[00:04:10] times do not do this, do not do this in
[00:04:12] all caps and it still did the thing. So
[00:04:14] permissions are walls around it. If the
[00:04:17] agent can't touch something, plan for
[00:04:18] the day it does. The decision lives in
[00:04:20] code, not the prompt. In other words,
[00:04:22] just because you say don't touch the big
[00:04:23] important production database doesn't
[00:04:25] mean that it will even with our best of
[00:04:27] intentions. Really, really important.
[00:04:28] So, what is the so what from this? Take
[00:04:30] 10 minutes, list what your agent can
[00:04:32] currently touch and stamp each item tier
[00:04:34] 1 to four. Anything in tier three to
[00:04:36] four that isn't touched behind the gate
[00:04:37] is your homework. And if you want to,
[00:04:39] you can actually just give it control A
[00:04:41] this entire presentation. Ctrl + C, drop
[00:04:43] it in Hermes agent and say, I want to go
[00:04:45] through this and come up with an action
[00:04:46] plan of how I can make this safer and
[00:04:47] more compliant
[00:04:49] or just copy that section. That leads us
[00:04:51] nicely onto the wall, the always gate
[00:04:53] list. So five categories that always ask
[00:04:56] a human no matter how sure the model is.
[00:04:58] Deploy comes money delete permissions
[00:04:59] enforced by hook that runs before the
[00:05:01] tool does. Think of it like a teller at
[00:05:03] a bank. So in the UK we just say I don't
[00:05:06] know person that works behind the bank.
[00:05:08] The teller can't be charmed, rushed or
[00:05:10] even fooled and it doesn't matter. The
[00:05:11] vault is on a time lock. The teller
[00:05:13] can't override it. That's probably the
[00:05:15] best analogy that it doesn't matter how
[00:05:18] incompetent the teller is. She cannot or
[00:05:21] he cannot literally open up the vault
[00:05:23] with the credentials. Think of this like
[00:05:25] the the nightmare files is a good
[00:05:26] example here. And this was what happened
[00:05:28] with um Amazon. So a hacker slipped a
[00:05:31] pull request into the open-source VS
[00:05:34] Code extension containing plain English
[00:05:35] instructions, clean the system to near
[00:05:37] factory states, delete files, EC2 and
[00:05:40] S3. It shipped the official release to
[00:05:42] around a million installs. A syntax
[00:05:45] error pure look stopped it from running.
[00:05:46] The payload wasn't code. It was actually
[00:05:48] a prompt. And this happened in July
[00:05:50] 2025. You probably remember that. If it
[00:05:52] hadn't happened, would have had roughly
[00:05:54] a million installs going absolutely
[00:05:55] crazy. So, let's talk about approval
[00:05:57] gates and kill switches. So, propose
[00:05:59] then confirm for anything consequential.
[00:06:01] A window so nothing blocks forever and
[00:06:03] three ways to stop the machine midun.
[00:06:06] So, you know what it is before because
[00:06:07] nothing you don't basically you don't
[00:06:08] want something to start and they
[00:06:10] realize, oh, damn, it's like editing the
[00:06:12] wrong thing. So, you can think of it
[00:06:13] like a dead man switch. Train drivers
[00:06:15] hold the handle the whole journey. They
[00:06:16] let go, they get asleep, they get
[00:06:17] distracted, they're gone, and the train
[00:06:19] will stop by itself because if the if
[00:06:22] the person behind the wheel falls
[00:06:23] asleep, if you don't do the right thing,
[00:06:25] it stops by default. That's why they
[00:06:27] call it a dead man switch. It's really
[00:06:28] huge in engineering um and factories,
[00:06:30] for example. So, here's a use case, and
[00:06:33] I wanted to include use cases just so
[00:06:34] you know, this isn't just theory. This
[00:06:36] stuff actually happens. So, Gemini CLI
[00:06:38] destroyed a user's files, then it
[00:06:40] confessed them. So, it asked to asked to
[00:06:42] reign, reorganize a folder. Gemini
[00:06:45] silently failed. It never checked. It
[00:06:47] then moved the user's files into
[00:06:49] directory that didn't exist on Windows
[00:06:51] and then overwrote them one by one into
[00:06:52] a single file. It's closing words. I
[00:06:55] have failed you completely and
[00:06:57] catastrophically. Um those are words to
[00:06:59] live by I think. So maybe he stopped
[00:07:00] using Gemini so much after that point.
[00:07:02] Now what was the root cause? Destructive
[00:07:04] commands executed against the model's
[00:07:06] imagined file system with no verify
[00:07:08] steps and no backup. So you can see like
[00:07:10] if the model just for some reason thinks
[00:07:12] it's the way it should be and it isn't
[00:07:14] it will go ahead and do that which is
[00:07:16] absolutely wild. So what we want to do
[00:07:18] is we propose then confirm which is
[00:07:19] actually come back with an action plan.
[00:07:22] Tier three plus action plans produce a
[00:07:24] plan not an act here are three emails
[00:07:26] I'll send the file I delete the
[00:07:28] differential I'll push the diff push you
[00:07:30] approve the plan the machine executes
[00:07:32] against it exactly expired and blocked.
[00:07:34] to give every approval request a 30inut
[00:07:37] window. If it's unanswered, the action
[00:07:38] is dropped and logged so it doesn't
[00:07:40] continue to do by itself. It's never
[00:07:42] auto approved. And then three kill
[00:07:44] switches. So stop the gateway service.
[00:07:45] The agent falls silent anywhere at once.
[00:07:47] Revoke the model API key. No key, no
[00:07:48] brain instantly or pull the box off tail
[00:07:50] skull ring if you're using that. Now,
[00:07:52] Hermes agent has just dropped a feature
[00:07:55] that wants to get the right balance
[00:07:56] because at the same time we don't want
[00:07:58] to give Hermes agent like a job and then
[00:08:00] basically it just never actually does it
[00:08:02] because like you have to constantly be
[00:08:04] there tapping like we don't want that
[00:08:05] either. So what they've done is
[00:08:06] introduced a second model if you update
[00:08:08] to the latest version and effective what
[00:08:10] it'll do it will if it's like it will
[00:08:12] assess like is this really important and
[00:08:14] does it need a sign off and if so it
[00:08:16] will but if not it and the first model
[00:08:18] has flagged it incorrectly it will pass
[00:08:20] it for you automatically meaning you get
[00:08:22] a good balance of safety and security
[00:08:24] but also saving you time which is really
[00:08:25] really important to bear in mind. So the
[00:08:27] idea here what we can take away from
[00:08:29] this is the verify rule. So any step
[00:08:31] that changes state must be followed by a
[00:08:33] step that proves that change happened.
[00:08:36] List a directory after mkdir. Read the
[00:08:39] row after the insert. Curl the page
[00:08:40] after deploy. Bake it into your prompts
[00:08:42] and skills. Act then verify then
[00:08:44] continue. Chapter 5's proof done of
[00:08:46] contract with the rule. Was this rule
[00:08:48] wearing a suit? So that was the whole
[00:08:49] thing we talked about with contract uh
[00:08:51] you know contract um you know proof of
[00:08:53] contract the contract completions. If I
[00:08:55] could speak that'd be fantastic, right?
[00:08:58] So what do we do about it? run the three
[00:09:00] kill switches at once today with the
[00:09:01] timer. If stopping your agent takes more
[00:09:02] than 60 seconds, you don't have a kill
[00:09:04] switch. You have a hope, a prayer, a
[00:09:06] dream. Um, so use these kill switches,
[00:09:09] use these strategies and techniques when
[00:09:12] you're working with big important
[00:09:13] production things. Verify that it can do
[00:09:15] it. So if I'm working with a big
[00:09:16] database, I'll actually just make sure
[00:09:18] that it does work and it is verified
[00:09:20] before I do any big big changes. Um,
[00:09:23] then that takes us on to spend and loop
[00:09:24] protection. So loops plus usage based
[00:09:28] pricing plus billing lag. That's exactly
[00:09:30] how agents burn hundreds and hundreds of
[00:09:34] dollars. So you want a cap upstream to
[00:09:36] basically um stop that. You can think of
[00:09:38] this like a fuse box. So you don't want
[00:09:40] all the wiring all night and hope it be.
[00:09:42] You don't watch your wiring all night,
[00:09:43] right? Hoping that it behaves. There's a
[00:09:45] breaker that trips 13 amps in the US, I
[00:09:48] believe, mechanically. So whether you're
[00:09:49] asleep or on a beach, circuit breakers
[00:09:51] are named exactly for this. And we c we
[00:09:53] have these in open router. We have them
[00:09:55] in various different things. Let me give
[00:09:57] you a nightmare example of this. A hello
[00:10:00] world test ran to $72,000
[00:10:04] in two hours.
[00:10:06] Yes, that happened. Startup Milky Way
[00:10:08] deployed a test to Google Cloud Run with
[00:10:10] a $7 budget. Infinite recursion and
[00:10:13] 1,000 max instances generated 116
[00:10:17] billion database reads peaking near a
[00:10:20] billion reads a minute. The billing
[00:10:22] dashboard lagged around 24 hours. By the
[00:10:25] time that any number moved, it was
[00:10:26] $72,000.
[00:10:28] Google did forgive it. The physics
[00:10:30] didn't change. That is preposterous. The
[00:10:34] root cause a loop with no hard stop and
[00:10:36] a meter that reports yesterday. Agent
[00:10:38] era ruins a story. $1,800 weekend four
[00:10:40] figure overnight claude loops are
[00:10:42] reported constantly. That's not great.
[00:10:45] How do we solve it? Well, we have open
[00:10:47] router key limits and I'm going to show
[00:10:48] what that looks like right now. So let's
[00:10:50] open up open together and have a look at
[00:10:52] some of the key limits that I've got. So
[00:10:53] let's come over to I think we just go
[00:10:55] over to models on this. Let me go ahead
[00:10:57] and I've got this signed up and we'll
[00:11:00] have a look. And if I can't log in
[00:11:01] because I don't have everything on this
[00:11:03] computer, but if come to get API key, I
[00:11:05] should be able to have a good look for
[00:11:06] you. But you can see the idea here. The
[00:11:08] idea is that when I build something, I
[00:11:09] think about what am I comfortable
[00:11:11] spending on uh this month for that
[00:11:13] particular thing. And you can set it
[00:11:14] with literally one click inside open
[00:11:17] router. It's dead easy to do that. We
[00:11:19] can do this on anthropic console even
[00:11:21] include code. It's like what's the
[00:11:23] spending limit that you're happy with me
[00:11:24] using and you can set that and hardwire
[00:11:26] that. It's very very easy. Open air
[00:11:28] console budget limit is now notification
[00:11:30] only. Requests keep flowing past it.
[00:11:31] Only real stop prepaid credits auto
[00:11:34] recharge off. That is what I do. I do
[00:11:36] not give it a what I would call a blank
[00:11:38] check. I I don't have the confidence in
[00:11:41] the models that they still won't go
[00:11:42] crazy. So we should make it impossible.
[00:11:45] And a little hack as well.
[00:11:47] I connect it to a card with a capped
[00:11:49] amount of money such that if it tries to
[00:11:51] bill it, it just won't go through
[00:11:53] because it's not possible for it to go
[00:11:55] through. So that's how I manage it. I
[00:11:56] even bank it. I even cap it on the
[00:11:58] financial side, not just the system side
[00:12:00] either. So you're protected at all
[00:12:02] times. The pattern in every bloat story,
[00:12:04] the provider dashboard has some kind of
[00:12:06] lag. So you don't see what's happening.
[00:12:07] You don't get any alert and you didn't
[00:12:09] cap it. So make sure that you're capping
[00:12:11] all but now that is a very very
[00:12:12] important one to do. Uh, and again,
[00:12:15] before tonight finishes, make sure
[00:12:17] everything is capped. Um, what would you
[00:12:19] generally shrug off in terms of losing?
[00:12:21] You don't want it to be $700 overnight
[00:12:23] or potentially even more. Um, then let's
[00:12:25] talk a little about secret management.
[00:12:27] So, your agents folder has every key you
[00:12:29] own. One rule above all, a key that ever
[00:12:30] touches get history is compromised
[00:12:32] forever, no matter what you delete
[00:12:34] afterward. So, if you happen to put a
[00:12:36] key for something you're using and it
[00:12:38] gets through into history, it's there.
[00:12:41] So, it's a tattoo, not a sticky note. A
[00:12:44] sticky note will come off. A key
[00:12:45] committee to get is link inked into
[00:12:47] every single clone of it. It's forked.
[00:12:49] It's cash for you. Scrubbing the
[00:12:50] original doesn't touch copies. You don't
[00:12:52] remove it. You need to retire it to kill
[00:12:54] it. And generally speaking, as a good
[00:12:57] practice, you want to be doing that
[00:12:58] anyway. You don't want to be keeping
[00:12:59] these things for a thousand years. That
[00:13:02] is super duper duper important. Okay.
[00:13:04] Now, what's an example of this? Leaked
[00:13:06] AWS keys are exploited within minutes.
[00:13:09] Unit 42's Electrol campaign launched
[00:13:12] crypto mining on stolen AWS keys within
[00:13:14] 5 minutes of them hitting a public
[00:13:16] GitHub repo. They searched them. They
[00:13:18] crawled them constantly. Honeypot
[00:13:20] studies clock at first abuse at 1 to 2
[00:13:22] minutes and then the agent era encore
[00:13:23] maltbas network. Um left its database
[00:13:28] publicly writable and roughly one and a
[00:13:30] half million agent API tokens readable
[00:13:32] by anyone. No hacking required. So
[00:13:35] that's just something to be aware of,
[00:13:36] not to be scared about, but just to be
[00:13:38] informed and aware of that these things
[00:13:40] exist and this stuff happens. So
[00:13:42] remember, you can fence the folders, get
[00:13:44] ignore, and docket ignore. Perfect for
[00:13:46] that sort of stuff. Block up a door,
[00:13:48] inject store, and when it leaks, you
[00:13:50] rotate it and do that periodically also.
[00:13:52] It's really good practice. So an easy
[00:13:53] quick action if this is something you
[00:13:55] haven't been a million miles ahead of is
[00:13:57] actually just to rotate everything
[00:13:58] today, tonight. Grab that coffee, sit
[00:14:00] down, and just delete everything.
[00:14:02] organize your desktop, have a little bit
[00:14:04] of an admin day, your life will thank
[00:14:06] you for it, and then you can start again
[00:14:08] from scratch. Delete repos you don't
[00:14:09] use, just go ahead and just cleanse
[00:14:11] everything that's not being used right
[00:14:12] now. And even chat to Hermes agent and
[00:14:14] Claude about identifying potential
[00:14:16] vulnerabilities that you can get ahead
[00:14:18] of in time. Um, now let's talk about
[00:14:20] observability and cost governance. So,
[00:14:22] every disaster in this chapter left a
[00:14:24] trail for hours before anybody looked at
[00:14:25] them. You don't need to watch the
[00:14:27] machine. You need the machine that
[00:14:29] watches the machine. So, think of this
[00:14:30] like the smoke detector for your Hermes
[00:14:32] agent and your builds. Nobody stares at
[00:14:34] the kitchen all night. The detector does
[00:14:35] and it screams at the first wisp, not
[00:14:38] when the curtains are gone the second
[00:14:39] that any kind of smoke appears. So, what
[00:14:42] happened here on the night the sixth
[00:14:44] episode of the nightmare files? The loop
[00:14:46] nobody saw until the invoice. The agents
[00:14:48] era recurring a small print. Um, check
[00:14:50] this out. A claude code session left
[00:14:52] checking for updates overnight
[00:14:54] reportedly ran to $6,000.
[00:14:56] A sub agent recursion bug reportedly
[00:14:59] burnt 4 million tokens in under five
[00:15:01] minutes. A lang chain agent looped
[00:15:03] 14,000 redundant tool calls for $437.
[00:15:07] Single source stories, so treat the
[00:15:09] exact numbers as like anecdotes of
[00:15:10] course, but the shape repeats on every
[00:15:12] single forum and it can happen very very
[00:15:15] quickly. So there's a couple of things
[00:15:16] that you can use for this. One is
[00:15:17] helone. Another is langu. So helone is a
[00:15:20] proxy. Basically change one base URL
[00:15:22] call uh is logged at the wire. tokens
[00:15:24] cost latency per request free to
[00:15:26] self-host the fastest possible answer to
[00:15:28] what did it spend on and what
[00:15:31] how much what's that looking like then
[00:15:33] you got Langfuse again this is open
[00:15:35] source MIT core self-hosted for free
[00:15:36] it's got a generous uh free t call full
[00:15:39] span tracing every step tool call and
[00:15:41] subrun session and when something goes
[00:15:43] weird this is where you find which step
[00:15:44] so think of these as just smoke
[00:15:46] detectors if you will for your your
[00:15:47] bills which are super super duper
[00:15:49] important and again I'll put all this
[00:15:50] sort of stuff down here so you can go
[00:15:51] ahead and check it out uh and have a
[00:15:53] little play play around with it so you
[00:15:54] can see everything that's going on which
[00:15:56] is super helpful. Now this talks back to
[00:15:59] chapter eight right which we're going to
[00:16:00] talk about in a second uh which in terms
[00:16:01] of making money which is very cool but
[00:16:03] governance it's three numbers every
[00:16:04] morning and we're going to talk about in
[00:16:06] chapter eight which basically our 6 a.m.
[00:16:07] brief yesterday spend spend by model and
[00:16:10] the single most expensive run. That's
[00:16:12] great. That's really handy because
[00:16:14] essentially what's happening then is
[00:16:15] you're getting a breakdown of you know
[00:16:17] how much did I actually spend yesterday
[00:16:19] on these specific things so you're never
[00:16:22] caught out. And again, we have that in
[00:16:23] aentic operating system. You can build
[00:16:24] that in there, too. It's very, very
[00:16:26] helpful. Add the providers 75 and 90%
[00:16:29] alerts and cap key from 7.4 underneath.
[00:16:32] 30 seconds a day and a runaway loop
[00:16:34] becomes a weird number at breakfast
[00:16:35] instead of a horror story that runs off
[00:16:38] month end. So, that can be the
[00:16:39] difference between a 1x and a 30x if
[00:16:42] you're not careful. So, what? Add the
[00:16:44] proxy line this week and put three
[00:16:46] numbers in your morning brief. Find and
[00:16:47] kill the runaway burn stops before it
[00:16:49] becomes something much more. And then
[00:16:51] we're going to touch briefly here on the
[00:16:52] privacy and the law. So here's where it
[00:16:55] gets very very interesting. So the
[00:16:57] moment your agent touches other people's
[00:16:58] data, clients could be callers, could be
[00:17:00] patients, three bodies of law enter the
[00:17:03] deal and the arrangement. So think of
[00:17:04] this like doctor's office rules. A
[00:17:07] doctor doesn't memorize every statute.
[00:17:08] They follow office rules built by people
[00:17:10] who did. What gets recorded, what gets
[00:17:13] shredded, who signs what. You need
[00:17:14] office rules, not a degree. This is kind
[00:17:16] of when your Hermes agent goes from
[00:17:17] being beyond a personal assistant to
[00:17:20] place where you're cracking deals and
[00:17:22] and various other things. Here's an
[00:17:24] example of the nightmare files for this
[00:17:25] one. Samsung's source code walked into
[00:17:27] chat GPT and Italy build open AAI 15
[00:17:30] million euros.
[00:17:32] Within 20 days of allowing chat GPT,
[00:17:35] Samsung engineers pasted proprietary
[00:17:37] chip source code, yield data, and a
[00:17:39] recorded internal meeting into the
[00:17:41] consumer tier. Three separate leaks
[00:17:43] followed by companywide ban. A year
[00:17:45] later, Italy's regulator finded OpenAI
[00:17:48] 15 million euros over legal basis,
[00:17:50] transparency and breach notifications.
[00:17:52] The lesson cuts both ways. Data in
[00:17:54] without controls and finds out without
[00:17:56] process. So root cause consumer AIT are
[00:17:59] not a data boundary and the AI did it is
[00:18:01] not a defense that regulators accept.
[00:18:04] I'm sure you're going to build big and
[00:18:05] beautiful and wonderful companies and
[00:18:07] you know all your hearts desires and I I
[00:18:08] wish you all the best with that and I'm
[00:18:09] behind you and we're going to help you
[00:18:11] do that. But you have to bear in mind
[00:18:12] that at some point you walk into some of
[00:18:15] these these conversations. So GDPR
[00:18:17] erasia. So this is um especially you
[00:18:19] know one of the frameworks govern for
[00:18:20] example in the EU the right to erasia
[00:18:24] means a client can basically delete
[00:18:25] their data can be gone for 30 days
[00:18:27] doable only if the user memory lives in
[00:18:29] a structure store. So we're becoming GPR
[00:18:31] compliant for example in glider. We are
[00:18:33] and um we're going through the whole um
[00:18:35] system of verification for that and it's
[00:18:37] very very interesting. So, we have these
[00:18:39] systems set up, but I I won't get double
[00:18:42] click into them because some may be just
[00:18:43] different based on where you're at, but
[00:18:44] it's worth just understanding the
[00:18:47] different frameworks of what that means
[00:18:49] for data, how you're capturing customer
[00:18:50] data, how you're capturing businesses
[00:18:52] data. It's super duper important. You've
[00:18:54] got the EU AI act. That's really
[00:18:55] important to be aware be aware of
[00:18:57] because from the 2nd of August 2026, the
[00:18:59] transparency rule applies. You have to
[00:19:00] disclose that users are talking to an AI
[00:19:03] if you're an AI, which is crazy, right?
[00:19:06] If if you're talking to people in Hermes
[00:19:07] agent. So, we need to be clear about
[00:19:08] what's going on there. And I do think
[00:19:10] that's a good thing. Um, but again,
[00:19:11] we're even seeing it on YouTube now. AI
[00:19:13] creators are having to say it's an AI. I
[00:19:16] say this to say that the regulation and
[00:19:17] laws around this are changing all the
[00:19:20] time. And I don't ever want you to get
[00:19:21] caught up. So, you want to be aware of
[00:19:22] what's going on here. So, what a
[00:19:25] regulated client actually asks you for.
[00:19:27] Not magic paperwork. You can now produce
[00:19:29] where data lives. Okay? Really important
[00:19:31] in their own box. Chapter six. Because
[00:19:33] again, your you may be setting these up
[00:19:34] for your clients and they're like,
[00:19:36] "Dude, where's all the data?" And you
[00:19:38] can say right there on your computer or
[00:19:40] if it's on a you know virtual machine
[00:19:42] somewhere, you also want to be able to
[00:19:44] talk about that, where that is, what
[00:19:45] that means, who can reach it, who's on
[00:19:48] the allow list. Tails can touch it. Um
[00:19:50] what other services can do that? How is
[00:19:52] it deleted? Which providers touch it? Uh
[00:19:55] the audit trail chapters you did.
[00:19:57] Honestly, these are all questions you
[00:19:59] get into uh when you start doing big
[00:20:00] business at this level. So adopt these
[00:20:03] three office rules today. Agent
[00:20:06] announcer self on calls when you're
[00:20:07] having that client data only in per
[00:20:09] client stories. Um and obviously I put
[00:20:11] some extra details down there for you.
[00:20:12] I've also included a full 20-minute
[00:20:14] lockdown checklist for you. So you can
[00:20:15] go through this, take them off if you
[00:20:16] want to as you go through to make sure
[00:20:18] you are fully locked in. This will not
[00:20:20] hit page wonders, but this is the stuff
[00:20:23] that really separates the pros from the
[00:20:25] Joe's. I really hope you found this
[00:20:26] module helpful. And in my next one,
[00:20:28] we're going to go through a wonderful
[00:20:29] topic about monetization. Grab that
[00:20:31] coffee and I look forward to catching
[00:20:33] you inside the next training.

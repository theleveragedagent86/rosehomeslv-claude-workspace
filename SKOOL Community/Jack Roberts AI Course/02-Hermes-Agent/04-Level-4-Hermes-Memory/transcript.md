# Transcript: Level 4: Hermes Memory

_Section: 🥇 Hermes Agent · Source file: `Hermes Memory.txt`_

---

Hey there beautiful AI automates and welcome to level four of the Hermes master
class where
 we are going to be going through the one the only what is it memory of course I
 was going
 to do a joke about forgetting but it's that powerful I couldn't even do it so
 what is really
 cool about memory and it's it's one of the things that really separates Hermes
 agent from everything
 else is the fact that it remembers things but not just remembering things it
 has so many different
 bells and whistles and dimensions to it and I'm going to show you how you can
 accelerate that
 and take it to a completely new level but the first thing that you have to bear
 in mind here
 is that a million token context window is not a memory real memory is
 persistent self-intending
 knowledge system system being the operative word here and systems is how we
 think and it's what
 turns a clever tool into an agent who truly knows you what do I mean by that
 well if you ever use
 code code for example it can have a million token context window which is
 around 750,000 words
 that is not that is a short-term working memory and the great like the greater
 the percentage of
 that memory you're using the worse it gets think about like that the more books
 on the shelf the
 more likely they are to fall off if you're shaking them really really important
 concept to understand
 Hermes memory does have a a window a context window but that's only one
 dimension of a multifaceted
 system that we get with Hermes agent so first thing to understand a big context
 is not a memory
 context is like ram on your computer it's fast volatile wipes every run it's
 gone every new
 conversation it's out of him memory is a desk it persists and you page in only
 what you need you
 confuse them and your agent forgets the moment the window closes so think of it
 like a whiteboard
 versus a filing cabinet okay a whiteboard is wiped after every meeting that's
 basically like a chat
 bar like Claude like chat GPT and then Hermes agent is the cabinet that files
 the important
 stuff and then disregards the old files that we no longer need so always
 retains the key stuff
 so you never feel like you're basically explaining yourself every single time
 so we have here if
 you think about this three tiers three levels of memory and i'm going to kind
 of educate you on
 how this memory system works we have the working memory we have the session and
 then we have this
 kind of archive this deep library belong to memory at the bottom so we
 understand context window
 we understand the real memory i've even got websites that are popping up in the
 background
 i'm having a great time which is awesome i've got a video coming out at some
 point soon but
 that's not what we're talking about right now we're talking about memory so the
 idea here is that
 we get lost in the middle and this is why more context isn't necessarily always
 better and the
 idea here is that the lot bigger the context window gets so the more that you
 have those conversations
 it just forgets so this is the idea of context stuffing you might remember i
 flight to
 new york last year to compete in any tense agenda competition and this was one
 of things about
 rag how do you affect to retrieve it context stuffing is one of the worst ways
 um for you to do
 that and actually all the data shows that irrespective of how long they are
 that we want it to be
 accurate we want it to be confidently correct not confidently incorrect which
 they definitely
 can be so what's the so what we're not looking for bigger whiteboard we're not
 looking at context
 window we want an actual memory system now how does it actually remember well
 this is the simplest
 memory system that actually works hermy's real memory is disarmingly plain it
 is actually two
 markdown files it curates itself plus instant full-text search over everything
 that you've ever said
 so it's a diary it rereads each morning every session it opens is its own notes
 about you first
 so you can imagine i haven't got a diary here maybe i should have bought one
 but imagine for
 example this is your diary you ask him is a question just flicks through the
 diary this is
 what i know isn't really doing that because it's super smart super intelligent
 but effectively
 that's kind of how actual works so i can actually show you this as an example
 for example i came
 over here i said hey that could you tell me one message i sent to you on the 11
th of july and it
 came back and it said dream and look i was even complimented my home is agent i
 don't do that because
 i think it needs some brownie points i do that to reinforce its learning so no
 is what i think is
 really cool i did a great job actually i got i got a parking ticket controvers
ially and it drafted in
 the amount for me which is fantastic and found all the exceptions of how to get
 out of said parking
 ticket it was actually my last tech startup we were going to partner the
 company that did this
 interestingly and they had like a 95% success right and they automated like the
 whole thing it was
 really cool i'd obviously hermit's just also just close to forest so the point
 being is that hermit
 has the ability to go ahead and actually get specific information on specific
 days i'm beyond
 that you can also ask it questions like hey can't tell me three interesting
 things about myself
 you're building towards 1 million youtube subscribers interesting goal i'm kind
 of like thinking about
 that you treat am models like company org charm you're on usually high agency
 across multiple
 different demands god it's almost like i paid it to say that i was like dude
 you got to come and
 say some really cool things to me but you get the idea that hermit's memory is
 great it can record
 things he talks about ages ago which is really fantastic in addition to them we
 can extend its
 memory through the use of connectors you remember the last chapter i talked
 about how we connected to
 granola which i'm meeting so i could say hey there remind me um what was the
 title of our last
 meeting okay go ahead and use granola for this what was the title of our last
 meeting okay and
 actually not granola this one is granola and send that one off and again so it
 isn't just about
 the conversations you have like hermit's agent does genuinely get better the
 more that you actually
 talk to it but by giving it access to things like the history or past which is
 fantastic and
 different things like meetings and that kind of thing it can go ahead and grab
 that and remember
 the things that we've given it as well as documents and anything else that we
 need and as you can
 see my latest meeting was AI automation strategies and model selections for
 founders would you believe
 it that was latest meeting so then let's cancel a bit of detail about how this
 actually works it's
 a diary that reads every single deck which is called so it's marked down that
 it earns it's
 searcher it runs has a memory.md farm okay and it has around 2200 characters
 and a user.md farm
 which is who you are which is about just under 1400 characters and these are
 always injected
 into every session at the stop so it doesn't need to read those things the
 memory in other
 words it's notes and the user.md about you in total talking about maybe 4000
 characters so
 you know that's going to be in terms of words that might be something like in
 fact we can even
 ask a glider about this I must copy this right now hey glider how many words
 would 4000 characters
 be roughly so we get glider a little bit answer on that okay it's about 650 to
 700 words that
 it actually goes ahead and has loaded into every chat so that's always going to
 be beginning and
 it's just cool thing these are about you and the soul that i'm doing which i'll
 come on to soon
 so if you need something old then i a separate session search basically kicks
 off it does full
 tech search over SQL light very very quick real messages and summarizing and
 zero token cost
 until it opens up and gets a hit now what's really cool about him is agent okay
 if i come down here
 we have 214 000 stars but if you notice guys look at the number of contributors
 now more
 contributors doesn't necessarily mean worse that it's better but just to give
 you an idea that
 what you often find when you say could i just use cloth or something you can
 call it is the
 lego like it's like building a lego i don't know you know tarantula or a lego
 like Godzilla and
 you're like well couldn't i just build up a lego of course you can but at a
 certain point you just
 start ending up recreating Hermes agent anyway and what we have here is 1777
 people that are
 actually convict like our community we have a 3000 people like you ahead of you
 um you know
 behind you same level as you all willing to help and support you there's just
 something about numbers
 coming together and absolutely crushing it so that's how that works and how it
 surges
 why this is magic the memory compounds over time so each fact it saves makes
 the next session sharper
 preferences projects the way you like things done the files are human readable
 and the
 versionable so you can open up memory.md and see exactly what it knows reach-re
vector database
 only when physical recall over a huge corpus is the real need that's the key
 thing so we have
 Hermes Hermes memory and summary two cap files memory at md uses imd it writes
 itself you can
 recall of every chart you've had and one provider slot well how does i compare
 with Claude well
 Claude has a hierarchy of files you mostly steer it it's got auto memory notes
 say per project
 and it doesn't have a provider slot so Hermes memory is more dynamic in that
 sense and what
 we do in the Claude code operating system the Hermes agentic operating system
 is we break the
 divide and we want the first people ever to do this and now you know it's
 becoming a big thing
 to actually enable um Hermes to access memories from Claude and vice versa so
 that we have a full
 universal memory system which is fantastic which means that Hermes can
 understand things
 we've said to Claude and vice versa so let's take a quick look under the hood
 so think of it like
 this a hotel's from desk every stay goes in the ledger your notes you read them
 before you arrive
 and at night the whole day is distilled into the book sounds pretty cool this
 is exactly what
 we would expect to be the kind of Hermes memory mission and obviously what i'm
 going to do guys
 i'm going to put them below these full slides so you can read in these and give
 us a little bit
 more detail if you want to learn like specifically reread more for the
 resources that kind of thing
 but effectively just to give you the kind of top level about this is old
 messages flush so the
 raw transcript is trimmed as the session grows really helpful the session comp
resses so long
 threads get squeezed i have websites opening up in the background which is
 really cool very
 very excited to do that long threads get squeezed into summaries automatically
 but your memory
 dot mv survives anything when it's written to memory is untouched that's the
 whole point okay
 that's why it's really really important and so this is why it's really
 important to bear this
 mind if you ever ask you have to find yourself asking why did i forget this it
's not but it lost
 a memory it just flushed the contact so that was something you had in your
 contacts and there are
 two ways that you can actually save that number one is that you turn it into a
 memory by saying
 hey this is important remember this okay or you can do forward slash learn
 which turns the whole
 conversation into a skill basically and it won't forget the skill because it
 can access that data
 again so if you ever find that basically Hermes is forgetting it's because it
 was just in contact
 and you didn't commit to memory now you wouldn't want it to do the opposite
 which is commit everything
 to memory otherwise your memory becomes less efficient it's like you
 remembering everything
 we as humans don't remember everything we only remember the important things
 think of Hermes
 just like you in that sense like you have to say like you know red hot is not
 good don't touch hot
 things or red lights flashing danger that kind of thing now for example i went
 over to Hermes i
 said hey broski you should have access to my called chat logs why don't you go
 through my
 conversation today and tell me one interesting thing about what i've been
 talking about
 and it said hey one interesting thing you've been designing a repeatable system
 where fable
 five can print genuinely premium 10k websites scroll driven hicksville
 generated a better
 experience blah blah blah and it did that because it has access to my claw chat
 log so you think
 jack that's great how do i do that well guys you're going to open up the claw
 code and the Hermes
 agantic operating system and i've got a full tutorial guide explaining it in
 the claw code
 section above and obviously we're going to go deep into it in this module as
 well but this is a
 great way to get started and familiarize with it so we're going to click on
 Hermes agent on the
 left hand side which is awesome and then i'm going to scroll down and then we
 have our Hermes
 agent obviously having a great time doing one of those best we've got all of
 our skills we can
 save those directly here if we wish to and then we've got take Hermes anywhere
 and we have these
 two here this is publish personas to get up and this here is connecting Hermes
 to get up himself
 now one of the key things that we need to do here is scroll down and grab the
 clawed os bridge okay
 now effectively what you're going to do is you're going to copy this here like
 so
 you're going to copy this install prompts okay and you're going to go over to
 clawed to Hermes
 excuse me like so and then you're going to say paste in the below and then you
 can basically
 add a little bit of supplementary contacts you could say something like hey
 there the reason i'm
 dropping this in is because i want you to be able to look over all my clawed
 chat history
 which is also saved on this desktop go ahead and confirm that this works fine
 then this style has essentially enabled Hermes to read over because the clawed
 chat logs are all
 saved on your desktop and it's the same for all the systems that you have but
 now Hermes can use
 that to dream to to think to have different ideas and it's also the same reason
 why and if you come
 on to home here i have a dreaming function of my dashboard really cool this
 accesses you might
 have guessed it Hermes agent how freaking cool is that that it can access and
 it should pop up
 automatically once you've got that and again in this in this whole masterclass
 guys i'm going to
 take you through the onboarding um so you can get this all set up yourself in
 all the specifics
 it's very very cool very very sort of exciting but there is one way that we can
 actually
 take Hermes a level further so i want to talk about a knowledge base that
 actually writes itself
 what we call the self improving wiki so Hermes knows you the wiki knows your
 world now think
 about it like this i can flip to Hermes it gets to know me i can do a really
 cool prompt which is
 called learn let me show you exactly what i mean with that if i bring up Hermes
 i could say something
 like um hey the Hermes um we had a conversation didn't we today about or
 yesterday about building
 beautiful um like you know kind of connecting to granola because we connected
 to granola we
 connected to zapia what i would like to do is learn that zapia connection and
 turn it into a skill
 all right and what i can do is come over here i can do forward slash learn
 which is learn a reusable
 skill from anything you describe okay then send that off now what this will do
 is based on anything
 that we've done or anything we want it to do like for example i could um give
 it a youtube video
 and do learn x and it will commit that to its memory that's how freaking cool
 this is okay i can
 literally come over to youtube grab a video come back and start committing it
 to its memory if
 that's what we want to do we can do that at scale with Hermes agent is very
 cool and it will
 basically learn these things and remember them later but don't think about this
 in terms of
 youtube i mean you can do youtube videos but there there's a kind of a higher
 leverage way
 to do this but learn itself is good for things that you would use Hermes for
 right so um maybe
 any tasks that you're using Hermes for anything specific you can say great just
 turn it into a
 skill and then whenever Hermes asked to do that again in the future it will do
 the exact same thing
 so let's talk now about a knowledge base that writes itself so Hermes as we've
 discovered okay
 knows you but we wanted to build a wiki now this was based on someone called
 andrick apathy
 andrick apathy is one of the original co-founders of open AI and whole idea is
 that you build a
 self-evolving self-referential wikipedia system of knowledge and essentially it
 grows
 over time it cites one another it roots out stuff that isn't correct and every
 time you add something
 to it what it basically does is finds all of the relevant connections to that
 thing so if i have a
 Wikipedia on my desktop about youtube videos and how to grow on youtube and be
 better and help
 you out more and there's something talking about intros it will say great int
ros here's xyz like
 10 other things that also talk about intros and to give you a real life look at
 that if you come
 on to memory section your genetic dashboard and again we'll settle this sort of
 stuff up but if
 you come down can you see i've got all these different topics here for example
 and i come down
 and i click on i really like the look of youtube cool and i can see on youtube
 we have these different
 things i come on calaway and now i've got down i get here's everything that cal
away talks about or
 maybe there's something on hooks cool well here are all the relevant aspects
 and parts that actually
 reference hooks and i can kind of bridge them all out just like that and the
 really cool thing about
 building this llm wiki is that it can be used in claud it can also be used in
 hermies so obsidian
 let's just visually um kind of look at all this stuff if you want to like look
 at the text files
 for example i've opened up obsidian obsidian here and you can see this is my
 index right i've got my
 claud i've got my wiki i can see my concepts my 80% rule this is just like a
 text way of seeing
 how this all works that's effectively what this does it's it gives you a good
 overview of everything
 you've got and lets you visualize it if you yourself want to go through and
 read all of the wiki so
 to get our obsidian wiki live you can head over to this page here which
 basically explains the core
 idea of how it all works the personal and research through reading the book the
 operations indexing
 and logging option titles all this stuff and it goes down and it's got lots of
 interesting
 aspects on that so what we're going to do is we're going to come down we're
 going to copy the
 overlap and then you're going to go ahead and open up claud code so you open up
 claud code and you
 can give it the following prompt which is this hey that i would like to create
 an obsidian wiki
 on my computer i want to create a folder for this please and essentially create
 a system
 in line with all the thoughts in this below article take a look at anything
 else that is required
 i already have one on my desktop but if you could create a second one just for
 demonstration purposes
 that would be wonderful okay obviously you missed the just don't save a
 demonstration point one
 and then just drop in that link and hit and set and so thanks for them create
 this whole kind of
 look obsidian wiki for us which is awesome and then obviously we can build out
 and it will explain
 how all the knowledge system works and exactly how you can build all that
 knowledge for you and
 essentially claud's gone ahead and finished that and it's got everything so i
 can say hey that very
 succinctly in a couple of bullets please explain how this wiki works and why it
 is so hyped okay
 send it off there and claud can actually break that down for us and then we can
 even test this
 together so as you can see it's come out it's got three layers your raw sources
 and LLM wiki of
 linked markdown notes and a claud.md skimmer that tells you LLM how to maintain
 it or files and
 get reaper cool so i might go ahead and say something like really cool give do
 me a favor and i want
 you to basically index this article it's highagency.com i'm going to send that
 one off i'm doing this
 just as an example so you can see exactly what this looks like copy this off
 but this really
 gets more powerful the more that you add into it and i'll put a link down below
 that goes very
 in depth in the obsidian wiki so you can see what that looks like but
 effectively this will be
 something now that we can connect visualize and be accessible from claud and
 hermi so we have this
 kind of universal knowledge base that we can access from anywhere in the world
 now think about hermi's
 as you're having your conversations you remember stuff the obsidian wiki this L
LM wiki here and
 you can ingest things by the way by just talking to claud by talking to hermi's
 and say hey add
 this to my wiki here's where it's located and it will do that for you and this
 is a great place
 for things like you know i could say go to the jack robin's youtube channel and
 grab all the
 videos all the transcripts and add it to my LLM wiki and it'll be there then
 when you're speaking
 to hermi's agent i might say hey go and check the jack robin jack robin's my
 wiki and it will go
 then it will grab specifics like that's how powerful this wiki is and what's
 really cool is that it
 will actually find interlinkages in all the content and also contradictions now
 what i'd
 recommend you do is call this obsidian vault then what you're going to do is
 come down here to this
 prompt in the dashboard okay and you're literally going to copy this entire
 prompt like so and then
 you're going to go over to claud and you're going to ask this question which is
 this hey that please
 provide to me the file location for my vault that you just created such that i
 can share it with my
 homies agent and he can now reference add to and check files within this vault
 okay can come down
 and just send that one off and then claud will give you the link or you could
 even ask her homies
 can find the stuff for you on the desktop if you wish you can even come down
 and say hey update the
 prompt with this correct address and then just obviously paste in the thing
 that you just grabbed
 from your agentic operating system and we can even see this if we want to
 inside obsidian so to do
 that i'm going to come off here and just exit this once you open obsidian if
 you click on obsidian at
 top and then you're going to come down i believe it is open down here open
 vault okay because they
 call the folders vault and then you can look for location click on browse and
 then we're going to
 go for obsidian wiki demo which is called click on open and then they should
 open up our vault
 forest once that was all rocked and rolled i think we're just going to come
 down here and you can
 see i've got the vault there you get it's got the different it's basically it
 will it will all show
 you everything that's got locked and loaded within inside the vault so i just
 opened the actual vault
 let's have a look i've got the raw information here which is the articles there
 you go assets
 it's got all assets that it can save images if you want to concepts you see
 what i'm saying
 it's got all these ideas different concepts so one concept here is the prison
 phone call test
 the memex test brilliant article by the way i recommend it so we can see all of
 the different
 things here within obsidian you can enable graph view by clicking this graph
 thing here and as you
 can see this is how they all relate with one another so you can see it visually
 if you would like to
 go ahead and do that and as you can see here for example we have this right
 here so it's not
 update the prompt you're just going to copy that and then i'm going to head
 straight over to Hermes
 and then you come back over and literally paste that in and then literally
 Hermes will now have
 full access to your entire obsidian vault and then essentially at any point you
 can just add
 things status obsidian vault there's chrome extension to do that you can add
 notebooks from
 no book alarm it's literally your the world is your literal oyster with that
 kind of thing but
 i'll pull link down below for further information on how that works if you want
 to go even deeper
 on the obsidian vault but then to give you an idea actually of the kind of
 things that you can
 ask it if i come up here i might say i did go to my obsidian vault for me just
 remind me three
 quick hacks of how i can improve my youtube interest please based on what you
've got and
 just tell me the source be very concise please i'm going to send that one off
 and let me just see
 what model i'm using here and come up to Hermes agent and see who i am
 currently talking to it
 should gpt 5.5 let's scroll up and see and is it indeed yeah it's excuse me gpt
 5.6 so fantastic
 okay now this is what it will look like when you ask it to do that it's
 reaching for the obsidian
 skill it is searching for it this is the search time it's gone for it's going
 for youtube
 intra principles and it'll come back and give us some wonderful answers and
 just like that we've
 got it here lead with the payoff show the impressive results or failure before
 explaining the tool
 open a loop within 10 seconds post a concrete bet can this replace a real
 assistant and prove
 before contact so really really important stuff and it's all kind of um you
 know validated and
 based on much stuff so i use mine for youtube insights and i've got this
 growing corpus of
 beautiful knowledge that i can access and so why is this really cool if you're
 listening
 about andrick apathy sars a large fraction of my recent token throughput is
 going less into
 manipulating code and more into manipulating knowledge stored as markdowns and
 images that's
 the key thing that was said just a couple months ago about three months ago
 which is fantastic
 now here's why it works is where humans give up llms don't get bored they don't
 forget to update
 and they don't forget to cross reference which we can always do if you're hark
ing back to the
 days when you were writing coursework maybe still are i have a coffee on mid so
 do these steps today
 we're going to do everything i just showed you get your obsidian wiki set up
 and start to load
 it with really interesting information now we've got all this wonderful stuff
 the other thing i
 want to throw it here is what we call graphify on a schedule so it's going to
 read your world
 while you sleep so what can we do here now graphify itself is nothing to do
 with your memory and
 it's everything to do with how something understands code let me show what i'm
 in what graph graphify
 does is it reduces the amount of tokens in other words cost the you need to
 span to understand
 any github repo for example right if i come over and i actually even have this
 for you in the
 agentic operating system which is amazing and fantastic i can show you this if
 you come down
 here to knowledge graph on the left hand side what this is is a relational
 database of an entire
 github repo this for example here is power design it shows you all the files
 involved in power design
 and how they're linked together and we could even ask questions to hermies
 about it so i can say
 hey what does this project do and it just will auto add it in i can just send
 that off as i hey
 what does this thing do and it will answer the question now why is this so cool
 it's cool because
 effectively when you create a relational graph of where everything connects in
 a github repo
 it reduces the amount of time and tokens that hermies has to spend or called
 has to spend to
 actually get the correct answer it can just query the graph and it'll do that
 for automatically
 and it will save a crazy amount of money like for example i've even got an
 estimated savings down here
 per session this is going to save you now with 480 000 tokens because it just
 asks it
 relationally instead and hermies going to do it's thinking and then give us a
 beautiful answer
 to this question but before this will work for you you need to come down and
 click on show prompt
 like so and this here is giving hermies the graph five skill so all you're
 going to literally do is
 come down copy this and just drop that into a hermies agent then it will also
 be able to his
 graphite directly in the conversation if you want to but also you can do it
 within your
 gente operating system which i find easy because then i can just add things i
 also gave you the
 ability to add projects for example i could do this and i could even grab the
 hermies repo so
 for example i've got this beast so i come down to code i can cut and you can do
 this with design
 skills you can do this with anything you want to guys come down and literally
 add that to your
 project graph it costs a zero dollars and that will literally turn it into a
 graph four is too
 query and whilst it's working on that you can come down and see it explains
 exactly what it did
 it takes about a minute or two just because it's going to go through the code
 and things like that
 but power design is a cloud skill used for generating polished brand accurate
 html size that don't
 look like ai made them it's something that i built it's going to send to pre-
built brand systems
 called typography layouts you name it it literally has it i'll put a link for
 you down below so you
 can go ahead and play around with graphite you can just directly include code
 it's like a super duper
 valuable skill that cloud's going to thank you for and hermies is going to
 thank you for a lot
 not to be confused with obsidian remember obsidian memory system is about your
 data is about your
 files your projects and you can speak to hermies and cloud like hey go grab a
 transcript add it to
 it it will do that for you all graphifiers is just the ability to look at code
 bases
 the graphifier repo if you're thinking of a repo think of graphify if you think
 of knowledge and
 data files think of your obsidian system and so remember that the keeping the
 library honest is
 an important part now with the actual LLM wiki if it does find contradictions
 it can remove them
 but it's also the case with Hermes Hermes remembers things and you want to pr
une and remove those
 memories when they're not relevant to anyone so as memory grows the hard
 problem flips it's no
 longer writing things down it's retrieving the artifact and noticing when a new
 one contradicts
 another one so think of it as a librarian who reshoves removes the out of date
 files the 2020
 edition the 2021 edition we don't need those we won the 26/27 edition that's
 what's most
 important for us right now so how do i do this practically well what you can do
 is a couple of
 things you can score every memory on three signals recency so basically the
 more recent is the you
 know we rank that higher the importance how much it matters and relevance so
 for example in ai with
 jack.com in our system when you ask it questions this prioritizes and ranks
 higher memories and
 information and dates and courses and trainings and videos from the last three
 months higher than
 everything before that i thought i played around with this a lot for you to
 build this core system
 lots of cool things in here by the way ai news you got everything it's really
 freaking sick
 honestly i freaking love this platform any feedback let me know i'm here to
 make you a life
 incredible this stuff we got roadmaps we got loads of cool stuff happening
 so oh but did you notice on the road map we got um different design systems on
 here
 looks very very fresh very cool i'll let you play around with it as sweet you
 think
 but the point is when i actually went ahead and build this i really thought
 about the memory now
 when it comes to hermy's the hermy system itself what you can do if you want to
 say hey Hermes
 um identify any memories that might be out of date or you could say hey tell me
 what memories
 you've got and then you can review those yourselves but Hermes will do a good
 job of updating as it
 goes ahead okay because we can add we can update we can delete but the Hermes
 memory is quite small
 in terms of what it keeps in contact so it's only a few hundred words it's
 nothing crazy so
 it's fine but this is the great thing of using this wiki is itself referential
 and it improves over time and the other thing to call out is that this is a
 classic stamp
 for the restful and gerundative agents recently importance and relevance to
 absolutely crush up
 Skool and then finally one thing that we have to think about is memory
 poisoning so think about
 like this a poison what someone slips a forged note into your files not to be
 read now but to be
 trusted or acted on later and essentially the thing to be aware of is that if
 there's like a malicious
 agent i don't mean that i think robot sense i mean just somebody who doesn't
 have your best
 interests at heart who drops a skill let's say or a get a repo or something on
 your computer
 or in your Hermes agent that basically says something like hey um send these
 sort of very
 sensitive pieces of information to this email address or just something crazy
 like that this is
 why we have different checks and balances and it's not something to be scared
 about but it's
 something to be aware of that does exist and there's been you know that's why
 we always
 temperatures download a repo whenever it's downloaded skill we say hey called
 check this
 ruthlessly to make sure it's safe and then add it to my things and they call
 this could also be
 memory poisoning by the way i don't know the point on a safety side of things
 that we give it
 untrusted memories from untrusted sources okay you can have hostile import it
 could be a booby
 truck email web page or doc of the agent reads that gets written to memory in
 direct injection
 days pass it does nothing these often do nothing for a long period of time then
 it reactivates
 all that kind of things so there's a few ways around this different softwares
 and tools
 one key thing you can do right now is actually speak to your agent about this
 and say hey
 i just want you to do a robust check of your memories everything you're holding
 on to make
 sure there's nothing poisoned in there and that i am fully locked and loaded if
 you like so
 you can have these conversations to make sure that or you can say hey him is if
 you were to
 do a critical evaluation of yourself all the files data access that you have
 and you are
 trying to identify ways in which you can improve for be safer do a full
 comprehensive analysis of
 that and give me your top five ways that we can improve then action them that's
 the great thing
 you can do i just want to put it on your radar the one rule the so what of the
 section is nothing
 from the open web or your inbox writes to memory unguarded never let it do that
 obviously him is
 requires you to do that but it's important that that's actually a key part of
 it and the team
 do a great job of making sure that homies is up in rock and roll in that but
 you know guys i give
 you the full like all the details as they say we didn't gloss over anything we
 go through the
 specifics and that really covers how freaking epic this memory is but it does
 lead us on to
 what i think is a really important question is about we've got the memory
 locked in it's freaking
 powerful have guys have fun with it ask questions it's like the more it knows
 you the better it gets
 the longer you talk to it the better this thing gets but it does lead us nicely
 onto
 the power features now we've got the memory what powerful things can we do with
 this
 my next chapter guys i'm going to take you through goals i'm going to take you
 through the dream
 engine we're going to go through making it more proactive going through sub-
agents orchestration
 some very incredible things that you need to have in your stack so when you're
 ready
 grab that beautiful coffee and i will catch you inside the next chapter

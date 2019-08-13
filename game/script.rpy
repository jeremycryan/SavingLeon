# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform close:
    zoom 1.1

transform default:
    zoom 1.0

init python:

    aden_sprites = ("aden neutral", "aden smiling", "aden blushing")
    reg_sprites = ("reg neutral",)
    leon_sprites = ("leon neutral",)
    nate_sprites = ("nate neutral",)
    serpens_sprites = ("serpens neutral",)
    brian_sprites = ("brian neutral",)
    sprite_dict = {"aden": aden_sprites,
                    "reg": reg_sprites,
                    "leon": leon_sprites,
                    "nate": nate_sprites,
                    "serpens": serpens_sprites,
                    "brian": brian_sprites}

    from functools import partial
    def bounce_callback(char, event, interact=True, **kwargs):
        if not interact:
            return
        if event == "begin":
            char_sprites = sprite_dict[char]
            for sprite in char_sprites:
                if renpy.showing(sprite):
                    renpy.show(sprite, at_list=[bounce])

define gui.text_font = "Candara.ttf"

define a = Character("Aden", image="aden", callback=partial(bounce_callback, "aden"))
define r = Character("Reg", image="reg", callback=partial(bounce_callback, "reg"))
define l = Character("Leon", image="leon", callback=partial(bounce_callback, "leon"))
define n = Character("Nate", image="nate", callback=partial(bounce_callback, "nate"))
define s = Character("Serpens", image="serpens", callback=partial(bounce_callback, "serpens"))
define b = Character("Brian", image="brian", callback=partial(bounce_callback, "brian"))
define boy = Character("Boy", image="aden", callback=partial(bounce_callback, "aden"))
define cl = Character("Court Lady")
define mc = Character("[mc_name]")
define coach = Character("Coach")
define teacher = Character("Teacher")

define fade_to_black = Fade(0.5, 1.0, 0.5)

transform bounce:
    yoffset 0
    easein .1 yoffset 10
    easeout .1 yoffset 0
    easein .1 yoffset -4
    easeout .1 yoffset 0
    yoffset 0

transform leftish:
    xalign 0.25
    yalign 1.0

transform rightish:
    xalign 0.75
    yalign 1.0

transform center:
    xalign 0.5
    yalign 1.0

# The game starts here.

label start:

    python:
        mc_name = renpy.input("What is your name?")
        mc_name = mc_name.strip().capitalize()
        if not mc_name:
            mc_name = "Gargle-flargle"

    "{i}Welcome, [mc_name].{/i}"

    menu:
        "Choose a chapter to playtest."
        "Start":
            "Starting from beginning."
        "Meeting Aden":
            jump Aden2
        "Practicing by himself":
            jump Aden5
        "Love is worth it":
            jump Aden9
        "Meeting Reg":
            jump Reg2
        "Study Buddy":
            jump Reg5
        "More than you can imagine":
            jump Reg9
        "First date":
            jump Reg11

    label intro:
        scene interrogation_room with fade_to_black
        "{i}Evidence locker for case #03762. There are six tapes, a photo album, and a receipt."

        label tape_menu:
            menu:
                "Tape: Li, Aden - deposition":
                    jump Aden2
                "Tape: Na, Reginald - deposition":
                    "Sorry, that doesn't exist yet."
                    jump Reg2
                "Tape: Giang, Brian - deposition":
                    "Sorry, that doesn't exist yet."
                    jump tape_menu
                "Tape: Dio, Serpens - deposition":
                    "Sorry, that doesn't exist yet."
                    jump tape_menu
                "Tape: Pacce, Nate - deposition":
                    "Sorry, that doesn't exist yet."
                    jump tape_menu
                "Tape: So, Leon - deposition":
                    "Sorry that doesn't exist yet."
                    jump tape_menu
                "Photo Album":
                    "Sorry, that doesn't exist yet."
                    jump tape_menu
                "Receipt":
                    "Sorry, that doesn't exist yet."
                    jump tape_menu

    label Aden2:
        scene interrogation_room with fade_to_black
        show aden neutral at center
        cl "Mr. Li, are you ready to begin?"
        a "I'm ready!"
        cl "Alright Mr. Li, I'm going to be asking you some questions about yourself and the occurrences of and leading up to the events of April 27, 2019."
        cl "You are sworn under the same oath that you will be for the upcoming trial. Is that clear?"
        a "Yup."
        cl "Mr. Li, I will need a clear yes or no please."
        a "Oh, sorry. Yes."
        cl "Okay, Mr. Li. Can you please state for the record your full name and your age?"
        a "My name is Aden Li, and I am 15 years old."
        cl "And what is your occupation?"
        a "My occupation?"
        cl "You are a student, yes?"
        a "Oh, yes."
        cl "At what school?"
        a "Bellington High School. I'm a freshman there."
        cl "Thank you. Can you tell me about your relationship to the victim, Mr. Li?"
        a "He was one of my very best friends! We played on the same soccer team together."
        cl "Which soccer team was this?"
        a "Well, we weren't {i}exactly{/i} on the same team. I mean, I guess we were for one game. For most of the season, he was on varsity and I was on JV. Alternate."
        cl "Mr. Li, I need you to state clearly what soccer team you and the victim were on."
        a "Oh, yes, sorry, of course! We played for the Bellington High School Tigers."
        cl "Can you tell me about your relationship with [mc_name]?"
        a "We were also friends, or... something like that at least."
        cl "Can you please elaborate?"
        a "The day we met was... transformative. No, that's not the right word for it."
        a "I'm just... I'm just trying to say it was an important day. Not because of anything in particular I did, but because she said something to me that... stuck with me."
        a "It was this last September, near the beginning of the school year. It was the day of the soccer tryouts. I don't know how, but I still remember it so clearly."
        "{i}I remember it too, Aden.{/i}"
        jump Aden3

    label Aden3:
        scene school_hallway with fade_to_black
        "{cps=8}{i}Briiiiiiiing!{/i}{/cps}"
        "{i}As the bell marking the end of sixth period rang through the hallways, I slowly began gathering my things. As I jammed the final notebook into my backpack, Leon appeared in the doorway of the classroom.{/i}"
        show leon neutral at center
        l "Hey [mc_name]! What's up?"
        mc "Hey Leon. Not much... I'm just burned out from history class."
        l "Yeah, me too."
        mc "Didn't you finish all your history requirements last year?"
        l "Oh, well, yeah... I just mean I'm --- I just remember what a bore history can be, heh! Memorizing all those dates. Blegh!"
        l "I mean, when will I ever be in a position where I'll need to know when the War of the Roses started?"
        l "Will someone ever point a gun to my head and threaten to pull the trigger unless I know what year the Battle of 1812 happened?"
        l "Or maybe high school is just trying to prepare us for Thursday Night Trivia?"
        mc "Haha, I'm sure that's it! I'm glad we're being prepared for something so important."
        l "It totally is important! I mean, how could we live without Thursday Night Trivia's $500 cash prize to split among a team of six?"
        mc "And ta-da, we've figured out the point of learning algebra."
        l "Haha, yeah you get it! Uh, by the way... It's warm cookie Wednesday at the school café. Want to go with me?"
        mc "Sure!"
        show school_hallway with fade_to_black
        show leon neutral at center
        l "Mmfp. I can't stop eating these! Do you think the cookies taste so good because they're overpriced? It's probably just some sort of psychological --- {i}oof{/i}!"
        show leon neutral:
            linear 0.5 leftish
        show reg neutral at center with moveinright
        show nate neutral at rightish behind reg with moveinright
        "{i}Suddenly, two boys in athletic attire had appeared. One of them had put Leon in a headlock that he was struggling to escape from, and the other was slowly shaking his head in both humor and disappointment{/i}"
        l "Guys, knock it off!"
        "{i}Leon skillfully escaped from the hold.{/i}"
        l "You're gonna make me drop my unreasonably priced cookie!"
        l "Uh, [mc_name], these are a couple of the guys on my soccer team. This is the captain, Nathaniel, and one of the midfielders, Reginald."
        mc "Hey Nate, hey Reg. Good to see you guys again."
        l "Oh, do you guys already know each other?"
        r "First of all, don't let me ever hear you call me Reginald. And secondly, yes, we have met. You see, me and your {i}girlfriend{/i} here ---"
        l "What!? She's not ---"
        n "Reg, cut it out. Instead of teasing Leon, maybe we should be talking about how he's eating loads of sugar right before tryouts? Leon, you're going to have a sugar crash."
        l "It's warm cookie Wednesday though! Do you want a piece?"
        n "No, thank you, I need to get back to my ever-so-important tabling duties."
        "{i}Nate sat down at a foldable table that I'd neglected to notice earlier and beckoned Reg to join him. Attached to the front was a huge white sign reading {i}\"SOCCER TRYOUTS TODAY!\"{/i} in immaculate handwriting."
        mc "Tryouts are this afternoon? Are people still signing up this late?"
        "{i}Reg sat down next to Nate and propped his feet on the table.{/i}"
        r "Not really. Coach just likes to make us sit here and suffer."
        n "It's not that bad, Reg."
        r "Maybe not for you... you don't have anything better to do!"
        n "That's not ---"
        boy "{cps=8}{i}Woooooa!{/i}{/cps}"
        show leon neutral:
            linear 0.3 left
        show reg neutral:
            linear 0.3 leftish
        show nate neutral:
            linear 0.3 center
        show aden smiling at right with moveinright
        boy "There's soccer tryouts? Can I sign up? When are they?"
        n "Hi! Yes, just put down your info here. Tryouts are this afternoon at 4:30."
        boy "They're today? That's so soon!"
        r "Yeah, not like we haven't been in the hallway advertising for the past week --- ouch!"
        "{i}Nate nudged Reg aggressively in the ribs, as the young boy began frantically scribbling on the sign-up sheet.{/i}"
        n "Yeah, they're today. No, that's where your emergency contact name goes... your name goes over there. Aden, is it? Do you have any experience, Aden?"
        a "Uhmm, I've watched soccer on TV!"
        n "..."
        l "..."
        r "Great! You've got everything you need to make --- ouch!"
        "{i}Nate nudged Reg in the ribs again, this time with double the force.{/i}"
        l "Uh, hey, the team is like, really competitive. Like, we made it to the state semi-finals this year. Are you sure you're feeling up to trying out for a team like that?"
        a "Yeah, I'm sure! Anyone can try out right? I think if I work really, really hard and have a positive mental attitude I'll be awesome!"
        n "I don't think it's really that simple. Most players on the varsity team have at least six years of experience. We've all trained really hard for years."
        r "What? You don't want to see the kid make a fool of himself out there?"
        n "Reg, stop it. Um, what's your name again?"
        a "Aden!"
        n "Aden, right, you look familiar. Aren't you in the band? I remember you being really good on the sax."
        n "Band practices are at the same time as soccer, so you'd have to quit band if you made the team. It would be a shame for the band to lose a player like you!"
        l "Yeah, sorry Aden... I'd have to agree with Nate."
        a "But I want to do something new and exciting! I think I'd have a lot of fun."
        "{i}Aden suddenly turned his attention to me as though he was pleading for someone to agree with him.{/i}"
        mc "Aden, I think you should..."
        menu:
            "What should Aden do?"
            "Try out for soccer":
                jump Aden4
            "Stay in band":
                "He does band"
                return
                #	Jump to correct spot

    label Aden4:
        mc "Aden, I think you should go for it. If you want to try out for the soccer team, you should try out for the soccer team!"
        l "Really, [mc_name]?"
        mc "Who knows? Maybe he'll surprise you."
        hide leon
        hide nate
        hide reg
        with moveoutleft
        show aden:
            linear 0.5 center
        "{i}Leon sighed and turned to Reg and Nate to quietly discuss this turn of events. Meanwhile, Aden smiled and blushed at me."
        a "Hey... thanks."
        mc "It's no problem."
        a "No, seriously, I appreciate it. I just... people have told me so many times what they think I can't do. Even worse, people have told me that I shouldn't even try because there's a chance I might not succeed."
        a "It's really nice to meet someone who... It's just refreshing to be encouraged for once."
        "{i}Aden blushed deeper.{/i}."
        a "Sorry, I think I overshared a little! I'm Aden! Oh, you probably heard that earlier. Sorry, I ---"
        mc "It's nice to meet you Aden. I'm [mc_name]."
        a "Nice to meet you, [mc_name]! I look forward to seeing you around school!"
        mc "See you around."
        hide aden
        show interrogation_room
        with fade_to_black
        show aden neutral at center
        a "I feel like she saw something in me that a lot of other people didn't. She was my first new friend at high school!"
        a "Because of her, I tried out for the soccer team and I made it! As a JV alternate, but still! I was confident that if I worked hard that I could become as good as Nate, or Reg, or..."
        cl "...or Leon?"
        a "Yeah... or Leon."
        cl "Mr. Li, I am still a little unclear as to your relationship with [mc_name]. The two of you were friends, right?"
        a "Well, yes and no."
        cl "What do you mean, \"yes and no\"?"
        a "We were, but then again... we were something else."
        cl "Mr. Li, it is important that we understand your relationship to everyone involved in the events that took place leading up to the evening of April 27, including [mc_name]."
        a "Okay, let me explain. For a while after the soccer tryouts, we didn't see much of each other. Just occasional glimpses in the hallway between classes."
        a "But, that changed entirely the day [mc_name]'s car broke down."
        cl "When was this?"
        a "Ummmmm... it must have been sometime in October. It was colder than usual for the time of year. She told me that she tried to start her car, but something was wrong. Something was {i}very{/i} wrong."
        jump Aden5

    label Aden5:
        scene school_parking_lot with fade_to_black
        "{i}It's so nice to finally head home after working on that group project for so long. Where did I park again? Ah, over there.{/i}"
        "{i}What? It's seriously not starting? Maybe I should call someone? ...aaaaaaaaand my phone's dead. Arg! Awesome luck today.{/i}"
        "{i}There's got to be someone who could help, right? The soccer fields are nearby, so maybe Leon or one of the other soccer boys can help me out.{/i}"
        scene soccer_field with fade_to_black
        "{i}Looks like they're scrimmaging. I don't want to interrupt or anything, so I guess I could wait till they're on a break. Huh? It looks like there's someone practicing over here by himself. Oh is that...?{/i}"
        show aden smiling at center
        a "Ah! [mc_name]! Hi!"
        mc "Hey Aden. Why are you practicing over here by yourself?"
        a @blushing "Ah, well I'm kind of, um, not very good! I think I was just getting in everyone's way."
        a @smiling "Coach told me to practice dribbling by myself but I just keep tripping over the ball. It's really hard!"
        mc "It sure looks tricky. It's great to see you working so hard!"
        a "Yeah! I just got to keep trying! Practice makes perfect. Soon, I'll be scoring game-winning goals and it'll all be worth it. Do you know how to play?"
        mc "I mean, Leon and I used to play in his back yard, but I've never been on a team or anything."
        a "Oh that's even better than me! Maybe you could help me practice sometime!"
        mc "Yeah, maybe! That might be fun!"
        coach "Alright! 5-minute water break!"
        show aden:
            linear 0.5 leftish
        show leon neutral at rightish with moveinright
        l "Hey, [mc_name]! What are you still doing here?"
        mc "Oh, my car won't start. I was wandering around to see if anyone could help."
        l "Wow, that sucks."
        a "Oh no! What are you going to do? Do you know how to jump start a car? I tried to do that once but something caught on fire and my mom was super mad an-"
        l "Ok, ok yeah I don't really know anything about jumpstarting but-"
        "{i}Leon looks around and seems to notice someone walking by the field.{/i}"
        l "Hey Serpens! Come here for a sec!"
        show leon:
            linear 0.5 center
        show serpens neutral at rightish behind leon with moveinright
        s "Um, hello."
        l "My friend [mc_name]'s car broke down. Are you about to drive home? Do you think you could give her a ride?"
        s "Oh, um. I...uhm. I guess that's fine... as long as [mc_name] is okay with it."
        a "Or if you want... you could stay and help me practice! My mom can give you a ride home when she picks me up."
        menu:
            "What should I do?"
            "Practice with Aden":
                jump Aden6
            "Go home with Serpens":
                "You ride home"
                return
                #	Jump to correct spot

    label Aden6:
        mc "I will stay and help you practice, Aden."
        a "Really!? This is gonna be so much fun!"
        mc "It's going to be hard work though, Aden. You have to be prepared to train hard if you want to be as good as the varsity players."
        a "I will! I promise! Thank you so much!"
        l "[mc_name], are you sure?"
        s "Yeah, I can drive you home, no problem."
        mc "No, you go ahead Serpens. I appreciate the offer, but I'm okay."
        l "Alright, whatever you say..."
        hide leon
        hide serpens
        with moveoutright
        show aden:
            linear 0.5 center
        mc "Okay, Aden. Let's get to it!"
        mc "The first thing I want you to try is the dribbling you were doing before, but instead of kicking the ball with your toes try using the inside of your feet."
        a "Woah! That makes it so much easier! Nobody showed me that trick until now!"
        mc "Really? It's a pretty basic soccer technique."
        a "Well, coach doesn't usually let me practice with the rest of the JV boys, and the upper classmen on varsity mostly ignore me... nobody was around to tell me I was doing it wrong."
        mc "That's terrible."
        a "No, it's okay! When I tried out for the team I knew I'd have a tough road ahead of me."
        a "I knew I would have to try so much harder than everyone else. I'm totally up for the challenge!"
        mc "I know you're up for the challenge, but you don't have a fighting chance without help from someone who knows the sport."
        a "But, if I practice really really hard..."
        mc "I'll tell you what... you and I are going to practice every day. We are going to show the coach and the varsity boys what you're capable of."
        mc "I know someone who plays on the soccer team at Bellington University, and I'll see if he can come help. Doess that work for you?"
        "{i}Suddenly, tears filled Aden's eyes."
        mc "Woah, what's wrong? What did I say?"
        a "Nothing! Really, it's nothing. I'm just happy. [mc_name]...thank you."
        a "Thank you for believing in me."
        scene interrogation_room with fade_to_black
        show aden neutral at center
        a "Don't you see, Your Honor? Sure, we were friends but... we were also something else!"
        a "I had teammates and coaches who didn't consider my contribution to the team worth their time, but then someone came along who did."
        cl "Aden, I am not a judge. You do not have to call me \"Your Honor\"."
        a "Oh, sorry. This is my first time doing one of these."
        cl "It's okay, let's just continue. Did your training sessions continue after the first encounter?"
        a "Yes, she even brought Brian along every now and then."
        cl "Who's Brian?"
        a "Brian Giang... he graduated from Bellington High last year. He was on the high school varsity team and now he plays for the Bellington University team."
        a "[mc_name] was friends with him I guess, so she asked him for help."
        cl "Would you consider Brian a friend?"
        a "Well, I didn't know him that well. I'd say he was more of a mentor. He had great life advice!"
        a "Or, at least at the time I thought it was good advice. In hindsight, his advice may have been what started this whole thing."
        jump Aden7

    label Aden7:
        scene soccer_field with fade_to_black
        "{i}I've been practicing after school with Aden for a while now. It's slow going, but I got to admit his energy is infectious. Having something to look forward to after school is nice.{/i}"
        show aden neutral at leftish
        show brian neutral at rightish
        a "Hey, [mc_name]! Guess what? Brian came early today!"
        b "We've just been warming up with some juggling."
        a "I can do three in a row now!"
        mc "That's fantastic. So, Brian... any particular exercises you had in mind for him today?"
        b "Ah, I think I remember some drills? Let me think..."
        scene soccer_field with fade_to_black
        show aden neutral at leftish
        show brian neutral at rightish
        b "No, you're supposed to do it like this --- see little spin move keep your head up, weave this way, and- there. Like that!"
        a "*pant* *pant*"
        a "I... uh, like this?"
        b "No, not really. Try and keep your shoulders open, and- ugh. Can we take a break?"
        a "Whaaaat? It's only been like 15 minutes."
        b "But I'm old and teaching is hard."
        a "You're not that old!"
        b "Kid, you'll understand when you're my age."
        a "Whatever! We can take a really really short break. Is that okay with you [mc_name]?"
        mc "Sure... so Brian you graduated last year? What's college like?"
        b "Well it's... I don't know. It's nice to have independence and stuff."
        b "Classes are way harder. It makes you mature really fast. Like I have this ex-girlfriend Cynthia and uh..."
        a "And?"
        b "Well I don't know if you're old enough to hear this story."
        a "I'm 15 not 5! And I know all about adult stuff like sex an-"
        b "Okay, not that kind of story, it's just ugh. That relationship was really messy. I guess we're both just messy people."
        b "We really cared about each other and I thought that would be enough to keep things together but it wasn't. Sometimes things just don't work out."
        b "I think before that I thought love was this all-powerful force that could do anything. But now I don't even know if love is even worth the trouble."
        b "I guess I grew from it."
        a "But that's so pessimistic! Just because it didn't work out that one time doesn't mean love isn't worth it."
        a "I mean love is the thing poets and artists and stuff all write about and it makes life awesome cause you get to share life with someone else you know?"
        b "Yeah, but love hurts. It's naïve to think it's an easy thing. It's more about flowers and long walks on the beach and all that."
        a "But it's still magic and you shouldn't give it up! What do you think, [mc_name]?"
        mc "I think that..."
        menu:
            "What do I think?"
            "Love is worth it.":
                jump Aden8
            "Love isn't worth all the trouble.":
                #   Jump to correct place
                return

    label Aden8:
        mc "Love is totally worth it."
        a "See, Brian?"
        b "Why are you so determined to prove me wrong? Aden... have you fallen in love with someone?"
        a "What!? Pssh, no... that's ridiculous."
        b "Oh, I think I see what's going on here. You---"
        a "Shut up, Brian! I'm not... you know... in love or anything."
        b "Whatever you say, man. But if you have---"
        a "I haven't!"
        b "Okay, well {i}if{/i} you have... let me give you some advice:"
        b "Bros.{w} Before.{w} Hoes{cps=3}...{/cps}{w=1.0} always."
        b "Let me tell you, this girl Cynthia, hot as can be. Even hotter than [mc_name]."
        a "Yeah, right! No way anybody's..."
        b "...yes?"
        a "Um, nothing. Continue."
        b "So, anyway, my best friend also had a thing for Cynthia. It sucked because I really liked her, but I didn't want to hurt my friend. The best decision I ever made was not telling him about us."
        b "After a while Cynthia and I didn't work out, but that friend and I... we still hang out. I would have lost him as a friend if he knew I'd been seeing her."
        b "Like I said, your number one priority has got to be your bros."
        mc "Having secrets can't be good for your friendship though, right?"
        b "He never found out, so what does it matter?"
        mc "But---"
        a "No, I get it! You did it for the sake of your friend. I think that's really cool."
        b "Well, I'm a pretty cool guy."
        a "You'd be even cooler if you got back to helping me practice!"
        b "Ugh. Fine."
        scene interrogation_room with fade_to_black
        show aden neutral at center
        a "I really looked up to Brian, so I didn't see at the time how bad his advice was."
        a "When I found myself in a similar situation, I thought I was doing the right thing by following Brian's example."
        cl "What do you mean you found yourself in the same situation?"
        a "I had begun to really like a girl... but one of my closest friends liked her too."
        cl "How did you know your friend liked the same girl?"
        a "Trust me. I knew."
        jump Aden9

    label Aden9:
        scene school_hallway with fade_to_black
        "{i}It's been a few months since we started practicing. It's crazy how much Aden's improved. I feel like it's only yesterday he could barely even kick the ball without tripping over his own feet...{/i}"
        show aden smiling at center
        a "[mc_name]! You're not going to believe this! Oh my gosh, it's so exciting!"
        a "I can't wait! This is crazy!"
        mc "Uh, hey, slow down Aden. What are you talking about?"
        a "Well okay, see there's this guy named Sean and he's on the varsity team, but he hurt his ankle so they needed an alternate, which is really awesome..."
        a "...I mean not awesome for him since you know, that hurts and sucks and everything, but..."
        a "They want me to take his place for the game tonight!"
        mc "That's awesome Aden! You've been working really hard, you deserve it!"
        a @blushing "Uh, I mean, well, I couldn't have done it without you. You're really amazing!"
        mc "Um, thanks, I- haha, I try my best. So, what time is the game tonight?"
        a "It's at 4:30. Why, are you... do you... are you planning to come watch?"
        mc "Of course I am! If... if you don't mind, of course."
        a "Oh, no, of course I don't mind! I'd love for... I'd really like for you to be there."
        a "Okay, I'll be sure to be awesome and score tons of goals and, like, be the MVP!"
        scene soccer_field with fade_to_black
        "{i}The soccer game was really intense. Varsity really is on a different level than JV.{/i}"
        "{i}The guys are really big compared to Aden, but he really held his own. He even made an assist! There's something kind of adorable about his tenacity.{/i}"
        show aden smiling at center
        a "Hey! [mc_name]! I'm so glad you came! Did you see me out there!"
        mc "Yeah, I did! That was so intense! You made an awesome assist."
        a "Yeah, I---"
        show aden:
            linear 0.5 leftish
        show leon neutral at rightish with moveinright
        l "Did you... did you come to see me play?"
        mc "Well, I---"
        l "Awwww, that's so sweet [mc_name]! I think this is the first time you've come to one of my games since middle school."
        l "I... actually really appreciate it."
        mc "Oh well, I'm glad you appreciate it but I actually---"
        l "No need to talk it down. It was really sweet, [mc_name]."
        l "I maybe would have tried a little harder to sccore a goal if I'd known you'd be here. I kinda missed an opportunity to show off."
        l "Oh jeez, that sounded weird! It's not like I'm trying to impress you in particular or anything, it's just---"
        mc "Leon, I..."
        menu:
            "Actually, I came to see Aden":
                jump Aden10
            "Don't correct him":
                #   Jump to correct place
                return

    label Aden10:
        mc "Well, actually Leon... I came to watch Aden play."
        l "Oh, you--- you did?"
        l "I'm sorry, I was being pretty presumptuous I guess. Oh, boy, so embarrassing..."
        "{i}Leon shifted nervously from foot to foot while a smile spread across Aden's face.{/i}"
        l "Well, um, I'm gonna go ahead and go home. Both of you, drive safe!"
        l "{size=-10}God, so embarrassing...{/size}"
        show aden:
            linear 0.5 center
        hide leon with moveoutright
        a "Uh, hey, [mc_name]... I think he likes you."
        mc "What? No way!"
        a "I'm serious!"
        mc "What makes you say that?"
        a "Did you see how excited he was when he thought you'd come to see him play? No boy gets that excited for a girl to watch him play a sport unless he's into her!"
        mc "But... YOU were that excited."
        a "... Yeah. I guess I was."
        scene interrogation_room with fade_to_black
        show aden neutral at center
        a "You see? I was in a situation just like Brian's! I liked [mc_name], but so did Leon. I couldn't bear to give her up, but I also couldn't stand the idea of Leon getting hurt because of me."
        a "So, I decided I would do my very best to make sure Leon wouldn't see [mc_name] and I together. You know, for his own protection."
        cl "So, you and [mc_name] weren't just friends because she was your girlfriend?"
        a "Not exactly. We continued hanging out and stuff, but it was never really official. The closest we ever came to that was when I invited her to be my date to Reg's party."
        cl "Are you referring to Reginald Na of Bellington High's class of 2020?"
        a "Yeah, that's Reg! After we won that game, Reg decided to throw a party for the varsity team."
        a "His dads were both surgeons back in South Korea, so here in the states they have this huuuuge house. Perfect for awesome parties!"
        cl "Mr. Li, can we focus on what happened when Reginald invited you to his party?"
        a "Oh, yeah. Of course."
        return

    label Reg2:
        scene interrogation_room with fade_to_black
        show reg neutral at center
        cl "Mr. Na, are you ready to begin?"
        r "As ready as I'll ever be, I guess."
        cl "Alright, Mr. Na, I'm going to be asking you some questions about yourself and the occurrences of and leading up to the night of April 27, 2019."
        cl "You are sworn under the same oath that you will be for the upcoming trial. Is that clear?"
        r "Yes."
        cl "Okay, let's begin. Can you state for the record your full name and age."
        r "I'm Reg Na, and I'm---"
        cl "I'm sorry Mr. Na, but I need you to clearly state your full {i}legal{/i} name."
        r "Fine. I'm {i}Reginald{/i} Na and I'm 18 years old. Everyone calls me Reg though, and I'm not going to make an exception for you."
        cl "Okay, Reg... you seem a bit on edge."
        r "I'm not on edge, I'm just kinda pissed. I was forced to dress up nice and come sit in front of a camera for hours so some lady can interrogate me."
        r "I just lost my best friend and I'm being treated as though I'm a suspect. I have an entire soccer team full of alibis, so I don't even understand why I'm here!"
        cl "I understand this can be frustrating Reginald---"
        r "Reg."
        cl "Sorry... Reg. I understand this can be frustrating, but it's important that we understand all the events leading up to your party and the relationships between everyone there."
        cl "Even if they seem insignificant, these interactions tell us a lot about the motives of everyone involved. We really want to figure out what happened to your friend, and we can't do that without your help."
        cl "Can I expect your cooperation?"
        r "Yeah, I guess."
        cl "Thank you, Mr. Na. Can you also state for the record your occupation?"
        r "I'm a senior in high school. Bellington."
        cl "And how did you know the victim."
        r "We played soccer together on the Bellington High School varsity team, but we were friends before that."
        cl "For how long?"
        r "I don't know. Since sixth grade or something."
        cl "And how about your relationship to [mc_name]?"
        r "We had a class together. AP Calculus."
        cl "Were you friendly in this class?"
        r "We were strangers at the beginning of the school year. I honestly don't think I'd ever talked to her before that class. I mean, she's a year below me so we'd never had a class together."
        r "I guess we officially met the day of soccer tryouts. I was skipping Mrs. Green's history class because she never takes attendance, and I entirely lost track of time."
        r "By the time I realized it, I was already late to AP Calc. There's this rule where you can't try out for any sports if you have detention hours, so I was really panicking."
        r "If I was caught coming to class late, I'd miss my senior season on the soccer team."
        cl "High stakes."
        r "Yeah. High stakes."
        jump Reg3

    label Reg3:
        scene classroom with fade_to_black
        "{i}Fifteen minutes into AP Calculus and the seat next to mine was empty once again. A couple times a week, the seat is occupied by a senior with dyed red hair and a bad attitude{/i}."
        "{i}The rest of the time it's empty while the senior is playing hooky.{/i}"
        teacher "Can anyone answer number 3b from the homework? Nobody?"
        teacher "How about you, [mc_name]?"
        mc "Um, I think it is 2π?"
        teacher "Ah, so close! It's actually -2π. Anybody want to help [mc_name] out and explain how we got that answer?"
        "{i}Yep. Calculus was kicking my butt.{/i}"
        r "We have to start by rewriting tan(x) as sin(x)/cos(x)."
        show reg neutral at center with moveinbottom
        "{i}Like magic, the seat next to mine was suddenly no longer vacant.{/i}"
        teacher "Ah, Reg. When did you sneak in here?"
        r "I've been here the entire period."
        teacher "Nice try. Just give me a moment to change your absence to a tardy."
        r "I'm not tardy."
        teacher "You weren't in time for the second bell, so you were tardy."
        r "Seriously, Teach! I've been here the whole time!"
        teacher "I may be old, but I'm not senile. I've been staring at that empty seat for fifteen minutes."
        r "No, I'm serious! Teach, you can't mark me tardy. Not today."
        teacher "[mc_name]. You sit next to Mr. Na every day---correction, you sit next to Mr. Na a couple times a week."
        teacher "I'm sure you can verify whether he was on time or not?"
        mc "Oh, well..."
        menu:
            "Tell the truth":
                #   Jump to correct thing
                jump Reg15a
            "Cover for Reg":
                jump Reg4

    label Reg4:
        mc "Reg was here in time for the second bell."
        teacher "[mc_name], don't lie for your classmate."
        mc "I'm not lying. He even lent me a pencil at the beginning of class because I forgot mine."
        teacher "Oh, really? Is that the pencil in question?"
        "{i}Glancing down, I realized I was holding a blue and purple wooden pencil with a sparkly pink tuft of feathers in place of an eraser."
        mc "...uh... yes. Yes, it is."
        teacher "Reginald? Are you prepared to stand by the statement that this is your pencil?"
        r "Yeah, I am. And don't call me Reginald."
        teacher "So, you came to class, on time, with this incredibly effeminate writing utensil in your possession?"
        "{i}The class snickered.{/i}"
        r "What can I say, I'm an effeminate guy. In fact, [mc_name] here was granted the honor of borrowing my favorite pencil."
        "{i}The snickering evolved into laughs.{/i}"
        r "It's got all my favorite colors---I'm especially fond of pink---and this... thing... on the end. Sparky and soft and shit..."
        teacher "Reg!"
        r "Sorry... sparkly and soft and... stuff..."
        r "You know, it actually is quite useful for putting on my eyeshadow in the morning. Even mascara when I'm feeling particularly flashy."
        "{i}The class roared with laughter.{/i}"
        teacher "Reg, that's enough. We all know you did not lend [mc_name] that pencil."
        r "And why's that? Because you think it's too girly?"
        "{i}The laughter died down.{/i}"
        r "Oh Teach... I thought you were better than that. Discriminating based on archaic gender norms?"
        r "Would you like to send me to the office for a late pass so I can tell the principal exactly how you treat your students?"
        teacher "That's not what---"
        r "Or, perhaps you'd rather just get rid of that tardy?"
        teacher "..."
        r "That's what I thought."
        "{i}Reg winked at me.{/i}"
        r "Continue your lesson. Sorry to interrupt."
        "{i}As the teacher returned to her lesson, murmurs rippled through the classroom. The boy sitting behind me gave Reg a high five. Reg looked at me out of the corner of his eyes and gave me another wink.{/i}"
        mc "{size=-10}Sorry for that.{/size}"
        r "No need to apologize. You saved my ass! If I got marked tardy today, I would have been stuck in detention this evening instead of trying out for the soccer team."
        r "Seriously, I owe you one. The name's Reg."
        mc "[mc_name]."
        r "Well, [mc_name], how can I make it up to you?"
        mc "You know, I could really use some help passing this class."
        r "I hear you, loud and clear... study buddy."
        "{i}Reg scribbled on a piece of paper for a few seconds, folded it, and slid it onto my desk.{/i}"
        r "How about after soccer tryouts this evening?"
        mc "Huh?"
        r "I wrote my address down. Be there at 6:30. Bring your calc book."
        mc "Oh, I... okay. I'll be there!"
        scene interrogation_room with fade_to_black
        show reg neutral at center
        r "From then on we would meet up a couple times a week to work on calc homework. [mc_name] was struggling a bit, but I'm a pro at this stuff."
        r "As the soccer season continued, we started having less and less time to study together, but we still managed every now and then. Each time we met up, she seemed to understand things more and more."
        r "By about halfway through the semester, she was consistently getting B's or higher on her assignments. Pretty soon, she wouldn't need me anymore."
        jump Reg5

    label Reg5:
        scene bedroom with fade_to_black
        show reg neutral at center
        mc "So then you multiply the whole thing by delta x and... simplify like that!"
        r "You got it!"
        mc "Everything is starting to come together! You've really held up your part of the deal."
        r "The deal?"
        mc "I covered for you the day of the soccer tryouts, and you helped me pass this class. I'm really starting to get it though, so... I think you've done your part!"
        r "What? But---"
        mc "You've been so helpful the last few weeks, but I don't want to take up more of your time than I need to."
        mc "I mean, the team will probably qualify for state again, and the team needs you to be focused on training."
        r "But [mc_name]... actually, you know that second order derivative thing we started learning about last week?"
        r "You've got it down, but I still don't. Can we at least keep studying together until I figure it out?"
        mc "Yeah, of course."
        r "And then there's the whole radial coordinate thing later on in the semester, and I already know I'm gonna be confused about that."
        mc "Wait, how do you know that?"
        r "...the syllabus."
        mc "Oh. Well, yeah, I guess that would be fine."
        scene bedroom with fade_to_black
        show reg neutral at center
        mc "So then, take this x here... subtract the 2π from both sides... and... ta-da!"
        r "Hmmmm. That doesn't seem quite right. What if we try... this?"
        mc "Oh, whoops! I keep showing you this wrong."
        r "That's okay. We'll figure it out."
        mc "I mean, sure, but... is it really the best idea for me to be teaching you this? Maybe we should ask someone else for help? Someone who's aready passed AP Calc?"
        r "No, you're doing fine, just try it again."
        mc "It's not a problem really. Nate from the soccer team is really good at math---"
        r "I said no, [mc_name]! You're doing just fine. Don't mess this up."
        mc "What do you mean, \"don't mess this up\"?"
        r "Nothing, just... I don't need Nate's help."
        mc "Well, I could ask someone else? Like Leon?"
        r "I said I don't need anyone else's help. We're doing fine, right?"
        "{i}I don't know why, but Reg seems really on edge about the idea of someone else helping him with calc. But, there's no way I can help him.{/i}"
        "{i}The only way to get him the help he needs is to ask someone else.{/i}"
        menu:
            "What should I do?"
            "Ask Nate for help":
                #   Jump to place
                jump Reg15b
            "Continue helping Reg alone":
                jump Reg6

    label Reg6:
        mc "Sure, I can keep helping you out. But we're probably going to have to start meeting more often, okay?"
        mc "It will take me longer to teach you this stuff than it would take someone like Nate."
        r "I can get on board with that."
        mc "Well, we better get back to it."
        scene interrogation_room with fade_to_black
        show reg neutral at center
        cl "Mr. Na, did you not say you were... let's see... a \"pro\" at this stuff?"
        r "Well, yeah. I kinda am. I took the class last year. The only reason I had to retake it was because of my attendance."
        r "I just taught myself all this shit, so I didn't need to go to class. But, turns out if you aren't in class on the day of the exam, you fail the exam."
        r "And if you fail the final, you fail the class. And if you fail the class, you're stuck taking it again the following year."
        cl "So, did you lie to [mc_name]?"
        r "More like I played dumb."
        cl "Why?"
        r "I liked spending time with her, but people like us don't just... hang out. I'm the rebellious jock type, and she's the secretary of the marching band."
        r "I skip class to smoke joints in the parking lot while she rocks perfect attendance. She's kind to everyone and I'm... abrasive."
        r "She's going to be stuck in the town forever with a husband, two kids, a dog, and a garden while I'm riding a motorcycle across the country."
        r "And yet... the best part of my day was being with her. There's no way I was going to give up our study sessions that easily."
        cl "Did you just see her as a friend or..."
        r "The more time I started spending with her, the more I started thinking maybe it was more than that. I even found myself getting weirdly... jealous."
        r "I'd never really felt that before, so I didn't understand it at first."
        cl "What were you jealous of?"
        r "Not what. Who."
        cl "Then who?"
        jump Reg7

    label Reg7:
        scene school_parking_lot with fade_to_black
        "{i}It's so nice to finally head home after working on that group project for so long. Where did I park again? Ah, over there.{/i}"
        "{i}What? It's seriously not starting? Maybe I should call someone? ...aaaaaaaaand my phone's dead. Arg! Awesome luck today.{/i}"
        "{i}There's got to be someone who could help, right? The soccer fields are nearby, so maybe Leon or one of the other soccer boys can help me out.{/i}"
        scene soccer_field with fade_to_black
        "{i}Looks like they're scrimmaging. I don't want to interrupt or anything, so I guess I could wait till they're on a break. Huh? It looks like there's someone practicing over here by himself. Oh is that...?{/i}"
        show aden smiling at center
        a "Ah! [mc_name]! Hi!"
        mc "Hey Aden. Why are you practicing over here by yourself?"
        a @blushing "Ah, well I'm kind of, um, not very good! I think I was just getting in everyone's way."
        a @smiling "Coach told me to practice dribbling by myself but I just keep tripping over the ball. It's really hard!"
        mc "It sure looks tricky. It's great to see you working so hard!"
        a "Yeah! I just got to keep trying! Practice makes perfect. Soon, I'll be scoring game-winning goals and it'll all be worth it. Do you know how to play?"
        mc "I mean, Leon and I used to play in his back yard, but I've never been on a team or anything."
        a "Oh that's even better than me! Maybe you could help me practice sometime!"
        mc "Yeah, maybe! That might be fun!"
        coach "Alright! 5-minute water break!"
        show aden:
            linear 0.5 leftish
        show leon neutral
        show reg neutral at rightish behind leon
        with moveinright
        r "Hey! [mc_name], what are you still doing here?"
        mc "Oh, my car won't start. I was wandering around to see if anyone could help."
        r "What are you doing with Aden? You guys know each other?"
        mc "Yeah, a little I guess---"
        a "What are you going to do about your car? Do you know how to jump start it? I tried to do that once but something caught fire and my mom was super mad an-"
        r "Just as good at car stuff as you are at soccer, huh---"
        l "Okay, okay yeah I don't really know about jumpstarting but-"
        "{i}Leon looks around and seems to notice someone walking by the field.{/i}"
        r "I might be able to help---"
        l "Hey Serpens! Come here for a sec!"
        show serpens neutral at right with moveinright
        s "Um, hello."
        l "My friend [mc_name]'s car broke down. Are you about to drive home? Do you think you could give her a ride?"
        s "Oh, um. I... uhm. I guess that's fine... as long as [mc_name] is okay with it."
        a "Or if you want... you could stay and help me practice! My mom can give you a ride home when she picks me up."
        menu:
            "What should I do?"
            "Practice with Aden":
                pass
            "Go home with Serpens":
                pass
        mc "I'll---"
        r "Wait, listen... the varsity team is actually short one of our assistant coaches. We could use someone to help toss balls to us. For headers and... stuff."
        l "Wait, who's mi--- {w=0.25}{i}oof!{/i}"
        "{i}Reg elbowed Leon in the gut. Leon glared back with an emotion somewhere between irritation and confusion.{/i}"
        r "We could use your help if we're gonna stand a chance at state."
        a "But... I asked first!"
        r "And you'll stop asking if you know what's best for the rest of the team."
        mc "Guys, stop arguing. I know what I'm gonna do."
        menu:
            "What should I do?"
            "Practice with Aden":
                jump Reg15ci
            "Go home with Serpens":
                jump Reg15cii
            "Help the varsity team practice":
                jump Reg8

    label Reg8:
        mc "I'll help the varsity team."
        a "What? But---"
        s "Hey Aden... you want a ride home, sport?"
        a "...fine."
        hide aden
        hide serpens
        with moveoutleft
        show leon:
            linear 0.5 leftish
        r "Thanks a bunch, [mc_name]."
        mc "It's not a problem, but I feel kinda bad about Aden---"
        r "Hey, don't worry about him. He'll be fine. The actual team, on the other hand, needs all the help we can get if we're gonna stand a chance at state."
        mc "Do you really? I mean, you guys are already so amazing!"
        r "We can never be too prepared! Also... I don't know, it's just nice hanging out with you. Or something."
        mc "Really?"
        r "Obviously. It's a shame we didn't get to know each other until my senior year."
        mc "Yeah, it is a shame, isn't it?"
        r "It is."
        "{i}Reg flashed me one of his award-winning winks as he skillfully used one foot to pop a soccer ball from the ground into his hand and then tossed it to me.{/i}"
        r "Hey, [mc_name]?"
        mc "Yeah?"
        r "Um, I just want to say..."
        mc "What?"
        r "Never mind. It's nothing."
        mc "Well, clearly it's not nothing."
        r "Fine, I just... I wanted to say thanks. For everything."
        r "For using your girly pencil to cover my ass, for studying calculus with me, and for liking me... I don't mean it like that, I mean it as a friend, obviously---"
        mc "My pleasure, Reg."
        r "Okay, enough of this mushy stuff. Let's practice!"
        scene interrogation_room with fade_to_black
        show reg neutral at center
        r "I know, it was selfish. I'll grant you that. I just... it's so hard to control these negative feelings."
        r "It felt like every minute that someone else got to spend with her was one minute that she was growing farther from me."
        cl "And you liked her?"
        r "Yeah. I liked her."
        cl "Did she feel the same way about you?"
        r "Umm..."
        cl "Sorry, let me rephrase... did she say or do anything to indicate she felt the same way about you at that time?"
        r "Well, I don't know. We spent a long time together, but that could mean anything. I guess maybe there was one indication around that time."
        cl "What was that?"
        r "She came to see one of my games."
        cl "Why do you think that was indicating something?"
        r "Seriously? I told you already she was secretary of the marching band, but do you know what else she does with her free time?"
        r "She was in the community service club, drama club, anime club... she makes her own cosplay for God's sake!"
        cl "I don't understand."
        r "People like [mc_name] don't go to sports events to watch sports."
        cl "Why was she there?"
        r "To watch me."
        jump Reg9

    label Reg9:
        scene soccer_field with fade_to_black
        "{i}It's been some time since I took the time to go to a high school soccer game.{/i}"
        "{i}However, I've been spending a lot of time with Reg recently, so I thought it would be pretty nice to see him play. And, to be completely honest, he does make a soccer jersey look pretty good.{/i}"
        show brian neutral at center
        b "[mc_name]?"
        mc "Oh, hey Brian! What brings you here?"
        b "Nothing in particular. Just supporting the guys. What brings you here?"
        mc "Same as you. Supporting the guys."
        "{i}Brian looked at me with one eyebrow raised, his eyes suspicious.{/i}"
        mc "Well, I came to support one guy in particular."
        b "That's what I thought. Leon?"
        mc "Well, of course Leon, but... I've actually been hanging out with Reg recently."
        b "Really I never would have expected someone like you to be friends with someone with his attitude. Or his hair."
        mc "He's nice! And he helps me with calculus."
        b "I knew there was some kind of ulterior motive! Anyway, I'm gonna go chat with the coach before the game starts. Enjoy the game!"
        mc "Thanks, you too!"
        hide brian with moveoutright
        "{i}From his position amid a warm-up drill, Reg caught my eye and winked.{/i}"
        scene soccer_field with fade_to_black
        "{i}{cps=8}Tweeeeeet!{/cps}{/i}"
        "{i}The ref blew the final whistle and raised her hand to indicate Bellington High as the winners. The crowd roared as the team celebrated and shook the hands of the opposing team.{/i}"
        show reg neutral at center with moveinleft
        "{i}The people around me began packing up their foldable chairs and coolers as Reg jogged away from his teammates to join me on the sidelines.{/i}"
        "{i}Before I could react, he gathered me into a bear hug.{/i}"
        mc "Excellent playing, Reg!"
        r "Hell yeah, man! You're like my good luck charm! I scored a personal best today!"
        mc "That was all you, Reg!"
        r "You helped me more than you can imagine."
        "{i}A few seconds passed. Suddenly, Reg realized that he'd been hugging me this entire time and quickly let go, blushing slightly.{/i}"
        r "Sorry about that. Got carried away. Just the adrenaline or something--- {i}oof!{/i}"
        show reg:
            linear 0.5 rightish
        show brian neutral at leftish with moveinleft
        b "{cps=8}Reginaaaaaald!{/cps}"
        "{i}Brian gave him a second hearty slap on the back.{/i}"
        r "Knock it off, Brian!"
        b "Ah, is Reggie in a bad mood?"
        r "Well now that you're here I am!"
        b "Oh, come on! You know you love me!"
        r "I find you irritating."
        b "Come on, Reggie, I came to see you play and this is the thanks I get?"
        r "Oh, you came for me? Well in that case---"
        show reg:
            linear 0.1 center
            linear 0.1 rightish
        with vpunch
        "{i}Reg hit Brian with a solid jab to the stomach to let him know he wasn't buying Brian's bull."
        b "Ow!"
        r "I didn't even hit you that hard."
        b "Still..."
        "{i}Reg rolled his eyes and directed his attention back toward me.{/i}"
        r "You know, I think a game like this deserves a party."
        b "Bruuuuh, that's a great idea!"
        r "You're not invited, Brian. I was thinking something chill at my parent's pace with a few cases of soda and the varsity team... and of course each player is allowed a plus one."
        r "What do you think, [mc_name]?"
        b "That sounds like a snooze-fest! I should throw one of my famous Giang college parties! Booze, hot girls, black lights, and plenty of dark corners to sneak off to---"
        r "Brian, nobody wants to go to your nasty-ass party. Right [mc_name]?"
        b "What!? My parties are legendary! It's the best god damn time in the world followed by the inability to remember any of it."
        b "An absolutely legendary time."
        b "Doesn't that sound fun, [mc_name]?"
        mc "Um, I guess..."
        menu:
            "Whose party sounds more fun?"
            "Brian's":
                jump Reg15d
            "Reg's":
                jump Reg10

    label Reg10:
        mc "I think Reg's party sounds fun."
        b "Pssh... high schoolers. Well I'm at least gonna bring some beer."
        "{i}Brian wandered off toward a crowd of spectators who were still cheering for the team's win.{/i}"
        show reg:
            linear 0.5 center
        hide brian with moveoutleft
        r "What a douche."
        mc "He's not that bad."
        r "...I guess he's not that bad."
        "{i}Reg's eyes wandered to where, several feet away, Brian had lifted a surprised Leon into the air in celebration. As Leon protested, Reg looked back at me.{/i}"
        r "So, about this party... I really want to do it."
        mc "That's great! It sounds fun."
        r "...I'd like you to be my plus one."
        mc "Really?"
        r "Really."
        mc "I'd love to."
        r "Great! So... I was actually wondering if you would want to go with me to the party... as a date?"
        mc "A date?"
        r "Yeah. Like, not as friends."
        mc "Well..."
        r "Before you answer, just... let me speak my bit."
        r "[mc_name], I really like you. Spending time with you makes me really happy, and whenever I'm not with you, I feel like I'm wasting my hours away."
        r "I know we are very different people, and maybe we're too different to make this work out, but... I just really think we would never forgive ourselves if we didn't take a shot."
        "{i}In that moment, Reg's typically tough exterior seemed to melt away. For a moment, his anger turned to genuine affection, and I saw him as someone I could fall in love with.{/i}"
        mc "I think we would, too."
        r "...really?"
        mc "Yes, I really do. I would be happy to be your date."
        "{i}Reg blushed as he tried to contain a smile.{/i}"
        r "Okay. Sounds good. Uh, well,... are you free to hang out right now?"
        mc "I'm Leon's ride home today so I can't, but I'll text you."
        r "Okay. You better not forget."
        mc "I won't."
        scene interrogation_room with fade_to_black
        show reg neutral at center
        cl "So, you and [mc_name] were together romantically?"
        r "Well, we weren't {i}together{/i} together. We'd have to see how the party goes."
        cl "And how did the party go?"
        r "Well, someone died."
        cl "I meant with respects to your relationship with [mc_name]."
        r "Yeah, I think we were a bit preoccupied by, ya know, someone dying."
        cl "Reg, I know it's tough to talk about, but I really need you to answer the question honestly."
        r "Fine. I'll tell you what happened."
        jump Reg11

    label Reg11:
        scene house_party_day with fade_to_black
        show reg neutral at center
        r "Thanks for volunteering to come early to help me set up."
        mc "Yeah, no problem!"
        r "I bet none of your other first dates involved vacuuming a five bedroom home, hehe!"
        mc "Actually, this is my first date ever."
        r "What? Really? If I knew that I would have bought you lobster or something!"
        mc "It's fine, haha! I like spending time with you, regardless of what we're doing."
        r "Well, I won't stand for it. We have some time before the party starts, so I'm going to make sure your first date is how a first date should be."
        r "Finish setting out the snacks for the party, and I'll be back in ten minutes!"
        hide reg with moveoutright
        "{i}Reg grabbed his keys and sprinted out the door before I could protest.{/i}"
        scene house_party_day with fade_to_black
        show reg neutral at center
        r "Okay, you can open your eyes."
        "{i}In front of me was a scene right out of a rom-com. A small table covered in a white sheet was surrounding by two chairs and topped with plates, cups, utensils, a candle, and a single rose in a vase.{/i}"
        "{i}Upon closer inspection, the rose appeared to be made of chocolate and covered in foil.{/i}"
        r "The 7-11 on the corner didn't have any real flowers, but I did my best with what they had."
        r "Come sit! I'm going to treat you to the three-course meal of your dreams... or at least the closest thing that a convenience store could supply. To start... Caesar salad!"
        "{i}Reg reached into a plastic grocery bag and pulled out two pre-packaged salads and a handful of dressing packets.{/i}"
        r "And for the main course... the seafood special!"
        "{i}Reg reached into the plastic bag and pulled out a can of clam chowder, a bag of Swedish fish, and a package of goldfish crackers.{/i}"
        r "And for desert... pie!"
        "{i}Reg turned the bag upside down and two small Hostess pies fell onto the table.{/i}"
        r "I know it's not exactly high-end, but---"
        mc "I love it."
        r "Huh?"
        mc "I love it. This is the best first date I could have hoped for."
        "{i}Reg looked at me with surprise, which quickly turned to embarrassment, then to a smile.{/i}"
        "{i}He reached a hand cautiously toward my face, paused, and then set it against my cheek. I felt my face flush under his touch.{/i}"
        "{i}Slowly, his fingers dropped from my face to my shoulder, then all the way down my arm to my hand where they intertwined with my own. Gently, he tugged my hand, pulling my upper body toward his.{/i}"
        hide reg with moveoutleft
        "{i}Our lips met for the first time, and my heartbeat crescendoed. For a moment, time froze. Then, as soon as it began, it was over, and Reg pulled away again.{/i}"
        show reg neutral at center with moveinleft
        r "[mc_name]?"
        "{i}My heart was beating so fast, I was afraid he would hear it.{/i}"
        mc "Yes?"
        r "Will you go out with me?"
        mc "Um, you mean---"
        r "Yeah, I do mean."
        mc "Well..."
        menu:
            "Be Reg's girlfriend?"
            "Yes":
                jump Reg12
            "No":
                jump Reg15e

    label Reg12:
        mc "Yeah, Reg. I'll be your girlfriend."
        "{i}Reg blushed, forcing a straight face.{/i}"
        r "Okay. Sweet."
        mc "Shall we eat?"
        r "Yeah."
        scene interrogation_room with fade_to_black
        show reg neutral at center
        cl "So, the two of you entered a romantic relationship on April 27?"
        r "Yeah, the same day as my party."
        cl "So what happened between you and [mc_name] the night of the party?"
        r "Well, we decided that the party would be a good place to go public---"
        cl "Go public?"
        r "Yeah. Like, tell our friends we were dating. You know, our big reveal."
        cl "Understood. Please continue."
        r "Everyone on the varsity soccer team was invited. I even invited a couple alums, like Brian."
        cl "You're talking about Brian Giang?"
        r "Yes."
        cl "Thank you, please continue."
        r "So, I was really excited for all the guys to see me with a pretty girl on my arm."
        cl "Who are you referring to when you say \"all the guys?\""
        r "The varsity soccer team. Nate, Leon, the rest. Do you want me to give you the roster?"
        cl "No, that's fine. Please continue."
        r "No, this is good. Do keep interrupting. At this rate I'll be here through graduation."
        cl "I'm sorry, Reginald. The floor is yours."
        r "..."
        cl "Sorry... Reg."
        r "There you go. As I was saying, I was really excited to see everyone there and to announce my new girlfriend."
        r "So, as you can imagine, I was pretty peeved when a certain someone decided not to show up..."

    label Reg13:
        scene house_party_night with fade_to_black
        "{i}Base thumping, people dancing, the smell of the booze Brian brought filling the air. The varsity soccer team sure knows how to party!{/i}"
        show reg neutral at center
        r "You having a good time, [mc_name]?"
        mc "Yeah!"
        r "Awesome. Have you seen Leon?"
        mc "No, I haven't. Sorry."
        r "Hey guys! Has anyone seen Leon?"
        "{i}There was no response from the masses.{/i}"
        r "What the hell? It's almost 10pm. He should be here by now."
        mc "Have you texted him?"
        r "I'm just gonna give him a call."
        "{i}Reg pulled out a phone, searched his contacts for Leon, and pressed call. The phone rang twice, and then Leon answered in a groggy voice.{/i}"
        l "Hello?"
        r "Were you sleeping, dude?"
        l "Uh, yeah?"
        r "What the fuck, man!? Why aren't you here?"
        l "Where?"
        r "At my party, dumbass!"
        l "That's happening?"
        r "Yeah, it's happening! You said you'd be here!"
        l "Yeah, but---"
        r "Get your ass over here, dude!"
        l "I'm sorry dude, Aden said it was cancelled."
        r "Aden!? That scrawny freshman kid who embarrassed himself at tryouts? He wasn't even invited!"
        r "Why the hell would he tell you it was cancelled!? You're so full of shit, Leon!"
        "{i}Reg kicked a table leg.{/i}"
        mc "Reg, calm down!"
        r "Leon, you are literally the only person on the team who didn't show up tonight. You know how much work I've put into planning this! You know that I've been looking forward to this!"
        r "I even have a really important announcement, and you couldn't even be bothered to come. "
        l "Reg, it isn't like that---"
        r "Just shut up and be here within the next 20 minutes. And you're gonna make this up to me, okay?"
        "{i}Reg hung up the phone and aggressively shoved it into his pocket.{/i}"
        mc "You alright?"
        r "Yeah, I'm just pissed off. Forgetting is one thing, but lying about it? Why would he do that?"
        mc "I'm sure he didn't mean it. Let's just go enjoy the party, okay?"
        r "Okay."
        scene house_party_night with fade_to_black
        show reg neutral at center
        r "Jeez, do you see that?"
        mc "See what?"
        r "Leon finally showed up... he's been here under and hour and he's already wasted."
        mc "Really? He doesn't even drink."
        r "Well, apparently he does."
        mc "You're being kind of hard on him, aren't you?"
        r "Let's just forget it and have a good time."
        l "{cps=8}Loooooook{/cps} who it is!"
        show reg:
            linear 0.3 leftish
        show leon neutral at rightish with moveinright
        "{i}Leon made his way through the crowd to where Reg and I were. He clumsily put an arm around my shoulder.{/i}"
        l "Juuuuuust the lady I was hoping to see!"
        mc "Hey, Leon. You okay?"
        l "I'm greeeeeat! So good to see you, mmmm... [mc_name]"
        "{i}Leon laughed and draped himself on me more aggressively. Reg stepped toward him with a glare.{/i}"
        r "What's the big idea, Leon?"
        mc "Reg, it's okay---"
        l "No- nothing, maaaan. Just hanging with m'{cps=8}laaaaady!{/cps}"
        "{i}Leon sloppily leaned in an kissed me on the cheek. Reg's face turned red, and he grabbed Leon's jacket to pull him off of me.{/i}"
        r "Hey! That's my girlfriend, you asshole!"
        mc "Reg, please let him go! He's just drunk."
        r "That's no excuse for touching you without your consent!"
        l "Huuuuuh? Girlfriend?"
        mc "Yeah. Reg and I are together, Leon."
        "{i}Leon's face filled with disappointment as he staggered a few steps backward, escaping from Reg's grasp.{/i}"
        l "Together?"
        mc "We were trying to find a better way to announce it, but yeah."
        l "But... I... I don't understand."
        mc "What don't you understand?"
        l "I don't- I don't understand why you don't like meeeeee."
        "{i}I was too in shock to respond. Leon looked so heartbroken. His entire being looked deflated. Utterly devastated.{/i}"
        "{i}I had no idea how to respond. Suddenly Leon was on the ground and Reg was standing over him, bellowing into his face.{/i}"
        r "What the fuck are you doing, man? You're supposed to be happy for me, and instead you've ruined this entire night!"
        "{i}The sounds of the crowd died down as everyone turned their attention to the drama unfolding on the dance floor.{/i}"
        r "You blew off my party for God knows what reason. You lied to me about it."
        r "You finally showed up, only to get shit-faced and slobber all over my girlfriend. And now you have the audacity to lay on the floor like you're a victim!"
        r "All evening you've been acting like a terrible friend!"
        "{i}Leon looked away shamefully.{/i}"
        r "Pick yourself up. Pick yourself up!"
        "{i}Brian helped Leon to his feet.{/i}"
        r "And for God's sake, stop drinking!"
        hide leon with moveoutright
        show reg:
            linear 0.3 center
        "{i}Leon walked into the crowd, his head down. Reg turned back toward me.{/i}"
        r "I'm sorry to yell in front of you."
        mc "Are you sure you aren't being too hard on him?"
        r "No. He was out of line."
        mc "Okay... do you want to go dance?"
        r "I'm not really in the partying mood anymore."
        mc "I understand."
        "{i}Reg gently put a hand around my waist.{/i}"
        r "I care about you a lot, so... it makes me really angry to see someone... touching you like that."
        mc "Yeah, but---"
        r "I know, I know. I have to work on that."
        "{i}Reg pulled me closer.{/i}"
        r "Hey... do you want to maybe... "
        "{i}Reg leaned in to whisper in my ear.{/i}"
        r "...go upstairs with me?"
        "{i}My heart skipped a beat and my face flushed. Reg's lips brushed my cheek and I felt myself wanting to be drawn deeper into his arms.{/i}"
        show leon neutral at left with moveinleft
        "{i}Just then, I made eye contact with Leon across the room. He stared for a moment with an expression I couldn't understand, then quickly turned away and disappeared into the crowd again.{/i}"
        hide leon with moveoutleft
        mc "Reg, I think you should talk to Leon."
        r "What? Why?"
        mc "The two of you have been friends for years. I hate seeing you two at odds."
        r "Please, let's not talk about this. I can talk to him tomorrow."
        r "Please. Come upstairs."
        menu:
            "What should I do?"
            "Go upstairs with Reg":
                jump Reg14
            "Encourage Reg to make up with Leon":
                jump Reg15f

    label Reg14:
        mc "Okay. Let's go upstairs."
        "{i}Reg tugged gently on my hands and led me up the stairs and into his bedroom, locking the door behind him. He didn't turn on the light.{/i}"
        "{i}Carefully, he led me to his bed, and we sat down on the foot of it. His hands wandered up my arms and came to rest on either side of my neck.{/i}"
        "{i}Through the dark I could see him look into my eyes for just a moment, then he pulled me into a deep kiss. I closed my eyes and let our bodies embrace each other.{/i}"
        scene interrogation_room with fade_to_black
        show reg neutral at center
        cl "So, did you and [mc_name] have sexual intercourse that night?"
        r "I'm not one to kiss and tell."
        cl "Very well. Were you with [mc_name] through the night of April 27?"
        r "Yes. Through to the morning. She left around 6am."
        cl "Were you with anyone else that night?"
        r "Nope. [mc_name] and I were in my room until morning."
        cl "Do you know anything about the current whereabouts of [mc_name]?"
        r "I do not."
        cl "Thank you, Mr. Na. No further questions."
        return

    label Reg15a:
        mc "He just walked in."
        "{i}The teacher shrugged at Reg while he glared daggers at me. She quickly changed her attendance sheet, then resumed teaching.{/i}"
        r "Thanks for that, asswipe."
        mc "Maybe try being on time?"
        "{i}He turned to face me, raising his voice slightly.{/i}"
        r "I was supposed to have soccer tryouts this afternoon, and now I won't be allowed to go because I'll be in detention. I'm gonna miss my senior year on the team, so yeah, thanks for that, asswipe."
        teacher "Reg, are you distracting your classmates?"
        r "Not as much as you're distracting them by incorrectly replacing sin(-x) with -csc(x)."
        "{i}The teacher turned to examine the board, then quickly started erasing her work. Reg gathered his belongings and headed toward the door.{/i}"
        teacher "Hey, Reg, where are you going?"
        r "Out."
        hide reg with moveoutright
        "{i}Reg disappeared into the hallway, making sure to flip me the bird on his way out. He's definitely a charmer.{/i}"
        scene interrogation_room with fade_to_black
        show reg neutral at center
        r "I didn't talk to her much after that. We just saw each other in class. We eventually ended up on decent terms, but we weren't friends or anything."
        cl "Does that mean she didn't go to your party on April 27?"
        r "No, she didn't."
        cl "Did you see her at all on April 27?"
        r "No. I was throwing a party."
        cl "And who can verify where you were during the party?"
        r "Literally anyone on the varsity soccer team. Except Leon."
        cl "Okay, that will be all. Thanks for your time Mr. Na."
        r "Thanks for wasting my time, it was my pleasure."
        hide reg with moveoutright
        cl "He's definitely a charmer."
        return

    label Reg15b:
        mc "I'm gonna call Nate right now and ask for his help."
        r "Don't worry about it."
        mc "It's no problem---"
        r "I said don't worry about it!"
        r "You're clearly either playing dumb or you really don't understand what's going on here, and if you don't understand what's happening by now, then you are a hopeless cause."
        mc "I thought I was starting to get it."
        "{i}Reg burst into exasperated laughter.{/i}"
        r "Oh my God! Are you seriously this dense?"
        mc "I thought---"
        r "I think we should study on our own from now on, okay?"
        mc "But---"
        r "Please, [mc_name]. Just leave."
        hide reg with moveoutright
        "{i}In silence, I left. We didn't study together again.{/i}"
        scene interrogation_room with fade_to_black
        show reg neutral at center
        cl "I'm confused... why did you cut off the study sessions?"
        r "I was only doing them in the first place because I liked her. Clearly she didn't like me back or else she would have picked up on it."
        cl "Did the two of you at least remain friends?"
        r "We were friendly. It took a little while for me to get over her, but after that we would chat in class every now and then."
        r "We weren't close friends or anything though."
        cl "Did she go to your party on April 27?"
        r "No, she didn't."
        cl "Did you see her at all on April 27?"
        r "No. I was throwing a party."
        cl "And who can verify where you were during the party?"
        r "Literally anyone on the varsity soccer team. Except Leon."
        cl "Okay, that will be all. Thanks for your time Mr. Na."
        r "Thanks for wasting my time, it was my pleasure."
        hide reg with moveoutright
        cl "He's definitely a charmer."
        return

    label Reg15ci:
        mc "I will stay and help you practice, Aden."
        a "Really!? This is gonna be so much fun!"
        mc "It's going to be hard work though, Aden. You have to be prepared to train hard if you want to be as good as the varsity players."
        a "I will! I promise! Thank you so much!"
        r "[mc_name], are you sure?"
        s "Yeah, I can drive you home, no problem."
        mc "No, you go ahead Serpens. I appreciate the offer, but I'm okay."
        r "Alright, whatever you say..."
        scene interrogation_room with fade_to_black
        show reg neutral at center
        r "I didn't talk to her much after that. I mean, obviously she was fonder of Aden than she was of me. We remained friends, but nothing else really happened."
        cl "Does that mean she didn't go to your party on April 27?"
        r "No, she didn't."
        cl "Did you see her at all on April 27?"
        r "No. I was throwing a party."
        cl "And who can verify where you were during the party?"
        r "Literally anyone on the varsity soccer team. Except Leon."
        cl "Okay, that will be all. Thanks for your time Mr. Na."
        r "Thanks for wasting my time, it was my pleasure."
        hide reg with moveoutright
        cl "He's definitely a charmer."
        return

    label Reg15cii:
        mc "I have a lot of homework to do, so I'm gonna just catch a ride with Serpens."
        a "Oh, okay... well maybe another time!"
        mc "Yeah. Maybe another time."
        scene interrogation_room with fade_to_black
        show reg neutral at center
        r "I didn't talk to her much after that. I mean, obviously she was fonder of Serpens than she was of me. We remained friends, but nothing else really happened."
        cl "Does that mean she didn't go to your party on April 27?"
        r "No, she didn't."
        cl "Did you see her at all on April 27?"
        r "No. I was throwing a party."
        cl "And who can verify where you were during the party?"
        r "Literally anyone on the varsity soccer team. Except Leon."
        cl "Okay, that will be all. Thanks for your time Mr. Na."
        r "Thanks for wasting my time, it was my pleasure."
        hide reg with moveoutright
        cl "He's definitely a charmer."
        return

    label Reg15d:
        mc "Brian's party sounds fun!"
        b "Well, I promised only the hottest girls would be at my party, so of course you'll be there."
        r "Brian, you're not even on the team anymore! I'm going to throw the varsity team party, and you can't do anything about it because you.{w=0.2} Are.{w=0.2} Not.{w=0.2} On.{w=0.2} The.{w=0.2} Team!"
        b "Okay, fine. Chill out."
        r "Neither of you are invited."
        mc "Hey, no need to be like that, Reg."
        r "Well, you clearly like Brian more than you like me, so just hang out with him that night. I'm sure you guys will have a great time getting drunk and looking at hot girls."
        mc "Reg---"
        r "Piss off."
        hide reg with moveoutleft
        show brian:
            linear 0.3 center
        "{i}Reg stormed off into a crowd of cheering fans as Brian and I looked at each other in shock. I don't fully understand what set him off, but I don't know as I'll be able to repair it before the party.{/i}"
        scene interrogation_room with fade_to_black
        show reg neutral at center
        r "It seems kind of silly now, but at the time I was really jealous of Brian."
        r "I was still mad about it when the party rolled around, so I didn't invite either of them, but since then we've all made up."
        cl "Does that mean she didn't go to your party on April 27?"
        r "No, she didn't."
        cl "Did you see her at all on April 27?"
        r "No. I was throwing a party."
        cl "And who can verify where you were during the party?"
        r "Literally anyone on the varsity soccer team. Except Leon."
        cl "Okay, that will be all. Thanks for your time Mr. Na."
        r "Thanks for wasting my time, it was my pleasure."
        hide reg with moveoutright
        cl "He's definitely a charmer."
        return

    label Reg15e:
        mc "I'm sorry, but... I just don't feel the same way."
        r "...are you serious?"
        mc "I'm sorry."
        r "Why did you say yes to a date then?"
        mc "I figured it was a friend date or something."
        r "Why on earth would you assume it was a friend date? Who even wastes their time on friend dates anyway?"
        mc "I'm sorry, Reg---"
        r "Did you seriously not know how I feel about you?"
        mc "No, I didn't."
        r "I've been throwing and throwing and throwing hints, and seriously nothing stuck?"
        mc "I'm sorry Reg, but I just didn't know!"
        r "I don't know if it's more upsetting to think that you led me on only to throw me away like garbage, or to think that you are actually so dense that you couldn't tell how I feel! Seriously!"
        mc "Reg---"
        r "You should leave."
        mc "But---"
        r "Now! And don't come back for the party. Don't come back. Ever."
        scene interrogation_room with fade_to_black
        show reg neutral at center
        r "She really broke my heart. I seriously thought she felt the same way toward me. It ruined the whole party for me."
        r "Liking someone who doesn't like you back... it hurts."
        cl "Did she come back for the party?"
        r "No. She may be dense, but she was smart enough not to do that."
        cl "Do you still have feelings for her?"
        r "Someone important to me once said “you cannot stop loving someone.” Now, I don't know much about love, but whatever I felt for [mc_name]... I don't think I can stop feeling that."
        cl "Did you see her at any other point the night of April 27, 2019 or at any point after that?"
        r "No. That was the last I saw her."
        cl "So, [mc_name] remains without an alibi. Reg, can anyone verify your whereabouts that night?"
        r "Literally anyone on the varsity soccer team. Except Leon."
        cl "Okay, that will be all. Thanks for your time Mr. Na."
        r "Thanks for wasting my time, it was my pleasure."
        hide reg with moveoutright
        cl "He's definitely a charmer."
        return

    label Reg15f:
        mc "You should really try to make up with Leon. It's not good to let these things linger for too long. "
        r "Please, [mc_name]... I don't want to ruin the magic of the night."
        mc "It'll be ruined if the party ends and you guys aren't friends anymore."
        r "Is Leon really your top priority right now? I'm baring myself to you right now, and you're focused on another guy?"
        mc "No, Reg---"
        r "First he throws himself all over you, then he basically confesses his love for you, and now you want to go run to him to make sure he's okay? Do you like him, or do you like me?"
        mc "Reg, stop. You're misinterpreting things."
        r "Oh, jeez, you can't even give me a straight answer. God dammit! You do like him, don't you?"
        "{i}Reg laughs sarcastically.{/i}"
        r "Guess what, [mc_name]? I knew all along how he feels about you. He talks about you all the time, and he's been doing that for years."
        r "You wanna know why I didn't tell you? I figured that if you knew he liked you that you would choose him over me."
        r "He's known you since you were kids, so he's got a huge advantage. The only reason I had a leg up on him was because I wasn't afraid to go after what I like."
        r "I made it clear that I liked you, so you saw me as an option. Leon didn't communicate his feelings, so you never saw him as anything more than a friend. Well, looks like I lost my advantage."
        "{i}A loud bang drew my attention back to the dance floor. Leon had opened the front door with so much force that it hit the wall and bounced back against him.{/i}"
        "{i}His face was red and there were tears on his cheeks. He stumbled out into the night, leaving the door open behind him.{/i}"
        mc "Reg, Leon just left and he looked really upset."
        r "Are you seriously bringing up Leon once a-fucking-gain?"
        mc "Reg, I think this is serious. He's in no state to be wandering around on his own."
        r "Then I give up. Go after him. Go to your new boyfriend."
        r "Get married. Have some kids. I don't care anymore."
        mc "Reg, your behavior is really selfish."
        r "One more reason to dump me and go date Mr. Perfect Leon."
        mc "Reg, I'm going to go check on Leon. It's not because I like him, okay? I like you! I'm dating YOU, Reg!"
        mc "But just because I'm not dating Leon doesn't mean I can let him be in danger. Please, Reg. Be here when I get back."
        scene interrogation_room with fade_to_black
        show reg neutral at center
        r "She never came back."
        cl "I'm sorry, Reginald."
        r "It's still Reg."
        cl "My apologies, Reg."
        r "I just... I felt so useless. I'd finally managed to find a person who I really cared about. She made me a better person, and I felt happiest when she was around."
        r "I also felt furious. Leon had managed to ruin my party and take away the one person who meant everything to me."
        cl "Did this anger cause you to consider being violent toward him?"
        r "What? Of course not!"
        cl "..."
        r "You aren't seriously suggesting something, are you?"
        cl "Is there anyone who can verify your location for the rest of the night? After Leon and [mc_name] left?"
        r "Well, no... I was so upset that I went to my room to be alone."
        cl "Reginald Na remains without an alibi. Thank you for your time, Mr. Na. You'll be hearing from us shortly."
        r "You can't be serious. I didn't hurt anyone! Please, you have to believe me!"
        cl "Mr. Na, I recommend you refrain from speaking until you've had a chance to talk with your lawyer."
        r "My lawyer? No, this isn't happening."
        cl "You will be escorted from the premises now."
        r "This isn't happening..."
        hide reg neutral with dissolve
        r "This isn't happening..."
        return



    return

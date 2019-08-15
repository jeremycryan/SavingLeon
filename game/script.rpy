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

define a = Character("Aden", image="aden", callback=partial(bounce_callback, "aden"), color="#CA85EA")
define r = Character("Reg", image="reg", callback=partial(bounce_callback, "reg"), color="#EF4F5F")
define l = Character("Leon", image="leon", callback=partial(bounce_callback, "leon"), color="#FFFFFF")
define n = Character("Nate", image="nate", callback=partial(bounce_callback, "nate"), color="#6CDD78")
define s = Character("Serpens", image="serpens", callback=partial(bounce_callback, "serpens"), color="#8693E8")
define b = Character("Brian", image="brian", callback=partial(bounce_callback, "brian"), color="#EDED80")
define boy = Character("Boy", image="aden", callback=partial(bounce_callback, "aden"), color="#CA85EA")
define cl = Character("Court Lady", color="#BFBFBF")
define mc = Character("[mc_name]", color="#E285E2")
define coach = Character("Coach", color="#BFBFBF")
define teacher = Character("Teacher", color="#BFBFBF")
define kelsie = Character("Kelsie", color="#BFBFBF")

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
        "Aden: Practicing by himself":
            jump Aden5
        "Aden: Proven me wrong":
            jump Aden11
        "Reg: Study Buddy":
            jump Reg5
        "Reg: First date":
            jump Reg11
        "Brian: Always time for a coffee pun":
            jump Brian5
        "Brian: One guy in particular":
            jump Brian11
        "Leon: The one":
            jump Leon5
        "Leon: We lost":
            jump Leon11

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
        "{i}Suddenly, two boys in athletic attire had appeared. One of them had put Leon in a headlock that he was struggling to escape from, and the other was slowly shaking his head in both humor and disappointment.{/i}"
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
                jump Aden15a

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
                jump Aden15b

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
                jump Aden15c

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
                jump Aden15d

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
        jump Aden11

    label Aden11:
        scene soccer_field with fade_to_black
        show aden at leftish
        show reg at rightish
        r "Hey, Aden... nice playing today."
        a "Thanks! I had so much fun!"
        r "Uh... I wanted to say... sorry for the things I said the day of tryouts. That was pretty uncool of me."
        a "Oh, that's okay! I appreciate your apology though!"
        r "You've certainly proven me wrong."
        "{i}Reg started to walk away, then paused and looked back over his shoulder. {/i}"
        r "Uh, I know you're not officially on the varsity team, but do you want to come to the party I'm throwing for the varsity team?"
        a "What?! Really?! Yeah, I'd love to!!!"
        r "Great! It's on April 27. You're allowed a plus one."
        a "Thanks, Reg!"
        hide reg with moveoutright
        show aden:
            linear 0.3 center
        a "Did you see that?! I just got invited to a party! And it's a varsity team party!"
        mc "I saw! Good for you, man."
        a "You'll be my plus one, right?"
        mc "Well..."
        menu:
            "Be Aden's plus one to the party?"
            "Yes":
                jump Aden12
            "No":
                jump Aden15e

    label Aden12:
        mc "Sure, I'll go with you!"
        a "Awesome! It's a date!"
        "{i}Aden suddenly realized what he's said. His eyes widened and his cheeks flushed.{/i}"
        a "I didn't mean--- sorry, I just---"
        mc "Aden..."
        a "Yeah?"
        mc "... it's a date."
        "{i}I smiled and felt my face get hot. Aden blushed back at me.{/i}"
        a "Uh, okay... a date it is then!"
        "{i}Suddenly, Aden's face turned serious.{/i}"
        a "Oh, no..."
        mc "What's wrong?"
        a "What about Leon?"
        mc "What do you mean?"
        a "He is really into you."
        mc "I don't know about that---"
        a "It would probably kill him to see you go with me."
        mc "Really?"
        "{i}Aden blushed.{/i}"
        a "I mean... it would kill me if you went with him."
        "{i}I blushed back, but forced myself to focus on the situation at hand.{/i}"
        mc "I hadn't even thought about that."
        a "I can't hurt him like that."
        mc "So... should we not go together."
        a "No, we can still go together. I just have to make sure Leon isn't there."
        mc "What???"
        a "Don't worry, I'll take care of it!"
        mc "I really don't think this is a good idea..."
        "{i}Aden ignored me.{/i}"
        a "Hey, you wanna grab a drink at Coffee Waves?"
        mc "Uh, I'm Leon's ride home so I can't today. Hey Aden..."
        mc "Don't do anything irrational."
        a "I won't! See you this weekend."
        mc "..."
        mc "I can't wait."
        show interrogation_room with fade_to_black
        show aden neutral at center
        a "I was so excited! My first ever date! It was going to be so awesome!"
        a "But... Leon. I thought back to Brian's story and I came up with a plan that was perfect! I could be with the girl I liked but without hurting my friend!"
        cl "What was the plan?"
        a "I would text Leon the day of the party to tell him that Reg had to reschedule the party so I was helping him pass on the news."
        a "Leon would skip, believing that the party was not happening, and I could go with [mc_name] without worrying about him seeing!"
        cl "..."
        a "I had his best interests in mind! I swear, I couldn't have known how it would turn out."
        a "I never wanted my friend to be hurt... this was the only way I could think to no break his heart."
        cl "So, what happened the night of the party?"
        a "Tragedy."
        cl "Can you tell me about it."
        a "..."
        cl "I know it's tough, but I need to understand all the events leading up to the homicide."
        a "It started out beautifully..."
        jump Aden13

    label Aden13:
        scene house_party_night
        "{i}Base thumping, people dancing, the smell of the booze Brian brought filling the air. The varisty soccer team sure knows how to party!{/i}"
        show aden neutral at center
        a "Ugh, this punch tastes aweful! Have you tried it?"
        mc "Aden, that has alcohol in it."
        a "What? But that's illegal!"
        "{i}He frantically dumped his drink in the garbage.{/i}"
        a "They should have some soda or something..."
        mc "Hey, Aden..."
        a "Huh?"
        mc "I haven't seen Leon yet... you didn't do anything did you?"
        a "Uh..."
        "{i}I suddenly spotted Leon come through the front door, a look of irritation on his face. {/i}"
        a "Oh, look! He just got here!"
        "{i}Leon caught Aden's eye and started making his way through the crowd in our direction. {/i}"
        a "[mc_name], we should go."
        mc "What did you---"
        "{i}Before I could protest, Aden had grabbed my hand and pulled me up the stairs and into an empty bedroom. {/i}"
        scene bedroom_night with fade_to_black
        show aden neutral at center
        "{i}The lights were off and Aden's hand was over my mouth. Through the crack  under the door, I way Leon's shadow appear, hesitate, then head back down the stairs. {/i}"
        "{i}Aden breathed a sigh of relief and removed his hand from my mouth. He was standing so close to me I could feel his breath gently on my neck. {/i}"
        "{i}As my eyes adjusted to the darkness, I could see him staring into my eyes with an unreadable expression. A moment passed as I felt my heart flutter. {/i}"
        "{i}Suddenly Aden no longer looked like a child of 15 full of naïvety and ignorance, but like a man of passion and kindness. I suddenly saw him as someone I could see myself falling in love with.{/i}"
        menu:
            "Kiss him":
                jump Aden14
            "Encourage him to make up with Leon":
                jump Aden15f

    label Aden14:
        "{i}I leaned my head toward him slowly and pressed my lips against his. He tensed up with shock for a moment, then let himself relax into it. {/i}"
        "{i}His hands tentatively cupped my face, then wandered to my lower back. For a moment that felt like eternity, we remained there. Then he slowly pulled away. {/i}"
        a "...that... was my first kiss."
        mc "...mine, too."
        "{i} He pulled me close again, and we continued exploring, carefully, these sensations that were new to us both.{/i}"
        scene interrogation_room with fade_to_black
        show aden neutral at center
        cl "Did you and [mc_name] have sexual intercourse that night?"
        a "Objection: relevance? Sustained."
        cl "Aden, for the last time this is not a courtroom. You also cannot object because you are not a lawyer. You also cannot sustain your own objection because you are not a judge."
        a "..."
        cl "Nonetheless, I will allow you not to answer that question. What happened after that?"
        a "We were in that bedroom for a while, and when we returned to the party, everyone had started to hear bits and pieces about what happened."
        cl "About what happened between you and [mc_name]?"
        a "No, of course not! About... you know..."
        cl "The death of your friend."
        a "Yeah."
        cl "So, you were with [mc_name] while the crime occurred?"
        a "Yes."
        cl "And can anyone else verify this?"
        a "Sure... just about anyone at the party can tell you we went upstairs together and came back down later. Plus, Reg's place has a security camera on the outside of the house, so we couldn't have realistically snuck out the window or anything ."
        cl "Okay. I have no further questions at this time. Mr. Li, thank you for your time."
        a "Are [mc_name] or I in trouble?"
        cl "I am not at liberty to discuss anything more at this time."
        a "Oh, okay."
        cl "Speaking of... do you know anything about [mc_name]'s current whereabouts?"
        a "No. I haven't seen her since the party."
        cl "Okay. Thanks for your cooperation, and we will be in contact if necessary."
        return

    label Aden15a:
        mc "You should keep up with the saxophone! With talent like yours, you could really go somewhere."
        a "But soccer looks like so much fun..."
        mc "It would be such a shame for you to deprive the world of your music."
        a "..."
        "{i}Defeated, Aden began erasing his name from the sign up sheet. Then, without a word, he disappeared down the hallway.{/i}"
        hide aden with moveoutright
        show interrogation_room with fade_to_black
        show aden neutral at center
        cl "So, you {i}weren't{/i} on the soccer team?"
        a "...no. I wasn't."
        a "It's like I was for the few glorious seconds my name was on that sheet, but... not really."
        cl "So, how did you know [mc_name]?"
        a "That was it. We interacted the day of the soccer tryouts and that's it. We didn't talk after that."
        cl "And you say it was... \"transformative\"? Can you explain?"
        a "I had been bored with band, but after that day I was resolved to put everything I had into my playing. And then a few months later... I made it into the All State Band!"
        cl "But, just to be clear, you were not on the soccer team and you did not have any further interaction with [mc_name]?"
        a "That's right!"
        cl "Were you present at Reginald Na's party on April 27, 2019? "
        a "No. "
        cl "And were you with [mc_name] the evening of April 27, 2019?"
        a "No."
        cl "Were you with anyone the evening of April 27, 2019?"
        a "No, I don't think so."
        cl "Thank you, Mr. Li, we have everything we need. [mc_name] remains without an alibi the night of the crime."
        a "Wait, there's no way she did it! She's w---"
        cl "In addition, Aden Li remains without an alibi the night of the crime. Mr. Li, thank you for your cooperation. You will be escorted out shortly."
        a "...there's no way... is there?"
        return

    label Aden15b:
        mc "I have a lot of homework to do, so I'm gonna just catch a ride with Serpens."
        a "Oh, okay... well maybe another time!"
        mc "Yeah. Maybe another time."
        show interrogation_room with fade_to_black
        a "We never did end up practicing together. In fact, we barely saw each other at all after that day."
        a "I'd still consider us friends though! She was always nice to me when we passed each other in the hall."
        cl "So, the two of you never had a relationship that could be considered something more than friends?"
        a "What? No, of course not. I mean, she's kinda cute but..."
        cl "But what?"
        a "But she clearly wasn't interested in me."
        cl "So I assume you were not with her on the night of April 27, 2019? "
        a "The night of Reg's party? No, not at all! I wasn't even invited because I wasn't on the varsity team."
        cl "Oh, so you weren't at the party at all?"
        a "No."
        cl "Where were you the evening of April 27, 2019?"
        a "At home studying."
        cl "Were you with anyone, or did anyone know where you were?"
        a "No, I was alone. My parents were out for the evening."
        cl "Thank you, Mr. Li, we have everything we need. [mc_name] remains without an alibi the night of the crime."
        a "Wait, there's no way she did it! She's w---"
        cl "In addition, Aden Li remains without an alibi the night of the crime. Mr. Li, thank you for your cooperation. You will be escorted out shortly."
        a "...there's no way... is there?"
        return

    label Aden15c:
        mc "I agree with Brian. Love is a pain."
        b "Yeah, she gets it! And if I'm being honest... she {i}can{/i} get it."
        a "Brian, don't be gross!"
        b "What do you say [mc_name]? You wanna spend a night not falling in love with me?"
        a "Brian, stop!"
        b "I'm joking, I'm joking! You're too sensitive Aden."
        b "If you want my advice, try going after a girl just for the thrill. Don't worry about love or romance."
        b "Just.{w=0.5} Thrill."
        a "I don't know..."
        b "Just for once, shut your brain off and let your instincts drive. Just take what you want and forget about the consequences, just---"
        "{i}Suddenly Aden's hands had grabbed my face and his lips were pressed to mine. I instinctively pushed him off and he fell to the ground.{/i}"
        b "Woah, Aden! That's not..."
        "{i}Aden scrambled to his feet, his face red from embarrassment. I was too shocked to speak.{/i}"
        a "[mc_name]..."
        b "Dude..."
        a "..."
        hide aden with moveoutleft
        "{i}Aden frantically grabbed his soccer equipment and sprinted away.{/i}"
        b "I can't help but feel slightly responsible."
        mc "That was shit advice, Brian."
        b "Yeah, most of my advice is."
        scene interrogation_room with fade_to_black
        show aden neutral at center
        a "...she didn't call after that. We stopped practicing. "
        cl "Did you have any interaction after that day?"
        a "No, not really. I was so embarrassed I mostly tried to avoid her!"
        cl "So you were not with [mc_name] the evening of April 27, 2019?"
        a "The night of Reg's party? No, not at all! I wasn't even invited because I wasn't on the varsity team."
        cl "Oh, so you weren't at the party at all?"
        a "No."
        cl "Where were you the evening of April 27, 2019?"
        a "At home studying."
        cl "Were you with anyone, or did anyone know where you were?"
        a "No, I was alone. My parents were out for the evening."
        cl "Thank you, Mr. Li, we have everything we need. [mc_name] remains without an alibi the night of the crime."
        a "Wait, there's no way she did it! She's w---"
        cl "In addition, Aden Li remains without an alibi the night of the crime. Mr. Li, thank you for your cooperation. You will be escorted out shortly."
        a "...there's no way... is there?"
        return

    label Aden15d:
        mc "I'm always happy to come see you play, Leon."
        "{i}Leon blushed slightly. Aden looked at me in confusion. {/i}"
        l "Thanks."
        "{i}The look of confusion on Aden's face was slowly replaced with a look of betrayal, then disappointment. He looked down at his feet and wandered off into the cheering crowd. {/i}"
        scene interrogation_room with fade_to_black
        show aden neutral at center
        a "I couldn't believe it! I actually thought she had come to see me... what a letdown."
        cl "Had your relationship changed the next time you saw her?"
        a "That was actually the last time I saw her."
        cl "Oh, so you didn't go to Reg's party?"
        a "I did, but she wasn't there. I would have invited her but..."
        cl "I understand. Do you have any reason to believe you know where she was the night of the party?"
        a "I have no idea."
        cl "And can anyone verify your location that night?"
        a "Sure. Brian, Reg, Nate... pretty much anyone on the varsity soccer team."
        cl "Okay, thank you for your time, Mr. Li. I think I've asked all the questions I need to."
        a "Are we or [mc_name] in trouble?"
        cl "You aren't. She might be."
        return

    label Aden15e:
        mc "Uh, no, I'm sorry."
        "{i}Aden dropped his eyes in disappointment. {/i}"
        mc "I'm so sorry i just... I don't see you as someone I would date."
        mc "Not that there's anything wrong with you! I  just don't feel that way."
        a "It's okay, I understand."
        "{i}Aden looked close to tears. {/i}"
        mc "Let's still be friends!"
        "{i}Aden ignored me and disappeared into the cheering crowd. {/i}"
        scene interrogation_room with fade_to_black
        show aden neutral at center
        a "I couldn't believe it! I actually thought she may have liked me... what a letdown."
        cl "Had your relationship changed the next time you saw her?"
        a "That was actually the last time I saw her."
        cl "Oh, so you didn't go to Reg's party?"
        a "I did, but she wasn't there."
        cl "I understand. Do you have any reason to believe you know where she was the night of the party?"
        a "I have no idea."
        cl "And can anyone verify your location that night?"
        a "Sure. Brian, Reg, Nate... pretty much anyone on the varsity soccer team."
        cl "Okay, thank you for your time, Mr. Li. I think I've asked all the questions I need to."
        a "Are we or [mc_name] in trouble?"
        cl "You aren't. She might be."
        return

    label Aden15f:
        mc "I think you should go make up with Leon."
        a "Huh? Right now?"
        mc "Yeah. You two are friends. I hate to see you at odds."
        a "But..."
        mc "We can come back to this afterward."
        "{i}Aden pulled away from me silently.{/i}"
        mc "...is everything alright?"
        a "...not really, [mc_name]. I... I thought maybe you liked me, but... this whole night you've been talking about Leon."
        mc "What? No, I---"
        a "I get it. He's older and more mature, and you guys have been friends since you were super young."
        mc "Aden, it's not like that---"
        a "I'm sorry, [mc_name], but I just need to be alone with my thoughts, okay?"
        "{i}I reached toward him, but he shied away. Devastated, I walked toward the door. {/i}"
        mc "Aden---"
        a "Please. Just go."
        scene interrogation_room with fade_to_black
        show aden neutral at center
        a "That was my first heartbreak. I thought she liked me, but the whole time she was thinking about Leon."
        a "I ended up staying in that bedroom for hours. By the time I went back downstairs, people had started getting texts about what happened."
        cl "Did you see [mc_name] again that night?"
        a "No. When I came out of the bedroom, she was gone."
        cl "I understand. Do you know where she went?"
        a "I have no idea."
        cl "And can anyone verify your location that night?"
        a "Sure. Brian, Reg, Nate... pretty much anyone on the varsity soccer team. They all saw me go upstairs and come down later. And Reg's house has security cameras so I would have been caught if I tried sneaking out the window while I was up there."
        cl "Okay, thank you for your time, Mr. Li. I think I've asked all the questions I need to."
        a "Am I or [mc_name] in trouble?"
        cl "You aren't. She might be."
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
        scene bedroom_night with fade_to_black
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
        r "Someone important to me once said \"you cannot stop loving someone.\" Now, I don't know much about love, but whatever I felt for [mc_name]... I don't think I can stop feeling that."
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

    label Brian2:
        scene interrogation_room with fade_to_black
        show brian neutral at center
        cl "Mr. Giang, are you ready to begin?"
        b "Yes."
        cl "Alright Mr. Giang, I'm going to be asking you some questions about yourself and the occurrences of and leading up to the evening of April 27, 2019."
        cl "You are sworn under the same oath that you will be for the upcoming trial. Is this clear?"
        b "Yes, I understand."
        cl "Excellent. Let's begin. Can you start by stating for the record your full name and age?"
        b "I'm Brian Giang, age 19."
        cl "And your occupation?"
        b "I'm a student at Bellington University, but I also work at a coffee shop near the high school. It's called Coffee Waves."
        cl "Oh, I love that place!"
        b "Yeah, me too. I get free drinks and a lot of cute high school girls come in. That's actually how I met [mc_name]. She came in one day with Leon."
        cl "This is Leon Hewett So?"
        b "Yes. Leon and I were on the soccer team together last year, before I graduated from the high school."
        cl "Thanks for verifying. Can you tell me about the day you met [mc_name] when she came with Leon to Coffee Waves?"
        b "Yeah, definitely! It was a Wednesday, I think."
        b "I of course recognized when Leon when he came in, but he brought with him this absolutely gorgeous friend I'd never met. Oh, man, she was wearing these jean shorts---"
        cl "Brian, focus."
        b "Okay, okay, sorry. I'll try to limit the extraneous comments."
        jump Brian3

    label Brian3:
        scene classroom with fade_to_black
        "{i}{cps=8}Briiiiiiiing.{/cps}{/i}"
        "{i}The bell announcing the beginning of lunch period woke me from a half-snooze. As I began putting my belongings into my backpack. I felt a hand on my shoulder.{/i}"
        show leon neutral at center
        "{i}I turned around to see Leon standing over me.{/i}"
        l "Hey, [mc_name]."
        mc "Hey Leon!"
        l "Want to grab a drink at Coffee Waves?"
        mc "Sure! I could certainly use the caffeine."
        l "Alright, let's go. I can drive."
        scene coffee_shop with fade_to_black
        show leon neutral at center
        l "Oh hey, Brian is working today! Have you met him?"
        mc "No, I don't think so."
        l "Hey Brian!"
        show brian neutral at rightish with moveinright
        show leon:
            linear 0.3 leftish
        b "{cps=8}Yoooooooo{/cps}, Leon! How's it going dude?"
        l "I'm good. Soccer tryouts are coming up next week."
        b "You feel ready?"
        l "Well, for some of us varsity guys it's just a formality. I've been on the team for two years, so I'm not super worried."
        b "Well, don't underestimate the new freshmen. One of them might take your spot!"
        l "Alright, man. I won't."
        "{i}Leon gestured in my direction.{/i}"
        l "Hey, I wanted to introduce you to my friend [mc_name]."
        b "Oh, [mc_name] is it? Nice to meet you. I'm Brian."
        "{i}Brian smiled at me with what he probably intended to be a sexy smolder.{/i}"
        b "They call me a coffee maestro because I grind so fine."
        l "Brian, stop joking around and just take our order."
        b "Okay, fine. What can I get you?"
        l "I'll take a pumpkin spice latte."
        b "AH, we've got ourselves a basic one! How about you, hot-tea?"
        l "Brian, knock it off with the coffee puns!"
        mc "Um, I's actually not sure what I want... any recommendations from either of you?"
        l "The pumpkin spice here is fantastic!"
        b "I'm quite fond of the caramel macchiato."
        mc "Hmmmm, those both sound good. I'm going to go with..."
        menu:
            "What should I order?"
            "Caramel macchiato":
                jump Brian4
            "Pumpkin spice":
                jump Brian15a

    label Brian4:
        mc "I'll take a caramel macchiato. I've never had one, so I'm curious how it tastes."
        b "Excellent choice! I'll need to hear your opinion once you've tried it."
        mc "I'll let you know before we leave!"
        b "Actually... let me talk to my boss. He might let me take my break a little early today so I can hang out with you for 15 minutes. Gimme a few minutes."
        hide brian with moveoutright
        show leon:
            linear 0.3 center
        "{i}Leon and I dropped our cash on the counter and claimed a small table in the otherwise empty coffee shop.{/i}"
        l "He's a character."
        mc "Seems like it! What's with all the uncomfortable pick-up lines?"
        l "He does that to everyone. He's a jokester."
        mc "Gotcha."
        show brian neutral at rightish with moveinright
        show leon:
            linear 0.3 leftish
        "{i}Brian reappeared by the table holding a try with three drinks. He placed each drink carefully on the table, and then sat in the chair next to mine.{/i}"
        b "So, what do you think?"
        "{i}I took a sip of my drink.{/i}"
        mc "It's delicious!"
        b "I know, right? I gave you an extra pump of caramel."
        "{i}He leaned toward me and dropped his voice to a whisper.{/i}"
        b "{size=-10}Don't tell my boss.{/size}"
        mc "Your secret is safe with me."
        b "How's yours, Leon?"
        l "It's tasty!"
        b "Fantastic. I really am a coffee genius."
        "{i}He turned to me and grabbed one of my hands.{/i}"
        b "I guess that's why it fells like there's something {i}brewing{/i} between the two of us."
        l "Brian, chill it with the coffee pickup lines!"
        b "Dude, I'm just messing with you. I'm not trying to steal your girl."
        l "My--- my girl?"
        b "You seriously think I would do you dirty like that? Naw, man. I may be a bit of a player, but I would never go after another guy's girlfriend."
        l "What?! We're not... she's not..."
        b "Wait, aren't you guys dating?"
        mc "Uh, no... we're just friends."
        b "Oh, my bad, dude. I just assumed by the way you interacted that something was going on."
        l "Oh, no. We've just been friends for a long time."
        b "Ah, I see. Then you wouldn't mind if I took a shot at her?"
        "{i}Brian raised an eyebrow suggestively.{/i}"
        l "Do you ever quit this act of yours?"
        b "Never."
        "{i}Brian realized he's been holding my hand this entire time and quickly dropped it in embarrassment.{/i}"
        b "Well, I think it's about time I went back to work. But hey, it was nice meeting you [mc_name]! Come back to see me soon."
        mc "I'll certainly try!"
        scene interrogation_room with fade_to_black
        show brian neutral at center
        b "She came to the coffee shop every now and then after that day. When she did, I would always make sure to chat her up, flirt a little, do my thing... What can I say?"
        b "She was cute, and I'm a jokester at heart. I wasn't being serious anyway."
        cl "Did anything else notable happen the other times she came to the coffee shop?"
        b "Yeah, there's one event I can think of that was noteworthy. The day [mc_name] had the misfortune of running into my ex."
        jump Brian5

    label Brian5:
        scene school_parking_lot with fade_to_black
        "{i}It's so nice to finally head home after working on that group project for so long. Where did I park again? Ah, over there.{/i}"
        "{i}What? It's seriously not starting? Maybe I should call someone? ...aaaaaaand my phone's dead. Arg! Awesome luck today.{/i}"
        "{i}There's got to be someone around who could help, right? Coffee Waves isn't too far of a walk. Maybe Brian is working today.{/i}"
        scene coffee_shop with fade_to_black
        "{i}I don't see Brian around here anywhere. Maybe he isn't working today?{/i}"
        "{i}There's a woman with a name tag reading \"Kelsie\" behind the counter. I could ask her if Brian is around anywhere, or I could just cut my losses and walk back to the soccer field and ask one of the soccer guys for help.{/i}"
        menu:
            "What should I do?"
            "Walk back to the soccer field":
                jump Brian6
            "Ask Kelsie if Brian is around":
                jump Brian15b

    label Brian6:
        "{i}It's a little bit of a walk back to the soccer field and it's sorta hot outside, so I think I'll order a lemonade for the road.{/i}"
        scene coffee_shop with fade_to_black
        kelsie "Lemonade for [mc_name]!"
        "{i}A voice from far behind the counter rang through the drone of the coffee shop.{/i}"
        b "[mc_name] is here?"
        show brian neutral at center
        b "Hey, [mc_name]! You should have asked for me. I was just doing some inventory."
        "{i}Brian looked over his shoulder at Kelsie, then back at me.{/i}"
        b "Oh, never mind, Kelsie's working today. If you had asked her for me, she probably would have thrown you out."
        mc "How come?"
        b "We dated a while back. It didn't end super well. It broke my heart."
        mc "What does that have to do with her throwing me out?"
        b "I messed up pretty bad in that relationship... she's constantly trying to find ways to get me back."
        b "I try to avoid working the same shift as her because every time I talk to a girl she butts in with some lie. She tells people I have a whole bunch of high school girlfriends and stuff like that."
        mc "That's pretty mean."
        b "I guess I deserve it a little. I mean, I'm a bit of a flirter, as you know. I kind of gave myself a bad reputation that way. But I still don't think that gives Kelsie permission to act like that."
        mc "No, of course not."
        b "I really cared about her. I still do. I don't understand why she acts like a jealous ex when she's the one who dumped me..."
        "{i}Brian paused for a moment, then blushed.{/i}"
        b "Sorry for oversharing. I'm sure you don't care about my relationship woes."
        b "I've been a pretty bad boyfriend over the years, and sometimes an even worse ex-boyfriend, so these aren't the kind of stories you'd care about."
        mc "It's no problem! You can talk to me about whatever you want."
        b "Seriously? You don't mind?"
        mc "Not at all!"
        b "Well... how about I text you about it?"
        mc "Sure!"
        b "Great! Can I put my number into your phone?"
        mc "...it's dead."
        b "Oh..."
        mc "...also my car broke down."
        b "Huh?"
        mc "I'm stuck here with no way to get home and no way to contact anyone for help."
        b "Why didn't you open with that?!"
        mc "To be honest, I forgot about it until now!"
        "{i}Brian gave a hearty laugh.{/i}"
        b "You're unbelievable. Where have you {i}bean{/i} all my life?"
        "{i}I giggled, despite my best efforts.{/i}"
        mc "Is now really the time for a coffee pun?"
        b "It's always time for a coffee pun."
        "{i}The two of us laughed. Kelsie glared at me with something that looked like murderous intent.{/i}"
        b "I get off in around half an hour. Why don't you hang out here until then, and then I can drive you home."
        mc "You are a life-saver!"
        b "I do my best. You can pay me back by giving me that phone number you promised."
        mc "Sure thing."
        scene interrogation_room with fade_to_black
        show brian neutral at center
        b "I finished my shift and drove her home. She put her number into my phone, and we texted every now and then."
        b "Not very often, and nothing too deep. She would ask what days I was working at Coffee Waves, I would send her score updates while watching the varsity soccer games, stuff like that."
        cl "Did these messages at any point become romantic or sexual?"
        b "No, of course not. I'm not one to send inappropriate pictures or explicit texts, and even if I was, we never had text conversations that went in that direction at all."
        cl "How about in person? Did your friendship ever evolve into something else?"
        b "Things started to change the day that Leon invited a group of us to the movies."
        cl "Who was in the group?"
        b "Leon So, Reg Na, [mc_name], and me."
        cl "What exactly happened?"
        b "Something lifechanging."
        jump Brian7

    label Brian7:
        scene school_hallway with fade_to_black
        show serpens neutral at center
        s "... and we're falling a little behind, so we should probably try to meet outside of school at some point."
        mc "Sorry, that's my fault. You keep having to explain everything to me."
        s "It's no problem,  really. At the risk of sounding egotistical, I'm pretty good at calculus."
        mc "Well, I appreciate it."
        s "So, in terms of meeting up---"
        l "Hey, [mc_name]!"
        show leon at rightish with moveinright
        show serpens:
            linear 0.3 leftish
        l "How's it going?"
        mc "Uh, pretty good. I was just chatting with Serpens about a calculus project."
        "{i}Leon seemed to notice Serpens for the first time.{/i}"
        l "Oh! Hey, man."
        s "Hey, man."
        "{i}Serpens and Leon fist bumped.{/i}"
        l "Hey, I'm planning on seeing a movie this evening with a group. You guys in?"
        mc "Sure! How about you, Serpens?"
        s "Uh, I'm kinda busy tonight..."
        l "Oh, that's too bad. Next time, I guess!"
        show leon:
            linear 0.3 center
        hide serpens with moveoutleft
        l "So, [mc_name]... I'll see you at the theatre around 7?"
        mc "Sounds good!"
        scene movie_theatre with fade_to_black
        show leon neutral at leftish
        show reg neutral at rightish
        show brian neutral at center
        l "Hey, [mc_name]! We're over here!"
        mc "Hey everyone."
        b "Glad you could make it."
        "{i}Brian leaned toward me and lowered his voice.{/i}"
        b "I've been thinking about you a latte."
        l "Brian!"
        b "Okay, okay! What's got you soy worked up?"
        "{i}Leon glared at Brian. Brian raised his hands in surrender.{/i}"
        r "Leon, Brian, stop flirting with each other and let's figure out which movie we want to watch."
        b "There's this awesome horror movie that just came out. Let's see that!"
        l "I don't really want to see something scary. Can we see that rom-com that's up for best picture?"
        b "Really? Man, you seriously are basic."
        l "[mc_name], what do you want to see?"
        menu:
            "Which movie do I want to see?"
            "Scary movie":
                jump Brian15c
            "Rom-com":
                jump Brian8

    label Brian8:
        mc "I'd like to see the rom-com."
        "{i}Brian clicked his tongue and shook his head.{/i}"
        b "I expected more from you, [mc_name]."
        "{i}He smiled and gently tapped my arm with the back of his hand.{/i}"
        b "Kidding."
        r "Let's stop sucking each other's dicks and go buy our tickets before we're late to the movie!"
        scene movie_theatre_interior with fade_to_black
        "{i}To my right, Leon was leaning forward in his seat, entirely engrossed in the plot on screen. To my left, Brian was on his third soda refill.{/i}"
        "{i}He was trying to act as though he wasn't interested in the movie, but on more than one occasion I caught him smiling{/i}"
        show brian neutral at center
        "{i}Brian leaned to whisper in my ear.{/i}"
        b "You know, if they would just go for it instead of skirting around their feelings for each other, they wouldn't be in this situation."
        mc "Yeah, tell me about it! He needs to just go for it. Nothing good ever came from people hiding their feelings."
        b "You think so?"
        mc "Of course. People miss opportunities when they don't communicate these things."
        "{i}A moment passed, and then I felt a weight over my shoulders. I glanced to my left to see that Brian had draped his arm over my shoulders.{/i}"
        mc "Very funny, Brian."
        "{i}I decided to play along by crossing my left arm across my chest and intertwining my fingers in his.{/i}"
        "{i}He squeezed me closer and whispered in my ear.{/i}"
        b "You make me crazy."
        mc "Well you mocha me crazy."
        "{i}I laughed under my breath but didn't let go of his hand. We stayed like that for several minutes.{/i}"
        hide brian with moveoutleft
        "{i}Finally, Brian had to break the hold to take his third trip to the bathroom.{/i}"
        scene movie_theatre with fade_to_black
        show leon neutral at leftish
        show reg neutral at rightish
        show brian neutral at center
        l "Wow, that was an excellent movie!"
        r "It was alright."
        l "What did you think, [mc_name]?"
        mc "I liked it, too!"
        l "How about you, Brian?"
        b "I didn't think I was going to be into it, but I actually enjoyed it."
        l "Oh, shoot... I left my jacket in the theatre."
        hide leon with moveoutleft
        r "I'm gonna run to the bathroom while we're waiting on him."
        hide reg with moveoutright
        b "You know, it's not really fair."
        mc "What do you mean?"
        b "That guy in the movie... he made some of the same kind of bad choices I did in previous relationships, and for him it worked out. It even made him more charming."
        mc "Like what?"
        b "He took his girl for granted. That's my most frequent mistake."
        mc "Well, he learned from it. Did you?"
        b "I like to think so."
        "{i}Brian dropped his eyes and shifted his weight.{/i}"
        b "I dated a lot in high school and I've dated a lot in college. I keep making the mistake of thinking I'm special somehow."
        b "Just because a lot of people crush on me, I let it go to my head. I forget that I'm not some perfect guy who girls are always going to come running back to."
        b "It's when I start acting like I'm granting my girlfriend some kind of high honor by going out with her that things start to disintegrate."
        "{i}Brian looked back at me.{/i}"
        b "Do you mind if I get a little personal?"
        mc "Not at all."
        b "I've never dumped someone in my life."
        mc "Wait... are you saying you are still in several relationships?"
        b "No, of course not. I've never dumped anyone, but I've been dumped plenty."
        mc "Oh, gotcha."
        b "Yeah. I mean, I liked everyone who I've dated. I still like them. Otherwise we wouldn't have dated."
        mc "Were you in love with any of them?"
        b "I used to think so. Until recently, I thought I'd loved every single one of them. Each time someone broke up with me, I thought I was losing my soul mate."
        mc "What changed?"
        b "I met someone who was real."
        mc "Really? Do I know her?"
        b "I---"
        l "Got it!"
        show leon neutral at leftish behind brian with moveinleft
        l "It took me a little bit to remember exactly where our seats were, but I found it."
        "{i} Leon looked around.{/i}"
        l "Where's Reg?"
        r "Right here."
        show reg neutral at rightish behind brian with moveinright
        "{i}Reg emerged from the bathroom, wiping his wet hands on his pants.{/i}"
        r "Are we ready to go get dinner?"
        l "Yep!"
        hide reg
        hide leon
        with moveoutright
        "{i}Brian looked at me as though he wanted to say something, then dropped his gaze and followed his friends.{/i}"
        "{i}I followed shortly after.{/i}"
        scene interrogation_room with fade_to_black
        show brian neutral at center
        cl "What was life-changing about that movie?"
        b "I realized that, without me noticing, my jokes had stopped. Suddenly, I started to mean all the things I said to her."
        cl "So, you realized you liked her?"
        b "Yeah."
        cl "Did she give any indication of liking you back?"
        b "At first I wasn't sure. She seemed to think it was still a joke, so it was hard to tell."
        b "After a while, I could barely take it anymore. I really wanted to tell her straight up how I felt, but I was afraid that I would just end up making the same mistakes I'd been making for years."
        b "With the girls before, it didn't matter anymore. But with [mc_name]... something was different. I was terrified of messing something up."
        b "But on the other hand... nothing good ever came of lying about your feelings, right?"
        cl "What did you do?"
        b "I texted her to meet me at Coffee Waves."
        b "And we had a chat."
        jump Brian9

    label Brian9:
        scene coffee_shop with fade_to_black
        "{i}Brian asked me to meet him for coffee today. Apparently he has something important to talk about. {/i}"
        show brian neutral at center
        b "Hey, [mc_name]. Thanks for meeting me."
        mc "Sure thing. Shall we sit?"
        "{i}We chose a table by the window. Kelsie slammed a caramel macchiato down in front of each of us without speaking a word.{/i}"
        b "I hope you don't mind I ordered for you."
        mc "Not at all! You picked exactly what I would have ordered. So, what did you want to talk about?"
        "{i}Brian looked away for several seconds, then back at me.{/i}"
        b "There's something I really want to do, but I'm afraid."
        mc "Like bungie jumping or something?"
        b "No, nothing like that. It's something I've done many times in the past, but every time it's been a mistake. Every time, it's ended horribly."
        mc "I don't understand."
        b "I know, but... I can't really give you any more details right now."
        mc "Okay..."
        b "The thing is, the reward is huge. It's something really important to me, and I'm not sure I'd ever forgive myself if I didn't take a chance."
        b "It's something important enough to me, that I'd be willing to change for it."
        b "But on the other hand... it's never worked. The chances are high that I would just end up making the same stupid mistake again. And if I do that, nothing will ever be the same."
        mc "I'm sorry, but I'm really confused---"
        b "The bottom line, [mc_name], is... is it a mistake to keep doing the same thing and expect different results?"
        menu:
            "Yes":
                jump Brian15d
            "No":
                jump Brian10

    label Brian10:
        mc "No."
        b "You don't think so?"
        mc "Well, it sounds like something is different this time. You said that the reward is something you'd be willing to change for, so that tells me that something."
        mc "It tells me that you wouldn't be making the same bad mistake again... you'd be making a different choice. Something similar maybe, but if you're going into it with a different energy, that could make a difference."
        mc "Although, I really don't know the context, so that might be ridiculous."
        b "No. It's not."
        "{i}A smile appeared on Brian's face. He grabbed my hands and his face became serious again. {/i}"
        b "I'm going to make that mistake now, okay?"
        mc "Uh, sure---"
        "{i} Suddenly, Brian's lips were pressed against mine. For a moment I was shocked, but I soon felt myself melt into the sensation. {/i}"
        "{i} His hands wandered up my arm and made their way to my head where his fingers gently became tangled in my hair. He used his new grip to pull my face more firmly against his. {/i}"
        "{i} Slowly, he unravelled his fingers from my hair and pulled away. {/i}"
        b "...nothing good ever came from people hiding their feelings."
        mc "...yeah."
        "{i} Brian leaned toward me intently and dropped his voice. {/i}"
        b "I want it to be different this time. I really care about you and I want to do this right. Are you in?"
        "{i} I paused to look at Brian more carefully. {/i}"
        "{i} On the outside, he looked like a player. He flirted aggressively and he'd been in too many relationships to count, but underneath... he was something else.{/i}"
        "{i} Underneath he was a person who cared deeply and loved recklessly. He was kind, and he could tell when something was real. The longer I stared at him, the more I could see him as someone I could fall in love with.{/i}"
        mc "Yeah. I'm in."
        b "...really?"
        mc "Really."
        "{i}Brian stood up from his seat and pulled me into an embrace. He stood there for several seconds and the world turned around us. {/i}"
        "{i}A child spilled his drink and cried. A bell rang as a woman entered the coffee shop with her dog. Kelsie looked at us disgustedly.{/i}"
        "{i} Brian slowly released me and kissed me once more on the forehead.{/i}"
        b "Uh, I guess I should get to class."
        "{i}My head was swimming.{/i}"
        mc "Uh, yeah. Me, too."
        b "Alright. I'll see you soon."
        mc "Yeah."
        b "...take care."
        hide brian with moveoutright
        "{i}Brian left the coffee shop as I stood there, frozen, watching him walk away. I felt a tiny smile creep onto my face.{/i}"
        kelsie "Poor, naïve child. You fell into the monster's grasp."
        "{i} I responded without looking away from Brian's receding form.{/i}"
        mc "Fuck off, Kelsie."
        scene interrogation_room with fade_to_black
        show brian neutral at center
        cl "So, you and [mc_name] became involved romantically?"
        b "Ya know, you start a lot of your sentences with \"so.\" That's going to get really confusing when you interview Leon."
        cl "How?"
        b "... because his last name is So. Do you not know his full name?"
        cl "Mr. Giang, let's get back on track, please. Were you and [mc_name] involved romantically?"
        b "I'm not sure how my story left that question unanswered."
        cl "Mr. Giang, the quicker you can answer my questions clearly, concisely, and without room for misinterpretation, the faster you can get out of here."
        b "Fine. Yes, we were involved romantically."
        cl "Did you consider her your girlfriend?"
        b "We never really had much time to talk about making it official in any wort of way. This was less than a week before the party."
        cl "Reg Na's party on April 27?"
        b "Yes. In fact, the day after we met up at Coffee Waves was the day of the big win that made Reg think to throw a party in the first place."
        jump Brian11

    label Brian11:
        scene soccer_field with fade_to_black
        "{i}It's been some time since I took the time to go to a high school soccer game. However, Brian's been texting me score updates for the last hour, and it sounds like the guys are doing really well.{/i}"
        show brian neutral at center
        b "[mc_name]?"
        mc "Hey, Brian!"
        b "I wasn't expecting to see you! What are you doing here?"
        mc "Same as you. Supporting the guys."
        "{i}Brian looked at me with one eyebrow raised, his eyes suspicious.{/i}"
        mc "Well, I came here to see one guy in particular."
        b "That's what I thought. Leon?"
        mc "Well, of course Leon, but... I've actually been hanging out with some barista recently. He works at Coffee Waves. Maybe you know him?"
        "{i}Brian gathered me in a side hug and smiled.{/i}"
        b "Good to see you."
        mc "Good to see you too."
        "{i}From his position on field, Reg caught my eye and winked.{/i}"
        b "Oh, I see you have an admirer!"
        mc "Oh, no, it's nothing like that. We're just friends. He helps me with calc every now and then."
        b "Well as long as you don't let yourself get stolen away by a younger, prettier guy."
        "{i}I laughed.{/i}"
        mc "You're embarrassing."
        scene soccer_field with fade_to_black
        "{i}{cps=8}Tweeeeeeet!{/cps}{/i}"
        "{i}The ref blew the final whistle and raised her hand to indicate Bellington High as the winners. The crowd roared as the team celebrated and shook the hands of the opposing team.{/i}"
        show reg neutral at center
        "{i}The people around me began packing up their foldable chairs and coolers as Reg jogged away from his teammates to join me on the sidelines. Before I could react, he gathered me into a bear hug.{/i}"
        mc "Excellent playing, Reg!"
        r "Hell yeah, man! You're like my good luck charm! I scored a personal best today!"
        mc "That was all you, Reg!"
        r "You helped more than you can imagine."
        "{i}A few seconds passed. Suddenly, Reg realized he'd been hugging me this entire time and quickly let go, blushing slightly.{/i}"
        show reg:
            linear 0.3 rightish
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
                jump Brian12
            "Reg's":
                jump Brian15e

    label Brian12:
        mc "Brian's party sounds fun!"
        b "Well, I promised only the hottest girls would be at my party, so of course you'll be there."
        "{i}Brian winked at me.{/i}"
        r "Brian, you're not even on the team anymore! I'm going to throw the varsity team party, and you can't do anything about it because you.{w=0.2} Are.{w=0.2} Not.{w=0.2} On.{w=0.2} The.{w=0.2} Team!"
        b "Okay, fine. Chill out."
        r "You better tread lightly or you're gonna get uninvited for real."
        "{i}Reg stormed off, but stopped to yell over his shoulder.{/i}"
        r "April 27. You can come because you're an alum, Brian, but you only get one plus one."
        hide reg with moveoutright
        show brian:
            linear 0.3 center
        "{i}He disappeared into the cheering crowd{/i}"
        mc "Wow. Sorry about that. I didn't realize that would set him off."
        b "It's okay. You can never tell with that kid."
        b "Besides, I appreciate you being on my side."
        "{i}He gave me a quick kiss.{/i}"
        b "I have a group project due tomorrow, so I should probably head back to campus. I'll see you at the party though! You'll be my plus one, right?"
        mc "Absolutely!"
        scene interrogation_room with fade_to_black
        show brian neutral at center
        b "Reg's party was that weekend. I used my fake ID to buy a bunch of booze, and I was really excited for it."
        b "[mc_name] and I arrived around 8:30 and hung out by the drink table most of the night."
        cl "Were you and [mc_name] drinking?"
        b "I was, but [mc_name] wasn't."
        cl "Did you drink enough for your judgement to be impaired?"
        b "No, I just got a little buzzed. Leon was the one who got totally messed up."
        cl "Can you please tell me, in detail, everything you remember from that night?"
        b "I'll do my best."
        jump Brian13

    label Brian13:
        scene house_party_night with fade_to_black
        show brian neutral at center
        b "You sure you don't want to try any?"
        mc "No, I don't drink."
        b "Suit yourself."
        "{i}Brian downed his drink.{/i}"
        b "Have you seen Leon?"
        mc "No, I haven't. He should have been here by now, right?"
        b "Yeah. I hope my man shows up soon. He's such a blast to party with!"
        show brian:
            linear 0.3 rightish
        show leon neutral at leftish with moveinleft
        "{i} Suddenly, the front door flew open, revealing a very angry Leon. He came inside and immediately plopped down on a couch and crossed his arms. Brian and I sat down next to him.{/i}"
        b "Dude, what's going on with you?"
        l "This night has blown chunks so far."
        mc "Really? What happened?"
        l "Well, let's start with earlier today when Aden told me the party had been cancelled. For some reason I trusted him, even though he's not even on the varsity team."
        l "So, I was sound asleep when Reg called me in a rage because he was upset that I didn't come to the party. He wouldn't even let me explain myself."
        l "I just don't understand why Aden would lie to me like that or how I'm supposed to make Reg trust me again."
        "{i}Leon put his head in his hands, and I put an arm around his shoulders to comfort him.{/i}"
        mc "Hey, it's okay---"
        b "You know what you need?"
        l "What?"
        b "Boooooooooooze!"
        l "I don't drink."
        b "So? There's a first time for everything."
        l "I'm not interested."
        mc "Brian, I really don't think that's a good idea right now---"
        b "Driiiiink!"
        l "No."
        b "Pleeeeeeease? I'll... give you five dollars! I'll mix all your drinks for you! I'll even... let you kiss my girlfriend!"
        mc "Brian!"
        b "Just please drink with me! Seriously, it'll cheer you up. It'll cheer me up, too."
        l "I don't know..."
        b "Come on, don't be a pussy. Have a drink!"
        mc "Brian, seriously! Don't pressure him. And don't use a term associated with feminimity as an insult."
        l "Fine."
        mc "...what?"
        l "Fine. Give me a drink."
        b "Hell, yeah!"
        mc "Leon, you don't have to..."
        l "I want to."
        mc "..."
        "{i}Brian poured Leon a massive drink, and Leon drained it in one go.{/i}"
        l "Again."
        b "Yeah, my man! He knows how to party!"
        mc "Leon, be careful!"
        "{i}Leon downed another drink.{/i}"
        l "Again."
        mc "Leon, please stop. I know you're upset, but this isn't safe."
        "{i} Brian handed him another drink, but I snatched it away before he could drink it. {/i}"
        mc "If I give this back, you have to promise you're going to drink at a reasonable pace."
        "{i} Leon paused for a moment, glaring at me.{/i}"
        l "Fine."
        hide leon with moveoutleft
        show brian:
            linear 0.3 center
        "{i} He snatched his drink out of my hand and disappeared into the crowd on the dance floor.{/i}"
        b "What a legend!"
        mc "Brian, he was really upset, plus this is his first time drinking. I'm kind of worried."
        b "He's fine. The only thing you need to worry about right now... is busting some killer dance moves with your date. Come one, let's go dance!"
        mc "... alright. Let's dance."
        scene house_party_night with fade_to_black
        show brian neutral at center
        "{i} Brian and I have been out on the dance floor for quite a few songs by now. We started out about an arm's distance from each other, but with each passing song, we got closer and closer.{/i}"
        "{i} By now, his arms were around my lower back and my hands were clasped behind his head. Brian gently pulled me toward him until our pelvises were touching. We were there for only a few seconds before he pushed me away and dropped his hands.{/i}"
        b "Hey, [mc_name]... do you want to get out of here?"
        "{i} Brian's eyes were filled with a passion I couldn't quite describe.{/i}"
        mc "I---"
        "{i} Suddenly, a commotion from across the room caught our attention. {/i}"
        show brian:
            linear 0.3 leftish
        show leon at rightish
        show reg at center
        with moveinright
        "{i}Leon was on the floor, drunk beyond recognition, and Reg was standing over him, screaming.{/i}"
        "{i}Brian grabbed my hand and led me through the crowd to see what was going on.{/i}"
        r "...and now you have the audacity to lay on the floor like you're a victim! All evening you've been acting like a terrible friend!"
        "{i}Leon looked away shamefully.{/i}"
        r "Pick yourself up. Pick yourself up!"
        "{i}Brian dropped my hand to help Leon to his feet.{/i}"
        r "And for God's sake, stop drinking!"
        hide reg with moveoutleft
        "{i}Brian carefully led Leon away, trying desperately to keep him from falling over.{/i}"
        b "What happened, man?"
        l "Shit."
        b "What?"
        l "Shit happened, okaaaaay?"
        "{i}Leon pushed Brian away and stumbled toward the door. He paused, dry heaved, and then disappeared out the door and into the night.{/i}"
        mc "He didn't look good."
        b "I've gotten much drunker than that and I still managed to walk home."
        mc "I think I need to call him a ride or something. I bet Serpens could come help..."
        b "He'll be fine. He's probably just hanging out on the porch."
        mc "I should really check---"
        b "See that? A guy just walked out after him. Can we please just let someone else deal with this?"
        "{i}In the dark it was hard to make out Brian's expression.{/i}"
        b "Please, [mc_name]?"
        mc "..."
        b "I'm begging you."
        menu:
            "What do I do?"
            "Go after Leon":
                jump Brian15f
            "Let someone else take care of Leon":
                jump Brian14

    label Brian14:
        mc "..."
        b "Thank you. Now..."
        "{i}Brian leaned closer.{/i}"
        b "...what do you say we get out of here?"
        "{i}I nodded and let Brian lead me out the back door and to his car.{/i}"
        scene car_interior with fade_to_black
        "{i}Brian was in the driver's seat and I had shotgun.{/i}"
        mc "Where to?"
        b "I was thinking... we stay right here."
        "{i}Brian reached across the center console and pulled a lever on the side of the passenger seat.{/i}"
        "{i}Suddenly, the chairback behind me had fully reclined. I let upper body recline with it.{/i}"
        "{i}Slowly, Brian swung each leg over the center console until he was kneeling on the passenger seat, straddling my hips.{/i}"
        "{i}He propped himself up over me with one hand and used the other to brush a strand of hair from my face. {/i}"
        b "I know I'm not perfect."
        mc "You're correct."
        b "I think you were a little disappointed about some of my actions this evening."
        mc "I was."
        b "But... I really want this to work."
        mc "... me too."
        "{i} Brian lowered himself until his mouth was level with my ear. Then he whispered softly into my soul. {/i}"
        b "I'm willing to change for you. I promise... I'll get this right."
        "{i} He lifted his head and pressed his lips against mine. I wrapped my hands around his upper body and pulled him closer, softly accepting his heart into mine.{/i}"
        show interrogation_room with fade_to_black
        cl "Did you and [mc_name] have sexual intercourse that night?"
        b "Can I decline to answer? I think in terms of statutory laws in this state, it would just be cleaner if I didn't have to explain my answer on record."
        cl "..."
        b "I'm not the one on trial, right?"
        cl "I'll accept it. Can you at least tell me if you were with [mc_name] all night?"
        b "Yeah. I eventually drove her back to my place and we put on a movie. We fell asleep on the couch and then I drove her home after we woke up in the morning."
        cl "Did you see anyone else that night?"
        b "No."
        cl "When was the last time you saw Leon?"
        b "When he left after Reg yelled at him."
        cl "And when did you last see [mc_name]?"
        b "Around 8am on the morning of April 28."
        cl "Do you know anything about her current whereabouts?"
        b "No."
        cl "Okay, thank you Mr. Giang. I have no further questions. I appreciate your openess and honesty."
        b "I was my pleasure. Besides... nothing good ever came out of someone hiding their feelings."
        return

    label Brian15a:
        mc "I'll take a pumpkin spice latte."
        b "Ah, we've got two basic bitches in the house! Alright, those'll be right out."
        scene interrogation_room with fade_to_black
        show brian neutral at center
        b "That was basically it. I brought out their drinks, they drank them, then they left."
        cl "Did you interact with [mc_name] at any point after that?"
        b "Yeah, occasionally. She stopped by Coffee Waves a few times after that, so we greeted each other, but we didn't chat much."
        cl "Would you consider the two of you friends?"
        b "Not really... more like acquaintances. I would have liked to get to know her better, though."
        b "I thought she was super hot, but obviously I wasn't going to make a move. Not for real. I can't do my boy Leon dirty like that."
        cl "What do you mean \"do him dirty\""
        b "I wasn't about to try and steal his girlfriend away."
        cl "[mc_name] and Leon were together?"
        b "Well, yeah, I assumed so. Based on the way he was looking at her at least. People don't look at each other like that if they're just friends."
        cl "People who were close to both Leon and [mc_name] have attested that they were not romantically involved. Could you have been mistaken?"
        b "I guess I could have."
        cl "Did Leon or [mc_name] ever directly say they were together?"
        b "Well... no, they didn't."
        cl "Okay, thanks for clarifying. Going back a little... you say you and [mc_name] weren't really friends. How about you and Leon?"
        b "We were buds. We didn't see each other often, but we were friendly with each other, just like everyone on the team."
        cl "Did you see Leon or [mc_name] on the night of April 27?"
        b "Not [mc_name]. I did see Leon though. He got really drunk and then left early. I didn't see anything noteworthy."
        cl "[mc_name] remains without an alibi. Can anyone verify your location that evening?"
        b "Yeah. I was hanging with Reg and Nate most of the night, so either of them."
        cl "Okay, thank you Mr. Giang. No further questions at this point."
        return

    label Brian15b:
        mc "Excuse me... is Brian working today?"
        kelsie "Who are you?"
        mc "I'm his friend. My car broke down so---"
        kelsie "He's not working today."
        "{i}I don't really know why, but Kelsie seemed really irritated.{/i}"
        kelsie "To tell you the truth, management is getting really tired of all you high school girls coming in here asking for him. It causes distractions when boyfriends or girlfriends of the baristas come to visit them while they're working, so it's generally frowned upon."
        kelsie "Brian is really close to being fired because he's had so many different girlfriends come in to ask to see him."
        "{i}Kelsie leaned over the counter and lowered her voice.{/i}"
        kelsie "If you don't want your boyfriend to be fired, I would recommend pissing off and not coming back while he's working."
        mc "I think you misunderstood---"
        kelsie "I don't want to hear it. All I want to hear is the sound of you leaving this coffee shop."
        "{i}Perplexed, I left the coffee shop. I had never met Kelsie before, but she seemed to really dislike me. I wonder why?{/i}"
        "{i}I shook the question out of my mind and refocused on the current issue. I still had a broken down car and a dead phone, and I was no closer to finding a friend who could help me out. I guess I better walk back to the soccer field and try my luck there.{/i}"
        scene interrogation_room with fade_to_black
        show brian neutral at center
        b "I was pretty pissed when I found out that my ex had told [mc_name] to leave instead of telling me she was there. I was in the back the whole time!"
        cl "Why would she do that?"
        b "I think she was jealous or mad at me or something. I don't know, man."
        cl "How did this affect your relationship to [mc_name]?"
        b "She didn't come back to Coffee Waves again."
        cl "Did you see her at all after that?"
        b "No, I don't think so."
        c "How about Leon?"
        b "I saw him at the occasional soccer event that I went to. We were still friendly of course, just like I am with all of my old teammates."
        cl "Did you see Leon or [mc_name] on the night of April 27?"
        b "Not [mc_name]. I did see Leon though. He got really drunk and then left early. I didn't see anything noteworthy."
        cl "[mc_name] remains without an alibi. Can anyone verify your location that evening?"
        b "Yeah. I was hanging with Reg and Nate most of the night, so either of them."
        cl "Okay, thank you Mr. Giang. No further questions at this point."
        return

    label Brian15c:
        mc "Let's watch a scary movie."
        b "Hell, yeah!"
        "{i}Brian fist bumped me.{/i}"
        b "This is gonna be awesome."
        scene interrogation_room with fade_to_black
        show brian neutral at center
        b "Yeah, it basically sucked."
        cl "How so?"
        b "Well, Leon and [mc_name] were both pretty spooked, so they kept clinging to each other. I could tell the really liked each other, and I can't compete with that."
        b "To be honest, I was beginning to like her, but... she clearly didn't feel the same way."
        cl "Did you see her again after the movie?"
        b "I ran into her at a soccer game at some point, but that's it."
        cl "Can you tell me about it?"
        b "Nothing really happened. We saw each other, we chatted, Reg yelled about something, and then we left."
        cl "Did you see Leon or [mc_name] on the night of April 27?"
        b "Not [mc_name]. I did see Leon though. He got really drunk and then left early. I didn't see anything noteworthy."
        cl "[mc_name] remains without an alibi. Can anyone verify your location that evening?"
        b "Yeah. I was hanging with Reg and Nate most of the night, so either of them."
        cl "Okay, thank you Mr. Giang. No further questions at this point."
        return

    label Brian15d:
        mc "I think it's kind of naïve to expect a different result."
        b "Really?"
        mc "Yeah. Now, can you tell me the context, please?"
        b "Never mind. Don't worry about it."
        mc "Are you sure?"
        b "I'm sure."
        scene interrogation_room with fade_to_black
        show brian neutral at center
        b "I was going to make a move, but... she was right. It would have been a stupid mistake and it would have ended up just like all my other relationships."
        cl "Did you stop seeing her?"
        b "Not entirely. We remained friends and I saw her every now and then at Coffee Waves."
        b "Most of the time when she came, she brought Leon. They seemed really happy together, so I tried not to bother them too much."
        cl "Did you see Leon or [mc_name] on the night of April 27?"
        b "Not [mc_name]. I did see Leon though. He got really drunk and then left early. I didn't see anything noteworthy."
        cl "[mc_name] remains without an alibi. Can anyone verify your location that evening?"
        b "Yeah. I was hanging with Reg and Nate most of the night, so either of them."
        cl "Okay, thank you Mr. Giang. No further questions at this point."
        return

    label Brian15e:
        mc "I think Reg's party sounds fun!"
        r "Good. Because I wouldn't have let this guy throw it anyway."
        "{i}Reg playfully jabbed Brian in the ribs.{/i}"
        "April 27. You're invited, Brian, because you're an alum. You are allowed to bring a plus one, but only one."
        "{i}Reg disappeared into the cheering crowd.{/i}"
        hide reg with moveoutleft
        show brian:
            linear 0.3 center
        b "Why didn't you have my back?"
        mc "I mean, your party sounded fun, but I didn't want to hurt Reg's feelings or anything."
        b "Are you... are you actually embarrassed of me?"
        mc "What? Of course not."
        "{i}Brian aggressively tried to swoop in for a kiss. Instinctively, I put my hands up to block him.{/i}"
        b "Oh my God. You won't even kiss me!"
        mc "That's not true!"
        b "No, I get it. You're embarrassed to be seen with your fuck up of a boyfriend by all your friends."
        mc "Boyfriend?"
        b "Well... Wait... Oh, I see what's happening."
        "{i}Brian turned away, took a deep breath, and then looked back toward me.{/i}"
        b "I'm not the only guy you're with, am I?"
        mc "What?! Of course you---"
        b "You seriously came to see someone else. I can't believe I didn't see it."
        b "Who? Reg? No, it must be Leon, huh? You don't want him to know you were hanging around with me on the side!"
        mc "Brian, stop, that's not what's---"
        b "Serves me right, doesn't it? Another giant mistake. Just like the others."
        mc "Please, Brian---"
        b "I need to leave. Don't text me again."
        hide brian with moveoutright
        "{i}With that, he was gone.{/i}"
        scene interrogation_room with fade_to_black
        show brian neutral at center
        b "It was a short romantic relationship, if you can even call it that. I should have known it would end the same way. I somehow manage to ruin everything."
        cl "Were you mad at Leon?"
        b "I guess I was a little jealous of Leon at first. I was even a little jealous of Reg, believe it or not. I mean, who knows how many guys she was seeing."
        b "But, at the end of the day, I was mostly just angry with myself."
        cl "Did you see [mc_name] again after that?"
        b "She tried to come to Coffee Waves the next day to talk, but I just let Kelsie deal with her."
        cl "Did you see [mc_name] on the night of April 27?"
        b "No."
        cl "How about Leon?"
        b "No."
        cl "He wasn't at the party?"
        b "I don't know. I didn't bother to go."
        cl "Oh, I see. Where were you that night?"
        b "I was in my dorm watching a movie."
        cl "Is there anyone who can verify your location that night?"
        b "Not really... my roommate was at a frat party and I didn't see any of my floormates either."
        cl "So, you had no alibi on the night of the crime, and you were jealous because you thought your girlfriend was cheating on you."
        cl "To be completely honest, Mr. Giang... it sounds like the perfect recipe for a crime of passion."
        b "What are you suggesting?"
        cl "I'm suggesting you prepare a lawyer."
        b "Do you think I could have done this?"
        cl "It is not my place to say."
        b "I didn't do it! You have to believe me! We were friends! We were---"
        cl "Thank you for your time, Mr. Giang. You will be hearing from us shortly."
        cl "Please escort him out."
        return

    label Leon2:
        scene interrogation_room with fade_to_black
        show leon neutral at center
        cl "Mr. So, are you ready to begin."
        l "Yeah."
        cl "Alright Mr. So, I'm going to be asking you some questions about yourself and the occurrences of and leading up to the evening of April 27, 2019. You are sworn under the same oath that you will be for the upcoming trial. Is this clear?"
        l "Yes, I understand."
        cl "Excellent. Let's begin. Please state for the record your full name and age."
        l "I am Leon Hewett So and I'm 17 years old."
        cl "And what is your occupation?"
        l "I'm a high schooler. I'm in my junior year."
        cl "At what school."
        l "Bellington High."
        cl "How do you know [mc_name]?"
        l "We've been friends since we were about seven. We've lived near each other almost our entire lives, so we would always play together as children."
        cl "Did you at any point become romantically involved with [mc_name]?"
        l "Well, I've liked her since I was very young, but she was liked by so many people. I never really stood a chance."
        cl "Did she ever indicate that she liked you back?"
        l "I don't know. She never said outright. There were times I thought maybe she did, but it was never conclusive."
        cl "What made you suspicious that she liked you?"
        l "Well, we spent a lot of time together. We hung out almost every day. She would tease me, laugh with me... whenever she would make plans to go anywhere, she would almost always invite me because I'm the person she wanted to share all those experiences with."
        l "We tried to share experiences even as insignificant as going out to coffee during the lunch period."
        jump Leon3

    label Leon3:
        scene classroom with fade_to_black
        "{i}{cps=8}Briiiiiiiing.{/cps}{/i}"
        "{i}The bell announcing the beginning of lunch period woke me from a half-snooze. As I began putting my belongings into my backpack. I felt a hand on my shoulder.{/i}"
        show leon neutral at center
        "{i}I turned around to see Leon standing over me.{/i}"
        l "Hey, [mc_name]."
        mc "Hey Leon!"
        l "Want to grab a drink at Coffee Waves?"
        mc "Sure! I could certainly use the caffeine."
        l "Alright, let's go. I can drive."
        scene coffee_shop with fade_to_black
        show leon neutral at center
        l "Oh hey, Brian is working today! Have you met him?"
        mc "No, I don't think so."
        l "Hey Brian!"
        show brian neutral at rightish with moveinright
        show leon:
            linear 0.3 leftish
        b "{cps=8}Yoooooooo{/cps}, Leon! How's it going dude?"
        l "I'm good. Soccer tryouts are coming up next week."
        b "You feel ready?"
        l "Well, for some of us varsity guys it's just a formality. I've been on the team for two years, so I'm not super worried."
        b "Well, don't underestimate the new freshmen. One of them might take your spot!"
        l "Alright, man. I won't."
        "{i}Leon gestured in my direction.{/i}"
        l "Hey, I wanted to introduce you to my friend [mc_name]."
        b "Oh, [mc_name] is it? Nice to meet you. I'm Brian."
        "{i}Brian smiled at me with what he probably intended to be a sexy smolder.{/i}"
        b "They call me a coffee maestro because I grind so fine."
        l "Brian, stop joking around and just take our order."
        b "Okay, fine. What can I get you?"
        l "I'll take a pumpkin spice latte."
        b "AH, we've got ourselves a basic one! How about you, hot-tea?"
        l "Brian, knock it off with the coffee puns!"
        mc "Um, I's actually not sure what I want... any recommendations from either of you?"
        l "The pumpkin spice here is fantastic!"
        b "I'm quite fond of the caramel macchiato."
        mc "Hmmmm, those both sound good. I'm going to go with..."
        menu:
            "What should I order?"
            "Caramel macchiato":
                jump Leon15a
            "Pumpkin spice":
                jump Leon4

    label Leon4:
        mc "I'll take a pumpkin spice latte."
        b "Ah, we've got two basic bitches in the house! Alright, those'll be right out."
        hide brian with moveoutright
        show leon:
            linear 0.3 center
        l "What do you think of your drink?"
        mc "It's disgusting."
        l "What? Really?"
        mc "No, I'm joking. It's just as tasty as you promised it was!"
        l "Oh, I'm so relieved! I was worried you were going to be stuck with a drink you hated."
        mc "Why would you be worried about that? That would just mean you get two drinks."
        l "...oh. I suppose you're right."
        "{i}He laughed.{/i}"
        l "In that case... are you sure you don't hate it?"
        "{i}I playfully punched Leon in the arm.{/i}"
        mc "You wish."
        scene coffee_shop with fade_to_black
        show leon neutral at center
        mc "...and then he straight up blackmailed her into not marking him tardy!"
        "{i}Leon roared with laughter.{/i}"
        l "What and absolute legend! That guy has no fear."
        "{i}Leon glanced at his phone{/i}"
        l "Oh, jeez. We've already been here for almost half hour. We should probably head back if we're gonna be in time for fifth period."
        mc "Don't you have a study period fifth?"
        l "Yeah. You have English, right?"
        mc "Yeah."
        mc "..."
        mc "...you wanna skip?"
        l "What?"
        mc "We should skip."
        l "Really? The perfect attendance, honor roll, goody-two-shoes wants to skip class?"
        mc "Mrs. Green doesn't take attendance."
        mc "Besides, it's been a while since we've had a chance to laugh like this together."
        "{i}Leon looked at me in shock, then looked away, blushing slightly.{/i}"
        mc "So... can we stay here just a little longer?"
        "{i}Leon blushed deeper. {/i}"
        l "Sure. Let's stay a little longer."
        scene coffee_shop with fade_to_black
        show leon neutral at center
        l "...so I guess the dilemma is less about morality and more about conformity to societal norms."
        mc "That makes sense. Oh wow, it's almost time for sixth period. We should probably head back toward campus."
        l "Or we could just... not."
        mc "You sure?"
        l "Yeah. We're supposed to have a sub today, so we're probably not doing anything."
        mc "We're running the mile in gym, so I'm happy to miss out on that."
        l "Awesome. I'll buy you another drink. What do you want?"
        mc "Pumpkin spice. Thanks, Leon!"
        l "No problem. Next one's on you, though."
        mc "Sure."
        show coffee_shop with fade_to_black
        show leon neutral at center
        l "... and this is your love line, and because of the way it intersects with your life line... that means the person you love with die an untimely death."
        mc "What?! Really?!"
        l "No, I'm making this up as I go."
        "{i}Leon smiled slyly and I laughed.{/i}"
        mc "Of course you are. Here, I'll do you."
        b "Sorry lovebirds, but I'm gonna have to break this up because we're closing."
        show leon:
            linear 0.3 center
        show brian neutral at rightish with moveinright
        "{i}I looked up from Leon's palm to see that the coffee shop was empty and Brian was holding a mop. I turned my head to the window and noticed for the first time that the sun had set and it was dark outside.{/i}"
        mc "Woah! I didn't even notice how late it had gotten!"
        l "Sorry, Brian. We'll get out of your hair."
        hide brian with moveoutright
        show leon:
            linear 0.3 center
        l "This was fun... let's do it again sometime."
        mc "I'd like that."
        l "See you tomorrow for breakfast?"
        mc "Yeah. Usual spot."
        l "See you then!"
        hide leon with moveoutleft
        scene interrogation_room with fade_to_black
        cl "The two of you were really close."
        l "Yeah. We were."
        cl "And you thought she might have liked you romantically?"
        l "Maybe I was just being hopeful, but... we've known each other almost our whole lives, and we still managed to have something to talk about for an entire afternoon and into the evening."
        l "Is it so much a stretch to think that if we still have things to talk about after ten years that we may still have things to talk about after twenty, or fifty, or eighty?"
        cl "Perhaps not."
        l "I just don't understand why what happened... happened."
        cl "The investigative team is still struggling to understand the suspect's motives. In my experience, it doesn't help to dwell on questions like that."
        cl "The best thing you can do is to answer our questions honestly so we can fully understand your relationship with [mc_name] and the events leading up to the tragedy."
        l "Alright."
        cl "So why don't we move on to the day of the soccer tryouts? I understand that was a significant day?"
        l "Yeah, it was."
        cl "So what happened?"
        l "Aden happened."
        jump Leon5

    label Leon5:
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
        "{i}Suddenly, two boys in athletic attire had appeared. One of them had put Leon in a headlock that he was struggling to escape from, and the other was slowly shaking his head in both humor and disappointment.{/i}"
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
        mc "Wow. Whoever wrote that sign has really nice handwriting."
        r "That's be me."
        "{i}Reg sat down next to Nate and propped his feet on the table.{/i}"
        r "What can I say, I'm an effeminate guy."
        "{i}Reg winked.{/i}"
        mc "Is anyone even signing up this late?"
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
                jump Leon15b
            "Stay in band":
                jump Leon6

    label Leon6:
        mc "Aden, I think you should..."
        "{i}I hesitated. This wasn't the right answer. {/i}"
        mc "Hey Leon, can I talk to you privately for a moment?"
        l "Uh, sure?"
        hide reg
        hide nate
        hide aden
        with moveoutright
        mc "What are you doing?"
        l "Uh, what do you mean?"
        mc "You are trying to discourage Aden from trying out."
        l "He's never played before."
        mc "So?"
        l "So..."
        mc "Leon, I know you mean well but... you're better than this."
        l "Huh?"
        mc "Remember back when we took tap dancing lessons together?"
        l "Yeah?"
        mc "And you loved it right?"
        l "Where are you going with this?"
        mc "Your dad told you that you weren't good enough to move on to the higher level with me, so he told you to just quit."
        l "... well, yes---"
        mc "You remember what you told him?"
        l "..."
        mc "This is what you said: \"You have no right to break another person's dream.\""
        l "...I remember."
        mc "I doesn't matter if he isn't good. It's not your place to break his dream."
        "{i}Leon stared at me with an expression I couldn't read. Suddenly, he pulled me into an embrace.{/i}"
        l "[mc_name]... what would I do without you?"
        "{i}I smiled and rested my head on his shoulder.{/i}"
        mc "Not the right thing."
        "{i}Briefly, I pulled him closer. Then, reluctantly, I broke the embrace.{/i}"
        mc "Now let's go invite that kid to try out for the team."
        scene interrogation_room with fade_to_black
        show leon neutral at center
        l "I feel like she always managed to remind me what kind of person I was trying to be. She made me a better version of myself."
        l "We may have not been together romantically, but we loved each other. Not the kind of love you were asking about, but  kind of love unique to us."
        cl "Anything else you can tell me about your relationship to [mc_name]?"
        l "Uh, there was the day I invited [mc_name] to the movies. That was an enlightening experience."
        cl "What happened?"
        l "A lot."
        jump Leon7

    label Leon7:
        scene school_hallway with fade_to_black
        show serpens neutral at center
        s "… and we're falling a little behind, so we should probably try to meet outside of school at some point."
        mc "Sorry, that's my fault. You keep having to explain everything to me."
        s "It's no problem,  really. At the risk of sounding egotistical, I'm pretty good at calculus."
        mc "Well, I appreciate it."
        s "So, in terms of meeting up---"
        l "Hey, [mc_name]!"
        show serpens:
            linear 0.3 leftish
        show leon neutral at rightish with moveinright
        l "How's it going?"
        mc "Uh, pretty good. I was just chatting with Serpens about a calculus project."
        "{i}Leon seemed to notice Serpens for the first time.{/i}"
        l "Oh! Hey, man."
        s "Hey, man."
        "{i}Serpens and Leon fist bumped.{/i}"
        l "Hey, I'm planning to go see a movie this evening. You guys in?"
        mc "Yeah, I'm in! How about you, Serpens?"
        s "Uh... I'm kinda busy tonight..."
        l "Oh, that's too bad. Next time, I guess!"
        hide serpens with moveoutleft
        show leon:
            linear 0.3 center
        l "So, [mc_name]... I'll see you at the theatre around 7?"
        mc "Sounds good!"
        "{i}I began to walk away. After taking a couple steps, I felt Leon grab my arm.{/i}"
        l "Actually..."
        mc "Yeah?"
        l "Well, practice was cancelled this afternoon, so I was wondering..."
        l "...if you'd like to grab dinner first?"
        "{i}My heart fluttered slightly.{/i}"
        mc "Uh, I..."
        "{i}Leon blushed and looked away.{/i}"
        l "It doesn't have to be a big deal or anything, I mean, we could get fast food if you don't want to go to a sit-down place, cuz that would look like we were, like on a date or something crazy like that, so we don't have to do that if you don't want, but if you, like want to go to a sit-down place that's fine too, I mean it's more that fine, that's great, but like we don't have to, ya know, it's chill---"
        "{i}I giggled.{/i}"
        l "What's so funny?"
        mc "You're just really cute when you get flustered."
        "{i}Leon blushed deeper.{/i}"
        mc "Where we go to eat isn't a big deal. We have plenty of time to go to a sit-down, and I'm not short on cash or anything. Do you have money? Is that why you're panicking about it?"
        l "No, I'm good on money. I was just worried that..."
        mc "That what?"
        l "...nevermind."
        mc "Okay, well in that case, let's..."
        menu:
            "Where should we go to eat?"
            "Fast food":
                jump Leon8
            "Sit-down restaurant":
                jump Leon15c

    label Leon8:
        mc "Let's get some fast food."
        l "Oh... okay."
        mc "Is that okay?"
        l "Oh, yeah, it's fine, just..."
        mc "Yeah?"
        l "Uh, nothing. Let's go."
        scene interrogation_room with fade_to_black
        show leon neutral at center
        l "To be honest, I kind of wanted it to be a date. Serpens was even enough of a bro to say he was busy so that it would just be [mc_name] and I."
        l "But when she suggested fast food, I figured that was her trying to subtly let me know that she didn't want it to be a date. Kind of a shame, but it was for the best."
        cl "Why do you say that?"
        l "It may not have been the outcome I wanted, but if she hadn't made it clear she didn't think of it as a date, I wouldn't have invited Brian and Reg along."
        l "If Brian hadn't been there, then what happened next couldn't have happened."
        jump Leon9

    label Leon9:
        scene movie_theatre with fade_to_black
        show leon neutral at leftish
        show reg neutral at rightish
        show brian neutral at center
        r "[mc_name], Leon! We're over here!"
        mc "Hey everyone."
        b "Glad you could make it."
        "{i}Brian leaned toward me and lowered his voice.{/i}"
        b "I've been thinking about you a latte."
        l "Brian!"
        b "Okay, okay! What's got you soy worked up?"
        "{i}Leon glared at Brian. Brian raised his hands in surrender.{/i}"
        r "Leon, Brian, stop flirting with each other and let's figure out which movie we want to watch."
        b "There's this awesome horror movie that just came out. Let's see that!"
        l "I don't really want to see something scary. Can we see that rom-com that's up for best picture?"
        b "Really? Man, you seriously are basic."
        l "[mc_name], what do you want to see?"
        menu:
            "Which movie do I want to see?"
            "Scary movie":
                jump Leon10
            "Rom-com":
                jump Leon15d

    label Leon10:
        m "Let's watch a scary movie."
        b "Hell, yeah!"
        "{i}Brian fist bumped me.{/i}"
        b "This is gonna be awesome."
        "{i}Brian enthusiastically led the way to the ticket line, Reg trailing shortly behind.{/i}"
        hide reg
        hide brian
        with moveoutright
        show leon:
            linear 0.3 center
        "{i}Leon touched my shoulder.{/i}"
        l "I don't know if can do this."
        mc "What do you mean?"
        l "I get really freaked out by movies like this."
        mc "Really? I didn't take you as one to be scared by movies."
        l "You're one to talk! You get really freaked out by this stuff."
        mc "But at least I enjoy it."
        "{i}I playfully nudged Leon in the arm.{/i}"
        mc "Tell you what... you can hold my hand if you get scared."
        "{i}Leon smiled rolled his eyes.{/i}"
        l "Fine. Let's do this."
        show movie_theatre_interior with fade_to_black
        "{i}To my left, Brian was staring in awe at the screen as a supernatural creature caused blood to come out of a protagonist's eyes.{/i}"
        "{i} To my right, Leon was cowering away from the screen with his legs tucked against his chest and his jacket covering his eyes.{/i}"
        show leon neutral at center
        l "Tell me when it's safe to look."
        "{i}The supernatural creature flew out a window and disappeared into the night.{/i}"
        mc "It just left, you can look."
        "{i}Leon cautiously peeked at the screen, then slowly lowered his jacket and put his feet back on the floor. His knuckles were white from gripping his jacket.{/i}"
        "{i}Within five seconds, we were kit with a jump scare. Leon and I both yelped in surprise. I looked down to realize that, without realizing it, I had leaned sideways against Leon and interlaced my fingers with his.{/i}"
        "{i}Embarrassed, I loosed my grip, but he instinctively pulled me closer. His eyes were fixed on the screen in horror and he didn't even seem to realize what had happened.{/i}"
        "{i}I flushed in embarrassment, but allowed him to stay where he was. For several minutes we remained there, Leon frozen in terror and me unable to concentrate on the movie because I could feel the warmth of Leon's body against my arm.{/i}"
        "{i}On the next jump scare, Leon grabbed my arm with his free hand and buried his face into my shoulder. It was only then that he seemed to realize what had happened. {/i}"
        "{i}He blushed beet red and started pulling himself away.{/i}"
        mc "You can stay there... if you want."
        "{i}Leon blushed deeper, but obliged.{/i}"
        l "Thank you."
        "{i}For the rest of the movie, Leon cowered into my arm and I gripped his hand. Somehow, it made us both feel much less afraid.{/i}"
        scene interrogation_room with fade_to_black
        show leon neutral at center
        l "If Brian hadn't suggested a horror movie..."
        cl "You never would have had that kind of physical intimacy."
        l "Exactly. I hate that you called it \"physical intimacy\", but yeah."
        l "I hated the movie, but..."
        l "It was a great experience."
        l "It told me something about where we stood. It wasn't necessarily a romantic touch, but it told me that I had a chance, you know? That maybe she felt the same way about me that I did about her."
        cl "I understand. Did that event change your relationship to [mc_name] at all?"
        l "For the outside it may not have seemed so, but... I could feel that we were both a little more embarrassed around each other. When we hung out, we'd let ourselves be a little closer to each other. We spoke a little softer and smiled a little more."
        l "It was subtle, but it was important."
        cl "I see. Was there ever a solid affirmation from [mc_name] whether she felt the same about you that you did about her?"
        l "Not really... there was the day I was invited to Reg's party though."
        cl "What happened?"
        l "[mc_name] came to see me play in the soccer game... or so I thought."
        jump Leon11

    label Leon11:
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
        "{i}It's been a long time since I've gone to a soccer game, so I figured today would be a good chance to go to one. Besides, Aden could use the support.{/i}"
        "{i}Plus, I can't stop thinking about the feeling of Leon's warmth in that dark movie theatre..."
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
                jump Leon15e
            "Don't correct him":
                jump Leon12

    label Leon12:
        mc "I'm always happy to come see you play."
        "{i}Leon blushed slightly. Aden looked at me in confusion. {/i}"
        l "Thanks."
        "{i}The look of confusion on Aden's face was slowly replaced with a look of betrayal, then disappointment. He looked down at his feet and wandered off into the cheering crowd. {/i}"
        l "Hey, [mc_name]... Reg is throwing a party this weekend for the varsity team..."
        mc "Uh-huh?"
        l "... would you like to be my date?"
        "{i}My heart skipped a beat. {/i}"
        mc "Uh..."
        l "I don't mean like... date... I just mean each guy gets to bring a plus one, so... will you be my plus one?"
        "{i}I let out a tiny sigh, unsure whether it was a sigh of relief or disappointment.{/i}"
        mc "Of course. I'd be happy to."
        l "Okay! Great! Uh, any chance you could give me a ride home?"
        mc "Absolutely."
        scene interrogation_room with fade_to_black
        show leon neutral center
        l "Oh, man... I hope she couldn't tell how nervous I was to ask her. I felt like I was going to pass out!"
        l "Even in the car ride home, my heart was beating so fast---"
        cl "Mr. So, can you tell me about the night of the party?"
        l "Oh, yeah of course. Get ready though..."
        l "It was a long night."
        jump Leon13

    label Leon13:
        scene bedroom with fade_to_black
        "{i}The day of the party, Leon got a message from Aden saying it had been cancelled. We were disappointed, but decided to hang out anyway. {/i}"
        "{i}We ended up sitting on his bedroom playing games into the evening. {/i}"
        l "Jengaaaaaaa!"
        "{i}As I was focusing on removing a piece from the wooden tower, Leon shoved the tower, sending it toppling. I yelped in surprise, and then we laughed. I playfully hit him in the arm. {/i}"
        mc "You jerk! I was going to win!"
        l "I know. That's why I had to take matters into my own hands!"
        "{i}He playfully hit me back. I retaliated by giving him a light shove. He dramatically topped backward, and the sudden lack of resistance sent me falling toward him. I caught myself by placing a hand on either side of him.{i}"
        "{i}Suddenly, I found myself hovering over him as he lay on his back. My hair had fallen over my shoulder and was brushing his chest. I could see his chest rising and falling ever more rapidly under the strands. {/i}"
        "{i}He was my best friend, but suddenly I could see him as something more. {/i}"
        "{i}No... who the hell am I trying to fool. I'd always been in love with him. It was just at this reason that I realized, without a doubt, that he liked me, too."
        menu:
            "Kiss him":
                jump Leon14
            "Say \"I love you\"":
                jump Leon14

    label Leon14:
        scene interrogation_room with fade_to_black
        show leon neutral at center
        l "No, [mc_name]. You don't get a happy ending. Not from me."
        l "Why? I'll tell you why."
        l "..."
        l "Because I'm already dead."
        l "You killed me."
        l "..."
        scene black
        l "You don't remember? Let me explain in words you can understand."
        l "I'd love to say we got a call from Reg saying the party was on, we went, we had a good time drinking with Brian, we saw Nate on a walk while getting a ride home from Serpens, and spent a fantastic night in each other's company."
        l "But you know that didn't happen."
        l "You went to the party with Aden. You made that decision. It is not something you can undo."
        l "He knew I loved you, something you never managed to pick up on. Because of that, he felt the need to protect me by {i}denying{/i} the party was happening."
        l "You became Reg's girlfriend. You made that decision. It is not something you can undo."
        l "He decided to announce it at the party. When I, one of his closest friends, did not show up, he was understandably {i}angry{/i}."
        l "He called me up and demanded I show up."
        l "You hung out with Brian by the drinks all night. You made that decision. It is not something you can undo."
        l "I got there feeling incredibly low. Aden, someone I considered a friend, had lied to me about the party. Reg, someone I almost considered a brother, thought I was a horrible person and demanded I come to a party I had no chance of enjoying."
        l "I was low enough that when Brian {i}bargained{/i} with me to drink, I gave in. I am not one to give in to that type of thing, but... you'd fallen for someone else and it broke me."
        l "I got too drunk to drive myself home. I called Serpens."
        l "You spend that night with Serpens. You made that decision. It is not something you can undo."
        l "After I climbed in the car with the two of you, it didn't take long for me to figure out what was going on."
        l "In my drunken state I confessed to you, but I knew it was hopeless. It made me feel so {i}depressed{/i} seeing you so close but being unable to reach you."
        l "But, you were with Serpens and there was nothing I could do about it."
        l "I caused a scene and he kicked me out of his car. That's when I saw you and Nate."
        l "You went on a romantic walk with Nate. You made that decision. It is not something you can undo."
        l "Seeing you with him took what was left of my soul and shattered it. He was kind and comforting, but his bottom line was that I would need to {i}accept{/i} that he was with you and that I needed to move on."
        l "I watched you choose five of my friends over me. I left you and Nate with nothing of myself left."
        l "This entire time, you could have sent someone after me. You could have saved me. But, each time, you let yourself fall in love with someone else."
        l "These are decisions {i}you{/i} made. Try all you want, but you can't take them back."
        l "I was so broken that I walked around for hours. It was dark, I was heartbroken, and you were thinking of some other boy you'd spent the night with..."
        l "I didn't notice the car coming toward me as I crossed the street in the darkness of the early morning. You were driving. Just like for the last decade of my life, you didn't see me even though I right in front of you."
        l "I died alone in the dark, in the middle of a strange street in an area of town that scared me."
        l "You only made it to my side after I was gone."
        l "..."
        l "But even this isn't the truth, is it."
        scene interrogation_room with fade_to_black
        show leon neutral at center
        l "You've been staring at the names on these tapes for hours, but you still haven't noticed, have you?"
        l "I am a fictional character, so losing me didn't matter. But you lost someone real, didn't you?"
        l "He was your first love, but you never told him how you felt. You couldn't even manage to be a good friend. By the time he was seventeen, he was so alone in the world that he climbed into the bath, took a handful of pills and fell asleep."
        l "He was surprised to wake up in the morning. More often than not, when someone attempts suicide and it doesn't work, they are thankful. They realize in their near-death experience that they really do have something to live for."
        l "Not him."
        l "He spent one more day of his life acting as though everything was okay. Then while his family was away, he took the family's gun into the backyard... and he put it in his mouth... and he pulled the trigger."
        l "Someone who loved him found him. You don't even remember who, do you? Maybe his sister, maybe his mom... you have no idea."
        l "You should have been there for him. But you let your affection turn to embarrassment and your embarrassment manifest toxicly."
        l "That was six years ago, and you're still carrying around that baggage, aren't you, Airborne_Mana--- uh, I mean, [mc_name]?"
        l "And now you've created a ridiculous game with a confusing premise because art is your only outlet for something like this. You've tried over the years to turn your grief into art, but you're never satisfied."
        l "Grief has five stages, and I'm guessing none of your players noticed until now that they've just followed a broken-hearted artist through each one."
        l "Rearrange the letters in Aden Li and you are left with denial. He denied me what could have been a magical night with the soccer team."
        l "Reg Na is anger. His misplaced anger hurt me beyond words and brought me low enough that I made a night full of mistakes."
        l "Brian Giang is bargaining. He bargained with me to make my first mistake of the night, and he won."
        l "Serpens Dio is depression. He had what I wanted but could never have. Nothing I'd ever experienced was more depressing."
        l "Nate C. Pacce is acceptance. Unfortunately, I couldn't bring myself to accept that I couldn't have you, despite his pleas."
        l "At the end of the day, it was you who killed me. So... who am I?"
        "{i}You are Leon Hewett So.{/i}"
        "{i}You are The One We Lost.{/i}"
        scene black with fade_to_black
        return

    label Leon15a:
        mc "I'll take a caramel macchiato. I've never had one, so I'm curious how it tastes."
        b "Excellent choice! I'll need to hear your opinion once you've tried it."
        mc "I'll let you know before we leave!"
        b "Actually... let me talk to my boss. He might let me take my break a little early today so I can hang out with you for 15 minutes. Gimme a few minutes."
        hide brian with moveoutright
        show leon:
            linear 0.3 center
        "{i}Leon and I dropped our cash on the counter and claimed a small table in the otherwise empty coffee shop.{/i}"
        l "He's a character."
        mc "Seems like it! What's with all the uncomfortable pick-up lines?"
        l "He does that to everyone. He's a jokester."
        mc "Gotcha."
        show brian neutral at rightish with moveinright
        show leon:
            linear 0.3 leftish
        "{i}Brian reappeared by the table holding a try with three drinks. He placed each drink carefully on the table, and then sat in the chair next to mine.{/i}"
        b "So, what do you think?"
        "{i}I took a sip of my drink.{/i}"
        mc "It's delicious!"
        b "I know, right? I gave you an extra pump of caramel."
        "{i}He leaned toward me and dropped his voice to a whisper.{/i}"
        b "{size=-10}Don't tell my boss.{/size}"
        mc "Your secret is safe with me."
        b "How's yours, Leon?"
        l "It's tasty!"
        b "Fantastic. I really am a coffee genius."
        "{i}He turned to me and grabbed one of my hands.{/i}"
        b "I guess that's why it fells like there's something {i}brewing{/i} between the two of us."
        l "Brian, chill it with the coffee pickup lines!"
        b "Dude, I'm just messing with you. I'm not trying to steal your girl."
        l "My--- my girl?"
        b "You seriously think I would do you dirty like that? Naw, man. I may be a bit of a player, but I would never go after another guy's girlfriend."
        l "What?! We're not... she's not..."
        b "Wait, aren't you guys dating?"
        mc "Uh, no... we're just friends."
        b "Oh, my bad, dude. I just assumed by the way you interacted that something was going on."
        l "Oh, no. We've just been friends for a long time."
        b "Ah, I see. Then you wouldn't mind if I took a shot at her?"
        "{i}Brian raised an eyebrow suggestively.{/i}"
        l "Do you ever quit this act of yours?"
        b "Never."
        "{i}Brian realized he's been holding my hand this entire time and quickly dropped it in embarrassment.{/i}"
        b "Well, I think it's about time I went back to work. But hey, it was nice meeting you [mc_name]! Come back to see me soon."
        mc "I'll certainly try!"
        scene interrogation_room with fade_to_black
        show leon neutral at center
        l "Turns out it wasn't a joke. He seriously took a shot at her. She eventually started falling for him."
        l "I had to silently cede her over to another person. It broke my fucking heart."
        cl "Oh, so she was actually dating Brian?"
        l "I don't know if it was ever entirely official, but basically, yeah."
        cl "Were they together the night of Reg's party?"
        l "Yeah."
        cl "So, what happened?"
        l "..."
        l "You know what happened."
        cl "..."
        cl "I know."
        cl "And I am so so sorry."
        "{i}Suddenly I heard a snap and the VHS of Leon's deposition began spitting shiny black tape.{/i}"
        "{i}The screen showed static, and I felt myself go cold.{/i}"
        return

    label Leon15b:
        mc "Aden, I think you should go for it. If you want to try out for the soccer team, you should try out for the soccer team!"
        a "Really, [mc_name]?"
        mc "Who knows? Maybe he’ll surprise you."
        scene interrogation_room with fade_to_black
        l "Aden and [mc_name] really hit it off. She eventually started falling for him."
        l "I had to silently cede her over to another person. It broke my fucking heart."
        cl "Oh, so she was actually dating Aden?"
        l "I don't know if it was ever entirely official, but basically, yeah."
        cl "Were they together the night of Reg's party?"
        l "Yeah."
        cl "So, what happened?"
        l "..."
        l "You know what happened."
        cl "..."
        cl "I know."
        cl "And I am so so sorry."
        "{i}Suddenly I heard a snap and the VHS of Leon's deposition began spitting shiny black tape.{/i}"
        "{i}The screen showed static, and I felt myself go cold.{/i}"
        return

    label Leon15c:
        mc "Let's go to a sit-down place."
        "{l}Leon blushed.{/i}"
        l "Oh... okay."
        mc "I just need to go home to change into something nicer, and then we can go. Sounds good?"
        l "Sounds great!"
        scene interrogation_room with fade_to_black
        show leon neutral at center
        l "It was a really nice dinner and movie. However, I didn't feel anything. It just felt like we were going as friends."
        l "It was at that point that I realized that's all we were going to be. She didn't like me the way I liked her."
        l "I don't know how I didn't notice at the time, but she was actually starting to fall for Serpens. I had to cede her to another person and it broke my fucking heart."
        cl "Oh, so she was actually dating Serpens?"
        l "I don't know if it was ever entirely official, but basically, yeah."
        cl "Were they together the night of Reg's party?"
        l "Yeah."
        cl "So, what happened?"
        l "..."
        l "You know what happened."
        cl "..."
        cl "I know."
        cl "And I am so so sorry."
        "{i}Suddenly I heard a snap and the VHS of Leon's deposition began spitting shiny black tape.{/i}"
        "{i}The screen showed static, and I felt myself go cold.{/i}"
        return

    label Leon15d:
        mc "I'd like to see the rom-com."
        "{i}Brian clicked his tongue and shook his head.{/i}"
        b "I expected more from you, [mc_name]."
        "{i}He smiled and gently tapped my arm with the back of his hand.{/i}"
        b "Kidding."
        r "Let's stop sucking each other's dicks and go buy our tickets before we're late to the movie!"
        scene interrogation_room with fade_to_black
        show leon neutral at center
        l "It movie, but I didn't feel anything. It just felt like we were going as friends."
        l "It was at that point that I realized that's all we were going to be. She didn't like me the way I liked her."
        l "I don't know how I didn't notice at the time, but she was actually starting to fall for Reg. Ironic, considering his comment before we went to buy tickets."
        l "I had to cede her to another person and it broke my fucking heart."
        cl "Oh, so she was actually dating Reg?"
        l "I don't know if it was ever entirely official, but basically, yeah."
        cl "Were they together the night of Reg's party?"
        l "Yeah."
        cl "So, what happened?"
        l "..."
        l "You know what happened."
        cl "..."
        cl "I know."
        cl "And I am so so sorry."
        "{i}Suddenly I heard a snap and the VHS of Leon's deposition began spitting shiny black tape.{/i}"
        "{i}The screen showed static, and I felt myself go cold.{/i}"
        return

    label Leon15e:
        mc "Well, actually Leon... I came to watch Aden play."
        l "Oh, you--- you did?"
        l "I'm sorry, I was being pretty presumptuous I guess. Oh, boy, so embarrassing..."
        "{i}Leon shifted nervously from foot to foot while a smile spread across Aden's face.{/i}"
        l "Well, um, I'm gonna go ahead and go home. Both of you, drive safe!"
        l "{size=-10}God, so embarrassing...{/size}"
        scene interrogation_room with fade_to_black
        show leon neutral at center
        l "I figured out in the most embarrassing way, that she didn't like me how I liked her. She only saw me as a friend."
        l "It was at that point that I realized that's all we were going to be. We would never be together."
        l "I don't know how I didn't notice at the time, but she was actually starting to fall for Nate. I had to cede her to another person and it broke my fucking heart."
        cl "Oh, so she was actually dating Nate?"
        l "I don't know if it was ever entirely official, but basically, yeah."
        cl "Were they together the night of Reg's party?"
        l "Yeah."
        cl "So, what happened?"
        l "..."
        l "You know what happened."
        cl "..."
        cl "I know."
        cl "And I am so so sorry."
        "{i}Suddenly I heard a snap and the VHS of Leon's deposition began spitting shiny black tape.{/i}"
        "{i} The screen showed static, and I felt myself go cold.{/i}"
        return




    return

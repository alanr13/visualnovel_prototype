label day1:
    call open_eyes

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    $ mc_name = "Alan"

    show screen time_hours
    show screen stats

    "Ohh fuck, I overslept AGAIN."

    "I have an important exams in 2 days, but I haven't learned anything."

    menu:
        "Ehhh"

        "Get up and do something.":
            call get_up
        "Rot in bed.":
            show black
            "Bad ending."
            jump _main_menu

    "Okay... so let's get to the bathroom."

    scene bg lazienka with wipeleft

    "*brushes teeth*"

    "okay, let's see with let's see what's going on in the house."

    scene bg salon with wipeleft
    show cat:
        xalign 0.75
        yalign 0.3

    $ hour = "10:15"

    c "Meow, meow"
    mc "Oh, hi sweetie, what's up"
    show cat:
        xalign 0.75
        yalign 0.3
        linear 0.2 yalign 0.2
        linear 0.2 yalign 0.3
        repeat 2
    c "Give me food"

    menu:
        "Feed him.":
            $ learnPointTotal += 5
            mc "No problem my boy, I'll get you something."
            call feed_cat
        "Don't feed him.":
            mc "Mom will feed you, I don't have time."
    
    scene bg korytarz with fade

    show dog at center

    $ hour = "10:20"

    "Oh hello [d]"

    d "Woof, woof"
    d "Let's go for a walk"

    menu:
        "Go for a walk":
            $ learnPointTotal += 5
            mc "Alright! Let's go."
            $ encounteredNami = True
            call walk_with_dog
        "Don't go for a walk":
            mc "Nah, sorry, I need to grind for an exam. Mom will go with you"
            call learn_alone
    
    $ hour = "23:00"

    scene bg pokoj with fade
    "Oh gosh, I'm so tired, let's go sleep and see how exam will go."
    return

label feed_cat:
    scene bg kuchnia with wiperight

    "Okay, let's see what we have there."

    show cat_food_small:
        xalign 0.42
        yalign 0.54

    "I see some cat food in a bowl on a counter."

    return 

label walk_with_dog:
    $ hour = "10:30"
    scene bg dwor1 with fade
    "Ahh, what a nice weather is today."
    scene bg dwor2 with wipeleft
    $ hour = "10:50"
    show nami_smile
    n "Oh, hi [mc]! What a pretty dog, I didn't know that you have one."
    "It's she again. Why won't she go away..."
    mc "H-h-hi."
    n "Can I pet him?"
    mc "Yes."
    n "What is his name?"
    mc "Axel."
    n "Who is the good boy? Axel, who is the good boy?"
    show nami_smile_blush
    n "I wanted to ask you something."
    mc "What's up?"
    show nami_neutral_blush
    n "There will be math exam in 2 days. Would you like to learn together?"
    menu:
        "Learn with Nami.":
            $ learnPointTotal += 10
            $ relationshipPointTotal += 5
            mc "Umm, ok, why not. Maybe together we can learn much more."
            show nami_smile_blush
            n "Yaaay! What about 3 pm in your house."
            mc "Sounds good. So see you then, bye."
            n "Bye."
            call learn_with_nami
        "Learn alone.":
            $ learnPointTotal += 5
            mc "No, I think I'm good learning alone."
            show nami_shout
            n " Uhh, why?!."
            mc "Because I don't know you much and I prefer to learn alone."
            show nami_neutral
            n "Umm, ok..."
            call learn_alone
    return

label learn_with_nami:
    scene bg pokoj
    $ hour = "15:00"
    "Okay, it's 3 pm, Nami should be there in a moment."
    "Oh, there she is."

    scene bg korytarz with wipeleft
    mc "Hi."
    show nami_smile
    n "Hello! How clean!"
    mc "Yeah, had to clean up, so it's more comfortable for us to learn."
    show nami_smile_blush
    n "Thank you!"
    mc "Do you want something to drink?"
    n "Yes, tea please."

    scene bg kuchnia with wipeleft
    "*makes tea*"

    scene bg salon with fade
    $ hour = "15:05"
    mc "There you go."
    show nami_smile
    n "Thanks."
    mc "So, how do you feel about maths? Because to be honest, I don't feel so confident."
    n "Don't worry, I'm good at it, so with me, you can learn much more." 
    mc "Hmm, so if you're good, why do you want to learn with me. We didn't talk much before,
    so it's quite strange."
    n "Well, I think learning together is pretty fun, and I know that you were always bad at maths,
    so why won't I help you?"
    "Is she into me? That's a weird excuse."
    mc "Hmm, that's generous of you..., but thanks :D"

    $ hour = "15:10"

    show nami_shout
    n "Hey! You seem very pesimistic! There's no other context in that."
    mc "Ok, ok, chill. I just have very bad situation, if I don't pass this exam, I will have to
    repeat the class."
    show nami_smile_blush
    n "That's why I'm here to help you :)."
    "Yeaa... She's definitely up to something."
    $ relationshipPointTotal += 5

    mc "Okay, so let's go to my room to learn."
    n "Yeah,let's go!"

    scene bg pokoj

    show nami_neutral at left
    n "What a nice room..."
    "Something draws her attention."

    show nami_smile_blush at right
    n "OHHH, ARE YOU ROBERT KUBICA FAN?! I didn't know that you're also an F1 fan!"
    mc "Yep xD, happened to be."
    n "Can I look at a poster?"

    menu:
        "Show poster":
            mc "Of course"
            hide nami_smile_blush
            $ relationshipPointTotal += 5
            $ learnPointTotal += 10
            call show_poster
        "Focus on learning":
            $ learnPointTotal += 5
            mc "Maybe not..., let's focus on learning."
            n "Ehhh, ok, you're so boring..."

    "*five hours passed*."
    $ hour = "20:10"

    show nami_neutral
    n "That was hell of a learning session."
    mc "Yeah, I'm so tired."
    n "Are you feeling better regarding your math?"
    mc "Yes, quite a bit."

    show nami_shout
    n "QUITE A BIT?! After 5 hours? That's impossible, are you really that dumb?"
    mc "Ey, ey, I was joking, chill out XD. But seriously, now I feel way more confident with my math,
    I'm starting to think that this exam might go well actually."
    show nami_smile
    n "Happy to hear that, it was a good learning session."
    n "Sooo... Good luck at the exam tommorrow!"
    mc "Thanks!"
    $ relationshipPointTotal += 5;
    $ hour = "20:15"
        
    "Anyway, let's play some CS for relax."
    scene bg game with wipeleft
    "*playing till 23:00*"

    return

label learn_alone:
    $ hour = "11:00"

    scene bg korytarz
    "Okay, back home. It's only 11 am, so I don't think I should be rushing with learning."
    "But... hmmm, if I don't pass that math exam, I'll repeat the class and I don't want it."

    menu:
        "Make some tea and start learning.":
            $ learnPointTotal += 10
            scene bg kuchnia with fade

        "One hour of gaming wont be too harsh.":
            scene bg pokoj with fade
            show bg game
            "*7 hours passed*"
            hide bg game
            $ hour = "18:00"
            scene bg pokoj with fade
            "Ok, I'm satisfied, let's go learning, what hour is it?"
            "THE FUUUUCK?! HOW?! IT'S 6 PM ALREADY! FUUUCK."

    scene bg pokoj with fade
    "Alright, let's get through it."
    show bg math
    $ learnPointTotal += 5
    "*learning till 23:00*"
    hide bg math

    return

label show_poster:
    show kubica
    pause 3.0
    n "Wooow, I remember that pretty well, despite being age of 5. My dad is also an F1 fan
    and he was very emotional about that win at Canada."
    mc "Yeah, that was huge. Pity that he had that crash in 2011."
    n "Mhm, he could've been a world champion definitely, massive talent."
    hide kubica
    show nami_smile
    "OMG! Wife material."
    mc "Hey, so if you're an F1 fan, how about we watch a next race that I'll be."
    show nami_smile_blush at right
    n "That's a good plan, but let's focus on learning for an exam first"

    return
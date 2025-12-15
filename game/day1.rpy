label day1:
    scene black
    pause 0.2
    scene bg pokoj
    show bg pokoj at wake_blur
    call open_eyes

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    $ mc_name = "Player"

    "Ohh fuck, I overslept AGAIN."

    "I have an important exams in 2 days, but I haven't learned anything."

    menu:
        "Ehhh"

        "Get up and do something.":
            call get_up
        "Rot in bed.":
            show black
            "Bad ending."

    "Okay... so let's get to the bathroom."

    scene bg lazienka with wipeleft

    "*brushes teeth*"

    "okay, let's see with let's see what's going on in the house."

    scene bg salon with wipeleft
    show cat:
        xalign 0.75
        yalign 0.3

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
            mc "No problem my boy, I'll get you something."
            call feed_cat
        "Don't feed him.":
            mc "Mom will feed you, I don't have time."
    
    scene bg korytarz with fade

    show dog at center

    "Oh hello [d]"

    d "Woof, woof"
    d "Let's go for a walk"

    menu:
        "Go for a walk":
            mc "Alright! Let's go."
        "Don't go for a walk":
            mc "Nah, sorry, I need to grind for an exam. Mom will go with you"

    return

label get_up:
    "It is so hard for me, but it's for my well-being."

    return

label feed_cat:
    scene bg kuchnia with wiperight

    "Okay, let's see what we have there."

    show cat_food_small:
        xalign 0.42
        yalign 0.54

    "I see some cat food in a bowl on a counter."

    return
            
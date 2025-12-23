label day2:
    call open_eyes

    $ hour = "8:00"
    "*one week later*"
    "Oh gosh, tommorrow is one more attempt on the math exam. Gotta learn something today."
    menu:
        "Get up":
            $ learnPointTotal += 5
            call get_up
        "5 minutes":
            call sleep

    scene bg lazienka with wipeleft
    "*brushes teeth*"
    
    "okay, let's see with let's see what's going on in the house."

    scene bg salon with wipeleft
    show cat:
        xalign 0.75
        yalign 0.3

    c "Meow, meow"
    mc "Sorry [c], but I don't really have time."
    c ":("

    scene bg korytarz with wipeleft

    show dog at center

    d "Woof, woof"
    mc "Nah, I'm so sorry [d], but I really gotta learn today."
    d ":("

    scene bg pokoj with fade

    "Okay, let's get to the computer."

    show bg game
    "*few hours passed*"
    hide bg game

    scene bg pokoj with fade
    "What am I doing? Why I'm doing this to myself. This procrastination bs is crazy."
    "It attacks you from nowhere. But chill, chill, it isn't over, right?"

    menu:
        "learn math":
            $ learnPointTotal += 5
            call learning

        "give up":
            show black
            "Bad ending."
            jump _main_menu
    
    "Okay, I think I've learned as much as I could. Maybe I could've learnt more, but... it is what is it."
    "Let's go to sleep."

    return

label learning:
    scene bg math
    "*learns for rest of the day*"

    return

label day1_nami:
    call open_eyes from _call_open_eyes_2

    $ hour = "8:00"
    scene bg pokoj 
    "*yawn* It's sunday, today I will meet with Nami to watch F1 race at 3 pm."
    "Let's get going with the day. I will go to the bathroom, then to kitchen for food and
    to my room back again to play some CS until 3 pm."

    scene bg lazienka with blinds
    "*brushes teeth*"

    scene bg kuchnia with wipeleft
    "*eats some food*"

    scene bg pokoj with wiperight
    show bg game
    "*plays CS until 3 pm*"
    hide bg game
    $ hour = "15:00"
    "*knock, knock*"
    "Oh, it's Nami"

    scene bg korytarz with fade
    show nami_smile
    n "Hiiii :)"
    mc "Hello, the wait for the race is finally over, let's go."
    show nami_smile_blush
    n "Let's go."
    hide nami_smile_blush

    scene bg pokoj with fade
    show race
    menu:
        "Talk to her about the race":
            $ relationshipPointTotal += 5
            mc "Verstappen is simply the best."
            n "Yeah, his driving his phenomenal, but sometimes he acts like a child."
            mc "What do you mean?"
            n "Spain, for example, when he collided with Russell, when he had to give him the position back."
            mc "Oh, okay. Yeah, I can agree on that, that behavior from the 4-time World Champion
            is unacceptable."
        "Silence":
            "*watches the race in silence*"
    $ hour = "17:00"
    hide race
    show nami_smile
    n "What a good race it was. I'm happy that Verstappen won."
    mc "Yep, but pity for Leclerc, too. He could've got 2nd place, but his engine stopped working"
    n "Mhm, grande strategia."
    mc "Umm, Nami, I wanted to ask you something."
    show nami_neutral
    n "What's up?"
    mc "Would you like to hang out more often?"
    if relationshipPointTotal == 5:
        show nami_smile_blush at right
        n "Yea, why not, it's fun."
        hide nami_smile_blush
        show black
        "Best ending."
        $ ending = "best"
        $ reset()
    else:
        "Maybe someday."
        show black
        "Bitter-sweet ending."
        $ ending = "bitter-sweet"
        $ reset()
    return
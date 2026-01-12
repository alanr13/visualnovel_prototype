label day1_1:
    call open_eyes from _call_open_eyes_1
    $ learnPointTotal = 0
    $ hour = "8:00"

    "*long yawn*"
    "*two months later*"
    "Oh gosh, is it a bad dream? No, it is unfortunately a reality. Yeah. Tommorrow's an exam
    that will decide whether I have to repeat the class or not. AND of course I'm not ready enough.
    Shit's crazy..."
    menu:
        "Get up":
            $ learnPointTotal += 10
            call get_up from _call_get_up_1
        "5 minutes":
            call sleep from _call_sleep

    scene bg lazienka with wipeleft
    "*brushes teeth*"
    
    "okay, let's see with let's see what's going on in the house."
    $ hour = "8:15"

    scene bg salon with wipeleft
    show cat:
        xalign 0.75
        yalign 0.3

    mc "Oh hello, [c]"
    c "Meow, meow"
    call show_cat from _call_show_cat
    c "Feed me now"
    menu:
        "Feed him":
            $ learnPointTotal += 5
            call feed_cat from _call_feed_cat_1
        "Don't feed him":
            mc "Sorry, I don't have time today."
            c "*angry noises*"
    
    scene bg korytarz with wiperight
    show dog at center
    d "Woof, woof"
    mc "Hiii, [d]"

    menu:
        "Go for a walk":
            $ learnPointTotal += 5
            mc "Okay, come for a walk, let's chill, before learning"
            scene bg dwor1 with fade
            "*walks with [d]*"
            scene bg dwor2 with wipeleft
            pause 3.0
        "Don't go for a walk":
            mc "Sorry, I have an important exam tommorrow, mum will go with you later."
            d "*sad dog sound*"
    
    scene bg korytarz with blinds
    $ hour = "9:00"
    "Okay, let's go learning."
    scene bg pokoj with wipeleft
    call learn_or_play from _call_learn_or_play
    
    $ hour = "15:00"
    "Time for a break and then let's do it again"
    scene bg kuchnia with blinds
    "*eats food*"
    $ hour = "16:00"
    scene bg pokoj with wipeleft
    call learn_or_play from _call_learn_or_play_1
    pause 5.0
    $ hour = "22:00"
    "*yawns* I'm so tired, let's go to sleep,  I hope I'll pass."

    return
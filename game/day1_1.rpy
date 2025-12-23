label day1_1:
    call open_eyes
    $ hour = "8:00"

    "*long yawn*"
    "Oh gosh, is it a bad dream? No, it is unfortunately a reality. Yeah. Tommorrow's an exam
    that will decide whether I have to repeat the class or not. AND of course I'm not ready enough.
    Shit's crazy..."
    menu:
        "Get up":
            $ learnPointTotal += 5
            call get_up
        "5 minutes":
            call sleep

    scene bg lazienka with wipeleft
    "*brushes teeth*"
    
    "okay, let's see with let's see what's going on in the house."
    return
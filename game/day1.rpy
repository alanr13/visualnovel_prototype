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

    "Ohh fuck, I overslept AGAIN."

    "I need to make this visual novel prototype in 5 days, but for some reason I don't have
    strength in myself to do so..."

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
    show cat at center

    c "Meow, meow"

    return

label get_up:
    "It is so hard for me, but it's for my well-being."


    return
            
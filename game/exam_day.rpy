label exam_day:
    $ hour = "8:00"
    scene black
    pause 0.2
    scene bg pokoj
    show bg pokoj at wake_blur
    call open_eyes

    "*yawn* Ahh, it's the live or die day. Let's see how it will go."

    scene bg lazienka with wipeleft
    "*brushes teeth*"

    scene bg korytarz with wipeleft
    show dog at center

    $ hour = "8:20"

    show dog at center
    d "Woof, woof"
    mc "Sorry [d], I gotta go for the exam, maybe later."
    d ":("

    scene bg szkola with fade

    $ hour = "8:50"
    "10 minutes, before the exam, let's get over it."

    scene bg sala with wipeleft

    $ hour = "9:00"
    "*writes exam*"

    scene bg szkola with wipeleft

    $ hour = "9:50"
    "*waits for exam results*"

    scene bg sala with fade

    $ hour = "10:30"

    show teacher_normal
    t "Alan, unfortunately, but you didn't pass the exam."
    mc "Ehh..."
    show teacher_angrytalk
    t "I'll give you one more chance, but if you don't pass the exam on the second try,
    you will not move up to the next grade."
    mc "O-okay, thank you, miss. I will take the opportunity."
    show teacher_normaltalk
    t "You better pass it."

    return
label exam_day:
    $ hour = "8:00"
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

    if persistent.playthrough == 0:
        if is_exam_passed(learnPointTotal):
            show teacher_normaltalk
            t "Alan, congratulations, you passed an exam with grade [grade]. You can be proud of yourself"
            mc "Yes! Thank you."
        else:
            if attempt == 0:
                show teacher_normal
                t "Alan, unfortunately, but you didn't pass the exam."
                mc "Ehh..."
                show teacher_angrytalk
                t "I'll give you one more chance, but if you don't pass the exam on the second try,
                you will not move up to the next grade."
                mc "O-okay, thank you, miss. I will take the opportunity."
                show teacher_normaltalk
                t "You better pass it."
                $ attempt += 1
            elif attempt == 1:
                show teacher_angrytalk
                t "Alan, you didn't pass the exam for the second time, it means that
                we'll meet in august on the decisive exam, if you will not pass it, then you
                will have to stay in the same class for one more year."
                mc "Ehhhh.... Understood."
                t "Alan, bloody hell, learn, get your act together."
                mc "I know, but it's just for some reason hard for me."
                show teacher_huh at left
                t "Is something bad happening in your life?"
                mc "Not necessarly bad. I just feel like I don't have energy. I have all these
                anxieties which don't give a break. They are constantly attacking me. I don't know
                how to fight it."
                t "Hey, I know how it feels, I had the same problem at your age. If you need to talk, you have
                contact to me on WhatsApp, you can chat with me anytime you want to."
                mc "Thank you miss, I appreciate that."
                t "Stay strong."
                $ attempt += 1
    
        scene bg szkola with blinds
        show nami_smile
        n "Hey [n], how did exam go? Have you passed it?"
        mc "Yes, I passed! Thank you, without your help, I could've passed it."
        show nami_smile_blush
        n "Your welcome :)"
        mc "Hey, I wanted to ask you something. Belgian Grand Prix will be on sunday, but you pro
        bably know it. Would you like to watch it together in my house?"

        if relationshipPointTotal > 10:
            n "What do you think? YES OF COURSE!"
            mc "Woohoo"
        else:
            show nami_neutral
            n "Sorry, I have already planned it with someone else."
            mc "Shame, but anyway... appreciate for help, bye."
            n "No problem, bye."
    elif persistent.playthrough == 1:
        if is_exam_passed(learnPointTotal):
            show teacher_normaltalk
            t "Alan, congratulations, you passed a decisive exam. You can be proud of yourself.
            You've endured the hard time."
            mc "Yes! Thank you."
        else:
            show teacher_angry
            t "Alan, I'm sorry, but you'll have to repeat the class."
            mc "Shame."
    return
    
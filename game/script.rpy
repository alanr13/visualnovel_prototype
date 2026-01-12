# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:
    if persistent.playthrough == 0:
        show screen time_hours
        show screen stats

        call day1 from _call_day1
        if isEndingBad(ending):
            return
        call exam_day from _call_exam_day
        
        if persistent.exam_passed == False:
            call day2 from _call_day2
            if isEndingBad(ending):
                return
            call exam_day from _call_exam_day_1
            if persistent.exam_passed == True:
                return
        else:
            $ reset()
            return

    elif persistent.playthrough == 1:
        show screen time_hours
        show screen stats

        if persistent.encounteredNami == True and persistent.exam_passed == True:
            call day1_nami from _call_day1_nami
        elif persistent.encounteredNami == False and persistent.exam_passed == False:
            call day1_1 from _call_day1_1
            call exam_day from _call_exam_day_2
return


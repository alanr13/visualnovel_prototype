# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:

    # day one
if persistent.playthrough == 0:
    call day1

    # exam day

    call exam_day

    # day two

    call day2

    # exam day

    call exam_day

    return

# elif persistent.playthrough == 1 && persistent.ending_failed:
#     call day1

#     # exam day

#     call exam_day

#     # day two

#     call day2

#     # exam day

#     call exam_day

#     return


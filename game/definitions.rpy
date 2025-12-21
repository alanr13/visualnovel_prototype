define EYE_OPENING_TIME = 1.5
define c = Character("Tygrysek")
define d = Character("Axel")
define mc = DynamicCharacter("mc_name")
define n = DynamicCharacter("n_name")
define t = DynamicCharacter("t_name")

default examPointTotal = 0
default learnPointTotal = 0
default relationshipPointTotal = 0
default mc_name = "Kupcia"
default n_name = "Nami"
default t_name = "Teacher"

default hour = "10:00"

image hour_text = Text("10:00", size=30, xalign=0.0, yalign=0.0)

image eyelid_top_img = Solid("#000", xysize=(config.screen_width, config.screen_height // 2))
image eyelid_bottom_img = Solid("#000", xysize=(config.screen_width, config.screen_height // 2))


image nami_neutral:
    "images/nami_neutral.png"
    yalign 0
image nami_neutral_blush:
    "images/nami_neutral_blush.png"
    yalign 0
image nami_shout:
    "images/nami_shout.png"
    yalign 0
image nami_shout_blush:
    "images/nami_shout_blush.png"
    yalign 0
image nami_smile:
    "images/nami_smile.png"
    yalign 0
image nami_smile_blush:
    "images/nami_smile_blush.png"
    yalign 0

image teacher_normal:
    "images/teacher_normal.png"
    yalign 0
image teacher_normaltalk:
    "images/teacher_normaltalk.png"
    yalign 0
image teacher_angry:
    "images/teacher_angry.png"
    yalign 0
image teacher_angrytalk:
    "images/teacher_angrytalk.png"
    yalign 0
image teacher_angrylaugh:
    "images/teacher_angrylaugh.png"
    yalign 0
image teacher_huh:
    "images/teacher_huh.png"
    yalign 0

image cat = "images/cat_meowjak.png"
image dog = "images/dog.png"
image cat_food = "images/cat_food.png"
image cat_food_small:
    "images/cat_food.png"
    zoom 0.35

screen time_hours():
    frame:
        xalign 0.0 yalign 0.0

        text "[hour]" size 30

screen stats():
    frame:
        xalign 1.0 yalign 0.0
        vbox:
            text "Learning: [learnPointTotal]"
            text "Exam: [examPointTotal]"
            text "Relationship: [relationshipPointTotal]"
    
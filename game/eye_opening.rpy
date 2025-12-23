transform eyelid_top:
    xpos 0
    ypos 0
    linear EYE_OPENING_TIME ypos -config.screen_height // 2

transform eyelid_bottom:
    xpos 0
    ypos config.screen_height // 2
    linear EYE_OPENING_TIME ypos config.screen_height


transform wake_blur:
    blur 15
    linear EYE_OPENING_TIME blur 0

label open_eyes:
    scene black
    pause 0.2
    scene bg pokoj
    show bg pokoj at wake_blur

    show eyelid_top_img at eyelid_top
    show eyelid_bottom_img at eyelid_bottom

    pause EYE_OPENING_TIME

    hide eyelid_top_img
    hide eyelid_bottom_img

    return
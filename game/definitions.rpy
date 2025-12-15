define EYE_OPENING_TIME = 1.5
define c = Character("Tygrysek")
define d = Character("Axel")
define mc = DynamicCharacter("mc_name")

default mc_name = "Kupcia"

image eyelid_top_img = Solid("#000", xysize=(config.screen_width, config.screen_height // 2))
image eyelid_bottom_img = Solid("#000", xysize=(config.screen_width, config.screen_height // 2))


image cat = "images/cat_meowjak.png"
image dog = "images/dog.png"
image cat_food = "images/cat_food.png"
image cat_food_small:
    "images/cat_food.png"
    zoom 0.35
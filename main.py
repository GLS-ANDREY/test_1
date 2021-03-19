import wrap_py as wrap
import wrap_py.ru

rezhim = "ne taskat"
wrap.world.create_world(1000, 1000)
wrap.world.set_world_background_color([255, 69, 78])
blue_man = wrap.sprite.add_sprite("blue_man", 500, 500, False)
kolt = wrap.sprite.add_sprite("kolt", 500, 500, False)
rocket = wrap.sprite.add_sprite("rocket_man", 500, 500, True, "rocket")
#wrap.sprite.add_sprite("blue_man",500,500,True,"man1")


@wrap.on_mouse_move
def taskat(buttons, pos):
    global rezhim
    if rezhim == "taskat":
        wrap.sprite.move_sprite_to(rocket, pos[0], pos[1])
    if rezhim == "kolt_taskat":
        wrap.sprite.move_sprite_to(kolt, pos[0], pos[1])
    if rezhim == "blue_man_taskat":
        wrap.sprite.move_sprite_to(blue_man, pos[0], pos[1])
    if 1 not in buttons:
        rezhim = "ne taskat"


@wrap.on_mouse_down
def na_nazhatie(button, pos):
    global rezhim
    popal_po_rakete = wrap.sprite.sprite_collide_point(rocket, pos[0], pos[1])
    popal_po_koltu = wrap.sprite.sprite_collide_point(kolt, pos[0], pos[1])
    popal_po_blue_manu = wrap.sprite.sprite_collide_point(blue_man, pos[0], pos[1])
    kolt_vidimi = wrap.sprite.is_sprite_visible(kolt)
    rocket_vidim = wrap.sprite.is_sprite_visible(rocket)
    blue_man_vidimi = wrap.sprite.is_sprite_visible(blue_man)
    if popal_po_rakete == True and button == 3 and rocket_vidim == True:
        wrap.sprite.hide_sprite(rocket)
        wrap.sprite.show_sprite(kolt)

    elif popal_po_koltu == True and button == 3 and kolt_vidimi == True:
        wrap.sprite.hide_sprite(kolt)
        wrap.sprite.show_sprite(blue_man)

    if rezhim == "ne taskat" and button == 1 and popal_po_rakete == True:
        rezhim = "taskat"
    if rezhim == "ne taskat" and button == 1 and popal_po_koltu == True and kolt_vidimi == True:
        rezhim = "kolt_taskat"
    if rezhim == "ne taskat" and button == 1 and popal_po_blue_manu == True and blue_man_vidimi == True:
        rezhim = "blue_man_taskat"


@wrap.on_mouse_up
def na_otpuskanie():
    global rezhim
    rezhim = "ne taskat"

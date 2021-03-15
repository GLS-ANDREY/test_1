import wrap_py, wrap_py.ru
from wrap_py import world, sprite

world.create_world(850, 850)
world.set_world_background_color([255, 0, 3])
sprite.add_sprite("rocket_man", 425, 425, True, "rocket")
@wrap_py.on_mouse_down(1)
def taskat():
    print(5)
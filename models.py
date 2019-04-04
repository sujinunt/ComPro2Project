import arcade.key
MOVEMENT_SPEED = 5
class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y


class Surviver(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.vx = 0
        self.vy = 0

    def update(self, delta):
        self.x += self.vx
        if self.x >= self.world.width:
            self.x = self.world.width


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.surviver = Surviver(self, 50, 100)

    def update(self, delta):
        self.surviver.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.A:
            self.surviver.vx-=MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.surviver.vx+=MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.surviver.vx = 0
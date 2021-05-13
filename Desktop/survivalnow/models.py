
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
        return


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.surviver = Surviver(self, 50, 100)

    def update(self, delta):
        self.surviver.update(delta)
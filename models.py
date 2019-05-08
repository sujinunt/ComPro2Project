import arcade.key
import math
import random
MOVEMENT_SPEED = 5
Zombie_SPEED = 3

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class Zombie(arcade.Sprite):

    def follow_sprite(self, player_sprite):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if random.randrange(100) == 0:
            start_x = self.center_x
            start_y = self.center_y
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)
            self.change_x = math.cos(angle) * Zombie_SPEED
            self.change_y = math.sin(angle) * Zombie_SPEED


class Surviver(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.vx = 0
        self.vy = 0

    def update(self, delta):
        self.x += self.vx
        self.y +=self.vy
        if self.x >= self.world.width-18:
            self.x = self.world.width-18
        elif self.x <= 22:
            self.x = 22
        elif self.y >= self.world.height-50:
            self.y = self.world.height-50
        elif self.y <= 50:
            self.y = 50


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.direction = 0
        self.weapon = 0 #no weapon
        self.surviver = Surviver(self, 50, 100)

    def update(self, delta):
        self.surviver.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.A:
            self.surviver.vx-=MOVEMENT_SPEED
            self.direction = 1
        elif key == arcade.key.D:
            self.surviver.vx+=MOVEMENT_SPEED
            self.direction = 0
        elif key == arcade.key.W:
            self.surviver.vy+=MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.surviver.vy-=MOVEMENT_SPEED
        if self.weapon==0:
            if key == arcade.key.F:
                self.weapon = 1
        elif self.weapon==1:
            if key == arcade.key.F:
                self.weapon=0

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.surviver.vx = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.surviver.vy = 0

import arcade
import random
import math
from models import World
from models import Zombie

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Survival now"
Zombie_count = 10
BULLET_SPEED = 5


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()


class SurvivalnowWindow(arcade.Window):
    def __init__(self, width, height,title):
        super().__init__(width, height,title)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.survival_sprite = ModelSprite('images/surviver_stay.png',
                                      model=self.world.surviver)
        self.survival_spritegun = ModelSprite('images/surviver_gun.png',
                                               model=self.world.surviver)
        self.total_time = 0.0
        self.zombielist=None
        self.bullet_list = None

    def setup(self):
        self.background = arcade.load_texture("images/background.png")
        """Time set sec"""
        self.total_time = 1000.0
        self.zombielist = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        for i in range(Zombie_count):
            zombie = Zombie("images/Zombie_stay.png", 1)
            # Position the zombie
            zombie.center_x = random.randint(600,700)
            zombie.center_y = random.randrange(SCREEN_HEIGHT)
            # Add the zombie to the lists
            self.zombielist.append(zombie)

    def update(self, delta):
        self.world.update(delta)
        self.total_time -= delta
        for zombie in self.zombielist:
            zombie.follow_sprite(self.survival_sprite)
        self.bullet_list.update()
        for bullet in self.bullet_list:
            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.zombielist)
            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.kill()
            # For every coin we hit, add to the score and remove the coin
            for zombie in hit_list:
                zombie.kill()
            # If the bullet flies off-screen, remove it.
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.kill()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        if self.world.weapon == 0:
            self.survival_sprite.draw()
        elif self.world.weapon == 1:
            self.survival_spritegun.draw()
        self.zombielist.draw()
        self.bullet_list.draw()
        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        output = f"Time: {minutes:02d}:{seconds:02d}"
        arcade.draw_text(output, 10, 370, arcade.color.BLACK, 20)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key,key_modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        # Create a bullet
        bullet = arcade.Sprite("images/Bullet.png", 0.8)
        start_x = self.survival_sprite.center_x
        start_y = self.survival_sprite.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y
        dest_x = x
        dest_y = y
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
        bullet.angle = math.degrees(angle)
        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED
        self.bullet_list.append(bullet)


if __name__ == '__main__':
    window = SurvivalnowWindow(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_TITLE)
    window.setup()
    arcade.run()
import arcade
import random
from models import World
from models import Zombie

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Survival now"
Zombie_count = 10



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


    def setup(self):
        self.background = arcade.load_texture("images/background.png")
        """Time set sec"""
        self.total_time = 1000.0
        self.zombielist = arcade.SpriteList()
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

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        if self.world.weapon == 0:
            self.survival_sprite.draw()
        elif self.world.weapon == 1:
            self.survival_spritegun.draw()
        self.zombielist.draw()
        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        output = f"Time: {minutes:02d}:{seconds:02d}"
        arcade.draw_text(output, 10, 370, arcade.color.BLACK, 20)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key,key_modifiers)


if __name__ == '__main__':
    window = SurvivalnowWindow(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_TITLE)
    window.setup()
    arcade.run()
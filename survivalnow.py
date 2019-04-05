import arcade

from models import World

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Survival now"


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
        self.total_time = 0.0

    def setup(self):
        arcade.set_background_color(arcade.color.GRAY)
        """Time set sec"""
        self.total_time = 1000.0

    def update(self, delta):
        self.world.update(delta)
        self.total_time -= delta

    def on_draw(self):
        arcade.start_render()
        self.survival_sprite.draw()
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
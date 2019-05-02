import arcade
import random
import math
import models
import tkinter
from tkinter import ttk
from models import World
from models import Zombie

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Survival now"
BULLET_SPEED = 10
username='Unknown'
# These numbers represent "states" that the game can be in.
INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3
win = 4


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

    def hit(self,sprite):
        if arcade.check_for_collision(self,sprite):
            return True


class SurvivalnowWindow(arcade.Window):
    def __init__(self, width, height,title):
        super().__init__(width, height,title)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.current_state = INSTRUCTIONS_PAGE_0
        self.total_time = 0.0
        self.Lasttime=0
        self.coin=0
        self.ammo=100
        self.zombiecount = 50
        self.hp =100
        self.zombielist=None
        self.bullet_list = None
        self.potionlist=None
        self.countlevel=1
        self.countzombiehit=0
        self.level = 1
        #Menu
        self.instructions = []
        texture = arcade.load_texture("images/Gamemenu.png")
        self.instructions.append(texture)
        texture = arcade.load_texture("images/Gameinstruction.png")
        self.instructions.append(texture)

    def setup(self):#set game start
        self.background = arcade.load_texture("images/background.png")
        #Character
        self.survival_sprite = ModelSprite('images/surviver_stay.png',
                                           model=self.world.surviver)
        self.survival_spritegun = ModelSprite('images/surviver_gun.png',
                                              model=self.world.surviver)
        self.survival_sprite_left = ModelSprite('images/surviver_stay_left.png',
                                                model=self.world.surviver)
        self.survival_spritegun_left = ModelSprite('images/surviver_gun_left.png',
                                                   model=self.world.surviver)
        self.cam=ModelSprite('images/hppotion.png',model=self.world.surviver)
        #---------------------------------------------------------------------------
        """Time set sec"""
        self.total_time=10
        self.zombiecount = 20
        self.zombielist = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.potionlist=arcade.SpriteList()
        self.countzombiehit = 0
        #level-------------------------------------
        if (self.countlevel % 2) == 0:
            self.total_time+=10*(self.level)
            self.ammo+=10
            models.Zombie_SPEED+=1
        elif self.countlevel==1:
            self.hp = 100
            self.ammo = 100
            self.coin = 0
            self.total_time=10.0
            self.Lasttime=0
            models.Zombie_SPEED=3
        #-------------------------------------------
        #zombie-----------------------------------------
        for i in range(self.zombiecount):
            zombie = Zombie("images/Zombie_stay.png", 1)
            No_place_zombie = False
            randomLeftorRight=random.randint(0,1)
            while not No_place_zombie:
            # Position the zombie
                if randomLeftorRight==0:
                    zombie.center_x = random.randint(1000,5000)
                elif randomLeftorRight==1:
                    zombie.center_x = random.randint(-3000, -200)
                zombie.center_y = random.randint(0,SCREEN_HEIGHT)
                zombie_hit_list = arcade.check_for_collision_with_list(zombie,self.zombielist)
                if len(zombie_hit_list) == 0:
                    No_place_zombie = True
            # Add the zombie to the lists
            self.zombielist.append(zombie)
        #----------------------------------------------------

    def draw_instructions_page(self, page_number):
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH //2, SCREEN_HEIGHT //2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)

    def draw_game_over(self):
        output = f"Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)
        survivaltime = f"SurvivalTime is {self.Lasttime:.2f} sec"
        arcade.draw_text(survivaltime, 250, 350, arcade.color.WHITE, 24)
        output = "Click to restart"
        arcade.draw_text(output, 300, 300, arcade.color.WHITE, 24)

    def draw_Win(self):
        output = "You Survive!"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)
        reward = f"Reward: Ammo+10"
        arcade.draw_text(reward, 260, 350, arcade.color.WHITE, 24)
        output = "Click to go to the next level"
        arcade.draw_text(output, 230, 300, arcade.color.WHITE, 24)

    def update(self, delta):
        if self.current_state == GAME_RUNNING:
            self.world.update(delta)
            self.total_time -= delta
            self.Lasttime+=delta
            if self.hp>=100:
                self.hp=100
            if self.world.weapon==0:
                self.hp+=0.1
            #zombie-----------------------------------------
            for zombie in self.zombielist:
                if self.world.weapon == 0:
                    if self.world.direction == 0:
                        zombie.follow_sprite(self.survival_sprite)
                        hitplayerright = self.survival_sprite.hit(zombie)
                        if hitplayerright is True:
                            self.hp -= 0.7
                    elif self.world.direction == 1:
                        zombie.follow_sprite(self.survival_sprite_left)
                        hitplayerleft = self.survival_sprite_left.hit(zombie)
                        if hitplayerleft is True:
                            self.hp -= 0.7
                elif self.world.weapon == 1:
                    if self.world.direction == 0:
                        zombie.follow_sprite(self.survival_spritegun)
                        hitplayerrightgun = self.survival_spritegun.hit(zombie)
                        if hitplayerrightgun is True:
                            self.hp -= 0.7
                    elif self.world.direction == 1:
                        zombie.follow_sprite(self.survival_spritegun_left)
                        hitplayerleftgun = self.survival_spritegun_left.hit(zombie)
                        if hitplayerleftgun is True:
                            self.hp -= 0.7
            #-----------------------------------------------------------
            #Character-------------------------------
            if self.hp<=0:#dead
                self.hp=0
                self.current_state = GAME_OVER
            if self.total_time <= 0.0:  # time up
                self.current_state = win
            #----------------------------------------
            #potion-----------------------------------------
            for potion in self.potionlist:
                if self.world.weapon == 0:
                    if self.world.direction == 0:
                        hitplayerright = self.survival_sprite.hit(potion)
                        if hitplayerright is True:
                            self.hp += 10
                            potion.kill()
                    elif self.world.direction == 1:
                        hitplayerleft = self.survival_sprite_left.hit(potion)
                        if hitplayerleft is True:
                            self.hp += 10
                            potion.kill()
                elif self.world.weapon == 1:
                    if self.world.direction == 0:
                        hitplayerrightgun = self.survival_spritegun.hit(potion)
                        if hitplayerrightgun is True:
                            self.hp += 10
                            potion.kill()
                    elif self.world.direction == 1:
                        hitplayerleftgun = self.survival_spritegun_left.hit(potion)
                        if hitplayerleftgun is True:
                            self.hp += 10
                            potion.kill()
            # ----------------------------------------

            #Bullet--------------------------------------
            self.bullet_list.update()
            if self.world.weapon == 1 and self.ammo>0:
                for bullet in self.bullet_list:
                    hit_list = arcade.check_for_collision_with_list(bullet, self.zombielist)
                    if len(hit_list) > 0:
                        bullet.kill()
                        self.ammo-=1
                    for zombie in hit_list:
                        if self.countzombiehit==2:
                            zombie.kill()
                            self.coin+=10
                            drop_potion = random.randint(0,10)
                            if drop_potion==3 or drop_potion ==7:
                                potion = arcade.Sprite("images/hppotion.png")
                                potion.set_position(zombie.center_x,zombie.center_y)
                                self.potionlist.append(potion)
                            zombie = Zombie("images/Zombie_stay.png", 1)
                            randomLeftorRight=random.randint(0,1)
                            No_place_zombie = False
                            while not No_place_zombie:
                                if randomLeftorRight == 0:
                                    zombie.center_x = random.randint(1000, 5000)
                                elif randomLeftorRight == 1:
                                    zombie.center_x = random.randint(-3000, -200)
                                zombie.center_y = random.randint(0, SCREEN_HEIGHT)
                                zombie_hit_list = arcade.check_for_collision_with_list(zombie, self.zombielist)
                                if len(zombie_hit_list) == 0:
                                    No_place_zombie = True
                            self.zombielist.append(zombie)
                            self.countzombiehit = 0
                        else:
                            self.countzombiehit+=1
                    if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                        bullet.kill()
                        self.ammo-=1
            #-----------------------------------------------------------------

    def draw_game(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.cam.draw()
        #Character----------------------------------------
        if self.world.weapon == 0:
            if self.world.direction==0:
                self.survival_sprite.draw()
            elif self.world.direction==1:
                self.survival_sprite_left.draw()
        elif self.world.weapon == 1:
            if self.world.direction==0:
                self.survival_spritegun.draw()
            elif self.world.direction==1:
                self.survival_spritegun_left.draw()
            self.bullet_list.draw()
        #--------------------------------------------------
        self.zombielist.draw()
        self.potionlist.draw()
        # Interface----------------------
        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        arcade.draw_rectangle_outline(self.cam.center_x+8,self.cam.center_y+70,100,15,arcade.color.BLACK)
        hp = f"HP:{self.hp:.0f}"
        arcade.draw_rectangle_filled(self.cam.center_x+8,self.cam.center_y+70,self.hp,15,arcade.color.RED)
        arcade.draw_text(hp,self.cam.center_x-40,self.cam.center_y+65,arcade.color.BLACK)
        arcade.draw_rectangle_filled(SCREEN_WIDTH-SCREEN_HEIGHT,SCREEN_HEIGHT-20,SCREEN_HEIGHT*2,40,arcade.color.BLACK)
        Time = f"Time: {minutes:02d}:{seconds:02d}|Level:{self.level}"
        arcade.draw_text(Time, 10, SCREEN_HEIGHT-30, arcade.color.WHITE, 20)
        Ammo = f"Ammo: {self.ammo}| Coin: {self.coin}"
        arcade.draw_text(Ammo, SCREEN_WIDTH - 325, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()
        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instructions_page(0)
        elif self.current_state == INSTRUCTIONS_PAGE_1:
            self.draw_instructions_page(1)
        elif self.current_state == GAME_RUNNING:
            self.draw_game()
        elif self.current_state==win:
            self.draw_game()
            self.draw_Win()
        else:
            self.draw_game()
            self.draw_game_over()

    def on_key_press(self, key, key_modifiers):
        if self.current_state == GAME_RUNNING:
            self.world.on_key_press(key, key_modifiers)
            if key==arcade.key.R and self.coin>=200:
                self.ammo+=10
                self.coin-=200

    def on_key_release(self, key, key_modifiers):
        if self.current_state == GAME_RUNNING:
            self.world.on_key_release(key,key_modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.current_state == INSTRUCTIONS_PAGE_0:
            # Next page of instructions.
            self.current_state = INSTRUCTIONS_PAGE_1
        elif self.current_state == INSTRUCTIONS_PAGE_1:
            # Start the game
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            # Restart the game.
            self.countlevel=1
            self.level=1
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == win:
            # Restart the game.
            self.level+=1
            self.countlevel=2
            self.setup()
            self.current_state = GAME_RUNNING
        # Create a bullet
        if self.current_state == GAME_RUNNING:
            if self.world.weapon == 1 and self.ammo>0:
                bullet = arcade.Sprite("images/Bullet.png", 0.8)
                if self.world.direction ==0:
                    self.start_x1 = self.survival_spritegun.center_x
                    self.start_y1 = self.survival_spritegun.center_y
                elif self.world.direction==1:
                    self.start_x1 = self.survival_spritegun_left.center_x
                    self.start_y1 = self.survival_spritegun_left.center_y
                start_x = self.start_x1
                start_y = self.start_y1
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
    window = SurvivalnowWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
# //This project relied heavily on the pygame library for the python language
# and the tutorials for the library that can be found on programarcagegames.com/
# That being said, the concept for the game is mine and the sprites used in the game
# were created by me in Microsoft Paint.//
# LCD_Solid font from http://www.fontspace.com/lcd-solid/lcd-solidda
# http://opengameart.org/content/explosion-set-1-m484-games

import pygame
import math
import random
# initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (225, 255, 255)
GREEN = (0, 255, 0)
RED = (225, 0, 0)
BLUE = (0, 0, 255)
GREY = (160,160,160)
YELLOW = (255, 242, 0)

class Player_ship(pygame.sprite.Sprite):
    # class for player 1 ship
    def __init__(self):
        super().__init__()
        # init sprite and hitbox/rect
        self.image = player1_sprite
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        # screen boundaries so you don't float off screen
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
        self.change_x = 0
        self.change_y = 0
        self.angle = 0
        self.con_angle = 0
        self.HP = 0
        self.score = 0
    def update(self):
        #moves the ship around when an arrow key is pressed
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        mouse_pos = pygame.mouse.get_pos()
        # makes the ship rotate towards the mouse, in order to aim

        self.angle = -math.atan2(self.rect.y - mouse_pos[1], self.rect.x - mouse_pos[0]) * (180 / math.pi) + 100

        # boundaries
        # boundaries are set to these numbers so that the conditions don't overlap
        # and leave the ship stuck the side of the screen bouncing back and forth
        if self.rect.right > self.right_boundary:
            self.rect.x = -20
        elif self.rect.left < self.left_boundary:
            self.rect.x = 1250

        if self.rect.bottom > self.bottom_boundary:
            self.rect.y = -20
        elif self.rect.top < self.top_boundary:
            self.rect.y = 690


class Enemy1_ships(pygame.sprite.Sprite):
    # class for enemy_ships using enemy_ship1 png
    def __init__(self):
        # call the parent class constructor
        super().__init__()
        #load the image
        self.image = enemy1_sprite
        # set transparent color
        self.image.set_colorkey(BLACK)
        # rectangle object with the dimensions of the image
        #update the position of image by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        # edges of bounce
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
        self.angle =  0
        # current speed and direction =
        self.change_x = 0
        self.change_y = 0

        # Health points
        self.HP = 0


    def update(self):

        pos = [player1.rect.x, player1.rect.y]
        #self.image = pygame.transform.rotate(self.image, self.angle)
        #updates after each frame
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        #determines the angle difference between the enemy and the player, so that the enemy can be turned appropriately
        self.angle = -math.atan2(self.rect.y - pos[1], self.rect.x - pos[0]) * (180/math.pi) + 100
        # change direction if the edge of the screen is touched
        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1


        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1

class Enemy2_ships(pygame.sprite.Sprite):
    # class for enemy_ships using enemy_ship1 png
    def __init__(self):
        # call the parent class constructor
        super().__init__()
        #load the image
        self.image = enemy2_sprite
        # set transparent color
        self.image.set_colorkey(BLACK)
        # rectangle object with the dimensions of the image
        #update the position of image by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        # edges of bounce
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
        self.angle =  0
        # current speed and direction =
        self.change_x = 0
        self.change_y = 0

        # Health points
        self.HP = 0


    def update(self):
        pos = [player1.rect.x, player1.rect.y]
        #self.image = pygame.transform.rotate(self.image, self.angle)
        #updates after each frame
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.angle = -math.atan2(self.rect.y - pos[1], self.rect.x - pos[0]) * (180/math.pi) + 100
        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1


        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1

class Boss_ships(pygame.sprite.Sprite):
    # class for enemy_ships using enemy_ship1 png
    def __init__(self):
        # call the parent class constructor
        super().__init__()
        #load the image
        self.image = boss_sprite
        # set transparent color
        self.image.set_colorkey(BLACK)
        # rectangle object with the dimensions of the image
        #update the position of image by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        # edges of bounce
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
        self.angle =  0
        # current speed and direction =
        self.change_x = 0
        self.change_y = 0

        # Health points
        self.HP = 0

    def spray(self, n,x_d, y_d):
        # should create a bullet hell type spray, key word is should
        x_s = player1.rect.x - 200
        y_s = player1.rect.y - 200

        # determines the spread of the bullets, might have to tweak it a bit
        for i in range(0,n,1):
            boss_bullet = BossBullet(self.rect.x + 30, self.rect.y +60, x_s, y_s)
            enemy_bullet_list.add(boss_bullet)
            global_sprites_list.add(boss_bullet)
            y_s += y_d
            x_s += x_d


    def update(self):
        pos = [player1.rect.x, player1.rect.y]
        #self.image = pygame.transform.rotate(self.image, self.angle)
        #updates after each frame
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        # same thing as the enmey angles, makes sure that the boss is turning towards the player
        self.angle = -math.atan2(self.rect.y - pos[1], self.rect.x - pos[0]) * (180/math.pi)
        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1


        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1


class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_start_x, bullet_start_y, bullet_dest_x, bullet_dest_y):

         # starting position should be somewhere around the ship, got to figure that out
         # destination should be the mouse which I will eventually convert to a croshair
         # Most likely going to stop the bullet at the destination and make it disapear
        # apparently this calls the parent class (Sprite) constructor (source google)
        super().__init__()

        self.image = pygame.Surface([11, 8])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        # starting position of the bullet, going to need some tweaking
        self.rect.x = bullet_start_x
        self.rect.y = bullet_start_y
        # pass in floating point numbers which are more accurate for aiming
        self.floating_point_x = bullet_start_x
        self.floating_point_y = bullet_start_y
        # angles for aiming between the starting point and the destination
        bullet_x_diff = bullet_dest_x - bullet_start_x
        bullet_y_diff = bullet_dest_y - bullet_start_y
        bullet_angle = math.atan2(bullet_y_diff, bullet_x_diff)

        # DAHMAGE
        self.damage = 10
        # taking into account the angle, calculate the change in x and y
        bullet_velocity = 11
        self.change_x = math.cos(bullet_angle) * bullet_velocity
        self.change_y = math.sin(bullet_angle) * bullet_velocity


    def update(self):
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        # convert rectx and recty to intergers
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

        # when the bullet flies off the screen, kill it
        if self.rect.x < 0 or self.rect.x > size[0] or self.rect.y < 0 or self.rect.y > size[1]:
            self.kill()

class Bomb(pygame.sprite.Sprite):
    def __init__(self, bomb_start_x, bomb_start_y, bomb_dest_x, bomb_dest_y):

         # starting position should be somewhere around the ship, got to figure that out
         # destination should be the mouse which I will eventually convert to a croshair
         # Most likely going to stop the bullet at the destination and make it disapear
        # apparently this calls the parent class (Sprite) constructor (source google)
        super().__init__()

        self.image = pygame.Surface([13, 13])
        self.image.fill(GREY)
        self.rect = self.image.get_rect()

        # starting position of the bullet, going to need some tweaking
        self.rect.x = bomb_start_x
        self.rect.y = bomb_start_y
        # pass in floating point numbers which are more accurate for aiming
        self.floating_point_x = bomb_start_x
        self.floating_point_y = bomb_start_y
        # angles for aiming between the starting point and the destination
        bomb_x_diff = bomb_dest_x - bomb_start_x
        bomb_y_diff = bomb_dest_y - bomb_start_y
        bomb_angle = math.atan2(bomb_y_diff, bomb_x_diff)

        # DAHMAGE
        self.damage = 30
        # taking into account the angle, calculate the change in x and y
        bomb_velocity = 6
        self.change_x = math.cos(bomb_angle) * bomb_velocity
        self.change_y = math.sin(bomb_angle) * bomb_velocity


    def update(self):
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        # convert rectx and recty to intergers
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

        # when the bullet flies off the screen, kill it
        if self.rect.x < 0 or self.rect.x > size[0] or self.rect.y < 0 or self.rect.y > size[1]:
            self.kill()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, enemy_bullet_start_x, enemy_bullet_start_y, enemy_bullet_dest_x, enemy_bullet_dest_y):

         # starting position should be somewhere around the ship, got to figure that out
         # destination should be the mouse which I will eventually convert to a croshair
         # Most likely going to stop the bullet at the destination and make it disapear
        # apparently this calls the parent class (Sprite) constructor (source google)
        super().__init__()

        self.image = pygame.Surface([11, 8])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        # starting position of the bullet, going to need some tweaking
        self.rect.x = enemy_bullet_start_x
        self.rect.y = enemy_bullet_start_y
        # pass in floating point numbers which are more accurate for aiming
        self.floating_point_x = enemy_bullet_start_x
        self.floating_point_y = enemy_bullet_start_y
        # angles for aiming between the starting point and the destination
        enemy_bullet_x_diff = enemy_bullet_dest_x - enemy_bullet_start_x
        enemy_bullet_y_diff = enemy_bullet_dest_y - enemy_bullet_start_y
        enemy_bullet_angle = math.atan2(enemy_bullet_y_diff, enemy_bullet_x_diff)

        # DAHMAGE
        self.damage = 10
        # taking into account the angle, calculate the change in x and y
        enemy_bullet_velocity = 8
        self.change_x = math.cos(enemy_bullet_angle) * enemy_bullet_velocity
        self.change_y = math.sin(enemy_bullet_angle) * enemy_bullet_velocity


    def update(self):
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        # convert rectx and recty to intergers
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

        # when the bullet flies off the screen, kill it
        if self.rect.x < 0 or self.rect.x > size[0] or self.rect.y < 0 or self.rect.y > size[1]:
            self.kill()

class BossBullet(pygame.sprite.Sprite):
    def __init__(self, enemy_bullet_start_x, enemy_bullet_start_y, enemy_bullet_dest_x, enemy_bullet_dest_y):

         # starting position should be somewhere around the ship, got to figure that out
         # destination should be the mouse which I will eventually convert to a croshair
         # Most likely going to stop the bullet at the destination and make it disapear
        # apparently this calls the parent class (Sprite) constructor (source google)
        super().__init__()

        self.image = pygame.Surface([11, 8])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        # starting position of the bullet, going to need some tweaking
        self.rect.x = enemy_bullet_start_x
        self.rect.y = enemy_bullet_start_y
        # pass in floating point numbers which are more accurate for aiming
        self.floating_point_x = enemy_bullet_start_x
        self.floating_point_y = enemy_bullet_start_y
        self.right_boundary = size[0]
        self.left_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = size[1]
        # angles for aiming between the starting point and the destination
        enemy_bullet_x_diff = enemy_bullet_dest_x - enemy_bullet_start_x
        enemy_bullet_y_diff = enemy_bullet_dest_y - enemy_bullet_start_y
        enemy_bullet_angle = math.atan2(enemy_bullet_y_diff, enemy_bullet_x_diff)

        # DAHMAGE
        self.damage = 10
        # taking into account the angle, calculate the change in x and y
        enemy_bullet_velocity = 8
        self.change_x = math.cos(enemy_bullet_angle) * enemy_bullet_velocity
        self.change_y = math.sin(enemy_bullet_angle) * enemy_bullet_velocity
        self.bounce = list()

    def update(self):
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        # convert rectx and recty to intergers
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

        if len(self.bounce) == 0 and (self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary):
            self.change_x *= -1
            self.bounce.append("1")

        elif len(self.bounce) == 1 and (self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary):
            self.change_y *= -1
            self.bounce.append("1")
            #bounce += 1
        # when the bullet flies off the screen, kill it
        elif len(self.bounce) == 1:
            if self.rect.x == 2 or self.rect.x == size[0] -2 or self.rect.y == 2 or self.rect.y == size[1]-2:
                self.kill()

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def button(text, x, y, width, height, text_size, i_color, a_color, action = None ):
    pos_m = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > pos_m[0] > x and y+height > pos_m[1] > y:
        pygame.draw.rect(screen, a_color, (x, y, width, height))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, i_color, (x, y, width, height))

    button_text = pygame.font.Font("LCD_Solid.ttf", text_size)
    text_surf, text_rect = text_objects(text, button_text)
    text_rect.center = ( (x+(width/2)), (y+(height/2)) )
    screen.blit(text_surf, text_rect)


# DETERMINES THE LEVEL THAT YOU ARE ON
level = list()

def Instructions():
    counter = 0
    instructions = True
    health_font = pygame.font.Font("LCD_Solid.ttf", 30)
    level_font = pygame.font.Font("LCD_Solid.ttf", 50)
    while instructions:
        screen.fill(BLACK)
        if len(level) == 0:
            level1_text = level_font.render("Level 1", True, WHITE)
            screen.blit(level1_text, [size[0] / 2 - 100, 300])

            instr_font = pygame.font.Font("LCD_Solid.ttf", 60)
            instr_text = instr_font.render("Defeat All Enemies", True, RED)
            screen.blit(instr_text, [300, size[1] / 2])
        elif len(level) == 1:
            level2_text = level_font.render("Level 2", True, WHITE)
            screen.blit(level2_text, [size[0] / 2 - 100, 300])

            instr_font = pygame.font.Font("LCD_Solid.ttf", 60)
            instr_text = instr_font.render("New Enemy!", True, RED)
            screen.blit(instr_text, [450, size[1] / 2])

        elif len(level) == 2:
            level3_text = level_font.render("Level 3", True, WHITE)
            screen.blit(level3_text, [size[0] / 2 - 100, 300])

            instr_font = pygame.font.Font("LCD_Solid.ttf", 60)
            instr_text = instr_font.render("Defeat All Enemies", True, RED)
            screen.blit(instr_text, [300, size[1] / 2])

        elif len(level) == 3:
            instr_font = pygame.font.Font("LCD_Solid.ttf", 60)
            instr_text = instr_font.render("Boss Battle", True, RED)
            screen.blit(instr_text, [400, size[1] / 2])

        if counter == 30:
            instructions = False

        counter += 1
        pygame.display.update()
        clock.tick(15)
    main_loop()

# screen for level complete
def Youwin(score):
    level.append("1")
    if len(level) == 4:
        level.clear()
    pygame.mouse.set_visible(True)
    winner = True
    while winner:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        global_sprites_list.empty()
        Enemy1_list.empty()
        Enemy2_list.empty()
        all_enemies_list.empty()
        bomb_list.empty()
        Player_list.empty()
        Boss_list.empty()
        bullet_list.empty()
        enemy_bullet_list.empty()
        screen.fill(BLACK)
        # sets up game over screeen
        font = pygame.font.Font("LCD_Solid.ttf", 100)
        go_text = font.render("Level Clear", True, BLUE)
        screen.blit(go_text, (size[0]/2 - 340, size[1]/3 - 100))
        score_font = pygame.font.Font("LCD_Solid.ttf", 50)
        score_text = score_font.render("Score: %d" % score, True, WHITE)
        screen.blit(score_text, (size[0]/2 - 170, size[1]/3))

        button("Next Level", 100, 300, 200, 60, 25, GREY, BLUE, Instructions)
        button("Quit", 950, 300, 200, 60, 25, GREY, RED, quit)

        pygame.display.update()
        clock.tick(15)
def controls():
    control = True

    #clears the enemies in the title screen so that they don't accumulate when checking controls
    float_list.empty()

    while control:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(BLACK)
        c_font = pygame.font.Font("LCD_Solid.ttf", 42)
        c_text = c_font.render("W, A, S, D ------------ Up, Left, Down, Right", True, BLUE)
        c2_text = c_font.render("Use Mouse To Aim", True, BLUE)
        c3_text = c_font.render("Mouse Click ------------ Shoot", True, BLUE)
        c4_text = c_font.render("Space ------------ Bomb (Only When Available)", True, BLUE)
        c5_text = c_font.render("P ------------ Pause Game", True, BLUE)
        screen.blit(c_text,  (50, size[1] / 3 - 70))
        screen.blit(c2_text, (50, size[1] / 3 ))
        screen.blit(c3_text, (50, size[1] / 3 + 70))
        screen.blit(c4_text, (50, size[1] / 3  + 140))
        screen.blit(c5_text, (50, size[1] / 3 + 210 ))

        button("BACK", size[0]/2 - 100, 550, 200, 60, 25, GREY, BLUE, title_loop)

        pygame.display.update()
        clock.tick(15)
def Gameover(score):
    level.clear()
    pygame.mouse.set_visible(True)
    game_over = True

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        global_sprites_list.empty()
        Enemy1_list.empty()
        Enemy2_list.empty()
        all_enemies_list.empty()
        bomb_list.empty()
        Player_list.empty()
        Boss_list.empty()
        bullet_list.empty()
        enemy_bullet_list.empty()
        screen.fill(BLACK)
        # sets up game over screeen
        font = pygame.font.Font("LCD_Solid.ttf", 100)
        go_text = font.render("GAME OVER!", True, RED)
        screen.blit(go_text, (size[0] / 2 - 300, size[1] / 3 - 50))
        score_font = pygame.font.Font("LCD_Solid.ttf", 50)
        score_text = score_font.render("Score: %d" % score, True, WHITE)
        screen.blit(score_text, (size[0]/2 - 170, size[1]/3 + 50))

        button("Play Again", 100, 300, 200, 60, 25, GREY, BLUE, title_loop)
        button("Quit", 950, 300, 200, 60, 25, GREY, RED, quit)

        pygame.display.update()
        clock.tick(15)

# function that display game complete screen (win the game)
def Complete(score):
    level.clear()
    pygame.mouse.set_visible(True)
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        global_sprites_list.empty()
        Enemy1_list.empty()
        Enemy2_list.empty()
        all_enemies_list.empty()
        bomb_list.empty()
        Player_list.empty()
        Boss_list.empty()
        bullet_list.empty()
        enemy_bullet_list.empty()
        screen.fill(BLACK)
        # sets up game over screeen
        font = pygame.font.Font("LCD_Solid.ttf", 100)
        go_text = font.render("YOU WIN!", True, RED)
        screen.blit(go_text, (size[0] / 2 - 250, size[1] / 3 - 50))
        score_font = pygame.font.Font("LCD_Solid.ttf", 50)
        score_text = score_font.render("Score: %d" % score, True, WHITE)
        screen.blit(score_text, (size[0]/2 - 200, 300))

        button("Main Menu", 100, 300, 200, 60, 25, GREY, BLUE, title_loop)
        button("Quit", 950, 300, 200, 60, 25, GREY, RED, quit)

        pygame.display.update()
        clock.tick(15)

# Code for opening a window for the game
size = (1280, 720)
screen = pygame.display.set_mode(size)

# player list in case of multiple players
Player_list = pygame.sprite.Group()
# list of enemy1 sprites
Enemy1_list = pygame.sprite.Group()
# list of enemy2 sprites
Enemy2_list = pygame.sprite.Group()
# Big Bad Boss list
Boss_list = pygame.sprite.Group()
# list of all enemy sprites()
all_enemies_list = pygame.sprite.Group()
# list of player bullet sprites
bullet_list = pygame.sprite.Group()
# bomb list
bomb_list = pygame.sprite.Group()
# enemy bullet list
enemy_bullet_list = pygame.sprite.Group()
# list of every sprite in the game
global_sprites_list = pygame.sprite.Group()
#list of explosion sprite animations
explosion_list = pygame.sprite.Group()
#list for the ships that float around during title screen
float_list = pygame.sprite.Group()

player1_sprite = pygame.image.load("player_ship.png").convert()
enemy1_sprite = pygame.image.load("enemy_ship1.png").convert()
enemy2_sprite = pygame.image.load("enemy_ship2.png").convert()
boss_sprite = pygame.image.load("boss.png").convert()
explosion1 = pygame.image.load("explosion1.png").convert()
explosion2 = pygame.image.load("explosion2.png").convert()
explosion3 = pygame.image.load("explosion3.png").convert()
explosion4 = pygame.image.load("explosion4.png").convert()
explosion5 = pygame.image.load("explosion5.png").convert()
explosion6 = pygame.image.load("explosion6.png").convert()
explosion7 = pygame.image.load("explosion7.png").convert()
crosshair = pygame.image.load("crosshair.png").convert()

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = crosshair
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

player1 = Player_ship()

class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = explosion2
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.counter = 0

    def update(self):
        self.counter += 1
        if 4 < self.counter < 8:
            self.image = explosion2
        elif 8 <= self.counter < 12:
            self.image = explosion3
        elif 12 <= self.counter < 16:
            self.image = explosion4
        elif 16 <= self.counter < 20:
            self.image = explosion5
        elif 20 <= self.counter < 24:
            self.image = explosion6
        elif self.counter >= 24:
            self.image = explosion7




def Genesis(e1, e2, b):
    # //Player Ship

    Player_list.add(player1)
    player1.HP = 150
    global_sprites_list.add(player1)
    #initial player location
    player1.rect.x = 640
    player1.rect.y = 360
    # boundaries
    player1.right_boundary = size[0] + 30
    player1.bottom_boundary = size[1] + 30
    player1.top_boundary = -30
    player1.left_boundary = -30

    # player ship position for enemy aiming
    pos = [player1.rect.x, player1.rect.y]
    # //enemy1
    #creates enemy ships according to e1 input
    for i in range(e1):
        enemy = Enemy1_ships()
        enemy.HP = 30
        # initial enemy location
        enemy.rect.x = random.randrange(size[0]-75)
        enemy.rect.y = random.randrange(size[1]-60)

        enemy.change_x = random.randrange(1, 4)
        enemy.change_y = random.randrange(1, 4)
        enemy.right_boundary = size[0]
        enemy.bottom_boundary = size[1]

        # add to lists
        Enemy1_list.add(enemy)
        all_enemies_list.add(enemy)
        global_sprites_list.add(enemy)
    # enemy1//
    #creates enemy based on e2 input
    for i in range(e2):
        enemy2 = Enemy2_ships()
        enemy2.HP = 50
        # initial enemy location
        enemy2.rect.x = random.randrange(size[0]-75)
        enemy2.rect.y = random.randrange(size[1]-60)

        enemy2.change_x = random.randrange(3, 5)
        enemy2.change_y = random.randrange(3, 5)
        enemy2.right_boundary = size[0]
        enemy2.bottom_boundary = size[1]

        # add to lists
        Enemy2_list.add(enemy2)
        all_enemies_list.add(enemy2)
        global_sprites_list.add(enemy2)

    # creates bosses based on b input, technically I could have alot of bosses on screen at once
    for i in range(b):
        boss = Boss_ships()
        boss.HP = 800

        boss.rect.x = random.randrange(100 , size[0] - 150)
        boss.rect.y = random.randrange(100, size[1] - 200)

        boss.change_x = random.randrange(4)
        boss.change_y = random.randrange(4)
        boss.right_boundary = size[0]
        boss.bottom_boundary = size[1]

        # add to lists
        Boss_list.add(boss)
        all_enemies_list.add(boss)
        global_sprites_list.add(boss)


# Set the name of the window
pygame.display.set_caption("Project X")

# loop until the user clicks exit
#done = False

# used to manage how fast the screen updates
clock = pygame.time.Clock()



#def main():
    #title_loop()

def title_loop():
    Title = True
    for i in range(random.randrange(2,5)):
        enemy = Enemy1_ships()
        enemy.HP = 30
        # initial enemy location
        enemy.rect.x = random.randrange(size[0]-75)
        enemy.rect.y = random.randrange(size[1]-60)

        enemy.change_x = random.randrange(5, 7)
        enemy.change_y = random.randrange(5, 7)
        enemy.right_boundary = size[0]
        enemy.bottom_boundary = size[1]

        float_list.add(enemy)
    x = random.randrange(1, 5)

    while Title:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(BLACK)
        # sets up the title screen
        font = pygame.font.Font("LCD_Solid.ttf", 120)
        title_text = font.render("PROJECT X", True, RED)
        screen.blit(title_text, [size[0]/2 - 300, size[1]/3])

        #// Random text under title
        silly_font = pygame.font.Font("LCD_Solid.ttf", 30)
        silly_text1 = silly_font.render('"10/10" - IGN', True, WHITE)
        silly_text2 = silly_font.render("Nobody Ever Uses The Bombs :|", True, WHITE)
        silly_text3 = silly_font.render("Defeat the Boss!!", True, WHITE)
        silly_text4 = silly_font.render("HAPPY 2017!!", True, WHITE)
        if x == 1:
            screen.blit(silly_text1, [size[0]/3 + 100, size[1]/2])
        elif x == 2:
            screen.blit(silly_text2, [size[0] / 3 - 20, size[1] / 2])
        elif x == 3:
            screen.blit(silly_text3, [size[0] / 3 + 80, size[1] / 2])
        elif x == 4:
            screen.blit(silly_text4, [size[0] / 3 + 120, size[1] / 2])
        #//

        created_font = pygame.font.Font("LCD_Solid.ttf", 20)
        created_text = created_font.render("Created By: Calvin Stewart", True, WHITE)
        screen.blit(created_text, [size[0] - 350, size[1] - 25])

        button("START", 200, 450, 200, 100, 50, GREY, BLUE, Instructions)
        button("CONTROLS", 500, 450, 300, 100, 50, GREY, YELLOW, controls)
        button("QUIT", 900, 450, 200, 100, 50, GREY, RED, quit)

        float_list.update()
        float_list.draw(screen)
        pygame.display.update()
        clock.tick(30)

# list used for pause(appends and empties based on pausing the game)
pause = list()









        # ----------Main Game Loop------------
def main_loop():
    pygame.mouse.set_visible(False)
    Aim = Crosshair()
    global_sprites_list.add(Aim)
    float_list.empty()
    #determines the level
    if len(level) == 0:
        Genesis(4, 0,0)
        player1.score = 0
    elif len(level) == 1:
        Genesis(3, 2, 0)
    elif len(level) == 2:
        Genesis(4, 3, 0)
    elif len(level) == 3:
        Genesis(1,1,1)

# enemy fire is an event that makes all of the enemies fire at the same time
    EnemyFire = pygame.USEREVENT
    pygame.time.set_timer(EnemyFire, random.randrange(1500, 2500))
    # type 2 enemiea fire
    Enemy2Fire = pygame.USEREVENT +1
    pygame.time.set_timer(Enemy2Fire, random.randrange(2500, 3000))
        # event code below here
# you get the drill (   p.s. this is alot of stuff to comment :/  )
    BossFire = pygame.USEREVENT +2
    pygame.time.set_timer(BossFire, random. randrange(2500, 3000))
    Bomb_available = pygame.USEREVENT +3
    bullet_available = pygame.USEREVENT +4
    ship_destroyed1 = pygame.USEREVENT +5
    ship_destroyed2 = pygame.USEREVENT +6
    done = False
    # limits the amounts of bombs and bullets you can fire at a time, to prevent cheap tactics
    ship_explosion1 = False
    ship_explosion2 = False
    deadship_x = 0
    deadship_y = 0
    bombs_away = True
    bullets_away = True
    while not done:
        # all of the events and controls and important stuff
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                quit()
                done = True  # loop is exited
            if event.type == Bomb_available:
                bombs_away = True
            if event.type == bullet_available:
                bullets_away = True
            elif event.type == pygame.KEYDOWN:
                # adjust change if arrow key is pressed
                if event.key == pygame.K_a:
                    player1.change_x = -4.5
                elif event.key == pygame.K_d:
                    player1.change_x = 4.5
                elif event.key == pygame.K_w:
                    player1.change_y = -4.5
                elif event.key == pygame.K_s:
                    player1.change_y = 4
                elif event.key == pygame.K_p:
                    if len(pause) == 0:
                        pause.append("1")
                    elif len(pause) == 1:
                        pause.clear()
            elif event.type == pygame.KEYUP:
                # stops the ship if a key is let up /
                # prevents the ship from continuing into space
                if event.key == pygame.K_a:
                    player1.change_x = 0
                elif event.key == pygame.K_d:
                    player1.change_x = 0
                elif event.key == pygame.K_w:
                    player1.change_y = 0
                elif event.key == pygame.K_s:
                    player1.change_y = 0

                elif event.key == pygame.K_SPACE:
                    if bombs_away == True:
                        #creates a bomb that is fired
                        bomb = Bomb(player1.rect.x + 30, player1.rect.y + 20, mouse_pos[0], mouse_pos[1])
                        # add it to the lists
                        global_sprites_list.add(bomb)
                        bomb_list.add(bomb)
                        bombs_away = False
                        pygame.time.set_timer(Bomb_available, 5000)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bullets_away == True:
                    # fires a bullet when the mouse is clicked
                    bullet = Bullet(player1.rect.x + 30, player1.rect.y + 20, mouse_pos[0], mouse_pos[1])
                    # add it to the lists
                    global_sprites_list.add(bullet)
                    bullet_list.add(bullet)
                    bullets_away = False
                    pygame.time.set_timer(bullet_available, 225)

            elif event.type == EnemyFire: #when the events that I created above happen this code executes
                for enemy in Enemy1_list:
                    enemy_bullet = EnemyBullet(enemy.rect.x, enemy.rect.y, player1.rect.x + 30, player1.rect.y + 20)
                    # add it to the lists
                    global_sprites_list.add(enemy_bullet)
                    enemy_bullet_list.add(enemy_bullet)
            elif event.type == Enemy2Fire:
                for enemy2 in Enemy2_list:
                    enemy2_bullet = EnemyBullet(enemy2.rect.x, enemy2.rect.y, player1.rect.x +30, player1.rect.y +20)
                    # add it to the lists
                    global_sprites_list.add(enemy2_bullet)
                    enemy_bullet_list.add(enemy2_bullet)
            elif event.type == BossFire:
                for boss in Boss_list:
                    boss.spray(9, 50 , 130)
            elif event.type == ship_destroyed1:
                ship_explosion1 = False
            elif event.type == ship_destroyed2:
                ship_explosion2 = False

# kills the player if health == 0 (aka if you suck)
            if player1.HP <= 0:
                player1.kill()
                Gameover(player1.score)
# clears the level if you kill all enemies (aka if you don't suck)
            if len(all_enemies_list) == 0:
                player1.score += player1.HP
                if len(level) == 3:
                    pygame.time.wait(500)
                    Complete(player1.score)
                else:
                    pygame.time.wait(500)
                    Youwin(player1.score)









        # event code above here

        # game logic below here
                # ROTATE ENEMY IMAGES AND RECTS
        for enemy in Enemy1_list:
            # makes the enemy rotate to the playership and retains the original rect center
            old_center = enemy.rect.center
            enemy.image = pygame.transform.rotate(enemy1_sprite, enemy.angle)
            enemy.rect = enemy.image.get_rect()
            enemy.rect.center = old_center
        # should do the same thing as enemy one, but we'll see and make adjustments
        for enemy2 in Enemy2_list:
            # makes the enemy rotate to the playership and retains the original rect center
            old2_center = enemy2.rect.center
            enemy2.image = pygame.transform.rotate(enemy2_sprite, enemy2.angle)
            enemy2.rect = enemy2.image.get_rect()
            enemy2.rect.center = old2_center
        for boss in Boss_list:
            boss_old_center = boss.rect.center
            boss.image = pygame.transform.rotate(boss_sprite, boss.angle)
            boss.rect = boss.image.get_rect()
            boss.rect.center = boss_old_center
            # create a bullet for the enemy to shoot
        # PLAYER ROTATION AND RECT
        player1_old_center = player1.rect.center
        player1.image = pygame.transform.rotate(player1_sprite, player1.angle)
        player1.rect = player1.image.get_rect()
        player1.rect.center = player1_old_center

#// COLLISION DETECTION FOR PROJECTILEs
        for bullet in bullet_list:
            # if the bullet hit an enemy
            enemy_hit = pygame.sprite.spritecollide(bullet, Enemy1_list, False)
            for enemy in enemy_hit:
                bullet_list.remove(bullet)
                global_sprites_list.remove(bullet)
                enemy.HP = enemy.HP - bullet.damage
                if enemy.HP <= 0:
                    player1.score += 100
                    # if it is killed, remove it from the list so that it no longer exists
                    deadship_x = enemy.rect.x
                    deadship_y = enemy.rect.y
                    enemy.kill()
                    Enemy1_list.remove(enemy)
                    all_enemies_list.remove(enemy)
                    if ship_explosion1 == False:
                        explosion_list.empty()
                        ship_explosion1 = True
                        pygame.time.set_timer(ship_destroyed1, 500)


            enemy2_hit = pygame.sprite.spritecollide(bullet, Enemy2_list, False)
            for enemy2 in enemy2_hit:
                bullet_list.remove(bullet)
                global_sprites_list.remove(bullet)
                enemy2.HP = enemy2.HP - bullet.damage
                if enemy2.HP <= 0:
                    player1.score += 200
                    deadship_x = enemy2.rect.x
                    deadship_y = enemy2.rect.y
                    enemy2.kill()
                    Enemy2_list.remove(enemy2)
                    all_enemies_list.remove(enemy2)
                    if ship_explosion2 == False:
                        explosion_list.empty()
                        ship_explosion2 = True
                        pygame.time.set_timer(ship_destroyed2, 500)
            boss_hit = pygame.sprite.spritecollide(bullet, Boss_list, False)
            for boss in boss_hit:
                bullet_list.remove(bullet)
                global_sprites_list.remove(bullet)
                boss.HP = boss.HP - bullet.damage
                if boss.HP <= 0:
                    boss.kill()
                    Boss_list.remove(boss)
                    all_enemies_list.remove(boss)


        for bomb in bomb_list:
            # if the bomb hit an enemy
            bomb_enemy_hit = pygame.sprite.spritecollide(bomb, Enemy1_list, False)
            for enemy in bomb_enemy_hit:
                bomb_list.remove(bomb)
                global_sprites_list.remove(bomb)
                enemy.HP = enemy.HP - bomb.damage
                if enemy.HP <= 0:
                    player1.score += 100
                    deadship_x = enemy.rect.x
                    deadship_y = enemy.rect.y
                    enemy.kill()
                    Enemy1_list.remove(enemy)
                    all_enemies_list.remove(enemy)
                    explosion_list.empty()
                    if ship_explosion1 == False:
                        ship_explosion1 = True
                        pygame.time.set_timer(ship_destroyed1, 500)

            bomb_enemy2_hit = pygame.sprite.spritecollide(bomb, Enemy2_list, False)
            for enemy2 in bomb_enemy2_hit:
                bomb_list.remove(bomb)
                global_sprites_list.remove(bomb)
                enemy2.HP = enemy2.HP - bomb.damage
                if enemy2.HP <= 0:
                    player1.score += 200
                    deadship_x = enemy2.rect.x
                    deadship_y = enemy2.rect.y
                    enemy2.kill()
                    Enemy2_list.remove(enemy2)
                    all_enemies_list.remove(enemy2)
                    if ship_explosion2 == False:
                        explosion_list.empty()
                        ship_explosion2 = True
                        pygame.time.set_timer(ship_destroyed2, 500)
            bomb_boss_hit = pygame.sprite.spritecollide(bomb, Boss_list, False)
            for boss in bomb_boss_hit:
                bomb_list.remove(bomb)
                global_sprites_list.remove(bomb)
                boss.HP = boss.HP - bomb.damage
                if boss.HP <= 0:
                    boss.kill()
                    Boss_list.remove(boss)
                    all_enemies_list.remove(boss)

        for enemy_bullet in enemy_bullet_list:
            # if the bullet hits the player ship
            players_hit = pygame.sprite.spritecollide(enemy_bullet, Player_list, False)
            for player in players_hit:
                enemy_bullet_list.remove(enemy_bullet)
                global_sprites_list.remove(enemy_bullet)
                player1.HP = player1.HP - enemy_bullet.damage

        for enemy2_bullet in enemy_bullet_list:
            # if the bullet hits the player ship
            players_hit = pygame.sprite.spritecollide(enemy2_bullet, Player_list, False)
            for player in players_hit:
                enemy_bullet_list.remove(enemy2_bullet)
                global_sprites_list.remove(enemy2_bullet)
                player1.HP = player1.HP - enemy2_bullet.damage

        # game logic above here

        screen.fill(BLACK)

        if len(pause) == 1:

            float_list.empty()
            font = pygame.font.Font("LCD_Solid.ttf", 100)
            title_text = font.render(" PAUSED", True, RED)
            screen.blit(title_text, [size[0] / 2 - 225, size[1] / 3])
        else:
            global_sprites_list.update()
            global_sprites_list.draw(screen)
            health_font = pygame.font.Font("LCD_Solid.ttf", 30)
            level_font = pygame.font.Font("LCD_Solid.ttf", 50)
            if player1.HP > 100:
                health_text = health_font.render("HP: " + str(player1.HP), True, GREEN)
                screen.blit(health_text, [0, 0])
            elif 100 >= player1.HP > 50:
                health_text = health_font.render("HP: " + str(player1.HP), True, YELLOW)
                screen.blit(health_text, [0, 0])
            else:
                health_text = health_font.render("HP: " + str(player1.HP), True, RED)
                screen.blit(health_text, [0, 0])


            if len(level) == 0:
                level1_text= level_font.render("Level 1", True, WHITE)
                screen.blit(level1_text, [size[0]/2 - 100, 0])
            elif len(level) == 1:
                level2_text= level_font.render("Level 2", True, WHITE)
                screen.blit(level2_text, [size[0]/2 - 100, 0])
            elif len(level) == 2:
                level3_text = level_font.render("Level 3", True, WHITE)
                screen.blit(level3_text, [size[0]/2 - 100, 0])
            elif len(level) == 3:
                boss_text = health_font.render("BOSS: " + str(boss.HP), True, RED)
                screen.blit(boss_text, [size[0] -350 , 0])

            if bombs_away == True:
                bomb_font = pygame.font.Font("LCD_Solid.ttf", 30, )
                bomb_text = bomb_font.render("Bomb available", True, WHITE)
                screen.blit(bomb_text, [0, size[1] - 35])

            #// animates the enemy explosion and scores
            if ship_explosion1 == True:
                explode = Explosion()
                explode.rect.x = deadship_x
                explode.rect.y = deadship_y
                explosion_list.add(explode)


                plus100_font = pygame.font.Font("LCD_Solid.ttf", 20)
                plus100_text = plus100_font.render("+100", True, WHITE)
                screen.blit(plus100_text, [deadship_x, deadship_y - 50])

                explosion_list.update()
                explosion_list.draw(screen)
            # in case I want to change the explosion for enemy2.. also shows +200 instead of +100
            if ship_explosion2 == True:

                explode = Explosion()
                explode.rect.x = deadship_x
                explode.rect.y = deadship_y
                explosion_list.add(explode)


                plus200_font = pygame.font.Font("LCD_Solid.ttf", 20)
                plus200_text = plus200_font.render("+200", True, WHITE)
                screen.blit(plus200_text, [deadship_x, deadship_y - 50])


                explosion_list.update()
                explosion_list.draw(screen)
            #//

            # shows the score on game screen while playing
            score_font = pygame.font.Font("LCD_Solid.ttf", 30)
            score_text = score_font.render("Score: %d" % player1.score, True, WHITE)
            screen.blit(score_text, [size[0] - 200, size[1] - 30] )




        # drawing code above here
        # flips the drawings so that they are displayed
        pygame.display.flip()


        # Limit to 60 frames (because thats what real gamers play at)
        clock.tick(60)

title_loop()
main_loop()
pygame.quit()
quit()
# -----------Title Screen Loop------------




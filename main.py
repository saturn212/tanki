import pygame as pg
import os
import sys
import random

import pygame.event

pg.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
lvl = 'game'

BLaCK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

from load import *


def lvlGAME():
    screen.fill(BLaCK)
    brick_group.draw(screen)
    brick_group.update()
    iron_group.draw(screen)
    iron_group.update()
    water_group.draw(screen)
    water_group.update()
    enemy_group.draw(screen)
    enemy_group.update()
    player_group.draw(screen)
    player_group.update()
    bullet_player_group.draw(screen)
    bullet_player_group.update()
    bullet_enemy_group.draw(screen)
    bullet_enemy_group.update()
    flag_group.draw(screen)
    flag_group.update()
    bush_group.draw(screen)
    bush_group.update()
    pg.display.update()

def startMenu():
    screen.fill((122, 122, 122))
    pg.display.update()

def DrawMaps(nameFile):
    maps = []
    source = "game lvl/" + str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 20):
            maps.append(file.readline().replace("\n", "").split(",")[0:-1])
    print(maps)
    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 40
        for j in range(0, len(maps[0])):
            pos[0] = 40 * j
            if maps[i][j] == '3':
                brick = Brick(brick_image, pos)
                brick_group.add(brick)
            elif maps[i][j] == '4':
                bush = Bush(bush_image, pos)
                bush_group.add(bush)
            elif maps[i][j] == '2':
                iron = Iron(iron_image, pos)
                iron_group.add(iron)
            elif maps[i][j] == '1':
                water = Water(water_image, pos)
                water_group.add(water)
            elif maps[i][j] == '6':
                enemy = Enemy(enemy_image, pos)
                enemy_group.add(enemy)
            elif maps[i][j] == '5':
                flag = Flag(flag_image, pos)
                flag_group.add(flag)

class Brick(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self):
        if pg.sprite.spritecollide(self, player_group, False):
            if player.dir == "top":
                    player.rect.top = self.rect.bottom
            elif player.dir == "left":
                player.rect.left = self.rect.right
            elif player.dir == "bottom":
                player.rect.bottom = self.rect.top
            elif player.dir == "right":
                player.rect.right = self.rect.left


class Bush(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self):
        if pg.sprite.spritecollide(self, player_group, False):
            pass


class Water(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self):

        if pg.sprite.spritecollide(self, player_group, False):
            if player.dir == "top":
                player.rect.top = self.rect.bottom
            elif player.dir == "left":
                player.rect.left = self.rect.right
            elif player.dir == "bottom":
                player.rect.bottom = self.rect.top
            elif player.dir == "right":
                player.rect.right = self.rect.left

class Iron(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self):
        if pg.sprite.spritecollide(self, player_group, False):
            if player.dir == "left":
                player.rect.left = self.rect.right
            if player.dir == "top":
                player.rect.top = self.rect.bottom
            elif player.dir == "left":
                player.rect.left = self.rect.right
            elif player.dir == "bottom":
                player.rect.bottom = self.rect.top
            elif player.dir == "right":
                player.rect.right = self.rect.left

class Flag(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self):
        if pg.sprite.spritecollide(self, player_group, False):
            if player.dir == "left":
                player.rect.left = self.rect.right

class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = "top"
        self.speed = 5
        self.timer_shot = 0
        self.frame = 0
        self.timer_anime = 0
        self.anime = False
    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_w]:
            self.image = pg.transform.rotate(player_image[self.frame], 0)
            self.rect.y -= self.speed
            self.dir = "top"
            self.anime = True
        elif key[pg.K_a]:
            self.image = pg.transform.rotate(player_image[self.frame], 90)
            self.rect.x -= self.speed
            self.dir = "left"
            self.anime = True
        elif key[pg.K_s]:
            self.image = pg.transform.rotate(player_image[self.frame], 180)
            self.rect.y += self.speed
            self.dir = "bottom"
            self.anime = True
        elif key[pg.K_d]:
            self.image = pg.transform.rotate(player_image[self.frame], 270)
            self.rect.x += self.speed
            self.dir = "right"
            self.anime = True
        else:
            self.anime = False
        if key[pg.K_SPACE] and self.timer_shot / FPS > 1:
            bullet = Bulet_player(player_bullet, self.rect.center, self.dir)
            bullet_player_group.add(bullet)
            self.timer_shot = 0
        self.timer_shot += 1
        shoot_sound.play()

        if self.anime:

            self.timer_anime += 1
            if self.timer_anime /FPS > 0.1:
                if self.frame == len(player_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.dir = "top"
        self.timer_moove = 0
        self.timer_shot = 0
    def update(self):

        self.timer_moove += 1
        if self.timer_moove / FPS > 2:
            if random.randint(1, 4) == 1:
                self.dir = "top"
            elif random.randint(1, 4) == 2:
                self.dir = 'bottom'
            elif random.randint(1, 4) == 3:
                self.dir = 'right'
            elif random.randint(1, 4) == 4:
                self.dir = 'left'

            self.timer_moove = 0


        if self.dir == "top":
            self.image = pg.transform.rotate(enemy_image, 0)
            self.rect.y -= self.speed
        elif self.dir == "right":
            self.image = pg.transform.rotate(enemy_image, 270)
            self.rect.x += self.speed
        elif self.dir == "bottom":
            self.image = pg.transform.rotate(enemy_image, 180)
            self.rect.y += self.speed
        elif self.dir == "left":
            self.image = pg.transform.rotate(enemy_image, 90)
            self.rect.x -= self.speed
        if pg.sprite.spritecollide(self, brick_group, False) or pg.sprite.spritecollide(self, water_group, False) or \
                pg.sprite.spritecollide(self, iron_group, False):

            self.timer_moove = 0
            if self.dir == "top":
                self.dir = "bottom"
            elif self.dir == "bottom":
                self.dir = "top"
            elif self.dir == "left":
                self.dir = "right"
            elif self.dir == "right":
                self.dir = "left"


        if  self.timer_shot / FPS > random.randint(1,3):
            bullet = Bulet_enemy(enemy_bullet, self.rect.center, self.dir)
            bullet_enemy_group.add(bullet)
            self.timer_shot = 0
        self.timer_shot += 1
class Bulet_player(pg.sprite.Sprite):
    def __init__(self, image, pos, dir):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dir
        self.speed = 7
        self.frame = 0
        self.timer_anime = 0
        self.anime = False
        self.boom = True
        if self.boom:
            boom_sound.play()
            self.boom = False
    def update(self):
        if self.dir == "top":
            self.rect.y -= self.speed
        elif self.dir == "bottom":
            self.rect.y += self.speed
        elif self.dir == "right":
            self.rect.x += self.speed
        elif self.dir == "left":
            self.rect.x -= self.speed

        if pg.sprite.spritecollide(self,enemy_group,True):
            self.anime = True
            self.speed = 0
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(bullet_image) - 1:
                    self.frame = 0
                    self.rect.center = (-1000, 0)
                    self.kill()
                else:
                    self.frame += 1
                self.timer_anime = 0
            self.image = bullet_image[self.frame]
        pg.sprite.groupcollide(bullet_player_group, brick_group, True, True)
        pg.sprite.groupcollide(bullet_player_group, iron_group, True, False)
        pg.sprite.groupcollide(bullet_player_group, flag_group, True, True)
        pg.sprite.groupcollide(bullet_player_group, enemy_group, True, True)

class Bulet_enemy(pg.sprite.Sprite):
    def __init__(self, image, pos, dir):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dir
        self.speed = 5
    def update(self):
        if self.dir == "top":
            self.rect.y -= self.speed
        elif self.dir == "bottom":
            self.rect.y += self.speed
        elif self.dir == "right":
            self.rect.x += self.speed
        elif self.dir == "left":
            self.rect.x -= self.speed
        pg.sprite.groupcollide(bullet_enemy_group, brick_group, True, True)
        pg.sprite.groupcollide(bullet_enemy_group, iron_group, True, False)
        pg.sprite.groupcollide(bullet_enemy_group, flag_group, True, True)


class Button (pg.sprite.Sprite):
    def __init__(self, image, pos, next_lvl, next):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.nextlvl = next_lvl
        self.text = text
        text.render = font.render(self.text,True, (255, 255, 255))
        screen.blit(text_render,(self.rect.x + 80, self.rect.y + 5))

        click = pg.mouse.get_pos()
        if pg.mouse.get_pressed()[0]:
            if self.rect.left < click[0] < self.rect.right and self.rect.top < click[1] <self.rect.bottom:
                lvl = self.nextlvl


brick_group = pg.sprite.Group()
bush_group = pg.sprite.Group()
iron_group = pg.sprite.Group()
water_group = pg.sprite.Group()
player_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
flag_group = pg.sprite.Group()
bullet_player_group = pg.sprite.Group()
bullet_enemy_group = pg.sprite.Group()
player = Player(player_image[0], (200, 640))
player_group.add(player)
button_group = pg.sprite.Group()
DrawMaps('1.txt')
while True:
    for event in pygame.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    if lvl == 'game':
        lvlGAME()
    elif lvl == 'menu':
        startMenu()
    clock.tick(FPS)
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
    bush_group.draw(screen)
    bush_group.update()
    iron_group.draw(screen)
    iron_group.update()
    water_group.draw(screen)
    water_group.update()
    enemy_group.draw(screen)
    enemy_group.update()
    player_group.draw(screen)
    player_group.update()
    flag_group.draw(screen)
    flag_group.update()
    pg.display.update()

def DrawMaps(nameFile):
    maps = []
    source = "game lvl/" + str(nameFile)
    with open(source, "r") as file:
        for i in range (0, 20):
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
            if player.dir == "left":
                    player.rect.left = self.rect.right

class Bush(pygame.sprite.Sprite):
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

class Water(pygame.sprite.Sprite):
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

    def update (self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.image = pg.transform.rotate(player_image, 90)
            self.rect.x -= self.speed
            self.dir = "left"


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

    def update(self):
        self.timer_moove += 1
        if self.timer_moove / FPS > 2:
            if random.randint(1, 4) == 1:
                self.dir = "top"
            elif random.randint(1,4) == 2:
                self.dir = 'bottom'
        if self.dir == "top":
            self.image = pg.transform.rotate(enemy_image, 0)
            self.rect.y -= self.speed
        elif self.dir == "right":
        elif self.dir ==
        elif self.dir ==




brick_group = pg.sprite.Group()
bush_group = pg.sprite.Group()
iron_group = pg.sprite.Group()
water_group = pg.sprite.Group()
player_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
flag_group = pg.sprite.Group()
player = Player(player_image, (200, 640))
player_group.add(player)
DrawMaps('1.txt')
while True:
    for event in pygame.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    if lvl == 'game':
        lvlGAME()
    clock.tick(FPS)
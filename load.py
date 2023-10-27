import pygame as pg
player_image = [pg.image.load('image/player/player 1.png').convert_alpha(),
pg.image.load('image/player/player 2.png').convert_alpha()]
player_bullet = pg.image.load('image/player/player bullet.png').convert_alpha()
enemy_image = pg.image.load('image/enemy/enemy.png').convert_alpha()
enemy_bullet = pg.image.load('image/enemy/enemy bullet.png').convert_alpha()
brick_image = pg.image.load('image/block/brick block.png').convert_alpha()
iron_image = pg.image.load('image/block/iron block.png').convert_alpha()
bush_image = pg.image.load('image/block/bush block.png').convert_alpha()
water_image = pg.image.load('image/block/water block.png').convert_alpha()
flag_image = pg.image.load('image/block/flag.png').convert_alpha()
bullet_image = [pg.image.load('image/player/boom/1.png').convert_alpha(),
                pg.image.load('image/player/boom/2.png').convert_alpha(),
                pg.image.load('image/player/boom/3.png').convert_alpha(),
                pg.image.load('image/player/boom/4.png').convert_alpha()]
shoot_sound = pg.mixer.Sound('sound/shot.mp3')
boom_sound = pg.mixer.Sound('sound/boom.mp3')
button_image = pg.image.load('image/button/button.png').convert_alpha()
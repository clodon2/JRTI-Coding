# Corey Verkouteren
# 12/9/21 -
# Mr Ball's PM
# PyGame Introduction

# Virus Avoider

import pygame as pg
import random as rd
from pygame.locals import *


class Virus(pg.sprite.Sprite):
    movecount = 0

    def __init__(self):
        super(Virus, self).__init__()
        virusimage = pg.transform.scale(pg.image.load("images/ViruswindowimageCorey.png"), (150, 41))
        self.surf = virusimage
        self.rect = self.surf.get_rect(
            center=(
                    (rd.randint(50, SCREEN_WIDTH - 41)),
                    (rd.randint(5, 10)),
                    ))
        self.speed = rd.randint(2, 10)

    def update(self):
        self.rect.move_ip(0, 5)
        if self.rect.top >= SCREEN_HEIGHT - 39:
            self.kill()


class Player(pg.sprite.Sprite):
    isMoving = False
    speed = 5
    lives = 4
    level = 1

    def setMoving(self, value):
        self.isMoving = value

    def increaseSpeed(self, increase):
        self.speed += increase

    def __init__(self, spriteimage):
        super(Player, self).__init__()
        self.finalsprite = pg.transform.scale(pg.image.load(spriteimage), [50, 64])
        self.surf = self.finalsprite
        self.rect = self.surf.get_rect(
            center=(
                    (SCREEN_WIDTH / 2),
                    (SCREEN_HEIGHT - 89),
                    ))

    def update(self, keypress):
        if keypress[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keypress[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
            # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


pg.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

font = pg.font.SysFont("Arial", 40)
clock = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Virus Avoider")

player = Player("images/grab icon.png")
# <a href="https://www.vecteezy.com/free-vector/mouse-icon">Mouse Icon Vectors by Vecteezy</a>
background = pg.image.load("images/Background Image.jpg")
# https://www.pexels.com/photo/scenic-view-of-snow-capped-mountains-during-night-3408744/
taskbar = pg.image.load("images/taskbar image.png")
# just a screenshot of my taskbar

all_sprites = pg.sprite.Group()
virus_sprites = pg.sprite.Group()
all_sprites.add(player)

ADDVIRUS = pg.USEREVENT + 1
pg.time.set_timer(ADDVIRUS, 3000)

screen.blit(background, (0, 0))
screen.blit(taskbar, (0, 761))

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.setMoving(True)

        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.setMoving(False)
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False

        if event.type == ADDVIRUS:
            newvirus = Virus()
            all_sprites.add(newvirus)
            virus_sprites.add(newvirus)

    pressed_keys = pg.key.get_pressed()
    player.update(pressed_keys)
    virus_sprites.update()

    screen.blit(background, (0, 0))
    screen.blit(taskbar, (0, 761))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pg.display.flip()
    # Ensure program maintains a maximum rate of 30 frames per second
    clock.tick(30)

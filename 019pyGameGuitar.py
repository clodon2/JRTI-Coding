# Corey Verkouteren
# 12/9/21 -
# Mr Ball's PM
# PyGame Introduction

# title
# possible sound: https://freesound.org/people/NoiseCollector/packs/647/?page=3

import pygame as pg
from pygame.locals import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800



class Player(pg.sprite.Sprite):
    isMoving = False
    moveCount = 0
    speed = 5
    level = 1

    def setMoving(self, value):
        self.isMoving = value

    def increaseSpeed(self, increase):
        self.speed += increase

    def __init__(self, spriteimage):
        super(Player, self).__init__()
        self.sprite = spriteimage
        self.surf = pg.image.load(spriteimage).convert_alpha()
        self.rect = self.surf.get_rect(
            center=(
                    (SCREEN_WIDTH / 2),
                    (SCREEN_HEIGHT - 64),
            )
        )

    def getImage(self):
        return self.sprite

    def update(self, keypress):
        playerAnimation = [self.sprite, pg.transform.rotate(self.surf, -45), pg.transform.rotate(self.surf, 45)]
        if self.moveCount > len(playerAnimation) - 1:
            self.moveCount = 0
            self.surf = pg.image.load(playerAnimation[self.moveCount]).convert_alpha()
            self.moveCount += 1
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
Lives = 4
black = (0, 0, 0)

red = 178
green = 190
blue = 181

myFont = pg.font.SysFont("Comicsans", 40)
clock = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Guitar: Welcome ")
player = Player("images/GuitarPlayerSmall.png")

all_sprites = pg.sprite.Group()
all_sprites.add(player)

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

        pressed_keys = pg.key.get_pressed()
        player.update(pressed_keys)

        screen.fill((red, green, blue))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        pg.display.flip()
        # Ensure program maintains a maximum rate of 30 frames per second
        clock.tick(30)

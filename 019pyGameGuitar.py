# Corey Verkouteren
# 12/9/21 -
# Mr Ball's PM
# PyGame Introduction

# title
# possible sound: https://freesound.org/people/NoiseCollector/packs/647/?page=3

import pygame as pg


class Player(pg.sprite.Sprite):
    isMoving = False
    level = 1


player = Player(pg.image.load("Images/GuitarPlayer.png"))

# Corey Verkouteren
# 12/9/21 - 12/22/21
# Mr Ball's PM
# PyGame Introduction

# Virus Avoider
import pygame as pg
import pygame.freetype
import random as rd
from pygame.locals import *


class Virus(pg.sprite.Sprite):
    def __init__(self):
        super(Virus, self).__init__()
        # Virus image I made myself
        virusimage = pg.transform.scale(pg.image.load("images/ViruswindowimageCorey.png"), (170, 47))
        self.surf = virusimage
        self.rect = self.surf.get_rect(
            center=(
                    (rd.randint(80, SCREEN_WIDTH - 80)),
                    (rd.randint(5, 10)),
                    ))
        self.speed = rd.randint(2, 10)

    def update(self):
        # moves virus and kills once it is past the taskbar image
        self.rect.move_ip(0, self.speed)
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

    def loseLife(self):
        self.lives -= 1

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
        # moves according to button press
        if keypress[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keypress[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        # keeps player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def resetPosition(self):
        self.rect.update(SCREEN_WIDTH/2 - 25, SCREEN_HEIGHT - 120, 50, 64)


class MenuButton(pg.sprite.Sprite):
    def __init__(self, button, location):
        super(MenuButton, self).__init__()
        self.surf = pg.image.load(button)
        self.rect = self.surf.get_rect(
            center=(
                    (SCREEN_WIDTH/2),
                    (SCREEN_HEIGHT - location),
                    ))

    def clicked(self):
        return False


class GameOverButton(pg.sprite.Sprite):
    def __init__(self, button, location):
        super(GameOverButton, self).__init__()
        self.surf = pg.image.load(button)
        self.rect = self.surf.get_rect(
            center=(
                    (SCREEN_WIDTH/2),
                    (SCREEN_HEIGHT - location),
                    ))


class Weapon(pg.sprite.Sprite):
    def __init__(self):
        wtype = rd.choice(["antivirus"])
        self.wtype = wtype
        self.speed = 5
        super(Weapon, self).__init__()
        if wtype == "antivirus":
            self.surf = pg.image.load("Images/placeholderweapon.png")
        self.rect = self.surf.get_rect(
            center=(
                player.rect.centerx,
                (player.rect.centery - self.surf.get_height()/2)
            ))

    def update(self):
        if self.wtype == "antivirus":
            self.surf = pg.image.load("Images/placeholderweapon.png")

        if self.rect.bottom <= 0:
            self.kill()
        else:
            self.rect.move_ip(0, -self.speed)


# initialize
pg.init()
pg.font.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# setup for essential things like font, fps, screen, and window title
gamefont = pg.freetype.Font("other/Segoe UI.ttf", 40)
clock = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Virus Avoider")
white = (255, 255, 255)

# Menu Stuff
menubackground = pg.image.load("Images/mountainriver.png")
# Photo by Roberto Nickson from Pexels
startbutton = MenuButton("Images/startbutton.png", 400)

# Game Stuff
player = Player("images/grab icon.png")
# <a href="https://www.vecteezy.com/free-vector/mouse-icon">Mouse Icon Vectors by Vecteezy</a>
background = pg.image.load("images/Background Image.jpg")
# https://www.pexels.com/photo/scenic-view-of-snow-capped-mountains-during-night-3408744/
taskbar = pg.image.load("images/taskbar image.png")
# just a screenshot of my taskbar

# Game Over stuff
retrybutton = GameOverButton("Images/retry.png", 400)
GObackground = pg.image.load("Images/gameoverbackground.png")

# sprite groups
#menu
menu_sprites = pg.sprite.Group()
menu_sprites.add(startbutton)
#game
all_sprites = pg.sprite.Group()
weapon_sprites = pg.sprite.Group()
virus_sprites = pg.sprite.Group()
all_sprites.add(player)
#gameover
gameover_sprites = pg.sprite.Group()
gameover_sprites.add(retrybutton)

# makes an event to add a virus. runs that event every 2 seconds
ADDVIRUS = pg.USEREVENT + 1
pg.time.set_timer(ADDVIRUS, 2000)

running = True
inmenu = True
gameover = False

while running:
    while inmenu:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                inmenu = False
                running = False

            if event.type == MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed(num_buttons=3)[0]:
                    if pg.Rect.collidepoint(startbutton.rect, pg.mouse.get_pos()):
                        inmenu = False

        screen.blit(menubackground, (0, 0))
        for entity in menu_sprites:
            screen.blit(entity.surf, entity.rect)

        pg.display.flip()
        # FPS
        clock.tick(30)


    while gameover:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameover = False
                running = False

            if event.type == MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed(num_buttons=3)[0]:
                    if pg.Rect.collidepoint(retrybutton.rect, pg.mouse.get_pos()):
                        player.lives = 4
                        player.resetPosition()
                        for entity in virus_sprites:
                            entity.kill()
                        gameover = False

        font, fontrect = gamefont.render("Game Over")
        screen.blit(font, (SCREEN_WIDTH - 400, 200))

        for entity in gameover_sprites:
            screen.blit(entity.surf, entity.rect)

        pg.display.flip()
        clock.tick(30)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.setMoving(True)

        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.setMoving(False)
            if event.key == K_UP:
                projectile = Weapon()
                weapon_sprites.add(projectile)
                all_sprites.add(projectile)
            # if user closes the window, the program turns off
            elif event.type == QUIT:
                running = False

        # adds a virus to appropriate sprite groups and instantiates it
        if event.type == ADDVIRUS:
            newvirus = Virus()
            all_sprites.add(newvirus)
            virus_sprites.add(newvirus)

    # detects collisions between player and any viruses and changes lives accordingly
    for entity in virus_sprites:
        if pg.Rect.colliderect(player.rect, entity.rect):
            player.loseLife()
            entity.kill()

    virusrects = []
    for entity in virus_sprites:
        virusrects.append(entity.rect)

    for entity in weapon_sprites:
        if pg.Rect.collidelistall(entity.rect, virusrects):
            hit = pg.Rect.collidelistall(entity.rect, virusrects)
            entity.kill()

    try:
        for i in hit:
            virus_sprites.sprites()[i].kill()
        hit = None
    except:
        pass

    if player.lives <= 0:
        gameover = True

    pressed_keys = pg.key.get_pressed()
    player.update(pressed_keys)
    virus_sprites.update()
    weapon_sprites.update()

    # loads here so that it is behind all surfaces
    screen.blit(background, (0, 0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # renders taskbar and life counter later so that they appear above the virus images
    screen.blit(taskbar, (0, 761))
    # makes a surface of text that displays the player's amount of lives
    lifecounter, lcsize = gamefont.render(str(player.lives), (0, 0, 0))
    screen.blit(lifecounter, (0, 0))

    pg.display.flip()
    # FPS
    clock.tick(30)

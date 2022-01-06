# Corey Verkouteren
# 12/9/21 - 1/6/22
# Mr Ball's PM
# PyGame Introduction

# Virus Avoider
import pygame as pg
import pygame.freetype
import random as rd
from pygame.locals import *


# from JrtiGameSupport, wouldn't recognize as an import for me
def import_folder(path):
    surface_list = []
    for _, __, image_files in pg.walk(path):
        for image in image_files:
            full_path = path + "/" + image
            image_surf = pg.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list


class Virus(pg.sprite.Sprite):
    def __init__(self):
        super(Virus, self).__init__()
        # explosion sprites from Felis Chaus, CC0 licence, https://opengameart.org/content/fire-explosion
        self.explosionani = import_folder("Images/explosion/")
        for s in self.explosionani:
            pg.transform.scale(s, (200, 200))
        # Virus image I made myself
        virusimage = pg.transform.scale(pg.image.load("images/ViruswindowimageCorey.png").convert_alpha(), (170, 47))
        self.surf = virusimage
        self.rect = self.surf.get_rect(
            center=(
                    (rd.randint(80, SCREEN_WIDTH - 80)),
                    (rd.randint(5, 10)),
                    ))
        self.speed = rd.randint(2, 10)
        self.dead = False

    def update(self):
        explosionframecount = 0
        if self.dead:
            if explosionframecount > len(self.explosionani) - 1:
                self.kill()
            else:
                self.surf = self.explosionani[explosionframecount]
                explosionframecount += 1
        # moves virus and kills once it is past the taskbar image
        self.rect.move_ip(0, self.speed)
        if self.rect.top >= SCREEN_HEIGHT - 39:
            self.kill()


class Player(pg.sprite.Sprite):
    isMoving = False
    speed = 5
    lives = 3
    level = 1

    def setMoving(self, value):
        self.isMoving = value

    def increaseSpeed(self, increase):
        self.speed += increase

    def loseLife(self):
        self.lives -= 1

    def __init__(self, spriteimage):
        super(Player, self).__init__()
        self.finalsprite = pg.transform.scale(pg.image.load(spriteimage).convert_alpha(), [50, 64])
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
        self.surf = pg.image.load(button).convert_alpha()
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
        self.surf = pg.image.load(button).convert_alpha()
        self.rect = self.surf.get_rect(
            center=(
                    (SCREEN_WIDTH/2),
                    (SCREEN_HEIGHT - location),
                    ))


class Weapon(pg.sprite.Sprite):
    def __init__(self):
        wtype = rd.choice(["rocket"])
        self.rocketcount = 0
        self.animationpace = 200
        self.wtype = wtype
        self.speed = 0
        super(Weapon, self).__init__()
        if wtype == "rocket":
            self.surf = pg.image.load("Images/rocketweapon/weaponrocket1.png").convert_alpha()
        self.rect = self.surf.get_rect(
            center=(
                player.rect.centerx,
                (player.rect.centery - self.surf.get_height()/2)
            ))

    def update(self):
        # all rocket sprites are my own
        rocketani = ["Images/rocketweapon/weaponrocket1.png", "Images/rocketweapon/weaponrocket2.png",
                     "Images/rocketweapon/weaponrocket3.png", "Images/rocketweapon/weaponrocket4.png",
                     "Images/rocketweapon/weaponrocket5.png"]
        # increases the time between sprite changes
        if self.animationpace <= pg.time.get_ticks():
            if self.wtype == "rocket":
                if self.rocketcount > len(rocketani) - 1:
                    self.rocketcount = 3
                self.surf = pg.image.load(rocketani[self.rocketcount]).convert_alpha()
                self.rocketcount += 1
                # increases speed exponentially, like a real rocket
                self.speed += 1
                self.speed *= 1.3
            self.animationpace = pg.time.get_ticks() + 200
        else:
            pass

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
menubackground = pg.image.load("Images/mountainriver.png").convert_alpha()
# Photo by Roberto Nickson from Pexels
startbutton = MenuButton("Images/startbutton.png", 400)

# Game Stuff
player = Player("images/grab icon.png")
# <a href="https://www.vecteezy.com/free-vector/mouse-icon">Mouse Icon Vectors by Vecteezy</a>
background = pg.image.load("images/Background Image.jpg").convert_alpha()
# https://www.pexels.com/photo/scenic-view-of-snow-capped-mountains-during-night-3408744/
taskbar = pg.image.load("images/taskbar image.png").convert_alpha()
# just a screenshot of my taskbar
weaponcooldown = 0

# Game Over stuff
retrybutton = GameOverButton("Images/retry.png", 500)
GObackground = pg.image.load("Images/gameoverbackground.png").convert_alpha()
BackToMenubutton = GameOverButton("Images/backtomenu.png", 300)

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
gameover_sprites.add(BackToMenubutton)

# makes an event to add a virus. runs that event every 2 seconds
ADDVIRUS = pg.USEREVENT + 1
pg.time.set_timer(ADDVIRUS, 1000)

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
                # if the player left clicks the start button, the player leaves the menu
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
                # detects if the user left clicks a button and responds by resetting the game and returning to a screen
                if pg.mouse.get_pressed(num_buttons=3)[0]:
                    if pg.Rect.collidepoint(retrybutton.rect, pg.mouse.get_pos()):
                        player.lives = 3
                        player.resetPosition()
                        for entity in virus_sprites:
                            entity.kill()
                        gameover = False
                    if pg.Rect.collidepoint(BackToMenubutton.rect, pg.mouse.get_pos()):
                        player.lives = 3
                        player.resetPosition()
                        for entity in virus_sprites:
                            entity.kill()
                            inmenu = True
                        gameover = False

        font, fontrect = gamefont.render("Game Over")
        screen.blit(font, (SCREEN_WIDTH - 400, 100))

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
                # prevents spam firing, only allows a shot every couple seconds
                if weaponcooldown + 2600 <= pg.time.get_ticks():
                    weaponcooldown = pg.time.get_ticks()
                    projectile = Weapon()
                    weapon_sprites.add(projectile)
                    all_sprites.add(projectile)
                else:
                    pass
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

    # detects weapon-virus collisions, and kills both if they collide
    for entity in weapon_sprites:
        if pg.Rect.collidelistall(entity.rect, virusrects):
            hit = pg.Rect.collidelistall(entity.rect, virusrects)
            entity.kill()
    try:
        for i in hit:
            virus_sprites.sprites()[i].dead = True
        hit = None
    except:
        pass

    # sends to gameover screen if the player runs out of lives
    if player.lives <= 0:
        gameover = True

    # all updates
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
    clock.tick(60)

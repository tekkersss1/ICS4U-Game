import os
import pygame as pg


#game options
TITLE = "Esteban Escapes"
WIDTH = 1200
HEIGHT = 608
FPS = 60

# define colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#set up assets
game_folder = os.path.dirname(__file__)
est_folder = os.path.join(game_folder, "EstebanEscapes")
img_folder = os.path.join(est_folder, "testimg")

#camera/bg
speed = 30
bg = pg.image.load(os.path.join(game_folder, 'images/templewip1.png'))#paths to important images
plt = pg.image.load(os.path.join(game_folder, 'images/tiles/platform-1.png'))

#player 'properties- allows for easy changing of important characteristics
PLAYER_GRAVITY = 0.6
JUMP = -7
PLAYER_SPEED = 5
PLAYER_HEALTH = 60

#platfroms and skull list, is what some element of the text file are appended to
PLATFORM_LIST = []
SKULL_LIST = []

#Default sizes for tiles
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE




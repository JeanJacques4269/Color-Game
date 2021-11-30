import platform
from colors import *
import pygame.math
from screeninfo import get_monitors

if platform.system() == "Windows":
    main = get_monitors()[0]  # Get screens size
    for m in get_monitors()[1:]:
        if m.width > main.width:
            main = m
    WIDTH, _ = main.width, main.height
else:
    WIDTH, _ = 1920, 1080
ratio = 3 / 7
WIDTH, HEIGHT = int(WIDTH * ratio), int(WIDTH * ratio * 9 / 16)
BLOCK = WIDTH // 16  # arbitrary mesure unit
FPS = 30

# Sprites

# shit
pygame.font.init()

button_font = pygame.font.Font(None, 25)

background = pygame.image.load("assets/baackground.jpg")
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

img_play_button = pygame.image.load('assets/startbtn.png')
img_play_button = pygame.transform.smoothscale(img_play_button, (BLOCK * 4, BLOCK * 4))

img_restart_button = pygame.image.load("assets/restartbtn.png")
img_restart_button = pygame.transform.smoothscale(img_restart_button, (BLOCK * 1, BLOCK * 1))

img_goback = pygame.image.load("assets/go_back.png")
img_goback = pygame.transform.smoothscale(img_goback, (BLOCK * 1, BLOCK * 1))

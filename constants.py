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
ratio = 2/7
WIDTH, HEIGHT = int(WIDTH * ratio), int(WIDTH * ratio * 9 / 16)
BLOCK = WIDTH // 16  # arbitrary mesure unit
FPS = 30

# Sprites

# shit
pygame.font.init()

button_font = pygame.font.Font(None, 25)

background = pygame.image.load("assets/baackground.jpg")
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

img_button = pygame.image.load('assets/startbtn.png')
img_button = pygame.transform.smoothscale(img_button, (BLOCK * 4, BLOCK * 4))



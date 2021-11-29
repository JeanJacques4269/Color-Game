import pygame.display
from loading_screen import StartPage
from constants import *
from button import Button, ButtonImg
from game_window import GamePage


class Game:
    def __init__(self, win):
        self.win = win
        self.game_is_on = False
        self.welcome_screen_is_on = True

        self.controler = [1, 0]  # loadiing, game

        self.game_window = GamePage(self.controler, self.win)
        self.welcome_window = StartPage(self.controler)

    def loading_screen(self):
        clock = pygame.time.Clock()

        while self.controler[0]:
            clock.tick(FPS)
            self.win.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.controler = [0, 0]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for object in self.welcome_window.clickable_objects:
                            if object.isMouseOn(event.pos):
                                object.on_click()
                                print(self.controler)
            self.welcome_window.update(self.win)
            pygame.display.flip()

            self.game_window.mainloop()

        pygame.quit()

    def change_val(self):
        self.game_is_on = True

import pygame.display
from screens.loading_screen import StartPage
from screens.game_screen import GamePage
from constants import *


class Game:
    def __init__(self, win):
        self.win = win
        self.game_is_on = False
        self.welcome_screen_is_on = True

        self.controler = [True,
                          False]  # keeps track of what window should be active with this format : [loading, game],
        # True means the corresponding window will be shown. if you want more screens,you add more elements to the list.

        self.game_window = GamePage(self.controler, self.win)
        self.loading_window = StartPage(self.controler)

    def run(self):
        clock = pygame.time.Clock()

        while self.controler[0]:
            clock.tick(FPS)  # slows down the loop to get a fixed frame rate
            self.win.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.controler = [0, 0]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for obj in self.loading_window.clickable_objects:
                            if obj.isMouseOn(event.pos):
                                obj.on_click()
            self.loading_window.update(self.win)
            pygame.display.flip()

            self.game_window.mainloop()

        pygame.quit()

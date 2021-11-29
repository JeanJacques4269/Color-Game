import random

from constants import *
from button import Button, ButtonImg
from entry import TextInputManager, TextInputVisualizer


class GamePage:
    def __init__(self, controler, win):
        self.important_var = controler
        self.win = win

        # Above Entry, the word
        self.i = 0  # keep track of the index
        self.font_label = pygame.font.SysFont("Consolas", 70)
        self.txt = ""
        self.txt_color = None
        self.next_word()

        # Entry
        manager = TextInputManager(validator=lambda input: len(input) <= 15)
        self.font_entry = pygame.font.SysFont("Consolas", 55)
        self.textinput_custom = TextInputVisualizer(manager=manager, font_object=self.font_entry)

        # Score
        self.score = 0
        self.font_score = pygame.font.SysFont("Consolas", 25)
        # other

    def mainloop(self):
        clock = pygame.time.Clock()
        self.textinput_custom.cursor_width = 0
        self.textinput_custom.font_color = BLACK

        while self.important_var[1]:
            clock.tick(FPS)
            self.win.fill(WHITE)

            events = pygame.event.get()
            self.textinput_custom.update(events)
            for event in events:
                if event.type == pygame.QUIT:
                    self.important_var = [0, 0]
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.submit(self.textinput_custom.value)

            self.update()
            pygame.display.flip()

    def submit(self, val):
        if val.upper() == reversed_dico[self.txt_color]:
            self.score += 100

        else:
            print(reversed_dico[self.txt_color])
            pass
        self.textinput_custom.value = ""
        self.next_word()

    def next_word(self):
        self.i += 1
        self.txt = rand_elem(list(dico.keys()))
        self.txt_color = rand_elem(list(dico.values()))

    def quit(self):
        self.important_var = [1, 0]

    def restart(self):
        self.__init__(self.important_var, self.win)

    def update(self):
        # entry
        self.win.blit(self.textinput_custom.surface,
                      self.textinput_custom.surface.get_rect(center=(WIDTH // 2 + 10, HEIGHT // 2)))
        # label
        render = self.font_label.render(self.txt, True, self.txt_color)
        self.win.blit(render, render.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 70)))  # needs to make relative

        # score
        render = self.font_score.render(f"Score : {self.score}", True, BLACK)
        self.win.blit(render, render.get_rect(topright=(WIDTH - 5, 5)))


def rand_elem(liste):
    return liste[random.randint(0, len(liste) - 1)]

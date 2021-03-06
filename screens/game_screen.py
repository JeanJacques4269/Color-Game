import random
from constants import *
from components.button import ButtonImg
from pygame_textinput import TextInputManager, TextInputVisualizer


class GamePage:
    def __init__(self, controler, win):
        self.important_var = controler
        self.win = win

        # The word you have to write the color of
        self.font_label = pygame.font.SysFont("Consolas", 70)
        self.txt = ""
        self.txt_color = None
        self.next_word()  # genereate the first word

        # Entry
        manager = TextInputManager(validator=lambda val: len(val) <= 15)
        self.font_entry = pygame.font.SysFont("Consolas", 55)
        self.textinput_custom = TextInputVisualizer(manager=manager, font_object=self.font_entry)
        self.textinput_custom.cursor_width = 0
        self.textinput_custom.font_color = BLACK

        # Score
        self.score = 0
        self.font_score = pygame.font.SysFont("Consolas", 25)

        # Timer
        self.time_remaining = default_time
        self.font_timer = pygame.font.SysFont("Consolas", 30)

        # RestartButton
        self.btn_restart = ButtonImg(img_restart_button, 0, 0, self.restart)
        self.btn_restart.rect = self.btn_restart.surface.get_rect(topright=(WIDTH - 10, 10))

        # Goback button
        self.btn_goback = ButtonImg(img_goback, 0, 0, self.quit)
        self.btn_goback.rect = self.btn_goback.surface.get_rect(topleft=(10, 10))

        self.clickable_objects = [self.btn_restart, self.btn_goback]

    def mainloop(self):
        clock = pygame.time.Clock()

        while self.important_var[1]:
            dt = clock.tick(FPS)
            self.time_remaining -= dt / 1000
            self.win.fill(WHITE)

            events = pygame.event.get()
            self.textinput_custom.update(events)
            for event in events:
                if event.type == pygame.QUIT:
                    self.important_var = [0, 0]
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.time_remaining > 0:
                            self.submit(self.textinput_custom.value)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for obj in self.clickable_objects:
                            if obj.isMouseOn(event.pos):
                                obj.on_click()
            self.update()
            pygame.display.flip()

    def submit(self, val):
        if len(val) < 3:
            return
            # check wether the world written corresponds to the color of the word
        if val.upper() == color_dico_reversed[self.txt_color]:
            self.score += 100

        else:
            print(color_dico_reversed[self.txt_color])
            pass
        self.textinput_custom.value = ""
        self.next_word()

    def next_word(self):
        self.txt = rand_elem(list(color_dico.keys()))
        self.txt_color = rand_elem(list(color_dico.values()))

    def update(self):
        # entry
        self.win.blit(self.textinput_custom.surface,
                      self.textinput_custom.surface.get_rect(center=(WIDTH // 2 + 10, HEIGHT // 2)))
        # label
        render = self.font_label.render(self.txt, True, self.txt_color)
        self.win.blit(render, render.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 70)))  # needs to make relative

        # score
        render = self.font_score.render(f"Score : {self.score}", True, BLACK)
        self.win.blit(render, render.get_rect(bottomleft=(0 + 10, HEIGHT - 10)))

        # timer
        if self.time_remaining < 0:
            self.time_remaining = 0
        render = self.font_timer.render(f"{self.time_remaining:.1f}s", True, RED)
        self.win.blit(render, render.get_rect(bottomright=(WIDTH - 10, HEIGHT - 10)))

        # btn restart
        self.win.blit(self.btn_restart.surface, self.btn_restart.rect)

        # btn go back
        self.win.blit(self.btn_goback.surface, self.btn_goback.rect)

    def restart(self):
        self.__init__(self.important_var, self.win)

    def quit(self):
        self.score = 0
        self.time_remaining = default_time
        self.important_var[0], self.important_var[1] = 1, 0


def rand_elem(liste):
    """
    Returns a random element in a list
    """
    return liste[random.randint(0, len(liste) - 1)]

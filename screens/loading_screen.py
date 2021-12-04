from constants import *
from components.button import ButtonImg


class StartPage:
    def __init__(self, controler):
        self.important_var = controler

        # bg
        self.background = background

        # title
        self.title_font = pygame.font.Font(None, 60)
        self.title_text = self.title_font.render('True Color', False, WHITE)

        # rules
        self.instruction_font = pygame.font.Font(None, 40)
        self.instrution_text = self.instruction_font.render('Type the font color not the word!', False, WHITE)

        # button start
        self.btn_start = ButtonImg(img_play_button, WIDTH // 2, 2 * HEIGHT // 3, self.quit)

        self.clickable_objects = [self.btn_start]

    def update(self, win):
        # bg
        win.blit(background, (0, 0))

        # title
        win.blit(self.title_text, self.title_text.get_rect(center=(WIDTH // 2, HEIGHT // 6)))

        # rules
        win.blit(self.instrution_text, self.instrution_text.get_rect(center=(WIDTH // 2, HEIGHT // 3)))

        # button start
        win.blit(self.btn_start.surface, self.btn_start.rect)

    def quit(self):
        self.important_var[0], self.important_var[1] = 0, 1  # we set the controller var to [False, True]
        # which means that we want to have the loading page

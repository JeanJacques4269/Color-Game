def rgb(a, b, c):
    return a, b, c


BLACK = 0, 0, 0
WHITE = 255, 255, 255
PINK = (145, 86, 114)
LIGHTBEIGE = 181, 136, 99
PURPLE = (155, 31, 233)
BROWN = (255, 1, 0)
GREEN = (0, 255, 1)
ORANGE = (250, 154, 0)
RED = 250, 41, 76
GRAY = (185, 224, 226)
BLUE = (0, 0, 255)
YELLOW = (253, 253, 4)

dico = {"PINK": (145, 86, 114),
        "PURPLE": (155, 31, 233),
        "BROWN": (255, 1, 0),
        "GREEN": (0, 255, 1),
        "ORANGE": (250, 154, 0),
        "GRAY": (185, 224, 226),
        "BLUE": (0, 0, 255),
        "YELLOW": (253, 253, 4),
        "BLACK": (0, 0, 0),
        "RED": (250, 41, 76),
        }
reversed_dico = dict(zip(dico.values(), dico.keys()))  # simple reversed dico

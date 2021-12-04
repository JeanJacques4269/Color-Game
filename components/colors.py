def rgb(a, b, c):
    return a, b, c


BLACK = 0, 0, 0
WHITE = 255, 255, 255
PINK = (223, 0, 125)
LIGHTBEIGE = 181, 136, 99
PURPLE = (155, 31, 233)
BROWN = (89, 62, 49)
GREEN = (0, 255, 1)
ORANGE = (250, 154, 0)
RED = 250, 41, 76
GRAY = (185, 224, 226)
BLUE = (0, 0, 255)
YELLOW = (253, 253, 4)

color_dico = dict()
with open("input.txt", 'r') as file:
    for line in file.readlines():
        color_dico[line.rstrip()] = globals()[
            line.rstrip()]  # globals is used to find a variable by its string representation

color_dico_reversed = dict(
    zip(color_dico.values(), color_dico.keys()))  # reversed color_dico which means that we inverted keys and values

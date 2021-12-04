# Brain challenge

This project is a game which has 2 different screens :

* one is called the `loading_screen` or `welcome_screen`, it is here that the rules are explained
* the other is the `game_screen` where you can find all of the game logic.

These pages are linked in the `run` fonction of the class/file `Game`/`game`

Here are the main features of this game :

## File handling

We use a text file to chose what colors we vant to add to the game.

input.txt :

```PINK
PURPLE
BROWN
GREEN
ORANGE
GRAY
BLUE
YELLOW
BLACK
RED
```

We read this file using this simple block

```python
color_dico = dict()
with open("input.txt", 'r') as file:
    for line in file.readlines():
        color_string = line.rstrip()  # we remove spaces and newlines
        color_dico[color_string] = globals()[color_string]  # we add the color to our color dicitonary
```

## Data structure

One of the most important data structure used in this project is the one of `color_dico`. I chose to use the builtin
type dictionnary in python because it makes in really easy and smooth to use in the game class !

The format of the dictionnary is `(key,value) = (str, (int,int,int))` `str` is the color name, and `(int,int,int)` is
the rgb encoding of the color.

Here is the code to verify if the color entered by the player is the color of the word shown on the screen:

```python
if val.upper() == color_dico_reversed[self.txt_color]:
    self.score += 100
```

* txt.color is the rgb encoding of the word shown on the screen

* val is the text that the player just wrote and submitted.

We can get the name of the color of the word by reversing our dictionnary which mean that we input the rgb value and it
gives us the corresponding color !

## Looping

in the run fonction of `game.py` we have an example of a game loop :

```python
while self.controler[0]:
    clock.tick(FPS)  # slows down the loop to get a fixed frame rate
    self.win.fill(BLACK)
    for event in pygame.event.get():
        pass
        # checks for user input
    self.loading_window.update(self.win)
    pygame.display.flip()
```

This is the basic implementation of a window in any kind of langage. Indeed, you have a pseudo infinite while loop and
every turn you:

* Check for user interaction and use specific fonction if he clicks somwhere for exampe
* Update the screen and all of its components
* Refresh the display

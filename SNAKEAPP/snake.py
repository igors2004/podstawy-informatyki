from tkinter import *
import random

GAME_WIDTH = 700 # STALE
GAME_HEIGHT = 700
SPEED = 60
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#3246a8" #NIEBIESKI
FOOD_COLOR = "#a89e32" #ZOLTY
BACKGROUND_COLOR= "#231036" #FIOLETOWY



class Snake:
    pass
class Food:
    pass
def nextturn():
    pass
def change_direction(new_direction):
    pass
def check_collision():
    pass
def game_over():
    pass



window=Tk()
window.title("SNAKE GAME")


score = 0
direction = 'down'
label = Label(window, text="Score: {}".format(score, font=('consolas', 100)))
label.pack()



window.mainloop()
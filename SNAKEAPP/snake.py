from tkinter import *
import random

GAME_WIDTH = 700  # STALE
GAME_HEIGHT = 700
SPEED = 60
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#3246a8"  # NIEBIESKI
FOOD_COLOR = "#a89e32"  # ZOLTY
BACKGROUND_COLOR = "#231036"  # FIOLETOWY



class Snake:
    pass
class Food:
    def __init__(self):

        x = random.randrange(0, (GAME_WIDTH / SPACE_SIZE))
        y = random.randint(0, GAME_HEIGHT)

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")


def next_turn():
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
label = Label(window, text="Score: {}".format(score), font=('consolas', 100))
label.pack()
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()




window.mainloop()
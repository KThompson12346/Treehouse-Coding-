from tkinter import *
from random import *

def random_colour_code():
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    colour_code = '#'
    for i in range(0,6):
        colour_code = colour_code + choice(hex_chars)
    return colour_code

window = Tk()
canvas = Canvas(window, width=500, height=500, bg='white')
canvas.grid(row=0, column=0)
# for i in range(0, 500):
while True:
    x1 = randint(0, 500)
    y1 = randint(0, 500)
    x2 = randint(0, 500)
    y2 = randint(0, 500)
    random_width = randint(1, 25)
    canvas.create_line(x1, y1, x2, y2, fill=random_colour_code(), width=random_width)
    canvas.update()
window.mainloop()

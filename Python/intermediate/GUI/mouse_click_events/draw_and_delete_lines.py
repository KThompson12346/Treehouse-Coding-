from tkinter import *
from random import *

def random_line(event):
    x1 = randint(0, 500)
    y1 = randint(0, 500)
    x2 = randint(0, 500)
    y2 = randint(0, 500)
    canvas.create_line(x1, y1, x2, y2, fill=f'#{randint(0, 0xffffff) :06x}', width=20)

def delete_lines(event):
    canvas.delete('all')


window = Tk()
canvas = Canvas(window, width=500, height=500, background='white')
canvas.bind('<Button-1>', random_line)
canvas.bind('<Button-3>', delete_lines)
canvas.grid(row=0, column=0)
window.mainloop()

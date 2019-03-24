from tkinter import *
from random import *

def random_line():
    x1 = randint(0, 500)
    y1 = randint(0, 500)
    x2 = randint(0, 500)
    y2 = randint(0, 500)
    canvas.create_line(x1, y1, x2, y2, fill=f'#{randint(0, 0xffffff) :06x}', width=20)

def delete_lines():
    canvas.delete('all')


window = Tk()
canvas = Canvas(window, width=500, height=500, background='white')
draw_button = Button(window, text='Click for a random coloured line', command=random_line)
delete_button = Button(window, text='Click to clear coloured lines', command=delete_lines)
canvas.grid(row=0, column=0)
draw_button.grid(row=1, column=0)
delete_button.grid(row=2, column=0)
window.mainloop()

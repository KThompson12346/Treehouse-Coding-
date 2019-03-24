from tkinter import *

def draw_line(event):
    global click_number # global variables that are used throughout the life of the programme, used as a counter for the clicks of the mouse
    global x1, y1 # used to hold the starting point of every line, is set to global variable so that the variables are still set even when the function has finished executing
    if click_number == 0:
        x1 = event.x
        y1 = event.y
        click_number = 1 # When this code is executed click_number is set to 1 to show that the first point of the line has been set
    else: # when this part of code is executed click number is 1, meaning that the second point of the line is to be set which will then invoke the create_line() method to create the line between the points
        x2 = event.x
        y2 = event.y
        canvas.create_line(x1, y1, x2, y2, fill='black', width=10)
        click_number = 0 # click_number is set back to 0 to initiate the start of the line

window = Tk()
canvas = Canvas(window, width=500, height=500, background='white')
canvas.grid(row=0, column=0)
canvas.bind('<Button-1>', draw_line)
click_number = 0
window.mainloop()

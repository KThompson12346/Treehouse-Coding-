# The Canvas Widget
# Allows for the drawing of shapes upon itself
# Useful for drawing graphs
# Allows for the plotting of values
# Can be used to implement custom widgets
from tkinter import *

window = Tk()
canvas_one = Canvas(window, width=200, height=200, background='white') # creates the canvas and sets the height and width
canvas_two = Canvas(window, width=200, height=200, background='green')
canvas_one.grid(row=0, column=0) # positions the canvas in window
canvas_two.grid(row=0, column=1)
window.mainloop()

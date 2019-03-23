# The Canvas Widget
# Allows for the drawing of shapes upon itself
# Useful for drawing graphs
# Allows for the plotting of values
# Can be used to implement custom widgets
from tkinter import *

window = Tk()
canvas_one = Canvas(window, width=400, height=400, background='yellow') # creates the canvas and sets the height and width
canvas_one.grid(row=0, column=0) # positions the canvas in window
canvas_one.create_line(0,0,400,400, fill='green', width=10) # creates a line using the points (0,0) and (400,400) using the .create_line()
canvas_one.create_line(400,0,0,400, fill='green', width=10)
canvas_one.create_line(200,0,200,400, fill='green', width=10)
canvas_one.create_line(0,200,400,200, fill='green', width=10) # width changes the thickness of the lines
window.mainloop()

from tkinter import *

window = Tk()
canvas = Canvas(window, width=700, height=500, background='white')
canvas.grid(row=0, column=0)
canvas.create_line(100, 100, 300, 100, 200, 300, 100, 100, fill='green', width=5) # triangle
canvas.create_line(400, 100, 600, 100, 650, 300, 350, 300, 400, 100, fill='yellow', width=5) # trapezium
canvas.create_line(100, 400, 650, 400, fill='red', width=5, arrow='both') # line with an arrow head at both ends
canvas.create_line(100, 450, 650, 450, fill='brown', width=5, arrow='last', arrowshape=(70, 40, 24)) # line with an arrowhead at the endpoint and with a custom shape using arrowshape tuple
window.mainloop()

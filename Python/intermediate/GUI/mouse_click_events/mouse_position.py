from tkinter import *

def display_coordinates(event):
    label['text'] = 'X = {}, Y = {}'.format(event.x, event.y)

window = Tk()
canvas = Canvas(window, width=500, height=500, background='white')
label = Label(window, border='4', relief='ridge', font='Broadway 16 bold', background='white', foreground='black')
canvas.bind('<Button-1>', display_coordinates) # .bind() binds an event to an event handler, the event '<Button-1>' has the event handler display_coordinates that shows where the mouse is being clicked on the canvas
canvas.grid(row=0, column=0)
label.grid(row=1, column=0)
window.mainloop()

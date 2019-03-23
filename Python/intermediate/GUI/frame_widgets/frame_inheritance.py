from tkinter import *

class RedFrame(Frame):
    def __init__(self, window):
        super().__init__() # sets initialisation for superclass, ensures inheritance takes place
        self['height'] = 150
        self['width'] = 150
        self['relief'] = RAISED
        self['bd'] = 8
        self['bg'] = 'red'

my_window = Tk()

frame_a = RedFrame(my_window)
frame_a.grid(row=0, column=0)

my_window.mainloop()

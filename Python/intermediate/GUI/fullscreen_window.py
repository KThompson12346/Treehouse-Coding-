from tkinter import *

window = Tk()

window_width = window.winfo_screenwidth() # gets the width of the monitor
window_height = window.winfo_screenheight() # gets the height of the monitor
window.geometry("%dx%d+0+0" % (window_width, window_height)) # %d is a string formatting operator that acts as a placeholder for a number within a string
# window.geometry("{}x{}+0+0".format(window_width, window_height)) <----- is the same as line 7
# window.geometry(f"{window_width}x{window_height}+0+0") <----- is the same as lines 7 and 8, this is known as the f string notation
window.mainloop()

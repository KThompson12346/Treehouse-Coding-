# A frame is rectangular region of the screen it is mainly used as a geometry master for other widgets i.e. it is a container widget
# Frame widgets are used to group other widgets into complex layouts
# Padding between widgets can be provided by a frame widget
# A frame class can also act as a base class when implementing compound widgets
# A container for other widgets
from tkinter import *

window = Tk()
window.title('Submit Form')
frame_name = Frame(window)
frame_address = Frame(window)

# Creation of all widgets labels, entries and buttons, lines 14-29
label_first = Label(frame_name, text='First Name')
label_middle = Label(frame_name, text='Middle Name')
label_last = Label(frame_name, text='Last Name')
label_first_line = Label(frame_address, text='First Line')
label_town = Label(frame_address, text='Town')
label_county = Label(frame_address, text='County')

entry_first = Entry(frame_name)
entry_middle = Entry(frame_name)
entry_last = Entry(frame_name)
entry_first_line = Entry(frame_address)
entry_town = Entry(frame_address)
entry_county = Entry(frame_address)

submit_name = Button(frame_name, text='     Submit     ')
submit_address = Button(frame_address, text='     Submit     ')

# lines 32-38 positioning of the widgets within the frame_name frame
label_first.grid(row=0, column=0)
label_middle.grid(row=1, column=0)
label_last.grid(row=2, column=0)
entry_first.grid(row=0, column=1)
entry_middle.grid(row=1, column=1)
entry_last.grid(row=2, column=1)
submit_name.grid(row=3, columnspan=2)
# lines 40-46 positioning of the widgets within the frame_address frame
label_first_line.grid(row=0, column=0)
label_town.grid(row=1, column=0)
label_county.grid(row=2, column=0)
entry_first_line.grid(row=0, column=1)
entry_town.grid(row=1, column=1)
entry_county.grid(row=2, column=1)
submit_address.grid(row=3, columnspan=2)

# lines 49 & 50 is the positioning of the frames within the windows
frame_name.grid(row=0, column=0)
frame_address.grid(row=0, column=1)

window.mainloop()

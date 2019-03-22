from tkinter import *

window = Tk()
# Tab order is the order of where the tab goes which is the order in which the objects are created
entry_a = Entry(window, background='red')
entry_b = Entry(window, background='yellow')
entry_c = Entry(window, background='white')

label_a = Label(window, text='First Name')
label_b = Label(window, text='Middle Name')
label_c = Label(window, text='Last Name')

label_a.grid(row=0, column=0)
label_b.grid(row=1, column=0)
label_c.grid(row=2, column=0)
entry_a.grid(row=0, column=1)
entry_b.grid(row=1, column=1)
entry_c.grid(row=2, column=1)

window.mainloop()

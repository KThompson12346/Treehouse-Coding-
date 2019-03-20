from tkinter import *

def add_label(): # method to add a label onto the window
    label_one = Label(window,
                    text='Hello World')
    label_one.pack()

window = Tk()
window.geometry("400x200")

# first_button = Button(window,
#                   text='Click Me',
#                   command=add_label) # button click event calls the method add_label
# first_button.pack()

label_1 = Label(window, width="20", height="3", background="red")
label_2 = Label(window, width="20", height="3", background="green")
label_3 = Label(window, width="20", height="3", background="blue")

button_1 = Button(window, text="Click Me 1")
button_2 = Button(window, text="Click Me 2")
button_3 = Button(window, text="Click Me 3")

# geometry grid manager for placing elements into a window, this is a 3x2 window
label_1.grid(row=0, column=0)
label_2.grid(row=1, column=1)
label_3.grid(row=0, column=2)

button_1.grid(row=1, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=1, column=2)

window.mainloop()

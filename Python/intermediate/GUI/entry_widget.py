from tkinter import *

def say_hello(): # function to handle button click event
    name_of_user = entry_1.get() # .get() gets whatever is in the entry widget
    string_to_display = 'Hello ' + name_of_user # puts together the user's text and string to be shown on the window
    label_2 = Label(window) # creates the label in the window
    label_2['text'] = string_to_display # puts the string in the text attribute for the label
    label_2.grid(row=1, column=1) # positions the label within the window

window = Tk()

label_1 = Label(window, text='Please enter your name:')
entry_1 = Entry(window) # creation of the entry widget
button_1 = Button(window, text='Click to enter your name', command=say_hello)

label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)
button_1.grid(row=1, column=0)

window.mainloop()

from tkinter import *

window = Tk()

def button_one():
    label['background'] = 'red'

def button_two():
    label['background'] = 'green'

def button_three():
    label['background'] = 'blue'


label = Label(window,
              width="20",
              height="3",
              text='Label One')

button_1 = Button(window, text='Red', width=10, height=3, command=button_one)
button_2 = Button(window, text='Green', width=10, height=3, command=button_two)
button_3 = Button(window, text='Blue', width=10, height=3, command=button_three)

label.grid(row=0, column=1)
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)



window.mainloop()

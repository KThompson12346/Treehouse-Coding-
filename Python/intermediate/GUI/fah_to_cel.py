from tkinter import *

window = Tk()

def convert():
    F = float(fah_entry_widget.get()) # gets the input from the entry widget and converts it to a float
    C = (F - 32) * 5 / 9 # the formula for converting the Fahrenheit into Celsius
    display_cel_label['text'] = str(C) # displays the fahrenheit in the label widget
# Line 10-14 is the creation of widget objects
fah_label = Label(window, width=20, height=3, text='Enter Fahrenheit Temp:')
fah_entry_widget = Entry(window, width=20)
cel_label_temp = Label(window, width=20, height=3, text='Celsius Temperature:')
display_cel_label = Label(window, width=20, height=3)
convert_button = Button(window, width=20, height=3, text='Convert', command=convert)
# Line 16-20 is the positioning of the widgets
fah_label.grid(row=0, column=0)
fah_entry_widget.grid(row=0, column=1)
cel_label_temp.grid(row=1, column=0)
display_cel_label.grid(row=1, column=1)
convert_button.grid(row=2, column=0)

fah_entry_widget.focus()
window.mainloop()

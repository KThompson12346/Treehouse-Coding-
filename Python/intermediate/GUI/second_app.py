from tkinter import *

my_window = Tk()

my_window.title('My window One')
my_window.configure(background='#857658')
my_window.geometry("400x200")
label_one = Label(my_window,
                  border=8,
                  relief='groove',
                  font='Verdana 22 bold',
                  background='red',
                  foreground='white',
                  text='Hello World',
                  padx=10,
                  pady=10)

label_one.pack()
label_one['text'] = 'Hello World Now!' # change text key after the label has been displayed
# print(label_one.keys()) # keys() shows all the avaiable keys that can hold values

window_two = Tk()
window_two.title('Window two')
window_two.geometry("400x200+100+400")
str_var = StringVar() # creates a string variable object that can be attached (line 34) and set using .set() (line 35)
label_two = Label(window_two,
                  border=10,
                  relief='solid',
                  font='Helvetica 22 italic',
                  foreground='green',
                  padx=10,
                  pady=10,
                  text='Hello World Label Two',
                  textvariable=str_var) # attaches the string variable to the label object
label_two.pack()
str_var.set("This is a string variable object") # sets the string variable objects value

button_1 = Button(window_two,
                  text='Click Me') # Button object
button_1.pack() # displays the button

my_window.mainloop()

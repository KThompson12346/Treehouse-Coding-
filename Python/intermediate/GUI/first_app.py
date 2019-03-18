from tkinter import * # Is an intermediatry between python and tcl/tk


# Creates an instance of the tkinter class
# Sets the title of the tk instance window
window = Tk()
window.title("My Window")
second_window = Tk()
second_window.title("Second Window")

# configure sets the different attributes of the tkinter window
window.configure(background='#b5b5b5') # Changes the colour of the window background, can use bg or background takes hexidecimal or name of colour
second_window.configure(background='#f9eab4')
window.geometry('300x300+300+100') # Takes width, height, x and y coordinates all as one string, i.e. 'widthxheight+xaxis+yaxis'

# Used to set the size of the tk instance Window
second_window_width = 500
second_window_height = 250
# Locate the height and width of the screen lines 20-25
screen_width = second_window.winfo_screenwidth()
screen_height = second_window.winfo_screenheight()
# finds the x and y coordinates for the top left of the window (for the tkinter window to be centered)
x_coordinate = (screen_width/2) - (second_window_width/2)
y_coordinate = (screen_height/2) - (second_window_height/2)
second_window.geometry("%dx%d+%d+%d" % (second_window_width, second_window_height, x_coordinate, y_coordinate)) # converts the formatted string (%d) into the values on other side of % (second_window_width, second_window_height, x_coordinate, y_coordinate)

# Labels in a window,
window_1_label = Label(window, text = 'Window 1 label', font='Broadway 18 bold italic', width=30) # This method builds the label object, and changes the font type, font size, bold and italic. The width is in text units, so the width is based on how many text characters can fit in the width (box)
window_1_label_2 = Label(window, text='Line one text\nLine two text\nLine three text', borderwidth=2, relief='solid') # Label with multiple lines of text, borderwidth of 3 and a solid border
window_2_label = Label(second_window, text = 'Window 2 label', background='black',foreground='white', font='Broadway') # same as above line but setting the background colour and font colour
window_2_label_2 = Label(second_window, text = 'window 2 label 2')
window_1_label.pack() # this method will display the labels
window_1_label_2.pack()
window_2_label.pack()

window.mainloop() # is the loop for the program that is waiting for user input (fetch/execute cycle)

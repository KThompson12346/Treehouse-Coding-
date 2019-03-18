import tkinter # Is an intermediatry between python and tcl/tk


# Creates an instance of the tkinter class
# Sets the title of the tk instance window
window = tkinter.Tk()
window.title("My Window")
second_window = tkinter.Tk()
second_window.title("Second Window")

# configure sets the different attributes of the tkinter window
window.configure(background='#b5b5b5') # Changes the colour of the window background, can use bg or background takes hexidecimal or name of colour
second_window.configure(background='#f9eab4')
window.geometry('200x200+300+100') # Takes width, height, x and y coordinates all as one string, i.e. 'widthxheight+xaxis+yaxis'

# Used to set the size of the tk instance Window
second_window_width = 500
second_window_height = 250
# Locate the height and width of the screen
screen_width = second_window.winfo_screenwidth()
screen_height = second_window.winfo_screenheight()
# finds the x and y coordinates for the top left of the window (for the tkinter window to be centered)
x_coordinate = (screen_width/2) - (second_window_width/2)
y_coordinate = (screen_height/2) - (second_window_height/2)
second_window.geometry("%dx%d+%d+%d" % (second_window_width, second_window_height, x_coordinate, y_coordinate)) # converts the formatted string (%d) into the values on other side of % (second_window_width, second_window_height, x_coordinate, y_coordinate)

window.mainloop() # is the loop for the program that is waiting for user input (fetch/execute cycle)

from bokeh.io import output_file, show
from bokeh.plotting import figure

output_file('test.html') # outputs the data visualisation to a html file to be viewed on the internet

plot = figure(plot_width=800, plot_height=400, tools='pan, box_zoom, reset') # figure() is configuration just of box that displays the images, plot_width and plot_height is the width and height of the box, tools is what tools can be used with the figure/image.

plot.square(x=[1, 2, 4, 8, 10], y=[6, 2, 18, 4, 9], size=10) # plot.square() will plot squares onto the figure/image box, x and y coordinates correspond to the positions in the list each is a squares position, size sets the size of the squares

show(plot) # show() is responsible for displaying the plot of squares in the figure/image box

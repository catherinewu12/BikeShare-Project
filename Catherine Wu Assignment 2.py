'''
Name: Catherine Wu
Student ID: 20099368
Date created: October 14th, 2018
Date last modified: October 23rd, 2018


This program creates a tkinter canvas and plots different mathematical functions
onto drawn x and y axes. The functions are defined in the program and include
two parabolas, two sinusoidal functions, one logarithmic function,
and one rational function. 
Each graph is able to be maniuplated so that the starting/ending x value, the
size and spacing of the plotted functions, and the colour of the plotted points
can be manipulated simply by changing the different parameter values.
'''


from tkinter import *
from math import *

CANV_WIDTH = 750
CANV_HEIGHT = 250


"""
This function draws a horizontal line across the middle of the canvas, and a
vertical line down the centre of the canvas using tkinter's default line thickness
and colour.
Ticks: Begin at the axis and draw a line that is tickSize length. For the
x-axis, the ticks are drawn beneath the axis while the y-axis ticks are drawn
to the left of the axis.
scale is the multiplier which affects the spacing between ticks along the axis.
"""
def draw_axes(scale, tickSize):
   
    # Draw the x axis
    width = w.winfo_width()
    w.create_line(get_x(-width//2),get_y(0),get_x(width//2),get_y(0))

    # Draw the y axis
    height = w.winfo_height()
    w.create_line(get_x(0),get_y(-height//2),get_x(0),get_y(height//2))

    
    
    #x-axis ticks
    for i in range(width):
        w.create_line(get_x(i*scale),height//2,get_x(i*scale),height//2 + tickSize)
        w.create_line(get_x(-i*scale),height//2,get_x(-i*scale),height//2 + tickSize)

    #y axis ticks
    for i in range(height):
        w.create_line(width//2,get_y(i*scale),width//2 - tickSize,get_y(i*scale))
        w.create_line(width//2,get_y(-i*scale),width//2 - tickSize,get_y(-i*scale))


"""
This function maps a Cartesian-style x coordinate (where x is 0 at the window's
horizontal centre) onto the tkinter canvas (where x is 0 is at the left
edge). x_val is the Cartesian x coordinate. The units of measurerment
are pixels.
""" 
def get_x(x_val):

    #reposition x value to a coordinate based on axes where origin is in the
    #centre of the screen
    width = w.winfo_width()
    x_pos = x_val + width//2

    #return a value for the x-coordinate based on the axes
    return x_pos 


"""
This function maps a Cartesian-style y coordinate (where y is 0 at the window's
vertical centre, and in which y grows in value upwards) onto the tkinter
canvas (where y is 0 is at the top edge, and y grows in value downwards).
y_val is the Cartesian y coordinate. The returned value is the
corresponding tkinter canvas x coordinate. The units of measurerment are
pixels.
"""
def get_y(y_val):

    #reposition y value to a coordinate based on axes where origin is in the
    #centre of the screen. Y values increase while moving down screen so
    #subtract from the x-axis (opposite of intuition)
    height = w.winfo_height()
    y_pos = height//2 - y_val

    #return a value for the y-coordinate based on the axes
    return y_pos 


"""
This function draws a single pixel "dot" at Cartesian coordinates (x,y).
The optional colour parameter determines the colour of the dot.
"""
def plot_point(x,y,colour='black'):

    #put x and y values through get_x and get_y functions to convert values into coordinates
    x_coord = get_x(x) 
    y_coord= get_y(y)

    #draw a tiny oval at the x and y coordinates
    #colour is optional and can be defined to change colour of the dot
    #dot will be black if call to function does not include colour parameter 
    w.create_oval(x_coord, y_coord, x_coord, y_coord, width = 0, fill = colour)

        
"""
This function plots a function, y = fn(x), onto the canvas.
"""
def plot_fn(fn,start_x,end_x,scale=20,colour='black'):
    """
    Parameters:

    * fn is a function that takes a single number parameter and returns a
      number.
	  
    * start_x is the left-most x value to be passed to fn.

    * end_x is the right-most x value to be passed to fn.
	
    * scale (optional) is used as a multiplier in both the x and y directions
      to "zoom in" on the plot. It is also used to increase the number of x
      coordinates "fed" to the fn function, to fill in all the horizontal gaps
      that would otherwise appear between the plotted points. scale is
      particularly useful for showing detail that would be otherwise be lost.

    * colour (optional) determines the colour of the plotted function.
	
    Note: nothing bad happens if start_x, end_x, or any y value computed from
    fn(x) is off the canvas. Those points simply will not be displayed.
    (Note to the student programmer: This happens automatically. You don't
    have to program it.)
    """

    x = start_x

    #loops through x values beginning from the start_x until the end_x
    while x < end_x:

        #scale the points so they plot onto the canvas based on the axes
        x_point = x*scale
        y_point = fn(x)*scale

        #ensure undefined points(returned as False from mathematical function)
        #are not plotted
        if y_point:
            #plot real points by calling plot_point function
            plot_point(x_point, y_point, colour)

        #increase the value of the x coordinate being plotted based on the scale
        #the greater the scale, the closer together the plotting of points
        x += 1/scale


"""
Mathematical functions:
Each function takes an input x value and outputs an fn(x),
y-coordinate, value, based on the mathematical formula
"""


"""This function returns the square of x"""   
def square(x):
    
    return x * x


"""This function returns a quadratic polynomial function (for testing)."""
def func_1(x):
    
    return -3 * square(x) + 2 * x + 1


"""This function returns log(x)""" 
def func_2(x):
    
    #log has domain x > 0 so use try/except to catch undefined fn(x) 
    try:
       log_graph = log(x)
    except:
        #exit function if fn(x) undefined and return to plot_fn to move onto
        #next x_val
        return False
    
    return log_graph


"""
This function returns a transformed rational function with its vertical
asymptote at x = -3
""" 
def func_3(x):
    
    #use try/except to catch division by 0 error
    try:
        rational_graph = 1/(x+3)
    except ZeroDivisionError:
        #exit function if fn(x) undefined and return to plot_fn to move onto
        #next x_val
        return False
    
    return rational_graph


"""create tkinter canvas on which functions, fn(x), will be plotted"""
master = Tk()
master.title('Plot THIS!')
w = Canvas(master,
           width=CANV_WIDTH,
           height=CANV_HEIGHT)
w.pack(expand=YES, fill=BOTH)
w.update() # makes w.winfo_width() and w.winfo_height() meaningful


"""function to call each mathematical function to be plotted onto canvas graph"""
def main():
    
    draw_axes(50,5)
    plot_fn(sin,-20,20,40,'green') # sin() is defined in the math module
    plot_fn(cos,-20,20,40,'blue')  # cos() is defined in the math module
    plot_fn(square,-20,20,40,'red')
    plot_fn(func_1,-20,20,40,'purple')
    plot_fn(func_2,-20,20,40,'brown')
    plot_fn(func_3,-20,20,40,'cyan')


#Run the program
main()

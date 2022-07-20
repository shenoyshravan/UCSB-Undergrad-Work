# drawings.py, Shravan Sharath Shenoy
import turtle

def drawRectangle_1(t):
   " docstring here "
   pass

   
def drawRectangle(t,width, height, tilt, penColor, fillColor):
   " docstring here "
   pass      

 
def drawTwoRectangles(t):
   " docstring here "
   pass

def drawTriangle(t, side, penColor, fillColor):
   " docstring here "
   pass

def drawTwoTriangles(t):
   " docstring here "
   pass      

if __name__=="__main__":
    chris = turtle.Turtle()
    chris.shape("turtle")
    chris.speed(0)
    chris.width(4)

def drawRectangle_1(t):
    """
    draw a rectangle with width 50, height 100, 
    tilt 0, pen color green and fill color yellow. 
    Use a turtle called t to create the drawing
    """
    t.color("green", "yellow")
    t.seth(0)        # Set the initial orientation to 0 degrees
    t.begin_fill()   
    t.forward(50)    # Move the turtle forward by 50 units
                     # in the direction that it was pointing
    t.left(90)       # Turn the turtle left by 90 degrees 
                     # relative to the direction it was pointing
    t.forward(100)   # Move the turtle forward by 100 units
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)       # Make sure the turtle is oriented back
                     # to its initial orientation
    t.end_fill()

def drawRectangle(t, width, height, tilt, penColor, fillColor):
    """
    draw a rectangle with a given width, height, penColor and fillColor,
    with the current location of the turtle being the 
    lower left corner, and the bottom side tilted by an angle tilt (specified in degrees)
    relative to the horizontal axis. After the rectangle is drawn, the turtle should return to its original position with an orientation of 0 degrees with respect to the x-axis.
    Use a turtle called t to create the drawing
    """
    t.color(penColor,fillColor)
    t.seth(tilt)
    t.begin_fill() 
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()
    return

def drawTwoRectangles(t):
    
    drawRectangle(t, 50, 100, 0, "red", "") 

    t.seth(0)   # Set the absolute heading of 
                # the turtle to 0 degrees (pointing east)


    # Move the turtle right by 100 units without 
    # drawing a line

    t.up()     
    t.forward(100)  
    t.down()
    
    drawRectangle(t, 100, 150, 22, "green", "yellow")
    return

def drawTriangle(t,side, penColor, fillColor):
    t.seth(0) 
    t.color(penColor,fillColor)
    t.begin_fill() 
    t.forward(side)
    t.left(120)
    t.forward(side)
    t.left(120)
    t.forward(side)
    t.left(120)
    t.end_fill()
    return

def drawTwoTriangles(t):
    t.seth(-90)
    t.up()     
    t.forward(50)  
    t.down()

    drawTriangle(t,30,"red","")

    t.seth(0)

    t.up()     
    t.forward(100)  
    t.down()
    
    drawTriangle(t,50,"green","yellow")
    return


drawTwoRectangles(chris)
drawTwoTriangles(chris)

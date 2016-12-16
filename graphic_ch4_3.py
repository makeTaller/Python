'''

Create archery target board
Created on Dec 15, 2016

@author: dsparrow
'''

from graphics import *

def main():

    win = GraphWin("Graphics Window")
    # Create archery target board
    
    radius = 30

    #for i in range(10):
    center = Point(85,50)
    
    circ = Circle(center,radius )
    circ.setOutline("black")
    circ.setFill("black")
    radius = radius -25

    l =Line(Point(80,45),Point(90,45))
    l.setFill("red")
    r = l.clone()
    r.move(20,0)
    
    mouth = Line(Point(85,70),Point(110,68))
    mouth.setFill("red")

    # create the eyes of the face
    lefteye = Circle(center,radius)
    lefteye.setFill("red")
    lefteye.setOutline("black")
    righteye= lefteye.clone()
    righteye.move(20,0)

    # draw the objects to display
    circ.draw(win)
    lefteye.draw(win)
    righteye.draw(win)
    l.draw(win)
    r.draw(win)
    mouth.draw(win)

    win.getMouse()
    win.close()

    #win.close()
     
main()
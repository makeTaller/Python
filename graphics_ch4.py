'''
Created on Dec 15, 2016

@author: dsparrow
'''

from graphics import *

def main():
    win = GraphWin("Graphics Window")
    win.setCoords(0.0, 0.0, 30.0, 30.0)
    
    message = Text(Point(5,0.5), "Click on three points")
    message.draw(win)

    # Get and draw four sides of a square
    p1 = Point(7,4)
    p1.draw(win)

    p2 = Point(7,26)
    p2.draw(win)

    p3 = Point(29,26)
    p3.draw(win)

    p4 = Point(29,4)
    p4.draw(win)

    #for i in range(10):
    shape = Polygon(p1,p2,p3,p4)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    message.setText("Click anywhere to quit")
    win.getMouse()
    #win.close()
     
main()
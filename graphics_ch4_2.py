'''

Create archery target board
Created on Dec 15, 2016

@author: dsparrow
'''

from graphics import *

def main():

    win = GraphWin("Graphics Window")
    # Create archery target board
    
    color = ['red','blue','yellow','cyan']
    radius = 30

    #for i in range(10):
    center = Point(85,50)
    
    for i in color:

        circ = Circle(center,radius )
        circ.setOutline(i)
        circ.setFill(i)
        radius = radius -8
        #circle_r += circ.getRadius() -8
        #circ.getCenter()
        circ.draw(win)

    win.getMouse()
    win.close()

    #win.close()
     
main()
'''

This is a christmas  scene 

created by: kirk Tolliver
'''
from graphics import *

def main():
    # Variables
    p1 = Point(0,400)
    p2 = Point(400,100)

    # Create the window manager
    win = GraphWin("Winter Season",400,400)
    win.setBackground("white")

    # Create the sky
    sky = Rectangle(Point(400,0),Point(0,300))
    sky.setFill("blue1")
    sky.draw(win)

    # Create the land 
    land = Rectangle(p1,p2)
    land.setFill("white")
    land.setWidth(1)
    land.draw(win)
     
    # Create the tree
    tree = Polygon(Point(80,280), Point(180,30),Point(280,280))
    tree.setFill("green")
    tree.draw(win)
    trunk = Rectangle(Point(170,340),Point(190,280))
    trunk.setFill("brown")
    trunk.draw(win)

    # Create snowmobile
    base = Oval(Point(255,340),Point(350,370))
    base.setFill("black")
    base.draw(win)
    
    snow = Oval(Point(260,330),Point(360,360))
    snow.setFill("purple")
    snow.draw(win)
    
    handle = Line(Point(320,310),Point(275,335))
    handle.setFill("purple")
    handle.setWidth(7)
    handle.draw(win)
    

    win.getMouse()
    win.close()
main()
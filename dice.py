# A progam that draws 5 dice 
# by: Kirk Tolliver

from graphics import *

def main():
	
	win = GraphWin(" Dice ", 800, 300)
	win.setCoords(0.0, 0.0,3.0,4.0)
        win.setBackground("blue")

        # Default Values
        x1 = 0.5
        x2 = 0.7
        y1 = 1.5
        y2 = 2.5

	point1 = Point(x1,y1)
	point2 = Point(x2,y2) 

        # Draw Die 1	
	die1 = Rectangle(point1,point2).draw(win)
        die1.setFill('white')
        position = Point(x1+.1,y1+.5).draw(win)



        # Draw Die 2	
	die2 = die1.clone().draw(win)
	die2.move(.5,0)
        position1 = Point(x1+.6,y1+.2).draw(win)
        position2 = Point(x1+.6,y1+.7).draw(win)

        

        # Draw Die 3	

	die3 = die2.clone().draw(win)
	die3.move(.5,0)
        position1 = Point(x1+1.05,y1+.1).draw(win)
        position2 = Point(x1+1.10,y1+.5).draw(win)
        position3 = Point(x1+1.15,y1+.8).draw(win)



        # Draw Die 4	
	die4 = die3.clone().draw(win)
	die4.move(.5,0)
        position1 = Point(x1+1.55,y1+.1).draw(win)
        position2 = Point(x1+1.65,y1+.8).draw(win)
        position3 = Point(x1+1.55,y1+.8).draw(win)
        position4 = Point(x1+1.65,y1+.1).draw(win)

        # Draw Die 5	
	die5 = die4.clone().draw(win)
	die5.move(.5,0)
        position1 = Point(x1+2.05,y1+.1).draw(win)
        position2 = Point(x1+2.15,y1+.8).draw(win)
        position3 = Point(x1+2.05,y1+.8).draw(win)
        position4 = Point(x1+2.15,y1+.1).draw(win)
        position5 = Point(x1+2.10,y1+.5).draw(win)


	win.getMouse()
	win.close()

	
main()

# A program that draws 5 dice 
# by: Kirk Tolliver

from graphics import *

def main():
	
	win = GraphWin("Celsius Converter", 800, 300)
	win.setCoords(0.0, 0.0,3.0,4.0)

	for i in range(5):
		incr = .2
		incr_point = incr_point + incr
		point1 = Point(0.5+incr_point,1.5)
		point2 = Point(0.7+incr_point,2.5) 
		die = Rectangle(point1,point2).draw(win)


	win.getMouse()
	win.close()

	
	main()

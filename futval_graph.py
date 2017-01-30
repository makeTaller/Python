'''
futval_graph.py


Created on Dec 14, 2016

@author: dsparrow
'''

from graphics import *

def main():
    # Indroduction
    
    print("This program plots the  growth of a 10-year investment.")
    
    
    # Get principal and interest rate
    principal = eval(raw_input("Enter the initial  principal: "))
    apr = eval(raw_input("Enter the annualized interest rate:"))
    
    # Create a graphic window with labels on left 
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setCoords(-1.75, -200, 11.5, 10400)
    win.setBackground("white")
    Text(Point(-1,0), '0.0K').draw(win)
    Text(Point(-1,2500), '2.5K').draw(win)
    Text(Point(-1,5000), '5.0K').draw(win)
    Text(Point(-1,7500), '7.5K').draw(win)
    Text(Point(-1,10000), '10.0K').draw(win)
    
    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1,principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1,11):
        # calculate value for the years
        principal  = principal * (1 + apr)
        #draw bar for this value
        bar = Rectangle(Point(year,0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
        
        
    input("Press <Enter> to quit")
    win.getMouse()
    win.close()
main()

'''
futval_graph1.py


Created on Dec 14, 2016

@author: dsparrow
'''

from graphics import *

def main():
    # Indroduction
    
    print("This program plosts the  growth of a 10-year investment.")
    
    
    # Get principal and interest rate
    principal = eval(raw_input("Enter the initial  principal: "))
    apr = eval(raw_input("Enter the annualized interest rate:"))
    
    # Create a graphic window with labels on left 
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20,230), '0.0K').draw(win)
    Text(Point(20,180), '2.5K').draw(win)
    Text(Point(20,130), '5.0K').draw(win)
    Text(Point(20,80), '7.5K').draw(win)
    Text(Point(20,30), '10.0K').draw(win)
    
    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65,230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1,11):
        # calculate value for the years
        principal *= (1 + apr)
        #draw bar for this valur
        x11  = year * 25 +40
        height = principal * 0.02
        bar = Rectangle(Point(x11,230), Point(x11 + 25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
        
        
    raw_input("Press <Enter> to quit")
    win.close()
main()
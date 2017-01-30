'''
futval_graph1.py


Created on Dec 14, 2016

@author: dsparrow
'''

from graphics import *

def main():
    # Indroduction
    
    print("This program plots the  growth of a 10-year investment.")
    

    #Draw the first win 
    win = GraphWin("Enter Values", 620, 540)
    win.setCoords(0.0,0.0,3.0,8.0)
    win.setBackground("white")

    Text(Point(1,3),"Enter Principal:").draw(win)
    Text(Point(1,2),"    Enter Apr:").draw(win)
    
    # Get principal and interest rate
    principal_input = Entry(Point(2,3),5)
    apr_input = Entry(Point(2,2),5)

    apr_input.setText("0.7")
    
    principal_input.draw(win)
    apr_input.draw(win)

    # Create a graphic win with labels on left 
    Text(Point(20,230), '0.0K').draw(win)
    Text(Point(20,180), '2.5K').draw(win)
    Text(Point(20,130), '5.0K').draw(win)
    Text(Point(20,80), '7.5K').draw(win)
    Text(Point(20,30), '10.0K').draw(win)


    # Convert Principal and Apr into integers
    principal = eval(principal_input.getText())
    apr = eval(apr_input.getText())

    
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
        
        

    input("Press <Enter> to quit")
    win.close()

main()

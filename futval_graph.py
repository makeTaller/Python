# futval_graph.py
# Draw scale labels on left side of window
#
# Draw label " 0.0K " at (20,230)
# Draw lable " 2.5K"  at (20,180)
# Draw lable " 5.0K"  at (20,130)
# Draw lable " 7.5K " at (20,80)
# Draw label "10.0K"  at (20,30)
from graphics import *

def main():
    #Introduction
    print("This program plots the growth of a 10-year investment.")

    #Get principal and interest rate
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))
    # Get a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 420,240)
    win.setBackground("white")
    Text(Point(20,230), ' 0.0K').draw(win)
    Text(Point(20,180), ' 2.5K').draw(win)
    Text(Point(20,130), ' 5.0K').draw(win)
    Text(Point(20,80), ' 7.5K').draw(win)
    Text(Point(20,30), ' 10.0K').draw(win)

    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40,230), Point(65,230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for sucessive years
    for year in range(1,11):
        #calculate value for the next years
        principal = principal * (1 + apr)
        #draw bar for this value
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11,230), Point(x11 +25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()

main()

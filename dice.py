# Dice
# by: Kirk Tolliver

from graphics import *

def main():
    win = GraphWin("Dice", 400,200)
    diceShape = Polygon(Point(1,15),Point(15,1),Point(15,30), Point(1,30))
    diceShape.draw(win)

main()

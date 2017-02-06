#!/usr/bin/python3

# This is a program that accepts two points and 
import math

def main():
    x1, y1 = eval(input("Enter the x1 and y1: "))
    y2, x2 = eval(input("Enter the x2 and y2: "))

    slope = y2 -y1 //x2 -y1
    distance = math.sqrt((x2-x1)**2 + (y2 -y1)**2)

    print("Distance: ", distance)
    print("Slope: ", slope )

main()

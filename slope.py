#!/usr/bin/python3

# This program calculates the two points of a slope.

def main():
    x1, x2 = eval(input("Enter the x1 and x2: "))
    y1, y2 = eval(input("Enter the y1 and y2: "))

    slope = y2*2 -y1*1 /x2*2 -x1*1
    print("Slope: ", slope )

main()

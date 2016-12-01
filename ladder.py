#!/usr/bin/python3
import math

def main():
    
    height, angle = eval(input("Enter the height and angle: " ))

    length = height/math.sin(angle)  

    print("The ladder must be: ", int(length), " ft" )
    
main()

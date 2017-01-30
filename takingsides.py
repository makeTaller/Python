#!/usr/bin/python3
import math

def main():
    
    a,b,c = eval(input("Enter the a, b, c sides: " ))

    side =  a + b + c/2 

    area = math.sqrt(side * (side -a) * (side - b) * (side-c))

    print("Sides is: ", side , "Area is: ", round(area,2))
    
main()

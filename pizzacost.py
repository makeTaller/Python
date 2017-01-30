#!/usr/bin/python3
# This program takes in the diameter of a pizza inches and gives the cost per radius.
import math

def main():
    price = eval(input("Enter the cost of the Pizza: "))
    diam = eval(input("Enter the diameter of the Pizza: "))
    radius = diam /2

    area =  math.pi * radius ** 2
    cost = area /price
    print(" Total = ", round(cost,2))
            
main()

#!/usr/bin/python3
# This is  Program to calculate the volume of a Sphere

import math
def main():
    #vol = eval(raw_input("Enter the Volume: "))
    radius = eval(raw_input("Enter the Radius: "))
    #area = eval(raw_input("Enter the Area: "))

    volume = 4/3 * math.pi * radius ** 3
    area = 4 * math.pi * radius ** 2
    print(" This is the Volume: ", volume)
    print(" This is the Area: ", area)

main()

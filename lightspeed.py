#!/usr/bin/python3
#
#This program determines distance to a lightening strike based on the time 
# elasped  between the flash  and the sound  of the thunder.

def main():
    time = eval(input("Enter the Time Elasped: "))
    sound = 1100
    mile = 5280

    distance = time /3

    print(" Distance: ", distance, "miles from you" )

main()

#!/usr/bin/python3

# A program to calculate the value of some chane in dollars


def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type. ")

    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickel: ")) 
    pennies = eval(input("Pennies: "))

    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print()
    print("The total value of your change is ", total)

main()


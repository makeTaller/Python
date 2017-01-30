#!/usr/bin/python3
#
# Factorial 
# Program to compyte the fatorial of al number
# Illustrates for loop with an accumulator

def main():
    n = eval(raw_input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
    print("The factorial of ", n, "is ", fact)

main()

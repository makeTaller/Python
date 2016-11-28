#!/usr/bin/python3

def main():

    for i in range(100):
        expr = input("Please enter the expression : ") 
        prob = eval(expr)
        print(expr, " = ", prob)

main()    

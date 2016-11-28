#!/usr/bin/python3
#
# This is the calculator  under development.

def main():
    print("hello, I'm a calculator.")

   # multi, add = input("Enter : (example: add,sub,div,multi)")
   # div, sub = input("")

    fnum = eval(input("Enter first number: "))

    oper = input("Enter : (example: add,sub,div,multi)")

    snum = eval(input("Enter second number: "))

    multi = eval( fnum * snum)
    add = eval( fnum + snum)
    div = eval( fnum / snum)
    sub = eval( fnum - snum)
    print("Total: ", total)

main()
    

#!/usr/bin/python3

# Calculates easter given the year and the new moon

def main():
    year = eval(input("Enter the Year: "))

    C = year//100

    epact = (8 + (C//4) -C + (8*C + 13) // 25 + 11* (year%19) %30)
    
    print("Easter: ", epact)

main()

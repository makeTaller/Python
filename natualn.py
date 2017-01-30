#!/usr/bin/python3

def main():
   
    num = eval(input("Enter the value: " ))
    nat = 1 
    
    for sum in range(1,num,1):
        nat =  nat + sum
        print( nat )

main()

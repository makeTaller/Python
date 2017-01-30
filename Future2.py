<<<<<<< HEAD
# Interest Rate Calulations
#	A program to calculate the interest gain in a ten year investement
#       This program is intended to show the accomulated value to the annual 
#       fixed investment.
#!/usr/bin/python3

def main():
    print("This program calculates the furture value")

    principal = eval(input("Enter the principal amount: "))
    apr = eval(input("Enter the Annual Percentage Rate: "))
    numYears = eval(input("Enter the number of Years: "))
    userAge = eval(input("Enter your Age: "))
    
    period = apr /4

    for i in range(10):
        total = principal * (1 + apr)
        userAge = userAge +1

    print("The value in ",numYears," years is: ", total * period," and you will be:", userAge)

main()
=======
# Interest Rate Calulations
#	A program to calculate the interest gain in a ten year investement
#       This program is intended to show the accomulated value to the annual 
#       fixed investment.
#!/usr/bin/python3

def main():
    print("This program calculates the furture value")

    principal = eval(input("Enter the principal amount: "))
    apr = eval(input("Enter the Annual Percentage Rate: "))
    numYears = eval(input("Enter the number of Years: "))
    userAge = eval(input("Enter your Age: "))
    period = apr /4

    print("Year | Value | Age ")
    print("===================")

    for i in range(numYears):
        total = principal * (1 + apr)
        userAge = userAge +1
        print("{0} {1:5} {2:5}".format(i +1, total, userAge))

main()
>>>>>>> 0a67ccec86c1d77a8456943d85c63d04037083ee

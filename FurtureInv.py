# Interest Rate Calulations
#	A program to calculate the interest gain in a ten year investement
#!/usr/bin/python3

def main():
    print("This program calculates the furture value")

    principal = eval(input("Enter the principal amount: "))
    apr = eval(input("Enter the Annual Percentage Rate: "))
    numYears = eval(input("Enter the number of Years: "))
    userAge = eval(input("Enter your Age: "))
    
    apr = apr / 100

    for i in range(numYears):
        total = principal * (1 + apr)
        userAge = userAge +1

    print("The value in ",numYears," years is: ", total," and you will be:", userAge)

main()

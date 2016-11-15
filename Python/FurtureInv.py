# Interest Rate Calulations
#	A program to calculate the interest gain in a ten year investement
#!/usr/bin/python3

def main():
	print("This program calculates the furture value")

    principal = eval(input("Enter the principal amount: "))
    apr = eval(input("Enter the Annual Percentage Rate: "))

    for i in range(10):
        prinicpal = principal * (1 + apr)

    print("The value in 10 years is: ", principal)

main()

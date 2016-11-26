# convert.py
#       A program tto convert Celius temp to Farenhiet
# by: kirk Tolliver

def main():
    #This code executes the program once, I added a for loop
    #celsius = eval(input("What is the Celsius temperture?"))
    #fahrenheit = 9/5 * celsius + 32
    #print("The temperture is", fahrenheit, "degrees in Fahrenheit")

    for i in range(5):

        celsius = eval(input("What is the Celsius temperture?"))
        fahrenheit = 9/5 * celsius + 32

        print(celsius, "is", fahrenheit, "degrees in Fahrenheit")

main()



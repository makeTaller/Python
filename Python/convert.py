# convert.py
#       A program tto convert Celius temp to Farenhiet
# by: kirk Tolliver

def main():
    celsius = eval(input("What is the Celsius temperture?"))
    fahrenheit = 9/5 * celsius + 32
    print("The temperture is", fahrenheit, "degrees in Fahrenheit")

main()

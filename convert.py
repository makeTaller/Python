# convert.py
#       A program tto convert Celius temp to Farenhiet
# by: kirk Tolliver

def main():
    #This code executes the program once, I added a for loop
    fahrenheit = eval(input("What is the Fahrenheit temperture?"))
    #print("The temperture is", fahrenheit, "degrees in Fahrenheit")

    #for i in range(5):

    celsius = (fahrenheit - 32) * 5/9  
        

    print( fahrenheit, "is", celsius,"degrees in celsius")

main()



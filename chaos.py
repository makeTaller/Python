<<<<<<< HEAD
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print(x)
=======
#This is a program that calculates the chaotic behavior
#by: kirk tolliver

def main():
    print("This program illustrates a chaotic funciton")
    first = eval(input("Enter a number between 0 and 1: "))
    second = eval(input("Enter a second number between 0 and 1: "))
    iter_val = eval(input("Enter the iteration value: "))

    print("index {0:5.2f} {1:5.2f}".format(first,second))
    print("-----------------")

    for i in range(iter_val):

        first = 3.9 * first * (1 -first)
        second = 3.9 * second * (1 -second)
        print("{0} {1:7.2f} {2:7.2f}".format(i+1,first,second))
>>>>>>> 3e05e0b40272dd0054d7ca2721106d3accccbabf

main()

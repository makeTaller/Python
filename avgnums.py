<<<<<<< HEAD

def main():
    nums = eval(input("Enter the amount of numbers to avergage: "))
    sum =1

    for j in range(nums,1,-1):
        n = eval(input("Enter the number: " ))
        sum = sum + n 
        
    print( "total:",  (sum -1)//nums)

main()
=======

def main():
    print("This progam genrates computer usernames.\n")

    #get user's first an last names

    first = input("Please enter your first name (all lowercase):")
    last = imput("Please enter your last name (all lowercase):")

    #concatenate first initial  with 7 vhars fo the last name.
    uname = first[0] = last[:7]

    #output the username 
    print("your username is:", uname)
main()
>>>>>>> 0a67ccec86c1d77a8456943d85c63d04037083ee

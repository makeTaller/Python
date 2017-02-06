
def main():
    print("This progam genrates computer usernames.\n")

    #get user's first an last names

    first = input("Please enter your first name (all lowercase):")
    last = input("Please enter your last name (all lowercase):")

    #concatenate first initial  with 7 chars fo the last name.
    uname = first[0] + last[:7]

    #output the username 
    print("your username is:", uname)
main()

# This is my version of a ceasar cipher that converterts words into Unicode keys
# by: Kirk Tolliver

def main():
    chrac = input("Enter the characters: ")
    key = eval(input("Enter the key: "))
    
    #This circleulates the last value to shift

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"*10
    convert = " "
    #list = alpha.split("") * 2

    for c in chrac:
        convert=alpha[ord(c)]
        ch = chr(ord(convert) + key)
        print(ch,end="")

main()

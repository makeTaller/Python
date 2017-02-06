# This is a word count program.
# by: Kirk Tolliver

def main():

    wc_input = input("Enter the filename: ")

    infile = open(wc_input,"r")

    chars = infile.read()
    print("Characters: ",len(chars))

    infile.close()


    infile = open(wc_input,"r")

    words = infile.read().split()
    print("Words: ",len(words))
        
    infile.close()

    infile = open(wc_input,"r")

    lines = infile.readlines()
    print("Lines: ",len(lines))
    infile.close()


main()
        


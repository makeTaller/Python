# This is a word count program.
# by: Kirk Tolliver

def main():

    wc_input = input("Enter the filename: ")

    infile = open(wc_input,"r")
    
    output_words = " "
    output_lines = [ ] 

    output_char = infile.read()
    print("Char = ",len(output_char))

    for word in infile.readline(): 
        input_words = w
        output_words = output_words + input_words
    print("Words = ",len(output_words))


    lines = infile.readlines()
    print(len(lines))

    for line in lines:
        print("Lines = ",line)

    infile.close()


main()
        


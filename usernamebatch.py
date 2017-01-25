# This is a User batch program
# by: Kirk Tolliver

def main():
    print("This progam genrates computer usernames.\n")

    #get file the user names are in

    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    # open the files
    infile = open(infileName,"r")
    outfile = open(outfileName,"w")

    #process each line of the input file
    for line in infile:
        #get the first and last names from line
        first,last = line.split()
        #create the username
        uname = (first[0]+last[:7]).lower()
        #write it to the output line
        print(uname,file=outfile)

    #close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)

main()

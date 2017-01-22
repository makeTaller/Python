# This is a program to change your name into a number
#by: Kirk Tolliver 

def main():
        # Return the number value of name

    # Get the name to be converted

    name = input("Enter Your Name: ")
    numer = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mesg = 0

    for n in name.upper():
        convert = numer.find(n)
        mesg = mesg + convert
       
    print("Your name in numerology is: ",mesg)

    #convert = numer.split(",")

    # Convert name into number
    ''' 
    for n in range(len(name)):
        con_name =  name[n]
        #result = name[n] + convert[str(con_name)]
        print(name[n],convert[n],result)
    
    

    for i in numer.split(","):
        conv = i
        mesg = mesg + conv
        print(i,end="")

    #for n in len(name):
       # name[n]

    print(len(numer))

    #for w in range(1,26):
        '''
main()

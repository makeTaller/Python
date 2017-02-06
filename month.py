# Working with the string spliter
# Calendar Program
# by: Kirk Tolliver

def main():
    # months is a list used as a lookup table
    #months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    months=[ "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    n = eval(input("Enter a month number (1-12): "))

    #compute starting postion of month n in months
    #pos = (n-1) * 3

    #Grab the appropriate slice from months
    #monthAbbrev = months[pos:pos+3]

    # print the result
    print("The month abbreviation is", months[n-1] + ".")
main()



def main():
    n = eval(input("Enter the number of terms: "))
    sum =1
    term1 = 1
    term2 =1

    for j in range(1,n,1):
        term1 = 4 /j 
        for i in range(j):
            #print(term1) 
            term2 = 4/(j+2)
            term4 = -4/(j+2)
            #i=j+1
            #print( term2)
        term3 = term1 - term2
        term4 = term3+ term4
        print(term3, term4 )

    #for i in range(n,1,-1): 
       #term2 = 4/on
       #term = i + term2
    #print(term,  sum)
main()


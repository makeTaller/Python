
def main():
    nums = eval(input("Enter the amount of numbers to avergage: "))
    sum =1

    for j in range(nums,1,-1):
        n = eval(input("Enter the number: " ))
        sum = sum + n 
        
    print( "total:",  (sum -1)//nums)

main()

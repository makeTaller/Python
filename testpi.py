def main():
    n = eval(input("Enter the n of terms: "))
    tot = 0
    denominator=1
    denominator_sign=1
    for i in range(n):
        tot = tot + 4/(denominator_sign*denominator)
        denominator = denominator + 2
        denominator_sign = denominator_sign * (-1)
        print(tot)
main()


# CS Professor with a rate of 100 - 0

def main():
    score = eval(input("Enter the score: "))
    scorecard = []
    grade=[A,B,C,D,F]
    
    # Get a score card of the number ranges
    for i in range(50,101):
        scorecard.append(i)
    
    A = scorecard[90:100]
    B = scorecard[80:89]
    C = scorecard[70:79]
    D = scorecard[60:69]
    F = scorecard[51:59]



    print(grade[0])

main() 

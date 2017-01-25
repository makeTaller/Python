# CS Professor with a rate of 100 - 0
# by: Kirk Tolliver

def main():
    score = eval(input("Enter the score: "))
    #scorecard = []
    #scorecard = " "
    #gradenum = []
    grade = []
    # Get a score card of the number ranges
    #for i in range(0,101):
        #scorecard.append(i)
    #    num = str(i) + ","
    #    scorecard += num
    #gradenum=scorecard.split(",")

    for s in range(0,59):
        grade.append("F")
    for s in range(10):
        grade.append("D")
    for s in range(10):
        grade.append("C")
    for s in range(10):
        grade.append("B")
    for s in range(10):
        grade.append("A")

    '''for j in gradenum:
        gradenum[0:59] = "F"
        gradenum[60:69]= "D"
        gradenum[70:79]= "C"
        gradenum[80:89]= "B"
        gradenum[90:100]= "A"
        '''

    print("You Got a:", grade[score])


main()

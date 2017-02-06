# Professor Gradin scale 
# by: kirk tolliver


def main():
    score = eval(input("Enter the score: "))
    grade = ['F','F','D','C','B','A']
    new_score = grade[score]
    print("Your Grade is: ", new_score)
main()

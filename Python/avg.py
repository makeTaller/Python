# avg.py
#   A simple program to average two exam scores
#   Illustrates use of multiple input

def main():
    print( "This program computes the average of two scores" )
    score1, score2 = eval(input( "Enter two scores separated by commas: " ))
    average = (score1 + score2) / 2

    print( "The average of the scores is: ", average)

main()

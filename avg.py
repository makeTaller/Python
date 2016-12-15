# avg.py
#   A simple program to average two exam scores
#   Illustrates use of multiple input

import graphics


def main():
    win = GraphWin("Average of 2", 500, 350)

    print( "This program computes the average of two scores" )
    score1, score2, score3 = eval(input( "Enter three scores separated by commas: " ))
    average = (score1 + score2 + score3) / 2

    print( "The average of the scores is: ", average)
    print(abs)
main()

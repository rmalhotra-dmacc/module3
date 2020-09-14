"""""
Program: average_scores.py
Author: Rajiv Malhotra
Last Modified Date: 09/10/2020
 
The program to  read in a person's names, last and first, their age and three scores out of 100. 
Take the three scores and find the average, storing into a variable
"""""


def average():
    score1 = input("Enter your first score:")
    score2 = input("Enter your second score:")
    score3 = input("Enter your third score:")
    return (int(score1) + int(score2) + int(score3)) / 3


if __name__ == '__main__':
    lastName = input("Enter your last name:")
    firstName = input("Enter your first name:")
    age = input("Enter your age:")
    average_score = average()
    print("{}, {}, age: {} average grade: {}".format(lastName, firstName, age, average_score))

#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using the following table:
try:
    sscore = input('Enter your score: ')
    fscore = float(sscore)

    if fscore > 1.0 or fscore < 0.0:
        print('Score must be between 0.0 and 1.0!')
    elif fscore >= 0.9:
        grade = 'A'
    elif fscore >= 0.8:
        grade = 'B'
    elif fscore >= 0.7:
        grade = 'C'
    elif fscore >= 0.6:
        grade = 'D'
    elif fscore >= 0.5:
        grade = 'E'
    else:
        grade = 'F'

        print('Your grade is:', grade)

except ValueError:
    print('Invalid score! Please enter a numeric value.')

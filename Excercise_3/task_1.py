'''
Imagine the following: It’s late at night. In front of you stands a huge pile of exams which still
need to be graded. They are all due for tomorrow. You can barely see straight, let alone assign the
correct grade for a given score in the exam.
You decide to whip out your sweet Python skills and write a quick script to help you grade
exams following the table below:
Points achieved Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59 F
'''


# Please do not modify this part of the code!
grade = '-'

# Your code goes here
score=int(input('Please enter score between 0 to 100:'))
if 0<=score<=100:
    if 90<=score<=100:
        grade='A'
    elif 80<=score<90:
        grade='B'
    elif 70<=score<80:
        grade='C'
    elif 60<=score<70:
        grade='D'
    else:
        grade='F'
else:
    print('This is invalid input.Please provide valid value for score')

print('The grade is',grade)
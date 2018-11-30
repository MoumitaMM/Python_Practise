# Please do not modify this part of the code! 
# This is just to show how you should name the variables containing your answers
task_0 = 'Python is cool!' * 3
print('Task 0:', task_0)


# Your code goes here
# Task 1
task_1 = True if (pow((pow(65,17)%3233),413)%3233 == 65) else False
print('Task 1:',task_1)

# Task 2
'''Use string slicing to split the word "doghouse" into the two separate English words "dog"
and "house". Fill the two variables accordingly.
'''
doghouse = "doghouse"
task_2_p1 =doghouse[0:3]
print('Task 2 p1:',task_2_p1)
task_2_p2 =doghouse[3:]
print('Task 2 p2:',task_2_p2)

# Task 3
''' A palindrome is a string that reads the same backward as forward. "anna" is an example
of a palindrome. Write a Python expression that checks if "anna" is a palindrome. Store the
result of this expression in the task_3 variable.
'''
task_3 = True if ('anna' == 'anna'[::-1]) else False
print('Task 3:', task_3)


# Task 4
'''
Find a Python expression that checks if a string is part of another string using membership
operators.
You have to check whether the string "alpha" is contained in the string "alphanumeric".
Store the result of this expression in the provided task_4 variable.
'''
task_4 = True if ('alpha' in 'alphanumeric' ) else False
print('Task 4:', task_4)

# Task 5
''' Find a Python expression that when given a string creates a new string with the original
string repeated multiple times:
Given "Python is cool!" create the string "Python is cool!Python is cool!Python is cool!
Store the result of this expression in the provided task_5 variable.
'''
s=input('Enter String for Task5:')
n=int(input('Repeatability of string for Task5:'))
task_5 = s*n
print('Task 5:', task_5)

# Task_6
''' The winner of a competition scored 95.66666666666667 points.
Write a Python expression that round this value to a two decimal digits (95.67).
Store the result of this expression in the provided task_6 variable.
Note: First define the variable percentage to be 95.66666666666667. Then find how to format
the string contained in this variable to a string rounded to two digits after the decimal
point 5.'''
percentage=95.66666666666667
task_6 =percentage
print('Task 6: %.2f'%(task_6))
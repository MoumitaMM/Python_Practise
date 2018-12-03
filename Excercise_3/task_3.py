'''
Password validator
You are the administrator of an online shopping site and you realize that the password restrictions
for users creating a new login are not rigorous enough. You decide to implement a Python
program that helps you check whether a new password meets the new, stricter password requirements
you came up with. The requirements are as follows:
a. The length of the password needs to be from 8 to 30 characters.
b. The password needs to contain at least 2 uppercase characters.
c. The password needs to contain at least 2 lowercase characters.
d. The password needs to contain at least 1 digit.
e. The password needs to contain exactly 1, but not more of the following special characters:
@/%&*_-

Your task is to implement a Python program that takes a password as input and checks whether
it meets the requirements listed above. Start by asking the user for a password and store the input
in a variable. To test all the requirements, you might have to iterate over the individual characters
of the input string. Also have a look at the string methods available in Python1, as some of them
will be very helpful for this task. The variable is_valid is already defined for you with an initial
boolean value of False. Your job is to assign it to either False or True, depending on whether
the given password meets all requirements or not. Your program does not need to print anything,
but if you want, you can print out a message displaying the is_valid variable to test whether
your validator works.
'''


# Please do not modify this part of the code!
special_character_set = "@/%&*_-"

is_valid = False

# Your code goes here
input_pwd=input('Please setup your password :')
cnt_upr=0
cnt_lwr=0
cnt_dgt=0
cnt_sp_ch=0
if 8<=len(input_pwd)<=30:
    for i in input_pwd:
        if i.isupper():
            cnt_upr+=1
        elif i.islower():
            cnt_lwr+=1
        elif i.isdigit():
            cnt_dgt+=1
        elif i in special_character_set:
            cnt_sp_ch+=1

    if cnt_upr>=2 and cnt_lwr>=2 and cnt_dgt>=1 and cnt_sp_ch==1 :
        is_valid = True
    else:
        is_valid = False
else:
    is_valid = False

print('Is the input password valid?',is_valid)
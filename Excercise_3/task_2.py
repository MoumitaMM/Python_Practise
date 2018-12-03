'''
Rock-Paper-Scissors
Rock-paper-scissors is a game in which at least two people simultaneously draw their hand in the
form of either a rock, a paper or a scissor. The following rules apply:
a. Rock beats scissors
b. Scissors beats paper
c. Paper beats rock
d. Same choice means a tie
Your task is to implement a Python version of the rock-paper-scissors game.

Start by prompting twice for an user input (once for user 1, once for user 2). Store the given inputs
in two variables and give them meaningful names. The input should be one of the three options:
Rock, Paper or Scissors. In case one or both of the inputs are invalid, assign the string value ”Wrong
input” to the variable result. If both inputs are correct, check who wins the game by applying
the rules mentioned above. You need to set the value of the variable result to either ”User 1
wins”, ”User 2 wins” or ”Tie” in case of a draw.
'''


# Please do not modify this part of the code!
result = ""

# Your code goes here
user1_input=input('Please input one of the three options in capital letters (ROCK, PAPER or SCISSORS):')
user2_input=input('Please input one of the three options in capital letters (ROCK, PAPER or SCISSORS):')
vld_inpt_lst=['ROCK','PAPER','SCISSORS']
if user1_input in vld_inpt_lst and user2_input in vld_inpt_lst:
    if user1_input==user2_input:
        result = 'Tie'
    elif user1_input=='ROCK' and user2_input=='SCISSORS':
        result = 'User 1 wins'
    elif user1_input=='SCISSORS' and user2_input=='ROCK':
        result = 'User 2 wins'
    elif user1_input=='SCISSORS' and user2_input=='PAPER':
        result = 'User 1 wins'
    elif user1_input=='PAPER' and user2_input=='SCISSORS':
        result = 'User 2 wins'
    elif user1_input=='PAPER' and user2_input=='ROCK':
        result = 'User 1 wins'
    elif user1_input=='ROCK' and user2_input=='PAPER':
        result = 'User 2 wins'
else:
    result ='Wrong input'
print('The result is :',result)
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

randNum = random.randint(1, 21)
userGuessCount = 0

while True:
    userGuessCount = userGuessCount + 1
    print('Take a guess.')
    guess = int(input())
    
    if randNum > guess:
        print('Your guess is too low.')
    elif randNum < guess:
        print('Your guess is too high.')
    elif randNum == guess:
        print('Good job, ' + name + '! You guess my number ' + str(userGuessCount) + ' guesses!')
        break



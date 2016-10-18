# Random Number Guessing Game
# Write a program that generates a random number in the range of 1 through
# 100, and asks the user to guess what the number is. If the user's guess is
# higher than the random number, the program should display
# 'Too high, try again'. If too low, 'Too low, try again'
# If the user guesses correct, congratulate user and then generate a new
# random number to start game over

import random

def main():

    play = Play()

    while play == True:
        generate_random = GenerateRandom()
        user_guess = UserGuess(generate_random)
        Play()

def Play():
    print()
    play = input('Would you like to play the guess game? (y/n) ')
    if play == 'y':
        return True
    elif play == 'n':
        print('Thank you for playing')
        return False

def GenerateRandom():
    print()
    print('=================== Guess a number ==================')
    num = random.randint(1, 101)
    return num

def UserGuess(random):
    guess = int(input('Guess between 1 and 100: '))

    while guess != random:
        if guess < random:
            print('Too Low, try again')
            guess = int(input('Guess between 1 and 100: '))
        elif guess > random:
            print('Too High, try again')
            guess = int(input('Guess between 1 and 100: '))
        
    print('You guessed right! Awesome.',
            'Your Guess:', guess, '\tComputer\'s pick:', random)

main()

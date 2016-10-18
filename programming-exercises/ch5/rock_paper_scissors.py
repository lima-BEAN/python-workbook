# Write a program that lets the user play Rock, Paper, Scissors
# against the computer. The program should work as follows:
# 1. When program begins, random number in range of 1 through 3 is generated
#    If number = 1, computer is rock
#    If number = 2, computer is paper
#    If number = 3, computer is scissor
# 2. User enters choice, 'rock', 'paper', 'scissor' at keyboard
# 3. Computer's choice displayed
# 4. Winner is selected by:
#     rock > scissor;   scissor > paper;    paper > rock;   tie-breaker
import random

def main():

    computer_pick = ComputerPick()
    user_pick = UserPick()

    Winner(computer_pick, user_pick)

def ComputerPick():
    print()
    print('=============== Rock Paper Scissors ==============')
    pick = random.randint(1, 3)

    if pick == 1:
        return 'Rock'
    elif pick == 2:
        return 'Paper'
    elif pick == 3:
        return 'Scissors'

def UserPick():
    pick = input('Choose paper, rock or scissors to compete with AI: ')

    if pick.capitalize() == 'Rock' or pick.capitalize() == 'Paper' or pick.capitalize() == 'Scissors':
        return pick.capitalize()
    

def Winner(cpu, usr):
    print('Computer:', cpu, '\tYou:', usr)
    if cpu == usr:
        print('You both chose', usr, 'Tie-breaker TIME!')
        main()
    elif cpu == 'Rock':
        if usr == 'Paper':
            print('YOU WIN with', usr, '\nSorry', cpu)
        elif usr == 'Scissors':
            print('Computer wins with', cpu, '\nSorry', usr)

    elif cpu == 'Paper':
        if usr == 'Scissors':
            print('YOU WIN with', usr, '\nSorry', cpu)
        elif usr == 'Rock':
            print('Computer wins with', cpu, '\nSorry', usr)

    elif cpu == 'Scissors':
        if usr == 'Rock':
            print('YOU WIN with', usr, '\nSorry', cpu)
        elif usr == 'Paper':
            print('Computer wins with', cpu, '\nSorry', usr)

main()

# Write a program that gives simple math quizzes. The program should display
# random numbers that are to be added, such as: 247 + 129
# The program should allow the student to enter the answer. If the answer is
# incorrect, a message showing the correct answer should be displayed

import random

def main():

    Greeting()
    
    random_a = RandomA()
    random_b = RandomB()
    add_random = AddRandom(random_a, random_b)

    CheckAnswer(random_a, random_b, add_random)


def Greeting():
    print()
    print('=================== Math Quiz =======================')
    print()


def RandomA():
    a = random.randint(1, 1001)
    return a
def RandomB():
    b = random.randint(1, 505)
    return b

def AddRandom(a, b):
    return a + b


def CheckAnswer(a, b, answer):
    user_answer = int(input('What is ' + str(a) + ' + ' + str(b) + ' ? '))
    if user_answer == answer:
        print('Awesome! That\'s right.')
    else:
        print('Sorry.', answer, 'is the right answer.')

main()

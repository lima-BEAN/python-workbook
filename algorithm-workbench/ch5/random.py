# Write a statement that generates a random number in the range of 1 through
# 100 and assigns it to a variable named rand.

import random

def main():
    rand = random_number()
    print('Random number between 1 - 100:', rand)

def random_number():
    return random.randint(1,100)

main()

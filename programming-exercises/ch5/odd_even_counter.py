# Write a program that generates 100 random numbers and keeps count
# of how many of those random numbers are even and how many are odd.

import random

GENERATE = 100

def main():

    random_numbers = RandomNumbers()
    
    Results(random_numbers)

def RandomNumbers():
    random_list = []
    for x in range(GENERATE):
        random_list.append(random.randint(1, 1000))
    return random_list


def Results(numbers):

    odd_count = 1
    even_count = 1
    print()
    print('============= Evens and Odds Generated ===================')

    for number in numbers:
        if (number % 2) != 0:
            print(number, 'is odd')
            odd_count += 1
        elif (number % 2) == 0:
            print(number, 'is even')
            even_count += 1
    print()
    print('There are', odd_count, 'odds and', even_count, 'evens',
          '\nFor a total of', len(numbers), 'random numbers generated')
        


main()

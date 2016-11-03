# Write a program that writes a series of random numbers to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random
# numbers the file will hold.

import random

def main():
    num_of_randoms = NumOfRandoms()
    Write(num_of_randoms)

def NumOfRandoms():
    num = int(input('How many random numbers would you like to write to file? '))
    return num

def Write(num):
    file = open('num_of_randoms.txt', 'w')
    for x in range(num):
        file.write(str(random.randint(1, 501)) + '\n')

main()

# Lottery Number Generator
# Design a program that generates a seven-digit lottery number.
# The program should generate 7 random numbers, each in the range
# of 0 through 9, and assign each number to a list element.
# (Random numbers were discussed in ch. 5.) Then write another loop
# that displays the contents of the list.
import random

def main():

    randoms = Randoms()
    Display(randoms)

def Randoms():
    randoms = []
    for r in range(7):
        random_num = random.randint(0, 9)
        randoms.append(random_num)
    return randoms

def Display(randoms):
    count = 0
    for num in randoms:
        count += 1
        print(str(count) + '. ' + str(num))

main()

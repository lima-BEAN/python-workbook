# Assume that a file containing a series of integers is named numbers.txt
# and exists on the computer's disk. Write a program that reads all of
# the numbers stored in the file and calculates their total

def main():
    numbers = Read()
    total = Total(numbers)
    Display(total)
    
def Read():
    numbers = []
    file = open('numbers.txt', 'r')
    for line in file:
        numbers.append(line.rstrip())
    return numbers

def Total(numbers):
    total = 0
    for x in numbers:
        total += int(x)
    return total

def Display(total):
    print('The sum of the numbers in numbers.txt is: ' + str(total))

main()

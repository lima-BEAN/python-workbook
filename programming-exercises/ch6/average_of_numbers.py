# Assume that a file containing a series of integers is named numbers.txt
# and exists on the computer's disk. Write a program that calculates
# the average of all the numbers stored in the file.

def main():
    number_count = Read()
    average = Average(number_count)
    Display(average)

def Read():
    numbers = []
    file = open('numbers.txt', 'r')
    for line in file:
        number = line.rstrip()
        numbers.append(number)
    return numbers

def Average(numbers):
    count = 0
    average = 0
    total = 0
    for num in numbers:
        total += int(num)
        count += 1
    average = total / count
    return average

def Display(average):
    print('The average for the numbers in numbers.txt is: ' + str(average))

main()

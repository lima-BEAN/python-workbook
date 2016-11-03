# Modify the program that you wrote for average_of_numbers.py so it handles
# the following exceptions:
#   - It should handle any IOError exceptions that are raised when the file
#     is opened and data is read from it.
#   - It should handle any ValueError exceptions that are raised when the items
#     that are read from the file are converted to a number.

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


## need to finish

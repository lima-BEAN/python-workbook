# Number Analysis Program
# Design a program that asks the user to enter a series of 20 numbers.
# The program should store the numbers in a list and then display
# the following data:
#   - The lowest number in the list
#   - The highest number in the list
#   - The total of the numbers in the list
#   - The average of the numbers in the list

def main():
    numbers =   Numbers()
    lowest =    Lowest(numbers)
    highest =   Highest(numbers)
    total =     Total(numbers)
    average =   Average(numbers, total)
    Display(numbers, lowest, highest, total, average)

def Numbers():
    numbers = []
    print()
    print('============== Number Analysis ================')
    print()
    print('Input 20 numbers to get an analysis')
    for x in range(20):
        number = float(input(str(x+1) + ': ' ))
        numbers.append(number)
    return numbers

def Lowest(numbers):
    lowest = None
    for num in numbers:
        if lowest == None or num < lowest:
            lowest = num
    return lowest

def Highest(numbers):
    highest = None
    for num in numbers:
        if highest == None or num > highest :
            highest = num
    return highest

def Total(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def Average(numbers, total):
    count = 0
    average = 0
    for num in numbers:
        count += 1
    average = total / count
    return average

def Display(numbers, lowest, highest, total, average):
    count = 0
    print()
    print('============== Results ============')
    for num in numbers:
        count += 1
        print(str(count) + '. ' + str(num))
    print()
    print('Lowest Number:', lowest)
    print('Highest Number:', highest)
    print('Total:', total)
    print('Average:', average)

main()

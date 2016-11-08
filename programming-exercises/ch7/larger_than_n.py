# Larger Than n
# In a program, write a function that accepts two arguments:
# a list and a number, n. Assume that the list contains numbers.
# The function should display all of the numbers in the list that
# are greater than the number n.
import random

def main():
    numbers = Numbers()
    user_num = UserNum()
    Compare(numbers, user_num)

def Numbers():
    numbers = []
    for x in range(20):
        number = random.randint(1, 100)
        numbers.append(number)
    return numbers

def UserNum():
    number = float(input('Choose between 1-100 to compare to a list of 20 random numbers. '))
    while number <= 0 or number > 100:
        number = float(input('Please choose a number between 1-100 '))
    return number

def Compare(numbers, user_num):
    greater_than =   []
    smaller_than =  []
    equal_to =      []
    count = 0
    
    for num in numbers:
        if num < user_num:
            smaller_than.append(num)
        elif num > user_num:
            greater_than.append(num)
        else:
            equal_to.append(num)
    print()
    print('====== Random Numbers Smaller Than Your Number =====')
    for num in smaller_than:
        count += 1
        print(str(count) + '. ' + str(num))
    print()
    print('====== Random Numbers Greater Than Your Number =====')
    for num in greater_than:
        count += 1
        print(str(count) + '. ' + str(num))
    print()
    print('====== Random Numbers Equal To Your Number =====')
    for num in equal_to:
        count += 1
        print(str(count) + '. ' + str(num))
main()

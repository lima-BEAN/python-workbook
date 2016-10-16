# Maximum of Two Values
# Write a function named max that accepts two integer values
# as arguments and returns the value that is the greater of
# the two. For example, if 7 and 12 are passed as arguments
# to the function, the function should return 12. Use the function
# in a program that prompts the user to enter two integer values.
# the program should display the value that is the greater of the two.

def main():

    Greeting()

    integer_a = IntegerA()
    integer_b = IntegerB()
    compare_integer = CompareInteger(integer_a, integer_b)
    
    Results(integer_a, integer_b, compare_integer)


def Greeting():
    print()
    print('=============== Max of Two ==================')
    print()

def IntegerA():
    a = float(input('Pick a number: '))
    return a

def IntegerB():
    b = float(input('Pick a number: '))
    return b

def CompareInteger(a, b):
    if a > b:
        return a
    elif a < b:
        return b

def Results(a, b, max_num):
    print()
    print('=============== Results =====================')

    if a == max_num:
        print(max_num, 'is bigger than', b)
    elif b == max_num:
        print(max_num, 'is bigger than', a)

main()

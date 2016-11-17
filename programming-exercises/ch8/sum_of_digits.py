# Sum of Digits in a String
# Write a program that asks the user to enter a series of single-digit
# numbers with nothing separating them. The program should display
# the sum of all the single digit numbers in the string.
# Ex: 2514, should return 12.

def main():
    string_digit    = StringDigit()
    sum_digits      = SumDigits(string_digit)
    Results(sum_digits)

def StringDigit():
    string = input('Enter a series of single digits with no spaces: ')
    return string

def SumDigits(string_digit):
    sum = 0
    for ch in string_digit:
        sum += int(ch)
    return sum

def Results(sum_digits):
    print('The sum of your series is:', sum_digits)

main()

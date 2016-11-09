# Write a loop that counts the number of digits that appear in the string
# reference by mystring.

def main():
    my_string = input('Write a sentence: ')
    CountDigits(my_string)

def CountDigits(string):
    count = 0
    for ch in string:
        if ch.isdigit():
            count += 1
    print('The digit count is:', count)

main()

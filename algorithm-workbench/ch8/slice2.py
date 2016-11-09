# Assume mystring references a string. Write a statement that uses a slicing
# expression and displays the last 3 characters in the string.

def main():
    string = input('Enter a sentence: ')
    new_string = string[-3:]
    print('New:', string)
    print('Old:', new_string)

main()

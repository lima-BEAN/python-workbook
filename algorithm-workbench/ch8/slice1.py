# Assume mystring references a string. Write a statement that uses a
# slicing expression and displays the first 3 characters in the string.

def main():
    string = input('Enter a sentence: ')
    new_string = string[:3]
    print('Old:', string)
    print('New:', new_string)

main()

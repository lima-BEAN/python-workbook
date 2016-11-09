# Write a function that accepts a string as an argument and displays
# the string backwords.

def main():
    string = input('Enter a sentence: ')
    new_string = string[::-1]
    print('Old string:', string)
    print('New string:', new_string)

main()

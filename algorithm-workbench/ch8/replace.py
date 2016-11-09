# Write code that makes a copy of a string with all occurences of
# the lowercase letter 't' converted to uppercase.

def main():
    string = input('Enter a sentence with at least 1 character \'t\': ')
    new_string = string.replace('t', 'T')
    print('Old string:', string)
    print('New string:', new_string)

main()

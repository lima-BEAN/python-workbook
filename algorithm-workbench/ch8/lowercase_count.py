# Write a loop that counts the number of lowercase characters that appear
# in the string referenced by mystring

def main():
    my_string = input('Enter a sentence: ')
    CountLower(my_string)

def CountLower(string):
    count = 0
    for ch in string:
        if ch.islower():
            count += 1
    print('Lowercase character count:', count)

main()

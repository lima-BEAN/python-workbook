# Write a loop that counts the number of space characters that appear
# in the string referenced mystring

def main():
    my_string = input('Write a sentence: ')
    Count(my_string)

def Count(string):
    count = 0
    for ch in string:
        if ch == ' ':
            count += 1
    print('There are', count, 'spaces in your sentence')

main()

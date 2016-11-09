# Write a statement that splits this string:
# mystring = 'cookies>milk>fudge>cake>ice cream'

def main():
    my_string = 'cookies>milk>fudge>cake>ice cream'
    string = my_string.split('>')
    print('Old:', my_string)
    print('New:', string)

main()

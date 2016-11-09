# Write a function that accepts a string as an argument and returns
# true if the argument ends with the substring '.com'. Otherwise, the
# function should return false.
substring = '.com'
def main():
    string = input('Enter a domain name with extension (.com, .net, .org, etc.): ')
    com_check = ComCheck(string)
    Results(com_check)

def ComCheck(string):
    if string.endswith(substring):
        return True
    else:
        return False

def Results(check):
    if check == True:
        print('Awesome. You have a .com domain extension')
    else:
        print('Sorry, you don\'t have a .com')

main()

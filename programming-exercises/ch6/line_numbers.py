# Write a program that asks the user for the name of a file.
# The program should display the contents of the file with
# each line preceded with a line number followed by a colon.
# The line numbering should start at 1.

def main():
    user_file = UserFile()
    Read(user_file)

def UserFile():
    file = input('What file would you like to open? (include .txt): ')
    return file

def Read(file):
    count = 1
    read_file = open(file, 'r')
    for x in read_file:
        content = x.rstrip()
        print(str(count) + ': ' + str(content))
        count += 1

main()

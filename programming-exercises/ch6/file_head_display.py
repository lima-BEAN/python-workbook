# Write a program that asks the user for the name of a file.
# The program should display only the first five lines of the
# file's contents. IF the file contains less than five lines,
# it should display the file's entire contents.

def main():
    user_file = UserFile()
    Read(user_file)

def UserFile():
    file = input('Name of file you want to read (include .txt extension): ')
    return file

def Read(file):
    read_file = open(file, 'r')
    for x in range(5):
        content = read_file.readline().rstrip()
        print(content)

main()

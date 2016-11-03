# Assume that a file containing a series of integers is named
# numbers.txt and exists on the computers disk. Write a program
# that displays all of the numbers in the file.

def main():
    Write()
    Read()

def Write():
    file = open('numbers.txt', 'w')

    for x in range(1, 11):
        file.write(str(x**2))
        file.write('\n')

def Read():
    file = open('numbers.txt', 'r')
    content = file.read()
    print(content)

main()

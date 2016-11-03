# Assume that a file containing a series of names (as strings) is named
# names.txt and exists on the computer's disk. Write a program that
# displays the number of names that are stored in the file.
# (Hint: Open the file and read every string stored in it. Use a
# variable to keep a count of the number of items that are read from the file.)

def main():
    Write()
    name_count = Read()
    Display(name_count)

def Write():
    file = open('names.txt', 'w')
    for x in range(10):
        file.write('lima-BEAN ' + str(x+1) + '\n')

def Read():
    count = 0
    file = open('names.txt', 'r')
    for line in file:
        count += 1
    return count

def Display(count):
    print('There are', count, 'names in the names.txt file')
    
main()

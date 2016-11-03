# This exercise assumes you have completed writing random numbers to a file.
# Write another program that reads the random numbers from the file, display
# the numbers and then displays the following data:
#   The total of the numbers
#   The number of random numbers read from the file

def main():
    Read()

def Read():
    count = 0
    total = 0
    file = open('num_of_randoms.txt', 'r')
    for line in file:
        number = line.rstrip()
        total += int(number)
        count += 1
    print('The sum of the random numbers: ' + str(total))
    print('The total amount of numbers read in .txt file: ' + str(count))

main()

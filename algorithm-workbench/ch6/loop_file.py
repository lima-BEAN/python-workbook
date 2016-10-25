# Write code that does the following:
# opens an output file, number_list.txt,
# uses a loop to write the numbers 1 through 100 to the file, then close file

def main():

    NumberList()

def NumberList():

    file = open('number_list.txt' ,'w')

    for x in range(1, 101):
        file.write(str(x) + '\n')
##        file.write('\n')

    file.close()

main()

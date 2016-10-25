# Write a program that opens an output file with the filename my_name.txt,
# writes your name to file and then closes the file.

def main():

    File()

def File():

    file = open('my_name.txt', 'w')
    file.write('lima-BEAN\n')
    file.close()

main()

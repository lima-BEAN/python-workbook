# Write code that opens an output file, number_list.tx,
# but does not erase the file's contents if it already exists.

def main():

    file = open('number_list.txt', 'a')

    file.close()

main()

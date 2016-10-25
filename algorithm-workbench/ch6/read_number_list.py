# Write code that does the following:
# Open number_list.txt, read all numbers from file and display. Then close file

def main():

    ReadNumbers()

def ReadNumbers():

    file = open('number_list.txt', 'r')

    content = file.readline()

    while content != '':

        print(content)
        content = file.readline()

main()

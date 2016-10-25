# Write a program that opens the my_name.txt, reads name from file,
# and then closes file.

def main():

    Read()

def Read():

    file = open('my_name.txt', 'r')
    content = file.read()
    file.close

    print(content)

main()

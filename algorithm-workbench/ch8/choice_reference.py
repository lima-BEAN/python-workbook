# Assume chouse references a string. The following if statement determines
# whether choice is equal to 'Y' or 'y':
# if choice == 'Y' or choice == 'y':
# rewrite this statement so it only makes one comparison and does
# not use the or operator.

def main():
    choice = input('Make your choice. (y/n) ')
    if choice.lower() == 'y':
        print('Yes. The choice is yours.')
    else:
        print('Whatever')

main()

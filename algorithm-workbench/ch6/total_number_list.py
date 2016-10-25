# read numer_list.txt file and add numbers up. display total

def main():

    AddNumbers()

def AddNumbers():

    total = 0
    
    file = open('number_list.txt', 'r')

    for line in file:
        line = line.rstrip('\n')
        amount = float(line)
        total += amount

    print(total)

main()

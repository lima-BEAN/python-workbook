# Assume each of the variables set1 and set2 references a set.
# Write code that creates another set containing only the elements
# that are found in both set1 and set2 and assigns the resulting
# set to the variable set3

import random

def main():
    set1 = Set()
    set2 = Set()
    set3 = InterSet(set1, set2)
    Results(set1, set2, set3)

def Set():
    my_set = set()
    rand_num = int
    for x in range(10):
        rand_num = random.randint(1,100)
        my_set.add(rand_num)
    return my_set

def InterSet(set1, set2):
    my_set = set()
    my_set = set1.intersection(set2)
    return my_set

def Results(set1, set2, set3):
    print('Set 1:', set1)
    print('Set 2:', set2)
    print('Set 3:', set3)

main()

# Assume the variable dct references a dictionary. Write an if statement
# that determines whether the key 'Jim' exists in the dictionary. If so,
# delete 'Jim' and its associated value

def main():
    dct = {'Jay':'Ford', 'Jerry': 'Chevy', 'Jim': 'Chrysler'}
    if 'Jim' in dct:
        popped_item = dct.pop('Jim')
        print('This was popped from dictionary ->', popped_item)
    else:
        print('Jim is not in dictionary')
    print(dct)

main()

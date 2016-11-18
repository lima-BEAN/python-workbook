# Assume the variable dct references a dictionary. Write an if statement that
# determines whether the key 'James' exists in the dictionary. If so,
# display the value that is associated with that key. If the key is not
# in the dictionary, display a message indicating so.

def main():
    dct = {'Francis': 1, 'Noah': 2, 'James': 3}
    if 'James' in dct:
        print('James value is', dct['James'])
    else:
        print('Not in dictionary')
        
main()

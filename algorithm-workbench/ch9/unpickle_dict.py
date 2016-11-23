# Write code that retrieves and unpickles the dictionary that was
# pickled in pickled_dict.py
# Steps to unpickle
# 1. Open file for binary reading
# 2. Call pickle module's load function to retrieve an object from a
#    file and unpickle it
# 3. After you unpickled all objects you want from file, close file

import pickle

def main():
    in_file = open('mydata.dat', 'rb')
    content = pickle.load(in_file)
    in_file.close()

    print(content)

main()

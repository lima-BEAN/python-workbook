# Assume the variable dict references a dictionary. Write code that pickles
# the dictionary and saves it to a file named mydata.dat
# Steps to pickle object:
# 1. Open a file for binary writing
# 2. Call the pickle module's dump method to pickle the obj and write to
#    specified file
# 3. After all objects are pickled and saved to file, close file

import pickle

def main():
    dct = {'Java':'Good', 'C#':'Better', 'Python':'Best'}
    out_file = open('mydata.dat', 'wb')
    pickle.dump(dct, out_file)
    out_file.close()

main()

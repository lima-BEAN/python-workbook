# Write a class definition named Book. The Book class should have data
# attributes for book's title, the author's name, and the publisher's name
# The class should also have the following:

# a. An __init__ method for the class. The method should accept an argument
#    for each of the data attributes.
# b. Accessor and Mutator methods for each data attribute
# c. An __str__ method that returns a string indicating the state of the obj.

import book

def main():
    my_book = book.Book('Harry Potter', 'J. K. Rowling', 'Hogwartz')
    print(my_book)
    
main()

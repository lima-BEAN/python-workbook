# Suppose my_car is the name of a variable that references an object, and
# go is the name of a method. Write a statement that uses the my_car
# variable to call the go method.
# (You do not have to pass any arguments to the go method)

class Car:

    def __init__(self, make, model, year, mpg):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mpg = mpg

    # Mutators (setters)
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_mpg(self, mpg):
        self.__mpg = mpg

    # Accessors (getters)
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mpg(self):
        return self.__mpg

    # Methods
    def Go(self):
       return 'You are going fast'

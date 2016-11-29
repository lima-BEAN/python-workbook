# Write a class named Car that has the following data attributes
# __year_model
# __make
# __speed
#
# The Car class should have an __init__ method that accepts the car's year
# model and make as arguments. These values should be assigned to the obj's
# __year_model and __make data attributes. It should also assigns 0 to the
# __speed data attribute.
#
# The class should also have the following methods:
# accelerate - Should add 5 to the speed data attribute each time it's called
# brake - Should subtract 5 from the speed data attribute each time it's called
# get_speed - Should return the current speed
#


class Car:

    # Initializers
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    # Mutators (setters)
    def set_year_model(self, year):
        self.__year_model = year

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = speed

    # Accessors (getters)
    def get_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    # Methods
    def Accelerate(self):
        self.__speed += 5

    def Brake(self):
        self.__speed -= 5

    def GetSpeed(self):
        print('Your current speed is ', self.__speed, 'mph')

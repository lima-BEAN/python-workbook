# Write a class named RetailItem that holds data about an item in a retail
# store. The class should store the following data in attributes:
# item description, units in inventory, and price.
#


class RetailItem:

    def __init__(self, desc, inventory, price):
        self.__desc = desc
        self.__inventory = inventory
        self.__price = price

    # Mutators (setters)
    def set_desc(self, desc):
        self.__desc = desc

    def set_inventory(self, inventory):
        self.__inventory = inventory

    def set_price(self, price):
        self.__price = price

    # Accessors
    def get_desc(self):
        return self.__desc

    def get_inventory(self):
        return self.__inventory

    def get_price(self):
        return self.__price

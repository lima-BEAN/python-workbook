# Exercise assumes you've created a RetailItem class.
# Create a CashRegister class that can be used with the
# RetailItem class. The CashRegister class should be able
# to internally keep a list of RetailItem objects. The
# class should have the following methods:
#
# purchase_item method that accepts a RetailItem obj as an argument.
# Each time the method is called, the RetailItem obj that is passed
# as an argument should be added to the list
#
# get_total method returns the total price of all the RetailItem objs.
# stored in the CashRegister objs internal list
#
# show_items method that displays data about the RetailItem objs stored
# in the CashRegister objs internal list.
#
# clear method that should clear the CashRegister objs internal list.
#

retail_list = list

class CashRegister:

    def __init__(self, item):
        self.__item = item

    def set_item(self, item):
        self.__item = item

    def get_item(self):
        return self.__item
    
    def purchase_item(item):
        retail_list.append(list(item))

    def get_total():
        total = 0
        for item in retail_list:
            total += item.get_price()
        return total

    def show_items():
        for item in retail_list:
            print('\nDesc:', item.get_desc(),
                  '\nCount:', item.get_inventory(),
                  '\nPrice:', item.get_price())

    def clear(self):
        del retail_list[:]

# Demonstrate the CashRegister class in a program that allows the user to
# select several items for purchase. When the user is ready to check
# out, the program should display a list of all the items he/she has
# selected for a purchase, as well as total price.

import retail_item
import cash_register

def main():
    add = input('Would you like to add an item to your cart? (y/n) ')
    while add == 'Y' or add == 'y':
        AddItem()
        add = input('Would you like to add another item? (y/n) ')
    Total()
    Show()

def AddItem():
    desc = input('What item would you like? ')
    inv = input('How many ' + desc + ' would you like? ')
    price = input('What is the price of that item? ')
    new_item = retail_item.RetailItem(desc, inv, price)
    cash_register.CashRegister.purchase_item(new_item)

def Total():
    print('The total amount for the items is:',
          cash_register.CashRegister.get_total())

def Show():
    print('Items purchased:')
    cash_register.CashRegister.show_items()

main()

# Once you have written the class, write a program that creates three
# RetailItem objects
import retail_item

def main():

    item1 = retail_item.RetailItem('Jacket', 12, 59.95)
    item2 = retail_item.RetailItem('Jeans', 40, 34.95)
    item3 = retail_item.RetailItem('Shirt', 20, 24.95)
    print()
    print('\t\tDescription\t\tUnits\t\tPrice')
    print('==============================================================')
    print('Item #1:\t', item1.get_desc(), '\t\t', item1.get_inventory(),
          '\t\t', item1.get_price())
    print('Item #2:\t', item2.get_desc(), '\t\t\t', item2.get_inventory(),
          '\t\t', item1.get_price())
    print('Item #3:\t', item3.get_desc(), '\t\t\t', item3.get_inventory(),
          '\t\t', item3.get_price())
    print('==============================================================')

    
main()

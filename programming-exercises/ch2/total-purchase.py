## A customer in a store is purchasing five items. Write a program that asks
## for the price of each item, and then displays the subtotal of the sale,
## the amount of sales tax, and the total.
## Assume the sales tax is 7 percent.


tax_percent = .07

x = 1

while x < 6:
    subtotal = int(input("What is the price for item " + str(x) + ": "))
    sales_tax = subtotal * tax_percent
    total = subtotal + sales_tax
    print("Item" + str(x) + "'s subtotal is $" + str(format(subtotal, ',.2f')), 
          "\n\tsales tax is $" + str(format(sales_tax, ',.2f')),
          "and the \n\ttotal amount is $" + str(format(total, ',.2f')))
    print("===================================")
    x += 1

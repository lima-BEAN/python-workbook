## Write a program that calculates the total amount of a meal purchased at
## a restaurant. The program should ask the user to enter the charge for the
## food, and then calculate the amount of a 18 percent tip and 7 percent
## sales tax. Display each of these amounts and the total

subtotal = int(input("What is your subtotal for your meal? "))
tip = subtotal * 0.18
sales_tax = subtotal * .07
total = subtotal + tip + sales_tax

print("Subtotal:", format(subtotal, ',.2f'),
      "\nSales tax:", format(sales_tax, '.2f'),
      "\nTip:", format(tip, '.2f'),
      "\nTotal:", format(total, '.2f'))

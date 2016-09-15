## Write a program that will ask the user to enter the amount
## of a purchase. The program should then compute the state and county sales
## tax. Assume the state sales tax is 5 percent and the county sales tax is 2.5
## percent. The program should display the amount of the purchase, the state
## sales tax, the county sales tax, the total sales tax, and the total of the
## sale (which is the sum of the amount of purchase plus the total sales tax)

purchase_amount = int(input("What is the purchasing amount? "))
state_tax = 0.05
county_tax = 0.025
total_tax = state_tax + county_tax
total_sale = format(purchase_amount + (purchase_amount * total_tax), '.2f')

print("The purchase amount for the item is $" + str(purchase_amount),
      "\n\tState tax:", format((state_tax * purchase_amount), '.2f'),
      "\n\tCounty tax:", format((county_tax * purchase_amount), '.2f'),
      "\n\tTotal tax:", format((total_tax * purchase_amount), '.2f'),
      "\n\tTotal sale amount is $" + str(total_sale))




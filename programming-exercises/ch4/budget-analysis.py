# Write a program that asks the user to enter the amount that he or she
# has budgeted for a month. A loop should then prompt the user to enter
# each of his or her expeneses for the month and keep a running total.
# When the loop finishes, the program should display the amount
# that the user is over or under budget

budget_amount = float(input("What is your budget amount? "))
expenses_amount = 0
item = 0
expense = 1

while expense != 0:
    item += 1
    expense = float(input("Enter expense amount for item " + str(item) +
                          '\nOr 0 if there are no more expense items '))
    expenses_amount += expense

over_under = budget_amount - expenses_amount


print("Your budget amount:", format(budget_amount, ',.2f'),
      "\nYour expenses amount:", format(expenses_amount, ',.2f'),
      "\nOver/Under Analysis:", format(over_under, ',.2f'))
    

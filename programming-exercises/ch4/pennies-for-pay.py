# Write a program that calculates the amount of money a person would earn
# over a period of time if his or her salary is one penny the first day,
# two pennies the second day, and continues to double each day.
# The program should ask the user for the number of days.
# Display a table showing what the salary was for each day, and then show the
# total pay at the end of the period. The output should be displayed in a
# dollar amount, not the number of pennies.



days = int(input('How many days would you like to work here? '))
print('Day\tSalary in $')
print('--------------------')

for day in range(1, (days+1)):
    if day >= 1:
        if day == 1:
            penny_pay = 1
        elif day == 2:
            penny_pay = 2
        else:
            penny_pay *= 2
        dollar_pay = penny_pay / 100
    print(day, '\t', format(dollar_pay, ',.2f'))
    


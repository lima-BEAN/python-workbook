# Create a change-counting game that gets the user to enter the number of coins
# required to make exactly one dollar. The program should prompt the user
# to enter the number of pennies, nickels, dimes and quarters. If the total
# value of the coins entered is equal to one dollar, the program should
# congratulate the user for winning the game. Otherwise, the program should
# display a message indicating whether the amount entered was more or less
# than one dollar

# Get user input for total counts of each set
penny_count = int(input("How many pennies do you have? "))
nickel_count = int(input("How many nickels do you have? "))
dime_count = int(input("How many dimes do you have? "))
quarter_count = int(input("How many quarters do you have? "))

# Convert counts to respective currency amount
penny_amount = penny_count * 0.01
nickel_amount = nickel_count * 0.05
dime_amount = dime_count * 0.10
quarter_amount = quarter_count * 0.25

# Get total amount collected
total_amount = penny_amount + nickel_amount + dime_amount + quarter_amount

if total_amount == 1.00:
    print("Hooray! You collected $" + str(format(total_amount, '.2f')))
else:
    if total_amount > 1.00:
        print("You collected $" + str(format(total_amount, '.2f')) +
              "\nWhich is more than $1.00")
    else:
        print("You collected $" + str(format(total_amount, '.2f')) +
              "\nWhich is less than $1.00")


# Write a program that asks the user for a number in the range of 1 through 7
# The program should display the corresponding day of the week,
# where 1 = Monday, 2 = Tuesday, etc..
# The program should display an error message if the user enters a number that
# is outside the range of 1 through 7

day = int(input("Pick a number (1-7) to choose the day of the week." +
                "\n1 = Monday, 2 = Tuesday, etc.: "))

if day == 1:
    print("You chose Monday")
elif day == 2:
    print("You chose Tuesday")
elif day == 3:
    print("You chose Wednesday")
elif day == 4:
    print("You chose Thursday")
elif day == 5:
    print("You chose Friday")
elif day == 6:
    print("You chose Saturday")
elif day == 7:
    print("You chose Sunday")
else:
    print("Choose a number within 1-7")

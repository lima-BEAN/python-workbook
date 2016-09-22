# Write a program that prompts the user to enter a number within the range of 1
# through 10. The program should display the Roman numeral version of that
# number. If the number is outside the range of 1 through 10,
# the program should display an error message.

number = int(input("What number do you want to convert to Roman Numeral? (1-10) "))

if number == 1:
    print(number, "is converted to I")
elif number == 2:
    print(number, "is converted to II")
elif number == 3:
    print(number, "is converted to III")
elif number == 4:
    print(number, "is converted to IV")
elif number == 5:
    print(number, "is converted to V")
elif number == 6:
    print(number, "is converted to VI")
elif number == 7:
    print(number, "is converted to VII")
elif number == 8:
    print(number, "is converted to VIII")
elif number == 9:
    print(number, "is converted to IX")
elif number == 10:
    print(number, "is converted to X")
else:
    print("Choose a number between 1 and 10")

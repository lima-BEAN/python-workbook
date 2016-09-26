# Write code that prompts the user to enter a number in the range
# of 1 through 100 and validates the input

valid = int(input("Enter a number between 1 - 100: "))

while valid >= 1 and valid <= 100:
    print("Great Job. You chose:", valid)
    valid = int(input("Input another value between 1 - 100: "))

print("Thanks for trying")

# Write code that prompts the user to enter a positive nonzero number and
# validates the input

validate = int(input("Enter a number greater than 0: "))

while validate > 0:
    print("Awesome! You entered:", validate)
    validate = int(input("Input anohter number greater than 0: "))

print("Thanks for playing")

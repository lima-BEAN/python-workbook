# Write an if-else statement that assigns 0 to the variable b
# if the variable a is less than 10.
# otherwise, it should assign 99 to variable b

# Ask user input for a
a = int(input("Choose a value for a: "))
# Initialize b
b = int


if a < 10:
    b = 0
else:
    b = 99

print("\nValue for a:", a,
      "\nValue for b:", b)

# Write an if statement that assigns 20 to the variable y
# and assigns 40 to the variable z if the variable x
# is greater than 100

# Ask user input for x
x = int(input("What is your x value? "))
# initialize y and z
y = 0
z = 0

if x > 100:
    y = 20
    z = 40

print("\nYour x-value:", x,
      "\nYou y-value:", y,
      "\nYour z-value:", z)

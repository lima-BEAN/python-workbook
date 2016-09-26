# Write a while loop that asks the user to enter two numbers.
# The numbers should be added and the sum displayed. The loop
# should ask the user if he or she wishes to perform the operation
# again. If so, the loop should repeat, otherwise it should terminate

keep_going = 'y'

while keep_going.lower() == 'y':
    num1 = int(input("Pick a number: "))
    num2 = int(input("Pick another number: "))
    total = num1 + num2
    print(num1, "+", num2, "=", total)
    keep_going = input("Would you like to add another set of numbers? (y/n) ")


    

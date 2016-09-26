# Write a program with a loop that asks the user to enter a series
# of positive numbers. The user should enter a negative number to
# signal the end of the series. After all positive numbers have
# been entered, the program should display their sum

number = 0
total = 0

while number >= 0:
    number = int(input("Enter a positive number to figure out sums. " +
                 "Enter negative number to exit "))
    if number >= 0:
        total += number
    

print('Your total sum', total)

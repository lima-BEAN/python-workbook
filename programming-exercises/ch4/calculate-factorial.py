# In mathematics, the notation n! represents the factorial of the nonnegative
# integer n. The factorial of n is the product of all the nonnegative integers
# from 1 to n. Example: 4! = 1 x 2 x 3 x 4 = 24

# Write a program that lets the user enter a nonnegative integer and then
# uses a loop to calculate the factorial of that number Display the factorial

factorial = int(input('Enter a positive number to find out factorial: ' +
                      'negative number to exit '))
product = 1

while factorial >= 0:
    for number in range(1, (factorial + 1)):
        product *= number
    print('The factorial of', factorial, 'is', product)
    factorial = int(input('Enter a positive number to find out factorial: ' +
                      'negative number to exit '))

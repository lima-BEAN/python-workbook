# A prime number is a number that is only evenly divisble by itself and 1.
# Write a Boolean function named is_prime which takes an integer as an
# argument and returns true or false whether integer is prime or not.
# Use the function in a program that prompts the user to enter a number and
# then displays a message indicating whether the number is primce

def main():

    number = Number()
    is_prime = IsPrime(number)

    Results(number, is_prime)

def Number():
    num = int(input('Choose a positive integer to see if it\'s prime or not. '))
    return num

def IsPrime(number):
    is_prime = bool
    
    for num in range(1, number+1):
        if (num != number and num != 1):
            if (number % num) == 0:
                is_prime = False
        elif ((num == number or num == 1) and is_prime != False):
            is_prime = True
            
    return is_prime

def Results(num, prime):
    print()

    if prime == True:
        print(num, 'is a prime number')
    elif prime == False:
        print(num, 'is not a prime number')

main()

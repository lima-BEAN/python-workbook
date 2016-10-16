# One foot equals 12 inches. Write a function named feet_to_inches that
# accepts a number of feet as an argument and returns the number of inches
# in that many feet. Use the function in a program that prompts the user to
# enter a number of feet and then displays the number of inches in that many
# feet.

FOOT_TO_INCHES = 12

def main():

    Greeting()

    feet = Feet()
    inches = FeetToInches(feet)

    Summary(feet, inches)

def Greeting():
    print()
    print('============ Feet to Inches Coverter =============')

def Feet():
    print()
    feet = float(input('How many feet do you want to convert to inches? '))
    return feet

def FeetToInches(feet):
    return feet * FOOT_TO_INCHES

def Summary(ft, inch):
    print()
    print('============ Feet to Inches Summary ==============')
    print('Feet:', ft, 'ft', '\nInches:', inch, 'in')

main()

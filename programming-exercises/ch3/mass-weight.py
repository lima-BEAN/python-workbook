# Scientists measure an object's mass in kilograms and its weight in newtons.
# If you know the amount of mass of an object in kilograms, you can calculate
# its weight in newtons with the following formula:
# weight = mass * 9.8
# Write a program that asks the user to enter an object's mass and then
# calculates its weight. If the object weighs more than 500 newtons,
# display a message indicating that it is too heavy.
# if the object weighs less than 100 newtons, indicate it's too light

mass = float(input('Enter object\'s mass: '))
weight = mass * 9.8

if weight > 500:
    print('The object is to heavy at', format(weight, '.2f'), 'newtons')
elif weight < 100:
    print('The object is to light at', format(weight, '.2f'), 'newtons')
else:
    print('Perfect. Your object\'s weight is', format(weight, '.2f'))

    

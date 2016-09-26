# Write a program that predicts the approximate size of a population of organisms
# The application should use text boxes to allow the user to enter the starting
# number of organisms, the average daily population increase (as percentage),
# and the number of days the organisms will be left to multiply.

number_organisms = int(input("Starting number of organisms: "))
percent_increase = int(input('What is the daily increase (as percenetage): '))
days_to_multiple = int(input('How many days to multiple: '))


print('Day\tPopulation')
for day in range(1, (days_to_multiple+1)):
    if day > 1:
        number_organisms += (number_organisms * percent_increase)/100
    print(day, '\t', format(number_organisms, '.1f'))

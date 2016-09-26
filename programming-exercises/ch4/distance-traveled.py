# The distance a vehicle travels can be calculated as follows:
# distance = speed x time
# Write a program that asks the user for the speed of a vehicle (in mph)
# and the number of hours it has traveled. It should then use a loop
# to display the distance the vehicle has traveled for each hour of that
# time period.

speed = int(input('What is the speed of the vehicle in mph? '))
time = int(input('How many hours have you traveled? '))

print('Hour\tDistance traveled')
print('-----------------------')
for hour in range(1, (time+1)):
    distance = speed * hour
    print(hour, '\t', distance)
    

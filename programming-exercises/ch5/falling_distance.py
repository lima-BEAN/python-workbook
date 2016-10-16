# When an object is falling because of gravity, the following formula
# can be used to determine the distance the object falls in a specific
# time period:  d = 1/2 gt**2
# d = distance in meters
# g = gravity (9.8)
# t = time in seconds
# Write a function named falling_distance that accepts an object's
# falling time (in seconds) as an argument. The function should return
# the distance, in meters, that the object has fallen during that time interval
# Write a program that calls the function in a loop that passes the values 1
# through 10 as arguments and displays the return value.

G = 9.8

def main():

    times = []
    distances = []
    
    Greeting()
    
    for x in range(10):
        
        falling_time = FallingTime()
        time_squared = TimeSquared(falling_time)
        falling_distance = FallingDistance(time_squared)

        times.append(falling_time)
        distances.append(falling_distance)

    Results(times, distances)

def Greeting():
    print()
    print('================ Falling Distance ===================')
    print('Please input 10 time periods to show distance traveled for each')

def FallingTime():
    time = int(input('How many seconds of free fall? '))
    return time

def TimeSquared(time):
    time_squared = time**2
    return time_squared

def FallingDistance(t_sq):
    dist = (1/2) * G * t_sq
    return dist

def Results(times, distances):
    print()
    print('======= Time (seconds) ======== Distance (meters) =======')
    for x in range(10):
        print('Time: ', times[x], '\t\t\t', 'Distance',
              format(distances[x], '.2f'))

main()
        

# The program has not been written what's been asked of it. Need to pass
# loop iterations as arguments to call function. Will review.

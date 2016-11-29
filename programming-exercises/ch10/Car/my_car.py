# Next, design a program that creates a Car object and then calls the
# accelerate method five times. After each call to the accelerate method,
# get the current speed of the car and display it. Then call the brake method
# 5 times. After each call to the brake method, get the current speed of the
# car and dislay it.
import car

def main():
    year = input('What is your car\'s year model? ')
    make = input('What is the car make? ')
    my_car = car.Car(year, make)

    for x in range(5):
        my_car.Accelerate()
        my_car.GetSpeed()

    for x in range(5):
        my_car.Brake()
        my_car.GetSpeed()
    
main()

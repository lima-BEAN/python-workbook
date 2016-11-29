# Suppose my_car is the name of a variable that references an object, and
# go is the name of a method. Write a statement that uses the my_car
# variable to call the go method.
# (You do not have to pass any arguments to the go method)
import car

def main():
    my_car = car.Car('Porsche', '911 twin turbo', 2012, 12)
    print('================ '+ my_car.Go() +' ====================')
    print('Make:', my_car.get_make(),
          '\nModel:', my_car.get_model(),
          '\nYear:', my_car.get_year(),
          '\nMPG:', my_car.get_mpg())
    print('=======================================================')
main()

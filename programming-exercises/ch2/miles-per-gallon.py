## A car's miles-per-gallon can be calculated with the following formula:
##    MPG = Miles driven Gallons of gas used
## Write a program that asks the user for the number of miles driven and the
## gallons of gas used. It should calculate the car's MPG and display the result

miles_driven = int(input("How many miles did you drive? "))
gallons_used = int(input("How many gallons of gas did you use? "))
mpg = miles_driven / gallons_used

print("Your miles per gallon is", mpg)

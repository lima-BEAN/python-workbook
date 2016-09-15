## Write a program that converts Celsius temperatures to Fahrenheit temperatures.
## The formula is as follows:
##   F = (9/5)C + 32
## The program should ask the user to enter a temperature in Celsius, and then
## display the temperature converted to Fahrenheit.

cel_temp = float(input("What is the Celsius temperature over there? "))
celsius_to_fahrenheit = ((9/5) * cel_temp) + 32

print("The celsius temp is:", format(cel_temp, '.1f'),
      "\nThe fahrenheit temp is:", format(celsius_to_fahrenheit, '.1f'))

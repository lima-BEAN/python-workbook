# Write a program that displays a table of the Celsius temperatures 0 through 20
# and their Fahrenheit equivalents. The formula for converting a temperature
# from Celsius to Fahrenheit is     F = (9/5)C + 32
# Your program must use a loop to display the table



print('Celsius\tFahrenheit')
print('-------------------')
for celsius in range(21):
    fahrenheit = ((9/5) * celsius) + 32
    print(celsius, '\t', format(fahrenheit, '.1f'))
    

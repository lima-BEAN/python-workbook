# Write a loop that calculates the total of the following series of numbers:
# 1/30 + 2/29 + 3/28 + .... + 30/1

total = 0

for x in range(1, 31):
    numerator = x
    for y in range(30, 0, -1):
        while numerator == x:
            denominator = y
            rational = x / y
            total += rational
            numerator += 1 
print(format(total, '.2f'))

        

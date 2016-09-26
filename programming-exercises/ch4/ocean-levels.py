# Assuming the ocean's level is currently rising at about 1.6 millimeters/yr,
# create an application that displays the number of millimeters that the ocean
# has risen each year for the next 25 years.

risen = 0

print('Year\tOcean level rise (per millimeter)')
print('---------------------------------------')

for year in range(1, 26):
    risen = year * 1.6
    print(year, '\t', format(risen, '.2f'))

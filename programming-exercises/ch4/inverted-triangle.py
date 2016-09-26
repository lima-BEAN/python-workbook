# Write a program that uses nested loops that draw an inverted triangle

base = 7

for y in range(base):
    for x in range(base, y, -1):
        print('*', end=' ')

    print()

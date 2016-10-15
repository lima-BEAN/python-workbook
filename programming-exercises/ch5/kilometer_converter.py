# Write a program that asks the user to enter a distance in kilometers
# and then converts that distance to miles.
# Conversion formula: mile = kilometers * 0.6214


def main():

    kilometers_ran = float(input('How many kilometers did you run? '))

    print('You ran', format(KilometerToMiles(kilometers_ran), '.2f'), 'miles.')

def KilometerToMiles(kilometer):
    return kilometer * 0.6214

main()

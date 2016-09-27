# The following statement calls a function named half, which returns a value
# that is half that of the argument. (Assume the number variable
# references a float value.) Write code for the function
# result = half(number)

def main():
    number = float(input('Choose a number to see some magic! '))
    result = half(number)
    print('Half of', number, 'is', result)

def half(num):
    return num / 2

main()

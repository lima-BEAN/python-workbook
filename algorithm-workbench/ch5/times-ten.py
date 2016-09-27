# Write a function name times_ten. The function should accept an argument
# and display the product of its argument multiplied times 10.

def main():
    num = int(input("What number would you like to multiply by 10? "))
    times_ten(num)

def times_ten(number):
    product = number * 10
    print(number, '* 10 =', product)

main()

# Write a while loop that lets the user enter a number. The number should be
# multiplied by 10, and the result assigned to a variable named product.
# The loop should iterate as long as product is less than 100

# initialize product
product = 0
multiple = 10

while product < 100:
    number = int(input("Pick a number to multiply by 10 and add to total: "))
    numProduct = number * multiple
    product += numProduct
    print("Product of", number, "*", multiple, "is", numProduct)

print("The total product is:", product)

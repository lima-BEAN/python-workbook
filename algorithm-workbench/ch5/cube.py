# A program contains the following function definition:
# def cube(num):
#   return num * num * num
#
# Write a statement that passes the value 4 to this function and assigns
# its return value to the variable result

def main():
    result = cube(4)
    print('4 cubed is', result)

def cube(num):
    return num * num * num

main()

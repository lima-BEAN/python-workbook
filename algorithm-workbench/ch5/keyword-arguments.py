# Look at the following functino definition
# def my_function(a, b, c):
#   d = (a + c) / b
#   print(d)
#
# a. write a statement that calls this function and uses keyword arguments
#    to pass 2 into a, 4 into b, and 6 into c
# b. What value will be displayed when the function call executes?

def main():
    print('You are going to input 3 values to see some magic!')
    first   = int(input('Enter first number: '))
    second  = int(input('Enter second number: '))
    third   = int(input('Enter third number: '))
    my_function(b = second, c = third, a = first)

def my_function(a, b, c):
    d = (a + c) / b
    print('(', a, '+', c, ')', '/', b, '=',  d)

main()

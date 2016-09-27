# Look at the following function header:
# def my_function(a, b, c):
# Now look at the following call to my_function
# my_function(3, 2, 1)
# When this call executes, what value will be assigned to a, b and c?

# since positional arguments => a = 3, b = 2, c = 1

def main():
    my_function(3, 2, 1)

def my_function(a, b, c):
    print('a:', a, 'b:', b, 'c:', c)

main()

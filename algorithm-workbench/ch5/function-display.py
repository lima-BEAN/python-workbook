# What will the following program display?
# def main():
#   x = 1
#   y = 3.4
#   print(x, y)                 1 3.4
#   change_us(x, y)             0 0
#   print(x, y)                 1 3.4 
#
# def change_us(a, b):
#   a = 0
#   b = 0
#   print(a, b)
#
# main()
#

def main():
    x = 1
    y = 3.4
    print(x, y)
    change_us(x, y)
    print(x, y)

def change_us(a, b):
    a = 0
    b = 0
    print(a, b)

main()

# Write code to create a set with the following integers as members:
# 10, 20, 30 and 40.

def main():
    new_set = set()
    x = 0
    while x <= 40:
        if x % 10 == 0 and x != 0:
            new_set.add(x)
        x += 1
    print(new_set)
    
main()

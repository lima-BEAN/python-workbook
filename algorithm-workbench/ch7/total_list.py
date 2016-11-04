# Write a function that accepts a list as an argument (assume the list
# contains integers) and returns the total of the values in the list.

def main():
    nums = [x**2 for x in range(1, 11)]
    Total(nums)

def Total(nums):
    total = 0
    for num in nums:
        total += num
    print('The sum of squares up to 10 is: ' + str(total))

main()

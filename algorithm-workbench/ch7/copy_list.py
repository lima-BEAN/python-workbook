# Assume the list numbers1 has 100 elements and numbers2 is an empty list.
# Write code that copies the values in numbers1 to numbers2.

def main():
    numbers1 = Numbers1()
    numbers2 = Numbers2(numbers1)
    Compare(numbers1, numbers2)

def Numbers1():
    numbers = [x**4 for x in range(10)]
    return numbers

def Numbers2(numbers1):
    numbers2 = []
    for number in numbers1:
        numbers2.append(number)
    return numbers2

def Compare(nums1, nums2):
    print()
    print('Num1 List \t Num2 List')
    print('=====================================')
    for num1 in nums1:
        for num2 in nums2:
            if num1 == num2:
                print(str(num1) + '\t =\t '+ str(num2))

main()

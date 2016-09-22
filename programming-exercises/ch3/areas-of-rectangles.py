# The area of a rectangle is the rectangle's length times its width
# Write a program that asks for the length and width of two rectangles
# The program should tell the user which rectangle has the greater area, or
# if the areas are the same.

length1 = int(input("What is the length of the rectangle1? "))
width1 = int(input("What is the width of the rectangle1? "))
area1 = length1 * width1

length2 = int(input("What is the length of the rectangle2? "))
width2 = int(input("What is the width of the rectangle2? "))
area2 = length2 * width2


if area1 != area2:
    if area1 > area2:
        print("Rectangle1 with area:", area1,
              "is greater than Rectangle2's area:", area2)
    else:
        print("Rectangle1 with area:", area1,
              "is less than Rectangle2's area:", area2)
else:
    print("Area1:", area1, "is EQUAL to Area2:", area2)

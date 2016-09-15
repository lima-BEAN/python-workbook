## One acre of land is equivalent to 43,560 square feet. Write a program
## that asks the user to enter the total square feet in a tract of land and
## calculates the number of acres in the tract.
## HINT: Divide the amount entered by 43,560 to get the number of acres.

total_square_feet = int(input("Enter the total square feet: "))
acre = 43560
total_acreage = total_square_feet / acre

print("You have", format(total_acreage, ',.2f'), "acres")

# A software company sells a package that retails for $99.
# Quantity discounts are given according to the following table:
# Quantity: 10-19   =>  Discount: 10%
# Quantity: 20-49   =>  Discount: 20%
# Quantity: 50-99   =>  Discount: 30%
# Quantity: 100+   =>  Discount: 40%

# Write a program that asks the user to enter the number of packages purchased
# The program should then display the amount of the discount (if any) and the
# total amount of the purchase after the discount.

# Initialize regular cost per package
cost_per_package = 99
# Get number of packages
packages_purchased = int(input("How many packages did you purchase? "))
# get total cost
total_cost = cost_per_package * packages_purchased


if packages_purchased >= 10 and packages_purchased <= 19:
    percent_off = 0.10
    discount = total_cost * percent_off
    discounted_cost = total_cost - discount
    print("\nAmount after discount $" + format(discounted_cost, '.2f') +
          "\nAmount of discount $" + format(discount, '.2f') +
          "\nDiscount percent " + format(percent_off, '.0%'))
elif packages_purchased >= 20 and packages_purchased <= 49:
        percent_off = 0.20
        discount = total_cost * percent_off
        discounted_cost = total_cost - discount
        print("\nAmount after discount $" + format(discounted_cost, '.2f') +
              "\nAmount of discount $" + format(discount, '.2f') +
              "\nDiscount percent " + format(percent_off, '.0%'))
elif packages_purchased >= 50 and packages_purchased <= 99:
        percent_off = 0.30
        discount = total_cost * percent_off
        discounted_cost = total_cost - discount
        print("\nAmount after discount $" + format(discounted_cost, '.2f') +
              "\nAmount of discount $" + format(discount, '.2f') +
              "\nDiscount percent " + format(percent_off, '.0%'))
elif packages_purchased >= 100:
        percent_off = 0.40
        discount = total_cost * percent_off
        discounted_cost = total_cost - discount
        print("\nAmount after discount $" + format(discounted_cost, '.2f') +
              "\nAmount of discount $" + format(discount, '.2f') +
              "\nDiscount percent " + format(percent_off, '.0%'))
else:
    print("You need to purchase at least 10 packages")
    

# The Fast Freight Shipping Company charges the following rates:
# Weight of Package: 2lbs or less                    =>  Rate per pound: $1.50
#                    over 2lbs, not more than 6lbs   =>                  $3.00
#                    over 6lbs, not more than 10lbs  =>                  $4.00
#                    over 10lbs                      =>                  $4.75

# Write a program that asks the user to enter the weight of a package and
# then displays the shipping charges

weight = float(input("Weight of package? "))

if weight <= 2:
    rate_per_lb = 1.50
    shipping_charges = weight * rate_per_lb
    print("Shipping charge is", shipping_charges)
    
elif weight > 2 and weight <= 6:
    rate_per_lb = 3.00
    shipping_charges = weight * rate_per_lb
    print("Shipping charge is", shipping_charges)

elif weight > 6 and weight <= 10:
    rate_per_lb = 4.00
    shipping_charges = weight * rate_per_lb
    print("Shipping charge is", shipping_charges)

else:
    rate_per_lb = 4.75
    shipping_charges = weight * rate_per_lb
    print("Shipping charge is", shipping_charges)


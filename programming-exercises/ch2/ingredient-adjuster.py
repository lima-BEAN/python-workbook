## A cookie recipe calls for the following ingredients:
## - 1.5 cups of sugar    
## - 1 cup of butter
## - 2.75 cups of flour
## The recipe produces 48 cookies with this amount of the ingredients.
## Write a program that asks the user how many cookies he or she wants to
## make, and then displays the number of cups of each ingredient needed
## for the specified number of cookies.

cookies = int(input("How many cookies do you want? "))
# 0.03215 cups of sugar per cookie
sugar = cookies * 0.03125
# 0.02083 cups of butter per cookie
butter = cookies * 0.02083
# 0.05729 cups of flour per cookie
flour = cookies * 0.05729

print("For", cookies, "cookies, you need:",
      "\n\t", format(sugar, ".2f"), "cups of sugar",
      "\n\t", format(butter, ".2f"), "cups of butter",
      "\n\t", format(flour, ".2f"), "cups of flour",

# The colors red, blue and yellow are known as the primary colors because
# they cannot be made by mixing other colors. When you mix two primary
# colors, you get a secondary color, as shown here:
# When you mix red and blue, you get purple
# When you mix red and yellow, you get orange
# When you mix blue and yellow, you get green

# Design a program that prompts the user to enter the names of two primary
# colors to mix. If the user enters anything other than 'red', 'blue', or
# 'yellow', the program should display an error message. Otherwise,
# the program should display the name of the secondary color that results.

primary1 = input("Choose a primary color: (yellow, blue or red) ")
primary2 = input("Choose another primary color: (yellow, blue or red) ")

if (primary1.lower() == 'yellow' and primary2.lower() == 'blue') or (primary2.lower() == 'yellow' and primary1.lower() == 'blue'):
    print("Your new secondary color is Green")
elif (primary1.lower() == 'yellow' and primary2.lower() == 'red') or (primary2.lower() == 'yellow' and primary1.lower() == 'red'):
    print("Your new secondary color is Orange")
    
elif (primary1.lower() == 'red' and primary2.lower() == 'blue') or (primary2.lower() == 'red' and primary1.lower() == 'blue'):
    print("Your new secondary color is Green")
elif (primary1.lower() == primary2.lower()):
    print("Choose TWO different Primary colors to get a secondary color.")
else:
    print('You need to choose a PRIMARY COLOR: (Yellow, Red, or Blue)')

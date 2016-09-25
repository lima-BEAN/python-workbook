# Write an if-else statemnet that determines whether the points variable
# is outside the range of 9 to 51. If the variable's value is outside this
# range it should display "Invalid points". Otherwise, it should
# display 'Valid points'


points = int(input("How many points did you score? "))

if points >= 9 or points <= 51:
    print("Valid points")
else:
    print("Invalid points!")
cd .

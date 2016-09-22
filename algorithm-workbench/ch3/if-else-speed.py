# Write an if-else statement that displays 'Speed is normal' if the
# speed variable is within the range of 24 to 56. If the speed variable's
# value is outside this range, display 'Speed is abnormal'

speed = int(input("How fast are you going? "))

if speed >= 24 and speed <= 56:
    print("Speed is normal")
else:
    print("Speed is abnormal")

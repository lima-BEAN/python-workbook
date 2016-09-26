# Running on a particular treadmill you burn 4.2 calories per
# minute. Write a program that uses a loop to display the
# number of calories burned after 10, 15, 20, 25, and 30 minutes.

calories_burned = 0

for calories in range(1, 31):
    calories_burned += 4.2
    while calories >= 10:
        if calories % 5 == 0:
            print("You have burned", format(calories_burned, '.1f'),
                  "calories in", calories, "minutes")
        calories = 0


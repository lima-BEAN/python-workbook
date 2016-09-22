# The date June 10, 1960, is special because when it is written in
# the following format, the month times the day equals the year:
# 6/10/60
# Design a program that asks the user to enter a month (in numeric form),
# a day, and a two-digit year. The program should then determine whether the
# month times the day equals the year. If so, it should display a message
# saying the date is not magic.

month = int(input("Please enter month in number format: "))
day = int(input("Please enter day in number format: "))
year = int(input("Please enter year in 2-digit format: "))

magic = month * day

if magic == year:
    print("WOW! Now that\'s magic\n" + str(month) + "/" + str(day) + "/" + str(year) +
          " The month * day: " + str(magic) + " equals the year: " + str(year))
else:
    print("No magic in the date this time!")

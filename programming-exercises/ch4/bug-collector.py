# A bug collector collects bugs every day for five days. Write a program
# that keeps a running total of the number of bugs collected during the
# five days. The loop should ask for the number of bugs collected for
# each day, and when the loop is finished, the program should display
# the total number of bugs collected.

bugs_collected = 0
days = 0

for x in range(5):
    bugs_daily = int(input("How many bugs have you collected for day " +
                           str(x+1) + " "))
    bugs_collected += bugs_daily
    days += 1
print("You collected", bugs_collected, "bugs in", days, "days")

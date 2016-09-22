# Write a program that asks the user to enter a number of seconds and works
# as follows:

# - There are 60 seconds in a minute. If number of seconds is >= 60,
#       the program should display the number of minutes in that many seconds
# - There are 3600 seconds in an hour. If the number of seconds entered
#       is >= 3,600, display number of hours in that many seconds
# - There are 86,400 seconds in a day. If the number of seconds entered
#       is >= 86,400, display the number of days in that many seconds


seconds = int(input("How many seconds? "))
minutes = int
hours = int
days = int

if seconds >= 60:
    if seconds >= 3600:
        if seconds >= 86400:
            days = seconds // 86400
            hours = (seconds % 86400) // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
        else:
            days = 0
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
    else:           
        days = 0
        hours = 0
        minutes = seconds // 60
        seconds = seconds % 60
        
else:
    days = 0
    hours = 0
    minutes = 0
    seconds = seconds
    
print("\nDays:", days,
      "\nHours:", hours,
      "\nMinutes:", minutes,
      "\nSeconds:", seconds)

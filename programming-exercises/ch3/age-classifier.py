# Write a program that asks the user to enter a person's age.
# The program should display a message indicating whether the
# person is an infant, a child, a teenager or an adult.
# Following are guidelines:
# If 1 year old or less, infant
# If older 1 yo, but younger than 13, child
# If at least 13 yo, but less than 20 yo, teenager
# If at least 20 yo, adult

age = int(input("How old are you? "))

if age <= 1:
    print("You are an infant. ")
elif age > 1 and age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

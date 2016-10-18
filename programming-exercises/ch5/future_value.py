# Future Value
# Suppose you have a certain amount of money in a savings account that
# earns compound monthly interest and you want to calculate the amount
# that you will have after a specific number of months.
# The formula:  F = P x (1 + i)**t
# F = Future Value
# P = Present Value
# i = monthly interest rate
# t = number of months
# Write a program that prompts the user to enter the account's present value,
# monthly interest rate and the number of months that the money will be left
# in the account. The program should pass these values to a function that
# returns the future value of the account, after the specified months.
# Program should display the account's future value

def main():

    present_value = PresentValue()
    monthly_interest = MonthlyInterest()
    num_of_months = NumOfMonths()
    future_value = FutureValue(present_value, monthly_interest, num_of_months)

    Results(present_value, monthly_interest, num_of_months, future_value)

def PresentValue():
    print()
    p_value = float(input('Enter present value: '))
    return p_value

def MonthlyInterest():
    interest = float(input('Enter monthly interest: '))
    return interest

def NumOfMonths():
    months = int(input('How many months: '))
    return months

def FutureValue(p_value, interest, months):
    f_value = p_value * ((1 + interest)**months)
    return f_value

def Results(p_value, interest, months, f_value):
    print()
    print('===================== Future Value ==========================')
    print('Present Value:', p_value, '\nMonthly Interest:', interest,
          '\nNumber of Months:', months, '\nFuture Value:', f_value)

main()

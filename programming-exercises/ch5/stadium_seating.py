# There are three seating categories at a stadium. For a softball game,
# Class A seats cost $20, Class B seats cost $15, and Class C seats cost $10
# Write a program that asks how many tickets for each class of seats were
# sold, and then displays the amount of income generated from ticket sales.

A_COST = 20
B_COST = 15
C_COST = 10

def main():

    Greeting()
    
    a_count = ACount()
    b_count = BCount()
    c_count = CCount()
    total_count = TotalCount(a_count, b_count, c_count)

    a_amount = AAmount(a_count)
    b_amount = BAmount(b_count)
    c_amount = CAmount(c_count)
    total_amount = TotalAmount(a_amount, b_amount, c_amount)

    PurchaseSummary(a_count, b_count, c_count, total_count,
                    a_amount, b_amount, c_amount, total_amount)

def Greeting():
    print()
    print('================= Ticket\'s For Sale ======================')
    print('Class A tickets: $' + str(A_COST), '\tClass B tickets: $' + str(B_COST),
          '\tClass C tickets: $' + str(C_COST))
    print()

def ACount():
    count = int(input('How many Class A tickets did you want? '))
    return count

def BCount():
    count = int(input('How many Class B tickets did you want? '))
    return count

def CCount():
    count = int(input('How many Class C tickets did you want? '))
    return count

def TotalCount(a, b, c):
    return a + b + c

def AAmount(count):
    return count * A_COST

def BAmount(count):
    return count * B_COST

def CAmount(count):
    return count * C_COST

def TotalAmount(a, b, c):
    return a + b + c

def PurchaseSummary(a_count, b_count, c_count, total_count,
                    a_amount, b_amount, c_amount, total_amount):
    print()
    print('================= Ticket Purchase Summary =================')
    print('\nNumber of Class A tickets:', a_count, '\t', 'Cost: $' + str(format(a_amount, '.2f')),
          '\nNumber of Class B tickets:', b_count, '\t', 'Cost: $' + str(format(b_amount, '.2f')),
          '\nNumber of Class C tickets:', c_count, '\t', 'Cost: $' + str(format(c_amount, '.2f')))
    print()
    print('\nTotal Tickets:', total_count, '\tTotal Cost: $' + str(format(total_amount, '.2f')))
    print('\n======================= Thank You ==========================')
    
main()

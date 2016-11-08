# Total Sales
# Design a program that asks the user to enter a store's sales for each
# day of the week. The amounts should be stored in a list. Use a loop
# to calculate the total sales for the week and display the result.

def main():

    sales = Sales(Greeting())
    total = Total(sales)
    
def Greeting():
    print()
    print('================ Store\'s Sales ===================')
    cont = input('Would you like to get the total sales for the week? (y/n) ')
    if cont.title() == 'Y':
        return True
    else:
        return False

def Sales(cont):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wedensday', 'Thursday', 'Friday', 'Saturday']
    sales = []
    print()
    
    if cont == True:
        for x in range(len(days)):
            sale = input('Sales for ' + days[x] + ': ')
            sales.append(sale)
    else:
        sales.append(0)
        print('Maybe next time')
        
    return sales

def Total(sales):
    total = 0
    for sale in sales:
        total += float(sale)
    print('Total for the week: ' + str(format(total, '.2f')))

main()

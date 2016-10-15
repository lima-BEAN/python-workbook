# Program exercise #6 in Chapter 2 was a Sales Tax Program.
# Redesign solution so subtasks are in functions.


## purchase_amount = int(input("What is the purchasing amount? "))
## state_tax = 0.05
## county_tax = 0.025
## total_tax = state_tax + county_tax
## total_sale = format(purchase_amount + (purchase_amount * total_tax), '.2f')
##
## print("The purchase amount for the item is $" + str(purchase_amount),
##      "\n\tState tax:", format((state_tax * purchase_amount), '.2f'),
##      "\n\tCounty tax:", format((county_tax * purchase_amount), '.2f'),
##      "\n\tTotal tax:", format((total_tax * purchase_amount), '.2f'),
## "\n\tTotal sale amount is $" + str(total_sale))

COUNTY_TAX = 0.025
STATE_TAX = 0.05

def main():

    purchase_amount = float(input('What is the purchasing amount? '))
    county_tax = CountyTax(purchase_amount)
    state_tax = StateTax(purchase_amount)
    total_tax = TotalTax(county_tax, state_tax)
    total_sale = TotalSale(purchase_amount, total_tax)

    PrintBill(purchase_amount, county_tax, state_tax,
              total_tax, total_sale)


def CountyTax(p_amount):
    return p_amount * COUNTY_TAX

def StateTax(p_amount):
    return p_amount * STATE_TAX

def TotalTax(c_tax, s_tax):
    return c_tax + s_tax

def TotalSale(p_amount, t_tax):
    return p_amount + t_tax


def PrintBill(p_amount, c_tax, s_tax, t_tax, t_sale):

    print('============ Bill Summary ================')
    print("Purchase amount:", format(p_amount, '.2f'), 
        "\nTotal tax:", '\t', format(t_tax, '.2f'),
        "\t\t=>","\tCounty tax:", format(c_tax, '.2f'),
        "+ State tax:", format(s_tax, '.2f'),
        "\nTotal sale:", '\t', format(t_sale, '.2f'))

main()

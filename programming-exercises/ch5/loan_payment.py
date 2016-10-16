# Write a program that asks the user to enter the monthly costs for the
# folowing expenses incurred from operating his or her automobile:
# loan payment, insurance, gas, oil, tires and maintenance.
# The program should then display the total monthly cost of these
# expenses, and the total annual cost of these expenses.

def main():
    
    print()
    print('Let\'s figure out your total monthly automobile expense')
    print('==========================================')
    
    loan_payment = LoanPayment()
    insurance_expense = InsuranceExpense()
    gas_expense = GasExpense()
    oil_expense = OilExpense()
    tire_expense = TireExpense()
    maint_expense = MaintExpense()
    total_car_expense = TotalCarExpense(loan_payment, insurance_expense, gas_expense, oil_expense, tire_expense, maint_expense)

    ChooseBill(loan_payment, insurance_expense, gas_expense, oil_expense, tire_expense, maint_expense, total_car_expense)
    
    
def LoanPayment():

    inst_type = input('What type of payment plan? ' +
                        'Weekly, Biweekly, Monthly? ')
        
    payment = float(input('How much is your loan payment? '))

    if inst_type.capitalize() == 'Weekly':
        return payment * 4
    elif inst_type.capitalize() == 'Biweekly':
        return payment * 2
    elif inst_type.capitalize() == 'Monthly':
        return payment
    

def InsuranceExpense():
    return float(input('How much is your insurance? '))

    
def GasExpense():
    occurence = int(input('How many times do you fill up each month? '))
    expense = float(input('How much do you pay for gas each time you fill up? '))
    return occurence * expense


def OilExpense():
    occurence = int(input('How many times do you change your oil per year? '))
    expense = float(input('How much do you pay for each oil change? '))
    average_monthly_expense = (occurence * expense) / 12
    return average_monthly_expense


def TireExpense():
    return float(input('How much for monthly tire maitenance? '))


def MaintExpense():
    return float(input('How much for monthly auto maintenance? '))


def TotalCarExpense(payment, insurance, gas, oil, tires, maint):
    return (payment + insurance + gas + oil + tires + maint)


def ChooseBill(loan_payment, insurance_expense, gas_expense, oil_expense, tire_expense, maint_expense, total_car_expense):
    print()
    bill_type = input('Which Liablility Bill would you like to see? ' +
                      'Monthly or Annually? or Both? ')

    if bill_type.capitalize() == 'Monthly':
        CarMonthlyBill(loan_payment, insurance_expense, gas_expense, oil_expense,
                       tire_expense, maint_expense, total_car_expense)        
    elif bill_type.capitalize() == 'Annually':
        CarAnnualBill(loan_payment, insurance_expense, gas_expense, oil_expense,
                       tire_expense, maint_expense, total_car_expense)
    elif bill_type.capitalize() == 'Both':
        CarBothBill(loan_payment, insurance_expense, gas_expense, oil_expense,
                       tire_expense, maint_expense, total_car_expense)

def CarMonthlyBill(payment, ins, gas, oil, tires, maint, total):
    print('============ Monthly Liability ============')
    print('Loan payment:', format(payment, '.2f'),
          '\nInsurance:', format(ins, '.2f'),
          '\nGas:', format(gas, '.2f'),
          '\nOil:', format(oil, '.2f'),
          '\nTires:', format(tires, '.2f'),
          '\nMainentance', format(maint, '.2f'),
          '\nTotal per Month:', format(total, '.2f'))

def CarAnnualBill(payment, ins, gas, oil, tires, maint, total):
    print('============ Annual Liability ============')
    print('Loan payment:', format(12*payment, '.2f'),
          '\nInsurance:', format(12*ins, '.2f'),
          '\nGas:', format(12*gas, '.2f'),
          '\nOil:', format(12*oil, '.2f'),
          '\nTires:', format(12*tires, '.2f'),
          '\nMainentance', format(12*maint, '.2f'),
          '\nTotal per Year:', format(12*total, '.2f'))

def CarBothBill(payment, ins, gas, oil, tires, maint, total):

    print()
    CarMonthlyBill(payment, ins, gas, oil, tires, maint, total)
    print()
    CarAnnualBill(payment, ins, gas, oil, tires, maint, total)
        
main()

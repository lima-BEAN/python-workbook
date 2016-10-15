# Many financial experts advise that property owners should
# insure their homes or buildings for at least 80% of the
# amount it would cost to replace the structure. Write a program
# that ask the user to enter the replacement cost a building and then
# displays the minimum amount of insurance he or she should buy for the
# property.

COVERAGE_PERCENT = 0.80

def main():

    replacement_cost = float(input('What is the replacement cost ' +
                                   'of the building? '))
    MinInsurance(replacement_cost)
    

def MinInsurance(r_cost):
    
    min_insurance = r_cost * COVERAGE_PERCENT
    print('Your minimum insurance coverage should be', format(min_insurance,
                                                              '.2f'))
    
main()
    

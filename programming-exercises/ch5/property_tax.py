# A county collects property taxes on the assessment value of property,
# which is 60 percent of the property's actual value. For example,
# if an acre of land is valued at $10,000, its assessment value is
# $6,000. The property tax is then 72 cents for each $100 of the assessment
# value. The tax for the acre assessed at $6,000 will be $43.20.
# Write a program that asks for the actual value of a piece of property
# and displays the assessment value and property tax.

ASSESSMENT_PERCENT = 0.60
PROPERTY_TAX = 0.72
PER_ASSESSMENT = 100

def main():

    Greeting()
    
    actual_value = ActualValue()
    assessment_value = AssessmentValue(actual_value)
    tax_value = TaxValue(assessment_value)
    
    PropertySummary(actual_value, assessment_value, tax_value)

def Greeting():
    print()
    print('=============== Property Assessment ==================')
    print('Let\'s find out your properties assesment value to get',
          'your property tax')

def ActualValue():
    print()
    actual = float(input('What is the actual value of the property? '))
    return actual
                  
def AssessmentValue(actual):
    assessment = actual * ASSESSMENT_PERCENT
    return assessment
                   
def TaxValue(assessment):
    property_tax = 0
    
## While loop is a few lines longer.
##    value = 0
##
##    while value < (assessment + 0.01):
##        if value % 100 == 0:
##            property_tax = count * PROPERTY_TAX
##        value += 1
##
##    

    for value in range(0, (int(assessment) + 1) , PER_ASSESSMENT):
##      if value % 100 == 0:  NOT NEEDED SINCE WE ITERATE SPECIFIC AMOUNT
        property_tax += PROPERTY_TAX

    
    return property_tax
                 
def PropertySummary(actual, assessment, tax):
    print()
    print('=============== Property Summary =====================')
    print('\nActual value:', '\t\t', format(actual, '.2f'),
          '\nAssessment value:', '\t', format(assessment, '.2f'),
          '\nProperty tax:', '\t\t', format(tax, '.2f'))
    print()
    print('======================================================')
    print('Thank you for choosing our tax calculator!')



main()

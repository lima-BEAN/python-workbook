# At one college, the tuition for a full-time student is $8,000 per semester.
# It has been announced that the tuition will increase by 3% each year
# for the next 5 years. Write a program with a loop that displays the
# projected semester tuition amount for the next 5 years.

tuition = 8000
increase = 0.03
print('Year\tTuition Cost')
print('-------------------')


for year in range(6):
    if year > 0:
        tuition = (tuition * increase) + tuition
    print(year, '\t', format(tuition, '.2f'))
        
    

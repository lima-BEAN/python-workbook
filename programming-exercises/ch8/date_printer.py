# Date Printer
# Write a program that reads a string from the user containing a date in
# the form mm/dd/yyyy. It should print the date in the form
# March 12, 2014

def main():
    user_date = UserDate()
    date_form = DateForm(user_date)
    Results(date_form)

def UserDate():
    date = input('Enter a date in the format (mm/dd/yyyy): ')
    return date

def DateForm(date):
    months = [  'January', 'Feburary', 'March', 'April', \
                'May', 'June', 'July', 'August',\
                'September', 'October', 'November', 'December' ]
    f_date = ''
    split_date = date.split('/')
    m_date = ''
    d_date = split_date[1]
    y_date = split_date[2]

    for x in range(len(months)):
        if int(split_date[0]) == x+1:
            m_date = months[x]

    f_date = m_date + ' ' + d_date + ', ' + y_date
    return f_date

def Results(date):
    print()
    print('Your formatted date is:', date)
    
main()

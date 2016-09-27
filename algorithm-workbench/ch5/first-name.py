# Write a function named get_first_name that asks the user to enter his or her
# first name and returns it

def main():
    first_name = input('What is your first name? ')
    get_first_name(first_name)
    
def get_first_name(f_name):
    print('Your first name is', f_name)
    
main()

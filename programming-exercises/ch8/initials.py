# Write a program that gets a string containing a person's first, middle
# and last names, and then display their first, middle and last initials.
# For example, John William Smith => J. W. S.

def main():
    name = Name()
    initials = Initials(name)
    Results(initials)
    
def Name():
    name = input('What is your full name? ')
    return name

def Initials(name):
    initial = name.split(' ')
    initials = []

    if len(initial) == 3:
        f_initial = initial[0][:1] + '.'
        m_initial = initial[1][:1] + '.'
        l_initial = initial[2][:1] + '.'

        initials.append(f_initial.title())
        initials.append(m_initial.title())
        initials.append(l_initial.title())

    elif len(initial) == 2:
        f_initial = initial[0][:1] + '.'
        l_initial = initial[1][:1] + '.'

        initials.append(f_initial.title())
        initials.append(l_initial.title())

    return initials

def Results(initials):
    full_initials = ''
    
    for x in range(len(initials)):
        full_initials += initials[x]
        full_initials += ' '
        
    print('Your initials are:', full_initials)

main()

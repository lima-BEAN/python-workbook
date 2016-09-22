# Rewrite code and use proper conventions of alignment and indetation
# if score >= A_score:
# print('Your grade is A.')
# else:
# if score >= B_score:
# print('Your grade is B.')
# else:
# if score >= C_score:
# print('Your grade is C.')
# else:
# if score >= D_score:
# print('Your grade is D.')
# else:
# print('Your grade is F.')

# ============================================

# Initiliaze A, B, C, D scores
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Ask for user's score
score = int(input("What is your score? "))

if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is an F.')

#=============================================
# Using elif

##if score >= A_score:
##    print('Your grade is A.')
##elif score >= B_score:
##    print('Your grade is B.')
##elif score >= C_score:
##    print('Your grade is C.')
##elif score >= D_score:
##    print('Your grade is D.')
##else:
##    print('Your grade is an F.')

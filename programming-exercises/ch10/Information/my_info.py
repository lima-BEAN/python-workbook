# Also, write a program that creates three instances of the class. One
# instance should hold your information, and the other two should hold
# your friends' or family members' information.
import information

def main():
    my_info = information.Information('LimaBean', '123 Beanstalk St.',
                                      '12 pods', '1-800-LimaBean')
    fam1_info = information.Information('GreenBean', '456 Green St.',
                                        '3 beans', '555-My-Greens')
    fam2_info = information.Information('BlackBean', '987 Refried St.',
                                        '7 black beans', '222-BLACK-REFRIED')
    print('My Info:', my_info.get_name())
    print('Fam1 Info:', fam1_info.get_name())
    print('Fam2 Info:', fam2_info.get_name())
    
main()

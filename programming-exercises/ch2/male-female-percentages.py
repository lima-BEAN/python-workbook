## Write a program that asks the user for the number of males and the
## number of females registered in a class. The program should display
## the percentage of males and females in the class.
## HINT: Suppose there are 8 males and 12 females in a class. There are
## 20 students in the class. The percentage of males can be calculated as
## 8 / 20 = 0.4, or 40%. The percentage of females can be calculated
## as 12 / 20 - 0.6, or 60%

males = int(input("How many males are in the class? "))
females = int(input("How many females are in the class? "))
total = males + females
percent_male = males / total
percent_female = females / total

print("Percentage of males:", format(percent_male, '.0%'),
        "\nPercentage of females:", format(percent_female, '.0%'))

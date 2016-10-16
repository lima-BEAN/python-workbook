# A nutritionist who works for a fitness club helps members by
# evaluating their diets. As part of her evaluation, she asks members
# for the number of fat grams and carbohydrate grams that they
# consumed in a day. Then she calculates the number of calories
# that result from the fat formula: calories from fat = fat grams * 9
# Next, she calculates the number of calories that result from the
# carbohydrates, using: calories from carbs = carbs grams * 4
# The nutritionist asks you to write a program that will make these calculations

CALORIE_FAT_MULTIPLE = 9
CALORIE_CARB_MULTIPLE = 4

def main():

    Greeting()
    
    daily_fat_cal = DailyFatCal()
    daily_carb_cal = DailyCarbCal()
    daily_total_cal = DailyTotalCal(daily_fat_cal, daily_carb_cal)

    DailyCalSummary(daily_fat_cal, daily_carb_cal, daily_total_cal)


def Greeting():
    print()
    print('============== Calorie Intake Calculator ================')
    print()

def DailyFatCal():
    grams = float(input('How many grams of fat did you intake today? '))
    calories_from_fat = grams * CALORIE_FAT_MULTIPLE
    return calories_from_fat

def DailyCarbCal():
    grams = float(input('How many grams of carbs did you intake today? '))
    calories_from_carb = grams * CALORIE_CARB_MULTIPLE
    return calories_from_carb

def DailyTotalCal(fat, carb):
    return fat + carb

def DailyCalSummary(fat, carb, total):
    print()
    print('============== Daily Calorie Summary ===================')
    print('\nFat calories:', '\t\t', format(fat, '.1f'), 'grams',
          '\nCarb calories:', '\t\t', format(carb, '.1f'), 'grams',
          '\nTotal calories:', '\t', format(total, '.1f'), 'grams')

main()

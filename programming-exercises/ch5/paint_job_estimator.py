# A painting company has determined that for every 112 square feet
# of wall space, one gallon of paint and eight hours of labor will be
# required. The company charges $35.00 per hour for labor. Write a
# program that asks the user to enter the square feet of wall space
# to be painted and the price of the paint per gallon. The program should
# display: # of gallons of paint required
#          Hours of labor worked
#          Cost of paint
#          Labor charges
#          Total cost of paint job

WALL_SPACE_COVERAGE = 112
GAL_PAINT_COVERAGE  = 1
LABOR_HOUR_COVERAGE = 8

PER_HOUR_CHARGE     = 35

def main():

    Greeting()

    wall_paint_req = WallPaintReq()
    gal_paint_req = GalPaintReq(wall_paint_req)
    labor_hour_req = LaborHourReq(wall_paint_req)

    paint_cost = PaintCost(gal_paint_req)
    labor_cost = LaborCost(labor_hour_req)
    total_cost = TotalCost(paint_cost, labor_cost)

    PaintBillSummary(wall_paint_req, gal_paint_req, labor_hour_req,
                     paint_cost, labor_cost, total_cost)

def Greeting():
    print()
    print('=================== Paint Job Estimator =====================')
    print()

def WallPaintReq():
    paint_sq_feet = float(input('How many square feet do you want to paint? '))
    return paint_sq_feet

def GalPaintReq(paint):
    gal = 0
    for x in range(0, int(paint+1), WALL_SPACE_COVERAGE):
        gal += GAL_PAINT_COVERAGE
    return gal

def LaborHourReq(paint):
    hr = 0
    for x in range(0, int(paint+1), WALL_SPACE_COVERAGE):
        hr += LABOR_HOUR_COVERAGE
    return hr

def PaintCost(gal):
    cost_per_gallon = float(input('How much is it for a gallon of paint? '))
    return gal * cost_per_gallon

def LaborCost(hr):
    return hr * PER_HOUR_CHARGE

def TotalCost(paint, labor):
    return paint + labor

def PaintBillSummary(wall, gal, hr, paint, labor, total):
    print()
    print('=================== Paint Job Summary =======================')
    print('\nFor a paint job of', wall, 'sqft.',
          '\nGallons of paint required:', gal,
          '\nLabor hours required:', hr,
          '\nPaint Cost:', paint,
          '\nLabor Cost:', labor,
          '\nTotal Cost:', total)
    print('=================== Thank you ==============================')

main()

# Write a statement that creates a two-dimensional list with 5 rows
# and 3 columns. Then write nested loops that get an integer value
# from the user for each element in the list.

ROW = 5
COL = 3

def main():

    d_list = [[0]*COL] * ROW
    fill = Fill(d_list)
    Show(fill)
    
def Fill(d_list):
    for x in range(ROW):
        for y in range(COL):
            d_list[x][y] = input('Enter a number: ')
    return d_list

def Show(fill):
    print(fill)

main()

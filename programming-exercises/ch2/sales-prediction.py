## A company has determined that its annual profit is typically 23 percent
## of total sales. Write a program that asks the user to enter the projected
## amount of total sales, and then displays the profit that will be made
## from that amount


projected_total_sales = int(input("What is the company's projected total sales? "))
profit_margin = 0.23
projected_profits = projected_total_sales + (projected_total_sales * profit_margin)

print("Your projected profits will be $" + str(format(projected_profits, ',.2f')))

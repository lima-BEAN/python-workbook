## Last month Joe purchased some stock in Acme Software Inc. Here are the
## details of the purchase:
## - The number of shares that Joe purchased was 2,000
## - When Joe purchased the stock, he paid $40.00 per share.
## - Joe paid his stockbroker a commission that amounted to 3 percent of the
##   amount he paid for the stock

## Two weeks later Joe sold the stock. Here are the details of the sale:
## - The number of shares that Joe sold was 2,000
## - He sold the stock for $42.75 per share
## - He paid his stockbroker another commission that amounted to 3 percent
##   of the amount he received for the stock.

## Write a program that displays the following info:
## - Amount of money Joe paid for the stock
## - Amount of commission Joe paid his broker when he bought the stock
## - Amount that Joe sold the stock for
## - Amount of commission Joe paid his broker when he sold the stock
## - Display the amount of money that Joe had left when he sold the stock
##   and paid his broker (both times). If this amount is positive, then
##   Joe made a profit . If the amount is negative, then Joe lost his money

# Shares bought
purchased_shares = 2000
purchased_dollar_per_share = 40
total_stock_purchase = (purchased_shares * purchased_dollar_per_share)
purchased_broker_commission = total_stock_purchase * 0.03
total_purchase = total_stock_purchase + purchased_broker_commission

# Shares sold
sold_shares = 2000
sold_dollar_per_share = 42.75
total_stock_sale = (sold_shares * sold_dollar_per_share)
sold_broker_commission = total_stock_sale * 0.03
total_sale = total_stock_sale - sold_broker_commission

# Profit/Loss
profit_or_loss = total_sale - (total_purchase)

# Display Stock Transaction
print("Cost for", purchased_shares, "shares at", purchased_dollar_per_share," per share:",
      total_stock_purchase, "\n\tBroker's commission:", purchased_broker_commission,
      "\nSold", sold_shares, "shares at", sold_dollar_per_share, "per share. For a total sale of:",
      total_stock_sale, "\n\tBroker's commission:", sold_broker_commission,
      "\nJoe made:", format(profit_or_loss, '.2f'))



#!/usr/bin/env python

"""
	hw6.1.py -- Sorting Stocks Between Close & Open Prices
	author: Danny Moncada
"""

stock_price = open('../../python_data/stock_prices.csv').readlines()[1:]

def by_closelessopen(arg):
    arg = arg.split(',')
    gain_or_loss = float(arg[5]) - float(arg[2])
    percent_increase = gain_or_loss / float(arg[2]) * 100
    return percent_increase
# I decided to do the extra credit portion and do the sorting function by percentage increase - that should be reflected in the output

sorted_stock = sorted(stock_price, key = by_closelessopen, reverse = True)[0:11]

for line in sorted_stock:
    line = line.rstrip()
    ticker, date, open, high, low, close, volume = line.split(',')
    print '{} ({}): +{}% ({}->{})'.format(ticker, date, round(((float(close)-float(open)) / float(open)) * 100, 2), open, close)

exit()
#!/usr/bin/env python

""""
	hw7.1.py -- Sorting Stocks Using Lambda Function
	author: Danny Moncada
"""

stock_price = open('../../python_data/stock_prices.csv').readlines()[1:]

sorted_stocks = sorted(stock_price, key = lambda x: ((float(x.split(',')[5]) - float(x.split(',')[2])) / 
    float(x.split(',')[2])), reverse = True)

# I chose to do it via the biggest percentage increase instead of biggest one-day gain

for line in sorted_stocks[0:10]:
    ticker, date, open, high, low, close, volume = line.split(',')
    print '{} {}: +{}% ({}->{})'.format(ticker, date, round((float(close) - float(open)) * 100 / float(open), 2), open, close)
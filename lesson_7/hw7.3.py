#!/usr/bin/env python

"""
	hw7.3.py -- Build A Dict of Lists Using Highest and Lowest Close Prices
	author: Danny Moncada
"""

new_dict = {}

for line in open('../../python_data/stock_prices.csv').readlines()[1:]:
    ticker, date, open, high, low, close, volume = line.split(',')
    if ticker not in new_dict:
        new_dict[ticker] = []
    new_dict[ticker].append(float(close))

for item in sorted(new_dict, key = lambda x: max(new_dict[x]) - min(new_dict[x]), reverse = True):
    print '{}: {} difference ({}-{})'.format(item, max(new_dict[item]) - min(new_dict[item]), min(new_dict[item]), max(new_dict[item]))
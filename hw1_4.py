#!/usr/bin/env python

"""
	hw1_4.py -- Share Calculator - calculate number of shares you can buy
	author: Danny Moncada
"""

def get_price(symbol):
	import urllib
	import json

	base_url = "http://finance.google.com/finance/info?client=ig&q={}:{}"
	try:
		content = urllib.urlopen(base_url.format('NASDAQ', symbol)).read()
	except IOError:
		exit('Error: cannot connect')
	try:
		obj = json.loads(content[3:]) #clearing out [3:]
	except ValueError:
		exit('Error: stock symbol ' + symbol + ' not found')
 
	current_price = obj[0]['l'].replace(',', '')
 
	return float(current_price)

aa = raw_input('please input the stock symbol you would like to buy: ')
bb = raw_input('please input the cash you have to invest: ')

cc = get_price(aa) # returns a float price

num_of_shares = int(bb) / int(cc)

price_per_share = round(cc, 2)

print 'with $' + bb + ' you can buy ' + str(num_of_shares) + ' shares of ' + aa + ' at $' + str(price_per_share) + "/share"
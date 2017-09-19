#!/usr/bin/env python

"""
	hw1_3.py -- price per unit comparison
	author: Danny Moncada
"""

product_size_a = raw_input('please enter the unit size of Product 1: ')

product_price_a = raw_input('please enter the price of Product 1: ')

product_size_b = raw_input('please enter the unit size of Product 2: ')

product_price_b = raw_input('please enter the price of Product 2: ')

cost_per_unit_a = float(product_price_a) / int(product_size_a)
rounded_a = round(cost_per_unit_a, 2)

cost_per_unit_b = float(product_price_b) / int(product_size_b)
rounded_b = round(cost_per_unit_b, 2)

comparison = round((cost_per_unit_a / cost_per_unit_b * 100), 2)

print 'Product 1 costs $' + str(rounded_a) + ' per unit'
print 'Product 2 costs $' + str(rounded_b) + ' per unit'
print 'Product 1 is ' + str(comparison) + '% the per-unit cost of Product 2'
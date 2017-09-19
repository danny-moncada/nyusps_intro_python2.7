#!/usr/bin/env python

from pprint import pprint

outer_dict = {}
file = open('../python_data/revenue.txt')

for line in file:
	company, state, revenue = line.split(',')
	if state not in outer_dict:
		outer_dict[state] = 0.0
	outer_dict[state] += float(revenue)

pprint(outer_dict)
print 
print outer_dict['NJ']
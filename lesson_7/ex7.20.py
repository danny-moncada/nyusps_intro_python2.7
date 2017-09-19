#!/usr/bin/env python

from pprint import pprint

outer_dict = {}
file = open('../python_data/revenue.txt')

for line in file:
	company, state, revenue = line.split(',')
	if state not in outer_dict:
		outer_dict[state] = []
	outer_dict[state].append(float(revenue))

pprint(outer_dict)
print
print round(sum(outer_dict['NY']) / len(outer_dict['NY']), 2)
#!/usr/bin/env python

revenue = '../python_data/revenue.txt'

for line in sorted(open(revenue).readlines(), key = lambda x: float(x.split(',')[-1])):
	print line.rstrip()

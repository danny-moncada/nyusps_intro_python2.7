#!/usr/bin/env python

revenue = open('../python_data/revenue.txt').readlines()

def float_sort(arg):
	val = float(arg.split(',')[2])
	return val

sorted_rev = sorted(revenue, key = float_sort)

for line in sorted_rev:
	print line.rstrip()



exit()
for line in revenue:
	num = float(line.rstrip().split(',')[2])
	print num

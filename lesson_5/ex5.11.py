#!/usr/bin/env python

mydict = {}

revenue = open('../python_data/revenue.txt').readlines()

for line in revenue:
	line = line.rstrip().split(',')
	state = line[1]
	rev = float(line[2])
	if state not in mydict:
		mydict[state] = 0.0
	mydict[state] += rev

print mydict
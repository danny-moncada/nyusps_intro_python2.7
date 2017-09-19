#!/usr/bin/env python

mydict = {}

file = open('../python_data/revenue.txt').readlines()

for line in file:
	line = line.rstrip().split(',')
	store = line[0]
	val = line[2]
	mydict[store] = val

print mydict
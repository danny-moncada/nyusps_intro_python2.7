#!usr/bin/env python


def getlines(filename):
	lines = open(filename).readlines()
	return lines
	
lines = getlines('/Users/dmoncada/Documents/Introduction to Python Programming_NYU/python_data/revenue.txt')

for line in lines:
	print line.rstrip()

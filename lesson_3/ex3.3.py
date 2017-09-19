#!/usr/bin/env python

count = 0
fh = open('../python_data/FF_abbreviated.txt')

for line in fh:
	count = count + 1
	print count, line
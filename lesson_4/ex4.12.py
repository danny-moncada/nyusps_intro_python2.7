#usr/bin/env python

revenue = open('../python_data/revenue.txt')

for lines in revenue:
	no_new_lines = lines.rstrip()
	print no_new_lines


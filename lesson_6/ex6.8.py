#!/usr/bin/env python

line_list = [
	'the value on this line is 3',
	'the value on this line is 1',
	'the value on this line is 4',
	'the value on this line is 2'
	]

def value_from_line(arg):
	num = int(arg.split()[6])
	return num

sorted_lines = sorted(line_list, key = value_from_line)

for line in sorted_lines:
	print line

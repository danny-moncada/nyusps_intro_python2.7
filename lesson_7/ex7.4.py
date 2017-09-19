#!/usr/bin/env python

line_list = [
	'the value on this line is 3',
	'the value on this line is 1',
	'the value on this line is 4',
	'the value on this line is 2'
	]

for line in sorted(line_list, key = lambda x: x.split()[-1]):
	print line
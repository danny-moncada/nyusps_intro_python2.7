#!/usr/bin/env python

from pprint import pprint

outer_list = {}

file = open('../python_data/student_db.txt')
lines = file.readlines()[1:]

for line in lines:
	std_id, street, city, state, std_zip = line.split(':')
	inner_dict = {'street': street, 'city': city, 'state': state, 'zip': std_zip.rstrip() }
	if state not in outer_list:
		outer_list[state] = 0
	outer_list[state] += 1

print outer_list
print
print outer_list['NY']

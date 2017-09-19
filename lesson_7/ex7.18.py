#!/usr/bin/env python

from pprint import pprint

outer_list = {}

file = open('../python_data/student_db.txt')
lines = file.readlines()[1:]

for line in lines:
	std_id, street, city, state, std_zip = line.split(':')
	#inner_dict = {'street': street, 'city': city, 'state': state, 'zip': std_zip.rstrip() }
	if state not in outer_list:
		outer_list[state] = []
	outer_list[state].append(std_id)

pprint(outer_list)
print
for i in outer_list['NJ']:
	print i

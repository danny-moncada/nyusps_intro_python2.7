#!/usr/bin/env python

from pprint import pprint

outer_list = [] 

file = open('../python_data/student_db.txt')
lines = file.readlines()[1:]

for line in lines:
	std_id, street, city, state, std_zip = line.split(':')
	inner_list = {'id' : std_id, 'city': city, 'state': state}
	outer_list.append(inner_list)

pprint(outer_list)
print
print outer_list[3]['city']

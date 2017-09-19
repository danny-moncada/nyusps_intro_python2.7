#!/usr/bin/env python

from pprint import pprint

outer_list = {}

file = open('../python_data/student_db.txt')
lines = file.readlines()[1:]

for line in lines:
	std_id, street, city, state, std_zip = line.split(':')
	if std_id not in outer_list:
		outer_list[std_id] = state

pprint(outer_list)
print 
print outer_list['ak9']

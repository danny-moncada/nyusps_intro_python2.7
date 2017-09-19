#!/usr/bin/env python

from pprint import pprint

outer_list = [] 

file = open('../python_data/student_db.txt')
lines = file.readlines()[1:]

for line in lines:
	std_id, street, city, state, std_zip = line.split(':')
	outer_list.append(std_id)

print outer_list
print outer_list[0]
#!/usr/bin/env python

from pprint import pprint

def bysum(arg):
	return sum(outer_dict[arg])

outer_dict = {}

lines = open('../python_data/FF_abbreviated.txt').read().splitlines()

for line in lines:
	items = line.split()
	year = line[0:4]
	if year not in outer_dict:
		outer_dict[year] = []
	outer_dict[year].append(float(items[1]))

print sorted(outer_dict, key=bysum)
#pprint(outer_dict)

exit()


outer_list = []
fh = open('../python_data/student_db.txt')
lines = fh.readlines()[1:]
for line in lines:
	this_id, street, city, state, this_zip = line.split(':')
	inner_list = { 'city' : city, 'state': state }
	outer_list.append(inner_list)

pprint(outer_list)
exit()
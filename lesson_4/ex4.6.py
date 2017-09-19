#usr/bin/env python

values_to_sum = []

revenue = open('../python_data/revenue.txt')

all_lines = revenue.readlines()
first_five = all_lines[0:5]

for line in all_lines:
	line_split = line.split(',')
	values = float(line_split[2])
	values_to_sum.append(values)

print sum(values_to_sum)

exit()
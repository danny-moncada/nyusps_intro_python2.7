#usr/bin/env python

student_ids = []

student_db = open('../python_data/student_db.txt')

all_lines = student_db.readlines()
all_but_first = all_lines[1:]

for line in all_but_first:
	elements = line.split(':')
	if 'NY' == elements[3]:
		ids = elements[0]
		student_ids.append(ids)

print student_ids

exit()
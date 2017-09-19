#usr/bin/env python

states_list = []

student_db = open('../python_data/student_db.txt')

all_lines = student_db.readlines()
all_but_first = all_lines[1:]

for line in all_but_first:
	elements = line.split(':')
	states = elements[3]
	states_list.append(states)

print states_list
exit()

lines = pw.readlines()
first_three = lines[0:3]
print first_three
#usr/bin/env python

new_list = []

student_db = open('../python_data/student_db.txt')

for line in student_db:
	split_lines = line.split(':')
	states = split_lines[3]
	new_list.append(states)

print new_list
exit()

lines = pw.readlines()
first_three = lines[0:3]
print first_three
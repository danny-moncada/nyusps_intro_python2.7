#!/usr/bin/env python

mydict = {}

student = open('../python_data/student_db.txt').readlines()[1:]

for line in student:
	line = line.rstrip().split(':')
	state = line[3]
	if state not in mydict:
		mydict[state] = 0
	mydict[state] += 1

print mydict
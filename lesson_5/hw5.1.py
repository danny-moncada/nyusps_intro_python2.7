#!/usr/bin/env python

"""
    hw5.1.py -- create a dict of student ids and address
    author: Danny Moncada
"""

mydict = {}

students = open('../../python_data/student_db.txt').readlines()[1:]

for line in students:
    line = line.rstrip().split(':')
    student_id = line[0]
    val = line[1:]
    if student_id not in mydict:
        mydict[student_id] = 0
    mydict[student_id] = val

print '{} records loaded.'.format(len(mydict))

while True:
    user_input = raw_input('please enter an id ("q" for quit): ')
    if user_input.startswith('q'):
        exit()
    elif user_input in mydict:
        address = mydict[user_input]
        print '\naddress for {}: \n{} \n{}, {} {}\n'.format(user_input, address[0], address[1], address[2], address[3])
    else:
        print 'sorry, that id does not exist chief\n'
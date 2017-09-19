#!/usr/bin/env python

from pprint import pprint

student_db = open('../python_data/student_db.txt').readlines()

student_db = [ line.rstrip() for line in open('../python_data/student_db.txt').readlines()[1:] ]

pprint(student_db)
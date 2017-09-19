#!/usr/bin/env python

from pprint import pprint

student_db = open('../python_data/student_db.txt').readlines()

student_db = [ line for line in open('../python_data/student_db.txt').readlines() ]

pprint(student_db)
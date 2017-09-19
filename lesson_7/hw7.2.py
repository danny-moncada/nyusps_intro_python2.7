#!/usr/bin/env python

"""
	hw7.2.py -- Use List Comprehension to Print Student IDs
	author: Danny Moncada"""

print [ ids.split(':')[0] for ids in open('../../python_data/student_db.txt').readlines()[1:] ]
#!usr/bin/env python

"""
	testing script to make sure filelib modules work
	author: Danny Moncada
"""

import filelib

datafile = 'student_db.txt'

lines = filelib.getlines(datafile, newlines=False)
print len(lines)

text = filelib.gettext(datafile)
print len(text)

#list_of_lists = filelib.getfields(datafile, delimiter='baddelimeter')

list_of_lists = filelib.getfields(datafile, delimiter = ':')
print list_of_lists
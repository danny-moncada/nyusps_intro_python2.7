#!/usr/bin/env python

"""
	hw2.3.py -- text replacement utility
	author: Danny Moncada
"""

sample_text = """And since you know you cannot see yourself,
so well as by reflection, I, your glass,
will modestly discover to yourself,
that of yourself which you yet know not of."""

def read_file(fname):
	try:
		text = open(fname).read()
 	except IOError:
 		print 'file {} not found or could not be read. '.format(fname)
 		print 'Using sample text instead.'
 		text = sample_text
 	return text

text = read_file(raw_input('please enter a filename: '))
target_text = raw_input('please enter search text: ')
replace_text = raw_input('please enter replace text: ')

modified_text = text.replace(target_text, replace_text)
print ""
print modified_text

replacements = modified_text.count(replace_text)
print ""
print '{} replacements made.'.format(replacements)
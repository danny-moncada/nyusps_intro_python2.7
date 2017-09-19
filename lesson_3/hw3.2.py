#/usr/bin/env python

"""
	hw_3.2.py -- wc emulation
	author: Danny Moncada
"""

filename = raw_input('please enter a filename: ')

read_file = open(filename)

text = read_file.read()
length_of_text = str(len(text))

words = text.split()
count_of_words = str(len(words))

lines = text.splitlines()
number_of_lines = str(len(lines))

print number_of_lines.rjust(8), count_of_words.rjust(8), length_of_text.rjust(8), filename.rjust(8)
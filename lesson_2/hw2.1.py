#!/usr/bin/env python

"""
	hw2.1.py -- count to '100' by 2's
	author: Danny Moncada
"""

counter = 0
while True:
    number = raw_input('please enter an integer: ')
    if number.isdigit():
		break
	print "sorry, '{}' is not a valid integer".format(number)
	print ""

number = int(number)
print "counting from 0 to 100 by {}'s".format(number)
print ""

while counter < 100:
	print counter
	counter = counter + number
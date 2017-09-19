#!/usr/bin/env python

"""
	hw2.2.py -- sum a sequence of integers
	author: Danny Moncada
"""

count = 0
varsum = 0

while True:
    var = raw_input('please enter an integer: ')
    if var.isdigit() and int(var) > 0:
        break
    print "sorry, '{}' is not a valid positive integer".format(var)

max_count = int(var)
		
while count < max_count:
    count = count + 1
    varsum = varsum + count

print 'sum from 1 to {} is {}'.format(var, varsum)
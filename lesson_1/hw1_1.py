#!/usr/bin/env python

"""
	hw1_1.py -- exponientation with tidy border
	author: Danny Moncada
"""

var_1 = raw_input("Please enter an integer:  ")
var_2 = raw_input("Please enter another integer:  ")

exponent = int(var_1) ** int(var_2)

length = len(str(exponent))

border = "=" * length

print border
print exponent
print border

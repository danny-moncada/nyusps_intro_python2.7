#!/usr/bin/env python

var = raw_input('how many times should I greet you? ')
if var.isdigit():
	count = 0
	while count < int(var):
		print 'Happy birthday to you!'
		count = count + 1
else:
	exit('error: please enter an integer')
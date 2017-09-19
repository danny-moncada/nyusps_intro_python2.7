#!/usr/bin/env python

while True:
	var = raw_input('please enter an integer: ')
	if var.isdigit():
		print 'THANKS FOR THE INTEGER'
		break
	else:
		print 'that was NOT an integer!'
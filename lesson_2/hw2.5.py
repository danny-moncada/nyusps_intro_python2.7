#!/usr/bin/env python

"""
	danny_moncada_2.5.py -- Number Guessor
	author: Danny Moncada
"""

max_number = 100
min_number = 0
halfway = (max_number + min_number) / 2

start = raw_input('Think of a number between 100 and 0, and I will try to guess it.  Hit [Enter] to start')

while True:

	user_input = raw_input('Is it {} (yes/no/quit)?  '.format(halfway))

	if user_input.startswith('y'):
		print 'I knew I could do it!'
		break

	elif user_input.startswith('n'):
		program_guess = raw_input('is it higher or lower than {}?  '.format(halfway))

		if program_guess.startswith('h'):
			min_number = halfway
			halfway = (max_number + min_number) / 2

		if program_guess.startswith('l'):
			max_number = halfway
			halfway = (max_number + min_number) / 2

	elif user_input.startswith('q'):
		exit()
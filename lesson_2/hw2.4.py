#!/usr/bin/env python

"""
	hw2.4.py -- Reverse Number Guessor
	author: Danny Moncada
"""

import random

number_to_guess = random.randint(1, 100)
count = 1

print "I am thinking of a number from 1 to 100.  Try to guess it and I'll give you hints about it."
print ""

while True:
	user_guess = raw_input('Your guess? (q to quit): ')
	
	if user_guess.isalpha():
		exit()

	if user_guess.isdigit():
		continue

guessed_number = int(user_guess)

while guessed_number != number_to_guess:

	if guessed_number > number_to_guess:
		count = count + 1
		break
		print "your guess is HIGHER than the number I'm thinking of."
		print ""
		
	elif guessed_number < number_to_guess:
		count = count + 1
		break
		print "your guess is LOWER than the number I'm thinking of."
		print ""
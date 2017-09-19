#!/usr/bin/env python

"""
    danny_moncada_2.6.py -- Find prime numbers
    Author: Danny Moncada
"""

print '* Prime Numbers *'

user_input = raw_input('Please enter max integer: ')
user_input = int(user_input)
prime_check = 2

while prime_check <= user_input:
    test_number = 2

    while test_number <= user_input:
        remainder = prime_check % test_number

        if test_number == prime_check:
            print '{} is prime.'.format(prime_check)
            break

        if remainder == 0:
            break
        test_number = test_number + 1

    prime_check = prime_check + 1
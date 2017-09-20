#!usr/bin/env python

import sys

try:
	firstint = int(sys.argv[1])
	secondint = int(sys.argv[2])

except IndexError:
	exit('Usage: {}').format(sys.argv[0])

print '{} + {} = {}'.format(firstint, secondint, firstint + secondint)


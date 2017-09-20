#!usr/bin/env python

import sys

try:
	firstint = int(sys.argv[1])
	secondint = int(sys.argv[2])

except (IndexError, ValueError):
	print 'Usage: {} {} {}'.format(sys.argv[0], '[int1]', '[int2]')
	exit()

print '{} + {} = {}'.format(firstint, secondint, firstint + secondint)


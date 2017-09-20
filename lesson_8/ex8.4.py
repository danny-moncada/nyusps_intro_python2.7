#!usr/bin/env python

import os
import sys

file = sys.argv[1]
in_dir = os.path.isfile(file)

if in_dir == True:
	print '{}: {} bytes'.format(file, os.path.getsize(file))
else:
	print 'error: {} not in directory'.format(file)
	exit()
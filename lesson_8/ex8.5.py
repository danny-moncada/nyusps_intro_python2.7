#!usr/bin/env python

import os
import sys

try:
	ldir = sys.argv[1]

	for item in os.listdir(ldir):
		full_item = os.path.join(ldir, item)
		if os.path.isfile(full_item):
			print '{} is a file'.format(item)
		elif os.path.isdir(full_item):
			print '{} is a dir'.format(item)
except IndexError:
	exit('you must provide a file path')
except OSError:
	exit('file path does not exist')
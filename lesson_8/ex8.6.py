#!usr/bin/env python

import os
import sys

user_input = raw_input('please enter a directory: ')

try:
	test_dir = user_input

	for file in os.listdir(test_dir):
		full_path = os.path.join(test_dir, file)
		size = os.path.getsize(full_path)
		
		if os.path.isfile(full_path):
			print '{} (file): {}'.format(file, size)
		elif os.path.isdir(full_path):
			print '{} (dir): {}'.format(file, size)

except IndexError:
	exit('you must provide a file path')
except OSError:
	exit('file path does not exist')
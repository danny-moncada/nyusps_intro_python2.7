#usr/bin/env python

file = open('../python_data/pyku.txt')

pyku = file.read()
master_list = pyku.split()

for word in master_list:
	print word
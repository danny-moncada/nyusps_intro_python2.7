#!/usr/bin/env python

pyku = '../python_data/pyku.txt'

for line in sorted(open(pyku).readlines(), key = lambda x: len(x.split())):
	print line.rstrip()


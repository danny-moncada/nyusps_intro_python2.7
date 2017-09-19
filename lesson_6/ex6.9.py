#!/usr/bin/env python

pyku = open('../python_data/pyku.txt').readlines()

def num_words(arg):
	num_words = len(arg.split())
	return num_words

sorted_pyku = sorted(pyku, key = num_words)

for line in sorted_pyku:
	print line.rstrip()

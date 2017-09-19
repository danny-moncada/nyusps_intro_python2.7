#!/usr/bin/env python

mydict = {}
mylist = ['Hey', 'there', 'I', 'am', 'amazing!']

for value in mylist:
	mydict[value] = len(value)

print mydict
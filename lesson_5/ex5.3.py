#!/usr/bin/env python

mydict = {}
mylist = ['Hey', 'there', 'I', 'am', 'amazing!']

for value in mylist:
	mydict[value] = len(value)

for key in mydict:
	print '"{}" has a length of {}'.format(key, mydict[key])

#print mydict	
#print '{} has a length of {}.'.format(mydict, len(value))
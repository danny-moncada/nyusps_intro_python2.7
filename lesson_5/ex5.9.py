#!/usr/bin/env python

mydict = {}

cities = ['Boston', 'Chicago', 'New York', 'Boston', 'Chicago', 'Boston']

for city in cities:
	if city not in mydict:
		mydict[city] = 0
	mydict[city] += 1
		

print mydict
print len(mydict)


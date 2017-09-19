#!/usr/bin/env python

mydict = {'c': 0.3, 'b': 7, 'a': 5}

sort_dict = sorted(mydict, key = mydict.get, reverse = True)

for key in sort_dict:
	print '{} => {}'.format(key, mydict[key])
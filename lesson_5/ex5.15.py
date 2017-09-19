#!/usr/bin/env python

mydict = {'c': 0.3, 'b': 7, 'a': 5}
valid_input = ['ascending', 'descending']

while True:
	direction = raw_input('please enter a direction: ')
	if direction not in valid_input:
		print 'please enter "{}" or "{}"'.format(valid_input[0], valid_input[1])
	elif direction == 'ascending':
		rev = False
		break
	elif direction == 'descending':
		rev = True
		break

sort_dict = sorted(mydict, key = mydict.get, reverse = rev)

for key in sort_dict:
	print '{} => {}'.format(key, mydict[key])
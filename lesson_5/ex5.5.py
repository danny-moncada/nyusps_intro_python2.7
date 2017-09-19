#!/usr/bin/env python

mydict = {}
mylist = ['Hey', 'there', 'I', 'am', 'amazing!']

for value in mylist:
	mydict[value] = len(value)

user_input = raw_input('please enter a word: ')

if user_input in mydict:
	print 'the word "{}" has a len of {}'.format(user_input, mydict[user_input])
else:
	print 'the word "{}" does not exist in the dictionary'.format(user_input)
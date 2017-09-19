#usr/bin/env python

new_set = set()
file = open('../python_data/pyku.txt')

pyku = file.read()
master_list = pyku.split()

for word in master_list:
	new_word = word.rstrip(',.!').lower()
	new_set.add(new_word)

print new_set
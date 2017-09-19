#usr/bin/env python

text = "we're certainly out of gouda but Python is great."
text_split = text.split()

new_set = set()
file = open('../python_data/pyku.txt')

pyku = file.read()
master_list = pyku.split()

for word in master_list:
	new_word = word.rstrip(',.!').lower()
	new_set.add(new_word)

for item in text_split:
	if item not in new_set:
		print item
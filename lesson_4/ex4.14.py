#usr/bin/env python

new_set = set()
sentence = "I could; I wouldn't.  I might?  Might I!"

split_sentence = sentence.split()

for word in split_sentence:
	new_word = word.rstrip('.!?;')
	lower = new_word.lower()
	new_set.add(lower)

print new_set
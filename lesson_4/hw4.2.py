#usr/bin/env python

"""
	hw4.2.py -- Spell Checker
	author: Danny
"""

spell_checker = set()

file = open('../../python_data/words.txt')
all_words = file.read()
master_list = all_words.split()

for word in master_list:
    new_word = word.rstrip(',.!').lower()
    spell_checker.add(new_word)

print '{} words in spelling words'.format(len(spell_checker))
print

count = 0

text_to_check = open('../../python_data/sawyer.txt')
sawyer = text_to_check.readlines()

for line in sawyer:
    words = line.split()
    count = count + 1

    for word in words:
        lower_case = word.rstrip('.,;:?!').lower()
        if lower_case not in spell_checker:
            print 'there is a misspelled word on line {}: {}'.format(count, lower_case)
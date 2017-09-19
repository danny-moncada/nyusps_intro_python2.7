#/usr/bin/env python

file = open('../python_data/pyku.txt')

file_text = file.read()
print file_text.count('spam')
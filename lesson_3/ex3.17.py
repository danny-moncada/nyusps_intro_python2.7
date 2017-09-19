#/usr/bin/env python

file = open('../python_data/pyku.txt')

file_text = file.read()
split_lines = file_text.split()

print type(split_lines)
print split_lines[0]
print split_lines[-1]
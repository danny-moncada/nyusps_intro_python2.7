#/usr/bin/env python

file = open('../python_data/pyku.txt')

file_text = file.read()
split_lines = file_text.splitlines()

first_line = split_lines[0]
last_line = split_lines[-1]

print type(split_lines)
print first_line
print last_line
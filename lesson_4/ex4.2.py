#usr/bin/env python

pw = open('../python_data/passwords.txt')

lines = pw.readlines()
first_three = lines[0:3]
print first_three
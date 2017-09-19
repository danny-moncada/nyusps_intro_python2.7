#/usr/bin/env python

ff_abbreviated = open('../python_data/FF_abbreviated.txt')

for line in ff_abbreviated:
    split_line = line.split()
    print split_line
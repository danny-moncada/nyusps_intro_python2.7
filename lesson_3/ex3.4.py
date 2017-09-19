#!/usr/bin/env python

year_to_filter = '1928'
fh = open('../python_data/FF_abbreviated.txt')

for line in fh:
    linesplit = line.split()
    fulldate = linesplit[0]
    year = fulldate[0:4]
        if year == year_to_filter:
            print linesplit
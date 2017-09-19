#/usr/bin/env python

ff_abbreviated = open('../python_data/FF_abbreviated.txt')
year_filter = '1928'

for line in ff_abbreviated:
    split_line = line.split()
    full_date = split_line[0]
    year_of_date = full_date[0:4]
    print year_of_date
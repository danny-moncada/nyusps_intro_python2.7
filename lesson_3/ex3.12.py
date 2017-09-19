#/usr/bin/env python

ff_abbreviated = open('../python_data/FF_abbreviated.txt')
year_filter = '1928'
count = 0

for line in ff_abbreviated:
    if line.startswith('1928'):
        count = count + 1
        full_date = line.split()[1]
        date_as_float = float(full_date) * 2
        print count, full_date, date_as_float
'''
    split_line = line.split()
    full_date = split_line[0]
    year_of_date = full_date[0:4]
    if year_of_date == year_filter:
        print year_of_date'''
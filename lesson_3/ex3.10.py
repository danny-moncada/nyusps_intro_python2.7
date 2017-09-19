#/usr/bin/env python

ff_abbreviated = open('../python_data/FF_abbreviated.txt')
year_filter = '1928'

for line in ff_abbreviated:
    if line.startswith('1928'):
        full_date = line.split()[1]
        print full_date
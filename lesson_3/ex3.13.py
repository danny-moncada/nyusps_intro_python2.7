#/usr/bin/env python

ff_abbreviated = open('../python_data/FF_abbreviated.txt')
year_filter = '1928'
floatsum = 0

for line in ff_abbreviated:
    if line.startswith('1928'):
        float_value = float(line.split()[1])
        floatsum = floatsum + float_value

print floatsum
'''
    split_line = line.split()
    full_date = split_line[0]
    year_of_date = full_date[0:4]
    if year_of_date == year_filter:
        print year_of_date'''
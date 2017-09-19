#!usr/bin/env python

year_filter = '1928'
count = 0

filename = open('../python_data/FF_abbreviated.txt')

for line in filename:
    data = line.split()
    fulldate = data[0]
    year = fulldate[0:4]

    if year == year_filter:
        count = count + 1
        print line
        
print count
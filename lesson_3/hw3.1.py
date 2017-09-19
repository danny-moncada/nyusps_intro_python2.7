#/usr/bin/env python

"""
	hw3.1.py -- Calculate average Mkt-RF value for a given year
	author: Danny Moncada
"""

count = 0
total_sum = 0

while True:
    year_to_filter = raw_input('please enter a 4-digit year: ')
    if year_to_filter.isdigit() and len(year_to_filter) == 4:
        break
    print 'sorry, that was bad input'

file = open('../../python_data/Fama-French_data.txt')

for line in file:
    if line.startswith(year_to_filter):
        count = count + 1
        split_lines = line.split()
        data_to_calculate = float(split_lines[1])
        
        total_sum = data_to_calculate + total_sum
        
average = total_sum / count
print 'count {}, sum {}, avg {}'.format(count, total_sum, average)
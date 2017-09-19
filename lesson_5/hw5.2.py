#!/usr/bin/env python

"""
    hw5.2.py -- create a dictonary that sums all Mkt-RF values per year
    author: Danny Moncada
"""

mydict = {}

farma_french = open('../../python_data/F-F_Research_Data_Factors_daily.txt').readlines()[5:-2]

for line in farma_french:
    line = line.split()
    year = line[0][0:4]
    mkt_rf = float(line[1])
    if year not in mydict:
        mydict[year] = 0.0
    mydict[year] += mkt_rf

max_value = len(mydict)

while True:
    results = raw_input('please enter number of results desired: ')
    direction = raw_input('select "highest" or "lowest" results: ')

    if results.isalpha():       
        print 'number results must be all digits'
        print
        continue
    if direction not in ['highest', 'lowest']:
        print 'top or bottom results must be "highest" or "lowest"'
        continue

    results = int(results)

    if results > max_value:
        print 'number results "{}" is greater than max "{}"'.format(results, max_value)
        continue
    break

if direction == 'highest':
    rev = True
else:
    rev = False

for key in sorted(mydict, key = mydict.get, reverse = rev)[0:results]:
    print '{}: {}'.format(key, mydict[key])

exit()
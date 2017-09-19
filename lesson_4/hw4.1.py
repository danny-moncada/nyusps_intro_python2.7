#usr/bin/env python

"""
    hw4.1.py -- Calculating average Mkt-RF
    author: Danny Moncada
"""

values = []
valid_actions = ['Mkt-RF', 'SMB', 'HML', 'RF']

while True:
    user_input = raw_input('please enter a 4-digit year: ')
    if user_input.isalpha() or len(user_input) != 4:
        print 'ERROR: 1st arg must be 4-digit year'
        continue

    print 'available factors: {}'.format(valid_actions)

    factor = raw_input('please enter a factor: ')
    if factor not in valid_actions:
        print 'Sorry, that factor does not exist.'
        continue
    break

research_file = open('../../python_data/F-F_Research_Data_Factors_daily.txt')
lines = research_file.readlines()[5:-2]

for line in lines:
    if user_input == line[0:4]:
        data_points = line.split()
        if factor == valid_actions[0]:
            mkt_rf = float(data_points[1])
            values.append(mkt_rf)
        elif factor == valid_actions[1]:
            smb = float(data_points[2])
            values.append(smb)
        elif factor == valid_actions[2]:
            hml = float(data_points[3])
            values.append(hml)
        else:
            rf = float(data_points[4])
            values.append(rf)

sorted_values = sorted(values)
count = len(values)

if count == 0:
    print 'no values found'
    exit()

highest = max(values)
lowest = min(values)
average = float(sum(values)) / count

if count % 2 != 0:
    median = sorted_values[count / 2]
else:
    median = (sorted_values[count / 2] + sorted_values[(count / 2) - 1]) / 2

print '{} ({}): {} values, max {}, min {}, median {}, avg {}'.format(user_input, factor, count, highest, lowest, median, average)
exit()
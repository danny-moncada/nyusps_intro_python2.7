#usr/bin/env python

values = [6, 1, 3, 2, 4, 5]
ordered_values = sorted(values)

length = len(ordered_values)

index_one = (length / 2) - 1
index_two = length / 2

median = (ordered_values[index_one] + ordered_values[index_two]) / float(2)

print median
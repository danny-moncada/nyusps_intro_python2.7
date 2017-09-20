#!/usr/bin/env python

"""
    hw8.1.py -- directory grep search text in file 
    author: Danny Moncada
"""

import os
import sys

try:
    path = sys.argv[1]
    text_search = sys.argv[2]

    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        text = open(filepath).readlines()
        count = 0

        for line in text:
            count += 1
            if text_search in line:
                print '{} ({}): {}'.format(file, count, line)

except IndexError:
    exit('error: please provide TWO arguments [filepath] [string]')
except (OSError, IOError):
    exit('error: that file path is not a valid directory')
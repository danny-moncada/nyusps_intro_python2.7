#!/usr/bin/env python

"""
    hw8.2.py -- Watched Directory
    author: Danny Moncada
"""

import os
import sys
import time

try: 
    filepath = sys.argv[1]
    oldset = set(os.listdir(filepath))

except IndexError:
    exit('error: please provide [filepath] as argument')
except OSError:
    exit('error: this is not a valid file path')

while True:
    time.sleep(5)
    newset = set(os.listdir(filepath))
    added = newset.difference(oldset)
    removed = oldset.difference(newset)
    for item in added:
        print '{} added'.format(item)
    for item in removed:
        print '{} removed'.format(item)
    oldset = newset
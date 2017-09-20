#!/usr/bin/env python

"""
    hw_8.3.py -- largest files using os.walk
    author: Danny Moncada
"""

import os
import sys

try:
    user_dir = sys.argv[1]
    num = int(sys.argv[2])
    test = os.listdir(user_dir)
except OSError:
    exit('error: you must enter a valid path')
except IndexError:
    exit('error: you must enter two args [filepath] [number]')
except ValueError:
    exit('error: the second arg must be a valid int')

my_dict = {}

for root, dirs, files in os.walk(user_dir):
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)
        if file_path not in my_dict:
            my_dict[file_path] = 0
        my_dict[file_path] = file_size

for file_path in sorted(my_dict, key=my_dict.get, reverse = True)[0:num]:
    print my_dict[file_path], file_path
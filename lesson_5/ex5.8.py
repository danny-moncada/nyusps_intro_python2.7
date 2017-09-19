#!/usr/bin/env python

personal_info = "595-33-9193:68:Columbus, OH"

split_info = personal_info.split(':')

print 'SS#: {} \nAge: {} \nResidence: {}'.format(split_info[0], split_info[1], split_info[2])
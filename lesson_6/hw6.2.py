#!/usr/bin/env python

"""
	hw6.2.py -- Read a config from multidimensional structure and print out in readable format
	author: Danny Moncada
"""

from config import conf

for entry in conf:
    print '{}:  {}'.format(entry.keys()[0], entry['domain'])
    
    for host_port in entry['database']:
        print '{}:  {}'.format(host_port, entry['database'][host_port])
    
    print '{}: '.format(entry.keys()[1])
    for plugins in entry['plugins']:
        print '   {}'.format(plugins)
    print
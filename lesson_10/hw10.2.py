#!usr/bin/env python

"""
	hw10.2.py -- list of a maximum size
	author: Danny Moncada
"""

class MaxSizeList(object):
    def __init__(self, val):
        self.emptylist = []
        self.maxsize = int(val)
    def push(self, str):
        self.emptylist.append(str)
        if len(self.emptylist) > self.maxsize:
            self.emptylist.pop(0)
    def get_list(self):
        return self.emptylist

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hi")
a.push("ho")
a.push("let's")
a.push("go")

b.push("hey")
b.push("ho")
b.push("let's")
b.push("go")

print a.get_list()
print b.get_list()

exit()
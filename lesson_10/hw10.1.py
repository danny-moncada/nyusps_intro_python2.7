#!usr/bin/env python

"""
	hw10.1.py -- create a class: Sqaure
	author: Danny Moncada
"""

class Square(object):
    def __init__(self):
        self.value = 2
    def squareme(self):
        self.value = self.value ** 2
    def getme(self):
        return self.value

n1 = Square()
n2 = Square()
n3 = Square()

n1.squareme()
val1 = n1.getme()
print val1
    
n2.squareme()
n2.squareme()
val2 = n2.getme()
print val2
print n1.getme()

n3.squareme()
n3.squareme()
n3.squareme()
n3.squareme()
n3.squareme()
val3 = n3.getme()
print val3

print n1.getme()
print n2.getme()
print n3.getme()
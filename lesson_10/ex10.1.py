#!usr/bin/env python

class ThisClass(object):
	def report(self):
		print id(self)

a = ThisClass()
b = ThisClass()
c = ThisClass()

a.report()
b.report()
c.report()
print

print id(a)
print id(b)
print id(c)
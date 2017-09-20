#!usr/bin/env python

class Sum(object):
	def add(self, val):
		if not hasattr(self, 'x'):
			self.x = 0
		self.x = self.x + val

myobj = Sum()
myobj.add(5)
myobj.add(20)

print myobj.x

exit()
from datetime import date, timedelta

dt = date(1926, 12, 30)
td = timedelta(days = 3)

dt = dt + timedelta(days = 3)

print dt

dt2 = date.today()
dt2 = dt2 + timedelta(days = 1)

print dt2

print type(dt)
print type(td)
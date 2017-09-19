#!/usr/bin/env python

sites_pages = {
	'example.com':	[
					    'index.html',
					    'about_us.html',
					    'contact_us.html'
					    ],
	'something.com': [
						'index2.html',
						'prize.html',
						'puppies.html',
						],
	'whateva.com':	[
						'main.html',
						'getting.html',
						'setting.html',
						],
}

for mylist in sites_pages:
	print mylist
	print '  ', sites_pages[mylist][0]
	print '  ', sites_pages[mylist][1]
	print '  ', sites_pages[mylist][2]
	print